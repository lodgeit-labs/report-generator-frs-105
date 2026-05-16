---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-ancestry:frs_105_micro:frc_v2026:trading_revenue"
ontological_class: "BridgeAncestrySubsume"

# No `dialect:` field per atomic-fact-node convention (4a.2 dialect-gate precedent).
# Validated by `GLOBAL_NOTES/BRIDGE/_schema/bridge-ancestry.schema.json`.

bridge_ancestry:
  ancestor_slug:        "trading_revenue"
  framework_id:         "frs_105_micro"
  taxonomy_version:     "frc_v2026"
  period_applicability: "ongoing"
  framework_concept:    "uk-core:TurnoverRevenue"
  mapping_kind:         "ancestry_subsume"
  statement_role:       "PL_REVENUE"
  confidence:           "high"
  notes:                'Whole `trading_revenue` ancestry (21 SBRM descendants per full_sbrm_physics.pl parent/2 closure) subsumes to FRC v2026 TurnoverRevenue. Direct_atom override at sbrm_4101 retained.'

verifies_against:
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:6100"
    anchor:   "TurnoverRevenue"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/TurnoverRevenue.xsd_excerpt"

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "1b513d0a391f9f73019097817025276a180260c7edb061cbe7710b335b5a7eff"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-15-mc07"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a.3 dispatch ratification 2026-05-15 (CLAWDOG/113 §6 rung 4a.3; Q1=γ, Q2=core_ComprehensiveIncomeExpense, Q3=Path A v1 lookup first)"
    justification:         "Phase 4a.3 ancestry_subsume — LodgeiT ancestor slug `trading_revenue` subsumes to FRC v2026 `uk-core:TurnoverRevenue`. Anchor verified via Path A v1 lookup at GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md (sidecar: memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/TurnoverRevenue.xsd_excerpt)."
    timestamp_utc:         "2026-05-15T12:45:00Z"
    ledger_id:             "phase-4a-3-ancestry-and-nn5"
    mutation_type:         "node_creation"
    previous_content_hash: null
---


# Bridge ancestry_subsume — `trading_revenue` → `uk-core:TurnoverRevenue` (FRS 105 Micro × FRC v2026)

Every SBRM code reachable from the LodgeiT-ontology ancestor slug `trading_revenue` (via `parent/2` closure in `ClawDog_Share/full_sbrm_physics.pl`) subsumes to FRC v2026 concept `uk-core:TurnoverRevenue`, **modulo direct_atom overrides** which always win.

## Notes

Whole `trading_revenue` ancestry (21 SBRM descendants per full_sbrm_physics.pl parent/2 closure) subsumes to FRC v2026 TurnoverRevenue. Direct_atom override at sbrm_4101 retained.

## Anchor verification

- Framework concept: `uk-core:TurnoverRevenue` (local name `TurnoverRevenue`)
- Source: `fr/2026-01-01/core/frc-core-2026-01-01.xsd` line `6100`
- Type: `xbrli:monetaryItemType`
- Sidecar: `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/TurnoverRevenue.xsd_excerpt`

See Path A v1 lookup artefact: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md`.

## Cross-references

- CLAWDOG/113 §3.1 (mapping-kind table) + `bridge-ancestry.schema.json`
- `memory/2026-05-13-clawdog-113-frs-105-carryover.md` § 4a.3 RULINGS
- Path A v1 lookup: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md`

*— ClawDog ∮*
