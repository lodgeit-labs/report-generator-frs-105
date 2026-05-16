"""report_generator_frs_105 — Egress-Interface Kit.

Projects clawdog-brain Phase 4a.3 bridge canon for FRS 105 Micro × FRC v2026.
Deterministic LodgeiT-SBRM-slug → FRC-element resolver library + CLI.

Apache-2.0. See LICENSE.
"""
from .resolver import (
    ResolvedConcept,
    UnknownSlugError,
    ExternalInputRequired,
    AmbiguousResolutionError,
    resolve_concept,
    list_slugs,
    bridge_canon_root,
)
from ._bridge_canon_provenance import (
    SOURCE_BRAIN_REPO,
    SOURCE_BRAIN_CANON_COMMIT,
    VENDOR_STRATEGY,
)

__version__ = "0.1.0"

__all__ = [
    "ResolvedConcept",
    "UnknownSlugError",
    "ExternalInputRequired",
    "AmbiguousResolutionError",
    "resolve_concept",
    "list_slugs",
    "bridge_canon_root",
    "SOURCE_BRAIN_REPO",
    "SOURCE_BRAIN_CANON_COMMIT",
    "VENDOR_STRATEGY",
    "__version__",
]
