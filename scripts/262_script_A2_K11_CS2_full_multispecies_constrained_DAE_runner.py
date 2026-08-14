#!/usr/bin/env python3
"""Thin bounded runner for the preregistered K11-CS2 base module.

Only ``--mode structural`` is currently authorized.  Evolution remains
fail-closed in the base module and cannot accidentally emit a physics PASS.
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
    parser.add_argument("--mode", choices=("structural",), default="structural")
    parser.add_argument("--lmax", type=int, default=8)
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = exact_structural_audit(
        lmax=args.lmax,
        max_runtime_seconds=args.max_runtime_seconds,
    )
    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output is not None:
        output = args.output.resolve()
        if output.exists():
            raise FileExistsError(f"immutable output already exists: {output}")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if result["verdict"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())

