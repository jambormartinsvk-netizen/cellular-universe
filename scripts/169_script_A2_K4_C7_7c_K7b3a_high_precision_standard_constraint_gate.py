#!/usr/bin/env python
"""Immutable K7b.3a gate using script 168 high-precision standard coefficients.

This extension of script 166 retains every K7b.1 check and adds the
preregistered activity-relative D-prime gate plus high-precision solver
provenance. No ODE is integrated.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "166_script_A2_K4_C7_7c_K7b1_high_precision_coefficient_constraint_audit.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

old_source = "165_script_A2_K4_C7_7c_K7b_registered_coefficient_export.py"
if source_text.count(old_source) != 2:
    raise RuntimeError("script 166 source-name marker count changed")
source_text = source_text.replace(
    old_source,
    "168_script_A2_K4_C7_7c_K7b3a_high_precision_standard_coefficient_export.py",
)

old_command = '''        "--fuel-fraction-coefficient", "1",
    ]
'''
new_command = '''        "--fuel-fraction-coefficient", "1",
        "--hp-mode", args.mode,
    ]
'''
if source_text.count(old_command) != 1:
    raise RuntimeError("script 166 source-command marker is not unique")
source_text = source_text.replace(old_command, new_command, 1)

old_registry = '''    standard = dict(registry.get("standard", {}))
    fractional = dict(registry.get("fractional", {}))
'''
new_registry = '''    hp_registry_all = dict(
        source.get("K7b3a_high_precision_standard_registry", {})
    )
    standard = dict(hp_registry_all.get(args.mode, {}))
    fractional = dict(registry.get("fractional", {}))
'''
if source_text.count(old_registry) != 1:
    raise RuntimeError("script 166 coefficient-registry marker is not unique")
source_text = source_text.replace(old_registry, new_registry, 1)

old_pass = '''    passed = all(bool(value) for value in checks.values())
    deadline()
'''
new_pass = '''    hp_solver_all = dict(
        source.get("K7b3a_high_precision_solver_audit", {})
    )
    hp_solver = dict(hp_solver_all.get(args.mode, {}))
    D_activity_relative_error = abs(
        rhs_values[3]-derivative_values[3]
    )/max(abs(derivative_values[3]), mp.mpf("1e-300"))
    checks["hp_standard_registry_present"] = bool(standard)
    checks["hp_standard_solver_full_rank"] = hp_solver.get("rank") == 88
    checks["hp_standard_solver_not_worse_than_double"] = (
        hp_solver.get("hp_not_worse_than_double") is True
    )
    checks["NID_D_activity_relative_below_0p1"] = (
        D_activity_relative_error < mp.mpf("0.1")
        if args.mode == "NID" else True
    )
    passed = all(bool(value) for value in checks.values())
    deadline()
'''
if source_text.count(old_pass) != 1:
    raise RuntimeError("script 166 pass marker is not unique")
source_text = source_text.replace(old_pass, new_pass, 1)

old_payload = '''        "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7B1_COEFFICIENT_CONSTRAINT_AUDIT"
            if passed else "REVIEW_C7_7C_K7B1_COEFFICIENT_CONSTRAINT_UNCLOSED"
        ),
'''
new_payload = '''        "K7b3a_high_precision_standard_solver": hp_solver,
        "D_activity_relative_error": float(D_activity_relative_error),
        "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7B3A_HIGH_PRECISION_STANDARD_GATE"
            if passed else "REVIEW_C7_7C_K7B3A_HIGH_PRECISION_STANDARD_UNCLOSED"
        ),
'''
if source_text.count(old_payload) != 1:
    raise RuntimeError("script 166 payload marker is not unique")
source_text = source_text.replace(old_payload, new_payload, 1)
source_text = source_text.replace(
    '"A2-K4 C7.7c-K7b.1 high-precision coefficient and constraint audit"',
    '"A2-K4 C7.7c-K7b.3a high-precision standard coefficient gate"',
    1,
)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

