"""Tests for PDK technology parity with gdsfactory core's generic PDK."""

import gpdk


def test_pdk_exposes_materials_index():
    """The PDK passes materials_index through to the Pdk."""
    assert gpdk.PDK.materials_index
    assert "Si" in gpdk.PDK.materials_index


def test_pdk_splits_containers_from_cells():
    """Container cells are registered under containers, not cells."""
    assert gpdk.PDK.containers
    assert "pack_doe" in gpdk.PDK.containers
    assert "pack_doe" not in gpdk.PDK.cells


def test_pdk_exposes_material_cards() -> None:
    """The PDK carries its project material cards for gsim."""
    assert gpdk.PDK.material_cards is gpdk.MATERIAL_CARDS
