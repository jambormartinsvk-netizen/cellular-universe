#!/usr/bin/env python
"""Independent bounded frame and verdict audit for A2-K8.1."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import subprocess
import sys
import time


def dot(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    return -a[0]*b[0] + sum(a[i]*b[i] for i in range(1, 4))


def projection(q: tuple[float, ...], u: tuple[float, ...]) -> tuple[float, ...]:
    uq = dot(u, q)
    return tuple(q[i]+u[i]*uq for i in range(4))


def four_velocity(vx: float) -> tuple[float, ...]:
    gamma = 1.0/math.sqrt(1.0-vx*vx)
    return (gamma, gamma*vx, 0.0, 0.0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        parser.error("runtime must be in (0,5]")
    started = time.monotonic()
    source = Path(__file__).with_name(
        "150_script_A2_K8_1_number_source_covariant_moment_ledger.py"
    )
    run = subprocess.run(
        [sys.executable, str(source), "--max-runtime-seconds", "4", "--samples", "1000"],
        capture_output=True, text=True, timeout=4.5, check=False,
    )
    if run.returncode != 0:
        raise RuntimeError(f"script 150 returned {run.returncode}: {run.stdout[-800:]} {run.stderr[-800:]}")
    payload = json.loads(run.stdout)
    uc = four_velocity(0.10)
    uf = four_velocity(-0.12)
    q = 0.15
    Qc = tuple(q*x for x in uc)
    Qf = tuple(q*x for x in uf)
    Pc = projection(Qc, uc)
    Pf_in_c = projection(Qf, uc)
    checks = {
        "source_ledger_pass": payload.get("execution_verdict") == "PASS_K8_1_MOMENT_IDENTITIES",
        "all_source_checks_pass": all(payload.get("checks", {}).values()),
        "comoving_injection_has_zero_c_frame_momentum": max(abs(x) for x in Pc) < 2e-14,
        "different_birth_frame_has_nonzero_c_frame_momentum": max(abs(x) for x in Pf_in_c) > 1e-4,
        "parent_gate_remains_open": payload.get("gate_verdict") == "G2_PARENT_OPEN_MOMENT_NOT_FIXED_BY_Sn",
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K8.1 independent frame mapping audit",
        "checks": checks,
        "c_frame_spatial_projection_for_Q_parallel_uc": Pc,
        "c_frame_spatial_projection_for_Q_parallel_uf": Pf_in_c,
        "frame_map": {
            "Q_parallel_u_c": "deterministic cold-fluid limit maps to A2-K1",
            "Q_parallel_u_f": "deterministic cold-fluid limit maps to A2-K3",
            "Q_parallel_u_d": "deterministic cold-fluid limit maps to A2-K4",
            "general_collision_kernel": "genuinely open K8 daughter; must specify momentum, pressure and noise moments",
        },
        "execution_verdict": "PASS_K8_1_INDEPENDENT_FRAME_AUDIT" if passed else "REVIEW_K8_1_FRAME_AUDIT",
        "physical_verdict": "K8 parent remains open at G1; scalar S_n alone cannot pass G2",
        "fine_depth": "10.0/100",
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

