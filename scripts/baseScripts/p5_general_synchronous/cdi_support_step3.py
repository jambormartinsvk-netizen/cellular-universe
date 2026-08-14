"""Bounded CDI support step 3 for KMPC-040.

No physical equation or threshold is introduced here.  The module reuses the
frozen R-A solver, reconstructs the already-audited single order-7 M1
float64 correction, regresses supports [0,3] and [0,5], and audits only the
new powers 6 and 7 of support [0,7].
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

from . import cdi_support_ladder as step2
from . import full_ra_contract as ra_contract
from . import full_ra_m3_seed as physics
from . import m1_order7_provenance as provenance
from . import mode_resolved_puiseux as v1
from . import s1_collective_contract as collective_contract


RUN_ID = "KMPC-040"
OUTPUT_NAME = "RUN_KMPC_040_P5_3G7_CDI_SUPPORT_STEP_3_05_07.json"
FAILURE_NAME = "RUN_KMPC_040_P5_3G7_CDI_SUPPORT_STEP_3_05_07_TECHNICAL_FAILURE.json"
MODE = "CDI"
K_MPC = 0.05
VARIANT = "nominal"
GLOBAL_GATE = "C1"
LOCAL_STEP = "CDI_SUPPORT_STEP_3"
REGRESSION_SUPPORTS = ((0, 3), (0, 5))
CANDIDATE_SUPPORT = (0, 5)
AUDIT_SUPPORT = (0, 7)
LEADING_J = 1
CORRECTION_ABS_MAX = 1.0e-14
REGRESSION_REL_TOL = 1.0e-12
REGRESSION_ABS_TOL = 1.0e-14
KMPC035 = (
    "RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json",
    "A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01",
)
KMPC036 = (
    "RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json",
    "39BB388669E74C9368BD823C5FF5C68A487B7FC1CD4F74EACBF64D9A08B7B497",
)
KMPC039 = (
    "RUN_KMPC_039_P5_3G7_M1_ORDER7_CONTEXT_OWNER.json",
    "BDF3317235FEDEA23EDF8C23563423014F2E98A461C6E638C474DF94471CE016",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(step2.source_hashes())
    for name in (
        "m1_order7_provenance.py",
        "cdi_support_step3.py",
    ):
        hashes[name] = sha256_file(here / name)
    return hashes


def make_deadline(limit: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(limit) or limit <= 0.0 or limit > 4.8:
        raise ValueError("KMPC-040 runtime must be in (0, 4.8] seconds")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-040 CDI support step-3 internal deadline exceeded")

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


def _count(support: tuple[int, int], species: int) -> int:
    return species * (support[1] - support[0] + 1)


def _valid_candidate_audit(
    candidate: tuple[int, int], audit: tuple[int, int]
) -> bool:
    return bool(
        candidate == CANDIDATE_SUPPORT
        and audit == (candidate[0], candidate[1] + 2)
        and audit == AUDIT_SUPPORT
    )


def support_guard() -> dict[str, object]:
    supports = {
        "regression_03": REGRESSION_SUPPORTS[0],
        "regression_candidate_05": REGRESSION_SUPPORTS[1],
        "audit_07": AUDIT_SUPPORT,
    }
    counts = {
        label: {
            "powers": support[1] - support[0] + 1,
            "F0": _count(support, 2),
            "M3": _count(support, len(ra_contract.AUTHORITATIVE_STATE)),
        }
        for label, support in supports.items()
    }
    negative_fixture = (0, 9)
    checks = {
        "regression_supports_exact_03_05": REGRESSION_SUPPORTS == ((0, 3), (0, 5)),
        "candidate_exact_05": CANDIDATE_SUPPORT == (0, 5),
        "audit_exact_candidate_hi_plus_2": _valid_candidate_audit(
            CANDIDATE_SUPPORT, AUDIT_SUPPORT
        ),
        "negative_09_rejected": not _valid_candidate_audit(
            CANDIDATE_SUPPORT, negative_fixture
        ),
        "F0_counts_exact_8_12_16": [row["F0"] for row in counts.values()]
        == [8, 12, 16],
        "M3_counts_exact_52_78_104": [row["M3"] for row in counts.values()]
        == [52, 78, 104],
        "leading_j_exact_1": int(physics.legacy.MODE_SPECS[MODE]["leading_j"])
        == LEADING_J,
        "surfaces_exact": tuple(physics.Z_SURFACES) == (1.0e-4, 1.0e-2),
        "thresholds_exact": bool(
            physics.LOW_COEFFICIENT_TOL == 1.0e-8
            and physics.TAIL_TOL == 1.0e-6
            and physics.ABS_FALLBACK_NORM == 1.0e-12
            and physics.ABS_FALLBACK_TOL == 1.0e-12
            and REGRESSION_REL_TOL == 1.0e-12
            and REGRESSION_ABS_TOL == 1.0e-14
        ),
    }
    return {
        "supports": {name: list(value) for name, value in supports.items()},
        "counts": counts,
        "negative_fixture": list(negative_fixture),
        "checks": checks,
        "pass": all(checks.values()),
    }


def _load_prerequisite(
    result_dir: Path, expected: tuple[str, str]
) -> tuple[dict[str, object], str]:
    path = result_dir / expected[0]
    observed = sha256_file(path)
    if observed != expected[1]:
        raise RuntimeError(f"immutable prerequisite hash mismatch: {expected[0]}")
    return json.loads(path.read_text(encoding="utf-8")), observed


def _state_from_json(
    raw: Mapping[str, Mapping[str, object]],
) -> dict[str, dict[int, float]]:
    powers = tuple(range(-1, 8))
    if set(raw) != set(v1.VARS):
        raise ValueError("immutable KMPC-036 M1 state registry mismatch")
    restored: dict[str, dict[int, float]] = {}
    for name in v1.VARS:
        if set(raw[name]) != {str(power) for power in powers}:
            raise ValueError(f"immutable KMPC-036 power registry mismatch for {name}")
        restored[name] = {power: float(raw[name][str(power)]) for power in powers}
    return restored


def _unpack_vector(
    vector: np.ndarray, pairs: tuple[tuple[str, int], ...]
) -> dict[str, dict[int, float]]:
    return {
        name: {
            power: float(vector[position])
            for position, (state, power) in enumerate(pairs)
            if state == name
        }
        for name in v1.VARS
    }


def _refined_m1_order7(
    result_dir: Path, deadline: Callable[[], None]
) -> tuple[dict[str, dict[int, float]], dict[str, object]]:
    reference, hash036 = _load_prerequisite(result_dir, KMPC036)
    closure, hash039 = _load_prerequisite(result_dir, KMPC039)
    reference_state = _state_from_json(reference["M1_order7_state"])
    inputs = v1.FrozenInputs()
    system = provenance._affine_system(7, inputs, deadline)
    full_matrix = system["driver_matrix"]
    full_constant = system["driver_constant"]
    anchor_index = int(system["anchor_index"])
    anchor_value = float(system["anchor_value"])
    reduced_matrix = np.delete(full_matrix, anchor_index, axis=1)
    reference_vector = provenance._vector_from_state(reference_state, system["pairs"])
    reference_reduced = np.delete(reference_vector, anchor_index)
    right_hand_side = (
        -full_constant - full_matrix[:, anchor_index] * anchor_value
    )
    residual = reduced_matrix @ reference_reduced - right_hand_side
    correction, _, correction_rank, correction_singular = np.linalg.lstsq(
        reduced_matrix, -residual, rcond=None
    )
    refined_reduced = reference_reduced + correction
    refined_full = np.empty(full_matrix.shape[1], dtype=float)
    refined_full[anchor_index] = anchor_value
    refined_full[np.arange(full_matrix.shape[1]) != anchor_index] = refined_reduced
    refined_state = _unpack_vector(refined_full, system["pairs"])
    driver = provenance._residual_metrics(
        full_matrix, full_constant, refined_full, system["driver_labels"]
    )
    holdout = provenance._residual_metrics(
        system["holdout_matrix"],
        system["holdout_constant"],
        refined_full,
        system["holdout_labels"],
    )
    lower = provenance._hybrid_regression(
        reference_state, refined_state, tuple(range(-1, 6))
    )
    correction_max = float(np.max(np.abs(correction)))
    expected_v2 = closure["v2_single_bounded_refinement"]
    correction_regression = math.isclose(
        correction_max,
        float(expected_v2["correction_max_abs"]),
        rel_tol=REGRESSION_REL_TOL,
        abs_tol=REGRESSION_ABS_TOL * 1.0e-2,
    )
    checks = {
        "KMPC036_identity": reference["identity"]
        == {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT, "order": 7},
        "KMPC039_candidate_closed": closure["candidate_interpretation_not_verdict"]
        == "PASS_M1_ORDER7_FLOAT64_SOLVER_FLOOR_CANDIDATE_ONLY",
        "KMPC039_v2_bounds_pass": bool(expected_v2["bounds_pass"]),
        "matrix_shapes_exact": bool(
            list(full_matrix.shape) == [121, 99]
            and list(reduced_matrix.shape) == [121, 98]
            and list(system["holdout_matrix"].shape) == [18, 99]
        ),
        "rank_exact_98": int(correction_rank) == 98,
        "one_correction_within_cap": correction_max <= CORRECTION_ABS_MAX,
        "correction_reproduces_KMPC039": correction_regression,
        "anchor_exact": bool(
            system["pairs"][anchor_index] == ("h", 1)
            and refined_full[anchor_index] == anchor_value
        ),
        "driver_initial_121_pass": bool(driver["row_count"] == 121 and driver["pass"]),
        "holdout_18_pass": bool(holdout["row_count"] == 18 and holdout["pass"]),
        "lower_minus1_through5_regression": bool(lower["pass"]),
        "finite": _all_finite(
            {"state": refined_state, "driver": driver, "holdout": holdout, "lower": lower}
        ),
    }
    standard = {
        target: dict(refined_state[source])
        for target, source in physics.STATE_TO_LEGACY.items()
    }
    metadata = {
        "method": "one deterministic float64 least-squares residual correction on frozen KMPC-036 matrix",
        "immutable_prerequisites": {
            "KMPC036": {"file": KMPC036[0], "sha256": hash036},
            "KMPC039": {"file": KMPC039[0], "sha256": hash039},
        },
        "dimensions": {
            "full": list(full_matrix.shape),
            "reduced": list(reduced_matrix.shape),
            "holdout": list(system["holdout_matrix"].shape),
        },
        "correction_count": 1,
        "correction_max_abs": correction_max,
        "correction_cap": CORRECTION_ABS_MAX,
        "correction_rank": int(correction_rank),
        "correction_singular_max": float(correction_singular[0]),
        "correction_singular_min_resolved": float(correction_singular[-1]),
        "driver_and_initial": {
            "row_count": driver["row_count"],
            "worst": driver["worst"],
            "pass": driver["pass"],
        },
        "holdout": {
            "row_count": holdout["row_count"],
            "worst": holdout["worst"],
            "pass": holdout["pass"],
        },
        "lower_regression": {"worst": lower["worst"], "pass": lower["pass"]},
        "checks": checks,
        "pass": all(checks.values()),
    }
    deadline()
    return standard, metadata


def _regression_guard(
    immutable: Mapping[str, object], solved: Mapping[str, Mapping[str, object]]
) -> dict[str, object]:
    expected_solved = immutable["solved_supports"]
    pairs = {
        "support_03_F0": (
            step2._restore_series(expected_solved["03"]["fuel"]["state"]),
            solved["03"]["fuel"]["state"],
        ),
        "support_03_M3": (
            step2._restore_series(expected_solved["03"]["m3"]["fractional_state"]),
            solved["03"]["m3"]["fractional_state"],
        ),
        "support_05_F0": (
            step2._restore_series(expected_solved["05"]["fuel"]["state"]),
            solved["05"]["fuel"]["state"],
        ),
        "support_05_M3": (
            step2._restore_series(expected_solved["05"]["m3"]["fractional_state"]),
            solved["05"]["m3"]["fractional_state"],
        ),
    }
    details = {
        label: step2._regression_metric(expected, observed)
        for label, (expected, observed) in pairs.items()
    }
    return {"details": details, "pass": all(row["pass"] for row in details.values())}


def _common_bridge(
    candidate: Mapping[str, Mapping[int, float]],
    audit: Mapping[str, Mapping[int, float]],
) -> dict[str, object]:
    expected_powers = tuple(range(0, 6))
    state_sets_equal = set(candidate) == set(audit)
    power_sets = {
        name: bool(
            tuple(candidate[name]) == expected_powers
            and all(power in audit[name] for power in expected_powers)
        )
        for name in candidate
    }
    metrics = physics._coefficient_metrics(dict(candidate), dict(audit))
    return {
        "expected_common_powers": list(expected_powers),
        "state_sets_equal": state_sets_equal,
        "power_sets": power_sets,
        "metrics": metrics,
        "pass": bool(state_sets_equal and all(power_sets.values()) and metrics["pass"]),
    }


def _pure_tail(
    series_by_state: Mapping[str, Mapping[int, float]],
    state_order: tuple[str, ...],
) -> dict[str, object]:
    base_powers = tuple(range(LEADING_J, CANDIDATE_SUPPORT[1] + 1))
    added_powers = tuple(range(CANDIDATE_SUPPORT[1] + 1, AUDIT_SUPPORT[1] + 1))
    by_z: dict[str, object] = {}
    all_pass = True
    all_finite = True
    for z in physics.Z_SURFACES:
        states: dict[str, object] = {}
        relative: list[tuple[float, str]] = []
        absolute: list[tuple[float, str]] = []
        for name in state_order:
            series = series_by_state[name]
            base = math.fsum(float(series.get(power, 0.0)) * z**power for power in base_powers)
            signed_added = math.fsum(
                float(series.get(power, 0.0)) * z**power for power in added_powers
            )
            envelope = math.fsum(
                abs(float(series.get(power, 0.0))) * z**power for power in added_powers
            )
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
                "base_candidate_05": base,
                "signed_added_tail_67_diagnostic": signed_added,
                "absolute_term_envelope_67_authoritative": envelope,
                "full_audit_07": full,
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
        "expected_added_powers": [6, 7],
        "authoritative_metric": "sum(abs(c_j)*z**j) for j=6,7",
        "signed_tail_role": "DIAGNOSTIC_ONLY",
        "by_z": by_z,
        "all_finite": all_finite,
        "pass": bool(all_pass and all_finite and added_powers == (6, 7)),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = make_deadline(max_runtime_seconds)
    guard = support_guard()
    immutable035, hash035 = _load_prerequisite(result_dir, KMPC035)
    standard, m1_meta = _refined_m1_order7(result_dir, deadline)
    registry_before = {
        "F0_primary": dict(physics.EXPECTED_F0_PRIMARY),
        "F0_extended": dict(physics.EXPECTED_F0_EXTENDED),
        "M3_primary": dict(physics.EXPECTED_M3_PRIMARY),
        "M3_extended": dict(physics.EXPECTED_M3_EXTENDED),
    }

    class ExpectedProbe(RuntimeError):
        pass

    def raise_after_mutation() -> None:
        raise ExpectedProbe("deterministic registry-restoration probe")

    probe_caught = False
    try:
        step2._solve_support(
            AUDIT_SUPPORT,
            physics._variant_inputs(VARIANT),
            standard,
            deadline,
            post_mutation_probe=raise_after_mutation,
        )
    except ExpectedProbe:
        probe_caught = True
    registry_after = {
        "F0_primary": dict(physics.EXPECTED_F0_PRIMARY),
        "F0_extended": dict(physics.EXPECTED_F0_EXTENDED),
        "M3_primary": dict(physics.EXPECTED_M3_PRIMARY),
        "M3_extended": dict(physics.EXPECTED_M3_EXTENDED),
    }
    json.dumps({"native": 1.0, "numpy": np.float64(2.0).item(), "finite": True})
    checks = {
        "support_guard": bool(guard["pass"]),
        "immutable_KMPC035_hash": hash035 == KMPC035[1],
        "immutable_KMPC035_identity": immutable035["identity"]
        == {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT},
        "refined_M1_order7": bool(m1_meta["pass"]),
        "standard_registry_exact": tuple(standard) == tuple(physics.STATE_TO_LEGACY),
        "standard_powers_exact_minus1_through7": all(
            tuple(values) == tuple(range(-1, 8)) for values in standard.values()
        ),
        "registry_probe_exception_caught": probe_caught,
        "all_shape_registries_restored_after_exception": registry_after == registry_before,
        "JSON_scalar_fixture": True,
    }
    deadline()
    return {
        "run_id": RUN_ID,
        "mode": "SMOKE_NO_RESULT_FILE",
        "checks": checks,
        "passed": all(checks.values()),
    }


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = make_deadline(max_runtime_seconds)
    guard = support_guard()
    immutable035, hash035 = _load_prerequisite(result_dir, KMPC035)
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
    inputs = physics._variant_inputs(VARIANT)
    standard, m1_meta = _refined_m1_order7(result_dir, deadline)
    solved = {
        "03": step2._solve_support((0, 3), inputs, standard, deadline),
        "05": step2._solve_support((0, 5), inputs, standard, deadline),
        "07": step2._solve_support((0, 7), inputs, standard, deadline),
    }
    regression = _regression_guard(immutable035, solved)
    common = {
        "F0": _common_bridge(solved["05"]["fuel"]["state"], solved["07"]["fuel"]["state"]),
        "M3": _common_bridge(
            solved["05"]["m3"]["fractional_state"],
            solved["07"]["m3"]["fractional_state"],
        ),
    }
    common_pass = all(row["pass"] for row in common.values())
    tails = {
        "F0": _pure_tail(
            solved["07"]["fuel"]["state"], tuple(sorted(solved["07"]["fuel"]["state"]))
        ),
        "M3": _pure_tail(
            solved["07"]["m3"]["fractional_state"],
            tuple(ra_contract.AUTHORITATIVE_STATE),
        ),
    }
    tail_pass = all(row["pass"] for row in tails.values())
    s_c0_guard = step2.c1._s_c0_actual_coefficient_guard(
        {
            "m3_primary": {"fractional_state": solved["05"]["m3"]["fractional_state"]},
            "m3_extended": {"fractional_state": solved["07"]["m3"]["fractional_state"]},
        }
    )
    core_checks = {
        "support_guard": bool(guard["pass"]),
        "immutable_KMPC035_hash": hash035 == KMPC035[1],
        "frozen_RA_contract": bool(frozen_contract["valid"]),
        "independent_RA_contract": bool(independent_contract.valid),
        "frozen_B1_left_null_Bianchi": frozen_b1["execution_verdict"]
        == "PASS_R_A_B1_CONTRACT_GUARD_ONLY",
        "production_TCA0_bridge": bool(tca0["pass"]),
        "refined_M1_order7": bool(m1_meta["pass"]),
        "support_03_core": bool(solved["03"]["pass"]),
        "support_05_core": bool(solved["05"]["pass"]),
        "support_07_core": bool(solved["07"]["pass"]),
        "conditional_S_C0_actual_05_07": bool(s_c0_guard["pass"]),
        "all_solve_common_and_tail_fields_finite": _all_finite(
            {"solved": solved, "common": common, "tails": tails}
        ),
    }
    core_pass = all(core_checks.values())
    if not regression["pass"] or not m1_meta["pass"]:
        candidate = "REVIEW_CDI_SUPPORT_STEP_3_REGRESSION_OR_M1_PROVENANCE_UNCLOSED"
    elif not core_pass:
        candidate = "REVIEW_CDI_SUPPORT_STEP_3_CORE_GATE_UNCLOSED"
    elif not common_pass:
        candidate = "REVIEW_CDI_SUPPORT_STEP_3_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED"
    elif not tail_pass:
        candidate = "REVIEW_CDI_SUPPORT_STEP_3_SUPPORT_05_REMAINDER_UNCLOSED"
    else:
        candidate = "PASS_CDI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY"
    deadline()
    payload = {
        "test": "A2-K4 P5.3g7 GLOBAL_C1 CDI_SUPPORT_STEP_3 support [0,5] to [0,7]",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "identity": {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT},
        "gate_identity": {"global_gate": GLOBAL_GATE, "local_step": LOCAL_STEP},
        "scope": {
            "included": "CDI regression [0,3]/[0,5], candidate [0,5], audit [0,7], common 0..5, tail 6,7",
            "excluded": "[0,9], new equations/parameters/thresholds, BI/NID/NIV, other k/variants, S-M, full hierarchy, ODE, G8/G9, CLASS/CMB/BBN/S8/H0",
        },
        "support_guard": guard,
        "immutable_KMPC035": {"file": KMPC035[0], "sha256": hash035},
        "frozen_contract": frozen_contract,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "M1_order7_reconstruction": m1_meta,
        "solved_supports": solved,
        "regression_against_KMPC035": regression,
        "common_coefficient_bridges_05_07": common,
        "common_coefficient_pass": common_pass,
        "pure_added_tails_67": tails,
        "pure_tail_pass": tail_pass,
        "conditional_S_C0_guard_05_07": s_c0_guard,
        "core_checks": core_checks,
        "core_pass": core_pass,
        "source_hashes": source_hashes(),
        "thresholds": {
            "regression_relative": REGRESSION_REL_TOL,
            "regression_absolute": REGRESSION_ABS_TOL,
            "M1_correction_absolute_max": CORRECTION_ABS_MAX,
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
        raise FloatingPointError("non-finite value in final KMPC-040 payload")
    return payload
