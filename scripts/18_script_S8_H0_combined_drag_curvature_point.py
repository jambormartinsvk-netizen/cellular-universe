"""Audit the proposed combined point Omega_K=0.002, gamma_drag=0.015.

The calculation reuses the explicit equations and CMB anchoring implemented in
script 17.  It is a reproduction inside the simplified script-09 framework,
not a full perturbation solution or cosmological likelihood.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path


def load_grid_module():
    path = Path(__file__).with_name("17_script_S8_H0_drag_curvature_grid_audit.py")
    spec = importlib.util.spec_from_file_location("grid_audit_17", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    audit = load_grid_module()
    omega_k0 = 0.002
    gamma_drag = 0.015

    _, _, lcdm_growth = audit.lcdm_reference()
    h, omega_m, xs, states, e, sound_horizon = audit.anchor(omega_k0)
    omega_r = audit.om_r_total(audit.DELTA_NEFF) / h**2
    w0, wa = audit.cpl_fit(xs, states, e, omega_m, omega_r, omega_k0)
    d = audit.growth(xs, states, e, gamma_drag)
    sigma8 = 0.811 * d / lcdm_growth
    s8 = sigma8 * math.sqrt(omega_m / 0.3)
    pseudo_chi2 = audit.chi2_3front(w0, wa, s8)

    output = {
        "input": {"Omega_K0": omega_k0, "gamma_drag": gamma_drag},
        "simplified_pipeline_result": {
            "H0": 100.0 * h,
            "Omega_m": omega_m,
            "w0": w0,
            "wa": wa,
            "sound_horizon_Mpc": sound_horizon,
            "sigma8": sigma8,
            "S8": s8,
            "chi2_3front": pseudo_chi2,
        },
        "distance_to_stated_goal": {
            "H0_minus_68": 100.0 * h - 68.0,
            "S8_minus_0p82": s8 - 0.82,
        },
        "status": "NUMERICALLY_REPRODUCIBLE_INSIDE_SIMPLIFIED_PIPELINE",
        "physical_limitations": [
            "drag is applied to the single total-matter perturbation, not only to ash/CDM",
            "energy and momentum transfer perturbations are absent",
            "chi2_3front is not a likelihood and contains no H0 or Omega_m term",
            "two new parameters are selected after inspecting the target data",
        ],
    }
    print(json.dumps(output, indent=2, sort_keys=True))

    checks = [
        66.0 < 100.0 * h < 69.0,
        0.75 < s8 < 0.90,
        math.isfinite(pseudo_chi2),
    ]
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
