"""Technical higher-support ladder for preregistered KMPC-029.

No physical equation is defined here.  The module calls the frozen KMPC-027
solver and temporarily widens only its expected-shape guard for AD J6/J8.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
import time
from typing import Callable

from . import full_ra_m3_seed as physics


RUN_ID = "KMPC-029"
MODE = "AD"
K_MPC = 0.05
VARIANT = "nominal"
SUPPORTS = (6, 8)
EXPECTED_M1_SHAPES = {
    6: {"full_unknowns": 88, "reduced_unknowns": 87, "rows": 110},
    8: {"full_unknowns": 110, "reduced_unknowns": 109, "rows": 132},
}
SUPPORT_PATTERN = "RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J{support}.json"
AGGREGATE_NAME = "RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_LADDER_ATTEMPT8.json"
REFERENCE_NAME = "RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_AD_K0p05_NOMINAL.json"
REFERENCE_SHA256 = "2294E8623675B49F2D5A814005306D4E98E3CBDF4A1A66BD3AE1A9C0331EFC83"
FROZEN_SCOPE = (
    "conditional Phi1 M3-TCA0 AD/k=0.05/nominal support-ladder only; "
    "no Phi2 CDM recoil, k->0/rho_c->0/delta->0 boundary closure, ODE, "
    "finite opacity, full hierarchy, CMB, S8, or S-M claim"
)


def expected_thresholds() -> dict[str, float]:
    return {
        "rcond": physics.RCOND,
        "pass_singular_ratio": physics.PASS_SINGULAR_RATIO,
        "driver": physics.DRIVER_TOL,
        "holdout": physics.HOLDOUT_TOL,
        "absolute_fallback_norm": physics.ABS_FALLBACK_NORM,
        "absolute_fallback": physics.ABS_FALLBACK_TOL,
        "low_coefficient": physics.LOW_COEFFICIENT_TOL,
        "tail": physics.TAIL_TOL,
    }


def support_name(support: int) -> str:
    if support not in SUPPORTS:
        raise ValueError(f"unsupported ladder support J{support}")
    return SUPPORT_PATTERN.format(support=support)


def _expected_counts(support: int) -> tuple[int, int]:
    return 2 * (support + 1), 13 * (support + 1)


def _core_checks(
    fuel_diag: dict[str, object], m3_diag: dict[str, object]
) -> dict[str, bool]:
    return {
        "F0_rank": bool(fuel_diag["pass_rank"]),
        "F0_driver": bool(fuel_diag["pass_driver"]),
        "F0_leading_postcheck": bool(fuel_diag["pass_leading_postcheck"]),
        "M3_rank": bool(m3_diag["pass_rank"]),
        "M3_driver": bool(m3_diag["pass_driver"]),
        "M3_holdout": bool(m3_diag["holdout"]["pass_holdout"]),
        "M3_forbidden_layers": bool(m3_diag["pass_forbidden_layers"]),
        "M3_forbidden_stress_guard": bool(
            m3_diag["pass_forbidden_stress_guard"]
        ),
        "M3_production_contract": bool(m3_diag["pass_production_contract"]),
        "M3_Uc_lower_regular": bool(
            m3_diag["Uc_lower_regular_max_abs"] <= physics.LEADING_TOL
        ),
    }


def _standard_state_for_support(
    support: int,
    inputs: object,
    deadline: Callable[[], None],
) -> tuple[dict[str, dict[int, float]], dict[str, object]]:
    """Run the existing hard-anchored M1 builder and audit all requested powers."""
    legacy_state, background, metadata = (
        physics.m1_anchor.solve_standard_seed_anchored(
            MODE, K_MPC, inputs, deadline, order=support
        )
    )
    v1 = physics.m1_anchor.v1
    exponents = list(range(-1, support + 1))
    series = v1.Series(-4, support + 5)
    row_map = v1._standard_rows(legacy_state, background, series)
    scale = max(
        max(
            abs(float(value))
            for values in legacy_state.values()
            for value in values.values()
        ),
        abs(float(metadata["m1_expected_h_coefficient"])),
        1.0e-14,
    )
    driver_max = max(
        abs(series.coef(row_map[row], power))
        for row in v1.DRIVER_ROWS
        for power in exponents
    )
    holdout_max = max(
        abs(series.coef(row_map[row], power))
        for row in v1.HOLDOUT_ROWS
        for power in exponents
    )
    initial_count = len(
        v1._initial_constraints(
            MODE, inputs.radiation_weights[1], inputs.radiation_weights[0]
        )
    )
    full_unknowns = len(v1.VARS) * len(exponents)
    rows = len(v1.DRIVER_ROWS) * len(exponents) + initial_count
    expected = EXPECTED_M1_SHAPES[support]
    inverse_condition = 1.0 / max(float(metadata["condition_resolved"]), 1.0)
    finite = all(
        math.isfinite(float(value))
        for values in legacy_state.values()
        for value in values.values()
    )
    audited = dict(metadata)
    audited.update(
        {
            "order": support,
            "exponents": exponents,
            "rows": rows,
            "expected_rows": expected["rows"],
            "expected_full_unknowns": expected["full_unknowns"],
            "expected_reduced_unknowns": expected["reduced_unknowns"],
            "full_order_driver_scaled_residual": float(driver_max / scale),
            "full_order_holdout_scaled_residual": float(holdout_max / scale),
            "residual_normalization": "legacy_global_max_state_coefficient",
            "inverse_resolved_condition": inverse_condition,
            "all_coefficients_finite": finite,
            "pass": bool(
                finite
                and rows == expected["rows"]
                and full_unknowns
                == metadata["full_vector_unknowns"]
                == expected["full_unknowns"]
                and metadata["rank"]
                == metadata["unknowns"]
                == expected["reduced_unknowns"]
                and metadata["hard_anchor_absolute_difference"]
                <= physics.ABS_FALLBACK_TOL
                and driver_max / scale <= physics.DRIVER_TOL
                and holdout_max / scale <= physics.HOLDOUT_TOL
                and inverse_condition >= physics.PASS_SINGULAR_RATIO
            ),
        }
    )
    state = {
        target: {
            power: float(value)
            for power, value in legacy_state[source].items()
        }
        for target, source in physics.STATE_TO_LEGACY.items()
    }
    deadline()
    return state, audited


def _series_finite(*collections: dict[str, dict[int, float]]) -> bool:
    return all(
        math.isfinite(float(value))
        for collection in collections
        for values in collection.values()
        for value in values.values()
    )


def run_support_atom(
    support: int,
    max_runtime_seconds: float,
    progress: dict[str, str],
) -> dict[str, object]:
    """Solve one AD higher support while restoring the frozen shape guards."""
    if support not in SUPPORTS:
        raise ValueError(f"unsupported ladder support J{support}")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError(f"{RUN_ID} support J{support} deadline exceeded")

    progress["current_phase"] = "FROZEN_GUARDS"
    frozen_contract = physics.validate_frozen_contract()
    frozen_b1 = physics.b1_guard.build_contract_guard(
        max_runtime_seconds=min(1.0, max_runtime_seconds)
    )
    tca0_bridge = physics.production_tca0_reduction_guard()
    progress["last_completed_phase"] = "FROZEN_GUARDS"
    deadline()

    progress["current_phase"] = "M1_STANDARD_STATE"
    inputs = physics._variant_inputs(VARIANT)
    standard, standard_meta = _standard_state_for_support(
        support, inputs, deadline
    )
    progress["last_completed_phase"] = "M1_STANDARD_STATE"
    deadline()

    expected_f0, expected_m3 = _expected_counts(support)
    before = {
        "F0_expected_extended": physics.EXPECTED_F0_EXTENDED[MODE],
        "M3_expected_extended": physics.EXPECTED_M3_EXTENDED[MODE],
    }
    if before != {"F0_expected_extended": 10, "M3_expected_extended": 65}:
        raise RuntimeError(f"unexpected frozen shape guards before adapter: {before}")

    fuel: dict[str, dict[int, float]]
    fuel_diag: dict[str, object]
    fractional: dict[str, dict[int, float]]
    m3_meta: dict[str, object]
    progress["current_phase"] = f"SUPPORT_J{support}_SOLVE"
    try:
        physics.EXPECTED_F0_EXTENDED[MODE] = expected_f0
        physics.EXPECTED_M3_EXTENDED[MODE] = expected_m3
        during = {
            "F0_expected_extended": physics.EXPECTED_F0_EXTENDED[MODE],
            "M3_expected_extended": physics.EXPECTED_M3_EXTENDED[MODE],
        }
        fuel, fuel_diag = physics._solve_fuel_zero(
            MODE, K_MPC, inputs, standard, (0, support), deadline
        )
        combined_standard = dict(standard)
        combined_standard.update(fuel)
        fractional, m3_meta = physics._solve_m3(
            MODE, K_MPC, inputs, combined_standard, (0, support), deadline
        )
        progress["last_completed_phase"] = f"SUPPORT_J{support}_SOLVE"
    finally:
        physics.EXPECTED_F0_EXTENDED[MODE] = before["F0_expected_extended"]
        physics.EXPECTED_M3_EXTENDED[MODE] = before["M3_expected_extended"]

    after = {
        "F0_expected_extended": physics.EXPECTED_F0_EXTENDED[MODE],
        "M3_expected_extended": physics.EXPECTED_M3_EXTENDED[MODE],
    }
    restored = after == before
    deadline()
    m3_diag = m3_meta["diagnostics"]
    checks = {
        "frozen_contract": bool(frozen_contract["valid"]),
        "frozen_B1_left_null_and_Bianchi_guard": (
            frozen_b1["execution_verdict"]
            == "PASS_R_A_B1_CONTRACT_GUARD_ONLY"
        ),
        "production_TCA0_bridge": bool(tca0_bridge["pass"]),
        "M1": bool(standard_meta["pass"]),
        "M1_exact_order": bool(standard_meta["order"] == support),
        "shape_guard_during": during
        == {
            "F0_expected_extended": expected_f0,
            "M3_expected_extended": expected_m3,
        },
        "shape_guard_restored": restored,
        "F0_exact_shape": bool(
            fuel_diag["rows"] == fuel_diag["unknowns"] == expected_f0
        ),
        "M3_exact_shape": bool(
            m3_diag["rows"] == m3_diag["unknowns"] == expected_m3
        ),
        "all_M1_F0_M3_coefficients_finite": bool(
            standard_meta["all_coefficients_finite"]
            and _series_finite(fuel, fractional)
        ),
        **_core_checks(fuel_diag, m3_diag),
    }
    passed = bool(checks) and all(checks.values())
    progress["current_phase"] = "COMPLETE"
    progress["last_completed_phase"] = "COMPLETE"
    return {
        "test": f"KMPC-029 AD/k=0.05/nominal support J{support}",
        "run_id": RUN_ID,
        "mode": MODE,
        "k_Mpc_inverse": K_MPC,
        "variant": VARIANT,
        "support": [0, support],
        "scope": FROZEN_SCOPE,
        "contract": frozen_contract,
        "frozen_B1_left_null_Bianchi_guard": frozen_b1,
        "production_TCA0_reduction_guard": tca0_bridge,
        "M1": standard_meta,
        "shape_guard_adapter": {
            "before": before,
            "during": during,
            "after": after,
            "restored": restored,
            "allowed_mutation_only": [
                "EXPECTED_F0_EXTENDED[AD]",
                "EXPECTED_M3_EXTENDED[AD]",
            ],
        },
        "fuel": {"state": fuel, "diagnostics": fuel_diag},
        "m3": {"fractional_state": fractional, **m3_meta},
        "source_hashes": physics.source_hashes(),
        "ladder_wrapper_sha256": physics.sha256_file(Path(__file__).resolve()),
        "thresholds": expected_thresholds(),
        "z_surfaces": list(physics.Z_SURFACES),
        "checks": checks,
        "execution_status": (
            "PASS_SUPPORT_SOLVE_ATOM" if passed else "REVIEW_SUPPORT_SOLVE_ATOM"
        ),
        "physics_verdict": "NONE_NOT_YET_AWARDED",
        "canonical_depth": "60/100",
        "score_effect": "NONE",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }


def _restore_series(value: object) -> object:
    if isinstance(value, dict):
        restored: dict[object, object] = {}
        for key, item in value.items():
            try:
                restored_key: object = int(key)
            except (TypeError, ValueError):
                restored_key = key
            restored[restored_key] = _restore_series(item)
        return restored
    if isinstance(value, list):
        return [_restore_series(item) for item in value]
    return value


def _effective_exponent(tail: dict[str, object]) -> float:
    deep = float(tail["physical_tail_by_z"][str(physics.Z_SURFACES[0])]["max_relative"])
    shallow = float(tail["physical_tail_by_z"][str(physics.Z_SURFACES[1])]["max_relative"])
    if deep <= 0.0 or shallow <= 0.0:
        return math.nan
    return math.log(shallow / deep) / math.log(
        physics.Z_SURFACES[1] / physics.Z_SURFACES[0]
    )


def _per_state_tail_and_new_terms(
    primary: dict[str, dict[int, float]],
    extended: dict[str, dict[int, float]],
) -> dict[str, object]:
    by_z: dict[str, object] = {}
    dominant_by_z: dict[str, object] = {}
    added_powers = sorted(
        {
            power
            for name, values in extended.items()
            for power in values
            if power not in primary[name]
        }
    )
    for z in physics.Z_SURFACES:
        rows: dict[str, object] = {}
        candidates: list[tuple[float, str, int, float]] = []
        for name in physics.contract.AUTHORITATIVE_STATE:
            primary_value = sum(
                value * z**power for power, value in primary[name].items()
            )
            extended_value = sum(
                value * z**power for power, value in extended[name].items()
            )
            difference = abs(extended_value - primary_value)
            scale = max(abs(primary_value), abs(extended_value))
            if scale > physics.ABS_FALLBACK_NORM:
                metric_kind = "relative"
                metric_value = difference / scale
                passed = metric_value <= physics.TAIL_TOL
            else:
                metric_kind = "absolute"
                metric_value = difference
                passed = metric_value <= physics.ABS_FALLBACK_TOL
            rows[name] = {
                "primary": float(primary_value),
                "extended": float(extended_value),
                "difference": float(difference),
                "metric_kind": metric_kind,
                "metric_value": float(metric_value),
                "pass": bool(passed),
            }
            for power in added_powers:
                coefficient = float(extended[name].get(power, 0.0))
                contribution = abs(coefficient * z**power)
                candidates.append((contribution, name, power, coefficient))
        winner = max(candidates, default=(0.0, "none", 0, 0.0))
        by_z[str(z)] = rows
        dominant_by_z[str(z)] = {
            "state": winner[1],
            "power": winner[2],
            "coefficient": winner[3],
            "absolute_cj_zj": winner[0],
            "status": "DIAGNOSTIC_ONLY",
        }
    finite = all(
        math.isfinite(float(item["metric_value"]))
        for rows in by_z.values()
        for item in rows.values()
    ) and all(
        math.isfinite(float(item["absolute_cj_zj"]))
        for item in dominant_by_z.values()
    )
    return {
        "added_powers": added_powers,
        "per_state_by_z": by_z,
        "dominant_new_term_by_z": dominant_by_z,
        "finite": finite,
    }


def _normalized_tail_scalar(tail: dict[str, object], z: float) -> float:
    surface = tail["physical_tail_by_z"][str(z)]
    return max(
        float(surface["max_relative"]) / physics.TAIL_TOL,
        float(surface["max_absolute_fallback"])
        / physics.ABS_FALLBACK_TOL,
    )


def aggregate_ladder(
    result_dir: Path,
    expected_source_hashes: dict[str, str],
    expected_wrapper_hash: str,
    observed_wrapper_hash: str,
    hash_file: Callable[[Path], str],
    max_runtime_seconds: float,
) -> dict[str, object]:
    """Compare immutable J4, J6 and J8 states; never execute a solve."""
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError(f"{RUN_ID} ladder aggregate deadline exceeded")

    expected_support_names = {support_name(support) for support in SUPPORTS}
    observed_support_names = {
        path.name
        for path in result_dir.glob(
            "RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J*.json"
        )
    }
    if observed_support_names != expected_support_names:
        raise RuntimeError(
            "support result set mismatch: "
            f"missing={sorted(expected_support_names - observed_support_names)}, "
            f"extra={sorted(observed_support_names - expected_support_names)}"
        )

    reference_path = result_dir / REFERENCE_NAME
    if hash_file(reference_path) != REFERENCE_SHA256:
        raise RuntimeError("KMPC-028 J4 reference hash mismatch")
    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    if reference.get("run_id") != "KMPC-028":
        raise RuntimeError("KMPC-028 J4 reference identity mismatch")

    support_data: dict[int, dict[str, object]] = {}
    evidence: dict[str, object] = {
        "J4_reference": {
            "path": reference_path.name,
            "sha256": REFERENCE_SHA256,
        }
    }
    checks: dict[str, bool] = {
        "wrapper_hash": observed_wrapper_hash == expected_wrapper_hash,
        "exact_support_result_set": len(observed_support_names) == 2,
        "J4_reference_verdict_is_expected_review": (
            reference.get("verdict") == "REVIEW_M3_TCA0_SEED_ATOM_UNCLOSED"
        ),
    }
    for support in SUPPORTS:
        path = result_dir / support_name(support)
        data = json.loads(path.read_text(encoding="utf-8"))
        support_data[support] = data
        label = f"J{support}"
        evidence[label] = {"path": path.name, "sha256": hash_file(path)}
        expected_f0, expected_m3 = _expected_counts(support)
        checks[f"{label}:identity"] = bool(
            data.get("run_id") == RUN_ID
            and data.get("mode") == MODE
            and data.get("k_Mpc_inverse") == K_MPC
            and data.get("variant") == VARIANT
            and data.get("support") == [0, support]
        )
        checks[f"{label}:source_hashes"] = (
            data.get("source_hashes") == expected_source_hashes
        )
        checks[f"{label}:wrapper_hash"] = (
            data.get("ladder_wrapper_sha256") == expected_wrapper_hash
        )
        checks[f"{label}:scope"] = data.get("scope") == FROZEN_SCOPE
        checks[f"{label}:thresholds"] = (
            data.get("thresholds") == expected_thresholds()
        )
        checks[f"{label}:runtime"] = data.get("runtime_limit_seconds") == 4.8
        checks[f"{label}:z_surfaces"] = (
            data.get("z_surfaces") == list(physics.Z_SURFACES)
        )
        checks[f"{label}:shape"] = bool(
            data["fuel"]["diagnostics"]["rows"]
            == data["fuel"]["diagnostics"]["unknowns"]
            == expected_f0
            and data["m3"]["diagnostics"]["rows"]
            == data["m3"]["diagnostics"]["unknowns"]
            == expected_m3
        )
        expected_m1 = EXPECTED_M1_SHAPES[support]
        checks[f"{label}:M1_order_and_shape"] = bool(
            data["M1"]["order"] == support
            and data["M1"]["rows"] == expected_m1["rows"]
            and data["M1"]["full_vector_unknowns"]
            == expected_m1["full_unknowns"]
            and data["M1"]["unknowns"]
            == data["M1"]["rank"]
            == expected_m1["reduced_unknowns"]
        )
        checks[f"{label}:all_checks"] = bool(data.get("checks")) and all(
            bool(value) for value in data.get("checks", {}).values()
        )
        checks[f"{label}:execution_status"] = (
            data.get("execution_status") == "PASS_SUPPORT_SOLVE_ATOM"
        )
        deadline()

    j4_m3 = _restore_series(
        reference["result"]["m3_extended"]["fractional_state"]
    )
    j4_f0 = _restore_series(reference["result"]["fuel_extended"]["state"])
    j6_m3 = _restore_series(support_data[6]["m3"]["fractional_state"])
    j6_f0 = _restore_series(support_data[6]["fuel"]["state"])
    j8_m3 = _restore_series(support_data[8]["m3"]["fractional_state"])
    j8_f0 = _restore_series(support_data[8]["fuel"]["state"])

    bridges = {
        "J4_J6_M3": physics._coefficient_metrics(j4_m3, j6_m3),
        "J4_J6_F0": physics._coefficient_metrics(j4_f0, j6_f0),
        "J6_J8_M3": physics._coefficient_metrics(j6_m3, j8_m3),
        "J6_J8_F0": physics._coefficient_metrics(j6_f0, j8_f0),
    }
    checks["all_common_coefficient_bridges"] = all(
        bool(value["pass"]) for value in bridges.values()
    )
    inputs = physics._variant_inputs(VARIANT)
    j4_j6_tail = physics._truncation_metrics(
        MODE, j4_m3, j6_m3, inputs, K_MPC
    )
    j6_j8_tail = physics._truncation_metrics(
        MODE, j6_m3, j8_m3, inputs, K_MPC
    )
    tail_detail = {
        "J4_J6": _per_state_tail_and_new_terms(j4_m3, j6_m3),
        "J6_J8": _per_state_tail_and_new_terms(j6_m3, j8_m3),
    }
    checks["tail_detail_finite"] = all(
        bool(value["finite"]) for value in tail_detail.values()
    )
    checks["exact_added_power_sets"] = bool(
        tail_detail["J4_J6"]["added_powers"] == [5, 6]
        and tail_detail["J6_J8"]["added_powers"] == [7, 8]
    )
    checks["dominant_new_power_membership"] = bool(
        all(
            item["power"] in tail_detail["J4_J6"]["added_powers"]
            for item in tail_detail["J4_J6"]["dominant_new_term_by_z"].values()
        )
        and all(
            item["power"] in tail_detail["J6_J8"]["added_powers"]
            for item in tail_detail["J6_J8"]["dominant_new_term_by_z"].values()
        )
    )
    normalized_tail_scalar_by_z = {
        str(z): {
            "J4_J6": _normalized_tail_scalar(j4_j6_tail, z),
            "J6_J8": _normalized_tail_scalar(j6_j8_tail, z),
        }
        for z in physics.Z_SURFACES
    }
    monotone_by_z = {
        str(z): bool(
            normalized_tail_scalar_by_z[str(z)]["J6_J8"]
            <= normalized_tail_scalar_by_z[str(z)]["J4_J6"]
        )
        for z in physics.Z_SURFACES
    }
    checks["tail_monotone_on_both_surfaces"] = all(monotone_by_z.values())
    j4_adequate = bool(j4_j6_tail["pass"] and j6_j8_tail["pass"])
    j6_adequate = bool((not j4_j6_tail["pass"]) and j6_j8_tail["pass"])
    structural_complete = bool(checks) and all(checks.values())
    if structural_complete and j4_adequate:
        candidate = "PASS_SUPPORT_LADDER_SENTINEL_J4_ADEQUATE"
    elif structural_complete and j6_adequate:
        candidate = "REVIEW_PRODUCTION_SUPPORT_MUST_BE_AT_LEAST_J6"
    else:
        candidate = "REVIEW_SUPPORT_LADDER_UNCLOSED"
    return {
        "test": "KMPC-029 AD support ladder J4/J6/J8 attempt 8",
        "run_id": RUN_ID,
        "scope": FROZEN_SCOPE,
        "evidence": evidence,
        "source_hashes": expected_source_hashes,
        "ladder_wrapper_sha256": observed_wrapper_hash,
        "thresholds": expected_thresholds(),
        "coefficient_bridges": bridges,
        "tails": {"J4_J6": j4_j6_tail, "J6_J8": j6_j8_tail},
        "per_state_tail_and_dominant_new_term_diagnostic_only": tail_detail,
        "effective_tail_exponent_diagnostic_only": {
            "J4_J6": _effective_exponent(j4_j6_tail),
            "J6_J8": _effective_exponent(j6_j8_tail),
        },
        "tail_monotone_by_z": monotone_by_z,
        "normalized_tail_scalar_by_z": normalized_tail_scalar_by_z,
        "checks": checks,
        "execution_status": (
            "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_NUMERICAL_AUDIT"
            if structural_complete
            else "TECHNICAL_OR_NUMERICAL_REVIEW_REQUIRED"
        ),
        "candidate_interpretation_not_verdict": candidate,
        "physics_verdict": "NONE_NOT_YET_AWARDED",
        "canonical_depth": "60/100",
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
