#!/usr/bin/env python
"""Bounded SHA-256 manifest for BR3B-2e scripts 104--108."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time


FILES = [
    "104_script_A2_K4_3b_RG_BR3B2e1_earliest_relative_radiation_modes.py",
    "105_script_A2_K4_3b_RG_BR3B2e2_NIV_shear_CAMB_constraint_crosscheck.py",
    "106_script_A2_K4_3b_RG_BR3B2e2_NIV_shear_CAMB_precompiled_crosscheck.py",
    "107_script_A2_K4_3b_RG_BR3B2e2_NID_NIV_shear_sector_solution.py",
    "108_script_A2_K4_3b_RG_BR3B2e2_NID_NIV_shear_sector_solution_bounded.py",
]


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--max-runtime-seconds",type=float,default=8.)
    a=ap.parse_args()
    if not 0<a.max_runtime_seconds<=10: ap.error("runtime must be in (0,10]")
    t0=time.monotonic(); here=Path(__file__).resolve().parent; rows=[]
    for name in FILES:
        if time.monotonic()-t0>a.max_runtime_seconds: raise TimeoutError("manifest deadline")
        data=(here/name).read_bytes(); rows.append({"file":name,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()})
    print(json.dumps({"test":"BR3B-2e scripts 104-108 SHA-256 manifest","entries":rows,
      "execution_verdict":"PASS_MANIFEST_CREATED","runtime_limit_seconds":a.max_runtime_seconds,
      "runtime_seconds":time.monotonic()-t0},indent=2,sort_keys=True)); return 0


if __name__=="__main__":
    try: raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)})); raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)})); raise SystemExit(2)
