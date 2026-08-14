#!/usr/bin/env python
"""Bounded SHA-256 manifest for BR3C-b scripts 136 and 137."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 10.0:
        parser.error("runtime must be in (0,10]")
    started = time.monotonic()
    root = Path(__file__).parent
    names = [
        "136_script_A2_K4_3b_RG_BR3C_b_segmented_early_evolution.py",
        "137_script_A2_K4_3b_RG_BR3C_b_equation_sign_audit.py",
    ]
    files = {}
    for name in names:
        if time.monotonic()-started > args.max_runtime_seconds:
            raise TimeoutError("BR3C-b manifest deadline exceeded")
        data = (root/name).read_bytes()
        files[name] = {
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        }
    passed = len(files) == len(names) and all(
        len(item["sha256"]) == 64 for item in files.values()
    )
    print(json.dumps({
        "test":"A2-K4.3b-RG BR3C-b scripts 136-137 SHA-256 manifest",
        "files":files,
        "execution_verdict":(
            "PASS_BR3C_B_MANIFEST_CREATED" if passed
            else "REVIEW_BR3C_B_MANIFEST_UNCLOSED"),
        "runtime_limit_seconds":args.max_runtime_seconds,
        "runtime_seconds":time.monotonic()-started,
    }, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)}))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)}))
        raise SystemExit(2)

