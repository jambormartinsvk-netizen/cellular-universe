#!/usr/bin/env python
"""Bounded SHA-256 manifest for BR3B scripts 97--102."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time


FILES = [
    "97_script_A2_K4_3b_RG_BR3B1_induced_coefficient_rank_gate.py",
    "98_script_A2_K4_3b_RG_BR3B2a_background_dressing_compatibility.py",
    "99_script_A2_K4_3b_RG_BR3B2b_full_source_Bianchi_ledger.py",
    "100_script_A2_K4_3b_RG_BR3B2c_physical_hx_sector.py",
    "101_script_A2_K4_3b_RG_BR3B2d_NID_NIV_power_ordering.py",
    "102_script_A2_K4_3b_RG_BR3B2d_NID_NIV_power_ordering_fixed.py",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 10.0:
        parser.error("runtime must be in (0, 10]")
    started = time.monotonic()
    here = Path(__file__).resolve().parent
    entries = []
    for name in FILES:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("manifest deadline exceeded")
        data = (here / name).read_bytes()
        entries.append({"file": name, "bytes": len(data),
                        "sha256": hashlib.sha256(data).hexdigest()})
    print(json.dumps({
        "test": "A2-K4.3b-RG-BR3B scripts 97-102 SHA-256 manifest",
        "entries": entries,
        "execution_verdict": "PASS_MANIFEST_CREATED",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }, indent=2, sort_keys=True))
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
