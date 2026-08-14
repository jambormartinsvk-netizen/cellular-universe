#!/usr/bin/env python
"""Bounded SHA-256 manifest for BR3B-2f scripts 110--116."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time


FILES = [
    "110_script_A2_K4_3b_RG_BR3B2f_CAMB_mode_coefficients_in_a.py",
    "111_script_A2_K4_3b_RG_BR3B2f2_NID_NIV_baryon_fraction_difference.py",
    "112_script_A2_K4_3b_RG_BR3B2f3_exact_Frobenius_standard_NID_NIV.py",
    "113_script_A2_K4_3b_RG_BR3B2f3_Frobenius_bounded_coefficients.py",
    "114_script_A2_K4_3b_RG_BR3B2f3_Frobenius_null_direction_audit.py",
    "115_script_A2_K4_3b_RG_BR3B2f3_Frobenius_null_direction_audit_fixed.py",
    "116_script_A2_K4_3b_RG_BR3B2f4_missing_matter_dressed_sector_audit.py",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 10.0:
        parser.error("runtime must be in (0,10]")
    started = time.monotonic()
    root = Path(__file__).resolve().parent
    rows = []
    for name in FILES:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("manifest deadline exceeded")
        path = root / name
        payload = path.read_bytes()
        rows.append({"file": f"scripts/{name}", "bytes": len(payload),
                     "sha256": hashlib.sha256(payload).hexdigest()})
    output = {
        "test": "A2-K4.3b-RG BR3B-2f scripts 110-116 manifest",
        "files": rows,
        "checks": {"all_seven_files_present": len(rows) == 7,
                   "all_hashes_unique": len({row["sha256"] for row in rows}) == 7},
        "artifact_status": {
            "110": "REVIEW_UNCLOSED",
            "111": "REVIEW_UNCLOSED",
            "112": "EXTERNAL_TIMEOUT_UNCLOSED",
            "113": "REVIEW_UNCLOSED",
            "114": "NOT_EXECUTED_DUPLICATE_PRESERVED",
            "115": "PASS",
            "116": "PASS",
        },
        "execution_verdict": "PASS_MANIFEST_CREATED",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)
