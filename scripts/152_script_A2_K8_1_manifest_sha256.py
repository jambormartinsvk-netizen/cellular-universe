#!/usr/bin/env python
"""Bounded SHA-256 manifest for A2-K8.1 scripts 150 and 151."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import time


def main() -> None:
    started = time.monotonic()
    root = Path(__file__).resolve().parent
    names = (
        "150_script_A2_K8_1_number_source_covariant_moment_ledger.py",
        "151_script_A2_K8_1_independent_frame_mapping_audit.py",
    )
    files = {}
    for name in names:
        if time.monotonic()-started > 5.0:
            raise TimeoutError("K8.1 manifest deadline exceeded")
        data = (root/name).read_bytes()
        files[name] = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    print(json.dumps({
        "test": "A2-K8.1 immutable script manifest",
        "files": files,
        "execution_verdict": "PASS_MANIFEST_COMPLETE",
        "runtime_limit_seconds": 5.0,
        "runtime_seconds": time.monotonic()-started,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

