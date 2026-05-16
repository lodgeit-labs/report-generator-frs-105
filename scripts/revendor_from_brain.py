#!/usr/bin/env python3
"""Re-vendor the bridge canon from a clawdog-brain checkout.

Usage:
    python scripts/revendor_from_brain.py \
        --brain-path /path/to/clawdog-brain/checkout \
        --brain-sha  <40-char-commit-sha>

What it does:
  1. Copies every file from <brain>/GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/**
     into bridge_canon/frs_105_micro/frc_v2026/** (byte-identical).
  2. Copies <brain>/GLOBAL_NOTES/BRIDGE/_schema/*.json into bridge_canon/.../_schema/.
  3. Copies <brain>/memory/sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/*.xsd_excerpt
     into bridge_canon_sidecars/BRIDGE-frs_105_micro-frc_v2026-path_a_v1/.
  4. Rebuilds the Kit wrapper-frontmatter around the lookup artefact body.
  5. Recomputes bridge_canon/MANIFEST.json (sha256 of every vendored file).
  6. Updates src/report_generator_frs_105/_bridge_canon_provenance.py with the
     new SOURCE_BRAIN_CANON_COMMIT.

The CI byte-check gate verifies steps (4) and (5) at PR time.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import shutil
import sys

KIT_ROOT = pathlib.Path(__file__).resolve().parent.parent
# v0.1.1 packaging fix (OT #59): bridge_canon moved into the package data dir
# so it ships in the wheel. All path operations below resolve relative to
# KIT_DATA_ROOT, not KIT_ROOT.
KIT_DATA_ROOT = KIT_ROOT / "src" / "report_generator_frs_105" / "data"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--brain-path", required=True, type=pathlib.Path)
    ap.add_argument("--brain-sha", required=True)
    args = ap.parse_args()

    brain = args.brain_path
    if not (brain / "GLOBAL_NOTES" / "BRIDGE").is_dir():
        print(f"❌ {brain} does not look like a clawdog-brain checkout", file=sys.stderr)
        return 1
    if len(args.brain_sha) != 40:
        print("❌ --brain-sha must be a 40-char commit hash", file=sys.stderr)
        return 1

    src_dir = brain / "GLOBAL_NOTES" / "BRIDGE" / "frs_105_micro" / "frc_v2026"
    dst_dir = KIT_DATA_ROOT / "bridge_canon" / "frs_105_micro" / "frc_v2026"

    # 1. wipe and re-copy
    if dst_dir.exists():
        shutil.rmtree(dst_dir)
    dst_dir.mkdir(parents=True)
    (dst_dir / "_ancestry_").mkdir()
    (dst_dir / "_schema").mkdir()

    for p in src_dir.iterdir():
        if p.is_dir() and p.name == "_ancestry_":
            for f in p.iterdir():
                shutil.copy2(f, dst_dir / "_ancestry_" / f.name)
        elif p.is_file() and p.name != "_path_a_v1_lookup_2026-05-15.md":
            shutil.copy2(p, dst_dir / p.name)

    # 2. schemas
    schema_src = brain / "GLOBAL_NOTES" / "BRIDGE" / "_schema"
    for f in schema_src.iterdir():
        if f.is_file():
            shutil.copy2(f, dst_dir / "_schema" / f.name)

    # 3. sidecars
    sc_src = brain / "memory" / "sidecars" / "BRIDGE-frs_105_micro-frc_v2026-path_a_v1"
    sc_dst = KIT_DATA_ROOT / "bridge_canon_sidecars" / "BRIDGE-frs_105_micro-frc_v2026-path_a_v1"
    if sc_dst.exists():
        shutil.rmtree(sc_dst)
    sc_dst.mkdir(parents=True)
    for f in sc_src.iterdir():
        if f.is_file():
            shutil.copy2(f, sc_dst / f.name)

    # 4. lookup artefact wrapper
    brain_lookup = src_dir / "_path_a_v1_lookup_2026-05-15.md"
    body_bytes = brain_lookup.read_bytes()
    body_hash = hashlib.sha256(body_bytes).hexdigest()
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    wrapper = (
        "---\n"
        "kit_vendor_wrapper:\n"
        f'  source_brain_repo:         "github.com/futureWA/clawdog-brain"\n'
        f'  source_brain_canon_commit: "{args.brain_sha}"\n'
        '  source_brain_path:         "GLOBAL_NOTES/BRIDGE/frs_105_micro/frc_v2026/_path_a_v1_lookup_2026-05-15.md"\n'
        f'  vendored_at_utc:           "{now}"\n'
        f'  body_sha256:               "{body_hash}"\n'
        f'  body_bytes:                {len(body_bytes)}\n'
        "  notes: |\n"
        "    Kit-side wrapper around byte-identical Brain canon body. The body below\n"
        "    the closing '---' marker is a verbatim byte-copy from Brain; body_sha256\n"
        "    above is the SHA-256 of those bytes. Kit-CI byte-check gate enforces\n"
        "    no drift. Pattern precedent: lodgeit-labs/clawdog/docs/INTEGRATOR_README.md.\n"
        "---\n"
    )
    (dst_dir / "_path_a_v1_lookup_2026-05-15.md").write_bytes(wrapper.encode("utf-8") + body_bytes)

    # 5. MANIFEST
    entries = []
    for root in (KIT_DATA_ROOT / "bridge_canon", KIT_DATA_ROOT / "bridge_canon_sidecars"):
        for p in sorted(root.rglob("*")):
            if not p.is_file() or p.name == "MANIFEST.json":
                continue
            # MANIFEST paths are KIT_DATA_ROOT-relative (e.g. "bridge_canon/...").
            # The byte-fidelity test resolves them against KIT_DATA_ROOT. Writing
            # KIT_ROOT-relative paths here yielded "src/report_generator_frs_105/
            # data/bridge_canon/..." entries which the test then double-nested
            # against KIT_DATA_ROOT and reported as missing (C2 bug discovery,
            # 2026-05-16). Aligning with v0.1.1 MANIFEST shape + test resolver.
            rel = p.relative_to(KIT_DATA_ROOT).as_posix()
            h = hashlib.sha256(p.read_bytes()).hexdigest()
            entries.append({"path": rel, "sha256": h, "bytes": p.stat().st_size})
    manifest = {
        "kit": "lodgeit-labs/report-generator-frs-105",
        "source_brain_repo": "github.com/futureWA/clawdog-brain",
        "source_brain_canon_commit": args.brain_sha,
        "vendor_strategy": "byte-copy (D4.2=b) + Kit-CI byte-check gate (CLAWDOG/141 precedent)",
        "note": "Each vendored file is byte-identical to its source in clawdog-brain at the declared commit. The lookup artefact carries a Kit wrapper-frontmatter; its sha256 here covers the full wrapped file. All other files are unwrapped byte-copies.",
        "files": entries,
    }
    (KIT_DATA_ROOT / "bridge_canon" / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n"
    )

    # 6. provenance module
    prov_path = KIT_ROOT / "src" / "report_generator_frs_105" / "_bridge_canon_provenance.py"
    prov_text = prov_path.read_text()
    import re
    prov_text = re.sub(
        r'SOURCE_BRAIN_CANON_COMMIT = ".+?"',
        f'SOURCE_BRAIN_CANON_COMMIT = "{args.brain_sha}"',
        prov_text,
    )
    prov_path.write_text(prov_text)

    print(f"✅ Re-vendored {len(entries)} files from clawdog-brain@{args.brain_sha[:8]}")
    print(f"   bridge_canon/MANIFEST.json refreshed")
    print(f"   Run: python -m pytest tests/ -v")
    return 0


if __name__ == "__main__":
    sys.exit(main())
