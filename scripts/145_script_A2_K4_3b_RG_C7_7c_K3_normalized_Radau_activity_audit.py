#!/usr/bin/env python
"""C7.7c-K3 activity audit; same criteria as 143 with Radau and headroom."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "143_script_A2_K4_3b_RG_C7_7c_K2_normalized_activity_audit.py"
)
text = SOURCE.read_text(encoding="utf-8")
replacements = [
    (
        "source",
        '"142_script_A2_K4_3b_RG_C7_7c_K2_normalized_component_evolution.py"',
        '"144_script_A2_K4_3b_RG_C7_7c_K3_normalized_Radau_evolution.py"',
    ),
    (
        "child_internal_limit",
        '        "--max-runtime-seconds", "50",',
        '        "--max-runtime-seconds", "45",',
    ),
    (
        "child_timeout_headroom",
        '        timeout=min(55.0, args.max_runtime_seconds), check=False',
        '        timeout=min(50.0, args.max_runtime_seconds), check=False',
    ),
    (
        "source_verdict",
        '== "PASS_C7_7C_K2_NORMALIZED_COMPONENT_EXPORT",',
        '== "PASS_C7_7C_K3_NORMALIZED_RADAU_EXPORT",',
    ),
    (
        "test_identity",
        '"test":"A2-K4.3b-RG C7.7c-K2 normalized species/mode activity audit"',
        '"test":"A2-K4.3b-RG C7.7c-K3 normalized Radau activity audit"',
    ),
    (
        "pass_verdict",
        '"PASS_C7_7C_K2_NORMALIZED_ACTIVITY"',
        '"PASS_C7_7C_K3_NORMALIZED_RADAU_ACTIVITY"',
    ),
    (
        "review_verdict",
        '"REVIEW_C7_7C_K2_NORMALIZED_ACTIVITY_UNCLOSED"',
        '"REVIEW_C7_7C_K3_NORMALIZED_RADAU_UNCLOSED"',
    ),
]
for label, old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"script 145 transform precondition {label!r}: expected 1, got {count}"
        )
    text = text.replace(old, new, 1)
code = compile(text, str(Path(__file__)), "exec")
exec(code, {"__name__":"__main__", "__file__":str(Path(__file__))})

