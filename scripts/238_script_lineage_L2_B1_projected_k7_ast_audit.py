#!/usr/bin/env python
"""Bounded AST/source audit of the projected K7 descendant set; no imports/ODE."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import time


ROOT = Path(__file__).resolve().parent.parent
TARGETS = (
    "179_script_A2_K4_C7_7c_K7c3_NID_deep_short_projected_ODE.py",
    "181_script_A2_K4_C7_7c_K7c3a_exact_linear_operator_profile.py",
    "182_script_A2_K4_C7_7c_K7c3a1_normalized_basis_operator_profile.py",
    "183_script_A2_K4_C7_7c_K7c3b_fixed_RK4_step_convergence.py",
    "197_script_A2_K4_C7_7c_K7c_P1_clean_standalone_RK4.py",
    "203_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4.py",
    "204_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4_complete.py",
    "205_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4_audited.py",
    "206_script_A2_K4_C7_7c_K7c_P3b_source_delta_audit.py",
    "207_script_A2_K4_C7_7c_K7c_P3b_source_delta_audit_tuple_fixed.py",
    "209_script_A2_K4_C7_7c_K7c_P4a_single_case_solver.py",
    "210_script_A2_K4_C7_7c_K7c_P4a_source_delta_audit.py",
    "213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py",
    "214_script_A2_K4_C7_7c_K7d_integrated_preflight_and_source_audit.py",
    "215_script_A2_K4_C7_7c_K7d_V1_offline_diagnostic_correction.py",
    "216_script_A2_K4_C7_7c_K7d_V2_HP_parity_shear_correction.py",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def write_once(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable output: {path}")
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def defined_functions(tree: ast.AST) -> set[str]:
    return {node.name for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}


def main() -> int:
    args = parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0, 5]")
    started = time.monotonic()
    rows: dict[str, object] = {}
    any_definer = False
    all_definers_limited = True
    for filename in TARGETS:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("L2-B1 internal deadline exceeded")
        path = ROOT / "scripts" / filename
        text = path.read_text(encoding="utf-8")
        tree = ast.parse(text, filename=str(path))
        functions = defined_functions(tree)
        defines_rhs = "physical_rhs" in functions
        has_uc_identifier = re.search(r"(?<![A-Za-z0-9_])u_?c(?![A-Za-z0-9_])", text, flags=re.IGNORECASE) is not None
        fixed_k_background = bool(re.search(r"\bk_mpc\s*=\s*0\.05\b|\bK_MPC\s*=\s*0\.05\b", text))
        mentions_rhs = "physical_rhs" in text
        if defines_rhs:
            status = "DEFINES_LIMITED_RHS" if not has_uc_identifier else "DEFINES_STATE_REQUIRING_MANUAL_REVIEW"
            any_definer = True
            all_definers_limited = all_definers_limited and not has_uc_identifier
        elif mentions_rhs:
            status = "CHECKER_OF_LIMITED_RHS"
        else:
            status = "HISTORICAL_RESULT_OR_LINEAGE_HELPER"
        rows[filename] = {
            "defines_physical_rhs": defines_rhs,
            "mentions_physical_rhs": mentions_rhs,
            "has_Uc_identifier": has_uc_identifier,
            "has_fixed_K_MPC_background_assignment": fixed_k_background,
            "classification": status,
        }
    checks = {
        "all_16_targets_parsed": len(rows) == len(TARGETS),
        "at_least_one_rhs_definer": any_definer,
        "all_rhs_definers_lack_Uc_as_expected": all_definers_limited,
        "known_fixed_K_background_definers_present": all(bool(rows[name]["has_fixed_K_MPC_background_assignment"]) for name in (
            "197_script_A2_K4_C7_7c_K7c_P1_clean_standalone_RK4.py",
            "209_script_A2_K4_C7_7c_K7c_P4a_single_case_solver.py",
            "213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py",
        )),
    }
    payload = {
        "test": "LINEAGE-L2-B1 projected K7 AST/state audit",
        "scope": "source AST/text only; no imports, ODE, score, or file rewrite",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "targets": rows,
        "verdict": "PASS_L2_B1_PROJECTED_K7_CLASSIFIED" if all(checks.values()) else "STOP_L2_B1_PROJECTED_K7_MAP_UNCLOSED",
    }
    write_once(args.output, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
