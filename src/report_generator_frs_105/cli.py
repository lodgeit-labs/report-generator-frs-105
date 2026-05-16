"""CLI: ``python -m report_generator_frs_105 resolve <slug>``."""
from __future__ import annotations

import argparse
import json
import sys

from . import __version__
from ._bridge_canon_provenance import SOURCE_BRAIN_CANON_COMMIT, SOURCE_BRAIN_REPO
from .resolver import (
    AmbiguousResolutionError,
    ExternalInputRequired,
    UnknownSlugError,
    list_slugs,
    resolve_concept,
)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="report-generator-frs-105",
        description=(
            "Resolve LodgeiT SBRM slugs to FRC v2026 framework concepts via the "
            "vendored clawdog-brain bridge canon."
        ),
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_resolve = sub.add_parser("resolve", help="Resolve a slug")
    p_resolve.add_argument("slug")
    p_resolve.add_argument("--framework", default="frs_105_micro")
    p_resolve.add_argument("--taxonomy-version", default="frc_v2026")
    p_resolve.add_argument("--period", default="ongoing")
    p_resolve.add_argument(
        "--raise-on-external-input", action="store_true",
        help="Exit 3 if the slug resolves to an external_input node.",
    )

    p_list = sub.add_parser("list", help="List available slugs")
    p_list.add_argument("--framework", default="frs_105_micro")
    p_list.add_argument("--taxonomy-version", default="frc_v2026")

    p_prov = sub.add_parser("provenance", help="Print vendored Brain provenance")

    args = parser.parse_args(argv)

    if args.cmd == "resolve":
        try:
            rc = resolve_concept(
                args.slug, args.framework, args.taxonomy_version, args.period,
                raise_on_external_input=args.raise_on_external_input,
            )
        except UnknownSlugError as exc:
            print(json.dumps({"error": "unknown_slug", "detail": str(exc)}), file=sys.stderr)
            return 2
        except ExternalInputRequired as exc:
            print(json.dumps({"error": "external_input_required", "detail": str(exc)}), file=sys.stderr)
            return 3
        except AmbiguousResolutionError as exc:
            print(json.dumps({"error": "ambiguous", "detail": str(exc)}), file=sys.stderr)
            return 4
        print(rc.to_json())
        return 0

    if args.cmd == "list":
        print(json.dumps(list_slugs(args.framework, args.taxonomy_version), indent=2))
        return 0

    if args.cmd == "provenance":
        print(json.dumps({
            "source_brain_repo": SOURCE_BRAIN_REPO,
            "source_brain_canon_commit": SOURCE_BRAIN_CANON_COMMIT,
            "kit_version": __version__,
        }, indent=2))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
