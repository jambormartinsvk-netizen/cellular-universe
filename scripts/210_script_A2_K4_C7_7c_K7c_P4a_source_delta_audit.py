#!/usr/bin/env python3
"""Fail-closed AST audit proving that 209 preserves the P3b physics."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import time
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASE = HERE / "205_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4_audited.py"
CANDIDATE = HERE / "209_script_A2_K4_C7_7c_K7c_P4a_single_case_solver.py"
DEFAULT_OUTPUT = ROOT / "Audit" / "A2_K4_K7C_P4A_SOURCE_DELTA_210_2026-07-15.json"
EXPECTED_BASE_SHA256 = (
    "B7EC8BAD3BFB0D48EC91D6F1BB0A602FA1834A021BB94C92D6D1B398D5F3CDC2"
)
EXPECTED_CANDIDATE_SHA256 = (
    "67E5B3C1B7C942242E4FEB4458A4CC81A52F6417E25D50A6E2009023F321A612"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def dump(node: ast.AST) -> str:
    return ast.dump(node, include_attributes=False)


def unique_function(tree: ast.AST, name: str) -> ast.FunctionDef:
    matches = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise RuntimeError(f"function {name!r} count changed: {len(matches)}")
    return matches[0]


def target_names(target: ast.AST) -> list[str]:
    if isinstance(target, ast.Name):
        return [target.id]
    if isinstance(target, (ast.Tuple, ast.List)):
        names: list[str] = []
        for element in target.elts:
            names.extend(target_names(element))
        return names
    return []


def unique_assignment_value(tree: ast.AST, name: str) -> ast.AST:
    matches: list[ast.AST] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                matches.append(node.value)
                continue
            if not isinstance(target, ast.Tuple) or not isinstance(node.value, ast.Tuple):
                continue
            if len(target.elts) != len(node.value.elts):
                continue
            for index, element in enumerate(target.elts):
                if isinstance(element, ast.Name) and element.id == name:
                    matches.append(node.value.elts[index])
    if len(matches) != 1:
        raise RuntimeError(f"assignment {name!r} count changed: {len(matches)}")
    return matches[0]


def unique_binding_statement(function: ast.FunctionDef, name: str) -> ast.Assign:
    matches: list[ast.Assign] = []
    for node in ast.walk(function):
        if not isinstance(node, ast.Assign):
            continue
        if any(name in target_names(target) for target in node.targets):
            matches.append(node)
    if len(matches) != 1:
        raise RuntimeError(
            f"binding statement {function.name}.{name} count changed: {len(matches)}"
        )
    return matches[0]


def return_components(function: ast.FunctionDef) -> list[ast.AST]:
    returns = [node for node in function.body if isinstance(node, ast.Return)]
    if len(returns) != 1:
        raise RuntimeError(f"{function.name} return count changed")
    value = returns[0].value
    if not isinstance(value, ast.Call) or not value.args:
        raise RuntimeError("physical_rhs return is not an np.asarray call")
    first = value.args[0]
    if not isinstance(first, ast.List):
        raise RuntimeError("physical_rhs return first argument is not a list")
    return list(first.elts)


def literal_assignment(tree: ast.AST, name: str) -> Any:
    return ast.literal_eval(unique_assignment_value(tree, name))


def main() -> int:
    parser = argparse.ArgumentParser(description="AST-only P4a source-delta audit")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    if not 0 < args.max_runtime_seconds <= 5:
        parser.error("max-runtime-seconds must be in (0,5]")
    if args.smoke:
        fixture = ast.parse("x_start, x_final = -25.0, -24.75")
        passed = (
            ast.literal_eval(unique_assignment_value(fixture, "x_start")) == -25.0
            and ast.literal_eval(unique_assignment_value(fixture, "x_final")) == -24.75
        )
        print(json.dumps({
            "smoke": True,
            "tuple_assignment_fixture_pass": passed,
            "physics_executed": False,
            "target_executed": False,
        }, sort_keys=True))
        return 0 if passed else 1

    output_path = args.output.resolve()
    if output_path.exists():
        raise FileExistsError(f"refusing to overwrite output: {output_path}")
    if not output_path.parent.is_dir():
        raise FileNotFoundError(f"output parent missing: {output_path.parent}")
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
        "SOURCE", "NAMES", "deep_seed", "shallow_seed", "y0", "envelope",
        "scale", "w0", "delta", "p", "h0", "omega_m0", "ombh2", "fb",
        "fc", "neff", "rn", "rg", "omega_r0", "hubble0_mpc", "k_mpc",
        "mu", "g2", "transfer_shape", "x_start", "x_final",
    )
    assignment_checks = {
        name: dump(unique_assignment_value(base_tree, name))
        == dump(unique_assignment_value(candidate_tree, name))
        for name in assignment_names
    }
    checks["all_registered_physical_assignments_ast_equal"] = all(
        assignment_checks.values()
    )

    base_background = unique_function(base_tree, "background")
    candidate_background = unique_function(candidate_tree, "background")
    checks["background_ast_equal"] = dump(base_background) == dump(
        candidate_background
    )

    base_rhs = unique_function(base_tree, "physical_rhs")
    candidate_rhs = unique_function(candidate_tree, "physical_rhs")
    binding_names = ("h", "b", "Og", "Wg", "dn", "Un", "hx", "Ah")
    binding_checks = {
        name: dump(unique_binding_statement(base_rhs, name))
        == dump(unique_binding_statement(candidate_rhs, name))
        for name in binding_names
    }
    checks["all_physical_rhs_bindings_ast_equal"] = all(binding_checks.values())
    base_components = return_components(base_rhs)
    candidate_components = return_components(candidate_rhs)
    component_checks = {
        str(index): dump(base_components[index]) == dump(candidate_components[index])
        for index in range(13)
    }
    checks["rhs_component_count_13"] = (
        len(base_components) == 13 and len(candidate_components) == 13
    )
    checks["all_13_rhs_components_ast_equal"] = all(component_checks.values())
    checks["scaled_rhs_ast_equal"] = dump(unique_function(base_tree, "scaled_rhs")) == dump(
        unique_function(candidate_tree, "scaled_rhs")
    )

    cases = literal_assignment(candidate_tree, "CASES")
    expected_cases = {
        "DOP853_MEDIUM": {"method": "DOP853", "rtol": 1e-9, "atol": 1e-11},
        "DOP853_TIGHT": {"method": "DOP853", "rtol": 1e-11, "atol": 1e-13},
        "RADAU_TIGHT": {"method": "Radau", "rtol": 1e-10, "atol": 1e-12},
    }
    checks["case_mapping_exact"] = cases == expected_cases
    solve_calls = [
        node for node in ast.walk(candidate_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "solve_ivp"
    ]
    checks["exactly_one_solve_ivp_call"] = len(solve_calls) == 1
    checks["no_fixed_RK4_integrator_in_candidate"] = not any(
        isinstance(node, ast.FunctionDef) and node.name == "integrate_fixed_rk4"
        for node in ast.walk(candidate_tree)
    )
    candidate_text = CANDIDATE.read_text(encoding="utf-8")
    checks["immutable_output_mode_present"] = 'open("x"' in candidate_text
    checks["reference_sha_literal_present"] = (
        "9E3C73D635924E829A5F57BA540EBB1F5861F67F21CFCE69BD93423D6FA8FC8D"
        in candidate_text
    )
    checks["rhs_cap_100000_present"] = "rhs_calls > 100000" in candidate_text
    checks["normalized_safety_cap_1e8_present"] = (
        "maximum_normalized_abs > 1e8" in candidate_text
    )

    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("P4a source-delta deadline exceeded")
    passed = all(checks.values())
    payload = {
        "test": "P4A_SOURCE_DELTA_210",
        "execution_verdict": (
            "PASS_P4A_SOURCE_DELTA_SOLVER_WRAPPER_ONLY"
            if passed else "REVIEW_P4A_SOURCE_DELTA_MISMATCH"
        ),
        "physics_executed": False,
        "target_executed": False,
        "base_sha256": base_hash,
        "candidate_sha256": candidate_hash,
        "checks": checks,
        "assignment_checks": assignment_checks,
        "binding_checks": binding_checks,
        "component_checks": component_checks,
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "scope_limit": "AST/source audit only; neither 205 nor 209 was imported or run",
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True)
    with output_path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(encoded + "\n")
    print(encoded)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

