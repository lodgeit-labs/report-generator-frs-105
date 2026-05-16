---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-ancestry:frs_105_micro:frc_v2026:comprehensive_income"
ontological_class: "BridgeAncestrySubsume"

# No `dialect:` field per atomic-fact-node convention (4a.2 dialect-gate precedent).
# Validated by `GLOBAL_NOTES/BRIDGE/_schema/bridge-ancestry.schema.json`.

bridge_ancestry:
  ancestor_slug:        "comprehensive_income"
  framework_id:         "frs_105_micro"
  taxonomy_version:     "frc_v2026"
  period_applicability: "ongoing"
  framework_concept:    "uk-core:ComprehensiveIncomeExpense"
  mapping_kind:         "ancestry_subsume"
  statement_role:       "OCI"
  confidence:           "high"
  notes:                'Per CLAWDOG/113 NN#5 — LodgeiT collocates OCI under `revenue` for AU/internal reasons; FRS 105 separates OCI from P&L. Every SBRM code under comprehensive_income subsumes to core:ComprehensiveIncomeExpense with statement_role=OCI, ensuring the NN#5 binary-failure test asserts against a non-empty subject set.'

verifies_against:
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:1900"
    anchor:   "ComprehensiveIncomeExpense"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/ComprehensiveIncomeExpense.xsd_excerpt"

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "a743ec92306c97681d51ea8ff39f13619f25b23fc8f8041957c57d5d06ff8c47"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-15-mc07"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a.3 dispatch ratification 2026-05-15 (CLAWDOG/113 §6 rung 4a.3; Q1=γ, Q2=core_ComprehensiveIncomeExpense, Q3=Path A v1 lookup first)"
    justification:         "Phase 4a.3 ancestry_subsume — LodgeiT ancestor slug `comprehensive_income` subsumes to FRC v2026 `uk-core:ComprehensiveIncomeExpense`. Anchor verified via Path A v1 lookup at GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md (sidecar: memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/ComprehensiveIncomeExpense.xsd_excerpt)."
    timestamp_utc:         "2026-05-15T12:45:00Z"
    ledger_id:             "phase-4a-3-ancestry-and-nn5"
    mutation_type:         "node_creation"
    previous_content_hash: null
---


# Bridge ancestry_subsume — `comprehensive_income` → `uk-core:ComprehensiveIncomeExpense` (FRS 105 Micro × FRC v2026)

Every SBRM code reachable from the LodgeiT-ontology ancestor slug `comprehensive_income` (via `parent/2` closure in `ClawDog_Share/full_sbrm_physics.pl`) subsumes to FRC v2026 concept `uk-core:ComprehensiveIncomeExpense`, **modulo direct_atom overrides** which always win.

## Notes

Per CLAWDOG/113 NN#5 — LodgeiT collocates OCI under `revenue` for AU/internal reasons; FRS 105 separates OCI from P&L. Every SBRM code under comprehensive_income subsumes to core:ComprehensiveIncomeExpense with statement_role=OCI, ensuring the NN#5 binary-failure test asserts against a non-empty subject set.

## Anchor verification

- Framework concept: `uk-core:ComprehensiveIncomeExpense` (local name `ComprehensiveIncomeExpense`)
- Source: `fr/2026-01-01/core/frc-core-2026-01-01.xsd` line `1900`
- Type: `xbrli:monetaryItemType`
- Sidecar: `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/ComprehensiveIncomeExpense.xsd_excerpt`

See Path A v1 lookup artefact: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md`.

## Cross-references

- CLAWDOG/113 §3.1 (mapping-kind table) + `bridge-ancestry.schema.json`
- `memory/2026-05-13-clawdog-113-frs-105-carryover.md` § 4a.3 RULINGS
- Path A v1 lookup: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md`

*— ClawDog ∮*
