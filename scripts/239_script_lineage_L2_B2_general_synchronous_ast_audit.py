#!/usr/bin/env python
"""Bounded source audit of general-synchronous/BR/P5 lineage; no imports or ODE."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import time


ROOT = Path(__file__).resolve().parent.parent
TARGETS = {
    "66_script_A2_K4_1_complete_regular_mode_basis.py": "STANDARD_NULL_BASELINE",
    "85_script_A2_K4_3b_RG_collective_K4_test_field_Puiseux_response.py": "TEST_FIELD_ONLY",
    "86_script_A2_K4_3b_RG_general_synchronous_K4_test_field_response.py": "TEST_FIELD_ONLY",
    "89_script_A2_K4_3b_RG_BR2_backreacted_superhorizon_evolution.py": "FULL_EARLY_SYSTEM_CANDIDATE",
    "90_script_A2_K4_3b_RG_BR2_conditioned_DAE_constraint_audit.py": "FULL_EARLY_SYSTEM_CANDIDATE",
    "92_script_A2_K4_3b_RG_BR2_Omega_conditioned_DAE_json_fixed_alias.py": "WRAPPER_ONLY",
    "94_script_A2_K4_3b_RG_BR2_velocity_roundoff_condition_gate_json_alias.py": "WRAPPER_ONLY",
    "95_script_A2_K4_3b_RG_BR3A_mode_resolved_Puiseux_sources.py": "TEST_FIELD_ONLY",
    "130_script_A2_K4_3b_RG_BR3C_a_two_surface_state_export.py": "SEED_SCOPE_ONLY",
    "136_script_A2_K4_3b_RG_BR3C_b_segmented_early_evolution.py": "REDUCED_K7_DESCENDANT",
    "140_script_A2_K4_3b_RG_BR3C_c_species_mode_activity_audit.py": "CHECKER_OF_REDUCED_STATE",
    "143_script_A2_K4_3b_RG_C7_7c_K2_normalized_activity_audit.py": "CHECKER_OF_REDUCED_STATE",
    "148_script_A2_K4_3b_RG_C7_7c_K4_analytic_envelope_activity_audit.py": "CHECKER_OF_REDUCED_STATE",
    "155_script_A2_K4_C7_7c_initial_rhs_condition_map.py": "REDUCED_K7_DIAGNOSTIC",
    "236_script_KMPC_003_P5_1_general_synchronous_static_ledger.py": "P5_STATIC_CONTRACT",
}


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


def has_word(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE) is not None


def main() -> int:
    args = parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0, 5]")
    started = time.monotonic()
    rows: dict[str, object] = {}
    for filename, expected in TARGETS.items():
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("L2-B2 internal deadline exceeded")
        path = ROOT / "scripts" / filename
        text = path.read_text(encoding="utf-8")
        tree = ast.parse(text, filename=str(path))
        functions = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
        rows[filename] = {
            "expected_classification": expected,
            "defines_rhs": "rhs" in functions or "rhs_flat" in functions,
            "has_Uc_semantics": has_word(text, r"(?<![A-Za-z0-9_])u_?c(?![A-Za-z0-9_])|\bUC\b"),
            "has_Ud_semantics": has_word(text, r"(?<![A-Za-z0-9_])u_?d(?![A-Za-z0-9_])"),
            "mentions_constraint": "constraint" in text.lower(),
            "fixed_metric_scope": "fixed standard metric" in text.lower() or "fixed metric" in text.lower(),
            "backreaction_excluded": (
                "no back-reacted" in text.lower()
                or "not induced metric" in text.lower()
                or "cannot close g7" in text.lower()
            ),
            "has_fixed_k_mpc_assignment": has_word(text, r"\bk_mpc\s*=\s*0\.05\b|\bK_MPC\s*=\s*0\.05\b"),
            "is_runpy_wrapper": "runpy.run_path" in text,
            "p5_full_state_contract": all(item in text for item in ("U_c", "U_b", "M_full")),
        }
    checks = {
        "all_targets_parsed": len(rows) == len(TARGETS),
        "full_candidates_carry_Uc_Ud_and_constraints": all(
            bool(rows[name]["has_Uc_semantics"]) and bool(rows[name]["has_Ud_semantics"]) and bool(rows[name]["mentions_constraint"])
            for name in ("89_script_A2_K4_3b_RG_BR2_backreacted_superhorizon_evolution.py", "90_script_A2_K4_3b_RG_BR2_conditioned_DAE_constraint_audit.py")
        ),
        "standard_null_baseline_is_not_mislabelled_full_energy_frame": (
            bool(rows["66_script_A2_K4_1_complete_regular_mode_basis.py"]["has_Uc_semantics"])
            and bool(rows["66_script_A2_K4_1_complete_regular_mode_basis.py"]["mentions_constraint"])
            and not bool(rows["66_script_A2_K4_1_complete_regular_mode_basis.py"]["has_Ud_semantics"])
        ),
        "test_fields_declare_limited_metric_scope": all(
            bool(rows[name]["has_Uc_semantics"]) and (bool(rows[name]["fixed_metric_scope"]) or bool(rows[name]["backreaction_excluded"]))
            for name in ("85_script_A2_K4_3b_RG_collective_K4_test_field_Puiseux_response.py", "86_script_A2_K4_3b_RG_general_synchronous_K4_test_field_response.py", "95_script_A2_K4_3b_RG_BR3A_mode_resolved_Puiseux_sources.py")
        ),
        "wrappers_are_not_misclassified_as_rhs": all(
            bool(rows[name]["is_runpy_wrapper"]) and not bool(rows[name]["defines_rhs"])
            for name in ("92_script_A2_K4_3b_RG_BR2_Omega_conditioned_DAE_json_fixed_alias.py", "94_script_A2_K4_3b_RG_BR2_velocity_roundoff_condition_gate_json_alias.py")
        ),
        "reduced_descendants_keep_old_fixed_k_marker": all(
            bool(rows[name]["has_fixed_k_mpc_assignment"])
            for name in ("136_script_A2_K4_3b_RG_BR3C_b_segmented_early_evolution.py", "155_script_A2_K4_C7_7c_initial_rhs_condition_map.py")
        ),
        "p5_static_contract_explicit": bool(rows["236_script_KMPC_003_P5_1_general_synchronous_static_ledger.py"]["p5_full_state_contract"]),
    }
    payload = {
        "test": "LINEAGE-L2-B2 general-synchronous/BR/P5 source-contract audit",
        "scope": "AST/text only; no imports, ODE, score, or source rewrite",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "targets": rows,
        "verdict": "PASS_L2_B2_LINEAGE_MAP" if all(checks.values()) else "STOP_L2_B2_LINEAGE_MAP_UNCLOSED",
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
