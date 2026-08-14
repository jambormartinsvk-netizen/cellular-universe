#!/usr/bin/env python3
"""Pointwise constraint and amplitude-scaling audit of script 45.

This script imports the exact current script-45 equations.  It does not
correct their physics.  It tests two claims that cannot be decided from
global maxima alone:

1. whether a reported global relative 00 residual of one is merely a
   zero-over-zero floor at inactive points; and
2. whether the linear transfer is invariant under a common rescaling of the
   initial relative mode when rtol=1e-12 and atol=1e-16 are used.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import solve_ivp


SOURCE = Path(__file__).with_name(
    "45_script_A2_K11_S8_K1b_superhorizon_instability_test.py"
)
SPEC = importlib.util.spec_from_file_location("script45_exact_revision", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load {SOURCE}")
S45 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = S45
SPEC.loader.exec_module(S45)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def run_scaled(
    step: float,
    q: float,
    lam: float,
    gamma: float,
    amplitude: float,
    rtol: float = 1.0e-12,
    atol: float = 1.0e-16,
) -> dict:
    p, xs, coeff = S45.build_background(lam, step)
    c0 = S45.at_index(coeff, 0)
    y0 = S45.initial_relative_mode(float(xs[0]), c0, p.delta) * amplitude
    rel0 = float(y0[S45.UF] - y0[S45.UC])

    def ode(x: float, y: np.ndarray) -> np.ndarray:
        c = {
            key: float(np.interp(x, xs, values))
            for key, values in coeff.items()
        }
        return S45.rhs(x, y, c, q, lam, p.delta, gamma)

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
    term_rows = []
    state_norms = []
    for x, y in zip(xs, sol.y.T):
        c = S45.at_index(coeff, len(residuals))
        dy = S45.rhs(float(x), y, c, q, lam, p.delta, gamma)
        terms = S45.constraint_terms(float(x), y, dy, c, q, p.delta)
        residuals.append(abs(float(np.sum(terms))))
        norms.append(float(np.sum(np.abs(terms))))
        term_rows.append(terms)
        state_norms.append(float(np.max(np.abs(y))))

    residuals = np.asarray(residuals)
    norms = np.asarray(norms)
    term_rows = np.asarray(term_rows)
    state_norms = np.asarray(state_norms)
    i_res = int(np.argmax(residuals))
    i_norm = int(np.argmax(norms))
    active_cut = max(float(np.max(norms)) * 1.0e-10, atol * 10.0)
    active = norms > active_cut
    ratios = np.divide(
        residuals,
        norms,
        out=np.zeros_like(residuals),
        where=norms > 0.0,
    )

    yf = sol.y[:, -1]
    relf = float(yf[S45.UF] - yf[S45.UC])
    return {
        "step": step,
        "q": q,
        "lambda": lam,
        "gamma": gamma,
        "amplitude": amplitude,
        "rtol": rtol,
        "atol": atol,
        "transfer": abs(relf / rel0),
        "final_relative_velocity": relf,
        "max_abs_state": float(np.max(np.abs(sol.y))),
        "max_abs_residual": float(residuals[i_res]),
        "max_term_norm": float(norms[i_norm]),
        "ratio_of_global_maxima": float(
            np.max(residuals) / max(float(np.max(norms)), 1.0e-300)
        ),
        "max_pointwise_relative_residual_active": float(
            np.max(ratios[active]) if np.any(active) else 0.0
        ),
        "active_cut": active_cut,
        "max_residual_point": {
            "index": i_res,
            "x": float(xs[i_res]),
            "a": float(math.exp(float(xs[i_res]))),
            "max_abs_state_at_point": float(state_norms[i_res]),
            "terms": [float(value) for value in term_rows[i_res]],
            "term_norm": float(norms[i_res]),
            "pointwise_relative_residual": float(ratios[i_res]),
        },
        "max_norm_point": {
            "index": i_norm,
            "x": float(xs[i_norm]),
            "a": float(math.exp(float(xs[i_norm]))),
            "residual": float(residuals[i_norm]),
            "term_norm": float(norms[i_norm]),
            "pointwise_relative_residual": float(ratios[i_norm]),
        },
        "all_finite": bool(np.all(np.isfinite(sol.y))),
    }


def log_difference(a: float, b: float) -> float:
    la = math.log(max(a, 1.0e-300))
    lb = math.log(max(b, 1.0e-300))
    return abs(la - lb) / max(abs(lb), 1.0)


def main() -> int:
    q = 1.0e-5
    lam = 0.15
    gamma = 0.03
    coarse_step = 1.25e-4
    fine_step = 6.25e-5

    unit_coarse = run_scaled(coarse_step, q, lam, gamma, 1.0)
    unit_fine = run_scaled(fine_step, q, lam, gamma, 1.0)
    scaled_fine = run_scaled(fine_step, q, lam, gamma, 1.0e12)

    step_error = log_difference(
        unit_coarse["transfer"], unit_fine["transfer"]
    )
    amplitude_error = log_difference(
        unit_fine["transfer"], scaled_fine["transfer"]
    )
    checks = {
        "step_converged_without_damping_bypass": step_error < 1.0e-6,
        "amplitude_scaling_1e12": amplitude_error < 1.0e-6,
        "pointwise_constraint_active": (
            unit_fine["max_pointwise_relative_residual_active"] < 1.0e-5
        ),
        "scaled_pointwise_constraint_active": (
            scaled_fine["max_pointwise_relative_residual_active"] < 1.0e-5
        ),
    }
    passed = all(checks.values())
    output = {
        "test": "Exact current script-45 constraint and scaling audit",
        "script45_sha256": sha256(SOURCE),
        "unit_coarse": unit_coarse,
        "unit_fine": unit_fine,
        "scaled_1e12_fine": scaled_fine,
        "step_log_transfer_relative_difference": step_error,
        "amplitude_log_transfer_relative_difference": amplitude_error,
        "checks": checks,
        "verdict": "PASS_CLAIMS" if passed else "FAIL_CLAIMS",
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
