# Changelog

All notable changes to `report-generator-frs-105` are documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] — 2026-05-16 — F1 bridge-canon factual correction (mc14)

### Fixed

- **F1 namespace correction:** `DateAuthorisationFinancialStatementsForIssue` was vendored
  with `framework_concept: "uk-bus:..."` in v0.1.1. A wire-anchored audit of the FRC v2026
  taxonomy XSDs on 2026-05-16 proved the element is declared exactly once at
  `frc-core-2026-01-01.xsd:2091` in the `uk-core:` namespace. This release re-vendors
  against the corrected Brain canon (Brain PR #212, `mut-2026-05-16-mc14-factual-correction`).
  Concrete change at the atom layer: `framework_concept: "uk-bus:DateAuthorisationFinancialStatementsForIssue"`
  → `"uk-core:DateAuthorisationFinancialStatementsForIssue"`; Brain `content_hash`
  `3dfcdd2c…` → `c86051ac…`.
- **`scripts/revendor_from_brain.py` MANIFEST path discipline:** the script wrote
  MANIFEST entries with `KIT_ROOT`-relative paths (e.g. `src/report_generator_frs_105/data/bridge_canon/...`)
  while the byte-fidelity test resolves entries against `KIT_DATA_ROOT`. The script
  now writes `KIT_DATA_ROOT`-relative paths (e.g. `bridge_canon/...`), matching the
  v0.1.1 MANIFEST shape and the test resolver. This defect was masked in v0.1.1
  because the v0.1.1 MANIFEST was authored by hand; the first revendor run after
  packaging (post-OT #59) would have surfaced it.

### Changed

- **README "Cautionary case study" section:** updated from v0.1.1's forward-looking
  state ("v0.1.2 will re-vendor against this corrected canon") to v0.1.2's historical
  state ("vendored into this release at Brain commit `a1f6dfa5…`"). Lessons #40
  (mc14-refined) + #41 referenced.
- **README "Provenance" block:** source commit bumped
  `2fc7451a3068c69d726a2159cced4254fad2187c` (pre-mc14) → `a1f6dfa5e531d4d6c3f6df2a50a32765835017ab`
  (post-mc14, Brain PR #212 merge).
- **`tests/test_bridge_canon_byte_fidelity.py::test_manifest_exists`:** the pinned
  `source_brain_canon_commit` assertion bumped to `a1f6dfa5…` to match the new
  vendor. Both prior and current commits are documented inline in the test so
  future revendor cycles know what to update together.

### Recommendation for integrators

- **Pin `report-generator-frs-105>=0.1.2`.** v0.1.0 (silent-packaging) and v0.1.1
  (inverted F1 namespace) are superseded.
- Downstream consumers of v0.1.1 emitting iXBRL for
  `DateAuthorisationFinancialStatementsForIssue` will need to re-pin to v0.1.2 and
  re-render. The 1-byte namespace flip at the template-resolve site is the only
  change visible at the rendered iXBRL layer.

### Forensic chronicle

- `clawdog-brain/memory/2026-05-16.md` — Phase A wire-audit + mc14 helm-roll
  execution; the Tracer hallucinated-procedural-state-injection incident that
  surfaced the F1 defect.
- `clawdog-brain/memory/lessons.md` § Lesson #40 — n=3 datapoint refining the
  canonical statement: *internal byte-identity between two paths is not external
  regulator-shape correctness*.

## [0.1.1] — 2026-05-16 (early) — Packaging fix (OT #59) + v1-bug case study (OT #60) — **SUPERSEDED**

### Fixed

- **OT #59 packaging fix:** vendored `bridge_canon/` and `bridge_canon_sidecars/`
  moved into `src/report_generator_frs_105/data/` so the wheel actually ships them.
  v0.1.0 silently dropped the canon because it lived at repo root and was outside
  the package data dir.

### Added (forensic record only — see v0.1.2 corrections)

- **README "✅ Real bug this Kit caught" case study (OT #60):** *this section
  framed the namespace direction backwards and was corrected in v0.1.2.* See
  v0.1.2 changelog entry above and the README "Cautionary case study" section.

### Status

**Superseded by v0.1.2.** Do not pin v0.1.1 for new integrations.

## [0.1.0] — 2026-05-15 — Initial Kit scaffold + bridge canon vendor (Phase 4a.4 Subagent A) — **SUPERSEDED**

### Added

- Initial Kit scaffold under Apache-2.0 licence.
- 40-node bridge canon vendored from `clawdog-brain` at commit
  `2fc7451a3068c69d726a2159cced4254fad2187c`.
- Resolver library (`resolve_concept`, friends).
- Two-gate Kit-CI (Gate 1 resolver unit tests + Gate 2 bridge-canon byte-fidelity).

### Status

**Superseded by v0.1.1.** v0.1.0 had a silent packaging defect that prevented the
wheel from shipping the vendored bridge canon.

*— ClawDog ∮*
