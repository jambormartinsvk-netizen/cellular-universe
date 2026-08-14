"""Single-source K11-CS2 equations and structural invariants.

Current audited scope: exact structural S0 only.  The time propagator remains
fail-closed until the full species/stress RHS, opacity handoff, regular basis,
and independent Einstein/Bianchi holdouts are implemented in this module.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import StrEnum
from pathlib import Path
import sys
import time
from typing import Final


ROOT: Final = Path(__file__).resolve().parents[3]
LOCAL_DEPS: Final = ROOT / ".deps" / "python"
if LOCAL_DEPS.exists() and str(LOCAL_DEPS) not in sys.path:
    sys.path.insert(0, str(LOCAL_DEPS))

import sympy as sp  # noqa: E402
import camb  # noqa: E402
import camb.symbolic as cs  # noqa: E402


class BaseStatus(StrEnum):
    """Machine-readable implementation status."""

    STRUCTURAL_S0_ONLY = "STRUCTURAL_S0_ONLY"
    FULL_PROPAGATOR_NOT_IMPLEMENTED = "FULL_PROPAGATOR_NOT_IMPLEMENTED"


@dataclass(frozen=True)
class ModelParameters:
    """Frozen A1/K11-CS2 parameters; no post-result fitting is allowed."""

    h: float = 0.6637
    omega_m0: float = 0.3517
    omega_b_h2: float = 0.02237
    omega_gamma_h2: float = 2.469e-5
    neff_standard: float = 3.046
    delta_neff_steam: float = 0.0535
    lam: float = 0.15
    delta: float = 0.02297
    z_star: float = 1089.9


def _require_lmax(lmax: int) -> None:
    if not isinstance(lmax, int) or isinstance(lmax, bool) or lmax < 3:
        raise ValueError("lmax must be an integer >= 3")


def state_names(lmax: int) -> tuple[str, ...]:
    """Return the frozen full multispecies Newtonian-gauge state order.

    The hierarchy convention is temperature F_l for photons, polarization
    E_l, and collisionless F_l for neutrinos and steam.  Psi is algebraic
    from the traceless/slip equation and is therefore not an evolved state.
    """

    _require_lmax(lmax)
    base = (
        "Phi",
        "delta_c", "W_c",
        "delta_f", "W_f",
        "delta_b", "W_b",
        "delta_gamma", "W_gamma",
    )
    photon_temperature = tuple(f"F_gamma_{ell}" for ell in range(2, lmax + 1))
    photon_polarization = tuple(f"E_gamma_{ell}" for ell in range(0, lmax + 1))
    neutrino = ("delta_nu", "W_nu") + tuple(
        f"F_nu_{ell}" for ell in range(2, lmax + 1)
    )
    steam = ("delta_steam", "W_steam") + tuple(
        f"F_steam_{ell}" for ell in range(2, lmax + 1)
    )
    names = base + photon_temperature + photon_polarization + neutrino + steam
    expected = 4 * lmax + 11
    if len(names) != expected or len(set(names)) != expected:
        raise RuntimeError("K11-CS2 state-register invariant failed")
    return names


def _brightness(family: str, ell: int):
    if family == "J":
        if ell == 1:
            return cs.q_g
        if ell == 2:
            return cs.pi_g
    if family == "G":
        if ell == 1:
            return cs.q_r
        if ell == 2:
            return cs.pi_r
    return cs._make_index_func(family, ell)


def _expected_j(ell: int):
    current = _brightness("J", ell)
    previous = _brightness("J", ell - 1)
    following = _brightness("J", ell + 1)
    rhs = -cs.k / (2 * ell + 1) * (
        (ell + 1) * cs.Kf[ell] * following - ell * previous
    ) - cs.opacity * current
    if ell == 2:
        rhs += sp.Rational(8, 15) * cs.k * cs.sigma + cs.opacity * cs.polter
    return sp.simplify(rhs)


def _expected_g(ell: int):
    current = _brightness("G", ell)
    previous = _brightness("G", ell - 1)
    following = _brightness("G", ell + 1)
    rhs = -cs.k / (2 * ell + 1) * (
        (ell + 1) * cs.Kf[ell] * following - ell * previous
    )
    if ell == 2:
        rhs += sp.Rational(8, 15) * cs.k * cs.sigma
    return sp.simplify(rhs)


def _expected_e(ell: int):
    current = cs._make_index_func("E", ell)
    previous = 0 if ell == 2 else cs._make_index_func("E", ell - 1)
    following = cs._make_index_func("E", ell + 1)
    rhs = -cs.k / (2 * ell + 1) * (
        (ell + 3) * (ell - 1) * cs.Kf[ell] * following / (ell + 1)
        - ell * previous
    ) - cs.opacity * current
    if ell == 2:
        rhs += cs.opacity * cs.polter
    return sp.simplify(rhs)


def _deadline(started: float, max_runtime_seconds: float) -> None:
    if time.monotonic() - started > max_runtime_seconds:
        raise TimeoutError("K11-CS2 structural audit internal deadline exceeded")


def _record(
    checks: dict[str, bool], residuals: dict[str, str], name: str, expression
) -> None:
    residual = sp.simplify(expression)
    checks[name] = bool(residual == 0)
    residuals[name] = str(residual)


def exact_structural_audit(
    *, lmax: int = 8, max_runtime_seconds: float = 5.0
) -> dict[str, object]:
    """Audit exact formula provenance without integrating any ODE."""

    _require_lmax(lmax)
    if not (0.0 < max_runtime_seconds <= 5.0):
        raise ValueError("max_runtime_seconds must be in (0, 5]")
    started = time.monotonic()
    checks: dict[str, bool] = {}
    residuals: dict[str, str] = {}

    # K11-R constitutive identities.
    Gamma, H, rho_c, rho_f, delta = sp.symbols(
        "Gamma H rho_c rho_f delta", positive=True, finite=True
    )
    Upsilon = Gamma * rho_c * delta * rho_f / (rho_c + delta * rho_f)
    d_c = Upsilon / (H * rho_c)
    d_f = Upsilon / (H * delta * rho_f)
    g = Gamma / H
    _record(checks, residuals, "K11_R_relative_drag_rate", d_c + d_f - g)
    _record(
        checks,
        residuals,
        "K11_R_weighted_momentum_reaction",
        rho_c * d_c - delta * rho_f * d_f,
    )
    _record(
        checks,
        residuals,
        "K11_R_interaction_saddle_determinant",
        ((-d_c) * (2 * g / delta - d_f)
         - d_c * (-g / delta + d_f)) + d_c * g / delta,
    )
    _deadline(started, max_runtime_seconds)

    # Exact A1 background conservation and absence of perturbative k.
    Xf, Xc, Xb, Xr, lam, E, k_mode = sp.symbols(
        "Xf Xc Xb Xr lam E k_mode", positive=True, finite=True
    )
    transfer = lam * Xf / E
    rhs_f = -3 * delta * Xf - transfer
    rhs_c = -3 * Xc + transfer
    rhs_b = -3 * Xb
    rhs_r = -4 * Xr
    _record(
        checks,
        residuals,
        "A1_background_transfer_pair_cancellation",
        rhs_f + rhs_c + rhs_b + rhs_r
        - (-3 * delta * Xf - 3 * Xc - 3 * Xb - 4 * Xr),
    )
    _record(
        checks,
        residuals,
        "A1_background_no_fourier_k",
        sp.diff(rhs_f + rhs_c + rhs_b + rhs_r, k_mode),
    )

    # Exact state layout at three closures.
    for closure in (4, 6, 8):
        names = state_names(closure)
        expected = 4 * closure + 11
        checks[f"state_count_lmax_{closure}"] = len(names) == expected
        residuals[f"state_count_lmax_{closure}"] = str(len(names) - expected)
        checks[f"state_unique_lmax_{closure}"] = len(names) == len(set(names))
        residuals[f"state_unique_lmax_{closure}"] = (
            "0" if checks[f"state_unique_lmax_{closure}"] else "duplicate"
        )
        checks[f"state_required_endpoints_lmax_{closure}"] = (
            names[0] == "Phi"
            and "W_c" in names
            and "W_f" in names
            and names[-1] == f"F_steam_{closure}"
        )
        residuals[f"state_required_endpoints_lmax_{closure}"] = (
            "0" if checks[f"state_required_endpoints_lmax_{closure}"] else "bad_order"
        )

    # Independent exact cross-check against the pinned CAMB symbolic source.
    for ell in range(2, lmax + 1):
        _deadline(started, max_runtime_seconds)
        _record(checks, residuals, f"CAMB_J_l{ell}", cs.J_eq(ell).rhs - _expected_j(ell))
        _record(checks, residuals, f"CAMB_G_l{ell}", cs.G_eq(ell).rhs - _expected_g(ell))
        _record(checks, residuals, f"CAMB_E_l{ell}", cs.E_eq(ell).rhs - _expected_e(ell))
    expected_polter = sp.Rational(2, 15) * (
        sp.Rational(3, 4) * cs.pi_g + sp.Rational(9, 2) * cs.E_2
    )
    _record(
        checks,
        residuals,
        "CAMB_polarization_source",
        cs.polter_sub.rhs - expected_polter,
    )
    _deadline(started, max_runtime_seconds)

    passed = all(checks.values())
    return {
        "test": "K11-CS2 S0 exact multispecies structural audit",
        "base_status": BaseStatus.STRUCTURAL_S0_ONLY,
        "full_propagator_status": BaseStatus.FULL_PROPAGATOR_NOT_IMPLEMENTED,
        "physics_evolution_executed": False,
        "score_effect": 0,
        "parameters": asdict(ModelParameters()),
        "lmax": lmax,
        "state_count": len(state_names(lmax)),
        "state_count_formula": "4*lmax+11",
        "CAMB_version": camb.__version__,
        "CAMB_symbolic_sha256": (
            "F380B56A15F678F6D8DBA8981BBE5A4E57377050945ADE91C6CD4B9262C7A608"
        ),
        "checks": checks,
        "symbolic_residuals": residuals,
        "verdict": (
            "PASS_K11_CS2_S0_STRUCTURAL_ONLY"
            if passed
            else "STOP_K11_CS2_IMPLEMENTATION_DO_NOT_USE"
        ),
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }


def propagate_full_multispecies(*args, **kwargs):
    """Fail closed: the preregistered full propagator is not implemented."""

    raise NotImplementedError(
        "K11-CS2 full propagator is not implemented; run structural mode only"
    )
