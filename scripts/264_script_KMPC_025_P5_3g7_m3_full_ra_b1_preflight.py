"""Bounded runner for the exact A2-K4 R-A B1 preflight."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from baseScripts.p5_general_synchronous.full_ra_b1_preflight import build_preflight


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--max-runtime-seconds", type=float, default=5.0)
    result.add_argument("--output", type=Path)
    result.add_argument("--smoke", action="store_true")
    return result


def main() -> int:
    args = parser().parse_args()
    limit = min(args.max_runtime_seconds, 2.0) if args.smoke else args.max_runtime_seconds
    payload = build_preflight(limit)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "execution_verdict": payload["execution_verdict"],
        "runtime_seconds": payload["runtime_seconds"],
        "checks_passed": sum(bool(value) for value in payload["checks"].values()),
        "checks_total": len(payload["checks"]),
        "output": str(args.output) if args.output else None,
    }
    print(json.dumps(summary, sort_keys=True), flush=True)
    return 0 if payload["execution_verdict"] == "PASS_R_A_B1_PREFLIGHT_ONLY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
