#!/usr/bin/env python3
"""A2-K4.1: complete regular constrained superhorizon mode basis.

Scope
-----
This script audits the nine-variable perfect-radiation K4 system used by
scripts 28--30.  It does not claim to replace a photon/neutrino Boltzmann
hierarchy.  It

1. derives the radiation-era indicial spectrum after imposing the 00
   Einstein constraint;
2. identifies every regular mode in that declared system;
3. integrates the full regular basis from deep radiation domination;
4. reports absolute transfers separately from the Gamma=0 reference;
5. checks start-time, wavenumber, solver, background, and constraint
   convergence.

The old recombination-normalized velocity-isocurvature vector is retained as
historical evidence, but is tested for membership in the primordial regular
subspace rather than assumed to be a regular initial mode.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys
from typing import Any

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import PchipInterpolator
import sympy as sp


HERE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K4 = load("a2_k4_1_base30", "30_script_A2_K4_full_superhorizon_relative_mode_converged.py")
B = K4.BASE28

MODE_NAMES = ("adiabatic", "cdm_density_isocurvature", "baryon_density_isocurvature")


def symbolic_indicial_audit(delta_value: float) -> dict[str, Any]:
    """Derive the constrained radiation-era Frobenius matrix.

    Variables after eliminating delta_r=-4 U_r are
    [delta_c,U_c,delta_f,U_f,delta_b,U_b,U_r,Phi], with U=a E u.
    """

    d, p = sp.symbols("d p", positive=True, real=True)
    acoef = 3 * (2 - d)
    bcoef = 9 * (2 * d - d**2)
    matrix = sp.zeros(8, 8)

    # Phi_x=-Phi+2 U_r; density equations use 3 Phi_x or 3 d Phi_x.
    matrix[0, 6], matrix[0, 7] = 6, -3
    matrix[1, 1], matrix[1, 7] = -2, 1
    matrix[2, 2], matrix[2, 3] = -acoef, -bcoef
    matrix[2, 6], matrix[2, 7] = 6 * d, -3 * d
    matrix[3, 2], matrix[3, 3], matrix[3, 7] = 1 / d, 1, 1
    matrix[4, 6], matrix[4, 7] = 6, -3
    matrix[5, 5], matrix[5, 7] = -2, 1
    matrix[6, 6], matrix[6, 7] = -2, 1
    matrix[7, 6], matrix[7, 7] = 2, -1

    characteristic = sp.factor((p * sp.eye(8) - matrix).det())
    expected = sp.factor(
        p**3 * (p + 2) ** 2 * (p + 3)
        * (p**2 + (5 - 3 * d) * p + 12 - 6 * d)
    )
    characteristic_check = bool(sp.simplify(characteristic - expected) == 0)
    zero_mode_dimension = 8 - int(matrix.rank())

    numeric_matrix = np.array(matrix.subs(d, delta_value), dtype=float)
    eigenvalues = np.linalg.eigvals(numeric_matrix)
    eigenvalues = sorted(eigenvalues, key=lambda value: (value.real, value.imag), reverse=True)
    regular_count = int(sum(value.real >= -1.0e-10 for value in eigenvalues))

    # Full z=[dc,Uc,df,Uf,db,Ub,dr,Ur,Phi] leading regular basis.
    regular_basis = np.array(
        [
            [-1.5, 1.0, 0.0],
            [0.5, 0.0, 0.0],
            [-1.5 * delta_value, 0.0, 0.0],
            [0.5, 0.0, 0.0],
            [-1.5, 0.0, 1.0],
            [0.5, 0.0, 0.0],
            [-2.0, 0.0, 0.0],
            [0.5, 0.0, 0.0],
            [1.0, 0.0, 0.0],
        ],
        dtype=float,
    )
    old_velocity_vector = np.zeros(9, dtype=float)
    old_velocity_vector[3] = 1.0  # asymptotic fuel-only U_f velocity seed
    coeff, *_ = np.linalg.lstsq(regular_basis, old_velocity_vector, rcond=None)
    projection = regular_basis @ coeff
    projection_residual = float(
        np.linalg.norm(old_velocity_vector - projection)
        / np.linalg.norm(old_velocity_vector)
    )
    old_mode_in_regular_span = bool(projection_residual < 1.0e-12)

    return {
        "variables": "[dc,Uc,df,Uf,db,Ub,Ur,Phi], dr=-4Ur",
        "characteristic_polynomial": str(characteristic),
        "expected_factorization": str(expected),
        "characteristic_check": characteristic_check,
        "zero_mode_dimension": zero_mode_dimension,
        "numeric_exponents": [
            {"real": float(value.real), "imag": float(value.imag)}
            for value in eigenvalues
        ],
        "regular_mode_count": regular_count,
        "regular_modes": list(MODE_NAMES),
        "old_velocity_seed_projection_residual": projection_residual,
        "old_velocity_seed_in_regular_span": old_mode_in_regular_span,
    }


def model_parameters(lam: float):
    defaults = B.BASE13.BASE.ModelParameters()
    return B.BASE13.BASE.ModelParameters(
        h=defaults.h,
        omega_m0=defaults.omega_m0,
        lam=lam,
        delta=defaults.delta,
        delta_neff=defaults.delta_neff,
        omega_b=defaults.omega_b,
        omega_gamma=defaults.omega_gamma,
        neff_standard=defaults.neff_standard,
        z_star=defaults.z_star,
    )


class Background:
    def __init__(self, lam: float, x_min: float, step: float):
        self.p = model_parameters(lam)
        settings = B.BASE13.BASE.IntegrationSettings(x_min=x_min, step=step)
        xs_desc, states_desc, self.xb0 = B.BASE13.integrate_background(
            self.p, settings
        )
        self.xs = np.asarray(xs_desc[::-1], dtype=float)
        self.states = np.asarray(states_desc[::-1], dtype=float)
        self.interpolator = PchipInterpolator(
            self.xs, self.states, axis=0, extrapolate=False
        )
        self.step = float(step)
        self.x_min = float(x_min)

    def state(self, x: float) -> np.ndarray:
        value = np.asarray(self.interpolator(x), dtype=float)
        if not np.all(np.isfinite(value)):
            raise FloatingPointError(f"Non-finite interpolated background at x={x}")
        return value


def initial_regular_basis(
    x: float, state: np.ndarray, background: Background, q: float
) -> np.ndarray:
    """Return exact-constraint finite-start representatives of all regular modes."""

    p = background.p
    xf, xc, xb, xr, e = B.component_background(x, state, background.xb0)
    a = math.exp(x)
    e2_x = -3.0 * xc - 3.0 * p.delta * xf - 3.0 * xb - 4.0 * xr
    h = e2_x / (2.0 * e * e)
    phi0 = 1.0
    clock = -(q * q + 3.0 * a * a * e * e) * phi0 / (
        3.0 * a * a * e * e * h
    )
    inertia = xc + p.delta * xf + xb + (4.0 / 3.0) * xr
    common_u = 2.0 * e * phi0 / (3.0 * a * inertia)
    lam_over_e = p.lam / e

    basis = np.zeros((9, 3), dtype=float)
    # Generalized common-clock adiabatic representative with Phi_x=0.
    basis[B.DC, 0] = (-3.0 + lam_over_e * xf / xc) * clock
    basis[B.UC, 0] = common_u
    basis[B.DF, 0] = (-3.0 * p.delta - lam_over_e) * clock
    basis[B.UF, 0] = common_u
    basis[B.DB, 0] = -3.0 * clock
    basis[B.UB, 0] = common_u
    basis[B.DR, 0] = -4.0 * clock
    basis[B.UR, 0] = common_u
    basis[B.PHI, 0] = phi0

    # Density isocurvature representatives with exact initial total density zero.
    basis[B.DC, 1] = 1.0
    basis[B.DR, 1] = -xc / xr
    basis[B.DB, 2] = 1.0
    basis[B.DR, 2] = -xb / xr
    return basis


def observable_matrix(
    x: float, basis: np.ndarray, state: np.ndarray, background: Background
) -> np.ndarray:
    """Dimensionless audit norm; U=aE u and df is scaled by 1/delta."""

    _, _, _, _, e = B.component_background(x, state, background.xb0)
    ae = math.exp(x) * e
    u_c = ae * basis[B.UC]
    u_f = ae * basis[B.UF]
    u_b = ae * basis[B.UB]
    u_r = ae * basis[B.UR]
    return np.vstack(
        [
            basis[B.PHI],
            basis[B.DC],
            basis[B.DF] / background.p.delta,
            basis[B.DB],
            basis[B.DR],
            u_c,
            u_f,
            u_b,
            u_r,
            u_f - u_c,
            u_c - u_b,
        ]
    )


def inverse_sqrt_gram(matrix: np.ndarray) -> np.ndarray:
    gram = matrix.T @ matrix
    values, vectors = np.linalg.eigh(gram)
    if np.min(values) <= 0.0:
        raise FloatingPointError("Regular initial basis has singular audit Gram matrix")
    return vectors @ np.diag(values ** -0.5) @ vectors.T


def integrate_regular_basis(
    background: Background,
    x_start: float,
    q: float,
    rtol: float,
    atol: float,
    samples: int = 2401,
) -> dict[str, Any]:
    state0 = background.state(x_start)
    y0 = initial_regular_basis(x_start, state0, background, q)
    obs0 = observable_matrix(x_start, y0, state0, background)
    orthonormalizer = inverse_sqrt_gram(obs0)

    def rhs_flat(x: float, flat: np.ndarray) -> np.ndarray:
        state = background.state(x)
        matrix = flat.reshape(9, 3)
        derivative = np.empty_like(matrix)
        for column in range(3):
            derivative[:, column] = B.rhs(
                x, matrix[:, column], state, background.xb0, background.p, q
            )
        return derivative.reshape(-1)

    times = np.linspace(x_start, 0.0, samples)
    solution = solve_ivp(
        rhs_flat,
        (x_start, 0.0),
        y0.reshape(-1),
        method="DOP853",
        t_eval=times,
        rtol=rtol,
        atol=atol,
    )
    if not solution.success:
        raise RuntimeError(solution.message)

    initial_mode_norms = np.linalg.norm(obs0, axis=0)
    max_mode_norms = np.zeros(3, dtype=float)
    max_relative_fc = np.zeros(3, dtype=float)
    max_singular = 0.0
    max_abs_residual = 0.0
    max_term_norm = 0.0
    initial_constraint_relative: list[float] = []
    final_obs = None

    for index, x in enumerate(solution.t):
        state = background.state(float(x))
        matrix = solution.y[:, index].reshape(9, 3)
        obs = observable_matrix(float(x), matrix, state, background)
        mode_norms = np.linalg.norm(obs, axis=0) / initial_mode_norms
        max_mode_norms = np.maximum(max_mode_norms, mode_norms)
        max_relative_fc = np.maximum(
            max_relative_fc, np.abs(obs[9]) / initial_mode_norms
        )
        singular = float(np.linalg.svd(obs @ orthonormalizer, compute_uv=False)[0])
        max_singular = max(max_singular, singular)

        for column in range(3):
            dy = B.rhs(
                float(x), matrix[:, column], state, background.xb0,
                background.p, q
            )
            terms = K4.raw_constraint_terms(
                float(x), matrix[:, column], dy, state, background.xb0, q
            )
            residual = abs(float(np.sum(terms)))
            norm = float(np.sum(np.abs(terms)))
            max_abs_residual = max(max_abs_residual, residual)
            max_term_norm = max(max_term_norm, norm)
            if index == 0:
                initial_constraint_relative.append(residual / max(norm, 1e-300))
        final_obs = obs

    if final_obs is None:
        raise RuntimeError("No perturbation samples were produced")
    final_mode_norms = np.linalg.norm(final_obs, axis=0) / initial_mode_norms
    final_normalized = final_obs / initial_mode_norms[np.newaxis, :]
    final_singular = float(
        np.linalg.svd(final_obs @ orthonormalizer, compute_uv=False)[0]
    )

    mode_summaries = {}
    for index, name in enumerate(MODE_NAMES):
        mode_summaries[name] = {
            "initial_audit_norm": float(initial_mode_norms[index]),
            "max_absolute_norm_transfer": float(max_mode_norms[index]),
            "final_absolute_norm_transfer": float(final_mode_norms[index]),
            "max_abs_Uf_minus_Uc_over_initial_norm": float(max_relative_fc[index]),
            "final_Phi_over_initial_norm": float(final_normalized[0, index]),
            "final_dc_over_initial_norm": float(final_normalized[1, index]),
            "final_df_over_delta_initial_norm": float(final_normalized[2, index]),
            "final_db_over_initial_norm": float(final_normalized[3, index]),
            "final_dr_over_initial_norm": float(final_normalized[4, index]),
        }

    return {
        "lambda": float(background.p.lam),
        "background_step": background.step,
        "x_start": float(x_start),
        "q_over_H0": float(q),
        "rtol": float(rtol),
        "atol": float(atol),
        "solver_success": bool(solution.success),
        "nfev": int(solution.nfev),
        "all_finite": bool(np.all(np.isfinite(solution.y))),
        "initial_constraint_relative": initial_constraint_relative,
        "global_relative_00_constraint_residual": float(
            max_abs_residual / max(max_term_norm, 1e-300)
        ),
        "max_regular_subspace_absolute_singular_transfer": float(max_singular),
        "final_regular_subspace_absolute_singular_transfer": float(final_singular),
        "mode_summaries": mode_summaries,
        "final_semantic_observable_matrix": final_normalized.tolist(),
        "early_lambda_over_E": float(background.p.lam / math.sqrt(np.sum(state0))),
    }


def relative_matrix_difference(first: dict[str, Any], reference: dict[str, Any]) -> float:
    a = np.asarray(first["final_semantic_observable_matrix"], dtype=float)
    b = np.asarray(reference["final_semantic_observable_matrix"], dtype=float)
    return float(np.linalg.norm(a - b) / max(np.linalg.norm(b), 1.0))


def main() -> int:
    defaults = B.BASE13.BASE.ModelParameters()
    symbolic = symbolic_indicial_audit(defaults.delta)
    lam = defaults.lam
    x_min = -22.0
    q = 1.0e-5

    coupled_fine_bg = Background(lam, x_min, 2.5e-4)
    coupled_coarse_bg = Background(lam, x_min, 5.0e-4)
    null_fine_bg = Background(0.0, x_min, 2.5e-4)

    primary = integrate_regular_basis(
        coupled_fine_bg, -20.0, q, rtol=1.0e-10, atol=1.0e-13
    )
    earlier_start = integrate_regular_basis(
        coupled_fine_bg, -22.0, q, rtol=1.0e-10, atol=1.0e-13
    )
    half_q = integrate_regular_basis(
        coupled_fine_bg, -20.0, 0.5 * q, rtol=1.0e-10, atol=1.0e-13
    )
    tighter = integrate_regular_basis(
        coupled_fine_bg, -20.0, q, rtol=3.0e-11, atol=3.0e-14
    )
    coarse_background = integrate_regular_basis(
        coupled_coarse_bg, -20.0, q, rtol=1.0e-10, atol=1.0e-13
    )
    null = integrate_regular_basis(
        null_fine_bg, -20.0, q, rtol=1.0e-10, atol=1.0e-13
    )

    start_difference = relative_matrix_difference(primary, earlier_start)
    q_difference = relative_matrix_difference(primary, half_q)
    solver_difference = relative_matrix_difference(primary, tighter)
    background_difference = relative_matrix_difference(primary, coarse_background)

    ratios_to_null = {}
    for name in MODE_NAMES:
        coupled_mode = primary["mode_summaries"][name]
        null_mode = null["mode_summaries"][name]
        ratios_to_null[name] = {
            "max_norm_ratio": float(
                coupled_mode["max_absolute_norm_transfer"]
                / max(null_mode["max_absolute_norm_transfer"], 1e-300)
            ),
            "final_norm_ratio": float(
                coupled_mode["final_absolute_norm_transfer"]
                / max(null_mode["final_absolute_norm_transfer"], 1e-300)
            ),
        }

    primordial_linearity_estimate = (
        1.0e-5 * primary["max_regular_subspace_absolute_singular_transfer"]
    )
    checks = {
        "symbolic_characteristic_factorization": symbolic["characteristic_check"],
        "exactly_three_regular_modes": symbolic["regular_mode_count"] == 3,
        "old_velocity_seed_not_regular": not symbolic["old_velocity_seed_in_regular_span"],
        "all_runs_finite": all(
            run["all_finite"]
            for run in (primary, earlier_start, half_q, tighter, coarse_background, null)
        ),
        "initial_constraints_controlled": max(primary["initial_constraint_relative"]) < 1e-10,
        "global_constraint_controlled": primary["global_relative_00_constraint_residual"] < 1e-6,
        "deep_start_converged": start_difference < 1e-5,
        "superhorizon_q_converged": q_difference < 1e-6,
        "solver_tolerance_converged": solver_difference < 1e-6,
        "background_step_converged": background_difference < 1e-6,
        "primordial_1e_minus_5_remains_linear": primordial_linearity_estimate < 1.0,
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K4.1 complete regular constrained superhorizon basis",
        "scope": (
            "Complete regular basis of the declared 9-variable perfect-radiation "
            "K4 system; not a photon/neutrino Boltzmann hierarchy or subhorizon test."
        ),
        "symbolic_indicial_audit": symbolic,
        "primary_coupled_run": primary,
        "null_reference": null,
        "ratios_to_null_reported_separately": ratios_to_null,
        "convergence": {
            "deep_start_matrix_difference": start_difference,
            "q_matrix_difference": q_difference,
            "solver_matrix_difference": solver_difference,
            "background_matrix_difference": background_difference,
        },
        "primordial_1e_minus_5_max_audit_norm": float(primordial_linearity_estimate),
        "checks": checks,
        "verdict": (
            "PASS_K4_1_REGULAR_SUPERHORIZON_BASIS"
            if passed else "K4_1_REQUIRES_REVIEW"
        ),
        "next_gate": (
            "K4.2 high-k/subhorizon principal symbol and physical growth; "
            "K4 is not yet a full A2 survivor."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
