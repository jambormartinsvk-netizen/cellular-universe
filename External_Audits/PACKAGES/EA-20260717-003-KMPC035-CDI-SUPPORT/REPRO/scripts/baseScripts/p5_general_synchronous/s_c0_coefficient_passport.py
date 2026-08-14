"""KMPC-032 exact lower-moment passport for the conditional S-C0 split.

This module does not enlarge or solve the frozen 13-state system.  It loads
the already anchored five M1 standard states, constructs an explicit
neutrino/steam view of delta_fs, U_fs and sigma_fs, and proves exact weighted
lift/collapse identities.  l=3,4 are tested only as generic linear operators;
five-mode higher-multipole coefficient dictionaries are not available here.
"""

from __future__ import annotations

import hashlib
import math
from pathlib import Path
import time
from typing import Callable, Mapping

import sympy as sp

from . import full_ra_contract as ra_contract
from . import full_ra_m3_seed as m3
from . import mode_resolved_puiseux as legacy
from . import s1_collective_contract as collective_contract


RUN_ID = "KMPC-032"
OUTPUT_NAME = "RUN_KMPC_032_P5_3G7_S_C0_COEFFICIENT_PASSPORT.json"
FAILURE_NAME = "RUN_KMPC_032_P5_3G7_S_C0_COEFFICIENT_PASSPORT_TECHNICAL_FAILURE.json"
K_MPC = 0.05
EXPECTED_CANDIDATE = (
    "PASS_S_C0_LOWER_MOMENT_COEFFICIENT_LIFT_COLLAPSE_PASSPORT_ONLY"
)
HIGHER_SCOPE = "HIGHER_MULTIPOLE_COEFFICIENTS_NOT_IN_SCOPE"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    names = (
        "full_ra_contract.py",
        "full_ra_m3_seed.py",
        "mode_resolved_puiseux.py",
        "mode_resolved_puiseux_v2_m1_anchored.py",
        "s1_collective_contract.py",
        "s_c0_coefficient_passport.py",
    )
    return {name: sha256_file(here / name) for name in names}


def make_deadline(max_runtime_seconds: float) -> Callable[[], None]:
    if not 0.0 < max_runtime_seconds <= 4.8:
        raise ValueError("internal runtime must be in (0, 4.8] seconds")
    started = time.monotonic()

    def check() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("KMPC-032 internal deadline exceeded")

    return check


def _q(value: object) -> sp.Rational:
    if isinstance(value, sp.Rational):
        return value
    if isinstance(value, int):
        return sp.Rational(value)
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("non-finite M1 coefficient")
        return sp.Rational(repr(value))
    return sp.Rational(str(value))


def exact_radiation_weights(n_s: sp.Rational = sp.Rational(107, 2000)) -> dict[str, sp.Rational]:
    alpha = sp.Rational(2271, 10000)
    n_nu = sp.Rational(1523, 500)
    total = 1 + alpha * (n_nu + n_s)
    weights = {
        "R_gamma": sp.cancel(1 / total),
        "R_nu": sp.cancel(alpha * n_nu / total),
        "R_s": sp.cancel(alpha * n_s / total),
    }
    weights["R_fs"] = sp.cancel(weights["R_nu"] + weights["R_s"])
    return weights


def _series_add(*items: Mapping[int, sp.Expr]) -> dict[int, sp.Expr]:
    keys = set().union(*(item.keys() for item in items))
    return {
        power: value
        for power in keys
        if (value := sp.cancel(sum(item.get(power, 0) for item in items))) != 0
    }


def _series_scale(item: Mapping[int, sp.Expr], factor: sp.Expr) -> dict[int, sp.Expr]:
    return {
        power: value
        for power, raw in item.items()
        if (value := sp.cancel(factor * raw)) != 0
    }


def _series_mul(first: Mapping[int, sp.Expr], second: Mapping[int, sp.Expr]) -> dict[int, sp.Expr]:
    out: dict[int, sp.Expr] = {}
    for left_power, left in first.items():
        for right_power, right in second.items():
            power = int(left_power + right_power)
            out[power] = out.get(power, 0) + left * right
    return {
        power: value
        for power, raw in out.items()
        if (value := sp.cancel(raw)) != 0
    }


def _series_dx(item: Mapping[int, sp.Expr]) -> dict[int, sp.Expr]:
    return {
        power: value
        for power, raw in item.items()
        if (value := sp.cancel(power * raw)) != 0
    }


def _exact_series(item: Mapping[int, float]) -> dict[int, sp.Expr]:
    return {int(power): _q(value) for power, value in item.items() if value != 0.0}


def _collisionless_rows(
    state: Mapping[str, Mapping[int, sp.Expr]],
    background: Mapping[str, Mapping[int, sp.Expr]],
) -> dict[str, dict[int, sp.Expr]]:
    hx = _series_dx(state["h"])
    etax = _series_dx(state["eta"])
    return {
        "continuity": _series_add(
            _series_dx(state["delta"]),
            _series_scale(_series_mul(background["s2"], state["U"]), sp.Rational(4, 3)),
            _series_scale(hx, sp.Rational(2, 3)),
        ),
        "shear": _series_add(
            _series_scale(_series_dx(state["sigma"]), 2),
            _series_scale(hx, sp.Rational(-4, 15)),
            _series_scale(etax, sp.Rational(-8, 5)),
            _series_scale(_series_mul(background["s2"], state["U"]), sp.Rational(-8, 15)),
        ),
        "Euler": _series_add(
            _series_dx(state["U"]),
            _series_scale(_series_mul(background["hc"], state["U"]), -1),
            _series_scale(state["delta"], sp.Rational(-1, 4)),
            state["sigma"],
        ),
    }


def _dictionary_residual(
    first: Mapping[int, sp.Expr], second: Mapping[int, sp.Expr]
) -> dict[int, sp.Expr]:
    return _series_add(first, _series_scale(second, -1))


def _lift_residual(value: sp.Expr, weights: Mapping[str, sp.Rational]) -> dict[str, sp.Expr]:
    y_fs = value
    y_nu = value
    y_s = value
    return {
        "nu_minus_s": sp.cancel(y_nu - y_s),
        "weighted_collapse": sp.cancel(
            weights["R_nu"] * y_nu
            + weights["R_s"] * y_s
            - weights["R_fs"] * y_fs
        ),
        "collapse_after_lift": sp.cancel(
            (weights["R_nu"] * y_nu + weights["R_s"] * y_s)
            / weights["R_fs"]
            - y_fs
        ),
    }


def _manifest_and_fixtures() -> tuple[dict[str, object], dict[str, object]]:
    candidate = collective_contract.canonical_candidate()
    production = collective_contract.validate_candidate(candidate)
    fixture_results: dict[str, object] = {}
    for name, fixture in collective_contract.negative_fixture_candidates().items():
        result = collective_contract.validate_candidate(fixture)
        fixture_results[name] = {
            "rejected": not result.valid,
            "errors": list(result.errors),
        }
    return (
        {"valid": production.valid, "errors": list(production.errors), "candidate": candidate},
        fixture_results,
    )


def run_smoke(max_runtime_seconds: float) -> dict[str, object]:
    deadline = make_deadline(max_runtime_seconds)
    manifest, fixtures = _manifest_and_fixtures()
    weights = exact_radiation_weights()
    deadline()
    checks = {
        "independent_candidate_contract": bool(manifest["valid"]),
        "ten_negative_fixtures_present": len(fixtures) == 10,
        "all_negative_fixtures_rejected": all(item["rejected"] for item in fixtures.values()),
        "exact_weight_sum": sp.cancel(weights["R_gamma"] + weights["R_fs"] - 1) == 0,
        "positive_steam_weight": weights["R_s"] > 0,
    }
    return {
        "run_id": RUN_ID,
        "mode": "SMOKE_NO_RESULT_FILE",
        "checks": checks,
        "passed": bool(checks) and all(checks.values()),
    }


def run_audit(max_runtime_seconds: float) -> dict[str, object]:
    deadline = make_deadline(max_runtime_seconds)
    manifest, fixtures = _manifest_and_fixtures()
    weights = exact_radiation_weights()
    inputs = legacy.FrozenInputs()

    frozen_contract = ra_contract.validate_contract(
        collective_contract.EXPECTED_STATE,
        collective_contract.EXPECTED_DRIVER,
        collective_contract.EXPECTED_HOLDOUT,
    )
    frozen_support_checks = {
        mode: {
            "primary": tuple(collective_contract.MODE_SPEC[mode]["primary"]) == tuple(m3.MODE_SUPPORT[mode]),
            "f0_primary": collective_contract.MODE_SPEC[mode]["f0_primary"] == m3.EXPECTED_F0_PRIMARY[mode],
            "f0_extended": collective_contract.MODE_SPEC[mode]["f0_extended"] == m3.EXPECTED_F0_EXTENDED[mode],
            "m3_primary": collective_contract.MODE_SPEC[mode]["m3_primary"] == m3.EXPECTED_M3_PRIMARY[mode],
            "m3_extended": collective_contract.MODE_SPEC[mode]["m3_extended"] == m3.EXPECTED_M3_EXTENDED[mode],
            "leading_j": collective_contract.MODE_SPEC[mode]["leading_j"] == legacy.MODE_SPECS[mode]["leading_j"],
        }
        for mode in collective_contract.MODES
    }
    deadline()

    mode_results: dict[str, object] = {}
    all_exact_lift = True
    all_row_identity = True
    all_standard_guards = True
    all_slot_identity = True

    for mode in collective_contract.MODES:
        deadline()
        standard, metadata = m3._standard_state(mode, K_MPC, inputs, deadline)
        all_standard_guards = all_standard_guards and bool(metadata["pass"])
        series = legacy.Series(-4, 10)
        background_float = legacy._standard_background(K_MPC, inputs, series)
        background = {
            "s2": _exact_series(background_float["s2"]),
            "hc": _exact_series(background_float["hc"]),
        }
        common_state = {
            "h": _exact_series(standard["h"]),
            "eta": _exact_series(standard["eta"]),
            "delta": _exact_series(standard["delta_fs"]),
            "U": _exact_series(standard["U_fs"]),
            "sigma": _exact_series(standard["sigma_fs"]),
        }
        row_fs = _collisionless_rows(common_state, background)
        row_nu = _collisionless_rows(dict(common_state), background)
        row_s = _collisionless_rows(dict(common_state), background)
        row_residuals = {
            name: {
                "nu_minus_fs": _dictionary_residual(row_nu[name], row_fs[name]),
                "steam_minus_fs": _dictionary_residual(row_s[name], row_fs[name]),
            }
            for name in row_fs
        }
        rows_zero = all(
            not residual
            for row in row_residuals.values()
            for residual in row.values()
        )
        all_row_identity = all_row_identity and rows_zero

        coefficient_results: dict[str, object] = {}
        for state_name, moment in collective_contract.STATE_TO_MOMENT.items():
            by_power: dict[str, object] = {}
            for power, raw in sorted(standard[state_name].items()):
                residual = _lift_residual(_q(raw), weights)
                by_power[str(power)] = {name: str(value) for name, value in residual.items()}
                all_exact_lift = all_exact_lift and all(value == 0 for value in residual.values())
            coefficient_results[moment] = by_power

        slot_results: dict[str, object] = {}
        lo, hi = collective_contract.MODE_SPEC[mode]["extended"]
        for moment in collective_contract.LOWER_MOMENTS:
            by_power: dict[str, object] = {}
            for power in range(lo, hi + 1):
                symbol = sp.Symbol(f"{mode}_{moment}_{power}")
                residual = _lift_residual(symbol, weights)
                by_power[str(power)] = {name: str(value) for name, value in residual.items()}
                all_slot_identity = all_slot_identity and all(value == 0 for value in residual.values())
            slot_results[moment] = by_power

        mode_results[mode] = {
            "standard_metadata": {
                key: metadata[key]
                for key in (
                    "rank", "unknowns", "hard_anchor_absolute_difference",
                    "condition_resolved", "driver_scaled_residual",
                    "holdout_scaled_residual", "pass",
                )
            },
            "actual_M1_coefficients_checked": sum(len(standard[name]) for name in collective_contract.STATE_TO_MOMENT),
            "coefficient_lift_residuals": coefficient_results,
            "registered_extended_slot_residuals": slot_results,
            "lower_moment_row_residuals": {
                row: {
                    label: {str(power): str(value) for power, value in residual.items()}
                    for label, residual in values.items()
                }
                for row, values in row_residuals.items()
            },
            "all_lower_moment_rows_equal": rows_zero,
        }

    deadline()
    y = sp.Symbol("Y")
    source_residuals = {
        moment: sp.cancel(
            weights["R_nu"] * y + weights["R_s"] * y - weights["R_fs"] * y
        )
        for moment in collective_contract.LOWER_MOMENTS
    }

    hierarchy_operator: dict[str, object] = {}
    all_hierarchy = True
    kappa = sp.Symbol("kappa")
    for ell in (3, 4):
        left = sp.Symbol(f"F_{ell-1}")
        right = sp.Symbol(f"F_{ell+1}")
        operator = sp.cancel(kappa * (ell * left - (ell + 1) * right) / (2 * ell + 1))
        residual = sp.cancel(
            weights["R_nu"] * operator
            + weights["R_s"] * operator
            - weights["R_fs"] * operator
        )
        hierarchy_operator[str(ell)] = str(residual)
        all_hierarchy = all_hierarchy and residual == 0

    nid_amplitude = sp.Symbol("D_NID", nonzero=True)
    niv_amplitude = sp.Symbol("U_NIV", nonzero=True)
    nid_correct = sp.cancel(
        weights["R_gamma"] * (-weights["R_fs"] / weights["R_gamma"] * nid_amplitude)
        + weights["R_fs"] * nid_amplitude
    )
    nid_wrong = sp.cancel(
        weights["R_gamma"] * (-weights["R_nu"] / weights["R_gamma"] * nid_amplitude)
        + weights["R_fs"] * nid_amplitude
    )
    niv_correct = sp.cancel(
        weights["R_gamma"] * (-weights["R_fs"] / weights["R_gamma"] * niv_amplitude)
        + weights["R_fs"] * niv_amplitude
    )
    niv_wrong = sp.cancel(
        weights["R_gamma"] * (-weights["R_nu"] / weights["R_gamma"] * niv_amplitude)
        + weights["R_fs"] * niv_amplitude
    )

    zero_weights = exact_radiation_weights(sp.Rational(0))
    zero_limit = {
        "R_s": sp.cancel(zero_weights["R_s"]),
        "R_fs_minus_R_nu": sp.cancel(zero_weights["R_fs"] - zero_weights["R_nu"]),
        "collapse": sp.cancel(
            zero_weights["R_nu"] * y + zero_weights["R_s"] * y - zero_weights["R_fs"] * y
        ),
    }

    checks = {
        "independent_candidate_contract": bool(manifest["valid"]),
        "frozen_RA_contract": bool(frozen_contract.valid),
        "frozen_support_and_count_contract": all(all(item.values()) for item in frozen_support_checks.values()),
        "exact_weight_sum": sp.cancel(weights["R_gamma"] + weights["R_fs"] - 1) == 0,
        "exact_Rfs_split": sp.cancel(weights["R_nu"] + weights["R_s"] - weights["R_fs"]) == 0,
        "positive_weights": all(value > 0 for value in weights.values()),
        "five_actual_M1_standard_guards": all_standard_guards,
        "actual_coefficient_lift_collapse": all_exact_lift,
        "registered_extended_slot_lift_collapse": all_slot_identity,
        "lower_moment_rows_equal_coefficientwise": all_row_identity,
        "density_momentum_shear_sources": all(value == 0 for value in source_residuals.values()),
        "hierarchy_operator_L3_L4_commutes": all_hierarchy,
        "NID_correct_Rfs_compensation": nid_correct == 0,
        "NID_wrong_Rnu_compensation_rejected": nid_wrong != 0,
        "NIV_correct_Rfs_compensation": niv_correct == 0,
        "NIV_wrong_Rnu_compensation_rejected": niv_wrong != 0,
        "collective_zero_limit": all(value == 0 for value in zero_limit.values()),
        "ten_negative_fixtures_present": len(fixtures) == 10,
        "all_negative_fixtures_rejected": all(item["rejected"] for item in fixtures.values()),
    }
    passed = bool(checks) and all(bool(value) for value in checks.values())
    deadline()
    return {
        "test": "A2-K4 P5.3g7 S-C0 lower-moment coefficient passport",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": EXPECTED_CANDIDATE if passed else "REVIEW_S_C0_PASSPORT_CHECK_FAILURE",
        "scope": {
            "included": "five anchored M1 states; delta_fs/U_fs/sigma_fs exact collective lift and sources",
            "higher_multipoles": HIGHER_SCOPE,
            "operator_only": "generic collisionless l=3,4 weighted-collapse commute",
            "excluded": "new solve, ODE, S-M microphysics, full seven-mode basis, finite opacity, CMB, G8, CLASS, S8/H0",
        },
        "inputs": {"k_mpc": K_MPC, "variant": "nominal", "modes": list(collective_contract.MODES)},
        "exact_weights": {name: str(value) for name, value in weights.items()},
        "manifest_validation": manifest,
        "frozen_support_checks": frozen_support_checks,
        "negative_fixtures": fixtures,
        "source_residuals": {name: str(value) for name, value in source_residuals.items()},
        "hierarchy_operator_residuals": hierarchy_operator,
        "NID_NIV_compensation": {
            "NID_correct": str(nid_correct), "NID_wrong_Rnu": str(nid_wrong),
            "NIV_correct": str(niv_correct), "NIV_wrong_Rnu": str(niv_wrong),
        },
        "zero_limit": {name: str(value) for name, value in zero_limit.items()},
        "mode_results": mode_results,
        "checks": checks,
        "all_checks_pass": passed,
        "source_hashes": source_hashes(),
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
        "score_effect": "NONE",
    }

