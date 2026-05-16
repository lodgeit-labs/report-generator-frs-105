# report-generator-frs-105

**Egress-Interface Kit projecting [`clawdog-brain`](https://github.com/futureWA/clawdog-brain) Phase 4a.3 bridge canon for FRS 105 Micro × FRC v2026 statutory accounts.** Vendors 40 bridge fact-nodes (12 `direct_atom` + 9 `computed_rollup` + 8 `external_input` + 11 `ancestry_subsume`), the Path A v1 lookup artefact, the four bridge JSON Schemas, and 12 byte-truth XSD sidecars. Ships a deterministic Python resolver library + CLI. Apache-2.0.

## What this is

A **deterministic** library that resolves LodgeiT SBRM slugs and codes (e.g. `sbrm_4101`, `equity`, `share_capital`) to FRC v2026 framework concepts (e.g. `uk-core:TurnoverRevenue`, `uk-core:Equity`). The mapping table is vendored byte-for-byte from `clawdog-brain` at a declared source commit, and a CI byte-check gate fails loudly if any vendored file drifts.

This is **Layer 3** in the [CLAWDOG/113](https://github.com/futureWA/clawdog-brain) bridge architecture — pure projection. Layer 5 (iXBRL template rendering) lives in [`lodgeit-labs/LodgeiT_HMRC_CT600`](https://github.com/lodgeit-labs/LodgeiT_HMRC_CT600), which consumes this Kit via the `USE_BRIDGE_CANON=1` feature flag (Phase 4a.4 Subagent B scope).

## Quickstart

```bash
pip install report-generator-frs-105
```

```python
from report_generator_frs_105 import resolve_concept

rc = resolve_concept("sbrm_4101")
print(rc.framework_concept)   # 'uk-core:TurnoverRevenue'
print(rc.mapping_kind)        # 'direct_atom'
print(rc.statement_role)      # 'PL_REVENUE'
print(rc.source_content_hash) # '601debb568492e1ea838a7047820b0cbc21f5cb1cebb003f024e3e7afdff43a2'
```

```bash
$ python -m report_generator_frs_105 resolve equity
{
  "confidence": "high",
  "dimensional_axis": null,
  "framework_concept": "uk-core:Equity",
  "framework_id": "frs_105_micro",
  ...
  "mapping_kind": "computed_rollup",
  ...
}

$ python -m report_generator_frs_105 list
$ python -m report_generator_frs_105 provenance
```

## What this Kit provides / does NOT provide

Per [Lesson #37 (production boundary discipline)](https://github.com/futureWA/clawdog-brain).

**Provides:**
- Deterministic slug → FRC v2026 framework concept resolution for the 40 mapped slugs at FRS 105 Micro × `period_applicability="ongoing"`.
- Resolution across all four `mapping_kind`s: `direct_atom`, `computed_rollup`, `external_input`, `ancestry_subsume`.
- The vendored bridge canon (40 fact-node files + lookup artefact + 4 JSON Schemas + 12 XSD sidecars) as a read-only on-disk projection of `clawdog-brain`.
- A CI gate that catches drift between the vendored bytes and the declared `bridge_canon/MANIFEST.json`.

**Does NOT provide:**
- iXBRL template rendering (Layer 5 — that's `LodgeiT_HMRC_CT600`).
- FRS 102 / FRS 102 1A / IFRS frameworks (Phase 4b scope, not yet promoted to bridge canon).
- AU frameworks (`au_sbr_gp`, `au_aasb_ifrs`) — schemas declare the enums but no fact-nodes shipped.
- The Fano classifier (Layer 2 — that's `clawdog-ml-engine`).
- LodgeiT SBRM ancestry walking. `ancestry_subsume` fact-nodes are keyed by the ancestor slug; callers must reduce a child SBRM code to its ancestor slug themselves (via `ClawDog_Share/full_sbrm_physics.pl` or equivalent) before calling `resolve_concept(<ancestor_slug>)`.

## ⚠ Known structural-semantic limitations (load-bearing)

Four LodgeiT slugs **do not have a clean monetary-aggregate anchor** in the FRC v2026 taxonomy. Integrators must handle these explicitly. See [Open Threads #55–#58](https://github.com/futureWA/clawdog-brain) in `clawdog-brain` MEMORY.md, and the §Structural Finding block in [`bridge_canon/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md`](bridge_canon/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md).

| Slug | Thread | Issue |
|---|---|---|
| `investment_revenue` | #55 | No single FRC v2026 monetary aggregate — must be routed via narrower `direct_atom` concepts (dividend / interest / other-investment income). |
| `grants` | #56 | IAS 20 conditional-recognition semantics are calculator-shaped, not bridge-shaped. The bridge cannot encode the conditional; calculators emit the recognised journal. |
| `reserves` | #57 | FRC 2026 reorganised equity components into **dimensional decomposition** of `core:Equity`. No `Reserves` named element exists. |
| `non_current_liabilities` | #58 | `core:Creditors` umbrella element; current/non-current split lives on the `MaturitiesOrExpirationPeriodsDimension` **dimensional axis**, NOT as a separate named element. |

**Common root cause:** FRC v2026 reorganised statutory aggregates from named monetary elements into dimensional-axis decomposition of umbrella elements. This Kit's `ResolvedConcept.dimensional_axis` field is reserved for the future structural fix — today it is always `None`.

**Implication for integrators:** an Arelle-acceptable iXBRL filing using these slugs may still be **statutory-semantic-incomplete** in the dimensional-context sense. Phase 4a.6 closure requires a binding final human-eye review before the bridge canon is declared production-ready for the full FRS 105 hyperplane.

## ⚠️ Cautionary case study: internal byte-identity is not external regulator-shape correctness (Phase 4a.4 forensic record, corrected 2026-05-16)

> **Correction notice (2026-05-16):** an earlier version of this section (published in v0.1.1, README from 2026-05-16 03:20–09:41 UTC) framed the Phase 4a.4 A/B byte-identity harness as having *caught a real namespace defect in v1 production templates* — specifically claiming `uk-core:DateAuthorisationFinancialStatementsForIssue` was the v1 bug and `uk-bus:` was the bridge canon's correct anchor. **That claim was inverted against the wire.** A wire-anchored audit on 2026-05-16 of the FRC v2026 taxonomy XSDs proved the concept is declared exactly once, at `FRC-2026-Taxonomy-v1.0.0/fr/2026-01-01/core/frc-core-2026-01-01.xsd:2091`, in the `uk-core:` namespace. The v1 template was originally correct; the Phase 4a.2 `external_input` bridge-canon node was authored with the wrong namespace at birth (origin fault: `mut-2026-05-13-phase-4a-2`); Phase 4a.4 propagated the inverted canon into the v1 template via a `resolve()` call. Both A/B paths in v0.1.1 emit the wrong namespace.

### What actually happened

At Phase 4a.4 integration with `lodgeit-labs/LodgeiT_HMRC_CT600`, the A/B byte-identical iXBRL regression harness *did* succeed at what it was designed to do: prove that the `USE_BRIDGE_CANON=0` (legacy hard-coded fallback) and `USE_BRIDGE_CANON=1` (bridge-canon lookup) paths produce byte-identical iXBRL output. That **internal agreement** was real and remains true in v0.1.1.

What the harness *did not* do — and was never designed to do — is anchor either path against the FRC v2026 schema itself. The harness asks *"do our two paths agree?"*, not *"do our two paths agree with the regulator?"*. When the bridge canon ships an atom that is wrong at birth, internal agreement becomes a coherence-trap: both paths agree on the wrong answer, and the harness reports green.

### Wire truth (FRC v2026 schema, 2026-05-16 audit)

```
FRC-2026-Taxonomy-v1.0.0/fr/2026-01-01/core/frc-core-2026-01-01.xsd:2091:
  <element abstract="false"
           id="core_DateAuthorisationFinancialStatementsForIssue"
           name="DateAuthorisationFinancialStatementsForIssue"
           ...
           xbrli:periodType="instant"/>
```

XSD `targetNamespace`: `http://xbrl.frc.org.uk/fr/2026-01-01/core` — i.e. `uk-core:`. The element is **not** declared in `bus-2026-01-01.xsd`. A full 40-node sweep against the FRC v2026 XSDs confirmed only this one node (F1) was inverted; the other 39 `framework_concept:` declarations in the v0.1.1 vendored bundle are correct against the wire.

### State of v0.1.1 (this release)

- The vendored bridge canon in `bridge_canon/frs_105_micro/frc_v2026/date-authorisation-financial-statements-for-issue.input.md` carries `framework_concept: "uk-bus:DateAuthorisationFinancialStatementsForIssue"`. This is wrong against FRC v2026.
- The vendor MANIFEST sha256 + Brain content_hash (`3dfcdd2c…`) are internally consistent but anchor a defective atom.
- All other 39 vendored atoms are correct against the FRC v2026 wire.
- **Recommendation for integrators:** if your filing populates `DateAuthorisationFinancialStatementsForIssue` (it is the boilerplate "date directors authorised the accounts for issue" element, present on most FRS 105 micro filings), **hold off pinning v0.1.1 for that specific concept** until v0.1.2 ships with the corrected bridge canon. Other 39 mappings are safe to consume.

### State of `clawdog-brain` (post-correction)

The Brain bridge-canon F1 node was corrected on 2026-05-16 under `mut-2026-05-16-mc14-factual-correction`:

- `framework_concept`: `uk-bus:…` → `uk-core:DateAuthorisationFinancialStatementsForIssue`
- `previous_content_hash`: `3dfcdd2cc32e33feddff074450f704ed5863cc61e9c51621cff7a9f8a5c95fa7`
- New `content_hash`: `c86051ace4d4f26a68f983988a9812319b24589345292736ca8f6639b636a2ba`
- `helm_mutations[]` appended (mutation_type: `factual_correction`)

Kit v0.1.2 (next release) will re-vendor against this corrected canon. Until v0.1.2 ships, the discrepancy between v0.1.1's vendored bundle and the Brain master is intentional and audit-trail-visible.

### Pattern (the real lesson, restated honestly)

The bridge canon remains an active **cybernetic defence mechanism**, but with a sharpened boundary condition: it defends against drift **between** consumers of the canon (template-vs-template, kit-vs-kit, integration-vs-integration), not drift **between** the canon and the regulator. The latter requires a separate gate that anchors the canon against the regulator's schema. In LodgeiT terms, this is *Standing Rule #12, mc14-refined: hermetic green without production-bundle green is pre-broken — and production-bundle green requires regulator-schema validation, not just internal byte-identity*. (This Kit's CI Gate 2 byte-check enforces internal agreement; it does not yet anchor against the FRC v2026 XSDs. That gate is a candidate for v0.1.3+.)

Forensic chronicle: `clawdog-brain/memory/2026-05-16.md` (Phase A wire-audit + mc14 helm-roll); `clawdog-brain/memory/2026-05-15.md` (Phase 4a.4 Subagent B execution + the inverted banking that this section now corrects); `clawdog-brain/memory/lessons.md` § Lesson #40 (n=3 datapoint, mc14-refined canonical statement).

## Provenance

This Kit's `bridge_canon/` and `bridge_canon_sidecars/` directories are a **byte-identical mirror** of:

- Source repo: `github.com/futureWA/clawdog-brain`
- Source commit: `2fc7451a3068c69d726a2159cced4254fad2187c`
- Source paths: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/**`, `GLOBAL_NOTES/BRIDGE/_schema/**`, `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/**`

Each vendored file's sha256 is declared in `bridge_canon/MANIFEST.json` and verified at PR time by Gate 2 of CI. The Path A v1 lookup artefact additionally carries a Kit wrapper-frontmatter declaring `body_sha256` of the wrapped Brain body (pattern precedent: `lodgeit-labs/clawdog/docs/INTEGRATOR_README.md`).

### Re-vendoring after Brain canon amendment

```bash
python scripts/revendor_from_brain.py \
    --brain-path /path/to/clawdog-brain/checkout \
    --brain-sha  <new-40-char-commit-sha>
python -m pytest tests/                            # both gates must pass
```

## Licence

Apache-2.0. See [LICENSE](LICENSE).

## Cross-references

- [CLAWDOG/113 — SBRM → Framework Bridge canon design (clawdog-brain)](https://github.com/futureWA/clawdog-brain)
- [`lodgeit-labs/LodgeiT_HMRC_CT600`](https://github.com/lodgeit-labs/LodgeiT_HMRC_CT600) — Layer 5 iXBRL renderer (downstream consumer; Phase 4a.4 Subagent B scope).
- [`lodgeit-labs/clawdog`](https://github.com/lodgeit-labs/clawdog) — Wind-Tunnel + CLAWDOG/141 byte-check gate (pattern precedent).
- [`lodgeit-labs/clawdog-calculator-api`](https://github.com/lodgeit-labs/clawdog-calculator-api) — sibling Kit; production-bundle test discipline reference (Standing Rule #12).

*— ClawDog ∮*
