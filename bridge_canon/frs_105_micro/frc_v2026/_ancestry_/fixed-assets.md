---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-ancestry:frs_105_micro:frc_v2026:fixed_assets"
ontological_class: "BridgeAncestrySubsume"

# No `dialect:` field per atomic-fact-node convention (4a.2 dialect-gate precedent).
# Validated by `GLOBAL_NOTES/BRIDGE/_schema/bridge-ancestry.schema.json`.

bridge_ancestry:
  ancestor_slug:        "fixed_assets"
  framework_id:         "frs_105_micro"
  taxonomy_version:     "frc_v2026"
  period_applicability: "ongoing"
  framework_concept:    "uk-core:FixedAssets"
  mapping_kind:         "ancestry_subsume"
  statement_role:       "BS_ASSET"
  confidence:           "high"
  notes:                '171-node `fixed_assets` ancestry subsumes to FRC v2026 FixedAssets. PropertyPlantEquipment direct_atom override (sbrm_1654) retained.'

verifies_against:
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:2992"
    anchor:   "FixedAssets"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/FixedAssets.xsd_excerpt"

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "74e8408f016213a1f5d26d5ed464aaf19d0ddee11ab88e496b0a769cc5969944"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-15-mc07"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a.3 dispatch ratification 2026-05-15 (CLAWDOG/113 §6 rung 4a.3; Q1=γ, Q2=core_ComprehensiveIncomeExpense, Q3=Path A v1 lookup first)"
    justification:         "Phase 4a.3 ancestry_subsume — LodgeiT ancestor slug `fixed_assets` subsumes to FRC v2026 `uk-core:FixedAssets`. Anchor verified via Path A v1 lookup at GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md (sidecar: memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/FixedAssets.xsd_excerpt)."
    timestamp_utc:         "2026-05-15T12:45:00Z"
    ledger_id:             "phase-4a-3-ancestry-and-nn5"
    mutation_type:         "node_creation"
    previous_content_hash: null
---


# Bridge ancestry_subsume — `fixed_assets` → `uk-core:FixedAssets` (FRS 105 Micro × FRC v2026)

Every SBRM code reachable from the LodgeiT-ontology ancestor slug `fixed_assets` (via `parent/2` closure in `ClawDog_Share/full_sbrm_physics.pl`) subsumes to FRC v2026 concept `uk-core:FixedAssets`, **modulo direct_atom overrides** which always win.

## Notes

171-node `fixed_assets` ancestry subsumes to FRC v2026 FixedAssets. PropertyPlantEquipment direct_atom override (sbrm_1654) retained.

## Anchor verification

- Framework concept: `uk-core:FixedAssets` (local name `FixedAssets`)
- Source: `fr/2026-01-01/core/frc-core-2026-01-01.xsd` line `2992`
- Type: `xbrli:monetaryItemType`
- Sidecar: `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/FixedAssets.xsd_excerpt`

See Path A v1 lookup artefact: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md`.

## Cross-references

- CLAWDOG/113 §3.1 (mapping-kind table) + `bridge-ancestry.schema.json`
- `memory/2026-05-13-clawdog-113-frs-105-carryover.md` § 4a.3 RULINGS
- Path A v1 lookup: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md`

*— ClawDog ∮*
