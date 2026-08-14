#!/usr/bin/env python
"""Immutable second fixed-RK4 refinement of script 183."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "183_script_A2_K4_C7_7c_K7c3b_fixed_RK4_step_convergence.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

replacements = (
    (
        "    coarse_steps, coarse_checkpoints, coarse_endpoint = integrate_fixed_rk4(0.0025)\n",
        "    coarse_steps, coarse_checkpoints, coarse_endpoint = integrate_fixed_rk4(0.00125)\n",
    ),
    (
        "    fine_steps, fine_checkpoints, fine_endpoint = integrate_fixed_rk4(0.00125)\n",
        "    fine_steps, fine_checkpoints, fine_endpoint = integrate_fixed_rk4(0.000625)\n",
    ),
    (
        '        "coarse_grid_exactly_100_steps":coarse_steps == 100,\n',
        '        "coarse_grid_exactly_200_steps":coarse_steps == 200,\n',
    ),
    (
        '        "fine_grid_exactly_200_steps":fine_steps == 200,\n',
        '        "fine_grid_exactly_400_steps":fine_steps == 400,\n',
    ),
    (
        '        "rhs_call_cap_2000_respected":rhs_calls <= 2000,\n',
        '        "rhs_call_cap_4000_respected":rhs_calls <= 4000,\n',
    ),
    (
        '        "solver":{"method":"fixed classical RK4","coarse_step":0.0025,\n'
        '            "fine_step":0.00125,"coarse_steps":coarse_steps,\n',
        '        "solver":{"method":"fixed classical RK4","coarse_step":0.00125,\n'
        '            "fine_step":0.000625,"coarse_steps":coarse_steps,\n',
    ),
    (
        '            "rhs_calls":2000},\n',
        '            "rhs_calls":4000},\n',
    ),
    (
        "A2-K4 C7.7c-K7c.3b fixed RK4 step-convergence",
        "A2-K4 C7.7c-K7c.3c second fixed RK4 refinement",
    ),
    (
        "PASS_C7_7C_K7C3B_FIXED_RK4_STEP_CONVERGENCE",
        "PASS_C7_7C_K7C3C_SECOND_FIXED_RK4_REFINEMENT",
    ),
    (
        "REVIEW_C7_7C_K7C3B_FIXED_RK4_UNCLOSED",
        "REVIEW_C7_7C_K7C3C_SECOND_RK4_UNCLOSED",
    ),
)
for old, new in replacements:
    if source_text.count(old) != 1:
        raise RuntimeError(f"script 183 refinement marker changed: {old[:70]!r}")
    source_text = source_text.replace(old, new, 1)

old_checks = "    passed = bool(checks) and all(checks.values())\n"
new_checks = (
    "    checks = {key:bool(value) for key,value in checks.items()}\n"
    "    passed = bool(checks) and all(checks.values())\n"
)
if source_text.count(old_checks) != 1:
    raise RuntimeError("script 183 bool-normalization marker changed")
source_text = source_text.replace(old_checks, new_checks, 1)

old_result = (
    '            "max_normalized_endpoint_step_difference":max_endpoint_difference,\n'
)
new_result = (
    '            "max_normalized_endpoint_step_difference":max_endpoint_difference,\n'
    '            "previous_refinement_difference":1.4432726876921487e-6,\n'
    '            "previous_over_current_difference":1.4432726876921487e-6/'
    'max(max_endpoint_difference,1e-300),\n'
)
if source_text.count(old_result) != 1:
    raise RuntimeError("script 183 result marker changed")
source_text = source_text.replace(old_result, new_result, 1)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
