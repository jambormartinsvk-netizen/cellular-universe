#!/usr/bin/env python3
"""Fail-closed no-ODE preflight for K7d runner 213."""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import py_compile
import sys
import time

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TARGET = HERE / "213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py"
SOURCE209 = HERE / "209_script_A2_K4_C7_7c_K7c_P4a_single_case_solver.py"
LEDGER = HERE / "00_PYTHON_FORMAL_ERROR_LEDGER.md"
PREREG = ROOT / "Questions" / (
    "A2_K4_C7_7C_K7D_G4_G6_G7_INTEGRATED_PREREGISTRATION_2026-07-15.md"
)
EXPECTED_SOURCE209_SHA256 = (
    "67E5B3C1B7C942242E4FEB4458A4CC81A52F6417E25D50A6E2009023F321A612"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def load_target():
    spec = importlib.util.spec_from_file_location("k7d_runner_213", TARGET)
    if spec is None or spec.loader is None:
        raise ImportError(TARGET)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser(description="K7d runner 213 formal/source preflight")
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    if not 2 <= args.max_runtime_seconds <= 10:
        parser.error("max-runtime-seconds must be in [2,10]")
    started = time.monotonic()
    py_compile.compile(str(TARGET), doraise=True)
    source = TARGET.read_text(encoding="utf-8")
    ledger = LEDGER.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(TARGET))
    subprocess_calls = []
    solve_calls = []
    immutable_open = False
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if isinstance(node.func, ast.Attribute) and node.func.attr == "run":
            subprocess_calls.append(node)
        if isinstance(node.func, ast.Name) and node.func.id == "solve_ivp":
            solve_calls.append(node)
        if isinstance(node.func, ast.Attribute) and node.func.attr == "open":
            immutable_open = immutable_open or bool(
                node.args and isinstance(node.args[0], ast.Constant)
                and node.args[0].value == "x"
            )
    target = load_target()
    checks: dict[str, bool] = {
        "target_py_compile": True,
        "source_209_hash_exact": sha256_file(SOURCE209) == EXPECTED_SOURCE209_SHA256,
        "error_ledger_present_nonempty": len(ledger) > 1000,
        "preregistration_present_nonempty": PREREG.is_file() and PREREG.stat().st_size > 1000,
        "all_subprocess_calls_have_timeout": bool(subprocess_calls) and all(
            any(keyword.arg == "timeout" for keyword in call.keywords)
            for call in subprocess_calls
        ),
        "exactly_one_solve_ivp_call": len(solve_calls) == 1,
        "immutable_x_mode_present": immutable_open,
        "no_np_interp": "np.interp" not in source,
        "no_generated_source_patch": ".replace(" not in source and "compile(" not in source,
        "internal_deadline_present": "single-case internal deadline exceeded" in source,
        "rhs_and_safety_caps_present": (
            "RHS call cap exceeded" in source and "normalized safety cap exceeded" in source
        ),
        "candidate_never_immediate_stop": (
            "CONFIRMATION_REQUIRED" in source and "STOP_K7D" not in source
        ),
        "state_names_exact": tuple(target.NAMES) == (
            "h", "eta", "delta_gamma", "D", "delta_b", "delta_c",
            "U_gamma", "M", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
        ),
        "case_matrix_exact": set(target.CASES) == {
            "NID_DEEP", "NID_SHALLOW", "NIV_DEEP", "NIV_SHALLOW",
        },
        "thresholds_exact": bool(
            target.RTOL == 1e-11 and target.ATOL == 1e-13
            and target.MAX_STEP == 0.05 and target.PARITY_MAX == 1e-10
            and target.CONSTRAINT_ABS == 1e-12 and target.CONSTRAINT_REL == 1e-8
            and target.ENDPOINT_L2_MAX == 3e-3
            and target.ENDPOINT_ENVELOPE_MAX == 1e-2
            and target.OVERLAP_ENVELOPE_MAX == 2e-2
        ),
    }
    points = (-25.0,) if args.smoke else (-25.0, -23.0, -18.0)
    max_zero = 0.0
    max_basis_parity = 0.0
    max_roundtrip = 0.0
    eye = np.eye(13, dtype=float)
    for x in points:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("K7d preflight deadline exceeded")
        max_zero = max(max_zero, float(np.max(np.abs(target.physical_rhs(x, np.zeros(13))))))
        probes = eye if not args.smoke else eye[:2]
        for probe in probes:
            projected_rhs = target.physical_rhs(x, probe)
            _, species_projected = target.species_rhs_and_projected_derivative(x, probe)
            scale = np.maximum(np.maximum(np.abs(projected_rhs), np.abs(species_projected)), 1.0)
            max_basis_parity = max(
                max_basis_parity,
                float(np.max(np.abs(projected_rhs - species_projected) / scale)),
            )
        probe = np.linspace(-0.7, 0.9, 13, dtype=float)
        species = target.projected_to_species(x, probe)
        recovered = target.projected_from_species(
            x, dict(zip(target.SPECIES_NAMES, map(float, species)))
        )
        max_roundtrip = max(
            max_roundtrip,
            float(np.max(np.abs(recovered - probe) / np.maximum(np.abs(probe), 1.0))),
        )
    checks["zero_rhs_below_1e-15"] = max_zero <= 1e-15
    checks["species_projected_basis_parity_below_1e-10"] = max_basis_parity <= 1e-10
    checks["projected_species_roundtrip_below_1e-14"] = max_roundtrip <= 1e-14
    checks = {key: bool(value) for key, value in checks.items()}
    passed = bool(checks) and all(checks.values())
    payload = {
        "test": "SCI-A2K4-C7G467-K7D-INTEGRATED-PREFLIGHT-SOURCE-AUDIT",
        "execution_verdict": (
            "PASS_K7D_PREFLIGHT_SOURCE_AUDIT"
            if passed else "REVIEW_K7D_PREFLIGHT_SOURCE_AUDIT"
        ),
        "physics_executed": False,
        "smoke": bool(args.smoke),
        "checks": checks,
        "metrics": {
            "max_zero_rhs": max_zero,
            "max_species_projected_basis_parity": max_basis_parity,
            "max_projected_species_roundtrip_scaled": max_roundtrip,
        },
        "hashes": {
            "self_214_sha256": sha256_file(Path(__file__)),
            "target_213_sha256": sha256_file(TARGET),
            "source_209_sha256": sha256_file(SOURCE209),
            "error_ledger_sha256": sha256_file(LEDGER),
            "preregistration_sha256": sha256_file(PREREG),
        },
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if passed else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}, indent=2))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}, indent=2))
        raise SystemExit(1)

