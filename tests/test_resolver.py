"""Unit tests for resolve_concept against the production vendored bundle.

Standing Rule #12 — tests run against the actual vendored canon, not a
hermetic fixture. Mirrors `lodgeit-labs/clawdog-calculator-api/tests/test_production_bundle.py`.
"""
import pytest

from report_generator_frs_105 import (
    ExternalInputRequired,
    ResolvedConcept,
    UnknownSlugError,
    list_slugs,
    resolve_concept,
)


def test_direct_atom_sbrm_4101():
    rc = resolve_concept("sbrm_4101")
    assert isinstance(rc, ResolvedConcept)
    assert rc.framework_concept == "uk-core:TurnoverRevenue"
    assert rc.mapping_kind == "direct_atom"
    assert rc.statement_role == "PL_REVENUE"
    assert rc.confidence == "high"
    assert rc.source_node_path.endswith("sbrm-4101.md")
    assert len(rc.source_content_hash) == 64


def test_direct_atom_hyphen_alias():
    # CLI passes "sbrm-4101"; API should normalise.
    rc = resolve_concept("sbrm-4101")
    assert rc.framework_concept == "uk-core:TurnoverRevenue"


def test_computed_rollup_equity():
    rc = resolve_concept("equity")
    # Precedence: ancestry_subsume wins over rollup when ancestor_slug matches.
    # Both resolve to uk-core:Equity but with different mapping_kind.
    assert rc.framework_concept == "uk-core:Equity"
    assert rc.mapping_kind in ("computed_rollup", "ancestry_subsume")


def test_ancestry_subsume_share_capital():
    rc = resolve_concept("share_capital")
    assert rc.mapping_kind == "ancestry_subsume"
    assert rc.framework_concept == "uk-core:ShareCapital"
    assert rc.statement_role == "EQUITY"


def test_external_input_does_not_raise_by_default():
    rc = resolve_concept("end-date-for-period-covered-by-report")
    assert rc.mapping_kind == "external_input"
    assert rc.framework_concept == "uk-bus:EndDateForPeriodCoveredByReport"


def test_external_input_raises_when_flag_set():
    with pytest.raises(ExternalInputRequired):
        resolve_concept(
            "end-date-for-period-covered-by-report",
            raise_on_external_input=True,
        )


def test_unknown_slug_raises():
    with pytest.raises(UnknownSlugError):
        resolve_concept("definitely_not_a_slug_xxxxx")


def test_to_json_roundtrip():
    rc = resolve_concept("sbrm_4101")
    import json
    payload = json.loads(rc.to_json())
    assert payload["framework_concept"] == "uk-core:TurnoverRevenue"
    assert payload["mapping_kind"] == "direct_atom"


def test_list_slugs_shape():
    listing = list_slugs()
    # 12 direct_atom sbrm fact-nodes, 11 ancestor slugs, computed_rollups + inputs share by_concept_slug
    assert len(listing["direct_atom_sbrm_codes"]) == 12
    assert len(listing["ancestor_slugs"]) == 11
    assert "equity" in listing["ancestor_slugs"]
    assert "sbrm_4101" in listing["direct_atom_sbrm_codes"]


def test_dimensional_axis_reserved_field():
    """The dimensional_axis field is None today (Hyperplane Mismatch unfixed)."""
    rc = resolve_concept("sbrm_4101")
    assert rc.dimensional_axis is None
