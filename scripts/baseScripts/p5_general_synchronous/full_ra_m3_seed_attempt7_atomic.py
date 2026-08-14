"""Technical atomisation layer for KMPC-028 attempt 7.

This module contains no physical equations.  It delegates every solve and
every physical diagnostic to the frozen KMPC-027 ``full_ra_m3_seed`` module.
One process handles one (mode, k, variant) atom so a technical deadline cannot
hide the status of the other atoms.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
import time
from typing import Callable

from . import full_ra_m3_seed as physics


RUN_ID = "KMPC-028"
MODES = ("AD", "CDI", "BI", "NID", "NIV")
K_VALUES = physics.K_VALUES
VARIANTS = ("nominal", "gamma0", "af0")
K_TOKENS = {0.005: "0p005", 0.05: "0p05", 0.15: "0p15"}
ATOM_PATTERN = "RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_{mode}_K{k_token}_{variant}.json"
AGGREGATE_NAME = "RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOMIC_ATTEMPT7.json"
FROZEN_SCOPE = (
    "conditional Phi1 M3-TCA0 seed only; no Phi2 CDM recoil, "
    "k->0/rho_c->0/delta->0 boundary closure, ODE, finite opacity, "
    "full hierarchy, CMB, S8, or S-M claim"
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
        "background_k": physics.BACKGROUND_K_TOL,
        "steam_split": physics.STEAM_SPLIT_TOL,
    }


def atom_name(mode: str, k_mpc: float, variant: str) -> str:
    validate_atom_identity(mode, k_mpc, variant)
    return ATOM_PATTERN.format(
        mode=mode,
        k_token=K_TOKENS[k_mpc],
        variant=variant.upper(),
    )


def validate_atom_identity(mode: str, k_mpc: float, variant: str) -> None:
    if mode not in MODES:
        raise ValueError(f"unsupported mode {mode!r}")
    if k_mpc not in K_TOKENS:
        raise ValueError(f"unsupported k {k_mpc!r}")
    if variant not in VARIANTS:
        raise ValueError(f"unsupported variant {variant!r}")


def run_atom(
    mode: str,
    k_mpc: float,
    variant: str,
    max_runtime_seconds: float,
    progress: dict[str, str],
) -> dict[str, object]:
    """Run exactly one frozen physics atom and return its complete evidence."""
    validate_atom_identity(mode, k_mpc, variant)
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError(
                f"{RUN_ID} {mode}/k={k_mpc}/{variant} internal deadline exceeded"
            )

    progress["current_phase"] = "FROZEN_CONTRACT"
    frozen_contract = physics.validate_frozen_contract()
    progress["last_completed_phase"] = "FROZEN_CONTRACT"
    deadline()

    progress["current_phase"] = "B1_LEFT_NULL_BIANCHI_GUARD"
    frozen_b1 = physics.b1_guard.build_contract_guard(
        max_runtime_seconds=min(1.0, max_runtime_seconds)
    )
    progress["last_completed_phase"] = "B1_LEFT_NULL_BIANCHI_GUARD"
    deadline()

    progress["current_phase"] = "PRODUCTION_TCA0_BRIDGE"
    tca0_bridge = physics.production_tca0_reduction_guard()
    progress["last_completed_phase"] = "PRODUCTION_TCA0_BRIDGE"
    deadline()

    progress["current_phase"] = "M1_STANDARD_STATE"
    standard, standard_meta = physics._standard_state(
        mode,
        k_mpc,
        physics._variant_inputs("nominal"),
        deadline,
    )
    progress["last_completed_phase"] = "M1_STANDARD_STATE"
    deadline()

    progress["current_phase"] = "F0_M3_PRIMARY_AND_EXTENDED_SOLVES"
    result = physics._single_variant(
        mode,
        k_mpc,
        variant,
        standard,
        deadline,
    )
    progress["last_completed_phase"] = "F0_M3_PRIMARY_AND_EXTENDED_SOLVES"
    deadline()

    progress["current_phase"] = "BACKGROUND_AND_STEAM_SPLIT"
    inputs = physics._variant_inputs(variant)
    backgrounds = {
        str(a): physics._physical_background(
            inputs, k_mpc, a, physics.BACKGROUND_MAX_J
        )
        for a in physics.A_VALUES_BACKGROUND
    }
    r_gamma, r_fs, r_nu, r_steam = inputs.radiation_weights
    split_residual = abs(r_nu + r_steam - r_fs)
    progress["last_completed_phase"] = "BACKGROUND_AND_STEAM_SPLIT"
    deadline()

    checks = {
        "frozen_contract": bool(frozen_contract["valid"]),
        "frozen_B1_left_null_and_Bianchi_guard": (
            frozen_b1["execution_verdict"]
            == "PASS_R_A_B1_CONTRACT_GUARD_ONLY"
        ),
        "production_TCA0_weighted_Euler_and_Thomson_bridge": bool(
            tca0_bridge["pass"]
        ),
        "M1_accepted_frozen_helper": bool(standard_meta["pass"]),
        "F0_M3_primary_extended_variant": bool(result["pass"]),
        "conditional_S_C_weight_split": bool(
            split_residual <= physics.STEAM_SPLIT_TOL
        ),
    }
    passed = bool(checks) and all(checks.values())
    progress["current_phase"] = "COMPLETE"
    progress["last_completed_phase"] = "COMPLETE"
    return {
        "test": (
            f"KMPC-028 attempt-7 atom {mode}/k={k_mpc}/{variant}"
        ),
        "run_id": RUN_ID,
        "mode": mode,
        "k_Mpc_inverse": k_mpc,
        "variant": variant,
        "scope": FROZEN_SCOPE,
        "contract": frozen_contract,
        "frozen_B1_left_null_Bianchi_guard": frozen_b1,
        "production_TCA0_reduction_guard": tca0_bridge,
        "M1": standard_meta,
        "result": result,
        "background_physical_values_by_a": backgrounds,
        "conditional_steam_split": {
            "R_gamma": r_gamma,
            "R_fs": r_fs,
            "R_nu": r_nu,
            "R_steam": r_steam,
            "residual": split_residual,
        },
        "source_hashes": physics.source_hashes(),
        "atomic_wrapper_sha256": physics.sha256_file(Path(__file__).resolve()),
        "thresholds": expected_thresholds(),
        "z_surfaces": list(physics.Z_SURFACES),
        "background_a_surfaces": list(physics.A_VALUES_BACKGROUND),
        "checks": checks,
        "verdict": (
            "PASS_M3_TCA0_SEED_CONDITIONAL_ATOM"
            if passed
            else "REVIEW_M3_TCA0_SEED_ATOM_UNCLOSED"
        ),
        "canonical_depth": "60/100",
        "score_effect": "NONE_UNTIL_WHOLE_G7_CLOSES",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }


def _restore_series(value: object) -> object:
    """Restore integer Puiseux powers after JSON stringifies mapping keys."""
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


def _spread(values: list[float]) -> float:
    if not values:
        return math.inf
    return float(
        (max(values) - min(values))
        / max(max(abs(value) for value in values), 1.0e-300)
    )


def aggregate_atoms(
    result_dir: Path,
    expected_source_hashes: dict[str, str],
    expected_wrapper_hash: str,
    observed_wrapper_hash: str,
    hash_file: Callable[[Path], str],
    max_runtime_seconds: float,
) -> dict[str, object]:
    """Audit 45 immutable atom files without executing a new solve."""
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError(f"{RUN_ID} aggregate internal deadline exceeded")

    expected_names = {
        atom_name(mode, k_mpc, variant)
        for mode in MODES
        for k_mpc in K_VALUES
        for variant in VARIANTS
    }
    observed_names = {
        path.name
        for path in result_dir.glob(
            "RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_*.json"
        )
    }
    if observed_names != expected_names:
        raise RuntimeError(
            "atom set mismatch: "
            f"missing={sorted(expected_names - observed_names)}, "
            f"extra={sorted(observed_names - expected_names)}"
        )

    atoms: dict[tuple[str, float, str], dict[str, object]] = {}
    evidence: dict[str, object] = {}
    checks: dict[str, bool] = {
        "exact_45_atom_names": len(expected_names) == 45,
        "wrapper_hash": observed_wrapper_hash == expected_wrapper_hash,
    }
    expected_threshold_map = expected_thresholds()
    backgrounds: dict[str, dict[str, list[float]]] = {
        str(a): {
            name: []
            for name in (
                "D",
                "H_Mpc_inverse",
                "rho_f_over_rho_r",
                "rho_ash_over_rho_r",
            )
        }
        for a in physics.A_VALUES_BACKGROUND
    }

    for mode in MODES:
        for k_mpc in K_VALUES:
            for variant in VARIANTS:
                path = result_dir / atom_name(mode, k_mpc, variant)
                data = json.loads(path.read_text(encoding="utf-8"))
                key = (mode, k_mpc, variant)
                atoms[key] = data
                label = f"{mode}:k={k_mpc}:{variant}"
                evidence[label] = {
                    "path": path.name,
                    "sha256": hash_file(path),
                    "runtime_seconds": data.get("runtime_seconds"),
                    "verdict": data.get("verdict"),
                }
                checks[f"{label}:identity"] = bool(
                    data.get("run_id") == RUN_ID
                    and data.get("mode") == mode
                    and data.get("k_Mpc_inverse") == k_mpc
                    and data.get("variant") == variant
                )
                checks[f"{label}:source_hashes"] = (
                    data.get("source_hashes") == expected_source_hashes
                )
                checks[f"{label}:wrapper_hash"] = (
                    data.get("atomic_wrapper_sha256")
                    == expected_wrapper_hash
                )
                checks[f"{label}:thresholds"] = (
                    data.get("thresholds") == expected_threshold_map
                )
                checks[f"{label}:runtime_limit"] = (
                    data.get("runtime_limit_seconds") == 4.8
                )
                checks[f"{label}:z_surfaces"] = (
                    data.get("z_surfaces") == list(physics.Z_SURFACES)
                )
                checks[f"{label}:background_a_surfaces"] = (
                    data.get("background_a_surfaces")
                    == list(physics.A_VALUES_BACKGROUND)
                )
                checks[f"{label}:scope"] = data.get("scope") == FROZEN_SCOPE
                expected_background_keys = {
                    str(a) for a in physics.A_VALUES_BACKGROUND
                }
                observed_backgrounds = data.get(
                    "background_physical_values_by_a", {}
                )
                expected_quantity_keys = {
                    "D",
                    "H_Mpc_inverse",
                    "rho_f_over_rho_r",
                    "rho_ash_over_rho_r",
                }
                checks[f"{label}:background_schema"] = bool(
                    set(observed_backgrounds) == expected_background_keys
                    and all(
                        set(quantities) == expected_quantity_keys
                        for quantities in observed_backgrounds.values()
                    )
                )
                checks[f"{label}:all_checks"] = bool(data.get("checks")) and all(
                    bool(value) for value in data.get("checks", {}).values()
                )
                checks[f"{label}:verdict"] = (
                    data.get("verdict")
                    == "PASS_M3_TCA0_SEED_CONDITIONAL_ATOM"
                )
                if variant == "nominal":
                    for a, quantities in data.get(
                        "background_physical_values_by_a", {}
                    ).items():
                        for name, value in quantities.items():
                            if a in backgrounds and name in backgrounds[a]:
                                backgrounds[a][name].append(float(value))
                deadline()

    bridges: dict[str, object] = {}
    for mode in MODES:
        for k_mpc in K_VALUES:
            nominal = atoms[(mode, k_mpc, "nominal")]["result"]
            af0 = atoms[(mode, k_mpc, "af0")]["result"]
            m3_bridge = physics._coefficient_metrics(
                _restore_series(
                    nominal["m3_primary"]["fractional_state"]
                ),
                _restore_series(af0["m3_primary"]["fractional_state"]),
            )
            f0_bridge = physics._coefficient_metrics(
                _restore_series(nominal["fuel_primary"]["state"]),
                _restore_series(af0["fuel_primary"]["state"]),
            )
            m3_extended_bridge = physics._coefficient_metrics(
                _restore_series(
                    nominal["m3_extended"]["fractional_state"]
                ),
                _restore_series(
                    af0["m3_extended"]["fractional_state"]
                ),
            )
            f0_extended_bridge = physics._coefficient_metrics(
                _restore_series(nominal["fuel_extended"]["state"]),
                _restore_series(af0["fuel_extended"]["state"]),
            )
            label = f"{mode}:k={k_mpc}:nominal_vs_af0"
            bridges[label] = {
                "M3_coefficients": m3_bridge,
                "F0_coefficients": f0_bridge,
                "M3_extended_coefficients": m3_extended_bridge,
                "F0_extended_coefficients": f0_extended_bridge,
            }
            checks[f"{label}:bridge"] = bool(
                m3_bridge["pass"]
                and f0_bridge["pass"]
                and m3_extended_bridge["pass"]
                and f0_extended_bridge["pass"]
            )
            deadline()

    background_spreads: dict[str, dict[str, float]] = {}
    expected_background_count = len(MODES) * len(K_VALUES)
    for a, quantities in backgrounds.items():
        background_spreads[a] = {}
        for name, values in quantities.items():
            spread = _spread(values)
            background_spreads[a][name] = spread
            checks[f"background:a={a}:{name}"] = bool(
                len(values) == expected_background_count
                and spread <= physics.BACKGROUND_K_TOL
            )

    technically_complete = bool(checks) and all(checks.values())
    return {
        "test": "KMPC-028 P5.3g7 M3 FULL/R-A attempt-7 atomic aggregate",
        "run_id": RUN_ID,
        "scope": FROZEN_SCOPE + "; technical aggregate of 45 immutable atoms",
        "atom_evidence": evidence,
        "nominal_vs_af0_new_solve_bridges": bridges,
        "background_physical_values_by_a": backgrounds,
        "cross_mode_and_k_background_relative_spreads": background_spreads,
        "source_hashes": expected_source_hashes,
        "wrapper_sha256": observed_wrapper_hash,
        "thresholds": expected_threshold_map,
        "checks": checks,
        "execution_status": (
            "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_NUMERICAL_AUDIT"
            if technically_complete
            else "TECHNICAL_REVIEW_REQUIRED"
        ),
        "verdict": "NONE_NOT_YET_AWARDED",
        "physics_verdict": "NONE_NOT_YET_AWARDED",
        "P5_3g7_verdict": "NOT_YET_AWARDED",
        "canonical_depth": "60/100",
        "score_effect": "NONE_UNTIL_WHOLE_G7_CLOSES",
        "release_trigger": "NONE",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
