#!/usr/bin/env python
"""Immutable correction: capture the HP registry only for physical_mu.

Script 171 is preserved. Its HP registry was overwritten by the later mu=0
reference solve. This wrapper changes only the capture condition; equations,
anchors, orders and tolerances remain unchanged. No ODE is run.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "171_script_A2_K4_C7_7c_K7b3b_hard_constrained_slice_corrected_export.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

old = "        '        if mode == args.hp_mode:\\n'\n"
new = (
    "        '        if mode == args.hp_mode and "
    "abs(mu-physical_mu) < 1e-30:\\n'\n"
)
if source_text.count(old) != 1:
    raise RuntimeError("script 171 physical-mu capture marker is not unique")
source_text = source_text.replace(old, new, 1)
source_text = source_text.replace(
    '"A2-K4 C7.7c-K7b.3b slice-corrected hard-constrained standard export"',
    '"A2-K4 C7.7c-K7b.3b.1 physical-mu hard-constrained export"',
    1,
)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
