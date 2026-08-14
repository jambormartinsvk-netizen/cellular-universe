#!/usr/bin/env python3
"""Recoverable numerical subset of the corrected script-45 audit.

Script 51 deliberately tested the submitted minus-projector force as a
negative drag rate.  That run overflowed to NaN before script 51 could
serialize the already completed physical-sign runs.  This successor keeps
the same corrected equations, omits that analytically anti-damping branch,
and serializes the finite runs.  Script 51 and its overflow remain part of
the audit trail.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys


SOURCE = Path(__file__).with_name(
    "51_script_A2_K11_script45_equation_and_sign_audit.py"
)
SPEC = importlib.util.spec_from_file_location("k11_corrected", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load {SOURCE}")
K11 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = K11
SPEC.loader.exec_module(K11)


def main() -> int:
    q = 1.0e-5
    lam = 0.15
    gamma = 0.03

    no_drag = K11.run(2.5e-4, q, lam, 0.0)
    physical = K11.run(2.5e-4, q, lam, gamma)
    physical_finer = K11.run(1.25e-4, q, lam, gamma)
    half_k = K11.run(2.5e-4, q / 2.0, lam, gamma)

    log_fine = math.log(max(physical_finer["absolute_transfer"], 1.0e-300))
    step_error = abs(
        math.log(max(physical["absolute_transfer"], 1.0e-300)) - log_fine
    ) / max(abs(log_fine), 1.0)
    k_error = abs(
        math.log(max(half_k["absolute_transfer"], 1.0e-300))
        - math.log(max(physical["absolute_transfer"], 1.0e-300))
    ) / max(abs(math.log(max(physical["absolute_transfer"], 1.0e-300))), 1.0)

    output = {
        "test": "Recoverable finite runs of corrected script-45 audit",
        "correct_K1_no_drag": no_drag,
        "physical_drag_gamma_0p03": physical,
        "physical_drag_finer_background": physical_finer,
        "physical_drag_half_k": half_k,
        "drag_gain_relative_to_correct_K1": (
            physical_finer["absolute_transfer"] / no_drag["absolute_transfer"]
        ),
        "step_log_transfer_relative_difference": step_error,
        "k_log_transfer_relative_difference": k_error,
        "submitted_minus_projector": {
            "analytic_interpretation": "anti-drag for metric signature (-,+,+,+)",
            "script51_observed_status": (
                "Radau overflow followed by inf/NaN in submitted-minus branch"
            ),
            "reason_not_repeated_here": (
                "preserve finite results and avoid hiding them behind the "
                "already documented explosive branch"
            ),
        },
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
