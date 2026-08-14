#!/usr/bin/env python3
"""Run one bounded K11-CS2/v002 structural-truncation lmax shard."""

from __future__ import annotations

import argparse
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
    # Lazy import is intentional: CLI validation must not pay CAMB/SymPy cost.
    from scripts.baseScripts.a2_k11_cs2.finite_hierarchy_preflight_v002 import (
        run_preflight,
    )

    result = run_preflight(
        lmax_values=(args.lmax,),
        max_runtime_seconds=args.max_runtime_seconds,
    )
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
                "lmax": args.lmax,
                "verdict": result["verdict"],
                "runtime_seconds": result["runtime_seconds"],
                "output": str(output),
            },
            sort_keys=True,
        ),
        flush=True,
    )
    return 0 if str(result["verdict"]).startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())

