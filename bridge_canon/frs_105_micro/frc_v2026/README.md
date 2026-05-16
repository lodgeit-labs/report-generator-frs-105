# FRS 105 Micro × FRC v2026 — Bridge Fact-Nodes

> **Framework:** UK FRS 105 Micro-Entity Statutory Accounts.
> **Taxonomy version:** FRC v2026 (`uk-core`, `uk-bus`, `dpl`, `direp`, `aurep` namespaces).
> **Phase 4a pilot:** in progress. Phase 4a.1 (this scaffold) merged; Phase 4a.2 (v1 promotion) next.

## Tree state at Phase 4a.1 closure

```
frs_105_micro/frc_v2026/
├── README.md                  # You are here
└── _ancestry_/                # ancestry_subsume rule nodes (populated in Phase 4a.3)
```

Empty subtree at 4a.1 closure — fact-nodes land in subsequent rungs:

| Rung | Adds | Estimated count |
|---|---|---|
| **4a.2** | `<sbrm_code>.md` (direct_atom) + `<framework_concept>.rollup.md` (computed_rollup) + `<framework_concept>.input.md` (external_input) | 12 + 9 + 7 = 28 |
| **4a.3** | `_ancestry_/<ancestor_slug>.md` (ancestry_subsume) | ~15 |
| **4a.4** | (no fact-node additions; Kit creation rung) | — |

Total target population at Phase 4a closure: **~43 fact-nodes.**

## Provenance — v1 source being canonicalised

The v1 production bridge for FRS 105 Micro currently lives in `lodgeit-labs/LodgeiT_HMRC_CT600`:

- **12 direct_atom mappings:** `SBRM_TO_UK_CORE_TAGS` Python dict.
- **9 computed_rollup formulas:** the aggregation-parents table in `memory/uk-taxonomy.md`.
- **7 external_input declarations:** the boilerplate context table in `memory/uk-taxonomy.md`.
- **Renderer:** `micro_entity_accounts.html` Jinja2 template — production-validated **0 errors / 0 warnings** under Arelle FRC v2026 (12,271 bytes; proven 2026-04-26 04:14 UTC).

Phase 4a is **canonicalisation**, not net-new construction. v1 has already passed regulator-grade validation; Phase 4a promotes it under the new declarative schema so multiple frameworks can scale from the same canon shape.

Per D3 ratification (Andrew, 2026-05-13 06:31 UTC): the v1 dict + Jinja2 templates stay in `LodgeiT_HMRC_CT600` as the *source-of-truth* until Phase 4a.4, when the new `lodgeit-labs/report-generator-frs-105` Egress Interface Kit lands; the LodgeiT_HMRC_CT600 v1 surface is deprecated in the same 4a.4 step.

## Identity tuple

Every fact-node in this subtree carries:

| Field | Value here |
|---|---|
| `framework_id` | `frs_105_micro` |
| `taxonomy_version` | `frc_v2026` |
| `period_applicability` | `ongoing` (default) or YYYY-MM-DD..YYYY-MM-DD bounded |
| `sbrm_code` | `sbrm_NNNN` (per node, for direct_atom nodes) |

`framework_id` + `taxonomy_version` are encoded in the directory path; `sbrm_code` is encoded in the filename; `period_applicability` lives in the front-matter (defaults to `ongoing` for current FY filings).

## Statement-role distribution (target, Phase 4a)

| Statement role | Approx. count |
|---|---|
| `PL_REVENUE` | ~3 direct_atom + roll-up parents |
| `PL_EXPENSE` | ~3 direct_atom + roll-up parents |
| `PL_COMPUTED` | 3 roll-ups (GrossProfitLoss, OperatingProfitLoss, ProfitLoss) |
| `BS_ASSET` | ~3 direct_atom + ancestry_subsume + roll-ups |
| `BS_LIABILITY` | ~2 direct_atom + ancestry_subsume + roll-ups |
| `EQUITY` | ~2 direct_atom + roll-up |
| `OCI` | 0 (FRS 105 Micro has no OCI statement; NN#5 routes `comprehensive_income` ancestry to `EQUITY_MOVEMENT` for this framework) |
| `BOILERPLATE` | 7 external_input |

## Non-negotiables specific to FRS 105 Micro

- **NN#5 specialisation:** FRS 105 Micro does **not** have a separate OCI statement. SBRM codes reachable from `comprehensive_income` ancestry route to `EQUITY_MOVEMENT` (the equity-statement movement line) for this framework. For FRS 102 1A and richer frameworks the same codes route to a true `OCI` statement.
- **Renderer-side requirement:** the v1 `micro_entity_accounts.html` template requires all 7 `BOILERPLATE` external_input concepts to be supplied at render time. Missing inputs produce a renderable but Arelle-invalid output. The Phase 4a Kit MUST refuse to render if any required external_input is unresolved (NN#4 generalised to render-time).

## Cross-references

- Bridge canon overview: [`../../README.md`](../../README.md)
- CLAWDOG/113 sprint design: [`../../../CLAWDOG/113_SBRM_TO_FRAMEWORK_BRIDGE.md`](../../../CLAWDOG/113_SBRM_TO_FRAMEWORK_BRIDGE.md)
- v1 baseline detail: [`memory/uk-taxonomy.md`](../../../../memory/uk-taxonomy.md)
- Phase 4a carry-over: [`memory/2026-05-13-clawdog-113-frs-105-carryover.md`](../../../../memory/2026-05-13-clawdog-113-frs-105-carryover.md)
- Layer 6 transports (UK): [`memory/ct600.md`](../../../../memory/ct600.md), [`memory/companies-house.md`](../../../../memory/companies-house.md)

*— ClawDog ∮*
