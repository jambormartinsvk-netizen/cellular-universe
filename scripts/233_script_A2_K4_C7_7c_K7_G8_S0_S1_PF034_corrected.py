#!/usr/bin/env python
"""Bounded PF-034 correction for G8 SCREEN-S0+S1; no ODEs or score award."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "scripts" / "baseScripts"
if str(BASE) not in sys.path:
    sys.path.insert(0, str(BASE))

from a2_k4_g8.structural_pf034 import exact_s0_s1_audit_pf034, state_names  # noqa: E402


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def write_immutable(path: Path, payload: dict[str, object]) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable output: {path}")
    if not path.parent.exists():
        raise FileNotFoundError(f"output parent does not exist: {path.parent}")
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-runtime-seconds", type=float, default=10.0)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 20.0):
        parser.error("--max-runtime-seconds must be in (0, 20]")
    if not args.smoke and args.output is None:
        parser.error("--output is required unless --smoke")
    if args.smoke:
        names = state_names(8)
        print(json.dumps({"smoke": "PASS", "lmax_8_count": len(names),
                          "first": names[0], "last": names[-1]}, sort_keys=True))
        return 0
    payload = exact_s0_s1_audit_pf034(args.max_runtime_seconds)
    payload["script_sha256"] = sha256_file(Path(__file__).resolve())
    payload["shared_module_sha256"] = sha256_file(BASE / "a2_k4_g8" / "structural_pf034.py")
    write_immutable(args.output.resolve(), payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["verdict"] == "PASS_G8_SCREEN_S0_S1_STRUCTURAL" else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}, sort_keys=True))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"verdict": "ERROR_UNCLOSED", "error": repr(exc)}, sort_keys=True))
        raise SystemExit(2)
