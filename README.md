# gpdk 0.0.1

The generic PDK for [gdsfactory](https://github.com/gdsfactory/gdsfactory), packaged as a
standalone PDK.

`gpdk` wraps every generic gdsfactory cell as a PDK cell, and owns the generic technology
(layers, layer stack, layer views, KLayout assets). It is the reference shape for other PDKs.

## Installation

    pip install gpdk

## Usage

    import gpdk

    gpdk.PDK.activate()
    c = gpdk.cells.straight(length=20)
    c.show()

## Cell library

`gpdk/cells/` is generated from the pinned gdsfactory version and is not hand-edited.
See `make cells-check` and `make cells-regen`.

## Simulation materials

The layer stack uses canonical material names (for example, `Si`, `SiO2`, and
`SiN`). Use those names for explicit solver overrides. The index and Lumerical
lookup dictionaries also accept the old `si`, `sio2`, and `sin` keys.

The project silicon card used by gsim is valid from 1.357 to 11.04 µm. This is
not an O-band material model. A material name in the stack does not guarantee
that a matching optical model is available for that solver.
