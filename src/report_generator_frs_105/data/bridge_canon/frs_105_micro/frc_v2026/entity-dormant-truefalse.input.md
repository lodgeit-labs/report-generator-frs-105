---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-input:frs_105_micro:frc_v2026:entity-dormant-truefalse"
ontological_class: "BridgeExternalInput"

# No `dialect:` field per atomic-fact-node convention.
# Validated by `GLOBAL_NOTES/BRIDGE/_schema/bridge-external-input.schema.json`.

bridge_external_input:
  framework_id:         "frs_105_micro"
  taxonomy_version:     "frc_v2026"
  period_applicability: "ongoing"
  framework_concept:    "uk-bus:EntityDormantTruefalse"
  mapping_kind:         "external_input"
  statement_role:       "BOILERPLATE"
  input_source:         "derived_from_classification"
  default_value:        false
  confidence:           "high"
  notes:                "Default false. Derived true when revenue and expense lines are absent or zero across the period (AA02 dormant filing path)."

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "9355c2b33520523b1626088be956186daef3a6af66a8d6190298391822504919"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-13-phase-4a-2"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a ratification 2026-05-13 06:31 UTC (CLAWDOG/113 §6)"
    justification:         "Phase 4a.2 promotion of v1 UK_CORE_BOILERPLATE entry into Brain canon as external_input: uk-bus:EntityDormantTruefalse"
    timestamp_utc:         "2026-05-13T06:42:00Z"
    ledger_id:             "phase-4a-2-v1-promotion"
    mutation_type:         "node_creation"
    previous_content_hash: null
---


# Bridge external-input — `uk-bus:EntityDormantTruefalse` (FRS 105 Micro × FRC v2026)

External-input declaration promoted from v1 production source `lodgeit-labs/LodgeiT_HMRC_CT600/scripts/extract_taxonomy.py::UK_CORE_BOILERPLATE` at commit `db49d5f`. This concept is NOT derivable from the TB; it is supplied at filing time from `derived_from_classification`.

## Notes

Default false. Derived true when revenue and expense lines are absent or zero across the period (AA02 dormant filing path).

## Cross-references

- CLAWDOG/113 §3.1 (mapping-kind table) + bridge-external-input.schema.json
- v1 production source: `LodgeiT_HMRC_CT600/scripts/extract_taxonomy.py` line 123+ at `db49d5f`
- Phase 4a.2 promotion chronicle: `memory/2026-05-13.md` § 06:42 UTC

*— ClawDog ∮*
