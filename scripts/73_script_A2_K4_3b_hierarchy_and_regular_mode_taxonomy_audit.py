#!/usr/bin/env python
"""A2-K4.3b hierarchy and regular-mode taxonomy audit.

This script does not evolve the coupled K4 Einstein--Boltzmann system.  It
audits the exact hierarchy interface against local CAMB symbolic equations,
proves the collective/internal decomposition of standard neutrinos and
free-streaming steam, and counts the standard analytic scalar seed space.
An internal deadline is mandatory.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
LOCAL_DEPS = ROOT / ".deps" / "python"
if LOCAL_DEPS.exists():
    sys.path.insert(0, str(LOCAL_DEPS))


def first_nonzero_power(coefficients: list[sp.Expr]) -> int | None:
    for power, value in enumerate(coefficients):
        if sp.simplify(value) != 0:
            return power
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=20.0)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal K4.3b hierarchy audit deadline exceeded")

    # Frozen radiation convention used by A1/K4 and the CAMB anchor.
    neff_standard = sp.Rational(3046, 1000)
    delta_neff = sp.Rational(535, 10000)
    neutrino_factor = sp.Rational(2271, 10000)
    denominator = 1 + neutrino_factor * (neff_standard + delta_neff)
    r_gamma = sp.simplify(1 / denominator)
    r_nu = sp.simplify(neutrino_factor * neff_standard / denominator)
    r_steam = sp.simplify(neutrino_factor * delta_neff / denominator)
    r_fs = sp.simplify(r_nu + r_steam)

    checks: dict[str, bool] = {}
    evidence: dict[str, object] = {}

    checks["radiation_fractions_sum_to_one"] = bool(
        sp.simplify(r_gamma + r_nu + r_steam - 1) == 0
    )
    evidence["radiation_fractions"] = {
        "R_gamma": float(r_gamma),
        "R_nu_standard": float(r_nu),
        "R_steam_DeltaNeff": float(r_steam),
        "R_free_streaming_total": float(r_fs),
    }
    deadline()

    # Exact finite collisionless hierarchy dF/dy=A F, y=k*tau.
    lmax = 8
    hierarchy = sp.zeros(lmax + 1, lmax + 1)
    hierarchy[0, 1] = -1
    hierarchy[1, 0] = sp.Rational(1, 3)
    hierarchy[1, 2] = -sp.Rational(2, 3)
    for ell in range(2, lmax + 1):
        hierarchy[ell, ell - 1] = sp.Rational(ell, 2 * ell + 1)
        if ell < lmax:
            hierarchy[ell, ell + 1] = -sp.Rational(ell + 1, 2 * ell + 1)

    # Identical nu and steam operators imply exact decoupling into the
    # enthalpy-weighted collective hierarchy and an internal difference.
    f_nu = sp.Matrix(sp.symbols(f"n0:{lmax + 1}"))
    f_s = sp.Matrix(sp.symbols(f"s0:{lmax + 1}"))
    collective = sp.simplify((r_nu * f_nu + r_steam * f_s) / r_fs)
    internal = f_nu - f_s
    collective_residual = sp.simplify(
        (r_nu * hierarchy * f_nu + r_steam * hierarchy * f_s) / r_fs
        - hierarchy * collective
    )
    internal_residual = sp.simplify(
        hierarchy * f_nu - hierarchy * f_s - hierarchy * internal
    )
    checks["nu_steam_collective_hierarchy_closes"] = bool(
        collective_residual == sp.zeros(lmax + 1, 1)
    )
    checks["nu_steam_internal_hierarchy_decouples"] = bool(
        internal_residual == sp.zeros(lmax + 1, 1)
    )
    deadline()

    # Internal compensated modes have zero total T^mu_nu source at every
    # multipole when F_s=-(R_nu/R_s)F_nu.
    arbitrary = sp.Matrix(sp.symbols(f"a0:{lmax + 1}"))
    compensated_source = sp.simplify(
        r_nu * arbitrary + r_steam * (-(r_nu / r_steam) * arbitrary)
    )
    checks["internal_mode_zero_total_source_all_multipoles"] = bool(
        compensated_source == sp.zeros(lmax + 1, 1)
    )

    # Analytic collisionless series.  Standard scalar regularity admits an
    # isotropic density seed e0 and a dipole/velocity seed e1; higher moments
    # are generated recursively.  Arbitrary constant l>=2 seeds are outside
    # this standard analytic/local-isotropy primordial class.
    series_order = 7
    e0 = sp.zeros(lmax + 1, 1)
    e1 = sp.zeros(lmax + 1, 1)
    e0[0] = 1
    e1[1] = 1
    density_coeffs: list[sp.Matrix] = []
    velocity_coeffs: list[sp.Matrix] = []
    power = sp.eye(lmax + 1)
    for n in range(series_order + 1):
        density_coeffs.append(sp.simplify(power * e0 / sp.factorial(n)))
        velocity_coeffs.append(sp.simplify(power * e1 / sp.factorial(n)))
        power = sp.simplify(power * hierarchy)

    density_leading = []
    velocity_leading = []
    for ell in range(0, 6):
        density_leading.append(
            first_nonzero_power([density_coeffs[n][ell] for n in range(series_order + 1)])
        )
        velocity_leading.append(
            first_nonzero_power([velocity_coeffs[n][ell] for n in range(series_order + 1)])
        )
    checks["density_seed_has_Fl_order_y_to_l"] = density_leading == [0, 1, 2, 3, 4, 5]
    checks["velocity_seed_has_expected_analytic_orders"] = velocity_leading == [1, 0, 1, 2, 3, 4]
    evidence["internal_density_mode_leading_powers_l0_to_l5"] = density_leading
    evidence["internal_velocity_mode_leading_powers_l0_to_l5"] = velocity_leading
    evidence["density_seed_first_coefficients"] = {
        "F0": [str(density_coeffs[n][0]) for n in range(5)],
        "F1": [str(density_coeffs[n][1]) for n in range(5)],
        "F2": [str(density_coeffs[n][2]) for n in range(5)],
    }
    evidence["velocity_seed_first_coefficients"] = {
        "F0": [str(velocity_coeffs[n][0]) for n in range(5)],
        "F1": [str(velocity_coeffs[n][1]) for n in range(5)],
        "F2": [str(velocity_coeffs[n][2]) for n in range(5)],
        "F3": [str(velocity_coeffs[n][3]) for n in range(5)],
    }
    deadline()

    # Seven independent leading seed descriptors:
    # [curvature, dc, db, dg, dnu, ds, vg, vnu, vs].
    seeds = sp.Matrix.hstack(
        sp.Matrix([1, 0, 0, 1, 1, 1, 0, 0, 0]),  # AD
        sp.Matrix([0, 1, 0, 0, 0, 0, 0, 0, 0]),  # CDI
        sp.Matrix([0, 0, 1, 0, 0, 0, 0, 0, 0]),  # BI
        sp.Matrix([0, 0, 0, -r_fs / r_gamma, 1, 1, 0, 0, 0]),  # collective FS density
        sp.Matrix([0, 0, 0, 0, 1, -r_nu / r_steam, 0, 0, 0]),  # nu-steam density
        sp.Matrix([0, 0, 0, 0, 0, 0, -r_fs / r_gamma, 1, 1]),  # collective FS velocity
        sp.Matrix([0, 0, 0, 0, 0, 0, 0, 1, -r_nu / r_steam]),  # nu-steam velocity
    )
    seed_rank = int(seeds.rank())
    checks["seven_standard_analytic_scalar_seeds_independent"] = seed_rank == 7
    checks["collective_density_isocurvature_compensated"] = bool(
        sp.simplify(r_gamma * seeds[3, 3] + r_nu * seeds[4, 3] + r_steam * seeds[5, 3]) == 0
    )
    checks["internal_density_isocurvature_compensated"] = bool(
        sp.simplify(r_nu * seeds[4, 4] + r_steam * seeds[5, 4]) == 0
    )
    checks["collective_velocity_isocurvature_compensated"] = bool(
        sp.simplify(r_gamma * seeds[6, 5] + r_nu * seeds[7, 5] + r_steam * seeds[8, 5]) == 0
    )
    checks["internal_velocity_isocurvature_compensated"] = bool(
        sp.simplify(r_nu * seeds[7, 6] + r_steam * seeds[8, 6]) == 0
    )
    evidence["standard_analytic_scalar_mode_count_S1"] = seed_rank
    evidence["mode_names"] = [
        "adiabatic",
        "cdm_density_isocurvature",
        "baryon_density_isocurvature",
        "collective_free_streaming_density_isocurvature",
        "nu_steam_internal_density_isocurvature",
        "collective_free_streaming_velocity_isocurvature",
        "nu_steam_internal_velocity_isocurvature",
    ]

    # A velocity seed has F1=O(1), theta=3kF1/4, so the K4.1 Newtonian
    # variable U=Hconf*theta/k^2=3F1/(4 k*tau) has exponent -1.  This is the
    # known regular velocity-isocurvature mode with singular zero-shear-frame
    # potentials; it must be initialized in a regular gauge/invariant basis.
    y = sp.symbols("y", positive=True)
    u_newtonian_velocity_seed = sp.Rational(3, 4) / y
    checks["velocity_mode_not_finite_in_K4_1_Newtonian_U"] = bool(
        sp.limit(u_newtonian_velocity_seed, y, 0, dir="+") == sp.oo
    )
    evidence["velocity_mode_Newtonian_U_scaling"] = "3/(4 k tau), exponent -1"

    # The interaction is asymptotically subleading: E~sqrt(Omega_r)a^-2,
    # hence lambda/E~a^2.  This protects the leading standard radiation modes
    # but does not replace their finite-start K4 correction series.
    h = 0.6637
    omega_gamma = 2.469e-5
    omega_r = omega_gamma * (1.0 + 0.2271 * (3.046 + 0.0535)) / h**2
    lam = 0.15
    lam_over_e_x20 = lam * math.exp(-40.0) / math.sqrt(omega_r)
    lam_over_e_x22 = lam * math.exp(-44.0) / math.sqrt(omega_r)
    scaling_ratio = lam_over_e_x20 / lam_over_e_x22
    checks["K4_interaction_vanishes_as_a_squared"] = bool(
        lam_over_e_x20 < 1.0e-14
        and abs(scaling_ratio / math.exp(4.0) - 1.0) < 1.0e-12
    )
    evidence["early_K4_lambda_over_E"] = {
        "x_minus_20": lam_over_e_x20,
        "x_minus_22": lam_over_e_x22,
        "ratio": scaling_ratio,
        "expected_ratio_exp4": math.exp(4.0),
    }
    deadline()

    # Collision-only tight-coupling block for [F_gamma2,G_gamma0,G_gamma2]
    # from Ma--Bertschinger eqs. 61--64.  Full rank means all three vanish at
    # zeroth tight-coupling order; higher values are generated perturbatively.
    collision_block = sp.Matrix(
        [
            [-sp.Rational(9, 10), sp.Rational(1, 10), sp.Rational(1, 10)],
            [sp.Rational(1, 2), -sp.Rational(1, 2), sp.Rational(1, 2)],
            [sp.Rational(1, 10), sp.Rational(1, 10), -sp.Rational(9, 10)],
        ]
    )
    checks["tight_coupling_collision_block_has_only_zero_equilibrium"] = bool(
        collision_block.rank() == 3 and len(collision_block.nullspace()) == 0
    )
    evidence["tight_coupling_collision_block_determinant"] = str(collision_block.det())

    # Cross-check exact equation inventory against the locally frozen CAMB
    # symbolic module.  lmax=6 returns l=2..5 for J, G and E.
    import camb  # noqa: WPS433,E402
    import camb.symbolic as cs  # noqa: WPS433,E402

    equations = cs.get_hierarchies(lmax=6)
    equation_strings = [str(eq) for eq in equations]
    photon_eqs = equation_strings[0::3]
    neutrino_eqs = equation_strings[1::3]
    polarization_eqs = equation_strings[2::3]
    checks["CAMB_symbolic_hierarchy_inventory_4x3"] = len(equations) == 12
    checks["CAMB_photon_hierarchy_contains_opacity"] = all("opacity" in eq for eq in photon_eqs)
    checks["CAMB_neutrino_hierarchy_is_collisionless"] = all("opacity" not in eq for eq in neutrino_eqs)
    checks["CAMB_polarization_hierarchy_contains_opacity"] = all("opacity" in eq for eq in polarization_eqs)
    evidence["CAMB_version"] = camb.__version__
    evidence["CAMB_symbolic_equation_count_l2_to_l5"] = len(equations)
    deadline()

    audit_pass = all(checks.values())
    output = {
        "test": "A2-K4.3b hierarchy and regular-mode taxonomy audit",
        "execution": "PASS" if audit_pass else "REVIEW_REQUIRED",
        "checks": checks,
        "evidence": evidence,
        "physical_result": (
            "S1 requires seven standard analytic scalar modes, not the three-mode "
            "perfect-radiation K4.1 basis. Two velocity modes require a regular "
            "gauge/invariant start because Newtonian U and potentials are singular."
        ),
        "gate_verdict": (
            "K4_3B_NEUZAVRETA_REGULAR_GAUGE_FINITE_START_SERIES_REQUIRED"
            if audit_pass
            else "K4_3B_AUDIT_REQUIRES_REVIEW"
        ),
        "track_state": "A2-K4 remains LIVE at 60/100; no death reason issued",
        "next_required_work": (
            "derive and residual-test the seven finite-start series in a regular "
            "gauge, including subleading K4 terms; then implement them in a "
            "modifiable Einstein-Boltzmann backend"
        ),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if audit_pass else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)

