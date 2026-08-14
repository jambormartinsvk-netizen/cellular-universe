#!/usr/bin/env python
"""Bounded semantic consistency audit of script 84 velocity output."""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "scripts" / "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py"


def load_seed_module():
    spec = importlib.util.spec_from_file_location("p53g3a_seed84", SOURCE)
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
    if "q_i=4 theta_i/(3 k)" not in source:
        raise RuntimeError("seed84 qnu declaration not found")
    module = load_seed_module()
    y = 2.0e-4
    k_values = (0.05, 0.10)
    rows: dict[str, object] = {}
    for mode in module.MODES:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.3g3a internal deadline exceeded")
        values = []
        for k in k_values:
            tau = y / k
            values.append(module.class_seed(mode, k, tau, 0.41, 0.59, 0.16, 0.84, 0.01))
        first, second = values
        qnu_ratio = float(second[5] / first[5]) if abs(first[5]) > 1.0e-300 else None
        eta_difference = float(abs(second[6] - first[6]))
        rows[mode] = {
            "fixed_y": y,
            "k_values": list(k_values),
            "seed5_ratio_k2_over_k1": qnu_ratio,
            "eta_difference": eta_difference,
            "seed5_values": [float(first[5]), float(second[5])],
        }
    niv = rows["initial_iso_neutrino_vel"]
    checks = {
        "source84_declares_seed5_as_qnu": True,
        "NIV_eta_is_invariant_at_fixed_y": niv["eta_difference"] < 1.0e-18,
        "NIV_seed5_is_invariant_at_fixed_y": niv["seed5_ratio_k2_over_k1"] is not None and abs(niv["seed5_ratio_k2_over_k1"] - 1.0) < 1.0e-12,
    }
    consistent = all(checks.values())
    payload = {
        "test": "KMPC-015 P5.3g3a script 84 velocity semantic audit",
        "scope": "semantic/unit consistency of seed84 only; no ODE, no claim about CAMB itself, no score, no G8",
        "source84_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "mode_samples": rows,
        "next_step": "restore P5.3g2 and independently constraint-test F2" if consistent else "treat seed84 velocity semantics as unresolved; obtain canonical same-convention seed or explicit conversion",
        "verdict": "PASS_P5_3G3A_SEED84_QNU_SEMANTICS" if consistent else "REVIEW_BLOCKED_SEED84_VELOCITY_SEMANTICS_CONTRADICTION",
    }
    if args.output.exists():
        raise FileExistsError(args.output)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if consistent else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as error:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(error)}))
        raise SystemExit(124)
