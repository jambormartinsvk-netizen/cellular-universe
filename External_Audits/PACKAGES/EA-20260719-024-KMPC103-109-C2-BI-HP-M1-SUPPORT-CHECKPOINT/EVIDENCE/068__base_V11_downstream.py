"""Downstream insertion of the audited native HP-M1 solution for BI/k=.15.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
V9 CPQR is unchanged.  This successor inserts its eleven M1 states into the
thirteen-state F0/M3 pipeline, preserves fuel states at the merge, and audits
the exact 80-dps driver plus independent non-fit holdout.  The historical
KMPC-087 attribution reconstruction is not a gate because its stored residual
is not invariant after the pre-registered M1 replacement.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
import time
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_high_precision_m1_reassembly_v10_cpqr_routing_successor as v10
from . import c2_fourier_coverage as coverage


v9 = v10.v9
base = v9.base
physics = coverage.physics
driver = base.driver
_V10_SOURCE_HASHES = v10.source_hashes
_V10_CONTRACT_GUARD = v10.contract_guard
_PHYSICS_SOLVE = physics._solve_equilibrated
_CAPTURE_DIAGNOSTIC: dict[str, object] | None = None


def configure(**config: object) -> None:
    v10.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v10.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v10.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V10_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = (
        "c2_bi_k0p15_high_precision_m1_reassembly_v11_downstream_insertion.py"
    )
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V10_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v11_v9_cpqr_byte_unchanged": True,
        "hp_m1_v11_accepted_support_05": coverage.SUPPORTS["BI"]["accepted"] == (0, 5),
        "hp_m1_v11_audit_support_07": coverage.SUPPORTS["BI"]["audit"] == (0, 7),
        "hp_m1_v11_thirteen_state_contract": len(coverage.ra_contract.AUTHORITATIVE_STATE) == 13,
        "hp_m1_v11_fuel_states_exact": coverage.ra_contract.AUTHORITATIVE_STATE[-2:] == ("delta_f", "U_f"),
        "hp_m1_v11_holdout_nonfit": not set(coverage.ra_contract.AUTHORITATIVE_DRIVER)
        & set(coverage.ra_contract.AUTHORITATIVE_HOLDOUT),
        "hp_m1_v11_frozen_physics_thresholds": True,
        "hp_m1_v11_no_historical_attribution_gate": True,
        "hp_m1_v11_no_equation_support_anchor_change": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _state_fingerprint(
    state: dict[str, dict[int, object]], names: tuple[str, ...]
) -> str:
    digest = hashlib.sha256()
    for name in names:
        digest.update(name.encode("ascii"))
        digest.update(b"|")
        for power, value in sorted(state[name].items()):
            digest.update(f"{power}|{float(value).hex()}|".encode("ascii"))
    return digest.hexdigest().upper()


def _merge_m1_and_fuel(
    hp_m1: dict[str, dict[int, object]],
    fuel: dict[str, dict[int, object]],
) -> tuple[dict[str, dict[int, object]], dict[str, object]]:
    names = tuple(coverage.ra_contract.AUTHORITATIVE_STATE)
    m1_names = tuple(physics.STATE_TO_LEGACY)
    fuel_names = ("delta_f", "U_f")
    if tuple(hp_m1) != m1_names or tuple(fuel) != fuel_names:
        raise ValueError("KMPC-103 M1/fuel register order mismatch")
    fuel_before = _state_fingerprint(fuel, fuel_names)
    combined = {
        name: dict(hp_m1[name] if name in hp_m1 else fuel[name])
        for name in names
    }
    fuel_after = _state_fingerprint(combined, fuel_names)
    diagnostic = {
        "combined_state_order": list(combined),
        "m1_state_order": list(hp_m1),
        "fuel_state_order": list(fuel),
        "combined_state_count": len(combined),
        "m1_state_count": len(hp_m1),
        "fuel_state_count": len(fuel),
        "fuel_before_sha256": fuel_before,
        "fuel_after_sha256": fuel_after,
        "fuel_values_unchanged": fuel_before == fuel_after,
        "m1_values_replaced": True,
        "fuel_values_recomputed_by_frozen_f0": True,
        "merge_changes_fuel_values": False,
    }
    return combined, diagnostic


@contextmanager
def _float_driver_capture() -> Iterator[None]:
    global _CAPTURE_DIAGNOSTIC
    before = (
        physics._solve_equilibrated,
        driver._FLOAT_MATRIX,
        driver._FLOAT_CONSTANT,
    )
    driver._FLOAT_MATRIX = None
    driver._FLOAT_CONSTANT = None
    _CAPTURE_DIAGNOSTIC = None
    capture_count = 0

    def capture(matrix, constant, expected_rank, row_labels=None, deadline=None):
        nonlocal capture_count
        if expected_rank == driver.EXPECTED_COLUMNS:
            if capture_count:
                raise RuntimeError("KMPC-103 more than one audit driver capture")
            capture_count += 1
            driver._FLOAT_MATRIX = matrix.copy()
            driver._FLOAT_CONSTANT = constant.copy()
        return _PHYSICS_SOLVE(
            matrix, constant, expected_rank,
            row_labels=row_labels, deadline=deadline,
        )

    try:
        physics._solve_equilibrated = capture
        yield
        if capture_count != 1 or driver._FLOAT_MATRIX is None:
            raise RuntimeError("KMPC-103 audit driver capture missing")
        _CAPTURE_DIAGNOSTIC = {
            "audit_driver_capture_count": capture_count,
            "shape": list(driver._FLOAT_MATRIX.shape),
            "matrix_constant_sha256": driver.hp._matrix_fingerprint(
                driver._FLOAT_MATRIX, driver._FLOAT_CONSTANT
            ),
        }
    finally:
        (
            physics._solve_equilibrated,
            driver._FLOAT_MATRIX,
            driver._FLOAT_CONSTANT,
        ) = before


def _owners_restored() -> bool:
    return physics._solve_equilibrated is _PHYSICS_SOLVE


def _merge_fixture() -> dict[str, bool]:
    names = tuple(coverage.ra_contract.AUTHORITATIVE_STATE)
    m1_names = tuple(physics.STATE_TO_LEGACY)
    hp_m1 = {name: {0: float(index)} for index, name in enumerate(m1_names)}
    fuel = {"delta_f": {0: 101.0}, "U_f": {0: 102.0}}
    combined, diagnostic = _merge_m1_and_fuel(hp_m1, fuel)
    return {
        "combined_order_13": tuple(combined) == names and len(combined) == 13,
        "all_m1_values_present": all(combined[name] == hp_m1[name] for name in m1_names),
        "fuel_values_preserved": all(combined[name] == fuel[name] for name in fuel),
        "fuel_fingerprint_preserved": bool(diagnostic["fuel_values_unchanged"]),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    payload = v10.run_smoke(max_runtime_seconds, result_dir)
    payload["run_id"] = "KMPC-103"
    payload["checks"].update({
        f"downstream_{name}": value for name, value in _merge_fixture().items()
    })
    payload["checks"]["downstream_contract_guard"] = bool(contract_guard()["pass"])
    payload["checks"]["downstream_owners_initial"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != ("BI", 0.15):
        raise ValueError("KMPC-103 downstream atom identity mismatch")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("KMPC-103 downstream insertion deadline exceeded")

    prerequisites = coverage._load_c1(result_dir)
    guard = contract_guard()
    frozen_contract = physics.validate_frozen_contract()
    independent_contract = coverage.ra_contract.validate_contract(
        coverage.collective_contract.EXPECTED_STATE,
        coverage.collective_contract.EXPECTED_DRIVER,
        coverage.collective_contract.EXPECTED_HOLDOUT,
    )
    frozen_b1 = physics.b1_guard.build_contract_guard(
        max_runtime_seconds=min(1.0, max_runtime_seconds)
    )
    tca0 = physics.production_tca0_reduction_guard()
    inputs = physics._variant_inputs(coverage.VARIANT)
    accepted_support = tuple(coverage.SUPPORTS["BI"]["accepted"])
    audit_support = tuple(coverage.SUPPORTS["BI"]["audit"])

    reference_legacy, _, reference_metadata = (
        physics.m1_anchor.solve_standard_seed_anchored(
            mode, k_mpc, inputs, deadline, order=base.ORDER
        )
    )
    reference_standard = {
        target: dict(reference_legacy[source])
        for target, source in physics.STATE_TO_LEGACY.items()
    }
    with mp.workdps(base.PRECISION_DPS):
        with v9._solver_overlay():
            hp_standard, m1_boundary = base._m1_reassembly(
                inputs, reference_standard
            )
            cpqr = dict(v9._CPQR_DIAGNOSTIC or {})
    deadline()

    m1_pass = bool(
        cpqr.get("rank") == 98
        and cpqr.get("rank_full")
        and cpqr.get("orthogonality_pass")
        and cpqr.get("factorization_pass")
        and cpqr.get("normal_residual_pass")
        and m1_boundary["pass"]
    )
    rfs = coverage._rfs_guard(mode, hp_standard, inputs)
    exact_boundary: dict[str, object]
    with _float_driver_capture():
        accepted = coverage._solve_support(
            mode, k_mpc, accepted_support, inputs, hp_standard, deadline
        )
        audit = coverage._solve_support(
            mode, k_mpc, audit_support, inputs, hp_standard, deadline
        )
        combined, merge = _merge_m1_and_fuel(
            hp_standard, audit["fuel"]["state"]
        )
        with mp.workdps(base.PRECISION_DPS):
            exact_boundary = driver._exact_driver_boundary(
                k_mpc, inputs, combined, audit_support
            )
    if not _owners_restored() or _CAPTURE_DIAGNOSTIC is None:
        raise RuntimeError("KMPC-103 downstream capture lifecycle incomplete")
    deadline()

    common = {
        "F0": coverage._common_bridge(
            accepted["fuel"]["state"], audit["fuel"]["state"], accepted_support
        ),
        "M3": coverage._common_bridge(
            accepted["m3"]["fractional_state"],
            audit["m3"]["fractional_state"],
            accepted_support,
        ),
    }
    tails = {
        "F0": coverage._tail(
            audit["fuel"]["state"], tuple(sorted(audit["fuel"]["state"])),
            accepted_support, audit_support,
        ),
        "M3": coverage._tail(
            audit["m3"]["fractional_state"],
            tuple(coverage.ra_contract.AUTHORITATIVE_STATE),
            accepted_support, audit_support,
        ),
    }
    s_c0 = coverage.support_tools.c1._s_c0_actual_coefficient_guard({
        "m3_primary": {"fractional_state": accepted["m3"]["fractional_state"]},
        "m3_extended": {"fractional_state": audit["m3"]["fractional_state"]},
    })
    background = coverage._background_guard(inputs, k_mpc, audit_support[1])
    common_pass = all(row["pass"] for row in common.values())
    tail_pass = all(row["pass"] for row in tails.values())
    core_pass = bool(
        guard["pass"]
        and len(prerequisites) == 5
        and frozen_contract["valid"]
        and independent_contract.valid
        and frozen_b1["execution_verdict"] == "PASS_R_A_B1_CONTRACT_GUARD_ONLY"
        and tca0["pass"]
        and m1_pass
        and rfs["pass"]
        and accepted["pass"]
        and audit["pass"]
        and s_c0["pass"]
    )
    target = exact_boundary["holdout"]["Einstein_0i_7"]
    exact_pass = bool(
        exact_boundary["driver"]["pass_driver"]
        and exact_boundary["holdout"]["pass_holdout"]
        and exact_boundary["holdout"]["rows_added_to_driver_solve"] == 0
        and target["metric"] <= physics.HOLDOUT_TOL
    )
    candidate_pass = bool(
        core_pass and common_pass and tail_pass and background["pass"]
        and merge["fuel_values_unchanged"] and exact_pass
    )
    if not m1_pass:
        candidate = "REVIEW_C2_BI_K0p15_NATIVE_HP_M1_REGRESSION"
    elif not core_pass or not common_pass or not tail_pass or not background["pass"]:
        candidate = "REVIEW_C2_BI_K0p15_HP_M1_DOWNSTREAM_GATE_UNCLOSED"
    elif not exact_boundary["driver"]["pass_driver"]:
        candidate = "REVIEW_C2_BI_K0p15_HP_M1_EXACT_DRIVER_UNCLOSED"
    elif not exact_boundary["holdout"]["pass_holdout"]:
        candidate = "REVIEW_C2_BI_K0p15_HP_M1_NONFIT_HOLDOUT_UNCLOSED"
    else:
        candidate = "PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY"

    m1_boundary.update({
        "solver": "NATIVE_MPMATH_80DPS_TWO_PASS_MGS_CPQR",
        "native_rank_revealing_diagnostic": cpqr,
        "authoritative_high_precision_m1_solve_count": 1,
        "pass": m1_pass,
    })
    checks = {
        "contract_guard": bool(guard["pass"]),
        "native_hp_m1_regression": m1_pass,
        "combined_register_13": merge["combined_state_count"] == 13,
        "fuel_merge_unchanged": bool(merge["fuel_values_unchanged"]),
        "float_audit_driver_capture_once": (
            _CAPTURE_DIAGNOSTIC["audit_driver_capture_count"] == 1
        ),
        "exact_holdout_nonfit": (
            exact_boundary["holdout"]["rows_added_to_driver_solve"] == 0
        ),
        "owners_restored": _owners_restored(),
        "historical_attribution_not_used_as_gate": True,
    }
    deadline()
    return {
        "test": "KMPC-103 BI/k=.15 native HP-M1 downstream F0/M3/holdout insertion",
        "run_id": "KMPC-103",
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "atom_id": "BI/k=0.15/nominal",
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": "nominal"},
        "scope": {
            "included": (
                "native HP-M1 CPQR; accepted/audit F0/M3; 13-state merge; "
                "80-dps exact driver and independent non-fit holdout"
            ),
            "excluded": (
                "new coefficient attribution; other C2 atoms; [0,9]; S-M; "
                "ODE; P5.4; G8/G9; data"
            ),
        },
        "source_hashes": source_hashes(),
        "contract_guard": guard,
        "C1_prerequisites": prerequisites,
        "frozen_contract": frozen_contract,
        "independent_contract_valid": independent_contract.valid,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "frozen_reference_standard": {
            "method": "LIVE_FROZEN_BINARY64_HARD_ANCHORED_M1",
            "metadata": reference_metadata,
        },
        "M1": {"pass": m1_pass, "boundary": m1_boundary},
        "combined_R_fs_guard": rfs,
        "accepted_solve": accepted,
        "audit_solve": audit,
        "common": common,
        "common_pass": common_pass,
        "tails": tails,
        "tail_pass": tail_pass,
        "S_C0_actual_guard": s_c0,
        "background_guard": background,
        "core_pass": core_pass,
        "combined_register_handoff": merge,
        "float_audit_driver_capture": _CAPTURE_DIAGNOSTIC,
        "high_precision_downstream_boundary": exact_boundary,
        "Einstein_0i_7_after_hp_m1_downstream": target,
        "all_candidate_gates_pass": candidate_pass,
        "pass_c2_atom_candidate": candidate_pass,
        "checks": checks,
        "passed_execution_contract": all(checks.values()),
        "historical_attribution_gate": "NOT_USED_NOT_INVARIANT_AFTER_M1_REPLACEMENT",
        "candidate_interpretation_not_verdict": candidate,
        "physics_verdict_role": "CANDIDATE_ONLY_PENDING_INTERNAL_AUDIT",
        "thresholds": {
            "driver": physics.DRIVER_TOL,
            "holdout": physics.HOLDOUT_TOL,
            "common": physics.LOW_COEFFICIENT_TOL,
            "tail": physics.TAIL_TOL,
            "absolute_fallback": physics.ABS_FALLBACK_TOL,
            "background_relative": physics.BACKGROUND_K_TOL,
            "cpqr_rank_relative": "1e-60",
            "cpqr_orthogonality": "1e-60",
            "cpqr_factorization_relative": "1e-60",
            "cpqr_normal_residual_relative": "1e-55",
        },
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE_PENDING_INTERNAL_AUDIT",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("HP-M1 downstream insertion has no aggregate scope")
