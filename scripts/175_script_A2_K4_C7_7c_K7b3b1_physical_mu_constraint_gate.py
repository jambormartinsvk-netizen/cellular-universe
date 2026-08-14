#!/usr/bin/env python
"""Immutable rerun of gate 172 with the physical-mu registry export 174."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "172_script_A2_K4_C7_7c_K7b3b_hard_constrained_constraint_gate.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

old_source = (
    "171_script_A2_K4_C7_7c_K7b3b_hard_constrained_slice_corrected_export.py"
)
new_source = (
    "174_script_A2_K4_C7_7c_K7b3b1_slice_and_physical_mu_export.py"
)
if source_text.count(old_source) != 1:
    raise RuntimeError("script 172 source marker is not unique")
source_text = source_text.replace(old_source, new_source, 1)
source_text = source_text.replace(
    "A2-K4 C7.7c-K7b.3b hard-constrained standard coefficient gate",
    "A2-K4 C7.7c-K7b.3b.1 physical-mu hard-constrained coefficient gate",
    1,
)
source_text = source_text.replace(
    "PASS_C7_7C_K7B3B_HARD_CONSTRAINED_STANDARD_GATE",
    "PASS_C7_7C_K7B3B1_PHYSICAL_MU_CONSTRAINT_GATE",
    1,
)
source_text = source_text.replace(
    "REVIEW_C7_7C_K7B3B_HARD_CONSTRAINED_STANDARD_UNCLOSED",
    "REVIEW_C7_7C_K7B3B1_PHYSICAL_MU_CONSTRAINT_UNCLOSED",
    1,
)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
