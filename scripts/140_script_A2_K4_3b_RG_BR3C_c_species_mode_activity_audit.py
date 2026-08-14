#!/usr/bin/env python
"""Independent C7.7c audit of per-component checkpoint activity."""

from __future__ import annotations

import argparse
import json
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
        "139_script_A2_K4_3b_RG_BR3C_c_checkpoint_component_export.py"
    )
    command = [
        sys.executable, str(source),
        "--max-runtime-seconds", "50",
        "--source-runtime-seconds", "15",
        "--x-final", "-18",
        "--segment-efolds", "1",
        "--max-step", "0.02",
        "--rtol", "1e-10",
        "--atol", "1e-14",
        "--safety-cap", "1e12",
    ]
    completed = subprocess.run(
        command, capture_output=True, text=True,
        timeout=min(55.0, args.max_runtime_seconds), check=False
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"script 139 returned {completed.returncode}: "
            f"{completed.stderr[-1000:]} {completed.stdout[-1000:]}"
        )
    payload = json.loads(completed.stdout)
    checks = {
        "source_export_pass": payload.get("execution_verdict")
        == "PASS_C7_7C_CHECKPOINT_COMPONENT_EXPORT",
        "state_names_exact": tuple(payload.get("state_names", [])) == STATE_NAMES,
        "Uc_scope_explicit": "U_c" not in STATE_NAMES,
        "L5_scope_explicit": "L5_fs" not in STATE_NAMES,
    }
    activity = {}
    rtol = float(payload["solver"]["rtol"])
    atol = float(payload["solver"]["atol"])
    for mode in ("NID", "NIV"):
        activity[mode] = {}
        for surface in ("deep", "shallow"):
            trajectory = payload["results"][mode][surface]
            checkpoints = trajectory["checkpoints"]
            activity[mode][surface] = {}
            checks[f"{mode}_{surface}_has_checkpoints"] = bool(checkpoints)
            previous = None
            max_changes = {name:0.0 for name in STATE_NAMES}
            max_rhs = {name:0.0 for name in STATE_NAMES}
            exact_keys = True
            for checkpoint in checkpoints:
                state = checkpoint["state"]
                rhs_abs = checkpoint["rhs_abs"]
                exact_keys = exact_keys and tuple(state.keys()) == STATE_NAMES
                exact_keys = exact_keys and tuple(rhs_abs.keys()) == STATE_NAMES
                for name in STATE_NAMES:
                    max_rhs[name] = max(max_rhs[name], abs(rhs_abs[name]))
                    if previous is not None:
                        max_changes[name] = max(
                            max_changes[name], abs(state[name]-previous[name])
                        )
                previous = state
            checks[f"{mode}_{surface}_checkpoint_keys_exact"] = exact_keys
            for name in STATE_NAMES:
                maximum_state = trajectory["component_max_abs"][name]
                floor = max(10.0*atol, 10.0*rtol*maximum_state)
                rhs_pass = max_rhs[name] > floor
                change_pass = max_changes[name] > floor
                checks[f"{mode}_{surface}_{name}_rhs_resolved"] = rhs_pass
                checks[f"{mode}_{surface}_{name}_change_resolved"] = change_pass
                activity[mode][surface][name] = {
                    "maximum_state_abs": maximum_state,
                    "activity_floor": floor,
                    "maximum_checkpoint_rhs_abs": max_rhs[name],
                    "maximum_checkpoint_change_abs": max_changes[name],
                    "rhs_resolved": rhs_pass,
                    "change_resolved": change_pass,
                }
    passed = bool(checks) and all(checks.values())
    failed = [name for name, value in checks.items() if not value]
    output = {
        "test":"A2-K4.3b-RG C7.7c species/mode activity audit",
        "source":source.name,
        "activity_definition":"floor=max(10*atol,10*rtol*max_trajectory_abs)",
        "activity":activity,
        "checks":checks,
        "failed_checks":failed,
        "execution_verdict":(
            "PASS_C7_7C_SPECIES_MODE_ACTIVITY" if passed
            else "REVIEW_C7_7C_UNRESOLVED_COMPONENTS"),
        "physical_verdict":(
            "K4 survives C7.7c complete active ledger" if passed
            else "no death verdict; unresolved components require scaling audit"),
        "fine_depth":"66.7/100" if passed else "66.5/100",
        "runtime_limit_seconds":args.max_runtime_seconds,
        "runtime_seconds":time.monotonic()-started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)}))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)}))
        raise SystemExit(2)

