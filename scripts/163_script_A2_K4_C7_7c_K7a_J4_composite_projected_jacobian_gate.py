#!/usr/bin/env python
"""Bounded composite K7a-J4 gate: safe projected audit plus 80-digit J3."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser()
    result.add_argument("--max-runtime-seconds", type=float, required=True)
    result.add_argument("--projected-runtime-seconds", type=float, default=6.0)
    result.add_argument("--source-runtime-seconds", type=float, default=3.0)
    result.add_argument("--tprime-runtime-seconds", type=float, default=2.0)
    result.add_argument("--profile-mode", choices=("NID", "NIV"), required=True)
    result.add_argument("--profile-surface", choices=("deep", "shallow"), required=True)
    return result


def parse_json(stdout: str, label: str) -> dict[str, object]:
    start = stdout.find("{")
    end = stdout.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError(f"{label} returned no JSON")
    return json.loads(stdout[start:end+1])


def main() -> int:
    args = parser().parse_args()
    if not 1.0 <= args.max_runtime_seconds <= 20.0:
        raise SystemExit("max-runtime-seconds must be in [1,20]")
    if not 0.5 <= args.projected_runtime_seconds <= 8.0:
        raise SystemExit("projected-runtime-seconds must be in [0.5,8]")
    if not 0.5 <= args.source_runtime_seconds <= 5.0:
        raise SystemExit("source-runtime-seconds must be in [0.5,5]")
    if not 0.5 <= args.tprime_runtime_seconds <= 5.0:
        raise SystemExit("tprime-runtime-seconds must be in [0.5,5]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic()-started > args.max_runtime_seconds:
            raise TimeoutError("K7a-J4 composite deadline exceeded")

    projected_command = [
        sys.executable,
        str(HERE/"162_script_A2_K4_C7_7c_K7a_J4_safe_projected_jacobian_audit.py"),
        "--max-runtime-seconds", str(args.projected_runtime_seconds),
        "--source-runtime-seconds", str(args.source_runtime_seconds),
        "--x-final", "-18",
        "--segment-efolds", "1",
        "--max-step", "0.02",
        "--rtol", "1e-10",
        "--atol", "1e-12",
        "--safety-cap", "1e12",
        "--profile-mode", args.profile_mode,
        "--profile-surface", args.profile_surface,
        "--profile-segments", "1",
    ]
    projected_child = subprocess.run(
        projected_command,
        capture_output=True,
        text=True,
        timeout=args.projected_runtime_seconds+1.0,
        check=False,
    )
    projected = parse_json(projected_child.stdout, "projected child")
    deadline()

    tprime_command = [
        sys.executable,
        str(HERE/"161_script_A2_K4_C7_7c_K7a_J3_cancellation_safe_Tprime_audit.py"),
        "--max-runtime-seconds", str(args.tprime_runtime_seconds),
        "--mode", args.profile_mode,
        "--surface", args.profile_surface,
        "--dps", "80",
    ]
    tprime_child = subprocess.run(
        tprime_command,
        capture_output=True,
        text=True,
        timeout=args.tprime_runtime_seconds+1.0,
        check=False,
    )
    tprime = parse_json(tprime_child.stdout, "Tprime child")
    deadline()

    projected_checks = dict(projected.get("checks", {}))
    fd_keys = [key for key in projected_checks if key.endswith("_K7a_Tprime_fd")]
    non_fd_checks = {
        key: value for key, value in projected_checks.items() if key not in fd_keys
    }
    audit = dict(projected.get("results", {}))
    # The K7a block is nested below mode/surface in the inherited result format.
    mode_result = dict(audit.get(args.profile_mode, {}))
    surface_result = dict(mode_result.get(args.profile_surface, {}))
    projected_audit = dict(
        surface_result.get("K7a_projected_jacobian_audit", {})
    )
    tprime_checks = dict(tprime.get("checks", {}))

    checks = {
        "projected_json_parsed": bool(projected),
        "Tprime_json_parsed": bool(tprime),
        "exactly_one_legacy_fd_diagnostic_present": len(fd_keys) == 1,
        "all_nonlegacy_projected_checks_pass": (
            bool(non_fd_checks) and all(bool(value) for value in non_fd_checks.values())
        ),
        "safe_ell_method_reported": (
            projected_audit.get("ell_method") == "denominator_x/denominator"
        ),
        "legacy_fd_remains_visible": (
            projected_audit.get("legacy_double_Tprime_fd_retained") is True
        ),
        "Tprime_child_exit_zero": tprime_child.returncode == 0,
        "Tprime_J3_verdict_pass": (
            tprime.get("execution_verdict")
            == "PASS_C7_7C_K7A_J3_CANCELLATION_SAFE_TPRIME"
        ),
        "all_Tprime_J3_checks_pass": (
            bool(tprime_checks) and all(bool(value) for value in tprime_checks.values())
        ),
        "Tprime_mode_matches": tprime.get("mode_label") == args.profile_mode,
        "Tprime_surface_matches": tprime.get("surface") == args.profile_surface,
    }
    passed = all(checks.values())
    payload = {
        "test": "A2-K4 C7.7c-K7a-J4 composite projected Jacobian gate",
        "profile_request": {
            "mode": args.profile_mode,
            "surface": args.profile_surface,
        },
        "child_return_codes": {
            "safe_projected": projected_child.returncode,
            "high_precision_Tprime": tprime_child.returncode,
        },
        "legacy_fd_diagnostic": {
            "keys": fd_keys,
            "values": {key: projected_checks[key] for key in fd_keys},
            "authoritative_for_J4": False,
            "reason": "J1 double-FD cancellation; replaced by bounded J3 evidence",
        },
        "safe_projected_summary": {
            "ell_method": projected_audit.get("ell_method"),
            "projected_relative_frobenius_error": projected_audit.get(
                "projected_relative_frobenius_error"
            ),
            "projected_max_abs_error": projected_audit.get(
                "projected_max_abs_error"
            ),
            "transform_condition_2": projected_audit.get("transform_condition_2"),
            "zero_limit_max_residual": projected_audit.get(
                "zero_limit_max_residual"
            ),
            "full_projected_spectral_radius": projected_audit.get(
                "full_projected_spectral_radius"
            ),
        },
        "high_precision_Tprime_summary": {
            "execution_verdict": tprime.get("execution_verdict"),
            "safe_relative_error": dict(tprime.get("Tprime", {})).get(
                "safe_relative_error"
            ),
        },
        "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7A_J4_COMPOSITE_PROJECTED_JACOBIAN"
            if passed else "REVIEW_C7_7C_K7A_J4_COMPOSITE_UNCLOSED"
        ),
        "physical_verdict": "algebraic/Jacobian gate only; no ODE evolution",
        "fine_depth": "66.5/100",
        "runtime_limits_seconds": {
            "total": args.max_runtime_seconds,
            "safe_projected": args.projected_runtime_seconds,
            "source": args.source_runtime_seconds,
            "high_precision_Tprime": args.tprime_runtime_seconds,
        },
        "runtime_seconds": time.monotonic()-started,
        "stderr_tail": {
            "safe_projected": projected_child.stderr[-500:],
            "high_precision_Tprime": tprime_child.stderr[-500:],
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

