"""Tests for PDK technology parity with gdsfactory core's generic PDK."""

import pytest
from pydantic import ValidationError

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
    assert gpdk.PDK.material_cards == gpdk.MATERIAL_CARDS


def test_pdk_material_cards_survive_copy_and_dump() -> None:
    """Cards are declared data, not an unserialized runtime attribute."""
    card = gpdk.MATERIAL_CARDS["Si"]
    for pdk in (gpdk.PDK, gpdk.PDK.model_copy()):
        assert pdk.material_cards["Si"] == card
        assert pdk.model_dump(include={"material_cards"}) == {
            "material_cards": {"Si": card.model_dump()}
        }


def test_pdk_rejects_invalid_material_card() -> None:
    """Reject invalid cards before publishing the PDK to a simulator."""
    with pytest.raises(ValidationError):
        type(gpdk.PDK)(name="invalid", material_cards={"Si": {"name": "Si"}})
