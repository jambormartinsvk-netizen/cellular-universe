#!/usr/bin/env python
"""Independent bounded order-5/order-6 audit of BR3C-a state surfaces."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import time


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=45.0)
    parser.add_argument("--child-runtime-seconds", type=float, default=15.0)
    parser.add_argument("--x-deep", type=float, default=-25.0)
    parser.add_argument("--x-shallow", type=float, default=-23.0)
    parser.add_argument("--k-mpc", type=float, default=0.05)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 50.0:
        parser.error("max runtime must be in (0,50]")
    if not 0.0 < args.child_runtime_seconds <= 15.0:
        parser.error("child runtime must be in (0,15]")

    started = time.monotonic()
    source = Path(__file__).with_name(
        "130_script_A2_K4_3b_RG_BR3C_a_two_surface_state_export.py"
    )

    def run(order: int) -> dict:
        remaining = args.max_runtime_seconds - (time.monotonic() - started)
        if remaining <= 1.0:
            raise TimeoutError("BR3C-a order audit deadline exceeded")
        command = [
            sys.executable,
            str(source),
            "--max-runtime-seconds",
            str(args.child_runtime_seconds),
            "--standard-order",
            str(order),
            "--x-deep",
            str(args.x_deep),
            "--x-shallow",
            str(args.x_shallow),
            "--k-mpc",
            str(args.k_mpc),
            "--fuel-fraction-coefficient",
            "1.0",
        ]
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=min(20.0, max(1.0, remaining)),
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"script 130 order {order} returned {completed.returncode}: "
                f"{completed.stderr[-1000:]} {completed.stdout[-1000:]}"
            )
        return json.loads(completed.stdout)

    order5 = run(5)
    order6 = run(6)
    checks = {
        "order5_source_pass": order5.get("execution_verdict")
        == "PASS_BR3C_A_TWO_SURFACE_STATE",
        "order6_source_pass": order6.get("execution_verdict")
        == "PASS_BR3C_A_TWO_SURFACE_STATE",
    }

    comparison = {}
    maximum_scaled_difference = 0.0
    maximum_absolute_difference = 0.0
    for mode in ("NID", "NIV"):
        comparison[mode] = {}
        for surface in ("deep", "shallow"):
            left = order5["BR3C_state_surfaces"][mode]["surfaces"][surface]
            right = order6["BR3C_state_surfaces"][mode]["surfaces"][surface]
            fields = {}
            surface_pass = True
            for group in ("state", "omegas"):
                for key, value5 in left[group].items():
                    value6 = right[group][key]
                    absolute = abs(value5 - value6)
                    scale = max(abs(value5), abs(value6), 1e-30)
                    scaled = absolute / (1e-10 + scale)
                    passed = absolute <= 1e-10 + 1e-8 * scale
                    fields[f"{group}.{key}"] = {
                        "absolute_difference": absolute,
                        "scaled_difference": scaled,
                        "pass": passed,
                    }
                    maximum_absolute_difference = max(
                        maximum_absolute_difference, absolute
                    )
                    maximum_scaled_difference = max(
                        maximum_scaled_difference, scaled
                    )
                    surface_pass = surface_pass and passed
            z_equal = abs(left["z"] - right["z"]) < 1e-30
            checks[f"{mode}_{surface}_same_z"] = z_equal
            checks[f"{mode}_{surface}_order5_order6_state_stable"] = surface_pass
            comparison[mode][surface] = {
                "z": left["z"],
                "fields": fields,
                "all_fields_pass": surface_pass,
            }

        norm5 = order5["BR3C_state_surfaces"][mode]["normalization"]
        norm6 = order6["BR3C_state_surfaces"][mode]["normalization"]
        checks[f"{mode}_same_normalization_anchor"] = norm5 == norm6

    checks["maximum_scaled_difference_below_1e-8"] = (
        maximum_scaled_difference < 1e-8
    )
    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4.3b-RG BR3C-a order-5/order-6 state audit",
        "source": source.name,
        "checks": checks,
        "comparison": comparison,
        "maximum_absolute_difference": maximum_absolute_difference,
        "maximum_scaled_difference": maximum_scaled_difference,
        "execution_verdict": (
            "PASS_BR3C_A_ORDER5_ORDER6_STATE_AUDIT"
            if passed
            else "REVIEW_BR3C_A_ORDER_AUDIT_UNCLOSED"
        ),
        "physical_verdict": (
            "K4 survives C7.7a cross-order audit"
            if passed
            else "no death verdict; inspect failed state comparison"
        ),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired as exc:
        print(
            json.dumps(
                {"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}
            )
        )
        raise SystemExit(124)
    except TimeoutError as exc:
        print(
            json.dumps(
                {"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}
            )
        )
        raise SystemExit(124)
    except Exception as exc:
        print(
            json.dumps(
                {"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}
            )
        )
        raise SystemExit(2)

