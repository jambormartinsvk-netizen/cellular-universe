#!/usr/bin/env python
"""Audited BR3B-2f-5 execution clone.

This immutable harness applies three checked repairs to script 119:

1. close the malformed fuel-ledger list (syntax only);
2. convert NumPy gate flags to Python booleans (JSON only);
3. correct the script-108 comparison source from photon to free-streaming
   velocity in the free-streaming shear equation.

The third correction changes only the legacy comparison oracle.  The coupled
11-row physical system solved by script 119 is unchanged.  CLASS implements
the ultra-relativistic shear derivative with ``theta_ur`` itself, confirming
that the source must use ``U_fs`` rather than ``U_gamma``.
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
        'jns = 8/15*(uge-ugl)',
        'jns = 8/15*(une-unl)',
    ),
)

text = SOURCE.read_text(encoding="utf-8")
for old, new in replacements:
    if text.count(old) != 1:
        raise RuntimeError(f"audited clone precondition failed for {old!r}")
    text = text.replace(old, new, 1)
code = compile(text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
