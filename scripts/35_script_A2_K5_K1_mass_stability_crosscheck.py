#!/usr/bin/env python3
"""Cross-check the reconstructed K5-K1 scalar and effective mass histories.

This script imports the same validated A1-K1 background and reconstructs

  m_phi^2/H0^2 = 3 d^2Y/dvarphi^2,
  m_eff^2/H0^2 = 3[d^2Y/dvarphi^2 + X_c(beta_,varphi + beta^2)],

where Y=V/(3 H0^2 Mpl^2).  It reports the minima and checks step
convergence.  A non-negative result is a background tachyon gate only; it is
not a substitute for the full quadratic perturbation action.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


BASE_PATH = Path(__file__).with_name(
    "13_script_A1_K1_cdm_background_audit_exact_zstar.py"
)
SPEC = importlib.util.spec_from_file_location("k5_mass_background", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)


def run(step: float) -> dict:
    p = BASE13.BASE.ModelParameters()
    x_star = -math.log1p(p.z_star)
    settings = BASE13.BASE.IntegrationSettings(x_min=x_star, step=step)
    xs_desc, states_desc, xb0 = BASE13.integrate_background(p, settings)
    xs = xs_desc[::-1]
    states = states_desc[::-1]

    xf, xm, _ = states.T
    xb = xb0 * np.exp(-3.0 * xs)
    xc = xm - xb
    e = np.sqrt(np.sum(states, axis=1))
    w = -1.0 + p.delta

    xf_x = -3.0 * p.delta * xf - p.lam * xf / e
    varphi_x = np.sqrt(3.0 * p.delta * xf) / e
    beta = p.lam * np.sqrt(xf) / (xc * math.sqrt(3.0 * p.delta))
    y_x = 0.5 * (1.0 - w) * xf_x
    y_varphi = y_x / varphi_x
    y_varphi2 = np.gradient(y_varphi, xs, edge_order=2) / varphi_x
    beta_varphi = np.gradient(beta, xs, edge_order=2) / varphi_x

    mphi2 = 3.0 * y_varphi2
    meff2 = 3.0 * (y_varphi2 + xc * (beta_varphi + beta**2))
    i_phi = int(np.argmin(mphi2))
    i_eff = int(np.argmin(meff2))

    return {
        "step": step,
        "mphi2_over_H0sq_min": float(mphi2[i_phi]),
        "mphi2_min_redshift": float(math.exp(-xs[i_phi]) - 1.0),
        "meff2_over_H0sq_min": float(meff2[i_eff]),
        "meff2_min_redshift": float(math.exp(-xs[i_eff]) - 1.0),
        "mphi2_over_H0sq_today": float(mphi2[-1]),
        "meff2_over_H0sq_today": float(meff2[-1]),
        "all_finite": bool(
            np.all(np.isfinite(mphi2)) and np.all(np.isfinite(meff2))
        ),
        "mphi2_nonnegative_on_background": bool(np.all(mphi2 >= 0.0)),
        "meff2_nonnegative_on_background": bool(np.all(meff2 >= 0.0)),
    }


def main() -> int:
    coarse = run(5.0e-4)
    fine = run(2.5e-4)
    keys = [
        "mphi2_over_H0sq_min",
        "meff2_over_H0sq_min",
        "mphi2_over_H0sq_today",
        "meff2_over_H0sq_today",
    ]
    convergence = {
        key: abs(coarse[key] - fine[key]) / max(abs(fine[key]), 1.0e-300)
        for key in keys
    }
    passed = (
        fine["all_finite"]
        and fine["mphi2_nonnegative_on_background"]
        and fine["meff2_nonnegative_on_background"]
        and all(value < 1.0e-5 for value in convergence.values())
    )
    output = {
        "test": "A2-K5-K1 reconstructed mass stability cross-check",
        "coarse": coarse,
        "fine": fine,
        "convergence_relative_difference": convergence,
        "status": "PASS_BACKGROUND_TACHYON_GATE" if passed else "FAIL_OR_REVIEW",
        "scope": (
            "Background Hessian check only; the full quadratic action and "
            "relativistic perturbation spectrum remain required."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
