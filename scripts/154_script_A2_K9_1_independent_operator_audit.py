#!/usr/bin/env python
"""Independent bounded audit of A2-K9.1 source output and interpretation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import time


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        parser.error("runtime must be in (0,5]")
    started = time.monotonic()
    source = Path(__file__).with_name("153_script_A2_K9_1_collision_moment_nonuniqueness.py")
    run = subprocess.run([sys.executable, str(source), "--max-runtime-seconds", "4"],
                         capture_output=True, text=True, timeout=4.5, check=False)
    if run.returncode != 0:
        raise RuntimeError(f"script 153 returned {run.returncode}: {run.stdout[-1000:]}")
    payload = json.loads(run.stdout)
    rows = payload["elastic_family"]
    checks = {
        "source_pass": payload.get("execution_verdict") == "PASS_K9_1_MOMENT_NONUNIQUENESS",
        "all_source_checks_pass": all(payload.get("checks", {}).values()),
        "same_number_moment_for_all_kappa": len({x["number_moment"] for x in rows}) == 1,
        "same_background_energy_for_all_kappa": len({x["background_energy"] for x in rows}) == 1,
        "different_linear_momentum_for_each_kappa": len({x["linear_momentum"] for x in rows}) == len(rows),
        "parent_G2_not_claimed": payload.get("gate_verdict") == "G2_OPEN_CONCRETE_COMMON_KERNEL_REQUIRED",
    }
    passed = all(checks.values())
    print(json.dumps({
        "test": "A2-K9.1 independent operator audit",
        "checks": checks,
        "execution_verdict": "PASS_K9_1_INDEPENDENT_AUDIT" if passed else "REVIEW_K9_1_UNCLOSED",
        "physical_verdict": "K9 remains a live G1 design class; one named operator is not yet a specified operator",
        "fine_depth": "10.0/100",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic()-started,
    }, indent=2, sort_keys=True))
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

