"""Find the two-parameter toy point that hits H0=68 and S8=0.82.

This is deliberately labelled a post-data calibration.  Two parameters are
chosen to hit two targets, so the result has no predictive statistical weight.
It only answers whether the simplified script-09 extension can algebraically
reach the requested point.
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
    target_h0 = 68.0
    target_s8 = 0.82

    # Initial interpolation from the independently reproduced K-grid points.
    k_low, h_low = 0.003, 67.73476481437683
    k_high, h_high = 0.005, 68.70603442192078
    slope = (h_high - h_low) / (k_high - k_low)
    omega_k = k_low + (target_h0 - h_low) / slope

    result = None
    for _ in range(2):
        h, omega_m, xs, states, e, sound_horizon = audit.anchor(omega_k)
        result = (h, omega_m, xs, states, e, sound_horizon)
        omega_k += (target_h0 - 100.0 * h) / slope
    assert result is not None
    h, omega_m, xs, states, e, sound_horizon = audit.anchor(omega_k)

    _, _, lcdm_growth = audit.lcdm_reference()

    def s8_for_drag(gamma_drag: float) -> float:
        d = audit.growth(xs, states, e, gamma_drag)
        sigma8 = 0.811 * d / lcdm_growth
        return sigma8 * math.sqrt(omega_m / 0.3)

    low, high = 0.0, 0.10
    for _ in range(60):
        middle = (low + high) / 2.0
        if s8_for_drag(middle) > target_s8:
            low = middle
        else:
            high = middle
    gamma_drag = (low + high) / 2.0
    s8 = s8_for_drag(gamma_drag)

    omega_r = audit.om_r_total(audit.DELTA_NEFF) / h**2
    w0, wa = audit.cpl_fit(xs, states, e, omega_m, omega_r, omega_k)
    pseudo_chi2 = audit.chi2_3front(w0, wa, s8)

    output = {
        "targets": {"H0": target_h0, "S8": target_s8},
        "post_data_calibrated_parameters": {
            "Omega_K0": omega_k,
            "gamma_drag": gamma_drag,
        },
        "simplified_pipeline_result": {
            "H0": 100.0 * h,
            "Omega_m": omega_m,
            "w0": w0,
            "wa": wa,
            "sound_horizon_Mpc": sound_horizon,
            "S8": s8,
            "chi2_3front": pseudo_chi2,
        },
        "status": "TARGET_REACHABLE_BY_TWO_PARAMETER_POST_DATA_CALIBRATION",
        "statistical_interpretation": "NO_PREDICTIVE_WEIGHT",
        "warning": "full perturbation equations and a real likelihood may move or exclude this point",
    }
    print(json.dumps(output, indent=2, sort_keys=True))

    checks = [abs(100.0 * h - target_h0) < 2.0e-3, abs(s8 - target_s8) < 1.0e-8]
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
