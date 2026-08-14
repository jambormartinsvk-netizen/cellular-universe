#!/usr/bin/env python
"""PF-012-corrected fail-closed physical-mu K7b gate.

This wrapper merges the audited 172/175 transformations directly into the
single wrapper layer 169.  The parser patch is inserted immediately before
169 compiles the final 166 text.  Only rank-metadata validation and explicit
negative-test fault injection are new; the physics producer remains 174.
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
        "174_script_A2_K4_C7_7c_K7b3b1_slice_and_physical_mu_export.py",
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
        'rank_fault_removed = []\n'
        '    if args.fault_remove_rank_key in ("reduced_rank", "both"):\n'
        '        hp_solver.pop("reduced_rank", None)\n'
        '        rank_fault_removed.append("reduced_rank")\n'
        '    if args.fault_remove_rank_key in ("free_count", "both"):\n'
        '        hp_solver.pop("free_count", None)\n'
        '        rank_fault_removed.append("free_count")\n'
        '    checks["hard_constraint_no_conflicts"] = (\n'
        '        hp_solver.get("hard_conflict_count") == 0\n'
        '    )\n'
        '    checks["hard_constraints_below_1e-60"] = (\n'
        '        mp.mpf(str(hp_solver.get("fixed_max_absolute_error", "inf")))\n'
        '        < mp.mpf("1e-60")\n'
        '    )\n'
        '    rank_keys_present = all(\n'
        '        key in hp_solver for key in ("reduced_rank", "free_count")\n'
        '    )\n'
        '    rank_values_plain_int = (\n'
        '        rank_keys_present\n'
        '        and type(hp_solver["reduced_rank"]) is int\n'
        '        and type(hp_solver["free_count"]) is int\n'
        '    )\n'
        '    checks["reduced_standard_rank_keys_present"] = rank_keys_present\n'
        '    checks["reduced_standard_rank_values_plain_int"] = rank_values_plain_int\n'
        '    checks["reduced_standard_system_full_rank"] = (\n'
        '        rank_values_plain_int\n'
        '        and hp_solver["reduced_rank"] == hp_solver["free_count"]\n'
        '    )\n'
        '    checks["hp_standard_solver_not_worse_than_double"] = (\n'
        '        hp_solver.get("hp_not_worse_than_double") is True\n'
        '    )',
    ),
    (
        '"K7b3a_high_precision_standard_solver": hp_solver,',
        '"rank_fault_injection": {\n'
        '            "requested": args.fault_remove_rank_key,\n'
        '            "removed": rank_fault_removed,\n'
        '        },\n'
        '        "K7b3b_hard_constrained_standard_solver": hp_solver,',
    ),
    (
        "PASS_C7_7C_K7B3A_HIGH_PRECISION_STANDARD_GATE",
        "PASS_C7_7C_K7B3B2A_FAIL_CLOSED_PHYSICAL_MU_GATE",
    ),
    (
        "REVIEW_C7_7C_K7B3A_HIGH_PRECISION_STANDARD_UNCLOSED",
        "REVIEW_C7_7C_K7B3B2A_FAIL_CLOSED_PHYSICAL_MU_UNCLOSED",
    ),
    (
        "A2-K4 C7.7c-K7b.3a high-precision standard coefficient gate",
        "A2-K4 C7.7c-K7b.3b.2a PF-012-corrected fail-closed physical-mu gate",
    ),
)

for old, new in replacements:
    if source_text.count(old) != 1:
        raise RuntimeError(f"script 169 merged marker count changed: {old[:100]!r}")
    source_text = source_text.replace(old, new, 1)

old_compile = '''code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
'''
new_compile = '''parser_old = """    parser.add_argument("--dps", type=int, default=80)
    return parser
"""
parser_new = """    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument(
        "--fault-remove-rank-key",
        choices=("none", "reduced_rank", "free_count", "both"),
        default="none",
        help="negative-control metadata fault injection; never changes physics",
    )
    return parser
"""
if source_text.count(parser_old) != 1:
    raise RuntimeError("final script 166 parser marker is not unique")
source_text = source_text.replace(parser_old, parser_new, 1)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
'''
if source_text.count(old_compile) != 1:
    raise RuntimeError("script 169 final compile marker is not unique")
source_text = source_text.replace(old_compile, new_compile, 1)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

