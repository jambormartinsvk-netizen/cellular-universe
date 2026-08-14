#!/usr/bin/env python
"""C7.7c-K2 immutable normalized-state extension of checkpoint export 139."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "139_script_A2_K4_3b_RG_BR3C_c_checkpoint_component_export.py"
)
text = SOURCE.read_text(encoding="utf-8")
MARKER = "]\nfor label, old, new in replacements:\n"
if text.count(MARKER) != 1:
    raise RuntimeError("script 139 normalized-extension marker is not unique")

addition = r'''    (
        "normalized_initial_state",
        '            x_current = float(source_surface["x"])\n'
        '            component_maxima = np.abs(y).copy()',
        '            x_current = float(source_surface["x"])\n'
        '            integration_scale = np.maximum(np.abs(y), 1e-300)\n'
        '            w = y/integration_scale\n'
        '            component_maxima = np.abs(y).copy()',
    ),
    (
        "normalized_solve",
        '                    solution = solve_ivp(\n'
        '                        rhs,\n'
        '                        (x_current, x_next),\n'
        '                        y,',
        '                    solution = solve_ivp(\n'
        '                        lambda x_scaled, w_scaled: rhs(x_scaled, w_scaled*integration_scale)/integration_scale,\n'
        '                        (x_current, x_next),\n'
        '                        w,',
    ),
    (
        "physical_component_maxima",
        '                        component_maxima, np.max(np.abs(solution.y), axis=1)\n',
        '                        component_maxima, np.max(np.abs(solution.y*integration_scale[:, None]), axis=1)\n',
    ),
    (
        "normalized_solution_update",
        '                y = np.asarray(solution.y[:, -1], dtype=float)\n'
        '                x_current = float(solution.t[-1])',
        '                w = np.asarray(solution.y[:, -1], dtype=float)\n'
        '                y = w*integration_scale\n'
        '                x_current = float(solution.t[-1])',
    ),
    (
        "integration_scale_output",
        '                "component_max_abs": {\n',
        '                "integration_scale": {name:float(value) for name, value in zip(STATE_NAMES, integration_scale)},\n'
        '                "component_max_abs": {\n',
    ),
    (
        "solver_scaling_output",
        '            "closure": "L5=0 bounded BR3C closure; full hierarchy pending",\n',
        '            "closure": "L5=0 bounded BR3C closure; full hierarchy pending",\n'
        '            "state_scaling":"w_i=y_i/max(abs(y_i_start),1e-300)",\n'
        '            "atol_interpretation":"normalized-state absolute tolerance",\n',
    ),
    (
        "normalized_test_identity",
        '"test": "A2-K4.3b-RG C7.7c checkpoint component export"',
        '"test": "A2-K4.3b-RG C7.7c-K2 normalized checkpoint component export"',
    ),
    (
        "normalized_execution_verdict",
        '"PASS_C7_7C_CHECKPOINT_COMPONENT_EXPORT"',
        '"PASS_C7_7C_K2_NORMALIZED_COMPONENT_EXPORT"',
    ),
    (
        "normalized_physical_verdict",
        '"C7.7b reproduced; C7.7c activity still requires independent audit"',
        '"C7.7b reproduced in normalized variables; C7.7c still requires independent audit"',
    ),
'''

text = text.replace(MARKER, addition + "]\nfor label, old, new in replacements:\n", 1)
code = compile(text, str(Path(__file__)), "exec")
exec(code, {"__name__":"__main__", "__file__":str(Path(__file__))})

