---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-input:frs_105_micro:frc_v2026:date-authorisation-financial-statements-for-issue"
ontological_class: "BridgeExternalInput"

# No `dialect:` field per atomic-fact-node convention.
# Validated by `GLOBAL_NOTES/BRIDGE/_schema/bridge-external-input.schema.json`.

bridge_external_input:
  framework_id:         "frs_105_micro"
  taxonomy_version:     "frc_v2026"
  period_applicability: "ongoing"
  framework_concept:    "uk-core:DateAuthorisationFinancialStatementsForIssue"
  mapping_kind:         "external_input"
  statement_role:       "BOILERPLATE"
  input_source:         "filing_metadata"
  confidence:           "high"
  notes:                "Date the directors authorised the accounts for issue. Supplied at filing time by the operator (CLAWDOG/112 §5 staging analogue) or computed as filing-day at submission."

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "c86051ace4d4f26a68f983988a9812319b24589345292736ca8f6639b636a2ba"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-13-phase-4a-2"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a ratification 2026-05-13 06:31 UTC (CLAWDOG/113 §6)"
    justification:         "Phase 4a.2 promotion of v1 UK_CORE_BOILERPLATE entry into Brain canon as external_input: uk-bus:DateAuthorisationFinancialStatementsForIssue"
    timestamp_utc:         "2026-05-13T06:42:00Z"
    ledger_id:             "phase-4a-2-v1-promotion"
    mutation_type:         "node_creation"
    previous_content_hash: null
  - mutation_id:           "mut-2026-05-16-mc14-factual-correction"
    agent_id:              "clawdog"
    authority:             |
      Andrew Noble — direct-voice authorisation 2026-05-16 09:35–09:41 UTC webchat
      ("B1 - give me more info" + ratification of the three sub-calls: branch name,
      combined PR, Phase C-gated subagent re-authorisation). Wire evidence:
      deterministic XSD audit of FRC v2026 taxonomy.
    justification:         |
      Phase A wire-anchored audit (2026-05-16 ~07:30–08:10 UTC) of the FRC v2026
      taxonomy XSDs proved that `DateAuthorisationFinancialStatementsForIssue`
      is declared exactly once, at
      `FRC-2026-Taxonomy-v1.0.0/fr/2026-01-01/core/frc-core-2026-01-01.xsd:2091`,
      with `targetNamespace="http://xbrl.frc.org.uk/fr/2026-01-01/core"` — i.e.
      `uk-core:`, not `uk-bus:`. The element is NOT declared in
      `bus-2026-01-01.xsd` (negative-evidence sweep clean). The originating
      `mut-2026-05-13-phase-4a-2` node_creation mutation baked the wrong
      namespace in at birth. The Phase 4a.4 A/B byte-identity harness (PR
      #12 on `lodgeit-labs/LodgeiT_HMRC_CT600`, merge SHA `dad24409`) did NOT
      catch a v1 bug as banked at the time; instead it corrupted a correct v1
      template (`uk-core:DateAuthorisationFinancialStatementsForIssue` at
      `db49d5f:micro_entity_accounts.html:65`) to match the wrong bridge
      canon. Internal A/B agreement is not external regulator-shape correctness
      (Lesson #40 n+1 datapoint banked in this PR). Sweep of the full 40-node
      bridge canon against FRC v2026 XSDs surfaced this as the *only* inverted
      namespace declaration; the other 39 are correct against the wire.
      Downstream blast radius requiring Phase C remediation (separate PRs,
      separate authorisations): (C1) Kit `report-generator-frs-105` README
      'Real bug this Kit caught' case study, which currently publishes the
      inverted claim as a marketing example; (C2) Kit revendor + v0.1.2
      release; (C3) CT600 forward-fix on `micro_entity_accounts.html` and the
      `resolve()` fallback. Brain-side correction (this mc14) corrects the
      bridge canon's atom; downstream consumers re-derive from this corrected
      canon.
    timestamp_utc:         "2026-05-16T09:41:44Z"
    ledger_id:             "mc14-factual-correction"
    mutation_type:         "factual_correction"
    content_hash_rolled:   true
    previous_content_hash: "3dfcdd2cc32e33feddff074450f704ed5863cc61e9c51621cff7a9f8a5c95fa7"
    fields_changed:
      - "bridge_external_input.framework_concept: 'uk-bus:DateAuthorisationFinancialStatementsForIssue' → 'uk-core:DateAuthorisationFinancialStatementsForIssue'"
      - "body H1 + Phase 4a.2 promotion provenance line updated to reflect the corrected canonical concept and to note the v1 template was originally correct"
---


# Bridge external-input — `uk-core:DateAuthorisationFinancialStatementsForIssue` (FRS 105 Micro × FRC v2026)

External-input declaration. The originating v1 production source `lodgeit-labs/LodgeiT_HMRC_CT600/scripts/extract_taxonomy.py::UK_CORE_BOILERPLATE` + `micro_entity_accounts.html:65` at commit `db49d5f` carried the correct `uk-core:` namespace. The Phase 4a.2 promotion (`mut-2026-05-13-phase-4a-2`) mistakenly baked `uk-bus:` into this node; corrected under `mut-2026-05-16-mc14-factual-correction` against deterministic FRC v2026 XSD evidence (`frc-core-2026-01-01.xsd:2091`, targetNamespace `uk-core`). This concept is NOT derivable from the TB; it is supplied at filing time from `filing_metadata`.

## Notes

Date the directors authorised the accounts for issue. Supplied at filing time by the operator (CLAWDOG/112 §5 staging analogue) or computed as filing-day at submission.

## Cross-references

- CLAWDOG/113 §3.1 (mapping-kind table) + bridge-external-input.schema.json
- v1 production source: `LodgeiT_HMRC_CT600/scripts/extract_taxonomy.py` line 123+ at `db49d5f`
- Phase 4a.2 promotion chronicle: `memory/2026-05-13.md` § 06:42 UTC

*— ClawDog ∮*
