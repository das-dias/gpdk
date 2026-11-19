"""Tests for the layer stack material tokens."""

from gpdk.layer_stack import get_layer_stack, get_process
from gpdk.simulation_settings import (
    SIMULATION_SETTINGS_LUMERICAL_FDTD,
    materials_index,
)


def test_layer_stack_material_tokens() -> None:
    """Every layer's material token matches the canonical gsim material names."""
    layer_stack = get_layer_stack()

    assert {name: level.material for name, level in layer_stack.layers.items()} == {
        "substrate": "Si",
        "box": "SiO2",
        "core": "Si",
        "shallow_etch": "Si",
        "deep_etch": "Si",
        "clad": "SiO2",
        "slab150": "Si",
        "slab90": "Si",
        "nitride": "SiN",
        "ge": "Ge",
        "undercut": "Air",
        "via_contact": "Al",
        "metal1": "Al",
        "heater": "TiN",
        "via1": "Al",
        "metal2": "Al",
        "via2": "Al",
        "metal3": "Al",
        "active": "Si",
        "poly": "Si",
        "mim": "TiN",
        "n": "Si",
        "p": "Si",
        "np": "Si",
        "pp": "Si",
        "npp": "Si",
        "ppp": "Si",
        "nwell": "Si",
    }


def test_layer_stack_material_tokens_serialize() -> None:
    """Serialized layer stack uses canonical material tokens."""
    serialized_layers = get_layer_stack().model_dump()["layers"]

    assert serialized_layers["core"]["material"] == "Si"
    assert serialized_layers["box"]["material"] == "SiO2"
    assert serialized_layers["nitride"]["material"] == "SiN"


def test_process_material_tokens() -> None:
    """Process steps use the canonical material tokens."""
    process_materials = {
        step.name: step.material for step in get_process() if hasattr(step, "material")
    }

    assert process_materials == {
        "strip_etch": "Si",
        "slab_etch": "Si",
        "viac_metallization": "Al",
        "viac_etch": "Al",
        "deposit_cladding": "SiO2",
    }


def test_material_registries_include_canonical_optical_tokens() -> None:
    """Material registries include the canonical optical tokens."""
    canonical_optical_materials = {"Si", "SiO2", "SiN"}

    assert canonical_optical_materials <= set(materials_index)
    assert canonical_optical_materials <= set(
        SIMULATION_SETTINGS_LUMERICAL_FDTD.material_name_to_lumerical
    )
    assert SIMULATION_SETTINGS_LUMERICAL_FDTD.background_material == "SiO2"
