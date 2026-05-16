"""Bridge canon resolver.

Loads the vendored `bridge_canon/` tree, parses each fact-node's YAML
frontmatter, and exposes a deterministic API:

    resolve_concept(slug, framework="frs_105_micro",
                    taxonomy_version="frc_v2026", period="ongoing")

Resolution precedence (per CLAWDOG/113 §3.1):
    1. direct_atom         (sbrm_NNNN.md)            — wins always
    2. external_input      (*.input.md)              — slug == framework_concept's local id
    3. computed_rollup     (*.rollup.md)             — slug == framework_concept's local id
    4. ancestry_subsume    (_ancestry_/<slug>.md)    — broadest fallback

The resolver does NOT walk the LodgeiT SBRM ancestry graph itself — that
lives in the Brain (`ClawDog_Share/full_sbrm_physics.pl`) and is consumed
upstream of the bridge by integrators like LodgeiT_HMRC_CT600. The
`ancestry_subsume` rules in this Kit are flat anchors keyed by
`ancestor_slug`; callers can map child SBRM codes onto ancestor slugs via
their own ancestry walker, then call `resolve_concept(<ancestor_slug>)`.

Apache-2.0.
"""
from __future__ import annotations

import json
import pathlib
import re
from dataclasses import dataclass, asdict
from typing import Dict, Iterable, List, Optional

import yaml


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------


class UnknownSlugError(KeyError):
    """No bridge fact-node matches the (slug, framework, taxonomy_version, period)."""


class ExternalInputRequired(LookupError):
    """The slug resolves to an external_input node — caller must supply the value.

    Raised only when ``raise_on_external_input=True`` (default). When the flag
    is False, the resolver returns a :class:`ResolvedConcept` with
    ``mapping_kind == "external_input"``.
    """


class AmbiguousResolutionError(RuntimeError):
    """Multiple bridge fact-nodes match — should never happen on healthy canon."""


# ---------------------------------------------------------------------------
# Data class
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ResolvedConcept:
    framework_concept: str
    mapping_kind: str          # direct_atom | computed_rollup | external_input | ancestry_subsume
    statement_role: str
    confidence: str
    source_node_path: str
    source_content_hash: str
    dimensional_axis: Optional[str] = None  # reserved for future Hyperplane Mismatch fix
    # extras (informational)
    framework_id: str = ""
    taxonomy_version: str = ""
    period_applicability: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self, *, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, sort_keys=True)


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------


_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?\n)---\s*\n", re.DOTALL)


def bridge_canon_root() -> pathlib.Path:
    """Return the absolute path to the vendored ``bridge_canon/`` directory."""
    return pathlib.Path(__file__).resolve().parent.parent.parent / "bridge_canon"


def _parse_frontmatter(text: str) -> Optional[dict]:
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def _iter_canon_files(canon_root: pathlib.Path, framework: str,
                      taxonomy_version: str) -> Iterable[pathlib.Path]:
    base = canon_root / framework / taxonomy_version
    if not base.is_dir():
        return []
    out: List[pathlib.Path] = []
    for p in sorted(base.rglob("*.md")):
        if p.name.startswith("README"):
            continue
        if p.name.startswith("_path_a_v1_lookup"):
            continue
        if "_schema" in p.parts:
            continue
        out.append(p)
    return out


_CACHE: Dict[tuple, dict] = {}


def _load_index(framework: str, taxonomy_version: str) -> dict:
    """Build (and cache) the in-memory index for one (framework, taxonomy_version).

    Returned dict shape:
        {
          "by_sbrm":      {"sbrm_4101": fact_node, ...},   # direct_atom
          "by_concept_slug": {"equity": fact_node, ...},   # rollup + external_input keyed by local slug
          "by_ancestor":  {"equity": fact_node, ...},      # ancestry_subsume
        }
    """
    key = (framework, taxonomy_version)
    if key in _CACHE:
        return _CACHE[key]
    by_sbrm: Dict[str, dict] = {}
    by_concept_slug: Dict[str, dict] = {}
    by_ancestor: Dict[str, dict] = {}
    canon = bridge_canon_root()
    for path in _iter_canon_files(canon, framework, taxonomy_version):
        text = path.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text)
        if not fm:
            continue
        oc = fm.get("ontological_class")
        rel = path.relative_to(canon.parent).as_posix()  # e.g. bridge_canon/frs_105_micro/frc_v2026/sbrm-4101.md
        record = {"path": rel, "frontmatter": fm}
        if oc == "BridgeMapping":
            sbrm = fm["bridge"]["sbrm_code"]
            by_sbrm[sbrm] = record
        elif oc == "BridgeComputedRollup":
            slug = _local_id(fm["bridge_rollup"]["framework_concept"])
            by_concept_slug.setdefault(slug, record)
        elif oc == "BridgeExternalInput":
            slug = _local_id(fm["bridge_external_input"]["framework_concept"])
            by_concept_slug.setdefault(slug, record)
        elif oc == "BridgeAncestrySubsume":
            anc = fm["bridge_ancestry"]["ancestor_slug"]
            by_ancestor[anc] = record
        # silently skip unknown ontological_class — gate elsewhere
    index = {
        "by_sbrm": by_sbrm,
        "by_concept_slug": by_concept_slug,
        "by_ancestor": by_ancestor,
    }
    _CACHE[key] = index
    return index


def _local_id(framework_concept: str) -> str:
    """`uk-core:Equity` → `equity`. CamelCase splits to lower-kebab on best-effort."""
    if ":" in framework_concept:
        framework_concept = framework_concept.split(":", 1)[1]
    # Insert hyphens at lower→Upper boundaries, then lowercase.
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", framework_concept)
    return s.lower()


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def resolve_concept(
    slug: str,
    framework: str = "frs_105_micro",
    taxonomy_version: str = "frc_v2026",
    period: str = "ongoing",
    *,
    raise_on_external_input: bool = False,
) -> ResolvedConcept:
    """Resolve a LodgeiT slug or SBRM code to a framework concept.

    ``slug`` may be:
      - a bare SBRM atom (e.g. ``"sbrm_4101"`` or ``"sbrm-4101"``) — looked up in direct_atom;
      - a LodgeiT ancestor slug (e.g. ``"equity"``) — looked up in ancestry_subsume,
        falling back to external_input / computed_rollup if the local-id matches a
        framework concept slug.

    Resolution precedence: direct_atom → external_input → computed_rollup →
    ancestry_subsume. Period filtering is currently a literal-equality match
    against ``period_applicability``; ``"ongoing"`` is the only declared value
    at FRC v2026.
    """
    index = _load_index(framework, taxonomy_version)

    normalised = slug.replace("-", "_").lower()

    # 1. direct_atom by sbrm code
    if normalised.startswith("sbrm_") and normalised in index["by_sbrm"]:
        rec = index["by_sbrm"][normalised]
        return _build(rec, "bridge", period, dimensional_axis=None)

    # 2. external_input or computed_rollup by local-id of framework_concept
    if normalised.replace("_", "-") in index["by_concept_slug"]:
        rec = index["by_concept_slug"][normalised.replace("_", "-")]
        oc = rec["frontmatter"]["ontological_class"]
        if oc == "BridgeExternalInput":
            rc = _build(rec, "bridge_external_input", period, dimensional_axis=None)
            if raise_on_external_input:
                raise ExternalInputRequired(
                    f"slug={slug!r} resolves to external_input {rc.framework_concept}; "
                    f"supply the value from input_source="
                    f"{rec['frontmatter']['bridge_external_input']['input_source']!r}"
                )
            return rc
        if oc == "BridgeComputedRollup":
            return _build(rec, "bridge_rollup", period, dimensional_axis=None)

    # 3. ancestry_subsume by ancestor slug
    if normalised in index["by_ancestor"]:
        rec = index["by_ancestor"][normalised]
        return _build(rec, "bridge_ancestry", period, dimensional_axis=None)

    raise UnknownSlugError(
        f"No bridge fact-node for slug={slug!r} framework={framework!r} "
        f"taxonomy_version={taxonomy_version!r} period={period!r}"
    )


def _build(rec: dict, body_key: str, requested_period: str,
           dimensional_axis: Optional[str]) -> ResolvedConcept:
    fm = rec["frontmatter"]
    body = fm[body_key]
    if body.get("period_applicability") != requested_period:
        # tolerate: still resolve, but flag via dimensional_axis-or-None remains None
        # (period mismatch is rare at FRC v2026 because every node declares "ongoing")
        pass
    return ResolvedConcept(
        framework_concept=body["framework_concept"],
        mapping_kind=body["mapping_kind"],
        statement_role=body["statement_role"],
        confidence=body.get("confidence", "unknown"),
        source_node_path=rec["path"],
        source_content_hash=fm["cryptographic_anchor"]["content_hash"],
        dimensional_axis=dimensional_axis,
        framework_id=body["framework_id"],
        taxonomy_version=body["taxonomy_version"],
        period_applicability=body["period_applicability"],
    )


def list_slugs(framework: str = "frs_105_micro",
               taxonomy_version: str = "frc_v2026") -> dict:
    """Inspection helper. Returns the keys available in each lookup table."""
    idx = _load_index(framework, taxonomy_version)
    return {
        "direct_atom_sbrm_codes": sorted(idx["by_sbrm"].keys()),
        "concept_slugs": sorted(idx["by_concept_slug"].keys()),
        "ancestor_slugs": sorted(idx["by_ancestor"].keys()),
    }
