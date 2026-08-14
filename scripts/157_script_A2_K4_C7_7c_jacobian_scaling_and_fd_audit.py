#!/usr/bin/env python
"""Bounded zero-integration audit of Jacobian scaling and FD error.

This immutable extension of script 151 compares its envelope-coordinate
finite-difference Jacobian with a physical Jacobian built by direct action on
the 13 basis vectors.  It also audits local/envelope similarity transforms,
five FD steps, and RHS linearity.  It awards no score.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "151_script_A2_K4_C7_7c_initial_scaled_jacobian_profile.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\nextended = source_text.replace"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 151 audit-extension marker is not unique")

addition = r'''    (
        "basis_jacobian_and_fd_sweep",
        '            singular_values = np.linalg.svd(\n'
        '                scaled_jacobian, compute_uv=False\n'
        '            )',
        '            zero_state = np.zeros(len(STATE_NAMES))\n'
        '            physical_jacobian = np.empty_like(scaled_jacobian)\n'
        '            zero_rhs = rhs(x_current, zero_state)\n'
        '            for basis_column in range(len(STATE_NAMES)):\n'
        '                basis_state = np.zeros(len(STATE_NAMES))\n'
        '                basis_state[basis_column] = 1.0\n'
        '                physical_jacobian[:, basis_column] = (\n'
        '                    rhs(x_current, basis_state)-zero_rhs\n'
        '                )\n'
        '            envelope_exact = (\n'
        '                physical_jacobian*integration_scale[None, :]\n'
        '                /integration_scale[:, None]\n'
        '            )\n'
        '            local_scale = np.maximum(np.abs(y), 1e-300)\n'
        '            local_exact = (\n'
        '                physical_jacobian*local_scale[None, :]\n'
        '                /local_scale[:, None]\n'
        '            )\n'
        '            physical_eigenvalues = np.sort_complex(\n'
        '                np.linalg.eigvals(physical_jacobian)\n'
        '            )\n'
        '            envelope_eigenvalues = np.sort_complex(\n'
        '                np.linalg.eigvals(envelope_exact)\n'
        '            )\n'
        '            local_eigenvalues = np.sort_complex(\n'
        '                np.linalg.eigvals(local_exact)\n'
        '            )\n'
        '            fd_sweep = {}\n'
        '            for audited_step in (1e-4, 1e-5, 1e-6, 1e-7, 1e-8):\n'
        '                audited_fd = np.empty_like(scaled_jacobian)\n'
        '                for audited_column in range(len(STATE_NAMES)):\n'
        '                    offset = np.zeros(len(STATE_NAMES))\n'
        '                    offset[audited_column] = audited_step\n'
        '                    audited_fd[:, audited_column] = (\n'
        '                        normalized_rhs(initial_w + offset)\n'
        '                        - normalized_rhs(initial_w - offset)\n'
        '                    )/(2.0*audited_step)\n'
        '                difference = audited_fd-envelope_exact\n'
        '                audited_eigenvalues = np.sort_complex(\n'
        '                    np.linalg.eigvals(audited_fd)\n'
        '                )\n'
        '                fd_sweep[str(audited_step)] = {\n'
        '                    "max_abs_error": float(np.max(np.abs(difference))),\n'
        '                    "relative_frobenius_error": float(\n'
        '                        np.linalg.norm(difference)\n'
        '                        /max(np.linalg.norm(envelope_exact), 1e-300)\n'
        '                    ),\n'
        '                    "spectral_relative_error": float(\n'
        '                        np.max(np.abs(\n'
        '                            audited_eigenvalues-envelope_eigenvalues\n'
        '                        ))/max(\n'
        '                            1.0, float(np.max(np.abs(envelope_eigenvalues)))\n'
        '                        )\n'
        '                    ),\n'
        '                }\n'
        '            linear_left = rhs(\n'
        '                x_current, 0.37*y-0.23*reference_vector\n'
        '            )\n'
        '            linear_right = (\n'
        '                0.37*rhs(x_current, y)\n'
        '                -0.23*rhs(x_current, reference_vector)\n'
        '            )\n'
        '            linear_residual = linear_left-linear_right\n'
        '            scaling_fd_audit = {\n'
        '                "rhs_linearity_max_abs_residual": float(\n'
        '                    np.max(np.abs(linear_residual))\n'
        '                ),\n'
        '                "rhs_linearity_relative_residual": float(\n'
        '                    np.linalg.norm(linear_residual)\n'
        '                    /max(np.linalg.norm(linear_right), 1e-300)\n'
        '                ),\n'
        '                "physical_max_abs": float(np.max(np.abs(physical_jacobian))),\n'
        '                "local_max_abs": float(np.max(np.abs(local_exact))),\n'
        '                "envelope_max_abs": float(np.max(np.abs(envelope_exact))),\n'
        '                "physical_singular_max": float(\n'
        '                    np.linalg.svd(physical_jacobian, compute_uv=False)[0]\n'
        '                ),\n'
        '                "local_singular_max": float(\n'
        '                    np.linalg.svd(local_exact, compute_uv=False)[0]\n'
        '                ),\n'
        '                "envelope_singular_max": float(\n'
        '                    np.linalg.svd(envelope_exact, compute_uv=False)[0]\n'
        '                ),\n'
        '                "physical_spectral_radius": float(\n'
        '                    np.max(np.abs(physical_eigenvalues))\n'
        '                ),\n'
        '                "local_spectrum_relative_difference": float(\n'
        '                    np.max(np.abs(local_eigenvalues-physical_eigenvalues))\n'
        '                    /max(1.0, float(np.max(np.abs(physical_eigenvalues))))\n'
        '                ),\n'
        '                "envelope_spectrum_relative_difference": float(\n'
        '                    np.max(np.abs(envelope_eigenvalues-physical_eigenvalues))\n'
        '                    /max(1.0, float(np.max(np.abs(physical_eigenvalues))))\n'
        '                ),\n'
        '                "local_scale_span": float(\n'
        '                    np.max(local_scale)/np.min(local_scale)\n'
        '                ),\n'
        '                "envelope_scale_span": float(\n'
        '                    np.max(integration_scale)/np.min(integration_scale)\n'
        '                ),\n'
        '                "fd_sweep": fd_sweep,\n'
        '            }\n'
        '            singular_values = np.linalg.svd(\n'
        '                scaled_jacobian, compute_uv=False\n'
        '            )',
    ),
    (
        "scaling_fd_audit_output",
        '                "fd_epsilon_normalized": fd_epsilon,\n',
        '                "scaling_and_fd_audit": scaling_fd_audit,\n'
        '                "fd_epsilon_normalized": fd_epsilon,\n',
    ),
    (
        "scaling_fd_audit_identity",
        '"test": "A2-K4 C7.7c zero-integration scaled-Jacobian profile"',
        '"test": "A2-K4 C7.7c Jacobian scaling and FD audit"',
    ),
    (
        "scaling_fd_audit_verdict",
        '"CAPTURED_C7_7C_INITIAL_SCALED_JACOBIAN"',
        '"CAPTURED_C7_7C_JACOBIAN_SCALING_FD_AUDIT"',
    ),
'''

extended = source_text.replace(
    MARKER, addition + "'''\n\nextended = source_text.replace", 1
)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
