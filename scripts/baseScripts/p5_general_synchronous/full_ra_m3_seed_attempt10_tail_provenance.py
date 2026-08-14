"""No-solve nested-support tail provenance for preregistered KMPC-031.

This module defines no physical equation and executes no solver.  It reads
immutable J4/J6/refined-J8 coefficients, separates common-coefficient drift
from explicit added powers, and applies the already frozen branch thresholds.
"""

from __future__ import annotations

from decimal import Decimal, localcontext
import json
import math
from pathlib import Path
import time

from . import full_ra_m3_seed as physics


RUN_ID = "KMPC-031"
OUTPUT_NAME = "RUN_KMPC_031_P5_3G7_M3_FULL_RA_DEEP_TAIL_BRANCH_PROVENANCE.json"
INPUTS = {
    "J4": (
        "RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_AD_K0p05_NOMINAL.json",
        "2294E8623675B49F2D5A814005306D4E98E3CBDF4A1A66BD3AE1A9C0331EFC83",
    ),
    "J6": (
        "RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J6.json",
        "658495A11A3C72262CDCBEC9B9515794E506A6C7F14F40865704AA26E6C4636A",
    ),
    "J8_ORIGINAL": (
        "RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J8.json",
        "1EE3FCDF3B77C6C7E4C26317A3F39AA45D4CFA5BA6B559E312E598BC3ED51AB8",
    ),
    "KMPC030": (
        "RUN_KMPC_030_P5_3G7_M3_FULL_RA_J8_ONE_REFINEMENT_AUDIT.json",
        "8CB706223C43EB4E72F2B56BE266C73E07349F2E0D6B32212E280AB64F803C6F",
    ),
}
SUPPORTS = {"J4": 4, "J6": 6, "J8": 8}
LEADING_J = 2
DECIMAL_PRECISION = 80
DECIMAL_RECONSTRUCTION_TOL = Decimal("1e-50")
FLOAT_DECIMAL_RTOL = 1.0e-12
FLOAT_DECIMAL_ATOL = 1.0e-300
RAW_EXPECTED = {
    "J4_J6": 1.2308231758460447e-5,
    "J6_J8_refined": 3.3632353573882635e-6,
}
EXPECTED_ROUNDED = {
    "J4_J6": {
        "0.0001": {"relative": 4.66448e-14, "absolute": 4.75112e-38},
        "0.01": {"relative": 4.66857e-8, "absolute": 4.84565e-28},
    },
    "J6_J8_refined": {
        "0.0001": {"relative": 5.16515e-24, "absolute": 3.28409e-46},
        "0.01": {"relative": 5.17916e-14, "absolute": 3.30475e-32},
    },
}
EXPECTED_NUMERICAL_CHECKS = frozenset(
    {
        "F0", "M1", "TCA0_bridge", "all_arrays_and_refined_series_finite",
        "capture_role_order_and_solver_identity", "direct_affine_extraction",
        "exactly_one_correction", "frozen_B1", "frozen_contract",
        "hooks_and_shape_guards_restored", "original_holdout",
        "original_incident_reproduced", "original_rank", "original_reproduction",
        "original_structural_guards", "refined_Uc_lower_regular",
        "refined_coefficient_drift", "refined_direct_driver",
        "refined_direct_holdout", "refined_driver", "refined_forbidden_layers",
        "refined_holdout",
    }
)
EXPECTED_LADDER_CHECKS = frozenset(
    {
        "all_F0_M3_common_coefficient_bridges", "dominant_new_power_membership",
        "exact_added_powers", "tail_details_finite",
        "tail_monotone_on_both_surfaces",
    }
)
FROZEN_SCOPE = (
    "conditional Phi1 M3-TCA0 AD/k=0.05/nominal no-solve support-tail "
    "provenance only; no new equations, solve, ODE, finite opacity, full "
    "hierarchy, CMB, S8, or K4 verdict"
)


def _load_locked(result_dir: Path) -> tuple[dict[str, object], dict[str, object]]:
    loaded: dict[str, object] = {}
    evidence: dict[str, object] = {}
    for label, (name, expected_hash) in INPUTS.items():
        path = result_dir / name
        observed_hash = physics.sha256_file(path)
        if observed_hash != expected_hash:
            raise RuntimeError(f"{label} immutable input hash mismatch")
        loaded[label] = json.loads(path.read_text(encoding="utf-8"))
        evidence[label] = {"file": name, "sha256": observed_hash}
    return loaded, evidence


def _d(value: float) -> Decimal:
    return Decimal(repr(float(value)))


def _restore_series(value: object) -> object:
    """Restore JSON integer exponent keys without importing an older wrapper."""
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


def _decimal_sum(
    series: dict[int, float], powers: range, z: Decimal
) -> Decimal:
    return sum((_d(series.get(power, 0.0)) * z**power for power in powers), Decimal(0))


def _float_sum(series: dict[int, float], powers: range, z: float) -> float:
    return math.fsum(float(series.get(power, 0.0)) * z**power for power in powers)


def _close_float_decimal(float_value: float, decimal_value: Decimal) -> bool:
    return math.isclose(
        float_value,
        float(decimal_value),
        rel_tol=FLOAT_DECIMAL_RTOL,
        abs_tol=FLOAT_DECIMAL_ATOL,
    )


def _bridge_decomposition(
    primary: dict[str, dict[int, float]],
    extended: dict[str, dict[int, float]],
    primary_support: int,
    extended_support: int,
) -> dict[str, object]:
    by_z: dict[str, object] = {}
    all_reconstruction = True
    all_crosschecks = True
    all_finite = True
    for z_float in physics.Z_SURFACES:
        z_key = str(z_float)
        z_decimal = Decimal(z_key)
        rows: dict[str, object] = {}
        relative_candidates: list[tuple[float, str]] = []
        absolute_candidates: list[tuple[float, str]] = []
        with localcontext() as context:
            context.prec = DECIMAL_PRECISION
            for name in physics.contract.AUTHORITATIVE_STATE:
                primary_series = primary[name]
                extended_series = extended[name]
                primary_full_d = _decimal_sum(
                    primary_series, range(0, primary_support + 1), z_decimal
                )
                extended_full_d = _decimal_sum(
                    extended_series, range(0, extended_support + 1), z_decimal
                )
                common_drift_d = sum(
                    (
                        (_d(extended_series.get(power, 0.0))
                         - _d(primary_series.get(power, 0.0)))
                        * z_decimal**power
                        for power in range(0, primary_support + 1)
                    ),
                    Decimal(0),
                )
                added_tail_d = _decimal_sum(
                    extended_series,
                    range(primary_support + 1, extended_support + 1),
                    z_decimal,
                )
                raw_difference_d = extended_full_d - primary_full_d
                reconstruction_d = abs(raw_difference_d - common_drift_d - added_tail_d)

                primary_full_f = _float_sum(
                    primary_series, range(0, primary_support + 1), z_float
                )
                extended_full_f = _float_sum(
                    extended_series, range(0, extended_support + 1), z_float
                )
                common_drift_f = math.fsum(
                    (
                        float(extended_series.get(power, 0.0))
                        - float(primary_series.get(power, 0.0))
                    )
                    * z_float**power
                    for power in range(0, primary_support + 1)
                )
                added_tail_f = _float_sum(
                    extended_series,
                    range(primary_support + 1, extended_support + 1),
                    z_float,
                )
                raw_difference_f = extended_full_f - primary_full_f
                float_reconstruction = abs(
                    raw_difference_f - common_drift_f - added_tail_f
                )

                projected_base_d = _decimal_sum(
                    extended_series,
                    range(LEADING_J, primary_support + 1),
                    z_decimal,
                )
                projected_full_d = projected_base_d + added_tail_d
                scale_d = max(abs(projected_base_d), abs(projected_full_d))
                if scale_d > _d(physics.ABS_FALLBACK_NORM):
                    branch = "relative"
                    metric_d = abs(added_tail_d) / scale_d
                    passed = metric_d <= _d(physics.TAIL_TOL)
                    relative_candidates.append((float(metric_d), name))
                else:
                    branch = "absolute"
                    metric_d = abs(added_tail_d)
                    passed = metric_d <= _d(physics.ABS_FALLBACK_TOL)
                    absolute_candidates.append((float(metric_d), name))

                crosschecks = {
                    "raw_difference": _close_float_decimal(
                        raw_difference_f, raw_difference_d
                    ),
                    "common_drift": _close_float_decimal(
                        common_drift_f, common_drift_d
                    ),
                    "added_tail": _close_float_decimal(added_tail_f, added_tail_d),
                }
                finite = bool(
                    all(
                        value.is_finite()
                        for value in (
                            primary_full_d,
                            extended_full_d,
                            common_drift_d,
                            added_tail_d,
                            raw_difference_d,
                            projected_base_d,
                            projected_full_d,
                            metric_d,
                        )
                    )
                    and all(
                        math.isfinite(value)
                        for value in (
                            primary_full_f,
                            extended_full_f,
                            common_drift_f,
                            added_tail_f,
                            raw_difference_f,
                            float_reconstruction,
                        )
                    )
                )
                row_reconstruction = bool(
                    reconstruction_d <= DECIMAL_RECONSTRUCTION_TOL
                )
                all_reconstruction = all_reconstruction and row_reconstruction
                # Only the directly evaluated added tail is a preregistered
                # float/Decimal gate.  Raw/common differences deliberately
                # expose near-cancellation and remain diagnostic.
                all_crosschecks = all_crosschecks and crosschecks["added_tail"]
                all_finite = all_finite and finite
                rows[name] = {
                    "raw_independent_solve_difference": str(raw_difference_d),
                    "common_low_coefficient_drift": str(common_drift_d),
                    "explicit_added_power_tail": str(added_tail_d),
                    "decimal_reconstruction_abs": str(reconstruction_d),
                    "float_reconstruction_abs": float_reconstruction,
                    "float_decimal_crosschecks": crosschecks,
                    "formal_projected_base": str(projected_base_d),
                    "formal_projected_full": str(projected_full_d),
                    "formal_scale": str(scale_d),
                    "metric_branch": branch,
                    "metric_value": float(metric_d),
                    "pass": bool(passed),
                    "finite": finite,
                }
        worst_relative = max(relative_candidates, default=(0.0, "none"))
        worst_absolute = max(absolute_candidates, default=(0.0, "none"))
        by_z[z_key] = {
            "rows": rows,
            "max_relative": worst_relative[0],
            "worst_relative_state": worst_relative[1],
            "max_absolute_fallback": worst_absolute[0],
            "worst_absolute_fallback_state": worst_absolute[1],
            "pass": bool(
                worst_relative[0] <= physics.TAIL_TOL
                and worst_absolute[0] <= physics.ABS_FALLBACK_TOL
            ),
        }
    return {
        "primary_support": primary_support,
        "extended_support": extended_support,
        "added_powers": list(range(primary_support + 1, extended_support + 1)),
        "by_z": by_z,
        "all_decimal_reconstruction": all_reconstruction,
        "all_required_added_tail_float_decimal_crosschecks": all_crosschecks,
        "all_finite": all_finite,
        "pass": all(bool(item["pass"]) for item in by_z.values()),
    }


def _normalized_tail(bridge: dict[str, object], z: float) -> float:
    surface = bridge["by_z"][str(z)]
    return max(
        float(surface["max_relative"]) / physics.TAIL_TOL,
        float(surface["max_absolute_fallback"]) / physics.ABS_FALLBACK_TOL,
    )


def run_audit(
    result_dir: Path,
    expected_source_hashes: dict[str, str],
    expected_wrapper_hash: str,
    observed_wrapper_hash: str,
    max_runtime_seconds: float,
    progress: dict[str, str],
) -> dict[str, object]:
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError(f"{RUN_ID} internal deadline exceeded")

    progress["current_phase"] = "IMMUTABLE_INPUTS"
    loaded, evidence = _load_locked(result_dir)
    j4_data = loaded["J4"]
    j6_data = loaded["J6"]
    j8_original_data = loaded["J8_ORIGINAL"]
    km30 = loaded["KMPC030"]
    identity_checks = {
        "J4_run_id": j4_data.get("run_id") == "KMPC-028",
        "J6_run_id": j6_data.get("run_id") == "KMPC-029",
        "J8_original_run_id": j8_original_data.get("run_id") == "KMPC-029",
        "KMPC030_run_id": km30.get("run_id") == "KMPC-030",
        "KMPC030_wrapper": (
            km30.get("attempt9_wrapper_sha256")
            == "A8E2EA26B6960F23298259EFBECFFC9806ECF10F0207AE4D2B2AD0C2713DA0AB"
        ),
        "KMPC030_exact_22_numerical_checks": (
            frozenset(km30.get("numerical_checks", {}))
            == EXPECTED_NUMERICAL_CHECKS
        )
        and all(bool(value) for value in km30["numerical_checks"].values()),
        "KMPC030_exact_5_ladder_checks": (
            frozenset(km30["ladder_closure"].get("checks", {}))
            == EXPECTED_LADDER_CHECKS
        )
        and all(bool(value) for value in km30["ladder_closure"]["checks"].values()),
    }
    progress["last_completed_phase"] = "IMMUTABLE_INPUTS"
    deadline()

    j4_unordered = _restore_series(
        j4_data["result"]["m3_extended"]["fractional_state"]
    )
    j6_unordered = _restore_series(j6_data["m3"]["fractional_state"])
    j8_unordered = _restore_series(
        km30["one_refinement"]["fractional_state"]
    )
    expected_state_set = set(physics.contract.AUTHORITATIVE_STATE)
    exact_state_sets = bool(
        set(j4_unordered) == expected_state_set
        and set(j6_unordered) == expected_state_set
        and set(j8_unordered) == expected_state_set
    )
    j4 = {name: j4_unordered[name] for name in physics.contract.AUTHORITATIVE_STATE}
    j6 = {name: j6_unordered[name] for name in physics.contract.AUTHORITATIVE_STATE}
    j8 = {name: j8_unordered[name] for name in physics.contract.AUTHORITATIVE_STATE}
    j4_f0 = _restore_series(j4_data["result"]["fuel_extended"]["state"])
    j6_f0 = _restore_series(j6_data["fuel"]["state"])
    j8_f0 = _restore_series(km30["F0"]["state"])
    canonical_state_remapping = bool(
        exact_state_sets
        and
        tuple(j4) == tuple(physics.contract.AUTHORITATIVE_STATE)
        and tuple(j6) == tuple(physics.contract.AUTHORITATIVE_STATE)
        and tuple(j8) == tuple(physics.contract.AUTHORITATIVE_STATE)
    )
    exact_powers = bool(
        all(sorted(j4[name]) == list(range(0, 5)) for name in j4)
        and all(sorted(j6[name]) == list(range(0, 7)) for name in j6)
        and all(sorted(j8[name]) == list(range(0, 9)) for name in j8)
    )
    expected_f0_states = {"delta_f", "U_f"}
    exact_f0_contract = bool(
        set(j4_f0) == set(j6_f0) == set(j8_f0) == expected_f0_states
        and all(sorted(j4_f0[name]) == list(range(0, 5)) for name in j4_f0)
        and all(sorted(j6_f0[name]) == list(range(0, 7)) for name in j6_f0)
        and all(sorted(j8_f0[name]) == list(range(0, 9)) for name in j8_f0)
    )
    leading_j_matches_frozen_mode = bool(
        LEADING_J == int(physics.legacy.MODE_SPECS["AD"]["leading_j"])
    )
    forbidden_max_by_support = {
        "J4": max(
            abs(float(j4[name][power]))
            for name in physics.contract.AUTHORITATIVE_STATE
            for power in range(0, LEADING_J)
        ),
        "J6": max(
            abs(float(j6[name][power]))
            for name in physics.contract.AUTHORITATIVE_STATE
            for power in range(0, LEADING_J)
        ),
        "refined_J8": max(
            abs(float(j8[name][power]))
            for name in physics.contract.AUTHORITATIVE_STATE
            for power in range(0, LEADING_J)
        ),
    }
    stored_forbidden_guards = {
        "J4": bool(
            j4_data["result"]["m3_extended"]["diagnostics"]
            ["pass_forbidden_layers"]
        ),
        "J6": bool(j6_data["checks"]["M3_forbidden_layers"]),
        "refined_J8": bool(km30["numerical_checks"]["refined_forbidden_layers"]),
    }
    stored_regularity_guards = {
        "J4": bool(
            j4_data["result"]["m3_extended"]["diagnostics"]
            ["Uc_lower_regular_max_abs"]
            <= physics.LEADING_TOL
        ),
        "J6": bool(j6_data["checks"]["M3_Uc_lower_regular"]),
        "refined_J8": bool(km30["numerical_checks"]["refined_Uc_lower_regular"]),
    }
    progress["current_phase"] = "CONTRACT_AND_BRIDGES"
    bridges = {
        "J4_J6_M3": physics._coefficient_metrics(j4, j6),
        "J4_J6_F0": physics._coefficient_metrics(j4_f0, j6_f0),
        "J6_J8_M3": physics._coefficient_metrics(j6, j8),
        "J6_J8_F0": physics._coefficient_metrics(j6_f0, j8_f0),
    }
    progress["last_completed_phase"] = "CONTRACT_AND_BRIDGES"
    deadline()

    progress["current_phase"] = "DECIMAL_FLOAT_DECOMPOSITION"
    decomposition = {
        "J4_J6": _bridge_decomposition(j4, j6, 4, 6),
        "J6_J8_refined": _bridge_decomposition(j6, j8, 6, 8),
    }
    progress["last_completed_phase"] = "DECIMAL_FLOAT_DECOMPOSITION"
    deadline()

    raw_tails = km30["ladder_closure"]["tails"]
    raw_reproduction = {
        label: bool(
            not bool(raw_tails[label]["pass"])
            and raw_tails[label]["physical_tail_by_z"]["0.0001"]
            ["worst_relative_state"]
            == "U_b"
            and math.isclose(
                float(raw_tails[label]["physical_tail_by_z"]["0.0001"]
                      ["max_relative"]),
                expected,
                rel_tol=1.0e-12,
                abs_tol=1.0e-18,
            )
        )
        for label, expected in RAW_EXPECTED.items()
    }
    normalized_by_z = {
        str(z): {
            label: _normalized_tail(bridge, z)
            for label, bridge in decomposition.items()
        }
        for z in physics.Z_SURFACES
    }
    monotone_by_z = {
        str(z): bool(
            normalized_by_z[str(z)]["J6_J8_refined"]
            <= normalized_by_z[str(z)]["J4_J6"]
        )
        for z in physics.Z_SURFACES
    }
    expected_rounding_checks: dict[str, object] = {}
    for label, surfaces in EXPECTED_ROUNDED.items():
        expected_rounding_checks[label] = {}
        for z_key, expected in surfaces.items():
            observed = decomposition[label]["by_z"][z_key]
            expected_rounding_checks[label][z_key] = {
                "relative": math.isclose(
                    float(observed["max_relative"]),
                    expected["relative"],
                    rel_tol=2.0e-5,
                    abs_tol=1.0e-300,
                ),
                "absolute": math.isclose(
                    float(observed["max_absolute_fallback"]),
                    expected["absolute"],
                    rel_tol=2.0e-5,
                    abs_tol=1.0e-300,
                ),
                "worst_relative_state": observed["worst_relative_state"] == "U_f",
            }

    source_text = Path(__file__).read_text(encoding="utf-8")
    forbidden_source_tokens = {
        "numpy_linalg_solve_absent": "np.linalg." + "solve",
        "solve_m3_call_absent": "physics._solve" + "_m3(",
        "solve_fuel_call_absent": "physics._solve" + "_fuel_zero(",
        "solve_ivp_absent": "solve_" + "ivp(",
    }
    no_solve_tokens = {
        label: token not in source_text
        for label, token in forbidden_source_tokens.items()
    }
    checks = {
        **identity_checks,
        "wrapper_hash": observed_wrapper_hash == expected_wrapper_hash,
        "source_hashes": physics.source_hashes() == expected_source_hashes,
        "exact_state_sets_and_canonical_remapping": canonical_state_remapping,
        "exact_power_sets": exact_powers,
        "exact_F0_state_and_power_contract": exact_f0_contract,
        "leading_j_matches_frozen_AD_mode": leading_j_matches_frozen_mode,
        "stored_forbidden_guards": all(stored_forbidden_guards.values()),
        "stored_Uc_regularity_guards": all(stored_regularity_guards.values()),
        "all_projected_layers_below_forbidden_tolerance": all(
            value <= physics.FORBIDDEN_TOL
            for value in forbidden_max_by_support.values()
        ),
        "all_common_F0_M3_bridges": all(
            bool(value["pass"]) for value in bridges.values()
        ),
        "raw_FAIL_reproduced_without_reclassification": all(
            raw_reproduction.values()
        ),
        "all_decimal_reconstruction": all(
            bool(value["all_decimal_reconstruction"])
            for value in decomposition.values()
        ),
        "all_required_added_tail_float_decimal_crosschecks": all(
            bool(value["all_required_added_tail_float_decimal_crosschecks"])
            for value in decomposition.values()
        ),
        "all_values_finite": all(
            bool(value["all_finite"]) for value in decomposition.values()
        ),
        "exact_added_power_sets": bool(
            decomposition["J4_J6"]["added_powers"] == [5, 6]
            and decomposition["J6_J8_refined"]["added_powers"] == [7, 8]
        ),
        "added_tail_monotone_both_surfaces": all(monotone_by_z.values()),
        "preregistered_rounded_expectations": all(
            all(all(item.values()) for item in surfaces.values())
            for surfaces in expected_rounding_checks.values()
        ),
        "no_solve_tokens": all(no_solve_tokens.values()),
    }
    structural_complete = bool(checks) and all(checks.values())
    j4_adequate = bool(
        decomposition["J4_J6"]["pass"]
        and decomposition["J6_J8_refined"]["pass"]
    )
    j6_adequate = bool(
        not decomposition["J4_J6"]["pass"]
        and decomposition["J6_J8_refined"]["pass"]
    )
    if structural_complete and j4_adequate:
        candidate = "CANDIDATE_SUPPORT_TRUNCATION_CLOSED_J4_SENTINEL_SCOPE"
    elif structural_complete and j6_adequate:
        candidate = "CANDIDATE_J6_MINIMUM_SENTINEL_SUPPORT"
    else:
        candidate = "REVIEW_SUPPORT_TAIL_UNCLOSED"
    progress["current_phase"] = "COMPLETE"
    progress["last_completed_phase"] = "COMPLETE"
    deadline()
    return {
        "test": "KMPC-031 no-solve deep-tail branch provenance",
        "run_id": RUN_ID,
        "scope": FROZEN_SCOPE,
        "evidence": evidence,
        "source_hashes": expected_source_hashes,
        "wrapper_sha256": observed_wrapper_hash,
        "thresholds": {
            "tail_relative": physics.TAIL_TOL,
            "absolute_branch_boundary": physics.ABS_FALLBACK_NORM,
            "absolute_fallback": physics.ABS_FALLBACK_TOL,
            "common_coefficient_relative": physics.LOW_COEFFICIENT_TOL,
            "decimal_precision": DECIMAL_PRECISION,
            "decimal_reconstruction_absolute": str(DECIMAL_RECONSTRUCTION_TOL),
            "float_decimal_relative": FLOAT_DECIMAL_RTOL,
            "float_decimal_absolute": FLOAT_DECIMAL_ATOL,
            "rounded_expectation_relative": 2.0e-5,
            "rounded_expectation_absolute": 1.0e-300,
        },
        "identity_checks": identity_checks,
        "common_coefficient_bridges": bridges,
        "formal_projection_guard": {
            "leading_j": LEADING_J,
            "frozen_mode_leading_j": int(
                physics.legacy.MODE_SPECS["AD"]["leading_j"]
            ),
            "forbidden_tolerance": physics.FORBIDDEN_TOL,
            "max_abs_by_support": forbidden_max_by_support,
            "stored_guards": stored_forbidden_guards,
            "stored_Uc_regularity_guards": stored_regularity_guards,
        },
        "raw_mixed_metric": {
            "status": "MIXED_COMMON_DRIFT_PLUS_ADDED_TAIL_DIAGNOSTIC",
            "reproduction_checks": raw_reproduction,
            "stored_tails": raw_tails,
        },
        "formal_added_support_tail": decomposition,
        "normalized_added_tail_by_z": normalized_by_z,
        "added_tail_monotone_by_z": monotone_by_z,
        "preregistered_rounded_expectation_checks": expected_rounding_checks,
        "no_solve_source_checks": no_solve_tokens,
        "checks": checks,
        "execution_status": (
            "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT"
            if structural_complete
            else "REVIEW_SUPPORT_TAIL_PROVENANCE_UNCLOSED"
        ),
        "candidate_interpretation_not_verdict": candidate,
        "physics_verdict": "NONE_NOT_YET_AWARDED",
        "canonical_depth": "60/100",
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "architecture_counter": "10/10",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
