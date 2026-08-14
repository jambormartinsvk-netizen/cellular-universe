#!/usr/bin/env python
"""Bounded SHA-256 manifest for the immutable C7.7c-K4 attempt."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import time


FILES = (
    "146_script_A2_K4_3b_RG_C7_7c_K4_analytic_reference_state.py",
    "147_script_A2_K4_3b_RG_C7_7c_K4_analytic_envelope_evolution.py",
    "148_script_A2_K4_3b_RG_C7_7c_K4_analytic_envelope_activity_audit.py",
)


def main() -> None:
    started = time.monotonic()
    root = Path(__file__).resolve().parent
    manifest = {}
    for name in FILES:
        if time.monotonic() - started > 5.0:
            raise TimeoutError("manifest internal deadline exceeded")
        data = (root/name).read_bytes()
        manifest[name] = {
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        }
    print(json.dumps({
        "test": "A2-K4 C7.7c-K4 immutable script manifest",
        "files": manifest,
        "execution_verdict": "PASS_MANIFEST_COMPLETE",
        "runtime_limit_seconds": 5.0,
        "runtime_seconds": time.monotonic()-started,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

