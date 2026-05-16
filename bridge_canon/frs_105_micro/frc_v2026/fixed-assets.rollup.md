---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-rollup:frs_105_micro:frc_v2026:fixed-assets"
ontological_class: "BridgeComputedRollup"

# No `dialect:` field per atomic-fact-node convention.
# Validated by `GLOBAL_NOTES/BRIDGE/_schema/bridge-rollup.schema.json`.

bridge_rollup:
  framework_id:         "frs_105_micro"
  taxonomy_version:     "frc_v2026"
  period_applicability: "ongoing"
  framework_concept:    "uk-core:FixedAssets"
  mapping_kind:         "computed_rollup"
  statement_role:       "BS_COMPUTED"
  formula: |
    % FixedAssets = PropertyPlantEquipment + IntangibleAssets + Investments etc.
    % FRS 105 Micro: micro template carries PPE only by default.
    'uk-core:FixedAssets'(P, V) :-
      framework_value(P, 'uk-core:PropertyPlantEquipment', V).
  depends_on:
    - "uk-core:PropertyPlantEquipment"
  confidence:           "medium"
  notes:                "FRS 105 Micro: passes through PPE; intangibles + investments empty by default. Generalises in FRS 102 1A."

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "f7bc7834b52270685d3ba377daa4745de8ae250efe47fe3e7768f8dc65f67cd6"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-13-phase-4a-2"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a ratification 2026-05-13 06:31 UTC (CLAWDOG/113 §6)"
    justification:         "Phase 4a.2 promotion of v1 UK_CORE_AGGREGATION_PARENTS entry into Brain canon as computed_rollup: uk-core:FixedAssets"
    timestamp_utc:         "2026-05-13T06:42:00Z"
    ledger_id:             "phase-4a-2-v1-promotion"
    mutation_type:         "node_creation"
    previous_content_hash: null
---


# Bridge computed-rollup — `uk-core:FixedAssets` (FRS 105 Micro × FRC v2026)

Computed-rollup promoted from v1 production source `lodgeit-labs/LodgeiT_HMRC_CT600/scripts/extract_taxonomy.py::UK_CORE_AGGREGATION_PARENTS` at commit `db49d5f`, anchored against the micro template at `templates/micro_entity_accounts.html` (production-validated 0 errors / 0 warnings under Arelle FRC v2026, 12,271 bytes, 2026-04-26 04:14 UTC).

## Formula (Prolog-flavoured)

```prolog
% FixedAssets = PropertyPlantEquipment + IntangibleAssets + Investments etc.
% FRS 105 Micro: micro template carries PPE only by default.
'uk-core:FixedAssets'(P, V) :-
  framework_value(P, 'uk-core:PropertyPlantEquipment', V).
```

## Depends on

- `uk-core:PropertyPlantEquipment`

## Notes

FRS 105 Micro: passes through PPE; intangibles + investments empty by default. Generalises in FRS 102 1A.

## Cross-references

- CLAWDOG/113 §3.4 (computed-rollup formula syntax)
- v1 production source: `LodgeiT_HMRC_CT600/scripts/extract_taxonomy.py` line 108+ at `db49d5f`
- Renderer: `LodgeiT_HMRC_CT600/templates/micro_entity_accounts.html`
- Phase 4a.2 promotion chronicle: `memory/2026-05-13.md` § 06:42 UTC

*— ClawDog ∮*
