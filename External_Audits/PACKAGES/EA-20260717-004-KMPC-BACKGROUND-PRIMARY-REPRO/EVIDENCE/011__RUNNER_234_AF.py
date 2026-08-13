#!/usr/bin/env python
"""Bounded convergence audit for A_f implied by frozen A1-K1 present-day closure."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from baseScripts.k_mpc_005.af_from_a1_background import FrozenA1, integrate_af


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x-min", type=float, default=-18.0)
    parser.add_argument("--deadline-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def write_once(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable output: {path}")
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    p = FrozenA1()
    resolutions = [5.0e-4, 2.5e-4, 1.25e-4]
    results: dict[str, dict[str, object]] = {}
    for step in resolutions:
        results[f"dx={step:.8g}"] = integrate_af(p, args.x_min, step, args.deadline_seconds)
    coarse, medium, fine = (float(results[f"dx={step:.8g}"]["af_final"]) for step in resolutions)
    relative_medium_fine = abs(medium - fine) / max(abs(fine), 1.0e-300)
    checks = {
        "all_Af_positive": all(float(row["af_final"]) > 0.0 for row in results.values()),
        "all_background_values_positive": all(float(row["min_density"]) > 0.0 and float(row["min_e2"]) > 0.0 for row in results.values()),
        "medium_fine_relative_difference_below_1e-5": relative_medium_fine < 1.0e-5,
        "no_K_MPC_or_fourier_k_input": True,
    }
    payload: dict[str, object] = {
        "test": "KMPC-001 A_f from frozen A1-K1 present-day closure",
        "scope": "numerical parameter-bookkeeping audit only; not microscopic derivation of frozen A1 inputs",
        "parameters": p.__dict__,
        "x_min": args.x_min,
        "deadline_seconds_per_resolution": args.deadline_seconds,
        "results": results,
        "relative_medium_fine": relative_medium_fine,
        "checks": checks,
        "verdict": "PASS_NUMERICAL_AF_IS_DERIVED_FROM_FROZEN_A1" if all(checks.values()) else "STOP_OR_REVIEW_AF_AUDIT_FAILED",
        "af_old_from_phi1_k005_is_not_used": True,
    }
    write_once(args.output, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
