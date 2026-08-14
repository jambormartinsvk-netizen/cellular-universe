#!/usr/bin/env python
"""Bounded P5.3g7 mode-resolved seed audit.

The only executable phase at present is M3-TCA0.  FULL-FINITE-OPACITY is
fail-closed until an audited n_e0*sigma_T normalization is supplied.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time

from baseScripts.p5_general_synchronous.mode_resolved_puiseux import (
    FrozenInputs,
    run_m3_tca0,
    symbolic_identities,
)


ROOT = Path(__file__).resolve().parents[1]
BASE = Path(__file__).with_name("baseScripts") / "p5_general_synchronous" / "mode_resolved_puiseux.py"
PREREG = ROOT / "tracks" / "A1" / "A1K1" / "A2" / "A2K4" / "SUBTRACKS" / "P5" / "P5_3_SEEDS" / "27_P5_3G7_M3_MODE_RESOLVED_PUISEUX_PREREGISTRATION_SK.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--phase", choices=("m3-tca0", "full-finite-opacity"), default="m3-tca0")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_once(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable output: {path}")
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0,5]")
    if not BASE.is_file() or not PREREG.is_file():
        raise FileNotFoundError("authoritative base module or preregistration is missing")
    started = time.monotonic()
    if args.smoke:
        residuals = symbolic_identities(FrozenInputs())
        passed = all(value == 0 for value in residuals.values())
        payload = {
            "test": "KMPC-022 smoke",
            "checks": {key: bool(value == 0) for key, value in residuals.items()},
            "verdict": "SMOKE_PASS" if passed else "SMOKE_STOP",
            "runtime_seconds": time.monotonic() - started,
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if passed else 1
    if args.output is None:
        raise ValueError("--output is required outside --smoke")
    if args.phase == "full-finite-opacity":
        payload = {
            "test": "KMPC-022 P5.3g7 full finite-opacity gate",
            "phase": "FULL-FINITE-OPACITY",
            "verdict": "REVIEW_BLOCKED_MISSING_DERIVED_NE0_SIGMA_T",
            "physical_calculation_executed": False,
            "reason": "P5.3g4/g5/g6 determine the formula and gauge map, but not the exact-A1 finite-start opacity normalization",
            "runtime_limit_seconds": args.max_runtime_seconds,
            "runtime_seconds": time.monotonic() - started,
        }
        write_once(args.output, payload)
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 3
    payload = run_m3_tca0(args.max_runtime_seconds)
    payload["source_sha256"] = {"base": sha256(BASE), "preregistration": sha256(PREREG)}
    write_once(args.output, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["verdict"] == "PASS_M3_TCA0_CONDITIONAL" else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)

