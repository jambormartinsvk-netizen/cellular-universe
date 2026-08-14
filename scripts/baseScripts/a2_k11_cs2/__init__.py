"""Authoritative in-progress base package for A2-K11/K11-CS2.

Heavy historical CAMB/SymPy entry points are resolved lazily.  Lightweight
contract and source-audit submodules must not pay that import cost.
"""

from __future__ import annotations

from importlib import import_module
from typing import Final


_LEGACY_EXPORTS: Final = {
    "BaseStatus",
    "ModelParameters",
    "exact_structural_audit",
    "state_names",
}
__all__ = tuple(sorted(_LEGACY_EXPORTS))


def __getattr__(name: str):
    if name not in _LEGACY_EXPORTS:
        raise AttributeError(name)
    module = import_module(".full_multispecies_constrained_dae", __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value
