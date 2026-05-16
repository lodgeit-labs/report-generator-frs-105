---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-ancestry:frs_105_micro:frc_v2026:non_current_liabilities"
ontological_class: "BridgeAncestrySubsume"

# No `dialect:` field per atomic-fact-node convention (4a.2 dialect-gate precedent).
# Validated by `GLOBAL_NOTES/BRIDGE/_schema/bridge-ancestry.schema.json`.

bridge_ancestry:
  ancestor_slug:        "non_current_liabilities"
  framework_id:         "frs_105_micro"
  taxonomy_version:     "frc_v2026"
  period_applicability: "ongoing"
  framework_concept:    "uk-core:Creditors"
  mapping_kind:         "ancestry_subsume"
  statement_role:       "BS_LIABILITY"
  confidence:           "high"
  notes:                '133-node `non_current_liabilities` ancestry subsumes to FRC v2026 Creditors aggregate. v1 baseline notes Creditors is the FRC element used by the micro-entity template (not the broader CurrentLiabilities element which serves group/holdco filings). Statement role BS_LIABILITY per micro-entity balance sheet layout.'

verifies_against:
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:2015"
    anchor:   "Creditors"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/Creditors.xsd_excerpt"

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "c2c6f71ce7fac609f5328d717bc8100d90c4c5ead82ef137a08fdbc023293ff5"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-15-mc07"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a.3 dispatch ratification 2026-05-15 (CLAWDOG/113 §6 rung 4a.3; Q1=γ, Q2=core_ComprehensiveIncomeExpense, Q3=Path A v1 lookup first)"
    justification:         "Phase 4a.3 ancestry_subsume — LodgeiT ancestor slug `non_current_liabilities` subsumes to FRC v2026 `uk-core:Creditors`. Anchor verified via Path A v1 lookup at GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md (sidecar: memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/Creditors.xsd_excerpt)."
    timestamp_utc:         "2026-05-15T12:45:00Z"
    ledger_id:             "phase-4a-3-ancestry-and-nn5"
    mutation_type:         "node_creation"
    previous_content_hash: null
---


# Bridge ancestry_subsume — `non_current_liabilities` → `uk-core:Creditors` (FRS 105 Micro × FRC v2026)

Every SBRM code reachable from the LodgeiT-ontology ancestor slug `non_current_liabilities` (via `parent/2` closure in `ClawDog_Share/full_sbrm_physics.pl`) subsumes to FRC v2026 concept `uk-core:Creditors`, **modulo direct_atom overrides** which always win.

## Notes

133-node `non_current_liabilities` ancestry subsumes to FRC v2026 Creditors aggregate. v1 baseline notes Creditors is the FRC element used by the micro-entity template (not the broader CurrentLiabilities element which serves group/holdco filings). Statement role BS_LIABILITY per micro-entity balance sheet layout.

## Anchor verification

- Framework concept: `uk-core:Creditors` (local name `Creditors`)
- Source: `fr/2026-01-01/core/frc-core-2026-01-01.xsd` line `2015`
- Type: `xbrli:monetaryItemType`
- Sidecar: `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/Creditors.xsd_excerpt`

See Path A v1 lookup artefact: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md`.

## Cross-references

- CLAWDOG/113 §3.1 (mapping-kind table) + `bridge-ancestry.schema.json`
- `memory/2026-05-13-clawdog-113-frs-105-carryover.md` § 4a.3 RULINGS
- Path A v1 lookup: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md`

*— ClawDog ∮*
