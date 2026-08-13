"""Read-only C2 aggregate over the ten authoritative mode-by-k atom raws.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
This module reads frozen JSON receipts only; it imports no physics solver.
"""

from __future__ import annotations

import hashlib
import json
import math
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Mapping


RUN_ID = "KMPC-127"
MODES = ("AD", "CDI", "BI", "NID", "NIV")
K_VALUES = (0.005, 0.15)
A_KEYS = ("1e-08", "3e-08")
BACKGROUND_QUANTITIES = (
    "D",
    "H_Mpc_inverse",
    "rho_f_over_rho_r",
    "rho_ash_over_rho_r",
)
BACKGROUND_SPREAD_TOL = 1.0e-12
EXECUTION_STATUS = "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT"


@dataclass(frozen=True)
class AtomSpec:
    mode: str
    k_mpc: float
    filename: str
    sha256: str
    candidate: str

    @property
    def key(self) -> str:
        return f"{self.mode}/k={self.k_mpc}"


ATOM_SPECS = (
    AtomSpec("AD", 0.005, "RUN_KMPC_063_P5_3G7_C2_AD_K0p005_SUPPORT_06_08.json",
             "CB0CEA5DD92BF85F0F0066FAD8DE77D5F8247B02B864FACF92FA374E0FBC85BD",
             "PASS_C2_AD_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY"),
    AtomSpec("AD", 0.15, "RUN_KMPC_066_P5_3G7_C2_AD_K0p15_SUPPORT_04_06.json",
             "81370874BCF25123565FBB117EDFEB4D51F12560CCC04BDC8CCDFC0DF8FDE816",
             "PASS_C2_AD_K0p15_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY"),
    AtomSpec("CDI", 0.005,
             "RUN_KMPC_073_P5_3G7_C2_CDI_K0p005_SUPPORT_07_09_PHASE_ORDER_SUCCESSOR.json",
             "B7B2B7231E20D90D7EA71F1934B795296B7B0C2772148988C0FCFB2CF96E8498",
             "PASS_C2_CDI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY"),
    AtomSpec("CDI", 0.15, "RUN_KMPC_075_P5_3G7_C2_CDI_K0p15_SAME_MATRIX_REFINEMENT.json",
             "19F5F0B38CFE62C6E2ECA277EE5F959D866967027C5AF721CF4B2E1A30B999B9",
             "PASS_C2_CDI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY"),
    AtomSpec("BI", 0.005,
             "RUN_KMPC_078_P5_3G7_C2_BI_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json",
             "F24894A043B531825DD36A424637D1E70244F89B66678AF945EA6C135918A359",
             "PASS_C2_BI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY"),
    AtomSpec(
        "BI", 0.15,
        "RUN_KMPC_112_P5_3G7_C2_BI_K0p15_HP_M1_CHECKPOINT_EXACT_RESUME_JSON_PARITY_SUCCESSOR.json",
        "FAF52256489BA7C105F9125C1ED9A68358C0187E5F7B8B1164E1BA036A6507A1",
        "PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY",
    ),
    AtomSpec("NID", 0.005,
             "RUN_KMPC_115_P5_3G7_C2_NID_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json",
             "7D7B9BC1F2874A20E0CB8116D657F7C0419D03B284D0161CFFDF89112B4E0851",
             "PASS_C2_NID_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY"),
    AtomSpec("NID", 0.15, "RUN_KMPC_117_P5_3G7_C2_NID_K0p15_SAME_MATRIX_REFINEMENT.json",
             "F9BE1AC95575B0A71E73596384360ADC382C651EE4C8BA067DD4313C4BE6C7C4",
             "PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY"),
    AtomSpec("NIV", 0.005,
             "RUN_KMPC_120_P5_3G7_C2_NIV_K0p005_SUPPORT_06_08_CHECKPOINT_RESUME.json",
             "D6350636F9BA27C541EF8CDC2585ED370E2F1E2EB35495E01198A8BAA47AB136",
             "PASS_C2_NIV_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY"),
    AtomSpec(
        "NIV", 0.15,
        "RUN_KMPC_126_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_MULTI_RANK_REFINEMENT.json",
        "1D46AFD1CDEB650A7787A5E6FE9E2304A5212FF1FE9AA47657BEAAAA557B8AA0",
        "PASS_C2_NIV_K0p15_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY",
    ),
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def make_deadline(max_runtime_seconds: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(max_runtime_seconds) or not 0.0 < max_runtime_seconds <= 4.8:
        raise ValueError("max_runtime_seconds must be finite and in (0, 4.8]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError(f"{RUN_ID} internal deadline exceeded")

    return started, deadline


def _require_mapping(container: Mapping[str, object], key: str) -> Mapping[str, object]:
    if key not in container or not isinstance(container[key], dict):
        raise KeyError(f"missing or non-object key: {key}")
    return container[key]  # type: ignore[return-value]


def _require_true(container: Mapping[str, object], key: str) -> bool:
    if key not in container or not isinstance(container[key], bool):
        raise KeyError(f"missing or non-boolean key: {key}")
    return container[key] is True


def _finite_number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{label} is not numeric")
    number = float(value)
    if not math.isfinite(number):
        raise FloatingPointError(f"{label} is non-finite")
    return number


def _contract_guard() -> dict[str, object]:
    identities = [(spec.mode, spec.k_mpc) for spec in ATOM_SPECS]
    expected = [(mode, k_mpc) for mode in MODES for k_mpc in K_VALUES]
    checks = {
        "ten_specs_exact": len(ATOM_SPECS) == 10,
        "cartesian_order_exact": identities == expected,
        "no_duplicate_identity": len(set(identities)) == 10,
        "no_duplicate_filename": len({spec.filename for spec in ATOM_SPECS}) == 10,
        "sha256_shape_exact": all(
            len(spec.sha256) == 64
            and all(char in "0123456789ABCDEF" for char in spec.sha256)
            for spec in ATOM_SPECS
        ),
        "pass_candidates_only": all(
            spec.candidate.startswith("PASS_C2_")
            and "TECHNICAL_FAILURE" not in spec.candidate
            for spec in ATOM_SPECS
        ),
        "background_contract_exact": (
            A_KEYS == ("1e-08", "3e-08")
            and BACKGROUND_QUANTITIES
            == ("D", "H_Mpc_inverse", "rho_f_over_rho_r", "rho_ash_over_rho_r")
            and BACKGROUND_SPREAD_TOL == 1.0e-12
        ),
    }
    return {"checks": checks, "pass": all(checks.values())}


def _load_atom(
    result_dir: Path,
    spec: AtomSpec,
    deadline: Callable[[], None],
) -> dict[str, object]:
    deadline()
    path = result_dir / spec.filename
    if not path.is_file():
        raise FileNotFoundError(f"missing frozen C2 atom: {spec.filename}")
    observed_hash = sha256_file(path)
    if observed_hash != spec.sha256:
        raise RuntimeError(
            f"SHA-256 mismatch for {spec.filename}: {observed_hash} != {spec.sha256}"
        )
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError(f"atom payload is not an object: {spec.filename}")
    identity = payload.get("identity")
    expected_identity = {
        "mode": spec.mode,
        "k_Mpc_inverse": spec.k_mpc,
        "variant": "nominal",
    }
    if identity != expected_identity:
        raise RuntimeError(f"identity mismatch for {spec.filename}")
    candidate = payload.get("candidate_interpretation_not_verdict")
    if candidate != spec.candidate:
        raise RuntimeError(f"candidate mismatch for {spec.filename}")
    status = payload.get("execution_status")
    if status != EXECUTION_STATUS:
        raise RuntimeError(f"execution status mismatch for {spec.filename}")
    if "TECHNICAL_FAILURE" in str(status) or "TECHNICAL_FAILURE" in str(candidate):
        raise RuntimeError(f"technical failure selected as atom: {spec.filename}")

    gates = {
        "core_pass": _require_true(payload, "core_pass"),
        "common_pass": _require_true(payload, "common_pass"),
        "tail_pass": _require_true(payload, "tail_pass"),
    }
    background = _require_mapping(payload, "background_guard")
    gates["background_pass"] = _require_true(background, "pass")
    by_a = _require_mapping(background, "by_a")
    observed: dict[str, dict[str, float]] = {}
    nested_background_pass = True
    for a_key in A_KEYS:
        row = _require_mapping(by_a, a_key)
        nested_background_pass = nested_background_pass and _require_true(row, "pass")
        metrics = _require_mapping(row, "metrics")
        observed[a_key] = {}
        for quantity in BACKGROUND_QUANTITIES:
            metric = _require_mapping(metrics, quantity)
            nested_background_pass = (
                nested_background_pass and _require_true(metric, "pass")
            )
            if "observed" not in metric:
                raise KeyError(f"missing observed value: {spec.filename}:{a_key}:{quantity}")
            observed[a_key][quantity] = _finite_number(
                metric["observed"], f"{spec.filename}:{a_key}:{quantity}"
            )
    gates["nested_background_pass"] = nested_background_pass
    deadline()
    return {
        "spec": spec,
        "path": path,
        "sha256": observed_hash,
        "payload": payload,
        "gates": gates,
        "background_observed": observed,
    }


def _aggregate_loaded(
    loaded: list[dict[str, object]],
    runtime_limit_seconds: float,
    runtime_seconds: float,
) -> dict[str, object]:
    expected_keys = [spec.key for spec in ATOM_SPECS]
    observed_keys = [entry["spec"].key for entry in loaded]  # type: ignore[union-attr]
    exact_register_pass = (
        len(loaded) == 10
        and observed_keys == expected_keys
        and len(set(observed_keys)) == 10
    )
    atom_rows: dict[str, object] = {}
    backgrounds: dict[str, dict[str, dict[str, float]]] = {}
    all_atoms_pass = True
    for entry in loaded:
        spec = entry["spec"]
        if not isinstance(spec, AtomSpec):
            raise TypeError("internal aggregate entry has invalid AtomSpec")
        gates = entry["gates"]
        if not isinstance(gates, dict):
            raise TypeError("internal aggregate entry has invalid gates")
        gate_pass = all(value is True for value in gates.values())
        all_atoms_pass = all_atoms_pass and gate_pass
        background = entry["background_observed"]
        if not isinstance(background, dict):
            raise TypeError("internal aggregate entry has invalid background")
        backgrounds[spec.key] = background  # type: ignore[assignment]
        payload = entry["payload"]
        if not isinstance(payload, dict):
            raise TypeError("internal aggregate entry has invalid payload")
        atom_rows[spec.key] = {
            "file": spec.filename,
            "sha256": entry["sha256"],
            "run_id": payload.get("run_id"),
            "identity": payload.get("identity"),
            "candidate_interpretation_not_verdict": (
                payload.get("candidate_interpretation_not_verdict")
            ),
            "execution_status": payload.get("execution_status"),
            "gates": gates,
            "all_required_gates_pass": gate_pass,
            "technical_failure_rejected": True,
        }

    spread_rows: dict[str, object] = {}
    spread_pass = True
    worst = (0.0, "none")
    for a_key in A_KEYS:
        metrics: dict[str, object] = {}
        for quantity in BACKGROUND_QUANTITIES:
            values = [backgrounds[key][a_key][quantity] for key in expected_keys]
            denominator = max(max(abs(value) for value in values), 1.0e-300)
            spread = (max(values) - min(values)) / denominator
            if not math.isfinite(spread):
                raise FloatingPointError(f"non-finite spread: {a_key}:{quantity}")
            passed = spread <= BACKGROUND_SPREAD_TOL
            spread_pass = spread_pass and passed
            worst = max(worst, (spread, f"a={a_key}:{quantity}"))
            metrics[quantity] = {
                "minimum": min(values),
                "maximum": max(values),
                "relative_spread": spread,
                "threshold": BACKGROUND_SPREAD_TOL,
                "pass": passed,
            }
        spread_rows[a_key] = {"metrics": metrics, "pass": all(
            bool(row["pass"]) for row in metrics.values()  # type: ignore[index]
        )}

    aggregate_pass = exact_register_pass and all_atoms_pass and spread_pass
    candidate = (
        "PASS_C2_FOURIER_COVERAGE_10_OF_10_CANDIDATE_ONLY"
        if aggregate_pass
        else "REVIEW_C2_AGGREGATE_GATE_UNCLOSED"
    )
    contract = _contract_guard()
    if contract["pass"] is not True:
        raise RuntimeError("frozen aggregate contract guard failed")
    return {
        "test": "A2-K4 P5.3g7 C2 authoritative atom coverage aggregate",
        "run_id": RUN_ID,
        "execution_status": EXECUTION_STATUS,
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "scope": {
            "included": (
                "read-only exact-hash C2 5-mode x 2-k atom register and "
                "cross-mode/cross-k background spread"
            ),
            "excluded": (
                "new solve, coefficient correction, C3 gamma0/af0, S-M, "
                "full hierarchy, ODE/P5.4, G8/G9 and data"
            ),
        },
        "read_only_no_physics_solve": True,
        "contract_guard": contract,
        "matrix": {
            "modes": list(MODES),
            "k_Mpc_inverse": list(K_VALUES),
            "variant": "nominal",
            "expected_atoms": 10,
            "observed_atoms": len(loaded),
            "expected_register": expected_keys,
            "observed_register": observed_keys,
            "exact_cartesian_register_pass": exact_register_pass,
        },
        "atoms": atom_rows,
        "all_atoms_pass": all_atoms_pass,
        "technical_failure_outputs_selected": 0,
        "technical_failure_exclusion_pass": True,
        "background_cross_mode_k_spread": spread_rows,
        "background_spread_threshold": BACKGROUND_SPREAD_TOL,
        "background_spread_pass": spread_pass,
        "worst_background_spread": {
            "relative_spread": worst[0],
            "label": worst[1],
        },
        "aggregate_gate_pass": aggregate_pass,
        "runtime_limit_seconds": runtime_limit_seconds,
        "runtime_seconds": runtime_seconds,
        "score_effect": "NONE",
        "K4_score_effect": "NONE_60_OF_100_UNCHANGED",
        "C3_effect": "UNLOCK_ONLY_IF_ORCHESTRATOR_ACCEPTS_C2_AGGREGATE_PASS",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = make_deadline(max_runtime_seconds)
    contract = _contract_guard()
    if contract["pass"] is not True:
        raise RuntimeError("frozen aggregate contract guard failed")
    loaded = [_load_atom(result_dir, spec, deadline) for spec in ATOM_SPECS]
    deadline()
    return _aggregate_loaded(
        loaded,
        runtime_limit_seconds=max_runtime_seconds,
        runtime_seconds=time.monotonic() - started,
    )


def run_smoke() -> dict[str, object]:
    checks: dict[str, bool] = {}
    contract = _contract_guard()
    checks["contract_guard"] = contract["pass"] is True
    try:
        _require_true({}, "missing")
    except KeyError:
        checks["AR51_missing_boolean_fail_closed"] = True
    else:
        checks["AR51_missing_boolean_fail_closed"] = False
    with tempfile.TemporaryDirectory(prefix="kmpc127_missing_") as directory:
        try:
            run_aggregate(1.0, Path(directory))
        except FileNotFoundError:
            checks["missing_atom_fail_closed"] = True
        else:
            checks["missing_atom_fail_closed"] = False
    checks["no_solver_symbols"] = all(
        name not in globals() for name in ("numpy", "solve", "lstsq", "mpmath")
    )
    return {
        "run_id": RUN_ID,
        "smoke_checks": checks,
        "pass": all(checks.values()),
        "physics_executed": False,
    }
