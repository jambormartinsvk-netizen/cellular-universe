#!/usr/bin/env python
"""Immutable physical gate for the slice-corrected hard-constrained export 171.

The script reuses every K7b.1 coefficient/constraint check, replaces only the
standard Puiseux registry by the 80-digit hard-constrained registry, and adds
the preregistered hard-anchor and NID D-prime activity checks. No ODE is run.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "169_script_A2_K4_C7_7c_K7b3a_high_precision_standard_constraint_gate.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

replacements = (
    (
        "168_script_A2_K4_C7_7c_K7b3a_high_precision_standard_coefficient_export.py",
        "171_script_A2_K4_C7_7c_K7b3b_hard_constrained_slice_corrected_export.py",
    ),
    (
        "K7b3a_high_precision_standard_registry",
        "K7b3b_high_precision_standard_registry",
    ),
    (
        "K7b3a_high_precision_solver_audit",
        "K7b3b_high_precision_solver_audit",
    ),
    (
        'checks["hp_standard_solver_full_rank"] = hp_solver.get("rank") == 88\n'
        '    checks["hp_standard_solver_not_worse_than_double"] = (\n'
        '        hp_solver.get("hp_not_worse_than_double") is True\n'
        '    )',
        'checks["hard_constraint_no_conflicts"] = (\n'
        '        hp_solver.get("hard_conflict_count") == 0\n'
        '    )\n'
        '    checks["hard_constraints_below_1e-60"] = (\n'
        '        mp.mpf(str(hp_solver.get("fixed_max_absolute_error", "inf")))\n'
        '        < mp.mpf("1e-60")\n'
        '    )\n'
        '    checks["reduced_standard_system_full_rank"] = (\n'
        '        hp_solver.get("reduced_rank") == hp_solver.get("free_count")\n'
        '    )\n'
        '    checks["hp_standard_solver_not_worse_than_double"] = (\n'
        '        hp_solver.get("hp_not_worse_than_double") is True\n'
        '    )',
    ),
    (
        '"K7b3a_high_precision_standard_solver": hp_solver,',
        '"K7b3b_hard_constrained_standard_solver": hp_solver,',
    ),
    (
        "PASS_C7_7C_K7B3A_HIGH_PRECISION_STANDARD_GATE",
        "PASS_C7_7C_K7B3B_HARD_CONSTRAINED_STANDARD_GATE",
    ),
    (
        "REVIEW_C7_7C_K7B3A_HIGH_PRECISION_STANDARD_UNCLOSED",
        "REVIEW_C7_7C_K7B3B_HARD_CONSTRAINED_STANDARD_UNCLOSED",
    ),
    (
        "A2-K4 C7.7c-K7b.3a high-precision standard coefficient gate",
        "A2-K4 C7.7c-K7b.3b hard-constrained standard coefficient gate",
    ),
)

for old, new in replacements:
    if source_text.count(old) != 1:
        raise RuntimeError(f"script 169 marker count changed: {old[:80]!r}")
    source_text = source_text.replace(old, new, 1)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
