"""Bounded NID GLOBAL_C1 primary/extended atom for KMPC-047.

No equation, parameter, support, surface, or threshold is introduced here.
The module applies the frozen R-A solver to NID only, verifies the combined
R_fs compensation, and separates common coefficients from the added tail.
"""

from __future__ import annotations

import hashlib
import json
import math
import numbers
from pathlib import Path
import time
from typing import Callable, Mapping

import numpy as np

from . import cdi_c1_coverage as shared
from . import full_ra_contract as ra_contract
from . import full_ra_m3_seed as physics
from . import s1_collective_contract as collective_contract


RUN_ID = "KMPC-047"
OUTPUT_NAME = "RUN_KMPC_047_P5_3G7_NID_C1_PRIMARY_EXTENDED_COVERAGE.json"
FAILURE_NAME = "RUN_KMPC_047_P5_3G7_NID_C1_PRIMARY_EXTENDED_COVERAGE_TECHNICAL_FAILURE.json"
MODE = "NID"
K_MPC = 0.05
VARIANT = "nominal"
PRIMARY = (0, 3)
EXTENDED = (0, 5)
LEADING_J = 0
S_C0_RESULT = (
    "RUN_KMPC_033_P5_3G7_S_C0_COEFFICIENT_PASSPORT_RERUN1.json",
    "4CED9D48FD9866113739580E20F69E8122D70204E37C055251C8A49B3E0CFE8C",
)
PREVIOUS_COVERAGE_RESULT = (
    "RUN_KMPC_046_P5_3G7_BI_SUPPORT_STEP_3_OWNER_SUCCESSOR.json",
    "60EC5A801FDDBAFFBA6CE184EBB3BC154879928385E6E37FB118781118615FB1",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(shared.source_hashes())
    hashes["nid_c1_coverage.py"] = sha256_file(here / "nid_c1_coverage.py")
    return hashes


def make_deadline(limit: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(limit) or limit <= 0.0 or limit > 4.8:
        raise ValueError("KMPC-047 runtime must be in (0, 4.8] seconds")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-047 NID C1 internal deadline exceeded")

    return started, deadline


def _all_finite(value: object) -> bool:
    if isinstance(value, Mapping):
        return all(_all_finite(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return all(_all_finite(item) for item in value)
    if isinstance(value, np.ndarray):
        return bool(np.all(np.isfinite(value)))
    if isinstance(value, np.generic):
        return _all_finite(value.item())
    if isinstance(value, numbers.Real):
        return math.isfinite(float(value))
    return True


def _support_guard() -> dict[str, object]:
    spec = collective_contract.MODE_SPEC[MODE]
    implementation_primary = tuple(physics.MODE_SUPPORT[MODE])
    implementation_extended = (implementation_primary[0], implementation_primary[1] + 2)
    primary_powers = implementation_primary[1] - implementation_primary[0] + 1
    extended_powers = implementation_extended[1] - implementation_extended[0] + 1
    derived = {
        "primary": implementation_primary,
        "extended": implementation_extended,
        "leading_j": int(physics.legacy.MODE_SPECS[MODE]["leading_j"]),
        "primary_power_count": primary_powers,
        "extended_power_count": extended_powers,
        "F0_primary": 2 * primary_powers,
        "F0_extended": 2 * extended_powers,
        "M3_primary": len(ra_contract.AUTHORITATIVE_STATE) * primary_powers,
        "M3_extended": len(ra_contract.AUTHORITATIVE_STATE) * extended_powers,
    }
    checks = {
        "contract_primary_exact_03": tuple(spec["primary"]) == PRIMARY,
        "implementation_primary_equals_contract": implementation_primary == tuple(spec["primary"]),
        "derived_extended_exact_05": implementation_extended == EXTENDED,
        "derived_extended_equals_contract": implementation_extended == tuple(spec["extended"]),
        "leading_j_exact_0": derived["leading_j"] == spec["leading_j"] == LEADING_J,
        "F0_counts_exact_8_12": bool(
            derived["F0_primary"] == spec["f0_primary"] == physics.EXPECTED_F0_PRIMARY[MODE] == 8
            and derived["F0_extended"] == spec["f0_extended"] == physics.EXPECTED_F0_EXTENDED[MODE] == 12
        ),
        "M3_counts_exact_52_78": bool(
            derived["M3_primary"] == spec["m3_primary"] == physics.EXPECTED_M3_PRIMARY[MODE] == 52
            and derived["M3_extended"] == spec["m3_extended"] == physics.EXPECTED_M3_EXTENDED[MODE] == 78
        ),
        "surfaces_exact": tuple(physics.Z_SURFACES) == (1.0e-4, 1.0e-2),
        "thresholds_exact": bool(
            physics.LOW_COEFFICIENT_TOL == 1.0e-8
            and physics.TAIL_TOL == 1.0e-6
            and physics.ABS_FALLBACK_NORM == 1.0e-12
            and physics.ABS_FALLBACK_TOL == 1.0e-12
        ),
    }
    return {"derived": derived, "checks": checks, "pass": all(checks.values())}


def _load_prerequisite(result_dir: Path, expected: tuple[str, str]) -> tuple[dict[str, object], str]:
    path = result_dir / expected[0]
    observed = sha256_file(path)
    if observed != expected[1]:
        raise RuntimeError(f"immutable prerequisite hash mismatch: {expected[0]}")
    return json.loads(path.read_text(encoding="utf-8")), observed


def _common_bridge(
    primary: Mapping[str, Mapping[int, float]],
    extended: Mapping[str, Mapping[int, float]],
) -> dict[str, object]:
    expected_powers = tuple(range(PRIMARY[0], PRIMARY[1] + 1))
    states_equal = set(primary) == set(extended)
    power_guard = {
        name: bool(
            tuple(primary[name]) == expected_powers
            and all(power in extended[name] for power in expected_powers)
        )
        for name in primary
    }
    metrics = physics._coefficient_metrics(dict(primary), dict(extended))
    return {
        "expected_common_powers": list(expected_powers),
        "state_sets_equal": states_equal,
        "power_guard": power_guard,
        "metrics": metrics,
        "pass": bool(states_equal and all(power_guard.values()) and metrics["pass"]),
    }


def _pure_added_tail(
    extended: Mapping[str, Mapping[int, float]], state_order: tuple[str, ...]
) -> dict[str, object]:
    base_powers = tuple(range(LEADING_J, PRIMARY[1] + 1))
    added_powers = tuple(range(PRIMARY[1] + 1, EXTENDED[1] + 1))
    by_z: dict[str, object] = {}
    all_pass = True
    all_finite = True
    for z in physics.Z_SURFACES:
        states: dict[str, object] = {}
        relative: list[tuple[float, str]] = []
        absolute: list[tuple[float, str]] = []
        for name in state_order:
            series = extended[name]
            base = math.fsum(float(series.get(power, 0.0)) * z**power for power in base_powers)
            signed_added = math.fsum(float(series.get(power, 0.0)) * z**power for power in added_powers)
            envelope = math.fsum(abs(float(series.get(power, 0.0))) * z**power for power in added_powers)
            full = base + signed_added
            finite = all(math.isfinite(value) for value in (base, signed_added, envelope, full))
            all_finite = all_finite and finite
            scale = max(abs(base), abs(full))
            if scale > physics.ABS_FALLBACK_NORM:
                branch = "relative"
                metric = envelope / scale
                passed = finite and metric <= physics.TAIL_TOL
                relative.append((metric, name))
            else:
                branch = "absolute"
                metric = envelope
                passed = finite and metric <= physics.ABS_FALLBACK_TOL
                absolute.append((metric, name))
            all_pass = all_pass and passed
            states[name] = {
                "base_primary_03": base,
                "signed_added_tail_45_diagnostic": signed_added,
                "absolute_term_envelope_45_authoritative": envelope,
                "full_extended_05": full,
                "signed_over_envelope_cancellation_diagnostic": (
                    None if envelope == 0.0 else abs(signed_added) / envelope
                ),
                "branch": branch,
                "metric": metric,
                "pass": passed,
            }
        worst_relative = max(relative, default=(0.0, "none"))
        worst_absolute = max(absolute, default=(0.0, "none"))
        by_z[str(z)] = {
            "states": states,
            "worst_relative": {"value": worst_relative[0], "state": worst_relative[1]},
            "worst_absolute": {"value": worst_absolute[0], "state": worst_absolute[1]},
            "pass": all(row["pass"] for row in states.values()),
        }
    return {
        "base_powers": list(base_powers),
        "added_powers": list(added_powers),
        "expected_added_powers": [4, 5],
        "authoritative_metric": "sum(abs(c_j)*z**j) for j=4,5",
        "signed_tail_role": "DIAGNOSTIC_ONLY",
        "by_z": by_z,
        "all_finite": all_finite,
        "pass": bool(all_pass and all_finite and added_powers == (4, 5)),
    }


def _combined_rfs_guard(
    standard: Mapping[str, Mapping[int, float]], inputs: object
) -> dict[str, object]:
    rg, rfs, rnu, rsteam = inputs.radiation_weights
    observed = {
        "delta_gamma_0": float(standard["delta_gamma"].get(0, 0.0)),
        "delta_fs_0": float(standard["delta_fs"].get(0, 0.0)),
        "U_gamma_0": float(standard["U_gamma"].get(0, 0.0)),
        "U_fs_0": float(standard["U_fs"].get(0, 0.0)),
        "U_b_0": float(standard["U_b"].get(0, 0.0)),
    }
    expected = {
        "delta_gamma_0": -rfs / rg,
        "delta_fs_0": 1.0,
        "U_gamma_0": -rfs / (4.0 * rg),
        "U_fs_0": 0.25,
        "U_b_0": -rfs / (4.0 * rg),
    }
    differences = {name: abs(observed[name] - value) for name, value in expected.items()}
    density_residual = rg * observed["delta_gamma_0"] + rfs * observed["delta_fs_0"]
    velocity_residual = rg * observed["U_gamma_0"] + rfs * observed["U_fs_0"]
    split_residual = rnu + rsteam - rfs
    return {
        "weights": {"R_gamma": rg, "R_fs": rfs, "R_nu": rnu, "R_steam": rsteam},
        "observed": observed,
        "expected_combined_R_fs": expected,
        "absolute_differences": differences,
        "density_compensation_residual": density_residual,
        "velocity_compensation_residual": velocity_residual,
        "R_nu_plus_R_steam_minus_R_fs": split_residual,
        "pass": bool(
            max(differences.values()) <= physics.ABS_FALLBACK_TOL
            and abs(density_residual) <= physics.STEAM_SPLIT_TOL
            and abs(velocity_residual) <= physics.STEAM_SPLIT_TOL
            and abs(split_residual) <= physics.STEAM_SPLIT_TOL
        ),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = make_deadline(max_runtime_seconds)
    guard = _support_guard()
    passport, passport_hash = _load_prerequisite(result_dir, S_C0_RESULT)
    previous, previous_hash = _load_prerequisite(result_dir, PREVIOUS_COVERAGE_RESULT)
    candidate = collective_contract.canonical_candidate()
    wrong_support = collective_contract.canonical_candidate()
    wrong_support["mode_spec"][MODE]["extended"] = (0, 6)
    wrong_weight = collective_contract.canonical_candidate()
    wrong_weight["nid_compensation_weight"] = "R_nu"
    sample = {"native": 1.0, "numpy": np.float64(2.0).item(), "finite": True}
    json.dumps(sample, allow_nan=False)
    checks = {
        "support_count_threshold_guard": bool(guard["pass"]),
        "canonical_collective_contract": collective_contract.validate_candidate(candidate).valid,
        "wrong_NID_extended_support_rejected": not collective_contract.validate_candidate(wrong_support).valid,
        "wrong_NID_R_nu_compensation_rejected": not collective_contract.validate_candidate(wrong_weight).valid,
        "fixed_identity": MODE == "NID" and K_MPC == 0.05 and VARIANT == "nominal",
        "immutable_S_C0_passport": bool(
            passport_hash == S_C0_RESULT[1]
            and passport["candidate_interpretation_not_verdict"]
            == "PASS_S_C0_LOWER_MOMENT_COEFFICIENT_LIFT_COLLAPSE_PASSPORT_ONLY"
        ),
        "immutable_previous_coverage": bool(
            previous_hash == PREVIOUS_COVERAGE_RESULT[1]
            and previous["candidate_interpretation_not_verdict"]
            == "PASS_BI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY"
        ),
        "JSON_scalar_fixture": True,
    }
    deadline()
    return {"run_id": RUN_ID, "mode": "SMOKE_NO_RESULT_FILE", "checks": checks, "passed": all(checks.values())}


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = make_deadline(max_runtime_seconds)
    support_guard = _support_guard()
    passport, passport_hash = _load_prerequisite(result_dir, S_C0_RESULT)
    previous, previous_hash = _load_prerequisite(result_dir, PREVIOUS_COVERAGE_RESULT)
    prerequisite_guard = bool(
        passport["candidate_interpretation_not_verdict"]
        == "PASS_S_C0_LOWER_MOMENT_COEFFICIENT_LIFT_COLLAPSE_PASSPORT_ONLY"
        and previous["candidate_interpretation_not_verdict"]
        == "PASS_BI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY"
    )
    frozen_contract = physics.validate_frozen_contract()
    independent_contract = ra_contract.validate_contract(
        collective_contract.EXPECTED_STATE,
        collective_contract.EXPECTED_DRIVER,
        collective_contract.EXPECTED_HOLDOUT,
    )
    frozen_b1 = physics.b1_guard.build_contract_guard(max_runtime_seconds=min(1.0, max_runtime_seconds))
    tca0 = physics.production_tca0_reduction_guard()
    inputs = physics._variant_inputs(VARIANT)
    standard, standard_meta = physics._standard_state(MODE, K_MPC, inputs, deadline)
    rfs_guard = _combined_rfs_guard(standard, inputs)
    result = physics._single_variant(MODE, K_MPC, VARIANT, standard, deadline)
    core = shared._diagnostic_core(result)
    s_c0_guard = shared._s_c0_actual_coefficient_guard(result)
    common = {
        "F0": _common_bridge(result["fuel_primary"]["state"], result["fuel_extended"]["state"]),
        "M3": _common_bridge(
            result["m3_primary"]["fractional_state"], result["m3_extended"]["fractional_state"]
        ),
    }
    common_pass = all(row["pass"] for row in common.values())
    tails = {
        "F0": _pure_added_tail(result["fuel_extended"]["state"], tuple(sorted(result["fuel_extended"]["state"]))),
        "M3": _pure_added_tail(result["m3_extended"]["fractional_state"], tuple(ra_contract.AUTHORITATIVE_STATE)),
    }
    tail_pass = all(row["pass"] for row in tails.values())
    core_checks = {
        "support_count_threshold_guard": bool(support_guard["pass"]),
        "immutable_prerequisites": prerequisite_guard,
        "frozen_RA_contract": bool(frozen_contract["valid"]),
        "independent_RA_contract": bool(independent_contract.valid),
        "frozen_B1_left_null_Bianchi": frozen_b1["execution_verdict"] == "PASS_R_A_B1_CONTRACT_GUARD_ONLY",
        "production_TCA0_bridge": bool(tca0["pass"]),
        "M1_standard_order5": bool(standard_meta["pass"]),
        "NID_combined_R_fs_compensation": bool(rfs_guard["pass"]),
        "NID_core_gates": bool(core["pass"]),
        "S_C0_actual_primary_extended_lower_moments": bool(s_c0_guard["pass"]),
        "all_common_tail_and_solve_fields_finite": _all_finite({"result": result, "common": common, "tails": tails}),
    }
    core_pass = all(core_checks.values())
    if not core_pass:
        candidate = "REVIEW_NID_C1_CORE_GATE_UNCLOSED"
    elif not common_pass:
        candidate = "REVIEW_NID_C1_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED"
    elif not tail_pass:
        candidate = "REVIEW_NID_C1_SUPPORT_EXTENSION_REQUIRED"
    else:
        candidate = "PASS_NID_C1_PRIMARY_EXTENDED_ATOM_CANDIDATE_ONLY"
    deadline()
    payload = {
        "test": "A2-K4 P5.3g7 GLOBAL_C1 NID primary [0,3] versus extended [0,5]",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
        "identity": {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT},
        "scope": {
            "included": "NID primary [0,3] versus extended [0,5], combined-R_fs compensation, F0/M3 common 0..3 and tail 4,5",
            "excluded": "NIV, other k/variants, S-M, full hierarchy, finite opacity, ODE, P5.4, G8/G9, CLASS/CMB/BBN/S8/H0",
        },
        "support_count_guard": support_guard,
        "immutable_prerequisites": {
            "S_C0": {"file": S_C0_RESULT[0], "sha256": passport_hash},
            "previous_coverage": {"file": PREVIOUS_COVERAGE_RESULT[0], "sha256": previous_hash, "role": "SEQUENTIAL_ONLY_NO_NUMERICAL_STATE_TRANSFER"},
        },
        "frozen_contract": frozen_contract,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "M1_standard_metadata": standard_meta,
        "NID_combined_R_fs_compensation_guard": rfs_guard,
        "core_gate": core,
        "S_C0_actual_coefficient_guard": s_c0_guard,
        "common_coefficient_bridges_03_05": common,
        "common_coefficient_pass": common_pass,
        "pure_added_tails_45": tails,
        "pure_tail_pass": tail_pass,
        "legacy_raw_mixed_truncation_diagnostic_only": result["truncation"],
        "solve_result": result,
        "core_checks": core_checks,
        "core_pass": core_pass,
        "source_hashes": source_hashes(),
        "thresholds": {
            "common_relative": physics.LOW_COEFFICIENT_TOL,
            "tail_relative": physics.TAIL_TOL,
            "absolute_fallback_norm": physics.ABS_FALLBACK_NORM,
            "absolute_fallback": physics.ABS_FALLBACK_TOL,
        },
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not _all_finite(payload):
        raise FloatingPointError("non-finite value in final KMPC-047 payload")
    return payload

