"""KMPC-057 C2 Fourier coverage over five modes and two new k values.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
One stable module serves ten separately published atoms and one aggregate.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import time
from typing import Callable, Mapping

from . import cdi_support_ladder as support_tools
from . import full_ra_contract as ra_contract
from . import full_ra_m3_seed as physics
from . import nid_c1_coverage as finite_owner
from . import niv_c1_coverage as niv_guard
from . import s1_collective_contract as collective_contract
from . import niv_support_step2_v2_finite_owner as lineage


RUN_ID = "KMPC-057"
MODES = ("AD", "CDI", "BI", "NID", "NIV")
K_VALUES = (0.005, 0.15)
VARIANT = "nominal"
SUPPORTS = {
    "AD": {"accepted": (0, 2), "audit": (0, 4), "m1_depth": 5},
    "CDI": {"accepted": (0, 5), "audit": (0, 7), "m1_depth": 7},
    "BI": {"accepted": (0, 5), "audit": (0, 7), "m1_depth": 7},
    "NID": {"accepted": (0, 5), "audit": (0, 7), "m1_depth": 7},
    "NIV": {"accepted": (-1, 4), "audit": (-1, 6), "m1_depth": 6},
}
C1_PREREQUISITES = {
    "AD": (
        "RUN_KMPC_031_P5_3G7_M3_FULL_RA_DEEP_TAIL_BRANCH_PROVENANCE.json",
        "C547F818E3918CD844CA06BEA32814279A9D4A20D662A9166114410645792FF6",
        "CANDIDATE_SUPPORT_TRUNCATION_CLOSED_J4_SENTINEL_SCOPE",
    ),
    "CDI": (
        "RUN_KMPC_040_P5_3G7_CDI_SUPPORT_STEP_3_05_07.json",
        "69C78F70ECD851D8B8A48E4E09445181C0D4559E9BD2E90A7BA19933351BD219",
        "PASS_CDI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
    ),
    "BI": (
        "RUN_KMPC_046_P5_3G7_BI_SUPPORT_STEP_3_OWNER_SUCCESSOR.json",
        "60EC5A801FDDBAFFBA6CE184EBB3BC154879928385E6E37FB118781118615FB1",
        "PASS_BI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
    ),
    "NID": (
        "RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json",
        "625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD",
        "PASS_NID_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
    ),
    "NIV": (
        "RUN_KMPC_056_P5_3G7_NIV_SUPPORT_STEP_2_FINITE_OWNER_SUCCESSOR.json",
        "9AF6410513C2B0A6142DA9B08E8A1D115670C644171B102683568E64D645C332",
        "PASS_NIV_SUPPORT_STEP_2_SUPPORT_MINUS1_4_ADEQUATE_CANDIDATE_ONLY",
    ),
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(lineage.source_hashes())
    hashes["c2_fourier_coverage.py"] = sha256_file(here / "c2_fourier_coverage.py")
    return hashes


def make_deadline(limit: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(limit) or limit <= 0.0 or limit > 4.8:
        raise ValueError("KMPC-057 runtime must be in (0, 4.8] seconds")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-057 C2 internal deadline exceeded")

    return started, deadline


def k_token(k_mpc: float) -> str:
    if k_mpc == 0.005:
        return "0p005"
    if k_mpc == 0.15:
        return "0p15"
    raise ValueError(f"unsupported C2 k={k_mpc}")


def atom_output_name(mode: str, k_mpc: float) -> str:
    if mode not in MODES:
        raise ValueError(mode)
    return f"RUN_KMPC_057_P5_3G7_C2_{mode}_K{k_token(k_mpc)}_NOMINAL.json"


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return atom_output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def _load_c1(result_dir: Path) -> dict[str, object]:
    loaded: dict[str, object] = {}
    for mode, (name, expected_hash, expected_candidate) in C1_PREREQUISITES.items():
        path = result_dir / name
        observed_hash = sha256_file(path)
        payload = json.loads(path.read_text(encoding="utf-8"))
        observed_candidate = payload.get("candidate_interpretation_not_verdict")
        if observed_hash != expected_hash or observed_candidate != expected_candidate:
            raise RuntimeError(f"immutable C1 prerequisite mismatch: {mode}")
        loaded[mode] = {"file": name, "sha256": observed_hash, "candidate": observed_candidate}
    return loaded


def contract_guard() -> dict[str, object]:
    checks: dict[str, bool] = {
        "modes_exact": MODES == tuple(collective_contract.MODES),
        "k_values_exact": K_VALUES == (0.005, 0.15),
        "variant_nominal": VARIANT == "nominal",
        "surfaces_exact": tuple(physics.Z_SURFACES) == (1.0e-4, 1.0e-2),
        "background_a_exact": tuple(physics.A_VALUES_BACKGROUND) == (1.0e-8, 3.0e-8),
        "thresholds_exact": bool(
            physics.LOW_COEFFICIENT_TOL == 1.0e-8
            and physics.TAIL_TOL == 1.0e-6
            and physics.ABS_FALLBACK_NORM == 1.0e-12
            and physics.ABS_FALLBACK_TOL == 1.0e-12
            and physics.BACKGROUND_K_TOL == 1.0e-12
        ),
    }
    derived: dict[str, object] = {}
    for mode in MODES:
        accepted = tuple(SUPPORTS[mode]["accepted"])
        audit = tuple(SUPPORTS[mode]["audit"])
        depth = int(SUPPORTS[mode]["m1_depth"])
        native = tuple(physics.MODE_SUPPORT[mode])
        expected_accepted = native if mode == "AD" else tuple(collective_contract.MODE_SPEC[mode]["extended"])
        mode_checks = {
            "accepted_matches_closed_C1": accepted == expected_accepted,
            "audit_is_plus2": audit == (accepted[0], accepted[1] + 2),
            "M1_depth_covers_audit": depth >= audit[1],
            "leading_matches": accepted[0] == int(physics.legacy.MODE_SPECS[mode]["f_min"]),
        }
        checks.update({f"{mode}_{name}": value for name, value in mode_checks.items()})
        derived[mode] = {
            "accepted": list(accepted), "audit": list(audit), "m1_depth": depth,
            "F0_counts": [2 * (accepted[1] - accepted[0] + 1), 2 * (audit[1] - audit[0] + 1)],
            "M3_counts": [13 * (accepted[1] - accepted[0] + 1), 13 * (audit[1] - audit[0] + 1)],
        }
    return {"derived": derived, "checks": checks, "pass": all(checks.values())}


def _standard_depth(
    mode: str, k_mpc: float, depth: int, inputs: object, deadline: Callable[[], None]
) -> tuple[dict[str, dict[int, float]], dict[str, object]]:
    state_legacy, background, metadata = physics.m1_anchor.solve_standard_seed_anchored(
        mode, k_mpc, inputs, deadline, order=depth
    )
    state = {target: dict(state_legacy[source]) for target, source in physics.STATE_TO_LEGACY.items()}
    series = physics.legacy.Series(-4, depth + 5)
    rows = physics.legacy._standard_rows(state_legacy, background, series)
    exponents = tuple(range(-1, depth + 1))
    scale = max(max(abs(float(value)) for values in state.values() for value in values.values()), 1.0e-14)
    driver_max = max(abs(series.coef(rows[row], power)) for row in physics.legacy.DRIVER_ROWS for power in exponents)
    holdout_max = max(abs(series.coef(rows[row], power)) for row in physics.legacy.HOLDOUT_ROWS for power in exponents)
    full = {
        "mode": mode, "k_Mpc_inverse": k_mpc, "depth": depth,
        "full_vector_unknowns_expected": 11 * (depth + 2),
        "reduced_unknowns_expected": 11 * (depth + 2) - 1,
        "driver_max_absolute": float(driver_max), "holdout_max_absolute": float(holdout_max),
        "state_scale": float(scale), "driver_global_state_scaled": float(driver_max / scale),
        "holdout_global_state_scaled": float(holdout_max / scale),
        "solver_metadata": dict(metadata),
        "finite": finite_owner._all_finite({"state": state, "metadata": metadata}),
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
    mode: str, k_mpc: float, support: tuple[int, int], inputs: object,
    standard: Mapping[str, Mapping[int, float]], deadline: Callable[[], None],
) -> dict[str, object]:
    native_primary = support == tuple(physics.MODE_SUPPORT[mode])
    f0_registry = physics.EXPECTED_F0_PRIMARY if native_primary else physics.EXPECTED_F0_EXTENDED
    m3_registry = physics.EXPECTED_M3_PRIMARY if native_primary else physics.EXPECTED_M3_EXTENDED
    expected_f0 = 2 * (support[1] - support[0] + 1)
    expected_m3 = 13 * (support[1] - support[0] + 1)
    before = {"F0": int(f0_registry[mode]), "M3": int(m3_registry[mode])}
    try:
        f0_registry[mode] = expected_f0
        m3_registry[mode] = expected_m3
        during = {"F0": int(f0_registry[mode]), "M3": int(m3_registry[mode])}
        fuel, fuel_diag = physics._solve_fuel_zero(mode, k_mpc, inputs, dict(standard), support, deadline)
        combined = {name: dict(values) for name, values in standard.items()}
        combined.update(fuel)
        fractional, m3_meta = physics._solve_m3(mode, k_mpc, inputs, combined, support, deadline)
    finally:
        f0_registry[mode] = before["F0"]
        m3_registry[mode] = before["M3"]
    after = {"F0": int(f0_registry[mode]), "M3": int(m3_registry[mode])}
    m3_diag = m3_meta["diagnostics"]
    checks = {
        "shape_guard_during": during == {"F0": expected_f0, "M3": expected_m3},
        "shape_guard_restored": after == before,
        "F0_exact_shape": fuel_diag["rows"] == fuel_diag["unknowns"] == expected_f0,
        "M3_exact_shape": m3_diag["rows"] == m3_diag["unknowns"] == expected_m3,
        "finite": finite_owner._all_finite({"fuel": fuel, "fuel_diag": fuel_diag, "m3": fractional, "m3_diag": m3_diag}),
        **support_tools._core_checks(fuel_diag, m3_diag),
    }
    deadline()
    return {
        "support": list(support), "expected_counts": {"F0": expected_f0, "M3": expected_m3},
        "shape_guard_adapter": {"before": before, "during": during, "after": after},
        "fuel": {"state": fuel, "diagnostics": fuel_diag},
        "m3": {"fractional_state": fractional, **m3_meta},
        "checks": checks, "pass": all(checks.values()),
    }


def _common_bridge(
    accepted: Mapping[str, Mapping[int, float]], audit: Mapping[str, Mapping[int, float]],
    support: tuple[int, int],
) -> dict[str, object]:
    powers = tuple(range(support[0], support[1] + 1))
    state_guard = set(accepted) == set(audit) and all(
        tuple(accepted[name]) == powers and all(power in audit[name] for power in powers)
        for name in accepted
    )
    metrics = physics._coefficient_metrics(dict(accepted), dict(audit))
    return {"expected_common_powers": list(powers), "state_power_guard": state_guard,
            "metrics": metrics, "pass": bool(state_guard and metrics["pass"])}


def _tail(
    audit: Mapping[str, Mapping[int, float]], state_order: tuple[str, ...],
    accepted_support: tuple[int, int], audit_support: tuple[int, int],
) -> dict[str, object]:
    base_powers = tuple(range(accepted_support[0], accepted_support[1] + 1))
    added_powers = tuple(range(accepted_support[1] + 1, audit_support[1] + 1))
    by_z: dict[str, object] = {}
    all_pass = True
    for z in physics.Z_SURFACES:
        states: dict[str, object] = {}
        relative: list[tuple[float, str]] = []
        absolute: list[tuple[float, str]] = []
        for name in state_order:
            series = audit[name]
            base = math.fsum(float(series.get(power, 0.0)) * z**power for power in base_powers)
            signed = math.fsum(float(series.get(power, 0.0)) * z**power for power in added_powers)
            envelope = math.fsum(abs(float(series.get(power, 0.0))) * z**power for power in added_powers)
            full = base + signed
            finite = all(math.isfinite(value) for value in (base, signed, envelope, full))
            scale = max(abs(base), abs(full))
            if scale > physics.ABS_FALLBACK_NORM:
                branch, metric = "relative", envelope / scale
                passed = finite and metric <= physics.TAIL_TOL
                relative.append((metric, name))
            else:
                branch, metric = "absolute", envelope
                passed = finite and metric <= physics.ABS_FALLBACK_TOL
                absolute.append((metric, name))
            all_pass = all_pass and passed
            states[name] = {"base": base, "signed_tail_diagnostic": signed,
                            "absolute_tail_envelope": envelope, "full": full,
                            "branch": branch, "metric": metric, "pass": passed}
        worst_relative = max(relative, default=(0.0, "none"))
        worst_absolute = max(absolute, default=(0.0, "none"))
        by_z[str(z)] = {"states": states,
                        "worst_relative": {"value": worst_relative[0], "state": worst_relative[1]},
                        "worst_absolute": {"value": worst_absolute[0], "state": worst_absolute[1]},
                        "pass": all(row["pass"] for row in states.values())}
    return {"base_powers": list(base_powers), "added_powers": list(added_powers),
            "authoritative_metric": "sum(abs(c_j)*z**j) over added powers",
            "signed_tail_role": "DIAGNOSTIC_ONLY", "by_z": by_z, "pass": all_pass}


def _background_guard(inputs: object, k_mpc: float, audit_hi: int) -> dict[str, object]:
    rows: dict[str, object] = {}
    worst = (0.0, "none")
    for a in physics.A_VALUES_BACKGROUND:
        observed = physics._physical_background(inputs, k_mpc, a, audit_hi)
        baseline = physics._physical_background(inputs, 0.05, a, audit_hi)
        metrics: dict[str, object] = {}
        for name in ("D", "H_Mpc_inverse", "rho_f_over_rho_r", "rho_ash_over_rho_r"):
            left, right = float(observed[name]), float(baseline[name])
            relative = abs(left - right) / max(abs(left), abs(right), 1.0e-300)
            metrics[name] = {"observed": left, "baseline_k0p05": right, "relative_difference": relative,
                             "pass": relative <= physics.BACKGROUND_K_TOL}
            worst = max(worst, (relative, f"a={a}:{name}"))
        rows[str(a)] = {"metrics": metrics, "pass": all(item["pass"] for item in metrics.values())}
    return {"a_surfaces": list(physics.A_VALUES_BACKGROUND), "by_a": rows,
            "worst_relative": worst[0], "worst_label": worst[1],
            "pass": all(row["pass"] for row in rows.values())}


def _rfs_guard(mode: str, standard: Mapping[str, Mapping[int, float]], inputs: object) -> dict[str, object]:
    if mode == "NID":
        return finite_owner._combined_rfs_guard(standard, inputs)
    if mode == "NIV":
        return niv_guard._combined_rfs_guard(standard, inputs)
    return {"mode": mode, "applicable": False, "pass": True}


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = make_deadline(max_runtime_seconds)
    prerequisites = _load_c1(result_dir)
    guard = contract_guard()
    wrong_mode_rejected = False
    wrong_k_rejected = False
    try:
        atom_output_name("WRONG", 0.005)
    except ValueError:
        wrong_mode_rejected = True
    try:
        atom_output_name("AD", 0.05)
    except ValueError:
        wrong_k_rejected = True
    names = [atom_output_name(mode, k) for mode in MODES for k in K_VALUES]
    checks = {
        "contract_guard": bool(guard["pass"]), "all_C1_prerequisites": len(prerequisites) == 5,
        "ten_unique_atom_names": len(names) == len(set(names)) == 10,
        "wrong_mode_rejected": wrong_mode_rejected, "wrong_k_rejected": wrong_k_rejected,
        "all_finite_fixture": finite_owner._all_finite({"native": 1.0, "nested": [True, 2]}),
        "nonfinite_fixture_rejected": not finite_owner._all_finite({"bad": float("inf")}),
    }
    deadline()
    return {"run_id": RUN_ID, "mode": "SMOKE_NO_RESULT_FILE", "checks": checks, "passed": all(checks.values())}


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = make_deadline(max_runtime_seconds)
    if mode not in MODES or k_mpc not in K_VALUES:
        raise ValueError("KMPC-057 atom identity outside frozen matrix")
    prerequisites = _load_c1(result_dir)
    guard = contract_guard()
    frozen_contract = physics.validate_frozen_contract()
    independent_contract = ra_contract.validate_contract(
        collective_contract.EXPECTED_STATE, collective_contract.EXPECTED_DRIVER, collective_contract.EXPECTED_HOLDOUT
    )
    frozen_b1 = physics.b1_guard.build_contract_guard(max_runtime_seconds=min(1.0, max_runtime_seconds))
    tca0 = physics.production_tca0_reduction_guard()
    inputs = physics._variant_inputs(VARIANT)
    spec = SUPPORTS[mode]
    accepted_support = tuple(spec["accepted"])
    audit_support = tuple(spec["audit"])
    standard, m1 = _standard_depth(mode, k_mpc, int(spec["m1_depth"]), inputs, deadline)
    rfs = _rfs_guard(mode, standard, inputs)
    if m1["pass"]:
        accepted = _solve_support(mode, k_mpc, accepted_support, inputs, standard, deadline)
        audit = _solve_support(mode, k_mpc, audit_support, inputs, standard, deadline)
        common = {
            "F0": _common_bridge(accepted["fuel"]["state"], audit["fuel"]["state"], accepted_support),
            "M3": _common_bridge(accepted["m3"]["fractional_state"], audit["m3"]["fractional_state"], accepted_support),
        }
        tails = {
            "F0": _tail(audit["fuel"]["state"], tuple(sorted(audit["fuel"]["state"])), accepted_support, audit_support),
            "M3": _tail(audit["m3"]["fractional_state"], tuple(ra_contract.AUTHORITATIVE_STATE), accepted_support, audit_support),
        }
        s_c0 = support_tools.c1._s_c0_actual_coefficient_guard({
            "m3_primary": {"fractional_state": accepted["m3"]["fractional_state"]},
            "m3_extended": {"fractional_state": audit["m3"]["fractional_state"]},
        })
    else:
        accepted = audit = {"pass": False, "status": "NOT_RUN_M1_BOUNDARY"}
        common = tails = {"F0": {"pass": False}, "M3": {"pass": False}}
        s_c0 = {"pass": False, "status": "NOT_RUN_M1_BOUNDARY"}
    background = _background_guard(inputs, k_mpc, audit_support[1])
    common_pass = all(row["pass"] for row in common.values())
    tail_pass = all(row["pass"] for row in tails.values())
    core_pass = bool(
        guard["pass"] and len(prerequisites) == 5 and frozen_contract["valid"]
        and independent_contract.valid and frozen_b1["execution_verdict"] == "PASS_R_A_B1_CONTRACT_GUARD_ONLY"
        and tca0["pass"] and m1["pass"] and rfs["pass"] and accepted["pass"] and audit["pass"]
        and s_c0["pass"]
    )
    if not m1["pass"]:
        candidate = "REVIEW_C2_M1_NUMERICAL_BOUNDARY"
    elif not core_pass:
        candidate = "REVIEW_C2_CORE_GATE_UNCLOSED"
    elif not common_pass:
        candidate = "REVIEW_C2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED"
    elif not tail_pass:
        candidate = "REVIEW_C2_SUPPORT_EXTENSION_REQUIRED"
    elif not background["pass"]:
        candidate = "STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY"
    else:
        candidate = "PASS_C2_FOURIER_ATOM_CANDIDATE_ONLY"
    deadline()
    payload = {
        "test": "A2-K4 P5.3g7 C2 Fourier nominal atom",
        "run_id": RUN_ID, "atom_id": f"{mode}/k={k_mpc}/nominal",
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": VARIANT},
        "scope": {"included": "one C2 nominal mode-k atom with accepted/audit support and local k=.05 background baseline",
                  "excluded": "other C2 atoms, C3 gamma0/af0, S-M, full hierarchy, ODE, G8/G9, data"},
        "C1_prerequisites": prerequisites, "contract_guard": guard,
        "frozen_contract": frozen_contract, "independent_contract_valid": independent_contract.valid,
        "frozen_B1_left_null_Bianchi": frozen_b1, "production_TCA0_bridge": tca0,
        "support_depth_spec": spec, "M1": m1, "combined_R_fs_guard": rfs,
        "accepted_solve": accepted, "audit_solve": audit, "common": common,
        "common_pass": common_pass, "tails": tails, "tail_pass": tail_pass,
        "S_C0_actual_guard": s_c0, "background_guard": background, "core_pass": core_pass,
        "source_hashes": source_hashes(),
        "thresholds": {"driver": physics.DRIVER_TOL, "holdout": physics.HOLDOUT_TOL,
                       "common": physics.LOW_COEFFICIENT_TOL, "tail": physics.TAIL_TOL,
                       "absolute_fallback": physics.ABS_FALLBACK_TOL,
                       "background_relative": physics.BACKGROUND_K_TOL},
        "runtime_limit_seconds": max_runtime_seconds, "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE", "release_trigger": "NONE", "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE", "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not finite_owner._all_finite(payload):
        raise FloatingPointError("non-finite value in KMPC-057 atom")
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = make_deadline(max_runtime_seconds)
    prerequisites = _load_c1(result_dir)
    atoms: dict[str, object] = {}
    backgrounds: dict[str, object] = {}
    for mode in MODES:
        for k_mpc in K_VALUES:
            name = atom_output_name(mode, k_mpc)
            path = result_dir / name
            payload = json.loads(path.read_text(encoding="utf-8"))
            identity = {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": VARIANT}
            if payload.get("identity") != identity or payload.get("candidate_interpretation_not_verdict") != "PASS_C2_FOURIER_ATOM_CANDIDATE_ONLY":
                raise RuntimeError(f"KMPC-057 aggregate atom mismatch: {name}")
            key = f"{mode}/k={k_mpc}"
            atoms[key] = {"file": name, "sha256": sha256_file(path),
                          "core_pass": payload["core_pass"], "common_pass": payload["common_pass"],
                          "tail_pass": payload["tail_pass"], "background_pass": payload["background_guard"]["pass"]}
            backgrounds[key] = payload["background_guard"]
            deadline()
    spread_rows: dict[str, object] = {}
    spread_pass = True
    for a in physics.A_VALUES_BACKGROUND:
        metrics: dict[str, object] = {}
        for quantity in ("D", "H_Mpc_inverse", "rho_f_over_rho_r", "rho_ash_over_rho_r"):
            values = [float(backgrounds[key]["by_a"][str(a)]["metrics"][quantity]["observed"]) for key in backgrounds]
            spread = (max(values) - min(values)) / max(max(abs(value) for value in values), 1.0e-300)
            passed = spread <= physics.BACKGROUND_K_TOL
            spread_pass = spread_pass and passed
            metrics[quantity] = {"relative_spread": spread, "pass": passed}
        spread_rows[str(a)] = metrics
    all_atoms_pass = all(all(row[field] for field in ("core_pass", "common_pass", "tail_pass", "background_pass")) for row in atoms.values())
    candidate = "PASS_C2_FOURIER_COVERAGE_10_OF_10_CANDIDATE_ONLY" if all_atoms_pass and spread_pass else "REVIEW_C2_AGGREGATE_GATE_UNCLOSED"
    payload = {
        "test": "A2-K4 P5.3g7 C2 Fourier coverage aggregate",
        "run_id": RUN_ID, "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
        "matrix": {"modes": list(MODES), "k_Mpc_inverse": list(K_VALUES), "variant": VARIANT,
                   "expected_atoms": 10, "observed_atoms": len(atoms)},
        "C1_prerequisites": prerequisites, "atoms": atoms, "all_atoms_pass": all_atoms_pass,
        "background_cross_mode_k_spread": spread_rows, "background_spread_pass": spread_pass,
        "source_hashes": source_hashes(), "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started, "score_effect": "NONE",
        "release_trigger": "NONE", "zenodo_trigger": "NONE", "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not finite_owner._all_finite(payload):
        raise FloatingPointError("non-finite value in KMPC-057 aggregate")
    return payload
