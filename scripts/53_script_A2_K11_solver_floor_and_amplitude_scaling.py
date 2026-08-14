#!/usr/bin/env python3
"""Amplitude-scaling audit of the corrected A2-K11 drag equations.

The perturbation system is linear.  Therefore multiplying every initial
perturbation by a constant A must multiply the whole solution by A while the
relative transfer |V_f-V_c|_final/|V_f-V_c|_initial remains unchanged.

This is a direct audit of the solver-floor problem found in script 45: its
reported final transfer is O(1e-13), although solve_ivp used atol=1e-10.
The equations and conventions are imported from the corrected successor 51.
No post-data parameter is fitted here.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import solve_ivp


SOURCE = Path(__file__).with_name(
    "51_script_A2_K11_script45_equation_and_sign_audit.py"
)
SPEC = importlib.util.spec_from_file_location("k11_equations", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load {SOURCE}")
K11 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = K11
SPEC.loader.exec_module(K11)


def run_scaled(
    step: float,
    q: float,
    lam: float,
    gamma: float,
    amplitude: float,
    rtol: float = 2.0e-9,
    atol: float = 2.0e-11,
) -> dict:
    p, xs, coeff = K11.build_background(lam, step)
    c0 = {key: float(value[0]) for key, value in coeff.items()}
    y0 = K11.initial_relative_mode(c0, p.delta) * amplitude
    relative_initial = float(y0[K11.UF] - y0[K11.UC])

    def ode(x: float, y: np.ndarray) -> np.ndarray:
        c = K11.interp_coeff(x, xs, coeff)
        return K11.corrected_rhs(x, y, c, q, lam, p.delta, gamma)

    sol = solve_ivp(
        ode,
        (float(xs[0]), float(xs[-1])),
        y0,
        method="Radau",
        t_eval=xs,
        rtol=rtol,
        atol=atol,
    )
    if not sol.success:
        raise RuntimeError(sol.message)

    residuals = []
    norms = []
    for x, y in zip(xs, sol.y.T):
        c = K11.interp_coeff(float(x), xs, coeff)
        dy = K11.corrected_rhs(float(x), y, c, q, lam, p.delta, gamma)
        residual, norm = K11.constraint(float(x), y, dy, c, q)
        residuals.append(residual)
        norms.append(norm)
    residuals = np.asarray(residuals)
    norms = np.asarray(norms)
    active = norms > max(float(np.max(norms)) * 1.0e-10, 1.0e-30)

    yf = sol.y[:, -1]
    relative_final = float(yf[K11.UF] - yf[K11.UC])
    return {
        "step": step,
        "q": q,
        "lambda": lam,
        "gamma": gamma,
        "initial_amplitude_scale": amplitude,
        "rtol": rtol,
        "atol": atol,
        "initial_relative_velocity": relative_initial,
        "final_relative_velocity": relative_final,
        "absolute_transfer": abs(relative_final / relative_initial),
        "max_abs_state": float(np.max(np.abs(sol.y))),
        "max_abs_00_residual": float(np.max(residuals)),
        "max_relative_00_residual_active": float(
            np.max(residuals[active] / norms[active]) if np.any(active) else 0.0
        ),
        "all_finite": bool(np.all(np.isfinite(sol.y))),
    }


def rel_log_difference(a: float, b: float) -> float:
    la = math.log(max(a, 1.0e-300))
    lb = math.log(max(b, 1.0e-300))
    return abs(la - lb) / max(abs(lb), 1.0)


def main() -> int:
    q = 1.0e-5
    lam = 0.15
    gamma = 0.03
    step = 2.5e-4

    unit = run_scaled(step, q, lam, gamma, 1.0)
    large = run_scaled(step, q, lam, gamma, 1.0e12)
    large_half_step = run_scaled(step / 2.0, q, lam, gamma, 1.0e12)

    amplitude_error = rel_log_difference(
        unit["absolute_transfer"], large["absolute_transfer"]
    )
    step_error_resolved = rel_log_difference(
        large["absolute_transfer"], large_half_step["absolute_transfer"]
    )

    checks = {
        "all_runs_finite": all(
            run["all_finite"] for run in (unit, large, large_half_step)
        ),
        "amplitude_scaling_1e12": amplitude_error < 1.0e-6,
        "resolved_step_convergence": step_error_resolved < 1.0e-6,
        "resolved_constraint_relative": (
            large_half_step["max_relative_00_residual_active"] < 1.0e-5
        ),
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K11 corrected-equation solver floor and amplitude scaling",
        "linear_system_requirement": (
            "transfer must be invariant under a common initial-amplitude rescaling"
        ),
        "unit_amplitude": unit,
        "amplitude_1e12": large,
        "amplitude_1e12_half_step": large_half_step,
        "amplitude_log_transfer_relative_difference": amplitude_error,
        "resolved_step_log_transfer_relative_difference": step_error_resolved,
        "checks": checks,
        "verdict": "PASS_NUMERICAL_RESOLUTION" if passed else "FAIL_NUMERICAL_RESOLUTION",
        "scope": (
            "Numerical resolution only.  A pass would not establish an action, "
            "a regular rho_f->0 limit, CMB viability, or an S8 prediction."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
