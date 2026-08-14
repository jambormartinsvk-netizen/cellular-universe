#!/usr/bin/env python
"""Immutable parser-path correction of composite K7a-J4 script 163."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "163_script_A2_K4_C7_7c_K7a_J4_composite_projected_jacobian_gate.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

old_path = '''    projected_audit = dict(
        surface_result.get("K7a_projected_jacobian_audit", {})
    )
'''
new_path = '''    zero_integration_diagnostic = dict(
        surface_result.get("zero_integration_jacobian_diagnostic", {})
    )
    projected_audit = dict(
        zero_integration_diagnostic.get("K7a_projected_jacobian_audit", {})
    )
'''
if source_text.count(old_path) != 1:
    raise RuntimeError("script 163 projected-audit path marker is not unique")
source_text = source_text.replace(old_path, new_path, 1)
source_text = source_text.replace(
    '"A2-K4 C7.7c-K7a-J4 composite projected Jacobian gate"',
    '"A2-K4 C7.7c-K7a-J4b parser-corrected composite projected Jacobian gate"',
    1,
)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

