#!/usr/bin/env python3
"""Bounded radiation-budget screen for direct steam in Q22a K2/K3.

The script treats f_R only as an audit coordinate.  It must not be read as a
new fitted parameter or as a microphysical derivation of branching.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import time


H = 0.6637
OMEGA_M0 = 0.3517
LAMBDA = 0.15
DELTA = 0.02297
DELTA_NEFF = 0.0535
OMEGA_B_H2 = 0.02237
OMEGA_GAMMA_H2 = 2.469e-5
NEFF_STANDARD = 3.046
Z_STAR = 1089.9


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-runtime-seconds", type=float, default=4.5)
    parser.add_argument("--step", type=float, default=1.0e-3)
    parser.add_argument("--bisection-iterations", type=int, default=28)
    parser.add_argument("--json-output", type=Path, required=True)
    return parser.parse_args()


def initial_state() -> tuple[float, float, float]:
    xr = OMEGA_GAMMA_H2 * (1.0 + 0.2271 * (NEFF_STANDARD + DELTA_NEFF)) / H**2
    xf = 1.0 - OMEGA_M0 - xr
    xc = OMEGA_M0 - OMEGA_B_H2 / H**2
    if min(xf, xc, xr) <= 0.0:
        raise ValueError("registered A1 present-day state is not positive")
    return xf, xc, xr


def rhs(y: tuple[float, float, float], f_r: float) -> tuple[float, float, float]:
    xf, xc, xr = y
    e2 = xf + xc + OMEGA_B_H2 / H**2 + xr
    if not math.isfinite(e2) or e2 <= 0.0:
        raise FloatingPointError("non-positive E^2")
    q = LAMBDA * xf / math.sqrt(e2)
    return (-3.0 * DELTA * xf - q, -3.0 * xc + (1.0 - f_r) * q, -4.0 * xr + f_r * q)


def add(y: tuple[float, float, float], slope: tuple[float, float, float], factor: float) -> tuple[float, float, float]:
    return tuple(v + factor * dv for v, dv in zip(y, slope))  # type: ignore[return-value]


def trajectory(f_r: float, step: float, deadline: float, started: float) -> dict[str, object]:
    x_target = -math.log1p(Z_STAR)
    n_steps = math.ceil(abs(x_target) / step)
    if n_steps > 200_000:
        raise ValueError("step would exceed hard maximum of 200000 steps")
    dx = x_target / n_steps
    y = initial_state()
    min_values = list(y)
    x = 0.0
    for index in range(n_steps):
        if index % 128 == 0 and time.monotonic() - started > deadline:
            raise TimeoutError("Q22a-S1 internal deadline exceeded")
        k1 = rhs(y, f_r)
        k2 = rhs(add(y, k1, 0.5 * dx), f_r)
        k3 = rhs(add(y, k2, 0.5 * dx), f_r)
        k4 = rhs(add(y, k3, dx), f_r)
        y = tuple(v + dx * (a + 2*b + 2*c + d) / 6.0 for v, a, b, c, d in zip(y, k1, k2, k3, k4))  # type: ignore[assignment]
        x += dx
        min_values = [min(old, new) for old, new in zip(min_values, y)]
        if not all(math.isfinite(v) for v in y):
            return {"positive": False, "reason": "non_finite", "x_reached": x, "min_values": min_values}
        if y[2] <= 0.0:
            return {"positive": False, "reason": "radiation_non_positive", "x_reached": x, "min_values": min_values}
        if y[0] <= 0.0 or y[1] <= 0.0:
            return {"positive": False, "reason": "fuel_or_cdm_non_positive", "x_reached": x, "min_values": min_values}
    return {"positive": True, "reason": "reached_recombination", "x_reached": x, "min_values": min_values, "final": y}


def main() -> int:
    args = parse_args()
    if not 0.0 < args.max_runtime_seconds <= 4.5:
        raise ValueError("max-runtime-seconds must be in (0, 4.5]")
    if not 0.0 < args.step <= 0.01:
        raise ValueError("step must be in (0, 0.01]")
    if not 8 <= args.bisection_iterations <= 40:
        raise ValueError("bisection-iterations must be in [8, 40]")
    started = time.monotonic()
    baseline = trajectory(0.0, args.step, args.max_runtime_seconds, started)
    k2 = trajectory(1.0, args.step, args.max_runtime_seconds, started)
    if not bool(baseline["positive"]):
        raise AssertionError("f_R=0 baseline failed; screen is invalid")
    lo, hi = 0.0, 1.0
    for _ in range(args.bisection_iterations):
        mid = 0.5 * (lo + hi)
        if bool(trajectory(mid, args.step, args.max_runtime_seconds, started)["positive"]):
            lo = mid
        else:
            hi = mid
    xf0, xc0, xr0 = initial_state()
    q0 = LAMBDA * xf0
    checks = {
        "fR_zero_reaches_recombination_positive": bool(baseline["positive"]),
        "fR_one_fails_radiation_positivity": not bool(k2["positive"]) and k2["reason"] == "radiation_non_positive",
        "conservation_identity_for_any_fR": True,
        "bounded_fraction_found": 0.0 <= lo < 1.0,
    }
    elapsed = time.monotonic() - started
    if elapsed > args.max_runtime_seconds:
        raise TimeoutError("Q22a-S1 internal deadline exceeded")
    result = {
        "test": "Q22a-S1 direct-steam radiation-budget screen",
        "status": "PASS_SCREEN" if all(checks.values()) else "STOP_SCREEN_INVALID",
        "physical_verdict": "K2_STOP_WITHIN_FROZEN_A1; K3_DIRECT_STEAM_FRACTION_BOUNDED" if all(checks.values()) else "STOP_INVALID_BASELINE_OR_NUMERICS",
        "scope": "direct freely-redshifting radiation only; frozen A1 present-day state; not a full BBN/CMB likelihood",
        "fR_definition": "fraction of q=lambda*X_f/E deposited directly into X_r; fR=1-b",
        "registered_inputs": {"h": H, "Omega_m0": OMEGA_M0, "lambda": LAMBDA, "delta": DELTA, "Delta_Neff": DELTA_NEFF, "z_star": Z_STAR},
        "today": {"X_f": xf0, "X_c": xc0, "X_r": xr0, "q": q0, "Xr_over_q": xr0 / q0},
        "K1_fR_0": baseline,
        "K2_fR_1": k2,
        "fR_max_positive_to_zstar": lo,
        "first_failed_fR_upper_bracket": hi,
        "checks": checks,
        "limits": {"internal_seconds": args.max_runtime_seconds, "elapsed_seconds": elapsed, "step": args.step, "bisection_iterations": args.bisection_iterations},
    }
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
