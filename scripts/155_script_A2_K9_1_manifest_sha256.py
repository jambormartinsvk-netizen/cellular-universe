#!/usr/bin/env python
"""Bounded SHA-256 manifest for A2-K9.1 scripts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import time


def main() -> None:
    started = time.monotonic()
    root = Path(__file__).resolve().parent
    files = {}
    for name in (
        "153_script_A2_K9_1_collision_moment_nonuniqueness.py",
        "154_script_A2_K9_1_independent_operator_audit.py",
    ):
        if time.monotonic()-started > 5.0:
            raise TimeoutError("K9.1 manifest deadline exceeded")
        data = (root/name).read_bytes()
        files[name] = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    print(json.dumps({"test": "A2-K9.1 immutable script manifest", "files": files,
                      "execution_verdict": "PASS_MANIFEST_COMPLETE",
                      "runtime_limit_seconds": 5.0,
                      "runtime_seconds": time.monotonic()-started}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

