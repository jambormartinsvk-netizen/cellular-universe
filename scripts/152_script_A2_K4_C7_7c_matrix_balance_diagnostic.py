#!/usr/bin/env python
"""Zero-integration matrix-balance diagnostic for A2-K4 C7.7c.

Extends script 151 with a diagonal similarity balance of the local normalized
Jacobian.  This is a diagnostic only: no evolution is solved and no score is
awarded.  Permutations are disabled so state identity remains unchanged.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "151_script_A2_K4_C7_7c_initial_scaled_jacobian_profile.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\nextended = source_text.replace"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 151 balance-extension marker is not unique")

addition = r'''    (
        "matrix_balance_import",
        'from scipy.integrate import solve_ivp\n',
        'from scipy.integrate import solve_ivp\n'
        'from scipy.linalg import matrix_balance\n',
    ),
    (
        "matrix_balance_calculation",
        '            eigenvalues = np.linalg.eigvals(scaled_jacobian)\n'
        '            absolute_jacobian = np.abs(scaled_jacobian)',
        '            eigenvalues = np.linalg.eigvals(scaled_jacobian)\n'
        '            balanced_jacobian, balance_transform = matrix_balance(\n'
        '                scaled_jacobian, permute=False, scale=True, separate=False\n'
        '            )\n'
        '            balance_diagonal = np.diag(balance_transform)\n'
        '            balanced_integration_scale = (\n'
        '                integration_scale*balance_diagonal\n'
        '            )\n'
        '            balanced_singular_values = np.linalg.svd(\n'
        '                balanced_jacobian, compute_uv=False\n'
        '            )\n'
        '            balanced_eigenvalues = np.linalg.eigvals(balanced_jacobian)\n'
        '            sorted_original_eigenvalues = np.sort_complex(eigenvalues)\n'
        '            sorted_balanced_eigenvalues = np.sort_complex(balanced_eigenvalues)\n'
        '            eigenvalue_relative_difference = float(\n'
        '                np.max(np.abs(\n'
        '                    sorted_original_eigenvalues\n'
        '                    - sorted_balanced_eigenvalues\n'
        '                ))/max(1.0, float(np.max(np.abs(eigenvalues))))\n'
        '            )\n'
        '            absolute_jacobian = np.abs(scaled_jacobian)',
    ),
    (
        "matrix_balance_output",
        '                "scaled_jacobian_spectral_radius": float(\n'
        '                    np.max(np.abs(eigenvalues))\n'
        '                ),\n'
        '                "scaled_jacobian_singular_max": float(singular_values[0]),',
        '                "scaled_jacobian_spectral_radius": float(\n'
        '                    np.max(np.abs(eigenvalues))\n'
        '                ),\n'
        '                "balanced_jacobian_max_abs": float(\n'
        '                    np.max(np.abs(balanced_jacobian))\n'
        '                ),\n'
        '                "balanced_jacobian_spectral_radius": float(\n'
        '                    np.max(np.abs(balanced_eigenvalues))\n'
        '                ),\n'
        '                "balanced_jacobian_singular_max": float(\n'
        '                    balanced_singular_values[0]\n'
        '                ),\n'
        '                "balance_eigenvalue_relative_difference": (\n'
        '                    eigenvalue_relative_difference\n'
        '                ),\n'
        '                "balance_diagonal_min": float(np.min(balance_diagonal)),\n'
        '                "balance_diagonal_max": float(np.max(balance_diagonal)),\n'
        '                "balanced_physical_scale_span_max_over_min": float(\n'
        '                    np.max(balanced_integration_scale)\n'
        '                    /np.min(balanced_integration_scale)\n'
        '                ),\n'
        '                "balance_diagonal": {\n'
        '                    name: float(value)\n'
        '                    for name, value in zip(STATE_NAMES, balance_diagonal)\n'
        '                },\n'
        '                "scaled_jacobian_singular_max": float(singular_values[0]),',
    ),
    (
        "matrix_balance_test_identity",
        '"test": "A2-K4 C7.7c zero-integration scaled-Jacobian profile"',
        '"test": "A2-K4 C7.7c zero-integration matrix-balance diagnostic"',
    ),
    (
        "matrix_balance_execution_verdict",
        '"CAPTURED_C7_7C_INITIAL_SCALED_JACOBIAN"',
        '"CAPTURED_C7_7C_MATRIX_BALANCE_DIAGNOSTIC"',
    ),
'''

extended = source_text.replace(
    MARKER, addition + "'''\n\nextended = source_text.replace", 1
)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
