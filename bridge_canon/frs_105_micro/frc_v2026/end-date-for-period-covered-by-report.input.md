---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-input:frs_105_micro:frc_v2026:end-date-for-period-covered-by-report"
ontological_class: "BridgeExternalInput"

# No `dialect:` field per atomic-fact-node convention.
# Validated by `GLOBAL_NOTES/BRIDGE/_schema/bridge-external-input.schema.json`.

bridge_external_input:
  framework_id:         "frs_105_micro"
  taxonomy_version:     "frc_v2026"
  period_applicability: "ongoing"
  framework_concept:    "uk-bus:EndDateForPeriodCoveredByReport"
  mapping_kind:         "external_input"
  statement_role:       "BOILERPLATE"
  input_source:         "period_metadata"
  confidence:           "high"
  notes:                "Period end date from the filing's period dimension."

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "2fa5cae08d345ea3569b0d91083af99425044085d36eab36fe379d8a8ed4b564"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-13-phase-4a-2"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a ratification 2026-05-13 06:31 UTC (CLAWDOG/113 §6)"
    justification:         "Phase 4a.2 promotion of v1 UK_CORE_BOILERPLATE entry into Brain canon as external_input: uk-bus:EndDateForPeriodCoveredByReport"
    timestamp_utc:         "2026-05-13T06:42:00Z"
    ledger_id:             "phase-4a-2-v1-promotion"
    mutation_type:         "node_creation"
    previous_content_hash: null
---


# Bridge external-input — `uk-bus:EndDateForPeriodCoveredByReport` (FRS 105 Micro × FRC v2026)

External-input declaration promoted from v1 production source `lodgeit-labs/LodgeiT_HMRC_CT600/scripts/extract_taxonomy.py::UK_CORE_BOILERPLATE` at commit `db49d5f`. This concept is NOT derivable from the TB; it is supplied at filing time from `period_metadata`.

## Notes

Period end date from the filing's period dimension.

## Cross-references

- CLAWDOG/113 §3.1 (mapping-kind table) + bridge-external-input.schema.json
- v1 production source: `LodgeiT_HMRC_CT600/scripts/extract_taxonomy.py` line 123+ at `db49d5f`
- Phase 4a.2 promotion chronicle: `memory/2026-05-13.md` § 06:42 UTC

*— ClawDog ∮*
