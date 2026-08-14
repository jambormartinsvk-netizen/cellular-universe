#!/usr/bin/env python3
"""Independent K4.1 cross-check with fixed-step RK4 and a separate mode audit.

This script does not import script 66.  It independently rebuilds the
radiation-era constrained matrix, verifies its three-dimensional regular
kernel, integrates the three regular modes with fixed-step RK4 on the
validated background grid, and compares the final observable matrix with the
adaptative-DOP853 result registered by script 66.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "28_script_A2_K4_full_superhorizon_relative_mode.py"
SPEC = importlib.util.spec_from_file_location("a2_k4_1_independent_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load {BASE_PATH}")
B = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = B
SPEC.loader.exec_module(B)


REFERENCE_FINAL = np.array(
    [
        [0.201878963767262, -0.1457138096248528, -0.02702275490192271],
        [-0.5841086794013148, 0.5119792391842966, -0.07381563293532413],
        [-2.0795375338203343, 21.316884717737622, 3.953235129073632],
        [-0.6546138859525702, -0.4371414288477899, 0.918931735298595],
        [-0.8728185146034257, -0.5828611482337175, -0.10809211557314616],
        [0.21820451571825533, -0.15201661676559894, -0.02819161606200717],
        [0.2182021132185596, -6.47572304140083, -1.2009285668330334],
        [0.2182045177839196, -0.14657950446371187, -0.027183298775633077],
        [0.21820419625930548, -0.9943849679280915, -0.18440957199360355],
        [-2.4024996957454853e-06, -6.323706424635231, -1.1727369507710264],
        [-2.0656642658939618e-09, -0.005437112301887065, -0.0010083172863740943],
    ],
    dtype=float,
)


def indicial_matrix(delta: float) -> np.ndarray:
    """Reduced variables [dc,Uc,df,Uf,db,Ub,Ur,Phi], with dr=-4Ur."""
    acoef = 3.0 * (2.0 - delta)
    bcoef = 9.0 * (2.0 * delta - delta * delta)
    matrix = np.zeros((8, 8), dtype=float)
    matrix[0, 6], matrix[0, 7] = 6.0, -3.0
    matrix[1, 1], matrix[1, 7] = -2.0, 1.0
    matrix[2, 2], matrix[2, 3] = -acoef, -bcoef
    matrix[2, 6], matrix[2, 7] = 6.0 * delta, -3.0 * delta
    matrix[3, 2], matrix[3, 3], matrix[3, 7] = 1.0 / delta, 1.0, 1.0
    matrix[4, 6], matrix[4, 7] = 6.0, -3.0
    matrix[5, 5], matrix[5, 7] = -2.0, 1.0
    matrix[6, 6], matrix[6, 7] = -2.0, 1.0
    matrix[7, 6], matrix[7, 7] = 2.0, -1.0
    return matrix


def regular_reduced_basis(delta: float) -> np.ndarray:
    # Columns: adiabatic, CDM density iso, baryon density iso.
    return np.array(
        [
            [-1.5, 1.0, 0.0],
            [0.5, 0.0, 0.0],
            [-1.5 * delta, 0.0, 0.0],
            [0.5, 0.0, 0.0],
            [-1.5, 0.0, 1.0],
            [0.5, 0.0, 0.0],
            [0.5, 0.0, 0.0],
            [1.0, 0.0, 0.0],
        ],
        dtype=float,
    )


def initial_basis(x: float, state: np.ndarray, xb0: float, p, q: float) -> np.ndarray:
    xf, xc, xb, xr, e = B.component_background(x, state, xb0)
    a = math.exp(x)
    e2_x = -3.0 * xc - 3.0 * p.delta * xf - 3.0 * xb - 4.0 * xr
    h = e2_x / (2.0 * e * e)
    clock = -(q * q + 3.0 * a * a * e * e) / (3.0 * a * a * e * e * h)
    inertia = xc + p.delta * xf + xb + (4.0 / 3.0) * xr
    common_u = 2.0 * e / (3.0 * a * inertia)
    lam_over_e = p.lam / e
    y = np.zeros((9, 3), dtype=float)
    y[B.DC, 0] = (-3.0 + lam_over_e * xf / xc) * clock
    y[B.UC, 0] = common_u
    y[B.DF, 0] = (-3.0 * p.delta - lam_over_e) * clock
    y[B.UF, 0] = common_u
    y[B.DB, 0] = -3.0 * clock
    y[B.UB, 0] = common_u
    y[B.DR, 0] = -4.0 * clock
    y[B.UR, 0] = common_u
    y[B.PHI, 0] = 1.0
    y[B.DC, 1] = 1.0
    y[B.DR, 1] = -xc / xr
    y[B.DB, 2] = 1.0
    y[B.DR, 2] = -xb / xr
    return y


def observables(x: float, y: np.ndarray, state: np.ndarray, xb0: float, p) -> np.ndarray:
    _, _, _, _, e = B.component_background(x, state, xb0)
    ae = math.exp(x) * e
    uc, uf, ub, ur = ae * y[B.UC], ae * y[B.UF], ae * y[B.UB], ae * y[B.UR]
    return np.vstack(
        [
            y[B.PHI], y[B.DC], y[B.DF] / p.delta, y[B.DB], y[B.DR],
            uc, uf, ub, ur, uf - uc, uc - ub,
        ]
    )


def run(step: float, q: float = 1.0e-5) -> dict:
    defaults = B.BASE13.BASE.ModelParameters()
    p = B.BASE13.BASE.ModelParameters(
        h=defaults.h,
        omega_m0=defaults.omega_m0,
        lam=defaults.lam,
        delta=defaults.delta,
        delta_neff=defaults.delta_neff,
        omega_b=defaults.omega_b,
        omega_gamma=defaults.omega_gamma,
        neff_standard=defaults.neff_standard,
        z_star=defaults.z_star,
    )
    settings = B.BASE13.BASE.IntegrationSettings(x_min=-20.0, step=step)
    xs_desc, states_desc, xb0 = B.BASE13.integrate_background(p, settings)
    xs = xs_desc[::-1]
    states = states_desc[::-1]
    y = initial_basis(float(xs[0]), states[0], xb0, p, q)
    obs0 = observables(float(xs[0]), y, states[0], xb0, p)
    norms0 = np.linalg.norm(obs0, axis=0)
    max_abs_residual = 0.0
    max_term_norm = 0.0

    def derivative(x: float, matrix: np.ndarray, state: np.ndarray) -> np.ndarray:
        out = np.empty_like(matrix)
        for column in range(3):
            out[:, column] = B.rhs(x, matrix[:, column], state, xb0, p, q)
        return out

    for i, x in enumerate(xs):
        if i > 0:
            x0, x1 = float(xs[i - 1]), float(x)
            dx = x1 - x0
            s0, s1 = states[i - 1], states[i]
            xm = 0.5 * (x0 + x1)
            hmid = 0.5 * dx
            b1 = B.BASE13.BASE.rhs(s0, p)
            b2 = B.BASE13.BASE.rhs(s0 + 0.5 * hmid * b1, p)
            b3 = B.BASE13.BASE.rhs(s0 + 0.5 * hmid * b2, p)
            b4 = B.BASE13.BASE.rhs(s0 + hmid * b3, p)
            sm = s0 + hmid * (b1 + 2.0 * b2 + 2.0 * b3 + b4) / 6.0
            k1 = derivative(x0, y, s0)
            k2 = derivative(xm, y + 0.5 * dx * k1, sm)
            k3 = derivative(xm, y + 0.5 * dx * k2, sm)
            k4 = derivative(x1, y + dx * k3, s1)
            y = y + dx * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0

        dy = derivative(float(x), y, states[i])
        for column in range(3):
            xf, xc, xb, xr, e = B.component_background(float(x), states[i], xb0)
            a = math.exp(float(x))
            density = (
                xc * y[B.DC, column] + xf * y[B.DF, column]
                + xb * y[B.DB, column] + xr * y[B.DR, column]
            )
            terms = np.array(
                [
                    q * q * y[B.PHI, column],
                    3.0 * (a * e) ** 2 * (dy[B.PHI, column] + y[B.PHI, column]),
                    1.5 * a * a * density,
                ]
            )
            max_abs_residual = max(max_abs_residual, abs(float(np.sum(terms))))
            max_term_norm = max(max_term_norm, float(np.sum(np.abs(terms))))

    final = observables(float(xs[-1]), y, states[-1], xb0, p) / norms0[np.newaxis, :]
    reference_difference = float(
        np.linalg.norm(final - REFERENCE_FINAL) / max(np.linalg.norm(REFERENCE_FINAL), 1.0)
    )
    return {
        "step": float(step),
        "points": int(len(xs)),
        "all_finite": bool(np.all(np.isfinite(y))),
        "global_relative_00_constraint_residual": float(
            max_abs_residual / max(max_term_norm, 1e-300)
        ),
        "reference_matrix_difference": reference_difference,
        "final_matrix": final.tolist(),
    }


def main() -> int:
    delta = B.BASE13.BASE.ModelParameters().delta
    matrix = indicial_matrix(delta)
    regular = regular_reduced_basis(delta)
    eigenvalues = np.linalg.eigvals(matrix)
    regular_residual = float(np.linalg.norm(matrix @ regular))
    nullity = int(8 - np.linalg.matrix_rank(matrix, tol=1e-12))
    coarse = run(5.0e-4)
    fine = run(2.5e-4)
    step_difference = float(
        np.linalg.norm(np.asarray(coarse["final_matrix"]) - np.asarray(fine["final_matrix"]))
        / max(np.linalg.norm(np.asarray(fine["final_matrix"])), 1.0)
    )
    checks = {
        "independent_nullity_three": nullity == 3,
        "explicit_regular_basis_in_kernel": regular_residual < 1e-12,
        "five_irregular_exponents": sum(value.real < -1e-10 for value in eigenvalues) == 5,
        "coarse_and_fine_finite": coarse["all_finite"] and fine["all_finite"],
        "fixed_RK4_constraint_controlled": fine["global_relative_00_constraint_residual"] < 1e-6,
        "fixed_RK4_step_converged": step_difference < 1e-6,
        "DOP853_reference_reproduced": fine["reference_matrix_difference"] < 2e-6,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    passed = all(checks.values())
    output = {
        "test": "A2-K4.1 independent fixed-RK4 and indicial-basis cross-check",
        "indicial_eigenvalues": [
            {"real": float(value.real), "imag": float(value.imag)}
            for value in sorted(eigenvalues, key=lambda z: (z.real, z.imag), reverse=True)
        ],
        "regular_kernel_dimension": nullity,
        "regular_basis_residual": regular_residual,
        "coarse": coarse,
        "fine_summary": {
            key: value for key, value in fine.items() if key != "final_matrix"
        },
        "fixed_RK4_step_matrix_difference": step_difference,
        "checks": checks,
        "verdict": "PASS_INDEPENDENT_CROSSCHECK" if passed else "REQUIRES_REVIEW",
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
