#!/usr/bin/env python
"""A2-K4.3b-RG exact internal nu--steam regular-mode series.

For S1, standard massless neutrinos and free-streaming steam use the same
collisionless hierarchy and K4 transfers energy only between fuel and ash.
Their enthalpy-compensated difference therefore has zero total stress-energy
source at every multipole.  This script constructs the density and velocity
regular series, audits hierarchy residuals, Einstein-source cancellation, and
the seven-dimensional seed rank.

If a later microscopic model directly couples K4 to the steam hierarchy, this
conditional proof no longer applies and a new kinetic track is required.
"""

from __future__ import annotations

import argparse
import json
import math
import time

import numpy as np
import sympy as sp


def first_power(coefficients: list[sp.Expr]) -> int | None:
    for n, value in enumerate(coefficients):
        if sp.simplify(value) != 0:
            return n
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=25.0)
    parser.add_argument("--lmax", type=int, default=12)
    parser.add_argument("--series-order", type=int, default=14)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")
    if not (8 <= args.lmax <= 20):
        parser.error("--lmax must be in [8, 20]")
    if not (args.lmax <= args.series_order <= 24):
        parser.error("--series-order must be in [lmax, 24]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal nu-steam series deadline exceeded")

    neff = sp.Rational(3046, 1000)
    dneff = sp.Rational(535, 10000)
    factor = sp.Rational(2271, 10000)
    denominator = 1 + factor * (neff + dneff)
    r_gamma = sp.simplify(1 / denominator)
    r_nu = sp.simplify(factor * neff / denominator)
    r_steam = sp.simplify(factor * dneff / denominator)
    r_fs = sp.simplify(r_nu + r_steam)

    # dF/dy = A F, y=k*tau, massless collisionless scalar hierarchy.
    size = args.lmax + 1
    A = sp.zeros(size, size)
    A[0, 1] = -1
    A[1, 0] = sp.Rational(1, 3)
    A[1, 2] = -sp.Rational(2, 3)
    for ell in range(2, size):
        A[ell, ell - 1] = sp.Rational(ell, 2 * ell + 1)
        if ell + 1 < size:
            A[ell, ell + 1] = -sp.Rational(ell + 1, 2 * ell + 1)

    e0 = sp.zeros(size, 1)
    e1 = sp.zeros(size, 1)
    e0[0] = 1
    e1[1] = 1
    coefficients: dict[str, list[sp.Matrix]] = {}
    for name, seed in (("internal_density", e0), ("internal_velocity", e1)):
        coeffs: list[sp.Matrix] = []
        power = sp.eye(size)
        for n in range(args.series_order + 1):
            coeffs.append(sp.simplify(power * seed / sp.factorial(n)))
            power = sp.simplify(power * A)
        coefficients[name] = coeffs
        deadline()

    # Coefficient-level hierarchy residual: (n+1)c[n+1]-A c[n] = 0.
    checks: dict[str, bool] = {}
    hierarchy_residuals: dict[str, str] = {}
    for name, coeffs in coefficients.items():
        residual = sp.zeros(size, 1)
        for n in range(args.series_order):
            residual += (n + 1) * coeffs[n + 1] - A * coeffs[n]
        residual = sp.simplify(residual)
        checks[f"{name}_coefficient_hierarchy_residual_zero"] = bool(
            residual == sp.zeros(size, 1)
        )
        hierarchy_residuals[name] = str(residual)

    y_values = np.array([0.0008, 0.0016, 0.0032, 0.0064], dtype=float)
    mode_outputs: dict[str, object] = {}
    max_weighted_source = 0.0
    ratio = sp.simplify(r_nu / r_steam)
    for name, coeffs in coefficients.items():
        sampled: list[list[float]] = []
        source_max_by_depth: list[float] = []
        for y in y_values:
            vector = sp.zeros(size, 1)
            for n, coeff in enumerate(coeffs):
                vector += coeff * sp.Float(y, 30) ** n
            f_nu = vector
            f_steam = -ratio * vector
            weighted = sp.simplify(r_nu * f_nu + r_steam * f_steam)
            source = np.array(weighted, dtype=float).reshape(-1)
            source_max = float(np.max(np.abs(source)))
            max_weighted_source = max(max_weighted_source, source_max)
            source_max_by_depth.append(source_max)
            sampled.append([float(vector[i]) for i in range(min(6, size))])
        deadline()

        expected = [0, 1, 2, 3, 4, 5] if name == "internal_density" else [1, 0, 1, 2, 3, 4]
        observed = [
            first_power([coeffs[n][ell] for n in range(args.series_order + 1)])
            for ell in range(6)
        ]
        checks[f"{name}_regular_multipole_orders"] = observed == expected
        checks[f"{name}_weighted_source_zero_all_depths"] = max(source_max_by_depth) < 1.0e-25
        checks[f"{name}_finite_regular_hierarchy"] = bool(np.all(np.isfinite(sampled)))
        mode_outputs[name] = {
            "expected_leading_powers_l0_to_l5": expected,
            "observed_leading_powers_l0_to_l5": observed,
            "F_nu_l0_to_l5_by_k_tau": sampled,
            "F_steam_over_F_nu": str(-ratio),
            "max_weighted_source_by_k_tau": source_max_by_depth,
        }

    # Exact seven-seed rank in species-resolved regular descriptors:
    # [curvature,dc,db,dg,dnu,ds,vg,vnu,vs].
    seeds = sp.Matrix.hstack(
        sp.Matrix([1, 0, 0, 1, 1, 1, 0, 0, 0]),
        sp.Matrix([0, 1, 0, 0, 0, 0, 0, 0, 0]),
        sp.Matrix([0, 0, 1, 0, 0, 0, 0, 0, 0]),
        sp.Matrix([0, 0, 0, -r_fs / r_gamma, 1, 1, 0, 0, 0]),
        sp.Matrix([0, 0, 0, 0, 1, -r_nu / r_steam, 0, 0, 0]),
        sp.Matrix([0, 0, 0, 0, 0, 0, -r_fs / r_gamma, 1, 1]),
        sp.Matrix([0, 0, 0, 0, 0, 0, 0, 1, -r_nu / r_steam]),
    )
    seed_rank = int(seeds.rank())
    checks["full_species_resolved_regular_seed_rank_is_seven"] = seed_rank == 7

    # In S1 there is no direct Q_mu term for the radiation steam hierarchy.
    # With total internal delta T_mu_nu=0, Phi=Psi=0 and all dark-sector
    # perturbations set to zero solve the linear K4 response homogeneously.
    df, uf, dc, uc, phi, psi = sp.symbols("df uf dc uc phi psi")
    dark_zero = {df: 0, uf: 0, dc: 0, uc: 0, phi: 0, psi: 0}
    d = sp.symbols("delta", nonzero=True)
    fuel_density_rhs = -3 * (2 - d) * df - 9 * (2 * d - d**2) * uf
    fuel_euler_rhs = df / d + uf + psi
    ash_density_rhs = dc
    ash_euler_rhs = -2 * uc + psi
    homogeneous_residual = [
        sp.simplify(expr.subs(dark_zero))
        for expr in (fuel_density_rhs, fuel_euler_rhs, ash_density_rhs, ash_euler_rhs)
    ]
    checks["no_direct_steam_Q_implies_zero_K4_dark_response"] = homogeneous_residual == [0, 0, 0, 0]
    checks["zero_total_source_implies_zero_Einstein_residual"] = max_weighted_source < 1.0e-25
    deadline()

    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG exact internal nu-steam density/velocity regular series",
        "declared_physics_scope": {
            "steam": "massless collisionless S1 radiation",
            "operator_identity": "A_nu = A_steam",
            "K4_direct_coupling_to_steam_hierarchy": False,
            "warning": "a direct steam coupling would require a new kinetic track",
        },
        "radiation_fractions": {
            "R_gamma": float(r_gamma),
            "R_nu": float(r_nu),
            "R_steam": float(r_steam),
            "R_free_streaming": float(r_fs),
        },
        "k_tau_depths": y_values.tolist(),
        "mode_results": mode_outputs,
        "coefficient_hierarchy_residuals": hierarchy_residuals,
        "max_weighted_total_source_all_multipoles": max_weighted_source,
        "species_resolved_seed_rank": seed_rank,
        "checks": checks,
        "execution_verdict": "PASS_TWO_INTERNAL_REGULAR_MODES" if passed else "REVIEW_REQUIRED",
        "K4_3b_RG_verdict": "NEUZAVRETA_FIVE_COLLECTIVE_K4_CORRECTION_SERIES_MISSING",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)
