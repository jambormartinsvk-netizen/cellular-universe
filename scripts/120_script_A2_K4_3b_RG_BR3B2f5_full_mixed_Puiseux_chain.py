#!/usr/bin/env python
"""BR3B-2f-5 immutable repair harness for script 119.

Scripts 118 and 119 are deliberately preserved: both fail the Python syntax
gate before executing physics because the four-value ``out.extend`` list in
``solve_fuel`` lacks its final list-closing bracket.  This numbered clone reads
119, verifies that exactly one known malformed token is present, performs that
single repair in memory, compiles it under the new filename, and executes it.
No result file or previous script is overwritten.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "119_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py"
)
BAD = 'vector[fuel_index[("df", 0)]], vector[fuel_index[("Uf", 0)]])'
GOOD = 'vector[fuel_index[("df", 0)]], vector[fuel_index[("Uf", 0)]]])'

text = SOURCE.read_text(encoding="utf-8")
if text.count(BAD) != 1:
    raise RuntimeError("immutable repair precondition failed: expected one token")
repaired = text.replace(BAD, GOOD, 1)
code = compile(repaired, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
