#!/usr/bin/env python
"""Bounded P3 comparison: frozen A1 D(a) versus normalized truncated K7 D(a)."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from baseScripts.k_mpc_005.af_from_a1_background import FrozenA1, integrate_samples, omega_r0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--af-json", type=Path, required=True)
    parser.add_argument("--x-min", type=float, default=-18.0)
    parser.add_argument("--deadline-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def write_once(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable output: {path}")
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def d_k7(a: float, af: float, params: FrozenA1, rad: float, p: float) -> float:
    correction = 1.0 / (p + 1.0) - 0.5
    return 1.0 + params.omega_m0 / rad * a + af * a**p * (
        1.0 + correction * params.lam * a**2 / math.sqrt(rad)
    )


def main() -> int:
    args = parse_args()
    prior = json.loads(args.af_json.read_text(encoding="utf-8"))
    if prior.get("verdict") != "PASS_NUMERICAL_AF_IS_DERIVED_FROM_FROZEN_A1":
        raise ValueError("A_f source is not the registered P2a PASS")
    af = float(prior["results"]["dx=0.000125"]["af_final"])
    raw = prior["parameters"]
    params = FrozenA1(
        h=float(raw["h"]), omega_m0=float(raw["omega_m0"]), lam=float(raw["lam"]),
        delta=float(raw["delta"]), omega_b=float(raw["omega_b"]),
        delta_neff=float(raw["delta_neff"]), omega_gamma=float(raw["omega_gamma"]),
        neff_standard=float(raw["neff_standard"]),
    )
    checkpoints = (-18.0, -16.0, -14.0, -12.0, -10.0, -8.0, -6.0, -4.0, -2.0, 0.0)
    trajectory = integrate_samples(params, args.x_min, 0.000125, checkpoints[:-1], args.deadline_seconds)
    rad = omega_r0(params)
    p = 4.0 - 3.0 * params.delta
    first_nonpositive: dict[str, float] | None = None
    previous_a = math.exp(args.x_min)
    previous_d = d_k7(previous_a, af, params, rad, p)
    grid_count = 36000
    for index in range(1, grid_count + 1):
        x = args.x_min * (1.0 - index / grid_count)
        a = math.exp(x)
        current_d = d_k7(a, af, params, rad, p)
        if first_nonpositive is None and previous_d > 0.0 and current_d <= 0.0:
            fraction = previous_d / (previous_d - current_d)
            first_nonpositive = {"a_linear_crossing": previous_a + fraction * (a - previous_a), "x_interval_end": x}
        previous_a, previous_d = a, current_d
    points: list[dict[str, float]] = []
    for x in checkpoints:
        a = math.exp(x)
        d_a1 = 1.0 / rad if x == 0.0 else trajectory["samples"][f"x={x:.1f}"]["D_a1"]
        points.append({"x": x, "a": a, "D_A1": d_a1, "D_K7_trunc": d_k7(a, af, params, rad, p)})
    a1_pass = bool(trajectory["min_density"] > 0.0 and trajectory["min_e2"] > 0.0 and all(v["D_A1"] > 0.0 for v in points))
    k7_pass = first_nonpositive is None and all(v["D_K7_trunc"] > 0.0 for v in points)
    payload = {
        "test": "KMPC-002 P3 frozen A1 versus normalized truncated K7 background",
        "scope": "background bookkeeping only; no perturbation ODE, CLASS, or score",
        "af_source": str(args.af_json), "af": af, "p_exponent": p, "omega_r0": rad,
        "truncated_correction_coefficient": 1.0 / (p + 1.0) - 0.5,
        "checks": {"a1_positive": a1_pass, "k7_truncated_positive_to_a1": k7_pass, "no_new_fit": True},
        "first_k7_nonpositive": first_nonpositive, "checkpoints": points,
        "trajectory": trajectory,
        "verdict": "PASS_P3_FULL_BACKGROUND_POSITIVE" if a1_pass and k7_pass else "STOP_K7_TRUNCATED_SERIES_IS_NOT_FULL_BACKGROUND",
    }
    write_once(args.output, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
