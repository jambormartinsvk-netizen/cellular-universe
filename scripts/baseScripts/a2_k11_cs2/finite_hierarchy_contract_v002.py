"""Authoritative K11-CS2/v002 finite-hierarchy contract.

The top rows are registered numerical truncations.  This module deliberately
does not describe any finite-lmax closure as exact physics.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class ContractValidation:
    accepted: bool
    reason: str


def _require_lmax(lmax: int) -> None:
    if not isinstance(lmax, int) or isinstance(lmax, bool) or lmax < 4:
        raise ValueError("lmax must be an integer >= 4")


def authoritative_state(lmax: int) -> tuple[str, ...]:
    _require_lmax(lmax)
    base = (
        "Phi",
        "delta_c", "W_c",
        "delta_f", "W_f",
        "delta_b", "W_b",
        "delta_gamma", "W_gamma",
    )
    photon_temperature = tuple(f"F_gamma_{ell}" for ell in range(2, lmax + 1))
    photon_polarization = tuple(f"E_gamma_{ell}" for ell in range(2, lmax + 1))
    neutrino = ("delta_nu", "W_nu") + tuple(
        f"F_nu_{ell}" for ell in range(2, lmax + 1)
    )
    steam = ("delta_steam", "W_steam") + tuple(
        f"F_steam_{ell}" for ell in range(2, lmax + 1)
    )
    state = base + photon_temperature + photon_polarization + neutrino + steam
    expected = 4 * lmax + 9
    if len(state) != expected or len(set(state)) != expected:
        raise RuntimeError("authoritative K11-CS2 state invariant failed")
    return state


def closure_registry() -> dict[str, dict[str, object]]:
    return {
        "F_gamma": {
            "scheme": "BESSEL_ASYMPTOTIC_NUMERICAL",
            "is_exact_physics": False,
            "requires_lmax_convergence": True,
        },
        "E_gamma": {
            "scheme": "ZERO_TAIL_NUMERICAL",
            "is_exact_physics": False,
            "requires_lmax_convergence": True,
        },
        "F_nu": {
            "scheme": "BESSEL_ASYMPTOTIC_NUMERICAL",
            "is_exact_physics": False,
            "requires_lmax_convergence": True,
        },
        "F_steam": {
            "scheme": "BESSEL_ASYMPTOTIC_NUMERICAL",
            "is_exact_physics": False,
            "requires_lmax_convergence": True,
        },
    }


def validate_contract(
    *, lmax: int, state: Iterable[str], rhs_keys: Iterable[str]
) -> ContractValidation:
    expected = authoritative_state(lmax)
    state_tuple = tuple(state)
    rhs_tuple = tuple(rhs_keys)
    if state_tuple != expected:
        return ContractValidation(False, "STATE_ORDERED_EXACT_SET_MISMATCH")
    if rhs_tuple != expected:
        return ContractValidation(False, "RHS_ORDERED_EXACT_SET_MISMATCH")
    if any(bool(meta["is_exact_physics"]) for meta in closure_registry().values()):
        return ContractValidation(False, "FALSE_EXACT_CLOSURE_CLAIM")
    if not all(
        bool(meta["requires_lmax_convergence"])
        for meta in closure_registry().values()
    ):
        return ContractValidation(False, "MISSING_LMAX_CONVERGENCE_REQUIREMENT")
    return ContractValidation(True, "PASS")

