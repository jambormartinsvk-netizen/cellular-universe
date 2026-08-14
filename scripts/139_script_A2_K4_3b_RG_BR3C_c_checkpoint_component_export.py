#!/usr/bin/env python
"""Immutable output-only extension of script 136 for C7.7c activity audit."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "136_script_A2_K4_3b_RG_BR3C_b_segmented_early_evolution.py"
)
source = SOURCE.read_text(encoding="utf-8")
replacements = [
    (
        "checkpoint_component_export",
        '                        "rhs_max_abs": float(np.max(np.abs(rhs_end))),\n'
        '                        "finite": checkpoint_finite,',
        '                        "rhs_max_abs": float(np.max(np.abs(rhs_end))),\n'
        '                        "state": {name:float(value) for name, value in zip(STATE_NAMES, y)},\n'
        '                        "rhs_abs": {name:float(abs(value)) for name, value in zip(STATE_NAMES, rhs_end)},\n'
        '                        "finite": checkpoint_finite,',
    ),
    (
        "test_identity",
        '"test": "A2-K4.3b-RG BR3C-b segmented early evolution"',
        '"test": "A2-K4.3b-RG C7.7c checkpoint component export"',
    ),
    (
        "execution_verdict",
        '"PASS_BR3C_B_SEGMENTED_EARLY_EVOLUTION"',
        '"PASS_C7_7C_CHECKPOINT_COMPONENT_EXPORT"',
    ),
    (
        "physical_verdict",
        '"K4 survives C7.7b finite early evolution"',
        '"C7.7b reproduced; C7.7c activity still requires independent audit"',
    ),
    (
        "fine_depth",
        '"fine_depth": "66.5/100" if passed else "66.2/100"',
        '"fine_depth": "66.5/100", "C7_7c_score_status":"NOT_YET_AWARDED"',
    ),
]
for label, old, new in replacements:
    count = source.count(old)
    if count != 1:
        raise RuntimeError(
            f"script 139 transform precondition {label!r}: expected 1, got {count}"
        )
    source = source.replace(old, new, 1)
code = compile(source, str(Path(__file__)), "exec")
exec(code, {"__name__":"__main__", "__file__":str(Path(__file__))})

