#!/usr/bin/env python
"""Preregistered C7.7c-K5 balanced one-segment evolution.

Immutable extension of script 150.  The only numerical change is a fixed
diagonal similarity balance derived from the local initial Jacobian.  Physics,
initial states, DOP853, tolerances, closure, and segment definitions are kept.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "150_script_A2_K4_C7_7c_segment_profiler.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\nextended = source_text.replace"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 150 K5-extension marker is not unique")

addition = r'''    (
        "K5_matrix_balance_import",
        'from scipy.integrate import solve_ivp\n',
        'from scipy.integrate import solve_ivp\n'
        'from scipy.linalg import matrix_balance\n',
    ),
    (
        "K5_fixed_balanced_scale",
        '            w = y/integration_scale\n'
        '            profile_target = min(',
        '            prebalance_integration_scale = integration_scale.copy()\n'
        '            prebalance_w = y/prebalance_integration_scale\n'
        '            def prebalance_rhs(w_value):\n'
        '                return (\n'
        '                    rhs(x_current, w_value*prebalance_integration_scale)\n'
        '                    /prebalance_integration_scale\n'
        '                )\n'
        '            fd_epsilon = 1e-7\n'
        '            prebalance_jacobian = np.empty((\n'
        '                len(STATE_NAMES), len(STATE_NAMES)\n'
        '            ))\n'
        '            for column in range(len(STATE_NAMES)):\n'
        '                offset = np.zeros(len(STATE_NAMES))\n'
        '                offset[column] = fd_epsilon\n'
        '                prebalance_jacobian[:, column] = (\n'
        '                    prebalance_rhs(prebalance_w + offset)\n'
        '                    - prebalance_rhs(prebalance_w - offset)\n'
        '                )/(2.0*fd_epsilon)\n'
        '            balanced_jacobian, balance_transform = matrix_balance(\n'
        '                prebalance_jacobian,\n'
        '                permute=False,\n'
        '                scale=True,\n'
        '                separate=False,\n'
        '            )\n'
        '            balance_diagonal = np.diag(balance_transform)\n'
        '            integration_scale = (\n'
        '                prebalance_integration_scale*balance_diagonal\n'
        '            )\n'
        '            w = y/integration_scale\n'
        '            original_eigenvalues = np.sort_complex(\n'
        '                np.linalg.eigvals(prebalance_jacobian)\n'
        '            )\n'
        '            balanced_eigenvalues = np.sort_complex(\n'
        '                np.linalg.eigvals(balanced_jacobian)\n'
        '            )\n'
        '            balance_eigenvalue_relative_difference = float(\n'
        '                np.max(np.abs(\n'
        '                    original_eigenvalues-balanced_eigenvalues\n'
        '                ))/max(\n'
        '                    1.0, float(np.max(np.abs(original_eigenvalues)))\n'
        '                )\n'
        '            )\n'
        '            prebalance_jacobian_max_abs = float(\n'
        '                np.max(np.abs(prebalance_jacobian))\n'
        '            )\n'
        '            balanced_jacobian_max_abs = float(\n'
        '                np.max(np.abs(balanced_jacobian))\n'
        '            )\n'
        '            balance_reduction_factor = (\n'
        '                prebalance_jacobian_max_abs\n'
        '                /max(balanced_jacobian_max_abs, 1e-300)\n'
        '            )\n'
        '            checks[f"{mode}_{surface}_balance_spectrum_preserved"] = (\n'
        '                balance_eigenvalue_relative_difference < 1e-8\n'
        '            )\n'
        '            checks[f"{mode}_{surface}_balance_reduction_ge_1e6"] = (\n'
        '                balance_reduction_factor >= 1e6\n'
        '            )\n'
        '            profile_target = min(',
    ),
    (
        "K5_balance_result_export",
        '                "integration_scale": {name:float(value) for name, value in zip(STATE_NAMES, integration_scale)},\n',
        '                "balance_diagnostic": {\n'
        '                    "fd_epsilon_normalized": fd_epsilon,\n'
        '                    "prebalance_jacobian_max_abs": prebalance_jacobian_max_abs,\n'
        '                    "balanced_jacobian_max_abs": balanced_jacobian_max_abs,\n'
        '                    "reduction_factor": float(balance_reduction_factor),\n'
        '                    "eigenvalue_relative_difference": (\n'
        '                        balance_eigenvalue_relative_difference\n'
        '                    ),\n'
        '                    "balance_diagonal": {\n'
        '                        name:float(value)\n'
        '                        for name, value in zip(STATE_NAMES, balance_diagonal)\n'
        '                    },\n'
        '                },\n'
        '                "prebalance_integration_scale": {\n'
        '                    name:float(value)\n'
        '                    for name, value in zip(\n'
        '                        STATE_NAMES, prebalance_integration_scale\n'
        '                    )\n'
        '                },\n'
        '                "integration_scale": {name:float(value) for name, value in zip(STATE_NAMES, integration_scale)},\n',
    ),
    (
        "K5_scaling_output",
        '"state_scaling":"w_i=y_i/max(abs(y_i_start),abs(y_i_series(x_ref=-18)),1e-300)"',
        '"state_scaling":"z_i=y_i/[S_env,i*D_i], fixed diagonal Jacobian balance, no permutation"',
    ),
    (
        "K5_test_identity",
        '"test": "A2-K4 C7.7c analytic-envelope single-trajectory segment profile"',
        '"test": "A2-K4 C7.7c-K5 fixed balanced one-segment evolution"',
    ),
    (
        "K5_execution_verdict",
        '"CAPTURED_C7_7C_SEGMENT_PROFILE"',
        '"PASS_C7_7C_K5_BALANCED_SEGMENT"',
    ),
    (
        "K5_physical_verdict",
        '"diagnostic profile only; no physical verdict and no score change"',
        '"K5 balanced segment gate only; no physical verdict and no score change"',
    ),
'''

extended = source_text.replace(
    MARKER, addition + "'''\n\nextended = source_text.replace", 1
)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
