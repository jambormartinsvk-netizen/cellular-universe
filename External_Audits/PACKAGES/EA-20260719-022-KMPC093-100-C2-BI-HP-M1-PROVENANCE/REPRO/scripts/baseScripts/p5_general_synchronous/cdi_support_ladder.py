"""Bounded CDI support ladder for KMPC-035.

No physical equation is defined here.  The module calls the frozen R-A
solver for supports [0,1], [0,3], and [0,5], reproduces immutable KMPC-034,
and isolates the omitted powers 4 and 5 relative to the candidate [0,3].
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

from . import cdi_c1_coverage as c1
from . import full_ra_contract as ra_contract
from . import full_ra_m3_seed as physics
from . import s1_collective_contract as collective_contract


RUN_ID = "KMPC-035"
OUTPUT_NAME = "RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json"
FAILURE_NAME = "RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER_TECHNICAL_FAILURE.json"
MODE = "CDI"
K_MPC = 0.05
VARIANT = "nominal"
GLOBAL_GATE = "C1"
LOCAL_STEP = "CDI_SUPPORT_STEP_2"
NOT_GLOBAL_GATE = "NOT_GLOBAL_C2_FOURIER_GATE"
REGRESSION_SUPPORT = (0, 1)
CANDIDATE_SUPPORT = (0, 3)
AUDIT_SUPPORT = (0, 5)
LEADING_J = 1
REGRESSION_REL_TOL = 1.0e-12
REGRESSION_ABS_TOL = 1.0e-14
C1_RESULT = (
    "RUN_KMPC_034_P5_3G7_CDI_C1_PRIMARY_EXTENDED_COVERAGE.json",
    "37FB4453CBFF38710CF5694C21104689F1B070742FB02324011AA389508DCE20",
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
        "cdi_support_ladder.py",
    ):
        hashes[name] = sha256_file(here / name)
    return hashes


def make_deadline(max_runtime_seconds: float) -> tuple[float, Callable[[], None]]:
    if not 0.0 < max_runtime_seconds <= 4.8:
        raise ValueError("internal runtime must be in (0, 4.8] seconds")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError(
                "KMPC-035 GLOBAL_C1 CDI_SUPPORT_STEP_2 internal deadline exceeded"
            )

    return started, deadline


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
    contract_primary = tuple(collective_contract.MODE_SPEC[MODE]["primary"])
    contract_extended = tuple(collective_contract.MODE_SPEC[MODE]["extended"])
    derived_audit = (contract_extended[0], contract_extended[1] + 2)
    negative_fixture = (contract_extended[0], contract_extended[1] + 3)
    supports = {
        "regression": REGRESSION_SUPPORT,
        "candidate": CANDIDATE_SUPPORT,
        "audit": AUDIT_SUPPORT,
    }
    derived_counts = {
        label: {
            "powers": support[1] - support[0] + 1,
            "F0": _count(support, 2),
            "M3": _count(support, len(ra_contract.AUTHORITATIVE_STATE)),
        }
        for label, support in supports.items()
    }
    checks = {
        "contract_primary_is_regression_01": contract_primary == REGRESSION_SUPPORT,
        "contract_extended_is_candidate_03": contract_extended == CANDIDATE_SUPPORT,
        "audit_is_candidate_hi_plus_2": derived_audit == AUDIT_SUPPORT,
        "negative_hi_plus_3_rejected": not _valid_candidate_audit(
            CANDIDATE_SUPPORT, negative_fixture
        ),
        "F0_counts_4_8_12": [
            derived_counts[label]["F0"]
            for label in ("regression", "candidate", "audit")
        ]
        == [4, 8, 12],
        "M3_counts_26_52_78": [
            derived_counts[label]["M3"]
            for label in ("regression", "candidate", "audit")
        ]
        == [26, 52, 78],
        "leading_j_1": int(physics.legacy.MODE_SPECS[MODE]["leading_j"])
        == LEADING_J,
        "surfaces_exact_1e4_1e2": tuple(physics.Z_SURFACES) == (1.0e-4, 1.0e-2),
        "surface_cap_0p05": max(physics.Z_SURFACES) <= 0.05,
        "thresholds_exact": bool(
            physics.TAIL_TOL == 1.0e-6
            and physics.ABS_FALLBACK_NORM == 1.0e-12
            and physics.ABS_FALLBACK_TOL == 1.0e-12
        ),
    }
    return {
        "supports": {name: list(value) for name, value in supports.items()},
        "derived_counts": derived_counts,
        "negative_fixture": list(negative_fixture),
        "checks": checks,
        "pass": all(checks.values()),
    }


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


def _core_checks(
    fuel_diag: Mapping[str, object], m3_diag: Mapping[str, object]
) -> dict[str, bool]:
    return {
        "F0_rank": bool(fuel_diag["pass_rank"]),
        "F0_driver": bool(fuel_diag["pass_driver"]),
        "F0_leading_postcheck": bool(fuel_diag["pass_leading_postcheck"]),
        "M3_rank": bool(m3_diag["pass_rank"]),
        "M3_driver": bool(m3_diag["pass_driver"]),
        "M3_independent_00_0i_holdout": bool(m3_diag["holdout"]["pass_holdout"]),
        "M3_forbidden_layers": bool(m3_diag["pass_forbidden_layers"]),
        "M3_forbidden_stress": bool(m3_diag["pass_forbidden_stress_guard"]),
        "M3_production_contract": bool(m3_diag["pass_production_contract"]),
        "M3_Uc_lower_regular": bool(
            float(m3_diag["Uc_lower_regular_max_abs"]) <= physics.LEADING_TOL
        ),
    }


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
    fuel: dict[str, dict[int, float]]
    fuel_diag: dict[str, object]
    fractional: dict[str, dict[int, float]]
    m3_meta: dict[str, object]
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
        "F0_exact_shape": bool(
            fuel_diag["rows"] == fuel_diag["unknowns"] == expected_f0
        ),
        "M3_exact_shape": bool(
            m3_diag["rows"] == m3_diag["unknowns"] == expected_m3
        ),
        "all_coefficients_and_diagnostics_finite": _all_finite(
            {"fuel": fuel, "fuel_diag": fuel_diag, "m3": fractional, "m3_diag": m3_diag}
        ),
        **_core_checks(fuel_diag, m3_diag),
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


def _regression_metric(
    expected: Mapping[str, Mapping[int, float]],
    observed: Mapping[str, Mapping[int, float]],
) -> dict[str, object]:
    exact_state_set = set(expected) == set(observed)
    exact_power_sets = exact_state_set and all(
        set(expected[name]) == set(observed[name]) for name in expected
    )
    rows: list[tuple[float, str, float, float, float, float]] = []
    if exact_power_sets:
        for name in sorted(expected):
            for power in sorted(expected[name]):
                left = float(expected[name][power])
                right = float(observed[name][power])
                difference = abs(left - right)
                scale = max(abs(left), abs(right))
                bound = max(REGRESSION_ABS_TOL, REGRESSION_REL_TOL * scale)
                ratio = difference / bound
                rows.append((ratio, f"{name}[{power}]", difference, bound, left, right))
    worst = max(rows, default=(0.0, "missing", 0.0, 0.0, 0.0, 0.0))
    finite = all(math.isfinite(item) for row in rows for item in (row[0], row[2], row[3], row[4], row[5]))
    passed = bool(exact_state_set and exact_power_sets and rows and finite and worst[0] <= 1.0)
    return {
        "exact_state_set": exact_state_set,
        "exact_power_sets": exact_power_sets,
        "coefficient_count": len(rows),
        "relative_tolerance": REGRESSION_REL_TOL,
        "absolute_tolerance": REGRESSION_ABS_TOL,
        "worst_bound_ratio": worst[0],
        "worst_coefficient": worst[1],
        "worst_absolute_difference": worst[2],
        "worst_allowed_bound": worst[3],
        "expected_value": worst[4],
        "observed_value": worst[5],
        "finite": finite,
        "pass": passed,
    }


def _regression_guard(
    immutable: Mapping[str, object], solved: Mapping[str, Mapping[str, object]]
) -> dict[str, object]:
    old = immutable["solve_result"]
    expected = {
        "support_01_F0": _restore_series(old["fuel_primary"]["state"]),
        "support_01_M3": _restore_series(old["m3_primary"]["fractional_state"]),
        "support_03_F0": _restore_series(old["fuel_extended"]["state"]),
        "support_03_M3": _restore_series(old["m3_extended"]["fractional_state"]),
    }
    observed = {
        "support_01_F0": solved["01"]["fuel"]["state"],
        "support_01_M3": solved["01"]["m3"]["fractional_state"],
        "support_03_F0": solved["03"]["fuel"]["state"],
        "support_03_M3": solved["03"]["m3"]["fractional_state"],
    }
    details = {
        name: _regression_metric(expected[name], observed[name]) for name in expected
    }
    return {"details": details, "pass": all(item["pass"] for item in details.values())}


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
            finite = all(
                math.isfinite(value) for value in (base, signed_added, envelope, full)
            )
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
            first_exact = next(
                (power for power in base_powers if float(series.get(power, 0.0)) != 0.0),
                None,
            )
            first_above_fallback = next(
                (
                    power
                    for power in base_powers
                    if abs(float(series.get(power, 0.0))) > physics.ABS_FALLBACK_NORM
                ),
                None,
            )
            cancellation_ratio = (
                None if envelope == 0.0 else abs(signed_added) / envelope
            )
            states[name] = {
                "base_candidate_03": base,
                "signed_added_tail_45_diagnostic": signed_added,
                "absolute_term_envelope_45_authoritative": envelope,
                "full_audit_05": full,
                "first_nonzero_candidate_power_exact_float": first_exact,
                "first_candidate_power_above_abs_fallback_norm": first_above_fallback,
                "signed_over_envelope_cancellation_diagnostic": cancellation_ratio,
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
            "pass": all(item["pass"] for item in states.values()),
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


def _tail_reduction_diagnostic(
    old_tail: Mapping[str, object], new_tail: Mapping[str, object]
) -> dict[str, object]:
    by_z: dict[str, object] = {}
    monotone = True
    for z in physics.Z_SURFACES:
        key = str(z)
        old_row = old_tail["by_z"][key]
        new_row = new_tail["by_z"][key]
        old_norm = max(
            float(old_row["worst_relative"]["value"]) / physics.TAIL_TOL,
            float(old_row["worst_absolute"]["value"]) / physics.ABS_FALLBACK_TOL,
        )
        new_norm = max(
            float(new_row["worst_relative"]["value"]) / physics.TAIL_TOL,
            float(new_row["worst_absolute"]["value"]) / physics.ABS_FALLBACK_TOL,
        )
        reduced = new_norm <= old_norm
        monotone = monotone and reduced
        ratio = None if new_norm == 0.0 else old_norm / new_norm
        ratio_finite = ratio is None or math.isfinite(ratio)
        by_z[key] = {
            "old_tail_23_normalized": old_norm,
            "new_tail_45_normalized": new_norm,
            "old_over_new": ratio if ratio_finite else None,
            "old_over_new_status": (
                "UNDEFINED_NEW_ZERO" if new_norm == 0.0
                else "FINITE" if ratio_finite
                else "NONFINITE_SUPPRESSED_DIAGNOSTIC_ONLY"
            ),
            "nonincreasing": reduced,
        }
    return {"by_z": by_z, "nonincreasing_both_surfaces": monotone, "status": "DIAGNOSTIC_ONLY"}


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = make_deadline(max_runtime_seconds)
    guard = support_guard()
    c1_path = result_dir / C1_RESULT[0]
    immutable_hash = sha256_file(c1_path)
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
    sample = {"native": 1.0, "numpy": np.float64(2.0), "finite": True}
    json.dumps({key: (value.item() if isinstance(value, np.generic) else value) for key, value in sample.items()})
    deadline()
    checks = {
        "support_guard": bool(guard["pass"]),
        "immutable_C1_hash": immutable_hash == C1_RESULT[1],
        "fixed_identity": MODE == "CDI" and K_MPC == 0.05 and VARIANT == "nominal",
        "JSON_scalar_fixture": True,
        "registry_probe_exception_caught": probe_caught,
        "all_shape_registries_restored_after_exception": registry_after
        == registry_before,
        "surfaces_exact": tuple(physics.Z_SURFACES) == (1.0e-4, 1.0e-2),
        "surface_cap": max(physics.Z_SURFACES) <= 0.05,
        "thresholds_frozen": bool(
            physics.TAIL_TOL == 1.0e-6
            and physics.ABS_FALLBACK_NORM == 1.0e-12
            and physics.ABS_FALLBACK_TOL == 1.0e-12
        ),
    }
    return {"run_id": RUN_ID, "mode": "SMOKE_NO_RESULT_FILE", "checks": checks, "passed": all(checks.values())}


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = make_deadline(max_runtime_seconds)
    guard = support_guard()
    c1_path = result_dir / C1_RESULT[0]
    immutable_hash = sha256_file(c1_path)
    if immutable_hash != C1_RESULT[1]:
        raise RuntimeError("immutable KMPC-034 hash mismatch")
    immutable = json.loads(c1_path.read_text(encoding="utf-8"))

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
    deadline()

    solved = {
        "01": _solve_support(REGRESSION_SUPPORT, inputs, standard, deadline),
        "03": _solve_support(CANDIDATE_SUPPORT, inputs, standard, deadline),
        "05": _solve_support(AUDIT_SUPPORT, inputs, standard, deadline),
    }
    regression = _regression_guard(immutable, solved)
    common = {
        "F0": physics._coefficient_metrics(
            solved["03"]["fuel"]["state"], solved["05"]["fuel"]["state"]
        ),
        "M3": physics._coefficient_metrics(
            solved["03"]["m3"]["fractional_state"],
            solved["05"]["m3"]["fractional_state"],
        ),
    }
    common_pass = all(item["pass"] for item in common.values())
    tails = {
        "F0": _pure_tail(
            solved["05"]["fuel"]["state"], tuple(sorted(solved["05"]["fuel"]["state"]))
        ),
        "M3": _pure_tail(
            solved["05"]["m3"]["fractional_state"],
            tuple(ra_contract.AUTHORITATIVE_STATE),
        ),
    }
    tail_pass = all(item["pass"] for item in tails.values())
    s_c0_guard = c1._s_c0_actual_coefficient_guard(
        {
            "m3_primary": {"fractional_state": solved["03"]["m3"]["fractional_state"]},
            "m3_extended": {"fractional_state": solved["05"]["m3"]["fractional_state"]},
        }
    )
    core_checks = {
        "support_guard": bool(guard["pass"]),
        "immutable_C1_hash": immutable_hash == C1_RESULT[1],
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
        candidate = "REVIEW_CDI_SUPPORT_STEP_2_REGRESSION_OR_FORMULA_DRIFT"
    elif not core_pass:
        candidate = "REVIEW_CDI_SUPPORT_STEP_2_CORE_GATE_UNCLOSED"
    elif not common_pass:
        candidate = "REVIEW_CDI_SUPPORT_STEP_2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED"
    elif not tail_pass:
        candidate = "REVIEW_CDI_SUPPORT_STEP_2_SUPPORT_03_REMAINDER_UNCLOSED"
    else:
        candidate = "PASS_CDI_SUPPORT_STEP_2_SUPPORT_03_ADEQUATE_CANDIDATE"
    reduction = _tail_reduction_diagnostic(immutable["pure_added_tail"], tails["M3"])
    deadline()
    payload = {
        "test": (
            "A2-K4 P5.3g7 GLOBAL_C1 CDI_SUPPORT_STEP_2 "
            "support [0,3] to [0,5] ladder"
        ),
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "identity": {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT},
        "gate_identity": {
            "global_gate": GLOBAL_GATE,
            "local_step": LOCAL_STEP,
            "not_global_gate": NOT_GLOBAL_GATE,
        },
        "scope": {
            "included": "CDI supports [0,1], [0,3], [0,5] on frozen R-A M3-TCA0",
            "excluded": (
                "BI/NID/NIV, other k/variants, S-M, physical steam origin, "
                "species-resolved F_l>=3, full hierarchy, ODE, G8/G9, "
                "BBN/CMB/CLASS/S8/H0"
            ),
        },
        "support_guard": guard,
        "immutable_C1": {"file": C1_RESULT[0], "sha256": immutable_hash},
        "frozen_contract": frozen_contract,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "M1_standard_metadata": standard_meta,
        "solved_supports": solved,
        "regression_against_C1": regression,
        "common_coefficient_bridges_03_05": common,
        "common_coefficient_pass": common_pass,
        "pure_added_tails_45": tails,
        "pure_tail_pass": tail_pass,
        "conditional_S_C0_guard_03_05": s_c0_guard,
        "tail_23_to_45_reduction_diagnostic_only": reduction,
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
        raise FloatingPointError("non-finite value in final KMPC-035 payload")
    return payload
