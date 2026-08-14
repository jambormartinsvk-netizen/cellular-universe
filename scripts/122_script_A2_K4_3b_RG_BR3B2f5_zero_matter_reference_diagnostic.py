#!/usr/bin/env python
"""Diagnostic clone for the two script-108 comparison failures in script 121.

It applies the same two technical repairs as script 121 and adds the solved
zero-matter standard series to the JSON ledger.  It deliberately preserves
the REVIEW verdict of the underlying audit; this file exists only to expose
the coefficients that generate the old/new source-vector difference.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "119_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py"
)
replacements = (
    (
        'vector[fuel_index[("df", 0)]], vector[fuel_index[("Uf", 0)]])',
        'vector[fuel_index[("df", 0)]], vector[fuel_index[("Uf", 0)]]])',
    ),
    (
        '    passed = bool(checks) and all(checks.values())',
        '    checks = {key: bool(value) for key, value in checks.items()}\n'
        '    passed = bool(checks) and all(checks.values())',
    ),
    (
        '"missing_layer_max_norm_zero_matter":zero_missing_norm}',
        '"missing_layer_max_norm_zero_matter":zero_missing_norm,\n'
        '                         "zero_standard_raw":std0}',
    ),
)

text = SOURCE.read_text(encoding="utf-8")
for old, new in replacements:
    if text.count(old) != 1:
        raise RuntimeError(f"diagnostic precondition failed for {old!r}")
    text = text.replace(old, new, 1)
code = compile(text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
