#!/usr/bin/env python
"""C7.7c-K3 clone of 142 changing only DOP853 to implicit Radau."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "142_script_A2_K4_3b_RG_C7_7c_K2_normalized_component_evolution.py"
)
text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\ntext = text.replace"
if text.count(MARKER) != 1:
    raise RuntimeError("script 142 Radau-extension marker is not unique")
addition = r'''    (
        "Radau_solver",
        '                        method="DOP853",',
        '                        method="Radau",',
    ),
    (
        "Radau_solver_output",
        '            "method": "DOP853",',
        '            "method": "Radau",',
    ),
    (
        "Radau_test_identity",
        '"test": "A2-K4.3b-RG C7.7c-K2 normalized checkpoint component export"',
        '"test": "A2-K4.3b-RG C7.7c-K3 normalized Radau component export"',
    ),
    (
        "Radau_execution_verdict",
        '"PASS_C7_7C_K2_NORMALIZED_COMPONENT_EXPORT"',
        '"PASS_C7_7C_K3_NORMALIZED_RADAU_EXPORT"',
    ),
'''
text = text.replace(MARKER, addition + "'''\n\ntext = text.replace", 1)
code = compile(text, str(Path(__file__)), "exec")
exec(code, {"__name__":"__main__", "__file__":str(Path(__file__))})

