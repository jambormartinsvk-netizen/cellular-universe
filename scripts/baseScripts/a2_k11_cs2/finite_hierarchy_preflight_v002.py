"""Bounded exact-set/interior/truncation preflight for K11-CS2/v002."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import sys
import time
from typing import Final


ROOT: Final = Path(__file__).resolve().parents[3]
LOCAL_DEPS: Final = ROOT / ".deps" / "python"
if LOCAL_DEPS.exists() and str(LOCAL_DEPS) not in sys.path:
    sys.path.insert(0, str(LOCAL_DEPS))

import sympy as sp  # noqa: E402
import camb  # noqa: E402
import camb.symbolic as cs  # noqa: E402

from .finite_hierarchy_contract_v002 import (  # noqa: E402
    authoritative_state,
    closure_registry,
    validate_contract,
)


def _deadline(started: float, limit: float) -> None:
    if time.monotonic() - started > limit:
        raise TimeoutError("K11-CS2/v002 preflight internal deadline exceeded")


def _digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest().upper()


def _brightness(family: str, ell: int):
    if family == "J":
        if ell == 1:
            return cs.q_g
        if ell == 2:
            return cs.pi_g
    if family == "G":
        if ell == 1:
            return cs.q_r
        if ell == 2:
            return cs.pi_r
    return cs._make_index_func(family, ell)


def _expected_j(ell: int):
    current = _brightness("J", ell)
    previous = _brightness("J", ell - 1)
    following = _brightness("J", ell + 1)
    value = -cs.k / (2 * ell + 1) * (
        (ell + 1) * cs.Kf[ell] * following - ell * previous
    ) - cs.opacity * current
    if ell == 2:
        value += sp.Rational(8, 15) * cs.k * cs.sigma + cs.opacity * cs.polter
    return sp.simplify(value)


def _expected_g(ell: int):
    current = _brightness("G", ell)
    previous = _brightness("G", ell - 1)
    following = _brightness("G", ell + 1)
    value = -cs.k / (2 * ell + 1) * (
        (ell + 1) * cs.Kf[ell] * following - ell * previous
    )
    if ell == 2:
        value += sp.Rational(8, 15) * cs.k * cs.sigma
    return sp.simplify(value)


def _expected_e(ell: int):
    current = cs._make_index_func("E", ell)
    previous = 0 if ell == 2 else cs._make_index_func("E", ell - 1)
    following = cs._make_index_func("E", ell + 1)
    value = cs.k / (2 * ell + 1) * (
        ell * previous
        - (ell + 3) * (ell - 1) * cs.Kf[ell] * following / (ell + 1)
    ) - cs.opacity * current
    if ell == 2:
        value += cs.opacity * cs.polter
    return sp.simplify(value)


def _zero_tail_e_top(ell: int):
    current = cs._make_index_func("E", ell)
    previous = cs._make_index_func("E", ell - 1)
    return sp.simplify(
        cs.k * ell * previous / (2 * ell + 1) - cs.opacity * current
    )


def _negative_fixtures(lmax: int) -> dict[str, bool]:
    exact = authoritative_state(lmax)
    fixtures = {
        "reject_extra_E0": exact + ("E_gamma_0",),
        "reject_extra_E1": exact + ("E_gamma_1",),
        "reject_missing_E2": tuple(x for x in exact if x != "E_gamma_2"),
        "reject_missing_steam_L": tuple(
            x for x in exact if x != f"F_steam_{lmax}"
        ),
        "reject_same_count_fake": exact[:-1] + ("fake_state",),
        "reject_duplicate": exact[:-1] + (exact[-2],),
        "reject_reordered": exact[:-2] + (exact[-1], exact[-2]),
    }
    rejected = {
        name: not validate_contract(lmax=lmax, state=value, rhs_keys=value).accepted
        for name, value in fixtures.items()
    }
    rejected["reject_rhs_extra"] = not validate_contract(
        lmax=lmax, state=exact, rhs_keys=exact + ("fake_rhs",)
    ).accepted
    rejected["reject_rhs_reordered"] = not validate_contract(
        lmax=lmax, state=exact, rhs_keys=exact[:-2] + (exact[-1], exact[-2])
    ).accepted
    return rejected


def run_preflight(*, lmax_values: tuple[int, ...], max_runtime_seconds: float) -> dict[str, object]:
    if not lmax_values:
        raise ValueError("at least one lmax is required")
    if not (0.0 < max_runtime_seconds <= 5.0):
        raise ValueError("max_runtime_seconds must be in (0, 5]")
    started = time.monotonic()
    checks: dict[str, bool] = {}
    residuals: dict[str, str] = {}
    counts: dict[str, int] = {}

    for lmax in lmax_values:
        _deadline(started, max_runtime_seconds)
        state = authoritative_state(lmax)
        counts[str(lmax)] = len(state)
        validation = validate_contract(lmax=lmax, state=state, rhs_keys=state)
        checks[f"contract_L{lmax}"] = validation.accepted
        residuals[f"contract_L{lmax}"] = validation.reason
        checks[f"count_L{lmax}"] = len(state) == 4 * lmax + 9
        residuals[f"count_L{lmax}"] = str(len(state) - (4 * lmax + 9))
        checks[f"no_E0_E1_L{lmax}"] = (
            "E_gamma_0" not in state and "E_gamma_1" not in state
        )
        residuals[f"no_E0_E1_L{lmax}"] = (
            "0" if checks[f"no_E0_E1_L{lmax}"] else "forbidden_state"
        )

        for ell in range(2, lmax):
            for family, source, expected in (
                ("J", cs.J_eq(ell).rhs, _expected_j(ell)),
                ("G", cs.G_eq(ell).rhs, _expected_g(ell)),
                ("E", cs.E_eq(ell).rhs, _expected_e(ell)),
            ):
                residual = sp.simplify(source - expected)
                checks[f"CAMB_{family}_interior_L{lmax}_l{ell}"] = residual == 0
                residuals[f"CAMB_{family}_interior_L{lmax}_l{ell}"] = str(residual)

        e_following = cs._make_index_func("E", lmax + 1)
        conditional_source = sp.simplify(cs.E_eq(lmax).rhs.subs(e_following, 0))
        conditional_residual = sp.simplify(
            conditional_source - _zero_tail_e_top(lmax)
        )
        checks[f"E_zero_tail_conditional_L{lmax}"] = conditional_residual == 0
        residuals[f"E_zero_tail_conditional_L{lmax}"] = str(conditional_residual)

        for name, rejected in _negative_fixtures(lmax).items():
            checks[f"{name}_L{lmax}"] = rejected
            residuals[f"{name}_L{lmax}"] = "0" if rejected else "accepted_bad_contract"

    registry = closure_registry()
    checks["closures_declared_non_exact"] = all(
        not bool(meta["is_exact_physics"]) for meta in registry.values()
    )
    residuals["closures_declared_non_exact"] = (
        "0" if checks["closures_declared_non_exact"] else "false_exact_claim"
    )
    checks["closures_require_lmax_convergence"] = all(
        bool(meta["requires_lmax_convergence"]) for meta in registry.values()
    )
    residuals["closures_require_lmax_convergence"] = (
        "0" if checks["closures_require_lmax_convergence"] else "missing_requirement"
    )
    _deadline(started, max_runtime_seconds)

    passed = all(checks.values())
    this_file = Path(__file__).resolve()
    contract_file = this_file.with_name("finite_hierarchy_contract_v002.py")
    return {
        "test": "K11-CS2 full v002 attempt 1 structural truncation preflight",
        "scope": "exact ordered set + exact CAMB interior + registered numerical top; no ODE",
        "verdict": (
            "PASS_ARCH_A_ATTEMPT_1_EXACT_SET_INTERIOR_AND_REGISTERED_TRUNCATION_ONLY"
            if passed else "STOP_ARCH_A_ATTEMPT_1_STRUCTURAL_OR_CONTRACT_FAILURE"
        ),
        "lmax_values": list(lmax_values),
        "state_count_formula": "4*lmax+9",
        "state_counts": counts,
        "checks": checks,
        "residuals": residuals,
        "closure_registry": registry,
        "camb_version": camb.__version__,
        "source_sha256": {
            "preflight": _digest(this_file),
            "contract": _digest(contract_file),
            "camb_symbolic": _digest(Path(cs.__file__).resolve()),
        },
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "required_next_gate": "full DAE plus lmax and closure-family convergence",
    }

