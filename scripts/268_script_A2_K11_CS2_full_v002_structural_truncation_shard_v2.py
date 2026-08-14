#!/usr/bin/env python3
"""Run one bounded K11-CS2/v002 structural shard with generic scope IDs."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lmax", type=int, choices=(4, 6, 8), required=True)
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    from scripts.baseScripts.a2_k11_cs2.finite_hierarchy_preflight_v002 import (
        run_preflight,
    )

    result = run_preflight(
        lmax_values=(args.lmax,),
        max_runtime_seconds=args.max_runtime_seconds,
    )
    upstream = str(result["verdict"])
    if not upstream.startswith("PASS_") or not all(result["checks"].values()):
        result["technical_attempt"] = 3
        result["upstream_scope_verdict"] = upstream
        result["verdict"] = "STOP_ARCH_A_STRUCTURAL_OR_CONTRACT_FAILURE"
        exit_code = 2
    else:
        result["technical_attempt"] = 3
        result["upstream_scope_verdict"] = upstream
        result["verdict"] = (
            "PASS_ARCH_A_EXACT_SET_INTERIOR_AND_REGISTERED_TRUNCATION_ONLY"
        )
        exit_code = 0
    result["test"] = "K11-CS2 full v002 structural truncation shard"
    runner = Path(__file__).resolve()
    result["runner_sha256"] = sha256(runner.read_bytes()).hexdigest().upper()

    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"immutable output already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "technical_attempt": 3,
                "lmax": args.lmax,
                "verdict": result["verdict"],
                "runtime_seconds": result["runtime_seconds"],
                "output": str(output),
            },
            sort_keys=True,
        ),
        flush=True,
    )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

