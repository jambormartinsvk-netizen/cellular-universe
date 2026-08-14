#!/usr/bin/env python
"""Immutable JSON-bool correction of fixed-RK4 script 183."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "183_script_A2_K4_C7_7c_K7c3b_fixed_RK4_step_convergence.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
old = "    passed = bool(checks) and all(checks.values())\n"
new = (
    "    checks = {key:bool(value) for key,value in checks.items()}\n"
    "    passed = bool(checks) and all(checks.values())\n"
)
if source_text.count(old) != 1:
    raise RuntimeError("script 183 checks-normalization marker is not unique")
source_text = source_text.replace(old, new, 1)
source_text = source_text.replace(
    "A2-K4 C7.7c-K7c.3b fixed RK4 step-convergence",
    "A2-K4 C7.7c-K7c.3b fixed RK4 JSON-bool-corrected convergence",
    1,
)
source_text = source_text.replace(
    "PASS_C7_7C_K7C3B_FIXED_RK4_STEP_CONVERGENCE",
    "PASS_C7_7C_K7C3B_FIXED_RK4_JSON_BOOL_CORRECTED",
    1,
)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
