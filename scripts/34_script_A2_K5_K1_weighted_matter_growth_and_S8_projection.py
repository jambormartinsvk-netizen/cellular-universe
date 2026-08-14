#!/usr/bin/env python3
"""Weight K5-K1 CDM+baryon growth and make a labelled S8 projection.

The registered 0.8745 S8 value is an internal pre-A2 pipeline output, not a
CLASS/CAMB result.  Multiplying it by the reconstructed action's matter-growth
ratio is therefore a diagnostic projection only and must not be reported as a
new exact prediction.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


BASE_PATH = Path(__file__).with_name(
    "33_script_A2_K5_K1_quasistatic_growth_gate.py"
)
SPEC = importlib.util.spec_from_file_location("k5_k1_growth", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load script 33: {BASE_PATH}")
BASE33 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE33
SPEC.loader.exec_module(BASE33)


def main() -> int:
    run = BASE33.run(2.5e-4)
    p = BASE33.BASE13.BASE.ModelParameters()
    _, xb0 = BASE33.BASE13.BASE.initial_state(p)
    xc0 = p.omega_m0-xb0
    xm0 = xc0+xb0

    baseline_s8 = 0.8745
    kids_central = 0.815
    kids_plus = 0.016
    kids_minus = 0.021

    results = {}
    for key, item in run["results"].items():
        full = item["full_K5_K1"]
        reference = item["GR_like_same_background"]
        delta_m_full = (xc0*full["delta_c_today"]+xb0*full["delta_b_today"])/xm0
        delta_m_reference = (
            xc0*reference["delta_c_today"]+xb0*reference["delta_b_today"]
        )/xm0
        ratio = delta_m_full/delta_m_reference
        projected_s8 = baseline_s8*ratio
        results[key] = {
            "delta_m_full": delta_m_full,
            "delta_m_GR_like": delta_m_reference,
            "weighted_matter_growth_ratio": ratio,
            "diagnostic_projected_S8": projected_s8,
            "conservative_high_side_KiDS_sigma_using_0.021": (
                projected_s8-kids_central
            )/kids_minus,
            "narrow_high_side_KiDS_sigma_using_0.016": (
                projected_s8-kids_central
            )/kids_plus,
        }

    ratios = [v["weighted_matter_growth_ratio"] for v in results.values()]
    enhanced = all(r > 1.0 for r in ratios)
    output = {
        "test": "A2-K5-K1 weighted matter growth and diagnostic S8 projection",
        "present_density_weights": {
            "X_c0": xc0,
            "X_b0": xb0,
            "X_m0": xm0,
        },
        "inputs": {
            "internal_pre_A2_baseline_S8": baseline_s8,
            "KiDS_Legacy_S8": kids_central,
            "KiDS_plus": kids_plus,
            "KiDS_minus": kids_minus,
        },
        "results": results,
        "checks": {
            "weighted_matter_growth_enhanced_on_all_scales": enhanced,
            "projected_S8_moves_in_wrong_direction": all(
                v["diagnostic_projected_S8"] > baseline_s8
                for v in results.values()
            ),
        },
        "status": "GROWTH_RISK_CONFIRMED_NOT_A_FULL_S8_PREDICTION",
        "warning": (
            "The projection inherits the unvalidated 0.8745 normalization. "
            "A death verdict requires the full scalar+CDM Boltzmann system and "
            "a CMB-normalized likelihood."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if enhanced else 1


if __name__ == "__main__":
    raise SystemExit(main())

