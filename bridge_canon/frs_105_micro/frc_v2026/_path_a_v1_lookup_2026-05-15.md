---
kit_vendor_wrapper:
  source_brain_repo:         "github.com/futureWA/clawdog-brain"
  source_brain_canon_commit: "2fc7451a3068c69d726a2159cced4254fad2187c"
  source_brain_path:         "GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md"
  vendored_at_utc:           "2026-05-16T02:14:49Z"
  body_sha256:               "6920d13ba2410d3c11343e64ccd6e3ea062cf755c6ca99bab9287de8c21787e2"
  body_bytes:                18420
  notes: |
    Kit-side wrapper around byte-identical Brain canon body. The body below
    the closing '---' marker is a verbatim byte-copy from Brain; body_sha256
    above is the SHA-256 of those bytes. Kit-CI byte-check gate enforces
    no drift. Pattern precedent: lodgeit-labs/clawdog/docs/INTEGRATOR_README.md.
---
---
"@context": "https://lodgeit-labs.org/sbrm/bridge/v1"
"@id": "urn:sbrm:bridge-pathA:frs_105_micro:frc_v2026:lookup_v1_2026-05-15"
ontological_class: "BridgePathALookup"
artefact_kind: "path_a_v1_lookup"
framework_id: "frs_105_micro"
taxonomy_version: "frc_v2026"
lookup_date: "2026-05-15"

# Standing Rule #11 — `verifies_against:` lifts the byte-truth claim out of
# prose and into machine-checkable form. Each entry pins a framework_concept
# element to its source XSD line + sidecar excerpt.
verifies_against:
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:1900"
    anchor:   "ComprehensiveIncomeExpense"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/ComprehensiveIncomeExpense.xsd_excerpt"
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:6100"
    anchor:   "TurnoverRevenue"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/TurnoverRevenue.xsd_excerpt"
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:2061"
    anchor:   "CurrentAssets"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/CurrentAssets.xsd_excerpt"
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:2992"
    anchor:   "FixedAssets"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/FixedAssets.xsd_excerpt"
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:1744"
    anchor:   "CashBankOnHand"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/CashBankOnHand.xsd_excerpt"
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:5219"
    anchor:   "PropertyPlantEquipment"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/PropertyPlantEquipment.xsd_excerpt"
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:2724"
    anchor:   "Equity"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/Equity.xsd_excerpt"
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:5577"
    anchor:   "ShareCapital"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/ShareCapital.xsd_excerpt"
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:5236"
    anchor:   "Provisions"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/Provisions.xsd_excerpt"
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:2015"
    anchor:   "Creditors"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/Creditors.xsd_excerpt"
  - source:   "ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip#fr/2026-01-01/core/frc-core-2026-01-01.xsd:5891"
    anchor:   "TaxTaxCreditOnProfitOrLossOnOrdinaryActivities"
    sidecar:  "memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/TaxTaxCreditOnProfitOrLossOnOrdinaryActivities.xsd_excerpt"

cryptographic_anchor:
  hash_algorithm: "SHA-256"
  hash_target:    "self"
  content_hash:   "9e681160b1e58deddb716bd18b77ddcfa61d1ac186c3686322bee72455776aff"
  ipfs_cid:       "PENDING_IPFS_BROADCAST"
  hash_domain:    "pre_anchor_draft"

cybernetic_state:
  status: "draft"

helm_mutations:
  - mutation_id:           "mut-2026-05-15-mc07"
    agent_id:              "clawdog"
    authority:             "Andrew Noble — Phase 4a.3 dispatch ratification 2026-05-15 (CLAWDOG/113 §6 rung 4a.3; Q1=γ, Q2=core_ComprehensiveIncomeExpense, Q3=Path A v1 lookup first)"
    justification:         "Phase 4a.3 — Path A v1 lookup against FRC v2026 taxonomy. Per Q3 ruling: mandatory Lesson #41 two-pass verification BEFORE drafting any ancestry_subsume fact-nodes. Output covers the 10 ratified anchors + the Q1 tax-charge anchor; surfaces 5 anchor-ambiguity HALTs for Andrew ratification (dispatch §G2)."
    timestamp_utc:         "2026-05-15T12:45:00Z"
    ledger_id:             "phase-4a-3-ancestry-and-nn5"
    mutation_type:         "node_creation"
    previous_content_hash: null
---


# Path A v1 lookup — FRS 105 Micro × FRC v2026 (2026-05-15)

Lookup artefact for Phase 4a.3 ancestry_subsume drafting. Per Q3 ruling in `memory/2026-05-13-clawdog-113-frs-105-carryover.md` § 4a.3 RULINGS, **no FRC v2026 framework_concept is anchored from memory.** Each anchor cited in this artefact has been parsed out of the FRC v2026 taxonomy XSD bytes and pinned to (a) its source XSD path, (b) its source line number, (c) its `type=` attribute, and (d) a sidecar file under `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/` carrying the exact `<element ... />` line.

## Method

**Pass 1 — Element existence index.** All 33 XSDs in `ClawDog_Share/FRC-2026-Taxonomy-v1.0.0.zip` parsed with `xml.etree.ElementTree`. Built lookup `{element_local_name → [(source_xsd, line_no, type_attr, substitutionGroup, id), ...]}` (8,024 distinct local-names across 33 XSDs). For each candidate framework_concept used by an ancestry_subsume rule or the Q1 tax-charge correction, the lookup is queried; the first hit in `fr/2026-01-01/core/frc-core-2026-01-01.xsd` (or `cd/2026-01-01/business/bus-2026-01-01.xsd` for entity-profile concepts) is recorded.

**Pass 2 — Type-prefix → namespace URI map.** Each XSD root's `xmlns:*` declarations are harvested. The two primary XSDs (core + bus) supply the prefix → URI mapping used to resolve every `type=` reference recorded in Pass 1. **No full DTS resolution is attempted** — that is Arelle's job at instance-validation time (per dispatch §Q3). Recording cross-namespace dependency by URI is sufficient evidence at this layer.

## Pass 1 — Element existence table

The 11 framework_concepts used by the 4a.3 PR (10 ancestry_subsume anchors + 1 Q1 tax-charge correction):

| framework_concept | element_local_name | xsd_path | line | type | sidecar |
|---|---|---|---|---|---|
| uk-core:ComprehensiveIncomeExpense | ComprehensiveIncomeExpense | `fr/2026-01-01/core/frc-core-2026-01-01.xsd` | 1900 | `xbrli:monetaryItemType` | `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/ComprehensiveIncomeExpense.xsd_excerpt` |
| uk-core:TurnoverRevenue | TurnoverRevenue | `fr/2026-01-01/core/frc-core-2026-01-01.xsd` | 6100 | `xbrli:monetaryItemType` | `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/TurnoverRevenue.xsd_excerpt` |
| uk-core:CurrentAssets | CurrentAssets | `fr/2026-01-01/core/frc-core-2026-01-01.xsd` | 2061 | `xbrli:monetaryItemType` | `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/CurrentAssets.xsd_excerpt` |
| uk-core:FixedAssets | FixedAssets | `fr/2026-01-01/core/frc-core-2026-01-01.xsd` | 2992 | `xbrli:monetaryItemType` | `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/FixedAssets.xsd_excerpt` |
| uk-core:CashBankOnHand | CashBankOnHand | `fr/2026-01-01/core/frc-core-2026-01-01.xsd` | 1744 | `xbrli:monetaryItemType` | `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/CashBankOnHand.xsd_excerpt` |
| uk-core:PropertyPlantEquipment | PropertyPlantEquipment | `fr/2026-01-01/core/frc-core-2026-01-01.xsd` | 5219 | `xbrli:monetaryItemType` | `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/PropertyPlantEquipment.xsd_excerpt` |
| uk-core:Equity | Equity | `fr/2026-01-01/core/frc-core-2026-01-01.xsd` | 2724 | `xbrli:monetaryItemType` | `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/Equity.xsd_excerpt` |
| uk-core:ShareCapital | ShareCapital | `fr/2026-01-01/core/frc-core-2026-01-01.xsd` | 5577 | `nonnum:domainItemType` | `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/ShareCapital.xsd_excerpt` |
| uk-core:Provisions | Provisions | `fr/2026-01-01/core/frc-core-2026-01-01.xsd` | 5236 | `xbrli:monetaryItemType` | `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/Provisions.xsd_excerpt` |
| uk-core:Creditors | Creditors | `fr/2026-01-01/core/frc-core-2026-01-01.xsd` | 2015 | `xbrli:monetaryItemType` | `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/Creditors.xsd_excerpt` |
| uk-core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities | TaxTaxCreditOnProfitOrLossOnOrdinaryActivities | `fr/2026-01-01/core/frc-core-2026-01-01.xsd` | 5891 | `xbrli:monetaryItemType` | `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/TaxTaxCreditOnProfitOrLossOnOrdinaryActivities.xsd_excerpt` |

Sidecars carry the exact byte-for-byte `<element ... />` line; see `memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/`.

## Pass 2 — Type-prefix → namespace URI map

Merged `xmlns:*` declarations from `fr/2026-01-01/core/frc-core-2026-01-01.xsd` + `cd/2026-01-01/business/bus-2026-01-01.xsd`:

| type_prefix | namespace_URI |
|---|---|
| bus | http://xbrl.frc.org.uk/cd/2026-01-01/business |
| core | http://xbrl.frc.org.uk/fr/2026-01-01/core |
| countries | http://xbrl.frc.org.uk/cd/2026-01-01/countries |
| curr | http://xbrl.frc.org.uk/cd/2026-01-01/currencies |
| lang | http://xbrl.frc.org.uk/cd/2026-01-01/languages |
| link | http://www.xbrl.org/2003/linkbase |
| nonnum | http://www.xbrl.org/dtr/type/non-numeric |
| num | http://www.xbrl.org/dtr/type/numeric |
| types | http://xbrl.frc.org.uk/general/2026-01-01/types |
| xbrldt | http://xbrl.org/2005/xbrldt |
| xbrli | http://www.xbrl.org/2003/instance |
| xlink | http://www.w3.org/1999/xlink |
| xsi | http://www.w3.org/2001/XMLSchema-instance |

The two prefixes that recur in every Pass 1 row are `xbrli` (most monetary aggregates) and `nonnum` (domain-item-type structural members like ShareCapital). Cross-namespace dependency is recorded; full DTS resolution deferred to Arelle.


## Anchor-Ambiguity HALT Surfaces (G2 — surfaced, then ratified)

The Path A lookup pass surfaced 5 LodgeiT slugs whose FRC v2026 anchor is structurally ambiguous. Per dispatch §G2, ClawDog HALTED rather than picking autonomously. The 4a.3 PR initially shipped 10 ratified ancestry_subsume rules per dispatch §G3 scope-clip. **Andrew ratified the 5 HALTs at 2026-05-15 23:44–23:55 UTC** (sub-table below records the resolutions); the amendment commit added 1 ancestry_subsume node (HALT #1) and 3 new open threads (#55/#56/#57). Final 4a.3 ancestry_subsume count: **11**.

| LodgeiT slug | Candidates considered | Why ambiguous | Downstream impact |
|---|---|---|---|
| `other_revenue` | `core:OtherOperatingIncome` (line 4959); `core:OtherOperatingIncomeFormat1` (line 4961); `core:OtherOperatingIncomeFormat2` (line 4962) | Three FRC v2026 elements all of `type=xbrli:monetaryItemType`. Format1/Format2 distinction is presentation-statement-layout-driven (FRS 102 Schedule 1 Format 1 vs Format 2). Cannot pick without ratifying which layout the FRS 105 micro template adopts (v1 production template uses neither explicitly — micro layout collapses other-income into operating result). | 237 descendant SBRM codes route to no ancestry rule; direct_atom mappings if any retained. NN#5 not impacted. |
| `investment_revenue` | No bare `InvestmentIncome` element exists in any of the 33 XSDs. Narrower candidates include `core:DividendsInterestIncomeInvestmentFunds`, `core:InterestPayableSimilarChargesFinanceCosts` (wrong sign — expense not income), `core:FurtherItemInterestIncomeComponentTotalInterestIncome` (compositional). | No 1:1 anchor; FRC v2026 splits the LodgeiT `investment_revenue` ancestry into dividends/interest/other-investment-income narrower concepts. Subsume to a single concept would lose information. | 117 descendant SBRM codes route via direct_atom mappings (when minted) rather than ancestry subsumption. Future Phase 4b consideration: per-leaf direct_atoms or a synthetic ancestry pair (`dividend_revenue` / `interest_revenue`). |
| `grants` | `core:GovernmentGrantIncome` (line 3563, monetary) | Single candidate but Hazard #3 (IAS 20 deferred-income treatment, memory/sbrm-to-ifrs-bridge.md) means LodgeiT `grants` semantics conflict with FRS 105 grant-recognition logic — grants may be deferred (liability) or recognised (income). Subsume rule cannot encode that conditional. Calculator-shaped, not bridge-shaped. | 25 descendant SBRM codes need calculator-emitted journals (per CLAWDOG/112 §5 staging-pattern) before bridge can route them. Defer. |
| `accounts_receivables` | `core:Debtors` (line 2115, monetary aggregate); `core:TradeDebtorsTradeReceivables` (line 6016, monetary, narrower) | Both monetary. `Debtors` is the FRC umbrella for amounts-falling-due-within-one-year; `TradeDebtorsTradeReceivables` is the trade-specific narrower concept. LodgeiT `accounts_receivables` has gross + provision children — could subsume to either. Existing 4a.2 direct_atom (sbrm_1141) targets `Debtors`; ancestry would be redundant or contradictory. | 7 descendant SBRM codes covered by 4a.2 direct_atom (sbrm_1141 → Debtors); ancestry rule deferred until LodgeiT semantics of `accounts_receivables` ancestry are ratified (trade-only or trade+other?). |
| `reserves` | `core:OtherReservesSubtotal` (line 4995, nonnum domain); subsidiary candidates include `core:RetainedEarningsAccumulatedLosses` (sbrm_3113 direct_atom in canon); structural `Reserves` aggregate element not present as a single non-abstract monetary item | Multiple narrower reserve concepts; no FRC v2026 element named bare `Reserves` of type monetary. Subsume would collapse distinct reserve categories. | 15 descendant SBRM codes route via direct_atom mappings; ancestry deferred. |

These 5 HALTs were surfaced for Andrew's decision; resolutions banked 2026-05-15 23:44–23:55 UTC:

| HALT | Resolution | Action |
|---|---|---|
| #1 `other_revenue` | **Anchored** to bare `core:OtherOperatingIncome` (frc-core:4959, monetary). Format1/Format2 variants are presentation-axis dispatched by renderer at render time. CF-1 wire-verification done before drafting. | New ancestry_subsume node minted: `_ancestry_/other-revenue.md`. |
| #2 `investment_revenue` | **Deferred.** No clean FRC v2026 monetary aggregate anchor. Slug-vs-FRS 105 mismatch is genuine. | Open Thread #55 opened. |
| #3 `grants` | **Deferred** per Hazard #3 (IAS 20 deferred-income is calculator-shaped, not bridge-shaped). | Open Thread #56 opened (Hazard #3 elaboration). |
| #4 `accounts_receivables` | **Skip-with-annotation.** 4a.2 direct_atom (sbrm_1141 → `Debtors`) already serves; ancestry rule would create non-determinism. Andrew flagged for human-eye inspection during Phase 4a.5 production-surface validation. | No new node minted; this annotation is the canonical record. |
| #5 `reserves` | **Deferred.** CF-1 wire-verification of subagent's `OtherReservesSubtotal` candidate (frc-core:4995) revealed it is `abstract="true"` + `type="nonnum:domainItemType"` (dimension domain head, NOT a value-bearing monetary aggregate). My recommendation to Andrew was based on a hallucinated element name (`OtherReservesIncludingProfitOrLossInPeriod`) that does not exist in any of the 33 XSDs; the wire falsified it. No clean FRS 105 monetary-aggregate anchor exists for `reserves` in this taxonomy version (FRC v2026 reorganised equity components to dimensional-axis decomposition of `core:Equity`). | Open Thread #57 opened. **CF-1 n=3 within-arc instance** banked in lessons.md. |

## Structural Finding — Slug-vs-FRS 105 Aggregate Sparseness

The 5-HALT pattern surfaces a real structural concern: **LodgeiT's AU-tax-flavoured slug ancestries do not have a 1:1 mapping density with FRS 105 statutory aggregates in the FRC v2026 taxonomy.** Of the 5 HALT-surfaced slugs:

- 1 anchored cleanly (HALT #1, `other_revenue`).
- 1 covered by an existing 4a.2 direct_atom (HALT #4, `accounts_receivables` → `sbrm_1141`).
- 3 have no clean monetary-aggregate anchor in FRC v2026 (HALTs #2, #3, #5 — `investment_revenue`, `grants`, `reserves`).

This is **3-of-5 = 60% sparseness** in the bridge mapping for the ambiguous slug subset. The 10 originally-shipped ancestry_subsume rules were the *easy* cases (clean monetary aggregates that line up with FRS 105 structure); the HALTs surface the *hard* cases where LodgeiT's AU-tax ontology and FRC v2026's UK-statutory ontology genuinely diverge.

Three underlying drivers:

1. **Taxonomic reorganisation in FRC 2026.** Equity-component balances (`RetainedEarnings`, `SharePremiumAccount`, `Reserves` family) moved from named monetary elements to dimensional-axis decomposition of `core:Equity`. This breaks 1:1 element lookups for slug ancestries that assumed FRC 2022/2023 layouts.
2. **Recognition-vs-flow conditionals.** Slugs like `grants` carry semantics that depend on conditional recognition logic (IAS 20 deferred-income). The bridge can't encode the conditional; calculators emit the recognised journal.
3. **AU-shaped ontology meets UK-shaped taxonomy.** Slugs like `investment_revenue` aggregate dividend + interest + other-investment-income; FRS 105 splits these into narrower concepts with statutory-specific treatment.

**Phase 4a.6 closure requirement (banked here):** before declaring Phase 4a complete, a **final human-eye review of the hyperplane mapping** is required — specifically Andrew or a qualified accountant inspects the cumulative bridge canon (direct_atom + computed_rollup + external_input + ancestry_subsume) against a real FRS 105 Micro filing to confirm the mapping density is sufficient for production. If the sparseness compounds with more LodgeiT slugs that get used in production filings, Phase 4b (FRS 102 1A) should explicitly budget for synthetic-ancestry-pair work (e.g. decomposing `investment_revenue` into `dividend_revenue` + `interest_revenue` + `other_investment_revenue`) before adopting the bridge as the canonical mapping layer for the next framework.

This finding will be carried into the Phase 4a.6 closure carry-over for explicit ratification at end-of-Phase-4a.


## Cross-references

- CLAWDOG/113 §6 rung 4a.3 (Phase 4a ladder)
- `memory/2026-05-13-clawdog-113-frs-105-carryover.md` § 4a.3 RULINGS (Q1/Q2/Q3 ratification)
- `memory/uk-taxonomy.md` § Source Artefacts (v1 mapping baseline that informed the candidate list)
- Lesson #41 (prose-vs-code fidelity — fired the requirement for this artefact)
- Lesson #38 (verbatim-claim discipline — the sidecars are the byte-truth)

*— ClawDog ∮*
