#!/usr/bin/env python3
"""Amplitude-rescue audit for the failed A3-K5/K1 growth screen.

For fixed transfer shape and background, sigma8 and S8 scale as sqrt(A_s).
This script asks how far the registered A_s=2.1e-9 would have to move to
bring each conservative A3 hybrid result down to the predeclared
KiDS-Legacy 3-sigma screening edge S8=0.863.

The Planck comparison uses ln(10^10 A_s)=3.044 +/- 0.014 from the published
base-LambdaCDM TT,TE,EE+lowE+lensing parameter table.  Its sigma ratios are
diagnostics, not a likelihood for K5/K1.
"""

from __future__ import annotations

import json
import math


AS_REGISTERED = 2.1e-9
LN10AS_PLANCK = 3.044
LN10AS_PLANCK_SIGMA = 0.014
S8_SCREEN = 0.863

CASES = {
    "constant_w_f_hybrid": 0.9836423799480062,
    "registered_CPL_hybrid": 1.0062658626394954,
    "older_internal_projection": 0.920,
}


def main() -> int:
    results = {}
    for label, s8 in CASES.items():
        required_as = AS_REGISTERED * (S8_SCREEN / s8) ** 2
        ln10as_required = math.log(1.0e10 * required_as)
        results[label] = {
            "input_S8": s8,
            "required_As_for_S8_screen": required_as,
            "required_As_fraction_of_registered": required_as / AS_REGISTERED,
            "required_fractional_reduction": 1.0 - required_as / AS_REGISTERED,
            "required_ln_1e10_As": ln10as_required,
            "diagnostic_distance_from_Planck_lnAs_sigma": (
                ln10as_required - LN10AS_PLANCK
            ) / LN10AS_PLANCK_SIGMA,
        }

    output = {
        "test": "A3-K5/K1 primordial-amplitude rescue requirement",
        "inputs": {
            "registered_As": AS_REGISTERED,
            "S8_screen": S8_SCREEN,
            "Planck_ln_1e10_As": LN10AS_PLANCK,
            "Planck_ln_1e10_As_sigma": LN10AS_PLANCK_SIGMA,
        },
        "scaling": "S8 proportional to sqrt(As) at fixed transfer/background",
        "results": results,
        "status": "AMPLITUDE_RESCUE_REQUIRES_LARGE_CMB_INCOMPATIBLE_SHIFT",
        "scope_warning": (
            "Planck sigma distances assume the base-LambdaCDM marginalized "
            "lnAs width and are not a K5/K1 likelihood."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
