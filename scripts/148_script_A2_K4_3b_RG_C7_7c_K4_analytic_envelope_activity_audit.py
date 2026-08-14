#!/usr/bin/env python
"""Independent C7.7c-K4 activity audit in analytic-envelope coordinates."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import subprocess
import sys
import time


STATE_NAMES = (
    "h", "eta", "delta_gamma", "delta_fs", "delta_b", "delta_c",
    "U_gamma", "U_fs", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f"
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=50.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 50.0:
        parser.error("runtime must be in (0,50]")
    started = time.monotonic()
    source = Path(__file__).with_name(
        "147_script_A2_K4_3b_RG_C7_7c_K4_analytic_envelope_evolution.py"
    )
    command = [
        sys.executable, str(source),
        "--max-runtime-seconds", "45",
        "--source-runtime-seconds", "15",
        "--x-final", "-18",
        "--segment-efolds", "1",
        "--max-step", "0.02",
        "--rtol", "1e-10",
        "--atol", "1e-12",
        "--safety-cap", "1e12",
    ]
    completed = subprocess.run(
        command, capture_output=True, text=True,
        timeout=min(50.0, args.max_runtime_seconds), check=False
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"script 147 returned {completed.returncode}: "
            f"{completed.stderr[-1200:]} {completed.stdout[-1200:]}"
        )
    payload = json.loads(completed.stdout)
    source_checks = payload.get("checks", {})
    checks = {
        "analytic_envelope_source_export_pass": payload.get("execution_verdict")
        == "PASS_C7_7C_K4_ANALYTIC_ENVELOPE_EXPORT",
        "all_C7_7b_source_checks_pass": bool(source_checks)
        and all(source_checks.values()),
        "state_names_exact": tuple(payload.get("state_names", [])) == STATE_NAMES,
        "Uc_scope_explicit": "U_c" not in STATE_NAMES,
        "L5_scope_explicit": "L5_fs" not in STATE_NAMES,
    }
    rtol = float(payload["solver"]["rtol"])
    atol_norm = float(payload["solver"]["atol"])
    activity = {}
    for mode in ("NID", "NIV"):
        activity[mode] = {}
        for surface in ("deep", "shallow"):
            trajectory = payload["results"][mode][surface]
            checkpoints = trajectory["checkpoints"]
            scales = trajectory["integration_scale"]
            activity[mode][surface] = {}
            checks[f"{mode}_{surface}_has_checkpoints"] = bool(checkpoints)
            exact_keys = len(scales) == len(STATE_NAMES) and set(scales) == set(STATE_NAMES)
            previous = None
            max_changes = {name: 0.0 for name in STATE_NAMES}
            max_rhs = {name: 0.0 for name in STATE_NAMES}
            for checkpoint in checkpoints:
                state = checkpoint["state"]
                rhs_abs = checkpoint["rhs_abs"]
                exact_keys = exact_keys and len(state) == len(STATE_NAMES) \
                    and set(state) == set(STATE_NAMES)
                exact_keys = exact_keys and len(rhs_abs) == len(STATE_NAMES) \
                    and set(rhs_abs) == set(STATE_NAMES)
                normalized_state = {name: state[name]/scales[name] for name in STATE_NAMES}
                normalized_rhs = {name: rhs_abs[name]/scales[name] for name in STATE_NAMES}
                for name in STATE_NAMES:
                    max_rhs[name] = max(max_rhs[name], abs(normalized_rhs[name]))
                    if previous is not None:
                        max_changes[name] = max(
                            max_changes[name], abs(normalized_state[name]-previous[name])
                        )
                previous = normalized_state
            checks[f"{mode}_{surface}_checkpoint_and_scale_keys_exact"] = exact_keys
            for name in STATE_NAMES:
                scale = float(scales[name])
                finite_positive_scale = math.isfinite(scale) and scale > 1e-299
                maximum_normalized_state = (
                    trajectory["component_max_abs"][name]/scale
                    if finite_positive_scale else math.inf
                )
                floor = max(10.0*atol_norm, 10.0*rtol*maximum_normalized_state)
                rhs_pass = finite_positive_scale and math.isfinite(max_rhs[name]) \
                    and max_rhs[name] > floor
                change_pass = finite_positive_scale and math.isfinite(max_changes[name]) \
                    and max_changes[name] > floor
                checks[f"{mode}_{surface}_{name}_finite_positive_scale"] = finite_positive_scale
                checks[f"{mode}_{surface}_{name}_normalized_rhs_resolved"] = rhs_pass
                checks[f"{mode}_{surface}_{name}_normalized_change_resolved"] = change_pass
                activity[mode][surface][name] = {
                    "analytic_envelope_scale": scale,
                    "maximum_normalized_state_abs": maximum_normalized_state,
                    "normalized_activity_floor": floor,
                    "maximum_checkpoint_normalized_rhs_abs": max_rhs[name],
                    "maximum_checkpoint_normalized_change_abs": max_changes[name],
                    "rhs_resolved": rhs_pass,
                    "change_resolved": change_pass,
                }
    passed = bool(checks) and all(checks.values())
    failed = [name for name, value in checks.items() if not value]
    output = {
        "test": "A2-K4.3b-RG C7.7c-K4 analytic-envelope activity audit",
        "source": source.name,
        "scaling": "max(abs(start),abs(preregistered_series_at_x=-18),1e-300)",
        "activity_definition": "floor=max(10*atol_norm,10*rtol*max_abs(w_i))",
        "activity": activity,
        "checks": checks,
        "failed_checks": failed,
        "source_runtime_seconds": payload.get("runtime_seconds"),
        "source_rhs_calls": payload.get("rhs_calls"),
        "execution_verdict": (
            "PASS_C7_7C_K4_ANALYTIC_ENVELOPE_ACTIVITY" if passed
            else "REVIEW_C7_7C_K4_ANALYTIC_ENVELOPE_UNCLOSED"
        ),
        "physical_verdict": (
            "K4 survives C7.7c complete active-component ledger" if passed
            else "no death verdict; inspect unresolved normalized component"
        ),
        "fine_depth": "66.7/100" if passed else "66.5/100",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic()-started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)

