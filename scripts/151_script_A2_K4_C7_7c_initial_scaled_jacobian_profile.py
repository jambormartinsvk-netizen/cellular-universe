#!/usr/bin/env python
"""Zero-integration local Jacobian profile for A2-K4 C7.7c.

The script is an immutable diagnostic extension of script 150.  It uses the
same equations and analytic-envelope scales, but sets the integration target
equal to the selected initial surface.  It evaluates a central finite-
difference Jacobian in normalized variables.  It changes no K4 score.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "150_script_A2_K4_C7_7c_segment_profiler.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\nextended = source_text.replace"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 150 Jacobian-extension marker is not unique")

addition = r'''    (
        "zero_integration_jacobian_profile",
        '            profile_target = min(\n'
        '                x_current + args.profile_segments*args.segment_efolds,\n'
        '                args.x_final,\n'
        '            )\n'
        '            component_maxima = np.abs(y).copy()',
        '            profile_target = x_current\n'
        '            component_maxima = np.abs(y).copy()\n'
        '            initial_w = np.asarray(w, dtype=float)\n'
        '            def normalized_rhs(w_value):\n'
        '                return rhs(x_current, w_value*integration_scale)/integration_scale\n'
        '            initial_normalized_rhs = normalized_rhs(initial_w)\n'
        '            fd_epsilon = 1e-7\n'
        '            scaled_jacobian = np.empty((len(STATE_NAMES), len(STATE_NAMES)))\n'
        '            for column in range(len(STATE_NAMES)):\n'
        '                offset = np.zeros(len(STATE_NAMES))\n'
        '                offset[column] = fd_epsilon\n'
        '                scaled_jacobian[:, column] = (\n'
        '                    normalized_rhs(initial_w + offset)\n'
        '                    - normalized_rhs(initial_w - offset)\n'
        '                )/(2.0*fd_epsilon)\n'
        '            singular_values = np.linalg.svd(\n'
        '                scaled_jacobian, compute_uv=False\n'
        '            )\n'
        '            eigenvalues = np.linalg.eigvals(scaled_jacobian)\n'
        '            absolute_jacobian = np.abs(scaled_jacobian)\n'
        '            flat_order = np.argsort(absolute_jacobian.ravel())[::-1]\n'
        '            top_scaled_couplings = []\n'
        '            for flat_index in flat_order[:10]:\n'
        '                row, column = np.unravel_index(\n'
        '                    int(flat_index), absolute_jacobian.shape\n'
        '                )\n'
        '                top_scaled_couplings.append({\n'
        '                    "equation": STATE_NAMES[row],\n'
        '                    "source_component": STATE_NAMES[column],\n'
        '                    "abs_scaled_jacobian": float(\n'
        '                        absolute_jacobian[row, column]\n'
        '                    ),\n'
        '                    "signed_scaled_jacobian": float(\n'
        '                        scaled_jacobian[row, column]\n'
        '                    ),\n'
        '                })\n'
        '            positive_singular = singular_values[\n'
        '                singular_values > max(singular_values[0]*1e-14, 1e-300)\n'
        '            ]\n'
        '            jacobian_diagnostic = {\n'
        '                "fd_epsilon_normalized": fd_epsilon,\n'
        '                "scale_span_max_over_min": float(\n'
        '                    np.max(integration_scale)/np.min(integration_scale)\n'
        '                ),\n'
        '                "initial_normalized_rhs_max_abs": float(\n'
        '                    np.max(np.abs(initial_normalized_rhs))\n'
        '                ),\n'
        '                "initial_normalized_rhs_dominant_component": (\n'
        '                    STATE_NAMES[int(np.argmax(np.abs(initial_normalized_rhs)))]\n'
        '                ),\n'
        '                "scaled_jacobian_max_abs": float(\n'
        '                    np.max(absolute_jacobian)\n'
        '                ),\n'
        '                "scaled_jacobian_spectral_radius": float(\n'
        '                    np.max(np.abs(eigenvalues))\n'
        '                ),\n'
        '                "scaled_jacobian_singular_max": float(singular_values[0]),\n'
        '                "scaled_jacobian_resolved_condition_proxy": (\n'
        '                    float(singular_values[0]/positive_singular[-1])\n'
        '                    if positive_singular.size else None\n'
        '                ),\n'
        '                "top_scaled_couplings": top_scaled_couplings,\n'
        '            }',
    ),
    (
        "jacobian_result_export",
        '                "x_start": float(source_surface["x"]),\n',
        '                "x_start": float(source_surface["x"]),\n'
        '                "zero_integration_jacobian_diagnostic": jacobian_diagnostic,\n',
    ),
    (
        "jacobian_profile_request_output",
        '            "score_effect": "NONE",\n'
        '        },',
        '            "score_effect": "NONE",\n'
        '            "diagnostic_only": True,\n'
        '        },',
    ),
    (
        "jacobian_test_identity",
        '"test": "A2-K4 C7.7c analytic-envelope single-trajectory segment profile"',
        '"test": "A2-K4 C7.7c zero-integration scaled-Jacobian profile"',
    ),
    (
        "jacobian_execution_verdict",
        '"CAPTURED_C7_7C_SEGMENT_PROFILE"',
        '"CAPTURED_C7_7C_INITIAL_SCALED_JACOBIAN"',
    ),
'''

extended = source_text.replace(
    MARKER, addition + "'''\n\nextended = source_text.replace", 1
)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
