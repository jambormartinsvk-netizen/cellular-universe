#!/usr/bin/env python3
"""Superseding output labels for the A2-K5-K1 diagnostic S8 projection.

Script 34 calculated both asymmetric KiDS-Legacy widths correctly but used an
ambiguous label for the wider 0.021 denominator.  For a projected value above
the KiDS central value, +0.016 is the formal high-side width.  The 0.021 result
is retained only as a deliberately conservative wider-error ratio.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


BASE_PATH = Path(__file__).with_name(
    "33_script_A2_K5_K1_quasistatic_growth_gate.py"
)
SPEC = importlib.util.spec_from_file_location("k5_k1_growth_corrected", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load script 33: {BASE_PATH}")
BASE33 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE33
SPEC.loader.exec_module(BASE33)


def main() -> int:
    run = BASE33.run(2.5e-4)
    p = BASE33.BASE13.BASE.ModelParameters()
    _, xb0 = BASE33.BASE13.BASE.initial_state(p)
    xc0 = p.omega_m0 - xb0
    xm0 = xc0 + xb0

    baseline_s8 = 0.8745
    kids_central = 0.815
    kids_plus = 0.016
    kids_minus = 0.021

    results = {}
    for key, item in run["results"].items():
        full = item["full_K5_K1"]
        reference = item["GR_like_same_background"]
        delta_m_full = (
            xc0 * full["delta_c_today"] + xb0 * full["delta_b_today"]
        ) / xm0
        delta_m_reference = (
            xc0 * reference["delta_c_today"]
            + xb0 * reference["delta_b_today"]
        ) / xm0
        ratio = delta_m_full / delta_m_reference
        projected_s8 = baseline_s8 * ratio
        results[key] = {
            "weighted_matter_growth_ratio": ratio,
            "diagnostic_projected_S8": projected_s8,
            "formal_asymmetric_high_side_sigma_using_plus_0.016": (
                projected_s8 - kids_central
            ) / kids_plus,
            "conservative_wider_error_ratio_using_0.021": (
                projected_s8 - kids_central
            ) / kids_minus,
        }

    output = {
        "test": "A2-K5-K1 diagnostic S8 projection with corrected labels",
        "supersedes_labels_only": "script 34",
        "physics_and_numerical_values_changed": False,
        "results": results,
        "status": "GROWTH_RISK_CONFIRMED_NOT_A_FULL_S8_PREDICTION",
        "warning": (
            "Neither ratio is a valid likelihood significance because the S8 "
            "projection is not a CMB-normalized Boltzmann prediction."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
