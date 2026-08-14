"""Exact S0/S1 identities for the G8 full-hierarchy route.

This module intentionally contains no ODE solver.  It is the shared algebraic
authority for the bounded G8 scripts 221--225.
"""

from __future__ import annotations

from pathlib import Path
import sys
import time
from typing import Callable

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
LOCAL_DEPS = ROOT / ".deps" / "python"
if LOCAL_DEPS.exists() and str(LOCAL_DEPS) not in sys.path:
    sys.path.insert(0, str(LOCAL_DEPS))

import camb  # noqa: E402
import camb.symbolic as cs  # noqa: E402


def state_names(lmax: int) -> tuple[str, ...]:
    """Return the frozen full-G8 state order, failing closed for bad lmax."""
    if not isinstance(lmax, int) or lmax < 2:
        raise ValueError("lmax must be an integer >= 2")
    base = (
        "h", "eta", "delta_gamma", "D", "delta_b", "delta_c",
        "U_gamma", "U_b", "M", "delta_f", "U_f",
    )
    multipoles = tuple(
        name for family in ("J", "E", "G")
        for ell in range(2, lmax + 1) for name in (f"{family}_{ell}",)
    )
    names = base + multipoles
    if len(names) != 3 * lmax + 8 or len(set(names)) != len(names):
        raise RuntimeError("G8 state register invariant failed")
    return names


def _brightness(name: str, ell: int):
    if name == "J":
        if ell == 1:
            return cs.q_g
        if ell == 2:
            return cs.pi_g
    if name == "G":
        if ell == 1:
            return cs.q_r
        if ell == 2:
            return cs.pi_r
    return cs._make_index_func(name, ell)


def _j_expected(ell: int):
    current = _brightness("J", ell)
    previous = _brightness("J", ell - 1)
    following = _brightness("J", ell + 1)
    rhs = -cs.k / (2 * ell + 1) * (
        (ell + 1) * cs.Kf[ell] * following - ell * previous
    ) - cs.opacity * current
    if ell == 2:
        rhs += sp.Rational(8, 15) * cs.k * cs.sigma + cs.opacity * cs.polter
    return sp.simplify(rhs)


def _g_expected(ell: int):
    current = _brightness("G", ell)
    previous = _brightness("G", ell - 1)
    following = _brightness("G", ell + 1)
    rhs = -cs.k / (2 * ell + 1) * (
        (ell + 1) * cs.Kf[ell] * following - ell * previous
    )
    if ell == 2:
        rhs += sp.Rational(8, 15) * cs.k * cs.sigma
    return sp.simplify(rhs)


def _e_expected(ell: int):
    current = cs._make_index_func("E", ell)
    previous = 0 if ell == 2 else cs._make_index_func("E", ell - 1)
    following = cs._make_index_func("E", ell + 1)
    rhs = -cs.k / (2 * ell + 1) * (
        (ell + 3) * (ell - 1) * cs.Kf[ell] * following / (ell + 1)
        - ell * previous
    ) - cs.opacity * current
    if ell == 2:
        rhs += cs.polter * cs.opacity
    return sp.simplify(rhs)


def _zero(value: sp.Expr) -> tuple[bool, str]:
    residual = sp.simplify(value)
    return bool(residual == 0), str(residual)


def _record(checks: dict[str, bool], residuals: dict[str, str], name: str,
            expression: sp.Expr) -> None:
    passed, residual = _zero(expression)
    checks[name] = passed
    residuals[name] = residual


def _deadline(started: float, seconds: float) -> None:
    if time.monotonic() - started > seconds:
        raise TimeoutError("G8 structural audit internal deadline exceeded")


def exact_s0_s1_audit(max_runtime_seconds: float) -> dict[str, object]:
    """Run exact CAMB provenance and K7-reduction identities only."""
    if not (0.0 < max_runtime_seconds <= 20.0):
        raise ValueError("max_runtime_seconds must be in (0, 20]")
    started = time.monotonic()
    checks: dict[str, bool] = {}
    residuals: dict[str, str] = {}

    for ell in range(2, 9):
        _deadline(started, max_runtime_seconds)
        _record(checks, residuals, f"CAMB_J_l{ell}", cs.J_eq(ell).rhs - _j_expected(ell))
        _record(checks, residuals, f"CAMB_G_l{ell}", cs.G_eq(ell).rhs - _g_expected(ell))
        _record(checks, residuals, f"CAMB_E_l{ell}", cs.E_eq(ell).rhs - _e_expected(ell))
    expected_polter = sp.Rational(2, 15) * (
        sp.Rational(3, 4) * cs.pi_g + sp.Rational(9, 2) * cs.E_2
    )
    _record(checks, residuals, "CAMB_polarization_source", cs.polter_sub.rhs - expected_polter)
    _deadline(started, max_runtime_seconds)

    for lmax, expected_count in ((8, 32), (12, 44), (16, 56)):
        names = state_names(lmax)
        checks[f"state_count_lmax_{lmax}"] = len(names) == expected_count
        checks[f"state_order_unique_lmax_{lmax}"] = len(names) == len(set(names))
        checks[f"state_endpoints_lmax_{lmax}"] = (
            names[:11] == (
                "h", "eta", "delta_gamma", "D", "delta_b", "delta_c",
                "U_gamma", "U_b", "M", "delta_f", "U_f",
            ) and names[11] == "J_2" and names[-1] == f"G_{lmax}"
        )
        residuals[f"state_count_lmax_{lmax}"] = str(len(names) - expected_count)
        residuals[f"state_order_unique_lmax_{lmax}"] = "0" if checks[f"state_order_unique_lmax_{lmax}"] else "duplicate"
        residuals[f"state_endpoints_lmax_{lmax}"] = "0" if checks[f"state_endpoints_lmax_{lmax}"] else "wrong_order"

    q, s2, sigma, L3, L4, L5 = sp.symbols("q s2 sigma L3 L4 L5")
    def scaled_collisionless(ell: int, previous: sp.Expr, current: sp.Expr,
                             following: sp.Expr) -> sp.Expr:
        return (-(ell - 2) * q * current
                + sp.Rational(ell, 2 * ell + 1) * s2 * previous
                - sp.Rational(ell + 1, 2 * ell + 1) * following)

    k7_l3 = -q * L3 + sp.Rational(6, 7) * s2 * sigma - sp.Rational(4, 7) * L4
    general_l3 = scaled_collisionless(3, 2 * sigma, L3, L4)
    _record(checks, residuals, "K7_l3_general_recurrence", general_l3 - k7_l3)
    k7_l4_with_l5 = -2 * q * L4 + sp.Rational(4, 9) * s2 * L3 - sp.Rational(5, 9) * L5
    general_l4 = scaled_collisionless(4, L3, L4, L5)
    _record(checks, residuals, "K7_l4_general_recurrence", general_l4 - k7_l4_with_l5)
    _record(checks, residuals, "K7_l4_registered_L5_zero_limit",
            general_l4.subs(L5, 0) - (-2 * q * L4 + sp.Rational(4, 9) * s2 * L3))

    U_gamma, U_b, delta_gamma, delta_b, kappa, R, c_b2 = sp.symbols(
        "U_gamma U_b delta_gamma delta_b kappa R c_b2", nonzero=True
    )
    photon_collision = kappa * (U_b - U_gamma)
    baryon_collision = kappa / R * (U_gamma - U_b)
    _record(checks, residuals, "Thomson_weighted_momentum_cancellation",
            photon_collision + R * baryon_collision)
    _record(checks, residuals, "Thomson_interaction_zero_limit",
            photon_collision.subs(U_b, U_gamma))

    photon_euler = q * U_gamma + delta_gamma / 4 - sp.symbols("sigma_gamma") + photon_collision
    baryon_euler = (q - 1) * U_b + c_b2 * delta_b + baryon_collision
    combined = sp.simplify((photon_euler + R * baryon_euler) / (1 + R))
    tight_limit = sp.simplify(combined.subs({U_b: U_gamma, sp.symbols("sigma_gamma"): 0, c_b2: 0}))
    k7_euler = q * U_gamma - R / (1 + R) * U_gamma + delta_gamma / (4 * (1 + R))
    _record(checks, residuals, "separate_photon_baryon_to_K7_combined_Euler", tight_limit - k7_euler)
    load_fraction, inv1r = sp.symbols("load_fraction inv1r")
    _record(checks, residuals, "combined_Euler_to_K7_background_notation",
            k7_euler.subs({R / (1 + R): load_fraction, 1 / (1 + R): inv1r})
            - (q * U_gamma - load_fraction * U_gamma + delta_gamma * inv1r / 4))
    _record(checks, residuals, "separate_continuity_to_K7_baryon",
            (-s2 * U_b - sp.symbols("h_x") / 2).subs(U_b, U_gamma)
            - (-s2 * U_gamma - sp.symbols("h_x") / 2))

    Og, On, Ob, Of, U_fs, U_f, M = sp.symbols("Og On Ob Of U_fs U_f M", nonzero=True)
    delta = sp.symbols("delta", nonzero=True)
    full_momentum = 2 * Og * U_gamma + sp.Rational(3, 2) * Ob * U_b + 2 * On * U_fs + sp.Rational(3, 2) * delta * Of * U_f
    k7_momentum = 2 * Og * U_gamma + sp.Rational(3, 2) * Ob * U_gamma + 2 * On * U_fs + sp.Rational(3, 2) * delta * Of * U_f
    _record(checks, residuals, "full_M_to_K7_projected_mapping", full_momentum.subs(U_b, U_gamma) - k7_momentum)
    _deadline(started, max_runtime_seconds)

    passed = all(checks.values())
    return {
        "test": "A2-K4 C7.7c K7 G8 SCREEN-S0+S1 exact structural algebra audit",
        "CAMB_version": camb.__version__,
        "physics_executed": False,
        "ode_executed": False,
        "score_effect": 0,
        "state_count_formula": "3*lmax+8",
        "state_counts": {str(lmax): len(state_names(lmax)) for lmax in (8, 12, 16)},
        "exact_check_count": len(checks),
        "checks": checks,
        "symbolic_residuals": residuals,
        "verdict": "PASS_G8_SCREEN_S0_S1_STRUCTURAL" if passed else "STOP_G8_IMPLEMENTATION_MAPPING",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
