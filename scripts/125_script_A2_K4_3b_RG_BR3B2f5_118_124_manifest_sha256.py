#!/usr/bin/env python
"""Bounded SHA-256 manifest for BR3B-2f-5 scripts 118--124."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time


FILES = [
    "118_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py",
    "119_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py",
    "120_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py",
    "121_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py",
    "122_script_A2_K4_3b_RG_BR3B2f5_zero_matter_reference_diagnostic.py",
    "123_script_A2_K4_3b_RG_BR3B2f5_script108_source_difference_audit.py",
    "124_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain_audited.py",
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
        "test": "A2-K4.3b-RG BR3B-2f-5 scripts 118-124 manifest",
        "files": rows,
        "checks": {
            "all_seven_files_present": len(rows) == 7,
            "all_hashes_unique": len({row["sha256"] for row in rows}) == 7,
        },
        "artifact_status": {
            "118": "SYNTAX_ERROR_UNCLOSED_PRESERVED",
            "119": "SYNTAX_ERROR_UNCLOSED_PRESERVED",
            "120": "JSON_SERIALIZATION_ERROR_UNCLOSED_PRESERVED",
            "121": "REVIEW_LEGACY_ORACLE_ERROR_LOCALIZED",
            "122": "PASS_DIAGNOSTIC_STANDARD_COEFFICIENTS_EXPOSED",
            "123": "PASS_DIFFERENCE_LOCALIZED_TO_NU_SHEAR",
            "124": "PASS_FULL_MIXED_CHAIN_THROUGH_COMMON_FUEL",
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
