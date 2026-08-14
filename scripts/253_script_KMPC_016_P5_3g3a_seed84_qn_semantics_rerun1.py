#!/usr/bin/env python
"""Bounded rerun: check the returned, not auxiliary, seed84 qn variable."""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "scripts" / "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py"


def load_module():
    spec = importlib.util.spec_from_file_location("p53g3a_rerun1_seed84", SOURCE)
    if spec is None or spec.loader is None:
        raise ImportError(SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0,5]")
    started = time.monotonic()
    source = SOURCE.read_text(encoding="utf-8")
    ast.parse(source, filename=SOURCE.name)
    module = load_module()
    y = 2.0e-4
    k1, k2 = 0.05, 0.10
    first = module.class_seed("initial_iso_neutrino_vel", k1, y / k1, 0.41, 0.59, 0.16, 0.84, 0.01)
    second = module.class_seed("initial_iso_neutrino_vel", k2, y / k2, 0.41, 0.59, 0.16, 0.84, 0.01)
    ratio = float(second[5] / first[5])
    checks = {
        "source_return_explicitly_converts_tn_to_qn": "qn = 4.0 * tn / (3.0 * k)" in source,
        "source_return_places_qn_at_index_5": "return np.array([dg, db, dc, dn, qg, qn, eta_s]" in source,
        "NIV_returned_qn_is_invariant_at_fixed_y": abs(ratio - 1.0) < 1.0e-12,
    }
    passed = all(checks.values())
    payload = {
        "test": "KMPC-016 P5.3g3a RERUN1 returned seed84 qn semantics",
        "scope": "NIV returned-qn convention only; leading-radiation semantic check, no eta exact-invariance claim, no ODE, no score",
        "source84_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "fixed_y": y,
        "k_values": [k1, k2],
        "returned_qn_values": [float(first[5]), float(second[5])],
        "ratio": ratio,
        "next_step": "rerun the l=2 candidate derivation with qn, not tn" if passed else "restrict P5.3g2 and inspect seed84 return convention",
        "verdict": "PASS_SCOPE_P5_3G3A_RETURNED_QN_SEMANTICS" if passed else "REVIEW_BLOCKED_P5_3G3A_RETURNED_QN_SEMANTICS",
    }
    if args.output.exists():
        raise FileExistsError(args.output)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if passed else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as error:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(error)}))
        raise SystemExit(124)
