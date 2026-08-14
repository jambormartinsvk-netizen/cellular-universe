#!/usr/bin/env python
"""Bounded four-surface aggregation of K7b.1 coefficient-floor scaling.

This script adds no retrospective pass threshold. It reproduces the four
registered profiles and reports deep/shallow scaling plus activity-relative
D/M derivative discrepancies. No ODE is integrated.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent


def parse_json(text: str) -> dict[str, object]:
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError("K7b.1 child returned no JSON")
    return json.loads(text[start:end + 1])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    parser.add_argument("--child-runtime-seconds", type=float, default=4.0)
    parser.add_argument("--source-runtime-seconds", type=float, default=2.0)
    args = parser.parse_args()
    if not 5.0 <= args.max_runtime_seconds <= 30.0:
        parser.error("max-runtime-seconds must be in [5,30]")
    if not 2.0 <= args.child_runtime_seconds <= 8.0:
        parser.error("child-runtime-seconds must be in [2,8]")
    if not 1.0 <= args.source_runtime_seconds <= 5.0:
        parser.error("source-runtime-seconds must be in [1,5]")
    started = time.monotonic()
    profiles: dict[str, dict[str, object]] = {}

    for mode in ("NID", "NIV"):
        for surface in ("deep", "shallow"):
            if time.monotonic() - started > args.max_runtime_seconds:
                raise TimeoutError("K7b.2 aggregation deadline exceeded")
            command = [
                sys.executable,
                str(HERE / "166_script_A2_K4_C7_7c_K7b1_high_precision_coefficient_constraint_audit.py"),
                "--max-runtime-seconds", str(args.child_runtime_seconds),
                "--source-runtime-seconds", str(args.source_runtime_seconds),
                "--mode", mode,
                "--surface", surface,
                "--dps", "80",
            ]
            child = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=args.child_runtime_seconds + 1.0,
                check=False,
            )
            data = parse_json(child.stdout)
            D = dict(dict(data["projected_rhs_audit"])["D"])
            M = dict(dict(data["projected_rhs_audit"])["M"])
            seeds = dict(data["projected_seeds"])
            z = float(dict(data["background"])["z_80_digit"])
            D_residual = abs(float(D["absolute_residual"]))
            D_series = abs(float(D["series_derivative"]))
            M_residual = abs(float(M["absolute_residual"]))
            M_series = abs(float(M["series_derivative"]))
            profiles[f"{mode}_{surface}"] = {
                "child_return_code": child.returncode,
                "child_verdict": data.get("execution_verdict"),
                "all_child_checks_pass": all(
                    bool(value) for value in dict(data["checks"]).values()
                ),
                "z": z,
                "D_rhs_absolute_residual": D_residual,
                "D_series_derivative_abs": D_series,
                "D_residual_over_series_derivative": D_residual / max(D_series, 1e-300),
                "M_rhs_absolute_residual": M_residual,
                "M_series_derivative_abs": M_series,
                "M_residual_over_series_derivative": M_residual / max(M_series, 1e-300),
                "density_scaled_residual": float(seeds["density_scaled_residual"]),
                "density_cancellation_condition": float(
                    seeds["density_cancellation_condition"]
                ),
            }

    scaling: dict[str, dict[str, float]] = {}
    for mode in ("NID", "NIV"):
        deep = profiles[f"{mode}_deep"]
        shallow = profiles[f"{mode}_shallow"]
        z_ratio = float(shallow["z"]) / float(deep["z"])

        def exponent(field: str) -> float:
            return math.log(
                float(shallow[field]) / float(deep[field])
            ) / math.log(z_ratio)

        scaling[mode] = {
            "z_shallow_over_deep": z_ratio,
            "D_rhs_residual_power": exponent("D_rhs_absolute_residual"),
            "M_rhs_residual_power": exponent("M_rhs_absolute_residual"),
            "density_scaled_residual_power": exponent("density_scaled_residual"),
            "density_condition_power": exponent("density_cancellation_condition"),
        }

    source_complete = all(
        item["child_return_code"] == 0 and item["all_child_checks_pass"]
        for item in profiles.values()
    )
    payload = {
        "test": "A2-K4 C7.7c-K7b.2 four-surface coefficient-floor scaling",
        "profiles": profiles,
        "deep_shallow_scaling": scaling,
        "source_complete": source_complete,
        "interpretation": {
            "status": "CAPTURED_NOT_A_PASS_GATE",
            "reason": "post-K7b.1 scaling audit; thresholds are not retrofitted",
            "decision_rule": (
                "K7b remains open if an active projected derivative is "
                "dominated by the registered coefficient floor"
            ),
        },
        "execution_verdict": (
            "CAPTURED_C7_7C_K7B2_COEFFICIENT_FLOOR_SCALING"
            if source_complete else "REVIEW_C7_7C_K7B2_SOURCE_UNCLOSED"
        ),
        "physical_verdict": "diagnostic scaling only; no ODE and no score change",
        "fine_depth": "66.5/100",
        "runtime_limits_seconds": {
            "total": args.max_runtime_seconds,
            "child": args.child_runtime_seconds,
            "source_per_child": args.source_runtime_seconds,
        },
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if source_complete else 1


if __name__ == "__main__":
    raise SystemExit(main())

