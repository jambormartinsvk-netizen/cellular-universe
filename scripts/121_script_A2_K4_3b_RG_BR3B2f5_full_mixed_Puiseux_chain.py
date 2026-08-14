#!/usr/bin/env python
"""BR3B-2f-5 immutable execution clone with two technical repairs.

The physics source remains script 119. This harness makes exactly two checked
in-memory repairs: it closes the malformed ``out.extend`` list, then converts
NumPy boolean gate values to Python ``bool`` before JSON serialization. Script
120 is retained because it exposed the second, serialization-only failure.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "119_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py"
)
BAD_BRACKET = 'vector[fuel_index[("df", 0)]], vector[fuel_index[("Uf", 0)]])'
GOOD_BRACKET = 'vector[fuel_index[("df", 0)]], vector[fuel_index[("Uf", 0)]]])'
BAD_BOOL = '    passed = bool(checks) and all(checks.values())'
GOOD_BOOL = (
    '    checks = {key: bool(value) for key, value in checks.items()}\n'
    '    passed = bool(checks) and all(checks.values())'
)

text = SOURCE.read_text(encoding="utf-8")
if text.count(BAD_BRACKET) != 1 or text.count(BAD_BOOL) != 1:
    raise RuntimeError("immutable repair precondition failed")
repaired = text.replace(BAD_BRACKET, GOOD_BRACKET, 1).replace(BAD_BOOL, GOOD_BOOL, 1)
code = compile(repaired, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
