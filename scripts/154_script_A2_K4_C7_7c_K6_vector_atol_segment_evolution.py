#!/usr/bin/env python
"""Preregistered C7.7c-K6 physical-state vector-atol segment evolution.

Immutable extension of script 139.  The physical state and RHS are unchanged;
the only numerical change is a fixed 13-component absolute-tolerance vector
derived from the preregistered analytic envelope.  No score is awarded here.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "139_script_A2_K4_3b_RG_BR3C_c_checkpoint_component_export.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "]\nfor label, old, new in replacements:\n"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 139 K6-extension marker is not unique")

addition = r'''    (
        "K6_reference_source",
        '"132_script_A2_K4_3b_RG_BR3C_a_registered_zero_projection.py"',
        '"146_script_A2_K4_3b_RG_C7_7c_K4_analytic_reference_state.py"',
    ),
    (
        "K6_reference_source_verdict",
        '== "PASS_BR3C_A_REGISTERED_ZERO_STATE"',
        '== "PASS_C7_7C_K4_ANALYTIC_REFERENCE_STATE"',
    ),
    (
        "K6_profile_cli",
        '    parser.add_argument("--safety-cap", type=float, default=1e12)\n',
        '    parser.add_argument("--safety-cap", type=float, default=1e12)\n'
        '    parser.add_argument("--profile-mode", choices=("NID", "NIV"), required=True)\n'
        '    parser.add_argument("--profile-surface", choices=("deep", "shallow"), required=True)\n'
        '    parser.add_argument("--profile-segments", type=int, default=1)\n',
    ),
    (
        "K6_profile_validation",
        '    args = parser.parse_args()\n'
        '    if not 0.0 < args.max_runtime_seconds <= 50.0:',
        '    args = parser.parse_args()\n'
        '    if not 1 <= args.profile_segments <= 7:\n'
        '        parser.error("profile segments must be in [1,7]")\n'
        '    if not 0.0 < args.max_runtime_seconds <= 50.0:',
    ),
    (
        "K6_single_mode",
        '    for mode in ("NID", "NIV"):',
        '    for mode in (args.profile_mode,):',
    ),
    (
        "K6_single_surface",
        '        for surface in ("deep", "shallow"):',
        '        for surface in (args.profile_surface,):',
    ),
    (
        "K6_fixed_vector_atol_and_target",
        '            x_current = float(source_surface["x"])\n'
        '            component_maxima = np.abs(y).copy()',
        '            x_current = float(source_surface["x"])\n'
        '            reference_state = source_payload["BR3C_state_surfaces"][mode]["surfaces"]["reference"]["state"]\n'
        '            reference_vector = np.asarray([reference_state[name] for name in STATE_NAMES], dtype=float)\n'
        '            analytic_envelope = np.maximum(\n'
        '                np.maximum(np.abs(y), np.abs(reference_vector)), 1e-300\n'
        '            )\n'
        '            component_atol = args.atol*analytic_envelope\n'
        '            profile_target = min(\n'
        '                x_current + args.profile_segments*args.segment_efolds,\n'
        '                args.x_final,\n'
        '            )\n'
        '            component_maxima = np.abs(y).copy()',
    ),
    (
        "K6_vector_atol",
        '                        atol=args.atol,',
        '                        atol=component_atol,',
    ),
    (
        "K6_profile_while_target",
        '            while x_current < args.x_final - 1e-13:',
        '            while x_current < profile_target - 1e-13:',
    ),
    (
        "K6_profile_segment_target",
        '                x_next = min(x_current + args.segment_efolds, args.x_final)',
        '                x_next = min(x_current + args.segment_efolds, profile_target)',
    ),
    (
        "K6_segment_timer_start",
        '                try:\n'
        '                    solution = solve_ivp(',
        '                segment_started = time.monotonic()\n'
        '                try:\n'
        '                    solution = solve_ivp(',
    ),
    (
        "K6_solver_metrics",
        '                total_nfev += int(solution.nfev)\n'
        '                if solution.y.size:',
        '                total_nfev += int(solution.nfev)\n'
        '                segment_wall_seconds = time.monotonic() - segment_started\n'
        '                accepted_steps = max(int(len(solution.t)) - 1, 0)\n'
        '                step_sizes = np.diff(solution.t)\n'
        '                if solution.y.size:',
    ),
    (
        "K6_checkpoint_metrics",
        '                        "nfev_segment": int(solution.nfev),\n'
        '                        "state_max_abs": float(np.max(np.abs(y))),',
        '                        "nfev_segment": int(solution.nfev),\n'
        '                        "segment_wall_seconds": float(segment_wall_seconds),\n'
        '                        "solver_points": int(len(solution.t)),\n'
        '                        "accepted_steps": int(accepted_steps),\n'
        '                        "nfev_per_accepted_step": float(\n'
        '                            solution.nfev/max(accepted_steps, 1)\n'
        '                        ),\n'
        '                        "accepted_step_min": (\n'
        '                            float(np.min(step_sizes)) if step_sizes.size else None\n'
        '                        ),\n'
        '                        "accepted_step_median": (\n'
        '                            float(np.median(step_sizes)) if step_sizes.size else None\n'
        '                        ),\n'
        '                        "accepted_step_max": (\n'
        '                            float(np.max(step_sizes)) if step_sizes.size else None\n'
        '                        ),\n'
        '                        "envelope_normalized_state_max_abs": float(\n'
        '                            np.max(np.abs(y)/analytic_envelope)\n'
        '                        ),\n'
        '                        "state_max_abs": float(np.max(np.abs(y))),',
    ),
    (
        "K6_expected_segments",
        '                math.ceil((args.x_final - float(source_surface["x"]))\n'
        '                          / args.segment_efolds - 1e-14)',
        '                math.ceil((profile_target - float(source_surface["x"]))\n'
        '                          / args.segment_efolds - 1e-14)',
    ),
    (
        "K6_reached_target",
        '            reached_final = abs(x_current - args.x_final) < 2e-12',
        '            reached_final = abs(x_current - profile_target) < 2e-12',
    ),
    (
        "K6_single_trajectory_check",
        '    checks["all_four_trajectories_present"] = sum(\n'
        '        len(mode_results) for mode_results in results.values()\n'
        '    ) == 4',
        '    checks["single_requested_trajectory_present"] = sum(\n'
        '        len(mode_results) for mode_results in results.values()\n'
        '    ) == 1',
    ),
    (
        "K6_tolerance_export",
        '                "component_max_abs": {\n',
        '                "analytic_envelope": {\n'
        '                    name:float(value)\n'
        '                    for name, value in zip(STATE_NAMES, analytic_envelope)\n'
        '                },\n'
        '                "component_atol": {\n'
        '                    name:float(value)\n'
        '                    for name, value in zip(STATE_NAMES, component_atol)\n'
        '                },\n'
        '                "component_max_abs": {\n',
    ),
    (
        "K6_profile_request_output",
        '        "results": results,\n',
        '        "profile_request": {\n'
        '            "mode": args.profile_mode,\n'
        '            "surface": args.profile_surface,\n'
        '            "segments": args.profile_segments,\n'
        '            "target_x": profile_target,\n'
        '            "score_effect": "NONE",\n'
        '        },\n'
        '        "results": results,\n',
    ),
    (
        "K6_solver_output",
        '            "atol": args.atol,\n',
        '            "atol_factor": args.atol,\n'
        '            "atol_interpretation": "component_atol_i=atol_factor*S_env_i",\n',
    ),
    (
        "K6_test_identity",
        '"test": "A2-K4.3b-RG C7.7c checkpoint component export"',
        '"test": "A2-K4 C7.7c-K6 physical-state vector-atol segment evolution"',
    ),
    (
        "K6_execution_verdict",
        '"PASS_C7_7C_CHECKPOINT_COMPONENT_EXPORT"',
        '"PASS_C7_7C_K6_VECTOR_ATOL_SEGMENT"',
    ),
    (
        "K6_physical_verdict",
        '"C7.7b reproduced; C7.7c activity still requires independent audit"',
        '"K6 vector-atol segment gate only; no physical verdict and no score change"',
    ),
'''

extended = source_text.replace(
    MARKER, addition + "]\nfor label, old, new in replacements:\n", 1
)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
