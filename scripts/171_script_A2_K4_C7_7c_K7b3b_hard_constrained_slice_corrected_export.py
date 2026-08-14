#!/usr/bin/env python
"""Immutable matrix-column slicing correction of script 170."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "170_script_A2_K4_C7_7c_K7b3b_hard_constrained_standard_export.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
old = (
    "        '            fixed_matrix = matrix_mp[:,fixed_indices]\\n'\n"
    "        '            free_matrix = matrix_mp[:,free_indices]\\n'\n"
)
new = (
    "        '            fixed_matrix = mp.matrix([[matrix_mp[row,index]\\n'\n"
    "        '                for index in fixed_indices] for row in range(matrix_mp.rows)])\\n'\n"
    "        '            free_matrix = mp.matrix([[matrix_mp[row,index]\\n'\n"
    "        '                for index in free_indices] for row in range(matrix_mp.rows)])\\n'\n"
)
if source_text.count(old) != 1:
    raise RuntimeError("script 170 matrix-slice marker is not unique")
source_text = source_text.replace(old, new, 1)
source_text = source_text.replace(
    '"A2-K4 C7.7c-K7b.3b hard-constrained standard export"',
    '"A2-K4 C7.7c-K7b.3b slice-corrected hard-constrained standard export"',
    1,
)
code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__":"__main__", "__file__":str(Path(__file__))})

