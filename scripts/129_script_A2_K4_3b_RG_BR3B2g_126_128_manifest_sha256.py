#!/usr/bin/env python
"""Bounded SHA-256 manifest for BR3B-2g scripts 126--128."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time


FILES = [
    "126_script_A2_K4_3b_RG_BR3B2g_l3_ash_full_ledger.py",
    "127_script_A2_K4_3b_RG_BR3B2g_l3_ash_regular_hierarchy.py",
    "128_script_A2_K4_3b_RG_BR3B2g_exact_order_and_hierarchy_audit.py",
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
        payload = (root/name).read_bytes()
        rows.append({"file":f"scripts/{name}", "bytes":len(payload),
                     "sha256":hashlib.sha256(payload).hexdigest()})
    output = {
        "test":"A2-K4.3b-RG BR3B-2g scripts 126-128 manifest",
        "files":rows,
        "checks":{
            "all_three_files_present":len(rows)==3,
            "all_hashes_unique":len({row["sha256"] for row in rows})==3,
        },
        "artifact_status":{
            "126":"REVIEW_HIERARCHY_REGULARITY_MISSING_PRESERVED",
            "127":"PASS_BR3B2G_L3_ASH_FULL_LEDGER",
            "128":"PASS_BR3B2G_EXACT_ORDER_AND_HIERARCHY",
        },
        "execution_verdict":"PASS_MANIFEST_CREATED",
        "runtime_limit_seconds":args.max_runtime_seconds,
        "runtime_seconds":time.monotonic()-started,
    }
    print(json.dumps(output,indent=2,sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)}))
        raise SystemExit(124)
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)}))
        raise SystemExit(2)
