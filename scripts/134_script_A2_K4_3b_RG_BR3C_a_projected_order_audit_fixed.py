#!/usr/bin/env python
"""Fixed clone of script 133 with context-unique source-verdict transforms."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "131_script_A2_K4_3b_RG_BR3C_a_order5_order6_state_audit.py"
)

replacements = [
    (
        "source",
        '"130_script_A2_K4_3b_RG_BR3C_a_two_surface_state_export.py"',
        '"132_script_A2_K4_3b_RG_BR3C_a_registered_zero_projection.py"',
    ),
    (
        "source_verdict_order5",
        '        "order5_source_pass": order5.get("execution_verdict")\n'
        '        == "PASS_BR3C_A_TWO_SURFACE_STATE",',
        '        "order5_source_pass": order5.get("execution_verdict")\n'
        '        == "PASS_BR3C_A_REGISTERED_ZERO_STATE",',
    ),
    (
        "source_verdict_order6",
        '        "order6_source_pass": order6.get("execution_verdict")\n'
        '        == "PASS_BR3C_A_TWO_SURFACE_STATE",',
        '        "order6_source_pass": order6.get("execution_verdict")\n'
        '        == "PASS_BR3C_A_REGISTERED_ZERO_STATE",',
    ),
    (
        "normalization",
        '        checks[f"{mode}_same_normalization_anchor"] = norm5 == norm6',
        '        checks[f"{mode}_same_normalization_definition"] = (\n'
        '            norm5["seed_amplitude"] == norm6["seed_amplitude"]\n'
        '            and norm5["fuel_fraction_coefficient"] == norm6["fuel_fraction_coefficient"]\n'
        '            and norm5["anchor_name"] == norm6["anchor_name"]\n'
        '            and norm5["anchor_expected"] == norm6["anchor_expected"])\n'
        '        checks[f"{mode}_anchor_values_agree_below_2e-12"] = (\n'
        '            abs(norm5["anchor_value"]-norm6["anchor_value"]) < 2e-12)',
    ),
    (
        "test_identity",
        '"test": "A2-K4.3b-RG BR3C-a order-5/order-6 state audit"',
        '"test": "A2-K4.3b-RG BR3C-a projected order-5/order-6 state audit"',
    ),
    (
        "pass_verdict",
        '"PASS_BR3C_A_ORDER5_ORDER6_STATE_AUDIT"',
        '"PASS_BR3C_A_PROJECTED_ORDER5_ORDER6_AUDIT"',
    ),
    (
        "review_verdict",
        '"REVIEW_BR3C_A_ORDER_AUDIT_UNCLOSED"',
        '"REVIEW_BR3C_A_PROJECTED_ORDER_AUDIT_UNCLOSED"',
    ),
]

text = SOURCE.read_text(encoding="utf-8")
for label, old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"script 134 transform precondition {label!r}: expected 1, got {count}"
        )
    text = text.replace(old, new, 1)

code = compile(text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

