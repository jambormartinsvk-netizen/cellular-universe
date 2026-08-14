"""Bounded BI support ladder step 2 for KMPC-042.

No physical equation or threshold is introduced.  The module reproduces the
immutable KMPC-041 supports [0,1] and [0,3], audits [0,5], compares only
common powers 0..3, and evaluates only the added-power envelopes 4 and 5.
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

from . import bi_c1_coverage as bi1
from . import cdi_support_ladder as step2
from . import full_ra_contract as ra_contract
from . import full_ra_m3_seed as physics
from . import s1_collective_contract as collective_contract


RUN_ID = "KMPC-042"
OUTPUT_NAME = "RUN_KMPC_042_P5_3G7_BI_SUPPORT_STEP_2_03_05.json"
FAILURE_NAME = "RUN_KMPC_042_P5_3G7_BI_SUPPORT_STEP_2_03_05_TECHNICAL_FAILURE.json"
MODE = "BI"
K_MPC = 0.05
VARIANT = "nominal"
GLOBAL_GATE = "C1"
LOCAL_STEP = "BI_SUPPORT_STEP_2"
REGRESSION_SUPPORT = (0, 1)
CANDIDATE_SUPPORT = (0, 3)
AUDIT_SUPPORT = (0, 5)
LEADING_J = 1
REGRESSION_REL_TOL = 1.0e-12
REGRESSION_ABS_TOL = 1.0e-14
KMPC041 = (
    "RUN_KMPC_041_P5_3G7_BI_C1_PRIMARY_EXTENDED_COVERAGE.json",
    "8BB006EF6606476D85168FBDCD913249E9EDE024C1017473376A33CF4C7AE183",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(bi1.source_hashes())
    for name in ("cdi_support_ladder.py", "bi_support_step2.py"):
        hashes[name] = sha256_file(here / name)
    return hashes


def make_deadline(limit: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(limit) or limit <= 0.0 or limit > 4.8:
        raise ValueError("KMPC-042 runtime must be in (0, 4.8] seconds")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-042 BI support step-2 internal deadline exceeded")

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
    spec = collective_contract.MODE_SPEC[MODE]
    supports = {
        "regression_01": REGRESSION_SUPPORT,
        "candidate_03": CANDIDATE_SUPPORT,
        "audit_05": AUDIT_SUPPORT,
    }
    counts = {
        label: {
            "powers": support[1] - support[0] + 1,
            "F0": _count(support, 2),
            "M3": _count(support, len(ra_contract.AUTHORITATIVE_STATE)),
        }
        for label, support in supports.items()
    }
    negative_fixture = (0, 7)
    checks = {
        "contract_primary_exact_01": tuple(spec["primary"]) == REGRESSION_SUPPORT,
        "contract_extended_exact_candidate_03": tuple(spec["extended"])
        == CANDIDATE_SUPPORT,
        "audit_exact_candidate_hi_plus_2": _valid_candidate_audit(
            CANDIDATE_SUPPORT, AUDIT_SUPPORT
        ),
        "negative_07_rejected": not _valid_candidate_audit(
            CANDIDATE_SUPPORT, negative_fixture
        ),
        "F0_counts_exact_4_8_12": [row["F0"] for row in counts.values()]
        == [4, 8, 12],
        "M3_counts_exact_26_52_78": [row["M3"] for row in counts.values()]
        == [26, 52, 78],
        "leading_j_exact_1": int(physics.legacy.MODE_SPECS[MODE]["leading_j"])
        == spec["leading_j"]
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


def _load_prerequisite(result_dir: Path) -> tuple[dict[str, object], str]:
    path = result_dir / KMPC041[0]
    observed = sha256_file(path)
    if observed != KMPC041[1]:
        raise RuntimeError("immutable KMPC-041 prerequisite hash mismatch")
    return json.loads(path.read_text(encoding="utf-8")), observed


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
        "all_coefficients_and_diagnostics_finite": _all_finite(
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
            "before": before,
            "during": during,
            "after": after,
            "restored": after == before,
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
        "support_01_F0": (
            step2._restore_series(old["fuel_primary"]["state"]),
            solved["01"]["fuel"]["state"],
        ),
        "support_01_M3": (
            step2._restore_series(old["m3_primary"]["fractional_state"]),
            solved["01"]["m3"]["fractional_state"],
        ),
        "support_03_F0": (
            step2._restore_series(old["fuel_extended"]["state"]),
            solved["03"]["fuel"]["state"],
        ),
        "support_03_M3": (
            step2._restore_series(old["m3_extended"]["fractional_state"]),
            solved["03"]["m3"]["fractional_state"],
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
    expected_powers = tuple(range(0, 4))
    states_equal = set(candidate) == set(audit)
    power_guard = {
        name: bool(
            tuple(candidate[name]) == expected_powers
            and all(power in audit[name] for power in expected_powers)
        )
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
                "base_candidate_03": base,
                "signed_added_tail_45_diagnostic": signed_added,
                "absolute_term_envelope_45_authoritative": envelope,
                "full_audit_05": full,
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
        raise ExpectedProbe("deterministic BI registry-restoration probe")

    probe_caught = False
    try:
        _solve_support(
            AUDIT_SUPPORT,
            physics._variant_inputs(VARIANT),
            {},
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
    json.dumps({"numpy": np.float64(1.0).item(), "finite": True}, allow_nan=False)
    checks = {
        "support_guard": bool(guard["pass"]),
        "immutable_KMPC041_hash": immutable_hash == KMPC041[1],
        "immutable_KMPC041_identity": immutable["identity"]
        == {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT},
        "immutable_KMPC041_candidate": immutable["candidate_interpretation_not_verdict"]
        == "REVIEW_BI_C1_SUPPORT_EXTENSION_REQUIRED",
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
    immutable, immutable_hash = _load_prerequisite(result_dir)
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
    standard, standard_meta = physics._standard_state(MODE, K_MPC, inputs, deadline)
    solved = {
        "01": _solve_support(REGRESSION_SUPPORT, inputs, standard, deadline),
        "03": _solve_support(CANDIDATE_SUPPORT, inputs, standard, deadline),
        "05": _solve_support(AUDIT_SUPPORT, inputs, standard, deadline),
    }
    regression = _regression_guard(immutable, solved)
    common = {
        "F0": _common_bridge(solved["03"]["fuel"]["state"], solved["05"]["fuel"]["state"]),
        "M3": _common_bridge(
            solved["03"]["m3"]["fractional_state"],
            solved["05"]["m3"]["fractional_state"],
        ),
    }
    common_pass = all(row["pass"] for row in common.values())
    tails = {
        "F0": _pure_tail(
            solved["05"]["fuel"]["state"], tuple(sorted(solved["05"]["fuel"]["state"]))
        ),
        "M3": _pure_tail(
            solved["05"]["m3"]["fractional_state"],
            tuple(ra_contract.AUTHORITATIVE_STATE),
        ),
    }
    tail_pass = all(row["pass"] for row in tails.values())
    s_c0_guard = step2.c1._s_c0_actual_coefficient_guard(
        {
            "m3_primary": {"fractional_state": solved["03"]["m3"]["fractional_state"]},
            "m3_extended": {"fractional_state": solved["05"]["m3"]["fractional_state"]},
        }
    )
    core_checks = {
        "support_guard": bool(guard["pass"]),
        "immutable_KMPC041_hash": immutable_hash == KMPC041[1],
        "frozen_RA_contract": bool(frozen_contract["valid"]),
        "independent_RA_contract": bool(independent_contract.valid),
        "frozen_B1_left_null_Bianchi": frozen_b1["execution_verdict"]
        == "PASS_R_A_B1_CONTRACT_GUARD_ONLY",
        "production_TCA0_bridge": bool(tca0["pass"]),
        "M1_standard_order5": bool(standard_meta["pass"]),
        "support_01_core": bool(solved["01"]["pass"]),
        "support_03_core": bool(solved["03"]["pass"]),
        "support_05_core": bool(solved["05"]["pass"]),
        "conditional_S_C0_actual_03_05": bool(s_c0_guard["pass"]),
        "all_solve_common_and_tail_fields_finite": _all_finite(
            {"solved": solved, "common": common, "tails": tails}
        ),
    }
    core_pass = all(core_checks.values())
    if not regression["pass"]:
        candidate = "REVIEW_BI_SUPPORT_STEP_2_REGRESSION_OR_FORMULA_DRIFT"
    elif not core_pass:
        candidate = "REVIEW_BI_SUPPORT_STEP_2_CORE_GATE_UNCLOSED"
    elif not common_pass:
        candidate = "REVIEW_BI_SUPPORT_STEP_2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED"
    elif not tail_pass:
        candidate = "REVIEW_BI_SUPPORT_STEP_2_SUPPORT_03_REMAINDER_UNCLOSED"
    else:
        candidate = "PASS_BI_SUPPORT_STEP_2_SUPPORT_03_ADEQUATE_CANDIDATE_ONLY"
    deadline()
    payload = {
        "test": "A2-K4 P5.3g7 GLOBAL_C1 BI_SUPPORT_STEP_2 [0,3] to [0,5]",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "identity": {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT},
        "gate_identity": {"global_gate": GLOBAL_GATE, "local_step": LOCAL_STEP},
        "scope": {
            "included": "BI regression [0,1]/[0,3], candidate [0,3], audit [0,5], common 0..3, tail 4,5",
            "excluded": "[0,7], order-7, NID/NIV, other k/variants, S-M, full hierarchy, ODE, P5.4, G8/G9, CLASS/CMB/BBN/S8/H0",
        },
        "support_guard": guard,
        "immutable_KMPC041": {"file": KMPC041[0], "sha256": immutable_hash},
        "frozen_contract": frozen_contract,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "M1_standard_metadata": standard_meta,
        "solved_supports": solved,
        "regression_against_KMPC041": regression,
        "common_coefficient_bridges_03_05": common,
        "common_coefficient_pass": common_pass,
        "pure_added_tails_45": tails,
        "pure_tail_pass": tail_pass,
        "conditional_S_C0_guard_03_05": s_c0_guard,
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
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not _all_finite(payload):
        raise FloatingPointError("non-finite value in final KMPC-042 payload")
    return payload
