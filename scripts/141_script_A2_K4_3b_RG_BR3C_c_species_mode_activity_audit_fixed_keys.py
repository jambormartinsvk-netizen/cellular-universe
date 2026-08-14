#!/usr/bin/env python
"""Fixed-key clone of script 140; activity thresholds are unchanged."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "140_script_A2_K4_3b_RG_BR3C_c_species_mode_activity_audit.py"
)
text = SOURCE.read_text(encoding="utf-8")
replacements = [
    (
        "state_key_set",
        '                exact_keys = exact_keys and tuple(state.keys()) == STATE_NAMES',
        '                exact_keys = exact_keys and len(state) == len(STATE_NAMES) and set(state) == set(STATE_NAMES)',
    ),
    (
        "rhs_key_set",
        '                exact_keys = exact_keys and tuple(rhs_abs.keys()) == STATE_NAMES',
        '                exact_keys = exact_keys and len(rhs_abs) == len(STATE_NAMES) and set(rhs_abs) == set(STATE_NAMES)',
    ),
    (
        "test_identity",
        '"test":"A2-K4.3b-RG C7.7c species/mode activity audit"',
        '"test":"A2-K4.3b-RG C7.7c species/mode activity audit fixed key sets"',
    ),
    (
        "review_verdict",
        '"REVIEW_C7_7C_UNRESOLVED_COMPONENTS"',
        '"REVIEW_C7_7C_UNRESOLVED_COMPONENTS_FIXED_KEYS"',
    ),
]
for label, old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"script 141 transform precondition {label!r}: expected 1, got {count}"
        )
    text = text.replace(old, new, 1)
code = compile(text, str(Path(__file__)), "exec")
exec(code, {"__name__":"__main__", "__file__":str(Path(__file__))})

