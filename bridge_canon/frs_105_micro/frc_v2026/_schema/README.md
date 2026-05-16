# Bridge Fact-Node Schemas

> **Schema directory for `GLOBAL_NOTES/BRIDGE/` Markdown fact-nodes.** Anchors CLAWDOG/113 non-negotiables on the data side: every canonical bridge node validates against one of these schemas before status promotion.

## Schemas (v1)

| Schema | Targets | Mapping kind | Status |
|---|---|---|---|
| `bridge-mapping.schema.json` | `<sbrm_code>.md` files under per-framework/per-version subtrees | `direct_atom` | **canonical** (Phase 4a.1 scaffold; first nodes validated in Phase 4a.2) |
| `bridge-ancestry.schema.json` | `_ancestry_/<ancestor_slug>.md` files | `ancestry_subsume` | **canonical** (Phase 4a.1 scaffold; first nodes validated in Phase 4a.3) |
| `bridge-rollup.schema.json` | `<framework_concept_id>.rollup.md` files | `computed_rollup` | **canonical** (Phase 4a.1 scaffold; first nodes validated in Phase 4a.2 from v1 aggregation parents) |
| `bridge-external-input.schema.json` | `<framework_concept_id>.input.md` files | `external_input` | **canonical** (Phase 4a.1 scaffold; first nodes validated in Phase 4a.2 from v1 boilerplate) |

## Why schemas live here

`GLOBAL_NOTES/BRIDGE/_schema/` (single underscore prefix) keeps schemas adjacent to the data they describe without polluting per-framework listings. The leading underscore sorts it ahead of `frs_105_micro/`, `frs_102_1a_small/`, etc., and signals "infrastructure, not content" by convention. Same pattern as `SBRM_RATE_TABLE/_schema/`.

Future frameworks add their bridge fact-nodes under the existing schemas — schemas are framework-agnostic by design. If a framework needs a structurally different mapping kind, a new schema lands here.

## Validation recipe

Local quick-check against all canonical bridge fact-nodes (run after each Phase 4a rung):

```bash
cd /path/to/clawdog-brain
python3 - <<'PY'
import yaml, json, jsonschema, glob
SCHEMAS = {
    "direct_atom":     json.load(open('GLOBAL_NOTES/BRIDGE/_schema/bridge-mapping.schema.json')),
    "ancestry_subsume":json.load(open('GLOBAL_NOTES/BRIDGE/_schema/bridge-ancestry.schema.json')),
    "computed_rollup": json.load(open('GLOBAL_NOTES/BRIDGE/_schema/bridge-rollup.schema.json')),
    "external_input":  json.load(open('GLOBAL_NOTES/BRIDGE/_schema/bridge-external-input.schema.json')),
}
for path in sorted(glob.glob('GLOBAL_NOTES/BRIDGE/*/*/[!_]*.md') + glob.glob('GLOBAL_NOTES/BRIDGE/*/*/*.rollup.md') + glob.glob('GLOBAL_NOTES/BRIDGE/*/*/*.input.md') + glob.glob('GLOBAL_NOTES/BRIDGE/*/*/_ancestry_/*.md')):
    text = open(path).read()
    if not text.startswith('---'): continue
    fm = yaml.safe_load(text.split('---', 2)[1])
    kind = fm.get('bridge', {}).get('mapping_kind') or fm.get('bridge_ancestry', {}).get('mapping_kind') or fm.get('bridge_rollup', {}).get('mapping_kind') or fm.get('bridge_external_input', {}).get('mapping_kind')
    schema = SCHEMAS.get(kind)
    if schema is None:
        print(f'  ⚠️  {path}: unknown mapping_kind={kind!r}')
        continue
    try:
        jsonschema.validate(fm, schema)
        print(f'  ✅ {path}  ({kind})')
    except jsonschema.ValidationError as e:
        print(f'  ❌ {path}: {e.message}')
PY
```

## Schema evolution

Schemas are versioned at the JSON Schema `$id` URL (`https://lodgeit-labs.org/sbrm/bridge/v1/schema/...`). When a breaking change is needed:

1. Bump the `v1` segment in `$id` to `v2`.
2. Save the new schema alongside the old (e.g. `bridge-mapping.v2.schema.json`).
3. Migrate nodes framework-by-framework — old framework subtrees may stay on v1 indefinitely, since old filings must remain reproducible.
4. Append a `helm_mutations[]` entry on every migrated node.

Do **not** silently mutate a schema in place once any node has been validated against it as `canonical`. Standing Rule #3 applies to schema files as much as to fact-nodes.

## Cross-references

- Sprint design (mapping-kind semantics): [`../../CLAWDOG/113_SBRM_TO_FRAMEWORK_BRIDGE.md`](../../CLAWDOG/113_SBRM_TO_FRAMEWORK_BRIDGE.md) §3
- Bridge canon overview: [`../README.md`](../README.md)
- Sibling pattern (rate tables): [`../../../SBRM_RATE_TABLE/_schema/README.md`](../../../SBRM_RATE_TABLE/_schema/README.md)

*— ClawDog ∮*
