#!/usr/bin/env python3
# DO_NOT_RUN_TECHNICAL: PF-031 did not support x_start/x_final tuple assignment.
"""Bounded AST-only source-delta audit for P3a-B scripts 197 and 205."""

from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import time
from typing import Any


HERE = Path(__file__).resolve().parent
BASE = HERE / "197_script_A2_K4_C7_7c_K7c_P1_clean_standalone_RK4.py"
CANDIDATE = HERE / "205_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4_audited.py"
DEFAULT_OUTPUT = (
    HERE.parent / "Audit" / "A2_K4_K7C_P3B_SOURCE_DELTA_206_2026-07-15.json"
)
EXPECTED_BASE_SHA256 = (
    "088B4CD58F57A30BD061D30042BA3E2CB5021DF9BF320003ED8291D86FB6C022"
)
EXPECTED_CANDIDATE_SHA256 = (
    "B7EC8BAD3BFB0D48EC91D6F1BB0A602FA1834A021BB94C92D6D1B398D5F3CDC2"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def ast_dump(node: ast.AST) -> str:
    return ast.dump(node, include_attributes=False)


def unique_function(tree: ast.AST, name: str) -> ast.FunctionDef:
    matches = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise RuntimeError(f"function {name!r} count changed: {len(matches)}")
    return matches[0]


def unique_assignment(tree: ast.AST, name: str) -> ast.AST:
    matches: list[ast.AST] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                matches.append(node.value)
    if len(matches) != 1:
        raise RuntimeError(f"assignment {name!r} count changed: {len(matches)}")
    return matches[0]


def unique_tuple_assignment(tree: ast.AST, first_name: str) -> ast.AST:
    matches: list[ast.AST] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Tuple) or not target.elts:
            continue
        first = target.elts[0]
        if isinstance(first, ast.Name) and first.id == first_name:
            matches.append(node.value)
    if len(matches) != 1:
        raise RuntimeError(
            f"tuple assignment {first_name!r} count changed: {len(matches)}"
        )
    return matches[0]


def return_components(function: ast.FunctionDef) -> list[ast.AST]:
    returns = [
        node for node in function.body if isinstance(node, ast.Return)
    ]
    if len(returns) != 1:
        raise RuntimeError(f"{function.name} return count changed")
    value = returns[0].value
    if not isinstance(value, ast.Call) or not value.args:
        raise RuntimeError("physical_rhs return is not the registered np.asarray call")
    first = value.args[0]
    if not isinstance(first, ast.List):
        raise RuntimeError("physical_rhs return first argument is not a list")
    return list(first.elts)


def pre_return_statements(function: ast.FunctionDef) -> list[str]:
    return [
        ast_dump(node) for node in function.body
        if not isinstance(node, ast.Return)
    ]


def flatten_additive(node: ast.AST, sign: int = 1) -> list[tuple[int, str]]:
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return flatten_additive(node.left, sign) + flatten_additive(node.right, sign)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Sub):
        return flatten_additive(node.left, sign) + flatten_additive(node.right, -sign)
    return [(sign, ast_dump(node))]


def counter_records(counter: Counter[tuple[int, str]]) -> list[dict[str, Any]]:
    rows = []
    for (sign, expression), count in sorted(counter.items()):
        rows.append({"sign": sign, "ast": expression, "count": count})
    return rows


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AST-only P3a-B source-delta audit")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--smoke", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.smoke:
        print(json.dumps({
            "smoke": True,
            "physics_executed": False,
            "target_executed": False,
            "test": "P3B_SOURCE_DELTA_206",
        }, sort_keys=True))
        return 0
    if not 0 < args.max_runtime_seconds <= 5:
        raise ValueError("--max-runtime-seconds must be in (0,5]")
    output_path = args.output.resolve()
    if output_path.exists():
        raise FileExistsError(f"refusing to overwrite output: {output_path}")
    started = time.monotonic()

    base_hash = sha256_file(BASE)
    candidate_hash = sha256_file(CANDIDATE)
    base_tree = ast.parse(BASE.read_text(encoding="utf-8"), filename=str(BASE))
    candidate_tree = ast.parse(
        CANDIDATE.read_text(encoding="utf-8"), filename=str(CANDIDATE)
    )

    checks: dict[str, bool] = {
        "base_hash_exact": base_hash == EXPECTED_BASE_SHA256,
        "candidate_hash_exact": candidate_hash == EXPECTED_CANDIDATE_SHA256,
    }

    assignment_names = (
        "SOURCE", "NAMES", "child", "source_results", "deep_seed",
        "shallow_seed", "y0", "envelope", "scale", "w0", "delta", "p",
        "h0", "omega_m0", "ombh2", "fb", "fc", "neff", "rn", "rg",
        "omega_r0", "hubble0_mpc", "k_mpc", "mu", "g2",
        "transfer_shape", "x_start", "x_final", "checkpoints_x",
    )
    assignment_checks = {}
    for name in assignment_names:
        assignment_checks[name] = (
            ast_dump(unique_assignment(base_tree, name))
            == ast_dump(unique_assignment(candidate_tree, name))
        )
    checks["all_registered_assignments_ast_equal"] = all(
        assignment_checks.values()
    )

    function_checks = {}
    for name in ("background", "scaled_rhs", "integrate_fixed_rk4"):
        function_checks[name] = (
            ast_dump(unique_function(base_tree, name))
            == ast_dump(unique_function(candidate_tree, name))
        )
    checks["background_scaled_rhs_integrator_ast_equal"] = all(
        function_checks.values()
    )

    base_rhs = unique_function(base_tree, "physical_rhs")
    candidate_rhs = unique_function(candidate_tree, "physical_rhs")
    checks["physical_rhs_arguments_equal"] = (
        ast_dump(base_rhs.args) == ast_dump(candidate_rhs.args)
    )
    checks["physical_rhs_pre_return_ast_equal"] = (
        pre_return_statements(base_rhs) == pre_return_statements(candidate_rhs)
    )

    base_components = return_components(base_rhs)
    candidate_components = return_components(candidate_rhs)
    checks["rhs_component_count_13"] = (
        len(base_components) == 13 and len(candidate_components) == 13
    )
    unchanged_component_checks = {
        str(index): ast_dump(base_components[index])
        == ast_dump(candidate_components[index])
        for index in list(range(7)) + list(range(8, 13))
    }
    checks["twelve_other_rhs_components_ast_equal"] = all(
        unchanged_component_checks.values()
    )

    base_terms = Counter(flatten_additive(base_components[7]))
    candidate_terms = Counter(flatten_additive(candidate_components[7]))
    missing_terms = base_terms - candidate_terms
    added_terms = candidate_terms - base_terms
    expected_missing = Counter([
        (
            1,
            ast_dump(ast.parse(
                '(1.5 * Ob - Wg * b["load_fraction"]) * Ug',
                mode="eval",
            ).body),
        ),
        (
            1,
            ast_dump(ast.parse(
                '(0.25 * Wg * b["inv1r"] - 0.5 * Og) * dg',
                mode="eval",
            ).body),
        ),
    ])
    checks["M_prime_no_added_terms"] = not added_terms
    checks["M_prime_missing_exactly_two_registered_terms"] = (
        missing_terms == expected_missing
    )
    checks["M_prime_remaining_term_count_is_seven"] = (
        sum(candidate_terms.values()) == 7
    )

    grid_call_checks = {}
    for name in ("grid100_steps", "grid200_steps", "grid400_steps"):
        grid_call_checks[name] = (
            ast_dump(unique_tuple_assignment(base_tree, name))
            == ast_dump(unique_tuple_assignment(candidate_tree, name))
        )
    checks["three_RK4_grid_calls_ast_equal"] = all(grid_call_checks.values())

    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("source-delta audit deadline exceeded")
    passed = all(checks.values())
    payload = {
        "test": "P3B_SOURCE_DELTA_206",
        "execution_verdict": (
            "PASS_P3B_SOURCE_DELTA_ONLY_TWO_ZERO_TERMS"
            if passed else "REVIEW_P3B_SOURCE_DELTA_MISMATCH"
        ),
        "physics_executed": False,
        "target_executed": False,
        "base_sha256": base_hash,
        "candidate_sha256": candidate_hash,
        "checks": checks,
        "assignment_checks": assignment_checks,
        "function_checks": function_checks,
        "unchanged_component_checks": unchanged_component_checks,
        "grid_call_checks": grid_call_checks,
        "M_prime_base_term_count": sum(base_terms.values()),
        "M_prime_candidate_term_count": sum(candidate_terms.values()),
        "M_prime_missing_terms": counter_records(missing_terms),
        "M_prime_added_terms": counter_records(added_terms),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "scope_limit": "AST/source comparison only; neither source was imported or executed",
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True)
    if not output_path.parent.is_dir():
        raise FileNotFoundError(f"output parent missing: {output_path.parent}")
    with output_path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(encoded + "\n")
    print(encoded)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
