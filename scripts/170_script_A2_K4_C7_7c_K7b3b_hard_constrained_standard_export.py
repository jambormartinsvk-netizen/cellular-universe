#!/usr/bin/env python
"""Immutable hard-constrained high-precision standard Puiseux export.

Initial and registered hierarchy-regularity conditions are eliminated as
fixed variables. Only the remaining coefficients enter the 80-digit least-
squares solve. No magnitude cutoff and no ODE are used.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "165_script_A2_K4_C7_7c_K7b_registered_coefficient_export.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\nextended = source_text"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 165 K7b.3b extension marker is not unique")

addition = r'''    (
        "K7b3b_mpmath_import",
        'import numpy as np\n',
        'import numpy as np\nimport mpmath as mp\n',
    ),
    (
        "K7b3b_mode_parser",
        '    parser.add_argument("--x-reference", type=float, default=-18.0)',
        '    parser.add_argument("--x-reference", type=float, default=-18.0)\n'
        '    parser.add_argument("--hp-mode", choices=("NID","NIV"), default="NID")',
    ),
    (
        "K7b3b_registry_initialization",
        '    checks = {}; results = {}; state_surfaces = {}; coefficient_registry = {}',
        '    checks = {}; results = {}; state_surfaces = {}; coefficient_registry = {}\n'
        '    hp_standard_registry = {}; hp_solver_audit = {}',
    ),
    (
        "K7b3b_hard_constrained_standard_solve",
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
        '            fixed_targets = {}\n'
        '            hard_conflicts = 0\n'
        '            for fixed_name,fixed_exponent,fixed_value in initial:\n'
        '                fixed_index = std_index[(fixed_name,fixed_exponent)]\n'
        '                fixed_mp = mp.mpf(repr(float(fixed_value)))\n'
        '                if fixed_index in fixed_targets and abs(fixed_targets[fixed_index]-fixed_mp) > mp.mpf("1e-60"):\n'
        '                    hard_conflicts += 1\n'
        '                fixed_targets[fixed_index] = fixed_mp\n'
        '            alpha_hp = mp.mpf("0.2271")*(mp.mpf("3.046")+mp.mpf("0.0535"))\n'
        '            if mode == "NID":\n'
        '                fixed_targets[std_index[("dg",0)]] = -alpha_hp\n'
        '                fixed_targets[std_index[("dn",0)]] = mp.mpf("1")\n'
        '                fixed_targets[std_index[("Ug",0)]] = -alpha_hp/4\n'
        '                fixed_targets[std_index[("Un",0)]] = mp.mpf("0.25")\n'
        '            else:\n'
        '                fixed_targets[std_index[("Ug",-1)]] = -3*alpha_hp/4\n'
        '                fixed_targets[std_index[("Un",-1)]] = mp.mpf("0.75")\n'
        '            fixed_indices = sorted(fixed_targets)\n'
        '            free_indices = [index for index in range(std_unknowns)\n'
        '                if index not in fixed_targets]\n'
        '            fixed_vector = mp.matrix([fixed_targets[index]\n'
        '                for index in fixed_indices])\n'
        '            fixed_matrix = matrix_mp[:,fixed_indices]\n'
        '            free_matrix = matrix_mp[:,free_indices]\n'
        '            reduced_rhs = rhs_mp-fixed_matrix*fixed_vector\n'
        '            normal_mp = free_matrix.T*free_matrix\n'
        '            normal_rhs_mp = free_matrix.T*reduced_rhs\n'
        '            free_solution = mp.lu_solve(normal_mp, normal_rhs_mp)\n'
        '            solution_mp = mp.matrix(std_unknowns,1)\n'
        '            for local,index in enumerate(fixed_indices):\n'
        '                solution_mp[index] = fixed_vector[local]\n'
        '            for local,index in enumerate(free_indices):\n'
        '                solution_mp[index] = free_solution[local]\n'
        '            hp_linear_residual = matrix_mp*solution_mp-rhs_mp\n'
        '            double_mp = mp.matrix([mp.mpf(repr(float(value)))\n'
        '                for value in double_solution])\n'
        '            double_linear_residual = matrix_mp*double_mp-rhs_mp\n'
        '            hp_max_residual = max(abs(value) for value in hp_linear_residual)\n'
        '            double_max_residual = max(abs(value) for value in double_linear_residual)\n'
        '            hp_normal_residual = normal_mp*free_solution-normal_rhs_mp\n'
        '            fixed_max_error = max(abs(solution_mp[index]-fixed_targets[index])\n'
        '                for index in fixed_indices)\n'
        '            reduced_rank = int(np.linalg.matrix_rank(matrix[:,free_indices]))\n'
        '            solution = np.asarray([float(value) for value in solution_mp])\n'
        '            hp_standard_registry[mode] = {name:{str(exponent):\n'
        '                mp.nstr(solution_mp[std_index[(name,exponent)]],80)\n'
        '                for exponent in std_exponents} for name in VARS}\n'
        '            hp_solver_audit[mode] = {\n'
        '                "dps":80, "method":"hard-constrained normal equations with mpmath LU",\n'
        '                "matrix_shape":list(matrix.shape), "original_rank":int(rank),\n'
        '                "fixed_count":len(fixed_indices), "free_count":len(free_indices),\n'
        '                "reduced_rank":reduced_rank, "hard_conflict_count":hard_conflicts,\n'
        '                "condition_resolved":float(singular[0]/singular[max(rank-1,0)]),\n'
        '                "hp_max_linear_residual":mp.nstr(hp_max_residual,30),\n'
        '                "double_max_linear_residual":mp.nstr(double_max_residual,30),\n'
        '                "hp_max_normal_residual":mp.nstr(max(abs(value)\n'
        '                    for value in hp_normal_residual),30),\n'
        '                "fixed_max_absolute_error":mp.nstr(fixed_max_error,30),\n'
        '                "hp_not_worse_than_double":bool(hp_max_residual <= double_max_residual),\n'
        '            }\n'
        '            deadline()\n'
        '        residual = matrix @ solution-rhs\n'
        '        scale = max(np.max(np.abs(matrix)*np.maximum(np.abs(solution)[None,:],1e-300)),\n'
        '                    np.max(np.abs(rhs)),1e-300)\n'
        '        standard = vector_to_standard(solution)',
    ),
    (
        "K7b3b_high_precision_registry_output",
        '      "K7b_coefficient_registry":coefficient_registry,"checks":checks,',
        '      "K7b_coefficient_registry":coefficient_registry,\n'
        '      "K7b3b_high_precision_standard_registry":hp_standard_registry,\n'
        '      "K7b3b_high_precision_solver_audit":hp_solver_audit,"checks":checks,',
    ),
    (
        "K7b3b_export_identity",
        '"test":"A2-K4 C7.7c-K7b registered coefficient export"',
        '"test":"A2-K4 C7.7c-K7b.3b hard-constrained standard export"',
    ),
'''

extended = source_text.replace(MARKER, addition + "'''\n\nextended = source_text",1)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__":"__main__", "__file__":str(Path(__file__))})

