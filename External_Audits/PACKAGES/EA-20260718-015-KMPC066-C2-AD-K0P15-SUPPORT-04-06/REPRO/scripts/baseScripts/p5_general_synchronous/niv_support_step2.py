"""Bounded NIV support step 2 for KMPC-055.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
The old depth-5 solves are regression-only; both new solves use M1 depth 6.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import time
from typing import Callable, Mapping

from . import cdi_support_ladder as step2
from . import full_ra_contract as ra_contract
from . import full_ra_m3_seed as physics
from . import niv_c1_coverage as niv1
from . import s1_collective_contract as collective_contract


RUN_ID = "KMPC-055"
MODE = "NIV"
K_MPC = 0.05
VARIANT = "nominal"
GLOBAL_GATE = "C1"
LOCAL_STEP = "NIV_SUPPORT_STEP_2"
REGRESSION_SUPPORT = (-1, 2)
CANDIDATE_SUPPORT = (-1, 4)
AUDIT_SUPPORT = (-1, 6)
LEADING_J = -1
REGRESSION_REL_TOL = 1.0e-12
REGRESSION_ABS_TOL = 1.0e-14
M1_BASELINE_DEPTH = 5
M1_AUDIT_DEPTH = 6
KMPC054 = (
    "RUN_KMPC_054_P5_3G7_NIV_C1_PRIMARY_EXTENDED_COVERAGE.json",
    "0CF322A7BA5964B78BBF9180B29FA8BBBE43A646ECEB05D444B6250568ECFB1E",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(niv1.source_hashes())
    for name in ("cdi_support_ladder.py", "niv_support_step2.py"):
        hashes[name] = sha256_file(here / name)
    return hashes


def make_deadline(limit: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(limit) or limit <= 0.0 or limit > 4.8:
        raise ValueError("KMPC-055 runtime must be in (0, 4.8] seconds")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-055 NIV support step-2 internal deadline exceeded")

    return started, deadline


def _count(support: tuple[int, int], species: int) -> int:
    return species * (support[1] - support[0] + 1)


def _valid_candidate_audit(candidate: tuple[int, int], audit: tuple[int, int]) -> bool:
    return bool(
        candidate == CANDIDATE_SUPPORT
        and audit == (candidate[0], candidate[1] + 2)
        and audit == AUDIT_SUPPORT
    )


def support_guard() -> dict[str, object]:
    spec = collective_contract.MODE_SPEC[MODE]
    supports = {
        "regression_minus1_2": REGRESSION_SUPPORT,
        "candidate_minus1_4": CANDIDATE_SUPPORT,
        "audit_minus1_6": AUDIT_SUPPORT,
    }
    counts = {
        label: {
            "powers": support[1] - support[0] + 1,
            "F0": _count(support, 2),
            "M3": _count(support, len(ra_contract.AUTHORITATIVE_STATE)),
        }
        for label, support in supports.items()
    }
    negative_fixture = (-1, 8)
    checks = {
        "contract_primary_exact_minus1_2": tuple(spec["primary"]) == REGRESSION_SUPPORT,
        "contract_extended_exact_candidate_minus1_4": tuple(spec["extended"]) == CANDIDATE_SUPPORT,
        "audit_exact_candidate_hi_plus_2": _valid_candidate_audit(CANDIDATE_SUPPORT, AUDIT_SUPPORT),
        "negative_minus1_8_rejected": not _valid_candidate_audit(CANDIDATE_SUPPORT, negative_fixture),
        "F0_counts_exact_8_12_16": [row["F0"] for row in counts.values()] == [8, 12, 16],
        "M3_counts_exact_52_78_104": [row["M3"] for row in counts.values()] == [52, 78, 104],
        "leading_j_exact_minus1": int(physics.legacy.MODE_SPECS[MODE]["leading_j"])
        == spec["leading_j"] == LEADING_J,
        "M1_depth6_covers_audit_high6": M1_AUDIT_DEPTH >= AUDIT_SUPPORT[1],
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


def _load_prerequisite(result_dir: Path) -> tuple[dict[str, object], str]:
    path = result_dir / KMPC054[0]
    observed = sha256_file(path)
    if observed != KMPC054[1]:
        raise RuntimeError("immutable KMPC-054 prerequisite hash mismatch")
    return json.loads(path.read_text(encoding="utf-8")), observed


def _standard_depth(
    depth: int, inputs: object, deadline: Callable[[], None]
) -> tuple[dict[str, dict[int, float]], dict[str, object]]:
    state_legacy, background, metadata = physics.m1_anchor.solve_standard_seed_anchored(
        MODE, K_MPC, inputs, deadline, order=depth
    )
    state = {
        target: dict(state_legacy[source])
        for target, source in physics.STATE_TO_LEGACY.items()
    }
    series = physics.legacy.Series(-4, depth + 5)
    rows = physics.legacy._standard_rows(state_legacy, background, series)
    exponents = tuple(range(-1, depth + 1))
    scale = max(
        max(abs(float(value)) for values in state.values() for value in values.values()),
        1.0e-14,
    )
    driver_max = max(
        abs(series.coef(rows[row], power))
        for row in physics.legacy.DRIVER_ROWS
        for power in exponents
    )
    holdout_max = max(
        abs(series.coef(rows[row], power))
        for row in physics.legacy.HOLDOUT_ROWS
        for power in exponents
    )
    full = {
        "depth": depth,
        "exponents": list(exponents),
        "full_vector_unknowns_expected": 11 * (depth + 2),
        "reduced_unknowns_expected": 11 * (depth + 2) - 1,
        "driver_max_absolute": float(driver_max),
        "holdout_max_absolute": float(holdout_max),
        "state_scale": float(scale),
        "driver_global_state_scaled": float(driver_max / scale),
        "holdout_global_state_scaled": float(holdout_max / scale),
        "finite": niv1._all_finite({"state": state, "metadata": metadata}),
        "solver_metadata": dict(metadata),
    }
    full["pass"] = bool(
        metadata["rank"] == metadata["unknowns"] == full["reduced_unknowns_expected"]
        and metadata["full_vector_unknowns"] == full["full_vector_unknowns_expected"]
        and metadata["hard_anchor_absolute_difference"] <= physics.ABS_FALLBACK_TOL
        and full["driver_global_state_scaled"] <= physics.DRIVER_TOL
        and full["holdout_global_state_scaled"] <= physics.DRIVER_TOL
        and full["finite"]
    )
    deadline()
    return state, full


def _solve_support(
    support: tuple[int, int],
    inputs: object,
    standard: Mapping[str, Mapping[int, float]],
    deadline: Callable[[], None],
    post_mutation_probe: Callable[[], None] | None = None,
) -> dict[str, object]:
    is_primary = support == REGRESSION_SUPPORT
    expected_f0 = _count(support, 2)
    expected_m3 = _count(support, len(ra_contract.AUTHORITATIVE_STATE))
    family = "primary" if is_primary else "extended"
    f0_registry = physics.EXPECTED_F0_PRIMARY if is_primary else physics.EXPECTED_F0_EXTENDED
    m3_registry = physics.EXPECTED_M3_PRIMARY if is_primary else physics.EXPECTED_M3_EXTENDED
    before = {"F0": int(f0_registry[MODE]), "M3": int(m3_registry[MODE])}
    during: dict[str, int] = {}
    try:
        f0_registry[MODE] = expected_f0
        m3_registry[MODE] = expected_m3
        during = {"F0": int(f0_registry[MODE]), "M3": int(m3_registry[MODE])}
        if post_mutation_probe is not None:
            post_mutation_probe()
        fuel, fuel_diag = physics._solve_fuel_zero(
            MODE, K_MPC, inputs, dict(standard), support, deadline
        )
        combined = {name: dict(values) for name, values in standard.items()}
        combined.update(fuel)
        fractional, m3_meta = physics._solve_m3(
            MODE, K_MPC, inputs, combined, support, deadline
        )
    finally:
        f0_registry[MODE] = before["F0"]
        m3_registry[MODE] = before["M3"]
    after = {"F0": int(f0_registry[MODE]), "M3": int(m3_registry[MODE])}
    m3_diag = m3_meta["diagnostics"]
    checks = {
        "shape_guard_during": during == {"F0": expected_f0, "M3": expected_m3},
        "shape_guard_restored": after == before,
        "F0_exact_shape": bool(fuel_diag["rows"] == fuel_diag["unknowns"] == expected_f0),
        "M3_exact_shape": bool(m3_diag["rows"] == m3_diag["unknowns"] == expected_m3),
        "all_coefficients_and_diagnostics_finite": niv1._all_finite(
            {"fuel": fuel, "fuel_diag": fuel_diag, "m3": fractional, "m3_diag": m3_diag}
        ),
        **step2._core_checks(fuel_diag, m3_diag),
    }
    deadline()
    return {
        "support": list(support),
        "registry_family": family,
        "expected_counts": {"F0": expected_f0, "M3": expected_m3},
        "shape_guard_adapter": {
            "before": before, "during": during, "after": after, "restored": after == before
        },
        "fuel": {"state": fuel, "diagnostics": fuel_diag},
        "m3": {"fractional_state": fractional, **m3_meta},
        "checks": checks,
        "pass": all(checks.values()),
    }


def _regression_guard(
    immutable: Mapping[str, object], solved: Mapping[str, Mapping[str, object]]
) -> dict[str, object]:
    old = immutable["solve_result"]
    pairs = {
        "support_minus1_2_F0": (
            step2._restore_series(old["fuel_primary"]["state"]),
            solved["old_primary"]["fuel"]["state"],
        ),
        "support_minus1_2_M3": (
            step2._restore_series(old["m3_primary"]["fractional_state"]),
            solved["old_primary"]["m3"]["fractional_state"],
        ),
        "support_minus1_4_F0": (
            step2._restore_series(old["fuel_extended"]["state"]),
            solved["old_extended"]["fuel"]["state"],
        ),
        "support_minus1_4_M3": (
            step2._restore_series(old["m3_extended"]["fractional_state"]),
            solved["old_extended"]["m3"]["fractional_state"],
        ),
    }
    details = {label: step2._regression_metric(expected, observed) for label, (expected, observed) in pairs.items()}
    return {"details": details, "pass": all(row["pass"] for row in details.values())}


def _common_bridge(
    candidate: Mapping[str, Mapping[int, float]],
    audit: Mapping[str, Mapping[int, float]],
) -> dict[str, object]:
    expected_powers = tuple(range(LEADING_J, CANDIDATE_SUPPORT[1] + 1))
    states_equal = set(candidate) == set(audit)
    power_guard = {
        name: bool(tuple(candidate[name]) == expected_powers and all(power in audit[name] for power in expected_powers))
        for name in candidate
    }
    metrics = physics._coefficient_metrics(dict(candidate), dict(audit))
    return {
        "expected_common_powers": list(expected_powers),
        "state_sets_equal": states_equal,
        "power_guard": power_guard,
        "metrics": metrics,
        "pass": bool(states_equal and all(power_guard.values()) and metrics["pass"]),
    }


def _pure_tail(
    audit_series: Mapping[str, Mapping[int, float]], state_order: tuple[str, ...]
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
            series = audit_series[name]
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
                "base_candidate_minus1_4": base,
                "signed_added_tail_56_diagnostic": signed_added,
                "absolute_term_envelope_56_authoritative": envelope,
                "full_audit_minus1_6": full,
                "signed_over_envelope_cancellation_diagnostic": None if envelope == 0.0 else abs(signed_added) / envelope,
                "branch": branch, "metric": metric, "pass": passed,
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
        "expected_added_powers": [5, 6],
        "authoritative_metric": "sum(abs(c_j)*z**j) for j=5,6",
        "signed_tail_role": "DIAGNOSTIC_ONLY",
        "by_z": by_z,
        "all_finite": all_finite,
        "pass": bool(all_pass and all_finite and added_powers == (5, 6)),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = make_deadline(max_runtime_seconds)
    guard = support_guard()
    immutable, immutable_hash = _load_prerequisite(result_dir)
    registry_before = {
        "F0_primary": dict(physics.EXPECTED_F0_PRIMARY),
        "F0_extended": dict(physics.EXPECTED_F0_EXTENDED),
        "M3_primary": dict(physics.EXPECTED_M3_PRIMARY),
        "M3_extended": dict(physics.EXPECTED_M3_EXTENDED),
    }

    class ExpectedProbe(RuntimeError):
        pass

    def raise_after_mutation() -> None:
        raise ExpectedProbe("deterministic NIV registry-restoration probe")

    probe_caught = False
    try:
        _solve_support(AUDIT_SUPPORT, physics._variant_inputs(VARIANT), {}, deadline, raise_after_mutation)
    except ExpectedProbe:
        probe_caught = True
    registry_after = {
        "F0_primary": dict(physics.EXPECTED_F0_PRIMARY),
        "F0_extended": dict(physics.EXPECTED_F0_EXTENDED),
        "M3_primary": dict(physics.EXPECTED_M3_PRIMARY),
        "M3_extended": dict(physics.EXPECTED_M3_EXTENDED),
    }
    checks = {
        "support_guard": bool(guard["pass"]),
        "immutable_KMPC054_hash": immutable_hash == KMPC054[1],
        "immutable_KMPC054_identity": immutable["identity"] == {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT},
        "immutable_KMPC054_candidate": immutable["candidate_interpretation_not_verdict"] == "REVIEW_NIV_C1_SUPPORT_EXTENSION_REQUIRED",
        "registry_probe_exception_caught": probe_caught,
        "all_shape_registries_restored_after_exception": registry_after == registry_before,
        "JSON_scalar_fixture": True,
    }
    deadline()
    return {"run_id": RUN_ID, "mode": "SMOKE_NO_RESULT_FILE", "checks": checks, "passed": all(checks.values())}


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = make_deadline(max_runtime_seconds)
    guard = support_guard()
    immutable, immutable_hash = _load_prerequisite(result_dir)
    frozen_contract = physics.validate_frozen_contract()
    independent_contract = ra_contract.validate_contract(
        collective_contract.EXPECTED_STATE, collective_contract.EXPECTED_DRIVER, collective_contract.EXPECTED_HOLDOUT
    )
    frozen_b1 = physics.b1_guard.build_contract_guard(max_runtime_seconds=min(1.0, max_runtime_seconds))
    tca0 = physics.production_tca0_reduction_guard()
    inputs = physics._variant_inputs(VARIANT)
    standard5, standard5_meta = physics._standard_state(MODE, K_MPC, inputs, deadline)
    old_solved = {
        "old_primary": _solve_support(REGRESSION_SUPPORT, inputs, standard5, deadline),
        "old_extended": _solve_support(CANDIDATE_SUPPORT, inputs, standard5, deadline),
    }
    regression = _regression_guard(immutable, old_solved)
    standard6, standard6_meta = _standard_depth(M1_AUDIT_DEPTH, inputs, deadline)
    solved = {
        "candidate_minus1_4": _solve_support(CANDIDATE_SUPPORT, inputs, standard6, deadline),
        "audit_minus1_6": _solve_support(AUDIT_SUPPORT, inputs, standard6, deadline),
    }
    common = {
        "F0": _common_bridge(solved["candidate_minus1_4"]["fuel"]["state"], solved["audit_minus1_6"]["fuel"]["state"]),
        "M3": _common_bridge(solved["candidate_minus1_4"]["m3"]["fractional_state"], solved["audit_minus1_6"]["m3"]["fractional_state"]),
    }
    common_pass = all(row["pass"] for row in common.values())
    tails = {
        "F0": _pure_tail(solved["audit_minus1_6"]["fuel"]["state"], tuple(sorted(solved["audit_minus1_6"]["fuel"]["state"]))),
        "M3": _pure_tail(solved["audit_minus1_6"]["m3"]["fractional_state"], tuple(ra_contract.AUTHORITATIVE_STATE)),
    }
    tail_pass = all(row["pass"] for row in tails.values())
    s_c0_guard = step2.c1._s_c0_actual_coefficient_guard({
        "m3_primary": {"fractional_state": solved["candidate_minus1_4"]["m3"]["fractional_state"]},
        "m3_extended": {"fractional_state": solved["audit_minus1_6"]["m3"]["fractional_state"]},
    })
    rfs_guard = niv1._combined_rfs_guard(standard6, inputs)
    depth_bridge = physics._coefficient_metrics(
        {name: {power: value for power, value in values.items() if power <= M1_BASELINE_DEPTH} for name, values in standard5.items()},
        {name: {power: value for power, value in values.items() if power <= M1_BASELINE_DEPTH} for name, values in standard6.items()},
    )
    core_checks = {
        "support_guard": bool(guard["pass"]),
        "immutable_KMPC054_hash": immutable_hash == KMPC054[1],
        "frozen_RA_contract": bool(frozen_contract["valid"]),
        "independent_RA_contract": bool(independent_contract.valid),
        "frozen_B1_left_null_Bianchi": frozen_b1["execution_verdict"] == "PASS_R_A_B1_CONTRACT_GUARD_ONLY",
        "production_TCA0_bridge": bool(tca0["pass"]),
        "M1_standard_depth5_regression_source": bool(standard5_meta["pass"]),
        "M1_standard_depth6": bool(standard6_meta["pass"]),
        "candidate_minus1_4_core": bool(solved["candidate_minus1_4"]["pass"]),
        "audit_minus1_6_core": bool(solved["audit_minus1_6"]["pass"]),
        "NIV_combined_R_fs_compensation_depth6": bool(rfs_guard["pass"]),
        "conditional_S_C0_actual_minus1_4_minus1_6": bool(s_c0_guard["pass"]),
        "all_solve_common_and_tail_fields_finite": niv1._all_finite({"solved": solved, "common": common, "tails": tails}),
    }
    core_pass = all(core_checks.values())
    if not regression["pass"]:
        candidate = "REVIEW_NIV_SUPPORT_STEP_2_REGRESSION_OR_FORMULA_DRIFT"
    elif not core_pass:
        candidate = "REVIEW_NIV_SUPPORT_STEP_2_CORE_GATE_UNCLOSED"
    elif not common_pass:
        candidate = "REVIEW_NIV_SUPPORT_STEP_2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED"
    elif not tail_pass:
        candidate = "REVIEW_NIV_SUPPORT_STEP_2_SUPPORT_MINUS1_4_REMAINDER_UNCLOSED"
    else:
        candidate = "PASS_NIV_SUPPORT_STEP_2_SUPPORT_MINUS1_4_ADEQUATE_CANDIDATE_ONLY"
    deadline()
    payload = {
        "test": "A2-K4 P5.3g7 GLOBAL_C1 NIV_SUPPORT_STEP_2 [-1,4] to [-1,6] with M1 depth 6",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
        "identity": {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT},
        "gate_identity": {"global_gate": GLOBAL_GATE, "local_step": LOCAL_STEP},
        "scope": {
            "included": "NIV depth5 immutable regression [-1,2]/[-1,4]; depth6 candidate [-1,4], audit [-1,6], common -1..4, tail 5,6",
            "excluded": "[-1,8], NID state/correction transfer, other k/variants, S-M, full hierarchy, ODE, P5.4, G8/G9, CLASS/CMB/BBN/S8/H0",
        },
        "support_guard": guard,
        "immutable_KMPC054": {"file": KMPC054[0], "sha256": immutable_hash},
        "frozen_contract": frozen_contract,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "M1_depth5_metadata": standard5_meta,
        "M1_depth6_metadata": standard6_meta,
        "M1_depth5_to_depth6_common_diagnostic": depth_bridge,
        "NIV_combined_R_fs_compensation_depth6_guard": rfs_guard,
        "depth5_regression_solved_supports": old_solved,
        "regression_against_KMPC054": regression,
        "depth6_solved_supports": solved,
        "common_coefficient_bridges_minus1_4_minus1_6": common,
        "common_coefficient_pass": common_pass,
        "pure_added_tails_56": tails,
        "pure_tail_pass": tail_pass,
        "conditional_S_C0_guard_minus1_4_minus1_6": s_c0_guard,
        "core_checks": core_checks,
        "core_pass": core_pass,
        "source_hashes": source_hashes(),
        "thresholds": {
            "regression_relative": REGRESSION_REL_TOL,
            "regression_absolute": REGRESSION_ABS_TOL,
            "common_relative": physics.LOW_COEFFICIENT_TOL,
            "tail_relative": physics.TAIL_TOL,
            "absolute_fallback_norm": physics.ABS_FALLBACK_NORM,
            "absolute_fallback": physics.ABS_FALLBACK_TOL,
        },
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE", "release_trigger": "NONE", "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE", "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not niv1._all_finite(payload):
        raise FloatingPointError("non-finite value in final KMPC-055 payload")
    return payload

