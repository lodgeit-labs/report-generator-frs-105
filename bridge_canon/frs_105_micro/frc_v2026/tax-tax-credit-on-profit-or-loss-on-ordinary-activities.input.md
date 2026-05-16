---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-input:frs_105_micro:frc_v2026:tax-tax-credit-on-profit-or-loss-on-ordinary-activities"
ontological_class: "BridgeExternalInput"

# No `dialect:` field per atomic-fact-node convention.
# Validated by `GLOBAL_NOTES/BRIDGE/_schema/bridge-external-input.schema.json`.

bridge_external_input:
  framework_id:         "frs_105_micro"
  taxonomy_version:     "frc_v2026"
  period_applicability: "ongoing"
  framework_concept:    "uk-core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities"
  mapping_kind:         "external_input"
  statement_role:       "PL_EXPENSE"
  input_source:         "operator_approval"
  confidence:           "high"
  notes:                "Tax charge crosses the inter-pipeline boundary from the CT600 calc-side to the accounts-side. Per Q1 ruling 2026-05-13 (carryover §4a.3): the value lands at render time via the operator_approval resolver (CLAWDOG/112 §5 staging-pattern analogue), NOT as a canon-side computed_rollup. The earlier 4a.2 mint (computed_rollup with synthetic lodgeit:ct600_tax_charge dependency) is structurally wrong — replaced under mut-2026-05-15-mc07 node_replacement."

verifies_against:
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:5891"
    anchor:   "TaxTaxCreditOnProfitOrLossOnOrdinaryActivities"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/TaxTaxCreditOnProfitOrLossOnOrdinaryActivities.xsd_excerpt"

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "82e038963eb0005481afbfb49148d127225bd7a93d84fba36cebb7828072a09b"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-15-mc07"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a.3 dispatch ratification 2026-05-15 (CLAWDOG/113 §6 rung 4a.3; Q1=γ, Q2=core_ComprehensiveIncomeExpense, Q3=Path A v1 lookup first)"
    justification:         "Phase 4a.3 Q1 correction — replaces the 4a.2 computed_rollup mint (content_hash 6a97fded72521998c40636542444f00b5af1f4b1d710007f5682ba6bdfbff3e3) with external_input (input_source: operator_approval) per ratified Q1=γ ruling. The tax charge is sourced from the CT600 pipeline via operator-approval staging, not derived from a synthetic lodgeit:ct600_tax_charge canon dependency. external_input count rises 7→8; computed_rollup count falls 10→9; total node count stays 29 (+10 ancestry_subsume = 39 in this PR; rolled per dispatch arithmetic 7→8 / 10→9 / 12 direct_atom + 10 ancestry = 39 not 44 because the dispatch's 44 assumed 15 ancestry, but G3 scope-clip ratified 10 + 5 HALTs)."
    timestamp_utc:         "2026-05-15T12:45:00Z"
    ledger_id:             "phase-4a-3-ancestry-and-nn5"
    mutation_type:         "node_replacement"
    previous_content_hash: "6a97fded72521998c40636542444f00b5af1f4b1d710007f5682ba6bdfbff3e3"
---


# Bridge external-input — `uk-core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` (FRS 105 Micro × FRC v2026)

External-input declaration for the tax charge on profit/loss on ordinary activities.

Per Q1 ruling (Andrew, 2026-05-13 07:19 UTC via Memory Tracer):

> Option β (synthetic namespace) hides the dependency. Option δ (new mapping kind) over-engineers a solution for a boundary edge-case. Option γ is the most architecturally honest. It explicitly declares that the tax charge is an external dependency coming from the CT600 pipeline and forces it through the standard operator approval/staging patterns you've already established.

**This node replaces** the 4a.2-minted `tax-tax-credit-on-profit-or-loss-on-ordinary-activities.rollup.md` (`computed_rollup`, previous_content_hash `6a97fded72521998c40636542444f00b5af1f4b1d710007f5682ba6bdfbff3e3`). The replaced node carried a synthetic `lodgeit:ct600_tax_charge` `depends_on` reference which masked an external boundary as an internal canon computation; structurally wrong under the four-atom bridge identity (D1) + Standing Rule #3 zero-hallucination provenance.

## Pipeline path

`LodgeiT_HMRC_CT600/master_pipeline.py` computes the tax charge in the CT600 calc-side leg (`TaxableTotalProfits × CorpTaxRate`, with reliefs). At accounts-side render time, the report-generator-frs-105 Kit (Phase 4a.4) resolves `uk-core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities` by calling the `operator_approval` resolver against the CT600 leg's emitted value, gated by the same staging-approval boundary used for calculator-emitted journals (CLAWDOG/112 §5).

## Anchor verification

- Framework concept: `uk-core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities`
- Source: `fr/2026-01-01/core/frc-core-2026-01-01.xsd` line `5891`
- Type: `xbrli:monetaryItemType`
- Sidecar: `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/TaxTaxCreditOnProfitOrLossOnOrdinaryActivities.xsd_excerpt`

## Cross-references

- CLAWDOG/113 §3.1 (mapping-kind table) + `bridge-external-input.schema.json`
- CLAWDOG/112 §5 (operator-approval staging-pattern analogue)
- `memory/2026-05-13-clawdog-113-frs-105-carryover.md` § 4a.3 RULINGS Q1
- Path A v1 lookup: `GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md`
- Predecessor (replaced): `tax-tax-credit-on-profit-or-loss-on-ordinary-activities.rollup.md` @ content_hash `6a97fded72521998c40636542444f00b5af1f4b1d710007f5682ba6bdfbff3e3`

*— ClawDog ∮*
