#!/usr/bin/env python
"""Bounded source audit of P5 seed provenance; no imports or ODE."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parent.parent
FILES = {
    "84": "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py",
    "86": "86_script_A2_K4_3b_RG_general_synchronous_K4_test_field_response.py",
    "89": "89_script_A2_K4_3b_RG_BR2_backreacted_superhorizon_evolution.py",
    "90": "90_script_A2_K4_3b_RG_BR2_conditioned_DAE_constraint_audit.py",
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--max-runtime-seconds", type=float, default=5.0)
    p.add_argument("--output", type=Path, required=True)
    return p.parse_args()


def write_once(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable output: {path}")
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def function_text(text: str, name: str) -> str:
    tree = ast.parse(text)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return ast.get_source_segment(text, node) or ""
    return ""


def main() -> int:
    args = parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0, 5]")
    started = time.monotonic()
    text: dict[str, str] = {}
    for key, filename in FILES.items():
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.3a internal deadline exceeded")
        value = (ROOT / "scripts" / filename).read_text(encoding="utf-8")
        ast.parse(value, filename=filename)
        text[key] = value
    initial89 = function_text(text["89"], "initial")
    initial90 = function_text(text["90"], "initial")
    initial86 = function_text(text["86"], "integrate")
    rows = {
        "84": {"declares_gamma_zero_seed_scope": "Gamma=0 regular synchronous/CDM-frame seed coefficients" in text["84"]},
        "89": {
            "imports_standard_class_seed": "S84.class_seed" in initial89,
            "initializes_zero_vector": "np.zeros(SIZE" in initial89,
            "does_not_assign_UC_for_standard_modes": "z[UC]" not in initial89,
            "does_not_assign_UF_for_standard_modes": "z[UF]" not in initial89,
            "does_not_assign_DF_for_standard_modes": "z[DF]" not in initial89,
        },
        "90": {
            "imports_standard_class_seed": "S84.class_seed" in initial90,
            "initializes_zero_vector": "np.zeros(SIZE" in initial90,
            "does_not_assign_UC_for_standard_modes": "z[UC]" not in initial90,
            "does_not_assign_UF_for_standard_modes": "z[UF]" not in initial90,
            "does_not_assign_DF_for_standard_modes": "z[DF]" not in initial90,
        },
        "86": {
            "fixed_metric_scope_declared": "fixed standard metric" in text["86"],
            "test_field_starts_new_dark_variables_at_zero": "0.0, 0.0, 0.0" in initial86,
        },
    }
    checks = {f"{group}_{name}": bool(value) for group, values in rows.items() for name, value in values.items()}
    payload = {
        "test": "KMPC-005 P5.3a full-seed provenance audit",
        "scope": "source provenance only; no ODE, no regularity proof, no score",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "findings": rows,
        "physical_verdict": "P5.3_SEED_REGULARITY_UNCLOSED_STANDARD_GAMMA0_EXTENSION_IDENTIFIED",
        "next_step": "derive exact-A1 Puiseux/Frobenius coefficients before P5.4",
        "verdict": "PASS_P5_3A_PROVENANCE_GAP_MAPPED" if all(checks.values()) else "STOP_P5_3A_PROVENANCE_MAP_UNCLOSED",
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
