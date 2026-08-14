#!/usr/bin/env python3
"""Technical rerun 1 for K11-CS2/S0 with bounded concise stdout.

Physics and all exact checks remain in the immutable-hash base module.  This
runner changes only output behavior relative to script 262.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.baseScripts.a2_k11_cs2 import exact_structural_audit  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lmax", type=int, default=8)
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = exact_structural_audit(
        lmax=args.lmax,
        max_runtime_seconds=args.max_runtime_seconds,
    )
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"immutable output already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = {
        "verdict": result["verdict"],
        "runtime_seconds": result["runtime_seconds"],
        "output": str(output),
        "full_payload_printed": False,
    }
    print(json.dumps(summary, sort_keys=True), flush=True)
    return 0 if result["verdict"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())

