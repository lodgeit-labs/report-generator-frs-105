"""Load-bearing byte-fidelity test.

Per CLAWDOG/141 Gate 3 precedent (lodgeit-labs/clawdog .github/workflows/test.yml):
every vendored canon file MUST hash to the sha256 declared in
``bridge_canon/MANIFEST.json``. The MANIFEST was computed at vendor time
against the byte-identical Brain canon at the declared source commit.

Two failure modes this gate catches:
  (a) Kit-side mutation of a vendored canon file (Standing Rule #7 — Kit is
      Egress Interface, the bridge_canon/ projection is read-only).
  (b) Brain canon was re-vendored but the MANIFEST sha256 was not refreshed.
      In that case re-run ``scripts/revendor_from_brain.py``.

Additionally, for the lookup artefact specifically (which carries a Kit-side
wrapper-frontmatter declaring ``body_sha256`` of the wrapped Brain body),
this test recomputes the body_sha256 and asserts equality. Mirrors exactly
the docs/INTEGRATOR_README.md pattern in lodgeit-labs/clawdog.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "bridge_canon" / "MANIFEST.json"


@pytest.fixture(scope="module")
def manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text())


def test_manifest_exists(manifest):
    assert manifest["source_brain_canon_commit"] == \
        "2fc7451a3068c69d726a2159cced4254fad2187c"
    assert len(manifest["files"]) >= 50  # 40 canon + 4 schema + 12 sidecars + readme + lookup
    assert manifest["kit"] == "lodgeit-labs/report-generator-frs-105"


def test_every_vendored_file_matches_declared_sha256(manifest):
    fails = []
    for entry in manifest["files"]:
        p = ROOT / entry["path"]
        if not p.is_file():
            fails.append((entry["path"], "missing"))
            continue
        actual = hashlib.sha256(p.read_bytes()).hexdigest()
        if actual != entry["sha256"]:
            fails.append((entry["path"], f"declared={entry['sha256']} actual={actual}"))
    if fails:
        msg = "\n".join(f"  {p}: {d}" for p, d in fails)
        raise AssertionError(
            f"❌ {len(fails)} vendored canon file(s) drifted from MANIFEST.json:\n{msg}\n"
            "Either revert the Kit-side edit, or re-run scripts/revendor_from_brain.py."
        )


_WRAPPER_BODY_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
_DECLARED_RE = re.compile(r'^\s*body_sha256:\s*"([0-9a-f]{64})"', re.MULTILINE)


def test_lookup_artefact_wrapper_body_sha256_matches_body_bytes():
    """The Kit's wrapper-frontmatter declares body_sha256 of the wrapped Brain body."""
    path = ROOT / "bridge_canon" / "frs_105_micro" / "frc_v2026" / "_path_a_v1_lookup_2026-05-15.md"
    content = path.read_text(encoding="utf-8")
    m = _DECLARED_RE.search(content)
    assert m, "lookup artefact missing body_sha256 in wrapper frontmatter"
    declared = m.group(1)
    body_match = _WRAPPER_BODY_RE.match(content)
    assert body_match, "lookup artefact missing wrapper frontmatter delimiters"
    body = content[body_match.end():]
    actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
    assert actual == declared, (
        f"DRIFT: declared body_sha256={declared} actual={actual} "
        f"(body length: {len(body.encode('utf-8'))} bytes)"
    )
