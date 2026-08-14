#!/usr/bin/env python
"""PF-012-corrected immutable successor of regression aggregate 190."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "190_script_A2_K4_C7_7c_K7b_P0_fail_closed_regression_gate.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

replacements = (
    (
        "189_script_A2_K4_C7_7c_K7b3b2_fail_closed_physical_mu_gate.py",
        "192_script_A2_K4_C7_7c_K7b3b2a_fail_closed_physical_mu_gate.py",
        2,
    ),
    (
        "PASS_C7_7C_K7B3B2_FAIL_CLOSED_PHYSICAL_MU_GATE",
        "PASS_C7_7C_K7B3B2A_FAIL_CLOSED_PHYSICAL_MU_GATE",
        1,
    ),
    (
        "REVIEW_C7_7C_K7B3B2_FAIL_CLOSED_PHYSICAL_MU_UNCLOSED",
        "REVIEW_C7_7C_K7B3B2A_FAIL_CLOSED_PHYSICAL_MU_UNCLOSED",
        1,
    ),
    (
        "A2-K4 C7.7c K7b P0 fail-closed regression gate",
        "A2-K4 C7.7c K7b P0a PF-012-corrected fail-closed regression gate",
        1,
    ),
    (
        "PASS_C7_7C_K7B_P0_FAIL_CLOSED_REGRESSION",
        "PASS_C7_7C_K7B_P0A_PF012_CORRECTED_REGRESSION",
        1,
    ),
    (
        "REVIEW_C7_7C_K7B_P0_FAIL_CLOSED_UNCLOSED",
        "REVIEW_C7_7C_K7B_P0A_PF012_CORRECTED_UNCLOSED",
        1,
    ),
)
for old, new, expected_count in replacements:
    if source_text.count(old) != expected_count:
        raise RuntimeError(
            f"script 190 successor marker count changed: {old!r}"
        )
    source_text = source_text.replace(old, new)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

