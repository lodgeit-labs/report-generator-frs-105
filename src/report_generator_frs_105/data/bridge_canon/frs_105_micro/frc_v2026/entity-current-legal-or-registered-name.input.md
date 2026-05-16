---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-input:frs_105_micro:frc_v2026:entity-current-legal-or-registered-name"
ontological_class: "BridgeExternalInput"

# No `dialect:` field per atomic-fact-node convention.
# Validated by `GLOBAL_NOTES/BRIDGE/_schema/bridge-external-input.schema.json`.

bridge_external_input:
  framework_id:         "frs_105_micro"
  taxonomy_version:     "frc_v2026"
  period_applicability: "ongoing"
  framework_concept:    "uk-bus:EntityCurrentLegalOrRegisteredName"
  mapping_kind:         "external_input"
  statement_role:       "BOILERPLATE"
  input_source:         "entity_profile"
  confidence:           "high"
  notes:                "Legal entity name from LodgeiT entity profile. Required by FRC v2026 micro filing."

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "0400ee32d7cefdcf2c991dae774309d70c713254d42b01a7d33c15c717505b6c"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-13-phase-4a-2"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a ratification 2026-05-13 06:31 UTC (CLAWDOG/113 §6)"
    justification:         "Phase 4a.2 promotion of v1 UK_CORE_BOILERPLATE entry into Brain canon as external_input: uk-bus:EntityCurrentLegalOrRegisteredName"
    timestamp_utc:         "2026-05-13T06:42:00Z"
    ledger_id:             "phase-4a-2-v1-promotion"
    mutation_type:         "node_creation"
    previous_content_hash: null
---


# Bridge external-input — `uk-bus:EntityCurrentLegalOrRegisteredName` (FRS 105 Micro × FRC v2026)

External-input declaration promoted from v1 production source `lodgeit-labs/LodgeiT_HMRC_CT600/scripts/extract_taxonomy.py::UK_CORE_BOILERPLATE` at commit `db49d5f`. This concept is NOT derivable from the TB; it is supplied at filing time from `entity_profile`.

## Notes

Legal entity name from LodgeiT entity profile. Required by FRC v2026 micro filing.

## Cross-references

- CLAWDOG/113 §3.1 (mapping-kind table) + bridge-external-input.schema.json
- v1 production source: `LodgeiT_HMRC_CT600/scripts/extract_taxonomy.py` line 123+ at `db49d5f`
- Phase 4a.2 promotion chronicle: `memory/2026-05-13.md` § 06:42 UTC

*— ClawDog ∮*
