"""KMPC-034 CDI C1 primary/extended coverage over frozen R-A physics.

The module introduces no physical equation.  It runs the existing CDI
primary [0,1] and extended [0,3] solves, separates invariant core gates from
legacy mixed-coefficient truncation, and evaluates a pure added-power tail.
"""

from __future__ import annotations

import hashlib
import math
from pathlib import Path
import time
from typing import Callable, Mapping

import numpy as np

from . import full_ra_contract as ra_contract
from . import full_ra_m3_seed as physics
from . import s1_collective_contract as collective_contract
from . import s_c0_coefficient_passport as s_c0_v1
from . import s_c0_coefficient_passport_v2_numpy_scalar as s_c0_v2


RUN_ID = "KMPC-034"
OUTPUT_NAME = "RUN_KMPC_034_P5_3G7_CDI_C1_PRIMARY_EXTENDED_COVERAGE.json"
FAILURE_NAME = "RUN_KMPC_034_P5_3G7_CDI_C1_PRIMARY_EXTENDED_COVERAGE_TECHNICAL_FAILURE.json"
MODE = "CDI"
K_MPC = 0.05
VARIANT = "nominal"
PRIMARY = (0, 1)
EXTENDED = (0, 3)
LEADING_J = 1
S_C0_RESULT = (
    "RUN_KMPC_033_P5_3G7_S_C0_COEFFICIENT_PASSPORT_RERUN1.json",
    "4CED9D48FD9866113739580E20F69E8122D70204E37C055251C8A49B3E0CFE8C",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(physics.source_hashes())
    for name in (
        "s1_collective_contract.py",
        "s_c0_coefficient_passport.py",
        "s_c0_coefficient_passport_v2_numpy_scalar.py",
        "cdi_c1_coverage.py",
    ):
        hashes[name] = sha256_file(here / name)
    return hashes


def make_deadline(max_runtime_seconds: float) -> tuple[float, Callable[[], None]]:
    if not 0.0 < max_runtime_seconds <= 4.8:
        raise ValueError("internal runtime must be in (0, 4.8] seconds")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("KMPC-034 CDI C1 internal deadline exceeded")

    return started, deadline


def _support_guard() -> dict[str, object]:
    spec = collective_contract.MODE_SPEC[MODE]
    implementation_primary = tuple(physics.MODE_SUPPORT[MODE])
    implementation_extended = (
        implementation_primary[0], implementation_primary[1] + 2
    )
    primary_powers = implementation_primary[1] - implementation_primary[0] + 1
    extended_powers = implementation_extended[1] - implementation_extended[0] + 1
    derived = {
        "primary": implementation_primary,
        "extended": implementation_extended,
        "leading_j": int(physics.legacy.MODE_SPECS[MODE]["leading_j"]),
        "primary_power_count": primary_powers,
        "extended_power_count": extended_powers,
        "f0_primary": 2 * primary_powers,
        "f0_extended": 2 * extended_powers,
        "m3_primary": len(ra_contract.AUTHORITATIVE_STATE) * primary_powers,
        "m3_extended": len(ra_contract.AUTHORITATIVE_STATE) * extended_powers,
    }
    checks = {
        "contract_primary_equals_preregistered": tuple(spec["primary"]) == PRIMARY,
        "implementation_primary_equals_contract": implementation_primary == tuple(spec["primary"]),
        "derived_extended_equals_preregistered": implementation_extended == EXTENDED,
        "derived_extended_equals_contract": implementation_extended == tuple(spec["extended"]),
        "leading_j_equals_contract": derived["leading_j"] == spec["leading_j"] == LEADING_J,
        "derived_F0_primary_equals_contract_and_implementation": (
            derived["f0_primary"] == spec["f0_primary"] == physics.EXPECTED_F0_PRIMARY[MODE]
        ),
        "derived_F0_extended_equals_contract_and_implementation": (
            derived["f0_extended"] == spec["f0_extended"] == physics.EXPECTED_F0_EXTENDED[MODE]
        ),
        "derived_M3_primary_equals_contract_and_implementation": (
            derived["m3_primary"] == spec["m3_primary"] == physics.EXPECTED_M3_PRIMARY[MODE]
        ),
        "derived_M3_extended_equals_contract_and_implementation": (
            derived["m3_extended"] == spec["m3_extended"] == physics.EXPECTED_M3_EXTENDED[MODE]
        ),
    }
    return {"derived": derived, "checks": checks, "pass": all(checks.values())}


def _all_finite(value: object) -> bool:
    if isinstance(value, Mapping):
        return all(_all_finite(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return all(_all_finite(item) for item in value)
    if isinstance(value, (float, np.floating)):
        return math.isfinite(float(value))
    return True


def _diagnostic_core(result: Mapping[str, object]) -> dict[str, object]:
    fuel_primary = result["fuel_primary"]["diagnostics"]
    fuel_extended = result["fuel_extended"]["diagnostics"]
    m3_primary = result["m3_primary"]["diagnostics"]
    m3_extended = result["m3_extended"]["diagnostics"]
    checks = {
        "fuel_primary_rank_driver_leading": bool(
            fuel_primary["pass_rank"]
            and fuel_primary["pass_driver"]
            and fuel_primary["pass_leading_postcheck"]
        ),
        "fuel_extended_rank_driver_leading": bool(
            fuel_extended["pass_rank"]
            and fuel_extended["pass_driver"]
            and fuel_extended["pass_leading_postcheck"]
        ),
        "m3_primary_rank_driver": bool(m3_primary["pass_rank"] and m3_primary["pass_driver"]),
        "m3_extended_rank_driver": bool(m3_extended["pass_rank"] and m3_extended["pass_driver"]),
        "m3_primary_independent_holdout": bool(m3_primary["holdout"]["pass_holdout"]),
        "m3_extended_independent_holdout": bool(m3_extended["holdout"]["pass_holdout"]),
        "m3_primary_forbidden_layers": bool(
            m3_primary["pass_forbidden_layers"] and m3_primary["pass_forbidden_stress_guard"]
        ),
        "m3_extended_forbidden_layers": bool(
            m3_extended["pass_forbidden_layers"] and m3_extended["pass_forbidden_stress_guard"]
        ),
        "m3_primary_production_contract": bool(m3_primary["pass_production_contract"]),
        "m3_extended_production_contract": bool(m3_extended["pass_production_contract"]),
        "m3_primary_Uc_lower_regular": (
            float(m3_primary["Uc_lower_regular_max_abs"]) <= physics.LEADING_TOL
        ),
        "m3_extended_Uc_lower_regular": (
            float(m3_extended["Uc_lower_regular_max_abs"]) <= physics.LEADING_TOL
        ),
        "all_result_fields_finite": _all_finite(result),
    }
    return {"checks": checks, "pass": all(checks.values())}


def _s_c0_actual_coefficient_guard(result: Mapping[str, object]) -> dict[str, object]:
    weights = s_c0_v1.exact_radiation_weights()
    details: dict[str, object] = {}
    passed = True
    for label in ("m3_primary", "m3_extended"):
        fractional = result[label]["fractional_state"]
        by_moment: dict[str, object] = {}
        for state_name, moment in collective_contract.STATE_TO_MOMENT.items():
            residuals: dict[str, object] = {}
            for power, raw in sorted(fractional[state_name].items()):
                residual = s_c0_v1._lift_residual(s_c0_v2.corrected_q(raw), weights)
                zero = all(value == 0 for value in residual.values())
                passed = passed and zero
                residuals[str(power)] = {
                    "pass": zero,
                    "residuals": {name: str(value) for name, value in residual.items()},
                }
            by_moment[moment] = residuals
        details[label] = by_moment
    return {"weights": {name: str(value) for name, value in weights.items()}, "details": details, "pass": passed}


def _pure_added_tail(fractional_extended: Mapping[str, Mapping[int, float]]) -> dict[str, object]:
    added_powers = tuple(range(PRIMARY[1] + 1, EXTENDED[1] + 1))
    expected_added = (2, 3)
    by_z: dict[str, object] = {}
    all_pass = True
    all_finite = True
    for z in physics.Z_SURFACES:
        rows: dict[str, object] = {}
        relative: list[tuple[float, str]] = []
        absolute: list[tuple[float, str]] = []
        for name in ra_contract.AUTHORITATIVE_STATE:
            series = fractional_extended[name]
            base = math.fsum(float(series.get(power, 0.0)) * z**power for power in range(LEADING_J, PRIMARY[1] + 1))
            added = math.fsum(float(series.get(power, 0.0)) * z**power for power in added_powers)
            full = base + added
            finite = all(math.isfinite(value) for value in (base, added, full))
            all_finite = all_finite and finite
            scale = max(abs(base), abs(full))
            if scale > physics.ABS_FALLBACK_NORM:
                branch = "relative"
                metric = abs(added) / scale
                passed = finite and metric <= physics.TAIL_TOL
                relative.append((metric, name))
            else:
                branch = "absolute"
                metric = abs(added)
                passed = finite and metric <= physics.ABS_FALLBACK_TOL
                absolute.append((metric, name))
            all_pass = all_pass and passed
            rows[name] = {
                "base_common_extended_coefficients": base,
                "pure_added_tail": added,
                "full_base_plus_added": full,
                "branch": branch,
                "metric": metric,
                "pass": passed,
            }
        worst_relative = max(relative, default=(0.0, "none"))
        worst_absolute = max(absolute, default=(0.0, "none"))
        by_z[str(z)] = {
            "states": rows,
            "worst_relative": {"value": worst_relative[0], "state": worst_relative[1]},
            "worst_absolute": {"value": worst_absolute[0], "state": worst_absolute[1]},
            "pass": all(item["pass"] for item in rows.values()),
        }
    return {
        "method": "extended coefficients only; common coefficient drift excluded",
        "base_powers": [LEADING_J, PRIMARY[1]],
        "added_powers": list(added_powers),
        "expected_added_powers": list(expected_added),
        "added_power_membership_pass": added_powers == expected_added,
        "by_z": by_z,
        "all_finite": all_finite,
        "pass": bool(all_pass and all_finite and added_powers == expected_added),
    }


def run_smoke(max_runtime_seconds: float) -> dict[str, object]:
    _, deadline = make_deadline(max_runtime_seconds)
    guard = _support_guard()
    candidate = collective_contract.canonical_candidate()
    wrong = collective_contract.canonical_candidate()
    wrong["mode_spec"][MODE]["extended"] = (0, 4)
    wrong_result = collective_contract.validate_candidate(wrong)
    deadline()
    checks = {
        "support_count_derivation": bool(guard["pass"]),
        "canonical_collective_contract": collective_contract.validate_candidate(candidate).valid,
        "wrong_CDI_extended_support_rejected": not wrong_result.valid,
        "fixed_identity": MODE == "CDI" and K_MPC == 0.05 and VARIANT == "nominal",
    }
    return {"run_id": RUN_ID, "mode": "SMOKE_NO_RESULT_FILE", "checks": checks, "passed": all(checks.values())}


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = make_deadline(max_runtime_seconds)
    support_guard = _support_guard()
    s_c0_path = result_dir / S_C0_RESULT[0]
    observed_s_c0_hash = sha256_file(s_c0_path)
    if observed_s_c0_hash != S_C0_RESULT[1]:
        raise RuntimeError("immutable KMPC-033 S-C0 passport hash mismatch")

    frozen_contract = physics.validate_frozen_contract()
    independent_contract = ra_contract.validate_contract(
        collective_contract.EXPECTED_STATE,
        collective_contract.EXPECTED_DRIVER,
        collective_contract.EXPECTED_HOLDOUT,
    )
    frozen_b1 = physics.b1_guard.build_contract_guard(
        max_runtime_seconds=min(1.0, max_runtime_seconds)
    )
    tca0 = physics.production_tca0_reduction_guard()
    deadline()

    inputs = physics._variant_inputs(VARIANT)
    standard, standard_meta = physics._standard_state(MODE, K_MPC, inputs, deadline)
    result = physics._single_variant(MODE, K_MPC, VARIANT, standard, deadline)
    deadline()

    core = _diagnostic_core(result)
    s_c0_guard = _s_c0_actual_coefficient_guard(result)
    pure_tail = _pure_added_tail(result["m3_extended"]["fractional_state"])
    common_coefficient_bridge = result["truncation"]["common_low_coefficients"]
    core_checks = {
        "support_count_guard": bool(support_guard["pass"]),
        "frozen_RA_contract": bool(frozen_contract["valid"]),
        "independent_RA_contract": bool(independent_contract.valid),
        "frozen_B1_left_null_Bianchi": (
            frozen_b1["execution_verdict"] == "PASS_R_A_B1_CONTRACT_GUARD_ONLY"
        ),
        "production_TCA0_bridge": bool(tca0["pass"]),
        "M1_standard_accepted": bool(standard_meta["pass"]),
        "CDI_core_gates": bool(core["pass"]),
        "S_C0_actual_primary_extended_lower_moments": bool(s_c0_guard["pass"]),
        "immutable_S_C0_passport_hash": observed_s_c0_hash == S_C0_RESULT[1],
    }
    core_pass = all(core_checks.values())
    common_pass = bool(common_coefficient_bridge["pass"])
    if core_pass and common_pass and pure_tail["pass"]:
        candidate = "PASS_CDI_C1_PRIMARY_EXTENDED_ATOM"
    elif core_pass and not common_pass:
        candidate = "REVIEW_CDI_C1_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED"
    elif core_pass:
        candidate = "REVIEW_CDI_C1_SUPPORT_EXTENSION_REQUIRED"
    else:
        candidate = "REVIEW_CDI_C1_CORE_GATE_UNCLOSED"
    deadline()
    return {
        "test": "A2-K4 P5.3g7 CDI C1 primary/extended coverage",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "identity": {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT},
        "scope": {
            "included": "CDI primary [0,1] versus extended [0,3] M3-TCA0 atom",
            "S_C0_role": "conditional lower-moment split guard only",
            "excluded": "BI/NID/NIV, other k/variants, S-M, full hierarchy, ODE, G8, CMB, CLASS, S8/H0",
        },
        "support_count_guard": support_guard,
        "frozen_contract": frozen_contract,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "M1_standard_metadata": standard_meta,
        "core_gate": core,
        "nominal_variant_scope": "NO_GAMMA0_OR_AF0_NULL_BRIDGE_EXECUTED_IN_C1",
        "S_C0_actual_coefficient_guard": s_c0_guard,
        "common_coefficient_bridge": common_coefficient_bridge,
        "pure_added_tail": pure_tail,
        "legacy_raw_mixed_truncation_diagnostic_only": result["truncation"],
        "solve_result": result,
        "core_checks": core_checks,
        "core_pass": core_pass,
        "common_coefficient_bridge_pass": common_pass,
        "pure_tail_pass": bool(pure_tail["pass"]),
        "source_hashes": source_hashes(),
        "S_C0_immutable_result": {"file": S_C0_RESULT[0], "sha256": observed_s_c0_hash},
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
