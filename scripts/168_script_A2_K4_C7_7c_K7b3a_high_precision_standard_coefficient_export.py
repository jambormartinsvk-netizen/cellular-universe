#!/usr/bin/env python
"""Immutable high-precision standard-coefficient extension of script 165.

Only the already assembled standard Puiseux least-squares system is re-solved
at 80 dps.  The original numpy solution and diagnostics remain available.
No ODE is integrated.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "165_script_A2_K4_C7_7c_K7b_registered_coefficient_export.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\nextended = source_text"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 165 K7b.3a extension marker is not unique")

addition = r'''    (
        "K7b3a_mpmath_import",
        'import numpy as np\n',
        'import numpy as np\nimport mpmath as mp\n',
    ),
    (
        "K7b3a_mode_parser",
        '    parser.add_argument("--x-reference", type=float, default=-18.0)',
        '    parser.add_argument("--x-reference", type=float, default=-18.0)\n'
        '    parser.add_argument("--hp-mode", choices=("NID","NIV"), default="NID")',
    ),
    (
        "K7b3a_registry_initialization",
        '    checks = {}; results = {}; state_surfaces = {}; coefficient_registry = {}',
        '    checks = {}; results = {}; state_surfaces = {}; coefficient_registry = {}\n'
        '    hp_standard_registry = {}; hp_solver_audit = {}',
    ),
    (
        "K7b3a_standard_normal_equation_solve",
        '        solution, _, rank, singular = np.linalg.lstsq(matrix, rhs, rcond=None)\n'
        '        residual = matrix @ solution - rhs\n'
        '        scale = max(np.max(np.abs(matrix) * np.maximum(np.abs(solution)[None, :], 1e-300)),\n'
        '                    np.max(np.abs(rhs)), 1e-300)\n'
        '        standard = vector_to_standard(solution)',
        '        double_solution, _, rank, singular = np.linalg.lstsq(matrix, rhs, rcond=None)\n'
        '        solution = double_solution\n'
        '        if mode == args.hp_mode:\n'
        '            deadline()\n'
        '            mp.mp.dps = 80\n'
        '            matrix_mp = mp.matrix([[mp.mpf(repr(float(value)))\n'
        '                for value in row] for row in matrix])\n'
        '            rhs_mp = mp.matrix([mp.mpf(repr(float(value))) for value in rhs])\n'
        '            normal_mp = matrix_mp.T*matrix_mp\n'
        '            normal_rhs_mp = matrix_mp.T*rhs_mp\n'
        '            solution_mp = mp.lu_solve(normal_mp, normal_rhs_mp)\n'
        '            hp_linear_residual = matrix_mp*solution_mp-rhs_mp\n'
        '            double_mp = mp.matrix([mp.mpf(repr(float(value)))\n'
        '                for value in double_solution])\n'
        '            double_linear_residual = matrix_mp*double_mp-rhs_mp\n'
        '            hp_max_residual = max(abs(value) for value in hp_linear_residual)\n'
        '            double_max_residual = max(abs(value) for value in double_linear_residual)\n'
        '            hp_normal_residual = normal_mp*solution_mp-normal_rhs_mp\n'
        '            solution = np.asarray([float(value) for value in solution_mp])\n'
        '            hp_standard_registry[mode] = {name:{str(exponent):\n'
        '                mp.nstr(solution_mp[std_index[(name, exponent)]], 80)\n'
        '                for exponent in std_exponents} for name in VARS}\n'
        '            hp_solver_audit[mode] = {\n'
        '                "dps":80, "method":"normal equations with mpmath LU",\n'
        '                "matrix_shape":list(matrix.shape), "rank":int(rank),\n'
        '                "condition_resolved":float(singular[0]/singular[max(rank-1,0)]),\n'
        '                "hp_max_linear_residual":mp.nstr(hp_max_residual,30),\n'
        '                "double_max_linear_residual":mp.nstr(double_max_residual,30),\n'
        '                "hp_max_normal_residual":mp.nstr(max(abs(value)\n'
        '                    for value in hp_normal_residual),30),\n'
        '                "hp_not_worse_than_double":bool(hp_max_residual <= double_max_residual),\n'
        '            }\n'
        '            deadline()\n'
        '        residual = matrix @ solution - rhs\n'
        '        scale = max(np.max(np.abs(matrix) * np.maximum(np.abs(solution)[None, :], 1e-300)),\n'
        '                    np.max(np.abs(rhs)), 1e-300)\n'
        '        standard = vector_to_standard(solution)',
    ),
    (
        "K7b3a_high_precision_registry_output",
        '      "K7b_coefficient_registry":coefficient_registry,"checks":checks,',
        '      "K7b_coefficient_registry":coefficient_registry,\n'
        '      "K7b3a_high_precision_standard_registry":hp_standard_registry,\n'
        '      "K7b3a_high_precision_solver_audit":hp_solver_audit,"checks":checks,',
    ),
    (
        "K7b3a_export_identity",
        '"test":"A2-K4 C7.7c-K7b registered coefficient export"',
        '"test":"A2-K4 C7.7c-K7b.3a high-precision standard coefficient export"',
    ),
'''

extended = source_text.replace(MARKER, addition + "'''\n\nextended = source_text", 1)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

