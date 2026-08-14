"""Bounded PF-064 repair runner for the independent R-A B1 contract guard."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from baseScripts.p5_general_synchronous.full_ra_b1_preflight_v2 import build_contract_guard


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--max-runtime-seconds", type=float, default=5.0)
    result.add_argument("--output", type=Path)
    result.add_argument("--smoke", action="store_true")
    return result


def main() -> int:
    args = parser().parse_args()
    limit = min(args.max_runtime_seconds, 2.0) if args.smoke else args.max_runtime_seconds
    payload = build_contract_guard(limit)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "execution_verdict": payload["execution_verdict"],
        "runtime_seconds": payload["runtime_seconds"],
        "checks_passed": sum(bool(value) for value in payload["checks"].values()),
        "checks_total": len(payload["checks"]),
        "negative_fixtures": len(payload["negative_fixtures"]),
        "output": str(args.output) if args.output else None,
    }, sort_keys=True), flush=True)
    return 0 if payload["execution_verdict"] == "PASS_R_A_B1_CONTRACT_GUARD_ONLY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
