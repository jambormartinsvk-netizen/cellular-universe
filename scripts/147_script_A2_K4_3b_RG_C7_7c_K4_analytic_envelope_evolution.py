#!/usr/bin/env python
"""C7.7c-K4 evolution with preregistered analytic-envelope scaling."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "142_script_A2_K4_3b_RG_C7_7c_K2_normalized_component_evolution.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\ntext = text.replace"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 142 analytic-envelope extension marker is not unique")

addition = r'''    (
        "analytic_reference_source",
        '"132_script_A2_K4_3b_RG_BR3C_a_registered_zero_projection.py"',
        '"146_script_A2_K4_3b_RG_C7_7c_K4_analytic_reference_state.py"',
    ),
    (
        "analytic_reference_source_verdict",
        '== "PASS_BR3C_A_REGISTERED_ZERO_STATE"',
        '== "PASS_C7_7C_K4_ANALYTIC_REFERENCE_STATE"',
    ),
    (
        "analytic_envelope_scale",
        '            integration_scale = np.maximum(np.abs(y), 1e-300)\n'
        '            w = y/integration_scale',
        '            reference_state = source_payload["BR3C_state_surfaces"][mode]["surfaces"]["reference"]["state"]\n'
        '            reference_vector = np.asarray([reference_state[name] for name in STATE_NAMES], dtype=float)\n'
        '            integration_scale = np.maximum(np.maximum(np.abs(y), np.abs(reference_vector)), 1e-300)\n'
        '            w = y/integration_scale',
    ),
    (
        "analytic_envelope_scaling_output",
        '"state_scaling":"w_i=y_i/max(abs(y_i_start),1e-300)"',
        '"state_scaling":"w_i=y_i/max(abs(y_i_start),abs(y_i_series(x_ref=-18)),1e-300)"',
    ),
    (
        "analytic_envelope_identity",
        '"test": "A2-K4.3b-RG C7.7c-K2 normalized checkpoint component export"',
        '"test": "A2-K4.3b-RG C7.7c-K4 analytic-envelope checkpoint export"',
    ),
    (
        "analytic_envelope_execution",
        '"PASS_C7_7C_K2_NORMALIZED_COMPONENT_EXPORT"',
        '"PASS_C7_7C_K4_ANALYTIC_ENVELOPE_EXPORT"',
    ),
    (
        "analytic_envelope_physical",
        '"C7.7b reproduced in normalized variables; C7.7c still requires independent audit"',
        '"C7.7b reproduced with analytic-envelope scaling; C7.7c still requires independent audit"',
    ),
'''

extended = source_text.replace(MARKER, addition + "'''\n\ntext = text.replace", 1)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

