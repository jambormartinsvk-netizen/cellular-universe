#!/usr/bin/env python3
"""A2-K4.2 bounded q=300 solver/background/start-time convergence gates."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace

import numpy as np


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


K42 = load("a2_k4_2_base70", "70_script_A2_K4_2_subhorizon_regular_basis.py")


def matrix_difference(candidate: dict, reference: dict) -> float:
    a = np.asarray(candidate["final_semantic_observable_matrix"], dtype=float)
    b = np.asarray(reference["final_semantic_observable_matrix"], dtype=float)
    return float(np.linalg.norm(a - b) / max(np.linalg.norm(b), 1.0))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=50.0)
    args = parser.parse_args()
    started = time.monotonic()

    configurations = {
        "base": dict(x_start=-20.0, background_step=1.25e-4, rtol=1e-9, atol=1e-12),
        "tighter_solver": dict(
            x_start=-20.0, background_step=1.25e-4, rtol=3e-10, atol=3e-13
        ),
        "coarser_background": dict(
            x_start=-20.0, background_step=2.5e-4, rtol=1e-9, atol=1e-12
        ),
        "earlier_start": dict(
            x_start=-22.0, background_step=1.25e-4, rtol=1e-9, atol=1e-12
        ),
    }
    results = {}
    try:
        for name, config in configurations.items():
            remaining = args.max_runtime_seconds - (time.monotonic() - started)
            if remaining <= 2.0:
                raise TimeoutError("global convergence-audit runtime exhausted")
            run_args = SimpleNamespace(
                q=300.0,
                lam=0.15,
                samples=1601,
                max_runtime_seconds=min(15.0, remaining - 1.0),
                **config,
            )
            print(f"CHECKPOINT convergence_{name}_start", flush=True)
            results[name] = K42.run(run_args)
            print(f"CHECKPOINT convergence_{name}_complete", flush=True)
    except TimeoutError as exc:
        print(
            json.dumps(
                {
                    "test": "A2-K4.2 q=300 convergence gates",
                    "verdict": "TIMEOUT_UNCLOSED_NOT_PHYSICS_FAIL",
                    "completed_configurations": list(results),
                    "reason": str(exc),
                },
                indent=2,
            )
        )
        return 2

    base = results["base"]
    differences = {
        name: matrix_difference(results[name], base)
        for name in ("tighter_solver", "coarser_background", "earlier_start")
    }
    thresholds = {
        "tighter_solver": 1e-5,
        "coarser_background": 1e-4,
        "earlier_start": 1e-4,
    }
    checks = {
        name: bool(differences[name] < thresholds[name]) for name in differences
    }
    summaries = {
        name: {
            "runtime_seconds": result["runtime_seconds"],
            "nfev": result["nfev"],
            "max_singular_transfer": result[
                "max_regular_subspace_absolute_singular_transfer"
            ],
            "max_active_pointwise_relative_constraint": result["constraint"][
                "max_active_pointwise_relative_residual"
            ],
        }
        for name, result in results.items()
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K4.2 q=300 convergence gates",
        "relative_final_matrix_differences": differences,
        "thresholds": thresholds,
        "checks": checks,
        "run_summaries": summaries,
        "total_runtime_seconds": time.monotonic() - started,
        "verdict": "PASS_K4_2_CONVERGENCE" if passed else "FAIL_K4_2_CONVERGENCE",
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
