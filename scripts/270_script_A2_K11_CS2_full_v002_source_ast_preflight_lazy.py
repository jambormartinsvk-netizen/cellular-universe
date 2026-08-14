#!/usr/bin/env python3
"""Run K11-CS2/v002 source-AST preflight through the audited lazy package."""

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
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    from scripts.baseScripts.a2_k11_cs2.finite_hierarchy_source_ast_preflight_v003 import (
        run_source_ast_preflight,
    )

    result = run_source_ast_preflight(max_runtime_seconds=args.max_runtime_seconds)
    result["technical_attempt"] = 5
    runner = Path(__file__).resolve()
    package_init = runner.parent / "baseScripts" / "a2_k11_cs2" / "__init__.py"
    result["runner_sha256"] = sha256(runner.read_bytes()).hexdigest().upper()
    result["package_init_sha256"] = sha256(package_init.read_bytes()).hexdigest().upper()
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
                "technical_attempt": result["technical_attempt"],
                "verdict": result["verdict"],
                "checks": result["check_count"],
                "failed": len(result["failed_checks"]),
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

