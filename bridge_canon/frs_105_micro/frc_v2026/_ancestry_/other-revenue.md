---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-ancestry:frs_105_micro:frc_v2026:other-revenue"
ontological_class: "BridgeAncestrySubsume"

# No `dialect:` field per atomic-fact-node convention (4a.2 dialect-gate precedent).
# Validated by `GLOBAL_NOTES/BRIDGE/_schema/bridge-ancestry.schema.json`.

bridge_ancestry:
  ancestor_slug:        "other_revenue"
  framework_id:         "frs_105_micro"
  taxonomy_version:     "frc_v2026"
  period_applicability: "ongoing"
  framework_concept:    "uk-core:OtherOperatingIncome"
  mapping_kind:         "ancestry_subsume"
  statement_role:       "PROFIT_LOSS"
  confidence:           "high"
  notes:                'HALT #1 resolution. Anchored to bare `OtherOperatingIncome` (general-purpose). Format1/Format2 variants treated as presentation-axis dispatched by the renderer at render time. FRS 105 Micro layout collapses other-income into operating result; the bare aggregate is the architecturally honest target.'

verifies_against:
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:4959"
    anchor:   "OtherOperatingIncome"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/OtherOperatingIncome.xsd_excerpt"

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "16221d3c57841343f7e40ae0990a13af4dae88b5f43b3526c5aef321ec525f2c"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-15-mc07b"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a.3 HALT #1 ratification 2026-05-15 23:44 UTC ('Halt 1 - anchor to bare - your recommend'); anchor wire-verified at frc-core:4959 type=xbrli:monetaryItemType per CF-1 discipline."
    justification:         "Phase 4a.3 HALT #1 resolution — LodgeiT ancestor slug `other_revenue` subsumes to FRC v2026 `uk-core:OtherOperatingIncome` (bare general-purpose, NOT Format1/Format2 variants — those are presentation-axis layout choices the renderer dispatches at render time). FRS 105 Micro template collapses other-income into operating result; bare aggregate matches that semantics. Anchor verified via Path A v1 lookup table (now updated for HALT #1 resolution). Wire-verified pre-draft per CF-1 (Asymmetric Perimeter generalisation, candidate forensic; same arc n=3 instance — see lessons.md § Candidate Forensics § CF-1)."
    timestamp_utc:         "2026-05-15T23:55:00Z"
    ledger_id:             "phase-4a-3-halt-resolutions-and-pr204-row"
    mutation_type:         "node_creation"
    previous_content_hash: null
---


# Bridge ancestry_subsume — `other_revenue` → `uk-core:OtherOperatingIncome` (FRS 105 Micro × FRC v2026)

Every SBRM code reachable from the LodgeiT-ontology ancestor slug `other_revenue` (via `parent/2` closure in `ClawDog_Share/full_sbrm_physics.pl`) subsumes to FRC v2026 concept `uk-core:OtherOperatingIncome`, **modulo direct_atom overrides** which always win.

## Notes

HALT #1 resolution. Andrew ratified 2026-05-15 23:44 UTC: anchor to **bare** `OtherOperatingIncome`, NOT the Format1/Format2 variants. Format1/Format2 distinction is a presentation-axis choice driven by Companies Act Schedule 1 layout selection (Format 1 = operating-by-nature; Format 2 = operating-by-function). FRS 105 Micro template collapses other-income into operating result, so the bare aggregate is the architecturally honest target. The renderer dispatches to Format1/Format2 at render time if the integrator's reporting framework demands one.

## Anchor verification

- Framework concept: `uk-core:OtherOperatingIncome` (local name `OtherOperatingIncome`)
- Source: `fr/2026-01-01/core/frc-core-2026-01-01.xsd` line `4959`
- Type: `xbrli:monetaryItemType`, `balance="credit"`, `periodType="duration"`, `abstract="false"`
- Sidecar: `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/OtherOperatingIncome.xsd_excerpt`

CF-1 discipline applied: the pre-decision (Andrew's "go your recommend") was wire-verified before this node was drafted. Element exists; line + type confirmed against the XSD bytes, not against ClawDog's recommendation prose.

See Path A v1 lookup artefact: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md` § HALT #1 resolution.

## Cross-references

- CLAWDOG/113 §3.1 (mapping-kind table) + `bridge-ancestry.schema.json`
- `memory/2026-05-13-clawdog-113-frs-105-carryover.md` § 4a.3 RULINGS
- `memory/lessons.md` § Candidate Forensics § CF-1 (n=3 within-arc instance)
- Path A v1 lookup: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md`

*— ClawDog ∮*
