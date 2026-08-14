#!/usr/bin/env python
"""Bounded, single-trajectory profiler for A2-K4 C7.7c.

This is an immutable audit extension of script 147.  It changes no equation,
coefficient, tolerance, initial state, or analytic-envelope scale.  It only
selects one mode/surface, limits the requested segment prefix, and exports
per-segment cost diagnostics.  The run is diagnostic and awards no score.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "147_script_A2_K4_3b_RG_C7_7c_K4_analytic_envelope_evolution.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\nextended = source_text.replace"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 147 profile-extension marker is not unique")

addition = r'''    (
        "profile_cli",
        '    parser.add_argument("--safety-cap", type=float, default=1e12)\n',
        '    parser.add_argument("--safety-cap", type=float, default=1e12)\n'
        '    parser.add_argument("--profile-mode", choices=("NID", "NIV"), required=True)\n'
        '    parser.add_argument("--profile-surface", choices=("deep", "shallow"), required=True)\n'
        '    parser.add_argument("--profile-segments", type=int, default=1)\n',
    ),
    (
        "profile_segment_validation",
        '    args = parser.parse_args()\n'
        '    if not 0.0 < args.max_runtime_seconds <= 50.0:',
        '    args = parser.parse_args()\n'
        '    if not 1 <= args.profile_segments <= 7:\n'
        '        parser.error("profile segments must be in [1,7]")\n'
        '    if not 0.0 < args.max_runtime_seconds <= 50.0:',
    ),
    (
        "profile_single_mode",
        '    for mode in ("NID", "NIV"):',
        '    for mode in (args.profile_mode,):',
    ),
    (
        "profile_single_surface",
        '        for surface in ("deep", "shallow"):',
        '        for surface in (args.profile_surface,):',
    ),
    (
        "profile_target",
        '            w = y/integration_scale\n'
        '            component_maxima = np.abs(y).copy()',
        '            w = y/integration_scale\n'
        '            profile_target = min(\n'
        '                x_current + args.profile_segments*args.segment_efolds,\n'
        '                args.x_final,\n'
        '            )\n'
        '            component_maxima = np.abs(y).copy()',
    ),
    (
        "profile_while_target",
        '            while x_current < args.x_final - 1e-13:',
        '            while x_current < profile_target - 1e-13:',
    ),
    (
        "profile_segment_target",
        '                x_next = min(x_current + args.segment_efolds, args.x_final)',
        '                x_next = min(x_current + args.segment_efolds, profile_target)',
    ),
    (
        "profile_segment_timer_start",
        '                try:\n'
        '                    solution = solve_ivp(',
        '                segment_started = time.monotonic()\n'
        '                try:\n'
        '                    solution = solve_ivp(',
    ),
    (
        "profile_solver_metrics",
        '                total_nfev += int(solution.nfev)\n'
        '                if solution.y.size:',
        '                total_nfev += int(solution.nfev)\n'
        '                segment_wall_seconds = time.monotonic() - segment_started\n'
        '                accepted_steps = max(int(len(solution.t)) - 1, 0)\n'
        '                step_sizes = np.diff(solution.t)\n'
        '                normalized_component_peaks = (\n'
        '                    np.max(np.abs(solution.y), axis=1)\n'
        '                    if solution.y.size else np.full(len(STATE_NAMES), np.nan)\n'
        '                )\n'
        '                if solution.y.size:',
    ),
    (
        "profile_checkpoint_metrics",
        '                        "nfev_segment": int(solution.nfev),\n'
        '                        "state_max_abs": float(np.max(np.abs(y))),',
        '                        "nfev_segment": int(solution.nfev),\n'
        '                        "segment_wall_seconds": float(segment_wall_seconds),\n'
        '                        "solver_points": int(len(solution.t)),\n'
        '                        "accepted_steps": int(accepted_steps),\n'
        '                        "nfev_per_accepted_step": (\n'
        '                            float(solution.nfev/max(accepted_steps, 1))\n'
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
        '                        "normalized_state_max_abs": float(\n'
        '                            np.max(normalized_component_peaks)\n'
        '                        ),\n'
        '                        "normalized_dominant_component": STATE_NAMES[int(\n'
        '                            np.argmax(normalized_component_peaks)\n'
        '                        )],\n'
        '                        "state_max_abs": float(np.max(np.abs(y))),',
    ),
    (
        "profile_expected_segments",
        '                math.ceil((args.x_final - float(source_surface["x"]))\n'
        '                          / args.segment_efolds - 1e-14)',
        '                math.ceil((profile_target - float(source_surface["x"]))\n'
        '                          / args.segment_efolds - 1e-14)',
    ),
    (
        "profile_reached_target",
        '            reached_final = abs(x_current - args.x_final) < 2e-12',
        '            reached_final = abs(x_current - profile_target) < 2e-12',
    ),
    (
        "profile_single_trajectory_check",
        '    checks["all_four_trajectories_present"] = sum(\n'
        '        len(mode_results) for mode_results in results.values()\n'
        '    ) == 4',
        '    checks["single_requested_trajectory_present"] = sum(\n'
        '        len(mode_results) for mode_results in results.values()\n'
        '    ) == 1',
    ),
    (
        "profile_request_output",
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
        "profile_test_identity",
        '"test": "A2-K4.3b-RG C7.7c-K4 analytic-envelope checkpoint export"',
        '"test": "A2-K4 C7.7c analytic-envelope single-trajectory segment profile"',
    ),
    (
        "profile_execution_verdict",
        '"PASS_C7_7C_K4_ANALYTIC_ENVELOPE_EXPORT"',
        '"CAPTURED_C7_7C_SEGMENT_PROFILE"',
    ),
    (
        "profile_physical_verdict",
        '"C7.7b reproduced with analytic-envelope scaling; C7.7c still requires independent audit"',
        '"diagnostic profile only; no physical verdict and no score change"',
    ),
'''

extended = source_text.replace(
    MARKER, addition + "'''\n\nextended = source_text.replace", 1
)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
