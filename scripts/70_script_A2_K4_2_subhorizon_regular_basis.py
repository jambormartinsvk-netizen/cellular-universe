#!/usr/bin/env python3
"""A2-K4.2: time-limited subhorizon audit of the complete regular K4 basis.

One process evaluates one declared configuration.  This keeps every numerical
run independently bounded and makes TIMEOUT an explicit unclosed result rather
than a physical failure.  Equations, initial modes and the observable norm are
imported from the audited K4.1 implementation (script 66).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
from typing import Any

import numpy as np
from scipy.integrate import solve_ivp


HERE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K41 = load("a2_k4_2_base66", "66_script_A2_K4_1_complete_regular_mode_basis.py")


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.monotonic()
    deadline = started + args.max_runtime_seconds

    def check_time(stage: str) -> None:
        if time.monotonic() > deadline:
            raise TimeoutError(
                f"internal limit {args.max_runtime_seconds:g} s exceeded at {stage}"
            )

    print("CHECKPOINT background_start", flush=True)
    background = K41.Background(args.lam, min(args.x_start, -22.0), args.background_step)
    check_time("background_complete")
    print("CHECKPOINT background_complete", flush=True)

    state0 = background.state(args.x_start)
    y0 = K41.initial_regular_basis(args.x_start, state0, background, args.q)
    obs0 = K41.observable_matrix(args.x_start, y0, state0, background)
    orthonormalizer = K41.inverse_sqrt_gram(obs0)
    initial_mode_norms = np.linalg.norm(obs0, axis=0)

    _, _, _, _, e0 = K41.B.component_background(
        args.x_start, state0, background.xb0
    )
    q_over_ae_start = args.q / (math.exp(args.x_start) * e0)

    def rhs_flat(x: float, flat: np.ndarray) -> np.ndarray:
        check_time("perturbation_rhs")
        state = background.state(x)
        matrix = flat.reshape(9, 3)
        derivative = np.empty_like(matrix)
        for column in range(3):
            derivative[:, column] = K41.B.rhs(
                x,
                matrix[:, column],
                state,
                background.xb0,
                background.p,
                args.q,
            )
        return derivative.reshape(-1)

    times = np.linspace(args.x_start, 0.0, args.samples)
    print("CHECKPOINT perturbation_start", flush=True)
    solution = solve_ivp(
        rhs_flat,
        (args.x_start, 0.0),
        y0.reshape(-1),
        method="DOP853",
        t_eval=times,
        rtol=args.rtol,
        atol=args.atol,
    )
    check_time("perturbation_complete")
    if not solution.success:
        raise RuntimeError(solution.message)
    print("CHECKPOINT perturbation_complete", flush=True)

    max_mode_norms = np.zeros(3, dtype=float)
    max_relative_fc = np.zeros(3, dtype=float)
    max_singular = 0.0
    residuals: list[float] = []
    term_norms: list[float] = []
    initial_constraint_relative: list[float] = []
    final_obs: np.ndarray | None = None

    for index, x in enumerate(solution.t):
        if index % 32 == 0:
            check_time("constraint_postprocess")
        state = background.state(float(x))
        matrix = solution.y[:, index].reshape(9, 3)
        obs = K41.observable_matrix(float(x), matrix, state, background)
        normalized_mode_norms = np.linalg.norm(obs, axis=0) / initial_mode_norms
        max_mode_norms = np.maximum(max_mode_norms, normalized_mode_norms)
        max_relative_fc = np.maximum(
            max_relative_fc, np.abs(obs[9]) / initial_mode_norms
        )
        singular = float(np.linalg.svd(obs @ orthonormalizer, compute_uv=False)[0])
        max_singular = max(max_singular, singular)

        for column in range(3):
            dy = K41.B.rhs(
                float(x),
                matrix[:, column],
                state,
                background.xb0,
                background.p,
                args.q,
            )
            terms = K41.K4.raw_constraint_terms(
                float(x), matrix[:, column], dy, state, background.xb0, args.q
            )
            residual = abs(float(np.sum(terms)))
            norm = float(np.sum(np.abs(terms)))
            residuals.append(residual)
            term_norms.append(norm)
            if index == 0:
                initial_constraint_relative.append(residual / max(norm, 1e-300))
        final_obs = obs

    if final_obs is None:
        raise RuntimeError("No perturbation samples were produced")

    max_term_norm = max(term_norms, default=0.0)
    active_floor = 1e-12 * max_term_norm
    active_relative = [
        residual / norm
        for residual, norm in zip(residuals, term_norms)
        if norm > active_floor and norm > 0.0
    ]
    final_mode_norms = np.linalg.norm(final_obs, axis=0) / initial_mode_norms
    final_normalized = final_obs / initial_mode_norms[np.newaxis, :]
    final_singular = float(
        np.linalg.svd(final_obs @ orthonormalizer, compute_uv=False)[0]
    )

    mode_summaries: dict[str, Any] = {}
    for index, name in enumerate(K41.MODE_NAMES):
        mode_summaries[name] = {
            "initial_audit_norm": float(initial_mode_norms[index]),
            "max_absolute_norm_transfer": float(max_mode_norms[index]),
            "final_absolute_norm_transfer": float(final_mode_norms[index]),
            "max_abs_Uf_minus_Uc_over_initial_norm": float(max_relative_fc[index]),
            "final_Phi_over_initial_norm": float(final_normalized[0, index]),
            "final_dc_over_initial_norm": float(final_normalized[1, index]),
            "final_df_over_delta_initial_norm": float(final_normalized[2, index]),
            "final_db_over_initial_norm": float(final_normalized[3, index]),
            "final_dr_over_initial_norm": float(final_normalized[4, index]),
        }

    max_abs_residual = max(residuals, default=0.0)
    output = {
        "test": "A2-K4.2 complete regular-basis subhorizon integration",
        "configuration": {
            "lambda": float(args.lam),
            "q_over_H0": float(args.q),
            "x_start": float(args.x_start),
            "background_step": float(args.background_step),
            "rtol": float(args.rtol),
            "atol": float(args.atol),
            "samples": int(args.samples),
            "internal_runtime_limit_seconds": float(args.max_runtime_seconds),
        },
        "q_over_aE_at_start": float(q_over_ae_start),
        "solver_success": bool(solution.success),
        "nfev": int(solution.nfev),
        "all_finite": bool(np.all(np.isfinite(solution.y))),
        "initial_constraint_relative": initial_constraint_relative,
        "constraint": {
            "max_absolute_residual": float(max_abs_residual),
            "max_term_norm": float(max_term_norm),
            "active_floor": float(active_floor),
            "active_point_count": len(active_relative),
            "max_active_pointwise_relative_residual": float(
                max(active_relative, default=0.0)
            ),
        },
        "max_regular_subspace_absolute_singular_transfer": float(max_singular),
        "final_regular_subspace_absolute_singular_transfer": float(final_singular),
        "linear_amplitude_estimate_for_1e-5_seed": float(1e-5 * max_singular),
        "mode_summaries": mode_summaries,
        "final_semantic_observable_matrix": final_normalized.tolist(),
        "runtime_seconds": time.monotonic() - started,
        "verdict": "NUMERICAL_RESULT_REQUIRES_CROSS_RUN_GATES",
    }
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=float, default=300.0)
    parser.add_argument("--lambda", dest="lam", type=float, default=0.15)
    parser.add_argument("--x-start", type=float, default=-20.0)
    parser.add_argument("--background-step", type=float, default=1.25e-4)
    parser.add_argument("--rtol", type=float, default=1e-9)
    parser.add_argument("--atol", type=float, default=1e-12)
    parser.add_argument("--samples", type=int, default=1601)
    parser.add_argument("--max-runtime-seconds", type=float, default=50.0)
    args = parser.parse_args()
    try:
        result = run(args)
    except TimeoutError as exc:
        print(
            json.dumps(
                {
                    "test": "A2-K4.2 complete regular-basis subhorizon integration",
                    "configuration": vars(args),
                    "verdict": "TIMEOUT_UNCLOSED_NOT_PHYSICS_FAIL",
                    "reason": str(exc),
                },
                indent=2,
                ensure_ascii=False,
            )
        )
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
