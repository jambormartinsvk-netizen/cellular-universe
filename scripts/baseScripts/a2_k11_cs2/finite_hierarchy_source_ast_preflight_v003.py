"""Lightweight pinned-source AST preflight for K11-CS2/v002."""

from __future__ import annotations

import ast
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import time

from .finite_hierarchy_contract_v002 import (
    authoritative_state,
    closure_registry,
    validate_contract,
)


PINNED_CAMB_SYMBOLIC_SHA256 = (
    "F380B56A15F678F6D8DBA8981BBE5A4E57377050945ADE91C6CD4B9262C7A608"
)
EXPECTED_COUNTS = {4: 25, 6: 33, 8: 41}
EXPECTED_ZERO_TAIL = {4: Fraction(4, 9), 6: Fraction(6, 13), 8: Fraction(8, 17)}
EXPECTED_UPPER = {
    4: Fraction(7, 15),
    6: Fraction(45, 91),
    8: Fraction(77, 153),
}


def _deadline(started: float, limit: float) -> None:
    if time.monotonic() - started > limit:
        raise TimeoutError("K11-CS2 source-AST preflight internal deadline exceeded")


def _dump_expr(source: str) -> str:
    node = ast.parse(f"value = {source}").body[0]
    assert isinstance(node, ast.Assign)
    return ast.dump(node.value, include_attributes=False)


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise RuntimeError(f"expected one function {name}, found {len(matches)}")
    return matches[0]


def _initial_eq(function: ast.FunctionDef) -> ast.expr:
    for node in function.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "eq" for target in node.targets
        ):
            return node.value
    raise RuntimeError(f"missing initial eq assignment in {function.name}")


def _ell2_update(function: ast.FunctionDef) -> ast.expr:
    for node in function.body:
        if isinstance(node, ast.If):
            for child in node.body:
                if isinstance(child, ast.Assign) and any(
                    isinstance(target, ast.Name) and target.id == "eq"
                    for target in child.targets
                ):
                    return child.value
    raise RuntimeError(f"missing ell=2 update in {function.name}")


def _return_expr(function: ast.FunctionDef) -> ast.expr:
    returns = [node for node in function.body if isinstance(node, ast.Return)]
    if len(returns) != 1 or returns[0].value is None:
        raise RuntimeError(f"invalid return structure in {function.name}")
    return returns[0].value


def _same(node: ast.expr, expected: str) -> bool:
    return ast.dump(node, include_attributes=False) == _dump_expr(expected)


def _hierarchy_loop_ok(function: ast.FunctionDef) -> bool:
    loops = [node for node in function.body if isinstance(node, ast.For)]
    if len(loops) != 1:
        return False
    loop = loops[0]
    if not isinstance(loop.target, ast.Name) or loop.target.id != "ell":
        return False
    expected_iter = ast.parse("for ell in range(2, lmax):\n    pass").body[0]
    assert isinstance(expected_iter, ast.For)
    if ast.dump(loop.iter, include_attributes=False) != ast.dump(
        expected_iter.iter, include_attributes=False
    ):
        return False
    calls = []
    for node in ast.walk(loop):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in {"J_eq", "G_eq", "E_eq"}:
                calls.append(node.func.id)
    return calls == ["J_eq", "G_eq", "E_eq"]


def _negative_fixtures(lmax: int) -> dict[str, bool]:
    exact = authoritative_state(lmax)
    fixtures = {
        "extra_E0": exact + ("E_gamma_0",),
        "extra_E1": exact + ("E_gamma_1",),
        "missing_E2": tuple(x for x in exact if x != "E_gamma_2"),
        "missing_steam_L": tuple(x for x in exact if x != f"F_steam_{lmax}"),
        "same_count_fake": exact[:-1] + ("fake_state",),
        "duplicate": exact[:-1] + (exact[-2],),
        "reordered": exact[:-2] + (exact[-1], exact[-2]),
    }
    result = {
        f"reject_{name}": not validate_contract(
            lmax=lmax, state=value, rhs_keys=value
        ).accepted
        for name, value in fixtures.items()
    }
    result["reject_rhs_extra"] = not validate_contract(
        lmax=lmax, state=exact, rhs_keys=exact + ("fake_rhs",)
    ).accepted
    result["reject_rhs_reordered"] = not validate_contract(
        lmax=lmax, state=exact, rhs_keys=exact[:-2] + (exact[-1], exact[-2])
    ).accepted
    return result


def run_source_ast_preflight(*, max_runtime_seconds: float = 5.0) -> dict[str, object]:
    if not (0.0 < max_runtime_seconds <= 5.0):
        raise ValueError("max_runtime_seconds must be in (0, 5]")
    started = time.monotonic()
    root = Path(__file__).resolve().parents[3]
    source_path = root / ".deps" / "python" / "camb" / "symbolic.py"
    source_bytes = source_path.read_bytes()
    source_hash = sha256(source_bytes).hexdigest().upper()
    source = source_bytes.decode("utf-8")
    tree = ast.parse(source, filename=str(source_path))
    checks: dict[str, bool] = {
        "pinned_camb_symbolic_hash": source_hash == PINNED_CAMB_SYMBOLIC_SHA256,
    }

    j_eq = _function(tree, "J_eq")
    g_eq = _function(tree, "G_eq")
    e_eq = _function(tree, "E_eq")
    hierarchy = _function(tree, "get_hierarchies")
    checks.update(
        {
            "J_initial_eq_ast": _same(
                _initial_eq(j_eq),
                "-k / (2 * L + 1) * ((L + 1) * Kf[L] * Glp - L * Glm) - opacity * Gl",
            ),
            "G_initial_eq_ast": _same(
                _initial_eq(g_eq),
                "-k / (2 * L + 1) * ((L + 1) * Kf[L] * Glp - L * Glm)",
            ),
            "E_initial_eq_ast": _same(
                _initial_eq(e_eq),
                "-k / (2 * L + 1) * ((L + 3) * (L - 1) * Kf[L] * Elp / (L + 1) - L * Elm) - opacity * El",
            ),
            "J_ell2_source_ast": _same(
                _ell2_update(j_eq), "eq + 8 * k / 15 * sigma + opacity * polter"
            ),
            "G_ell2_source_ast": _same(
                _ell2_update(g_eq), "eq + 8 * k / 15 * sigma"
            ),
            "E_ell2_source_ast": _same(
                _ell2_update(e_eq), "eq + polter * opacity"
            ),
            "J_return_substitution_ast": _same(
                _return_expr(j_eq),
                "Eq(diff(Gl, t), eq).subs({_make_index_func('J', 2): pi_g, _make_index_func('J', 1): q_g})",
            ),
            "G_return_substitution_ast": _same(
                _return_expr(g_eq),
                "Eq(diff(Gl, t), eq).subs({_make_index_func('G', 2): pi_r, _make_index_func('G', 1): q_r})",
            ),
            "E_return_substitution_ast": _same(
                _return_expr(e_eq),
                "Eq(diff(El, t), eq).subs(_make_index_func('E', 1), 0)",
            ),
            "hierarchy_range_and_families_ast": _hierarchy_loop_ok(hierarchy),
        }
    )

    counts: dict[str, int] = {}
    for lmax, expected_count in EXPECTED_COUNTS.items():
        _deadline(started, max_runtime_seconds)
        state = authoritative_state(lmax)
        counts[str(lmax)] = len(state)
        checks[f"contract_L{lmax}"] = validate_contract(
            lmax=lmax, state=state, rhs_keys=state
        ).accepted
        checks[f"hardcoded_count_L{lmax}"] = len(state) == expected_count
        checks[f"no_E0_E1_L{lmax}"] = (
            "E_gamma_0" not in state and "E_gamma_1" not in state
        )
        zero_tail = Fraction(lmax, 2 * lmax + 1)
        upper = Fraction((lmax + 3) * (lmax - 1), (lmax + 1) * (2 * lmax + 1))
        checks[f"zero_tail_coefficient_L{lmax}"] = zero_tail == EXPECTED_ZERO_TAIL[lmax]
        checks[f"CAMB_E_upper_coefficient_L{lmax}"] = upper == EXPECTED_UPPER[lmax]
        for name, rejected in _negative_fixtures(lmax).items():
            checks[f"{name}_L{lmax}"] = rejected

    registry = closure_registry()
    checks["closures_declared_non_exact"] = all(
        not bool(meta["is_exact_physics"]) for meta in registry.values()
    )
    checks["closures_require_lmax_convergence"] = all(
        bool(meta["requires_lmax_convergence"]) for meta in registry.values()
    )
    _deadline(started, max_runtime_seconds)
    passed = all(checks.values())
    this_file = Path(__file__).resolve()
    contract_file = this_file.with_name("finite_hierarchy_contract_v002.py")
    return {
        "test": "K11-CS2 full v002 pinned-source AST structural preflight",
        "technical_attempt": 4,
        "scope": "pinned CAMB source AST + exact ordered state contract + registered numerical truncation; no ODE",
        "verdict": (
            "PASS_ARCH_A_SOURCE_AST_EXACT_SET_AND_REGISTERED_TRUNCATION_ONLY"
            if passed else "STOP_ARCH_A_SOURCE_AST_OR_CONTRACT_FAILURE"
        ),
        "checks": checks,
        "check_count": len(checks),
        "failed_checks": [name for name, ok in checks.items() if not ok],
        "state_counts": counts,
        "closure_registry": registry,
        "source_sha256": {
            "camb_symbolic": source_hash,
            "preflight": sha256(this_file.read_bytes()).hexdigest().upper(),
            "contract": sha256(contract_file.read_bytes()).hexdigest().upper(),
        },
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "required_next_gate": "full DAE plus lmax and closure-family convergence",
    }

