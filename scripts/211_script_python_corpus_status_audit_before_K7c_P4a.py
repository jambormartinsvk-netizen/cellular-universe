#!/usr/bin/env python3
"""Bounded, non-executing corpus and target audit before P4a physics."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SELF = Path(__file__).name
DEFAULT_OUTPUT = ROOT / "Audit" / "A2_K4_K7C_P4A_CORPUS_CHECKER_211_2026-07-15.json"
EXPECTED_CORPUS_EXCLUDING_SELF = 216
EXPECTED_SYNTAX_FAILURES = {
    "118_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py",
    "119_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py",
}
EXPECTED_TARGET_HASHES = {
    "205_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4_audited.py":
        "B7EC8BAD3BFB0D48EC91D6F1BB0A602FA1834A021BB94C92D6D1B398D5F3CDC2",
    "209_script_A2_K4_C7_7c_K7c_P4a_single_case_solver.py":
        "67E5B3C1B7C942242E4FEB4458A4CC81A52F6417E25D50A6E2009023F321A612",
    "210_script_A2_K4_C7_7c_K7c_P4a_source_delta_audit.py":
        "D86022C8D8D5C32223ECD9F62097AEE09A6685C8358F8A1D1B0D691C897F662D",
    "212_script_A2_K4_C7_7c_K7c_P4a_offline_aggregate.py":
        "486ECEFB15A63401BDDD8D6DA045480FFD7A2A94E6F7CA67D0013A402CEE84AF",
}
FAIL_OPEN = re.compile(r"\.get\([^\n]+?\)\s*==\s*[A-Za-z_][A-Za-z0-9_]*\.get\(")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def has_entrypoint(tree: ast.Module) -> bool:
    return any(
        isinstance(node, ast.If)
        and "__name__" in ast.dump(node.test, include_attributes=False)
        and "__main__" in ast.dump(node.test, include_attributes=False)
        for node in tree.body
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="P4a non-executing corpus audit")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-runtime-seconds", type=float, default=15.0)
    args = parser.parse_args()
    if not 5 <= args.max_runtime_seconds <= 15:
        parser.error("max-runtime-seconds must be in [5,15]")
    output_path = args.output.resolve()
    if output_path.exists():
        raise FileExistsError(f"refusing to overwrite output: {output_path}")
    if not output_path.parent.is_dir():
        raise FileNotFoundError(f"output parent missing: {output_path.parent}")
    started = time.monotonic()

    paths = sorted(path for path in HERE.glob("*.py") if path.name != SELF)
    syntax_errors: list[str] = []
    target_records: dict[str, dict[str, object]] = {}
    for index, path in enumerate(paths):
        if index % 16 == 0 and time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P4a corpus audit deadline exceeded")
        text = path.read_text(encoding="utf-8")
        try:
            tree = ast.parse(text, filename=str(path))
            compile(tree, str(path), "exec")
        except SyntaxError:
            syntax_errors.append(path.name)
            continue
        if path.name in EXPECTED_TARGET_HASHES:
            target_records[path.name] = {
                "sha256": sha256_file(path),
                "entrypoint": has_entrypoint(tree),
                "fail_open_get_equality_absent": FAIL_OPEN.search(text) is None,
                "max_runtime_argument_present": "--max-runtime-seconds" in text,
                "immutable_output_mode_present": 'open("x"' in text,
            }

    target_checks: dict[str, bool] = {}
    for filename, expected_hash in EXPECTED_TARGET_HASHES.items():
        record = target_records.get(filename)
        target_checks[filename + ":present"] = record is not None
        if record is None:
            continue
        target_checks[filename + ":hash_exact"] = record["sha256"] == expected_hash
        target_checks[filename + ":entrypoint"] = record["entrypoint"] is True
        target_checks[filename + ":no_fail_open_get_equality"] = (
            record["fail_open_get_equality_absent"] is True
        )
        target_checks[filename + ":runtime_argument"] = (
            record["max_runtime_argument_present"] is True
        )
        target_checks[filename + ":immutable_output"] = (
            record["immutable_output_mode_present"] is True
        )

    runner_text = (
        HERE / "209_script_A2_K4_C7_7c_K7c_P4a_single_case_solver.py"
    ).read_text(encoding="utf-8")
    source_audit_text = (
        HERE / "210_script_A2_K4_C7_7c_K7c_P4a_source_delta_audit.py"
    ).read_text(encoding="utf-8")
    aggregate_text = (
        HERE / "212_script_A2_K4_C7_7c_K7c_P4a_offline_aggregate.py"
    ).read_text(encoding="utf-8")
    special_checks = {
        "runner_has_three_exact_case_ids": all(
            name in runner_text
            for name in ("DOP853_MEDIUM", "DOP853_TIGHT", "RADAU_TIGHT")
        ),
        "runner_has_solve_ivp": "solve_ivp" in runner_text,
        "runner_has_internal_deadline": "def deadline()" in runner_text,
        "runner_has_rhs_cap_100000": "rhs_calls > 100000" in runner_text,
        "source_audit_declares_no_target_execution": (
            '"target_executed": False' in source_audit_text
            and '"physics_executed": False' in source_audit_text
        ),
        "aggregate_has_no_subprocess": "subprocess" not in aggregate_text,
        "aggregate_has_no_solve_ivp": "solve_ivp" not in aggregate_text,
        "aggregate_uses_threshold_1e8": "LIMIT = 1e-8" in aggregate_text,
    }
    special_checks = {key: bool(value) for key, value in special_checks.items()}
    checks = {
        "corpus_count_excluding_checker_is_216": len(paths)
            == EXPECTED_CORPUS_EXCLUDING_SELF,
        "expected_syntax_failures_only": set(syntax_errors)
            == EXPECTED_SYNTAX_FAILURES,
        "all_target_checks_pass": bool(target_checks) and all(target_checks.values()),
        "all_special_checks_pass": all(special_checks.values()),
        "no_target_script_executed": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    passed = all(checks.values())
    payload = {
        "test": "bounded corpus status audit before K7c P4a",
        "execution_verdict": (
            "PASS_P4A_SCRIPT_CORPUS_INVENTORY"
            if passed else "REVIEW_P4A_SCRIPT_CORPUS_INVENTORY"
        ),
        "physics_executed": False,
        "target_executed": False,
        "corpus_count_excluding_checker": len(paths),
        "syntax_errors": syntax_errors,
        "target_records": target_records,
        "target_checks": target_checks,
        "special_checks": special_checks,
        "checks": checks,
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "scope_limit": "source/AST compilation only; no target import or execution",
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True)
    with output_path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(encoded + "\n")
    print(encoded)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

