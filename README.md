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

## ✅ Real bug this Kit caught (Phase 4a.4 integration case study)

The whole point of a deterministic content-hashed bridge canon (rather than a hand-authored mapping in each consumer's templates) is that hand-authored mappings drift. At Phase 4a.4 integration with `lodgeit-labs/LodgeiT_HMRC_CT600`, the A/B byte-identical iXBRL regression harness surfaced a real defect in the v1 production templates:

- **v1 (hand-authored):** `<ix:nonFraction name="uk-core:DateAuthorisationFinancialStatementsForIssue" ...>`
- **Bridge canon (deterministic):** `uk-bus:DateAuthorisationFinancialStatementsForIssue` (the concept lives in the `uk-bus` namespace, not `uk-core`, in FRC v2026)

The v1 templates carried the wrong namespace prefix on a single concept for an unknown duration. The bridge canon's Phase 4a.2 `external_input` node for that concept correctly anchors to `uk-bus`. The integration's feature-flag A/B byte-identity test refused to pass until the v1 hard-coded fallback was corrected to match the canonical value; net change at template level was a 1-byte shift (`core` → `bus`).

**Why this matters:** the v1 path reportedly passed Arelle FRC v2026 validation 0/0, suggesting Arelle treated the bad namespace as a soft warning rather than a hard error (or namespace-alias resolution was lenient). HMRC TE or Companies House strict validation might not be as forgiving — and downstream consumers of the rendered iXBRL (auditors, regulators, financial-data aggregators) parsing on exact namespace would treat the value as a distinct concept from the intended one.

**Pattern:** the bridge canon is an active **cybernetic defence mechanism**, not just administrative overhead. By forcing consumers to substitute against a deterministic content-hashed atom rather than typing a literal namespace prefix, this Kit surfaces silent namespace defects at the first integration.

Forensic chronicle: `clawdog-brain/memory/2026-05-15.md` (Phase 4a.4 Subagent B execution).

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
