#!/usr/bin/env python
"""Immutable normalized-basis correction of diagnostic script 181."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "181_script_A2_K4_C7_7c_K7c3a_exact_linear_operator_profile.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

old_probe = '''    physical_operator = np.column_stack([
        physical_rhs(x_start, np.eye(13, dtype=float)[:, column])-zero_rhs
        for column in range(13)
    ])
'''
new_probe = '''    physical_operator = np.column_stack([
        (physical_rhs(x_start, np.eye(13, dtype=float)[:, column]*scale[column])-zero_rhs)
        /scale[column] for column in range(13)
    ])
'''
if source_text.count(old_probe) != 1:
    raise RuntimeError("script 181 operator-probe marker is not unique")
source_text = source_text.replace(old_probe, new_probe, 1)
source_text = source_text.replace(
    '"method":"exact basis-column evaluation f(e_j)-f(0); no finite-difference step",',
    '"method":"exact linear column (f(S_j e_j)-f(0))/S_j; normalized probe amplitude 1; no FD step",',
    1,
)
source_text = source_text.replace(
    "A2-K4 C7.7c-K7c.3a exact linear-operator profile",
    "A2-K4 C7.7c-K7c.3a.1 normalized-basis linear-operator profile",
    1,
)
source_text = source_text.replace(
    "PASS_C7_7C_K7C3A_EXACT_LINEAR_OPERATOR_PROFILE",
    "PASS_C7_7C_K7C3A1_NORMALIZED_BASIS_OPERATOR_PROFILE",
    1,
)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
