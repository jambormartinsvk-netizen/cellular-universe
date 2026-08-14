"""Hash-bound two-stage execution of one deep C2 Fourier atom.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
This module changes execution segmentation only; equations and thresholds remain
owned by :mod:`c2_fourier_coverage` and its frozen lineage.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path
import time

from . import c2_fourier_coverage as legacy


_CONFIG: dict[str, object] | None = None
_C1_BASELINE = {
    "AD": (0, 2), "CDI": (0, 5), "BI": (0, 5), "NID": (0, 5), "NIV": (-1, 4)
}
_ACCEPTED = (0, 7)
_AUDIT = (0, 9)
_DEPTH = 9


def configure(**config: object) -> None:
    global _CONFIG
    required = {
        "run_id", "phase", "output_name", "checkpoint_name", "checkpoint_sha256",
        "prerequisite_name", "prerequisite_sha256", "prerequisite_candidate",
    }
    if set(config) != required or _CONFIG is not None:
        raise RuntimeError("checkpointed C2 configuration is not exact or already set")
    if config["phase"] not in {"checkpoint", "resume"}:
        raise ValueError("checkpointed C2 phase must be checkpoint or resume")
    if config["phase"] == "checkpoint" and config["checkpoint_sha256"] is not None:
        raise ValueError("checkpoint phase cannot consume a checkpoint hash")
    if config["phase"] == "resume" and not config["checkpoint_sha256"]:
        raise ValueError("resume phase requires an exact checkpoint hash")
    _CONFIG = dict(config)


def _cfg() -> dict[str, object]:
    if _CONFIG is None:
        raise RuntimeError("checkpointed C2 module is not configured")
    return _CONFIG


def atom_output_name(mode: str, k_mpc: float) -> str:
    if mode != "CDI" or k_mpc != 0.005:
        raise ValueError("checkpointed C2 identity is only CDI/k=.005")
    return str(_cfg()["output_name"])


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return atom_output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def source_hashes() -> dict[str, str]:
    hashes = dict(legacy.source_hashes())
    here = Path(__file__).resolve().parent
    hashes["c2_checkpointed_single_atom.py"] = legacy.sha256_file(
        here / "c2_checkpointed_single_atom.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    checks = {
        "identity_exact": True,
        "C1_baseline_exact": _C1_BASELINE == {
            mode: tuple(spec["accepted"]) for mode, spec in legacy.SUPPORTS.items()
        },
        "support_exact": _ACCEPTED == (0, 7) and _AUDIT == (0, 9),
        "audit_is_plus2": _AUDIT == (_ACCEPTED[0], _ACCEPTED[1] + 2),
        "M1_depth_covers_audit": _DEPTH == _AUDIT[1],
        "surfaces_exact": tuple(legacy.physics.Z_SURFACES) == (1.0e-4, 1.0e-2),
        "thresholds_exact": bool(
            legacy.physics.LOW_COEFFICIENT_TOL == 1.0e-8
            and legacy.physics.TAIL_TOL == 1.0e-6
            and legacy.physics.ABS_FALLBACK_TOL == 1.0e-12
            and legacy.physics.BACKGROUND_K_TOL == 1.0e-12
            and legacy.physics.DRIVER_TOL == 1.0e-10
            and legacy.physics.HOLDOUT_TOL == 1.0e-9
        ),
    }
    return {
        "checks": checks,
        "pass": all(checks.values()),
        "C1_baseline": _C1_BASELINE,
        "ladder_spec": {"accepted": _ACCEPTED, "audit": _AUDIT, "m1_depth": _DEPTH},
    }


def _load_ordering(result_dir: Path) -> dict[str, object]:
    cfg = _cfg()
    path = result_dir / str(cfg["prerequisite_name"])
    observed = legacy.sha256_file(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    candidate = payload.get("candidate_interpretation_not_verdict")
    if observed != cfg["prerequisite_sha256"] or candidate != cfg["prerequisite_candidate"]:
        raise RuntimeError("checkpointed C2 ordering prerequisite mismatch")
    return {
        "file": path.name,
        "sha256": observed,
        "candidate": candidate,
        "role": "ORDERING_ONLY_NOT_PHYSICS_TRANSFER",
    }


def _restore_state(raw: dict[str, object]) -> dict[str, dict[int, float]]:
    return {
        name: {int(power): float(value) for power, value in values.items()}
        for name, values in raw.items()
    }


def _restore_accepted(raw: dict[str, object]) -> dict[str, object]:
    accepted = copy.deepcopy(raw)
    accepted["fuel"]["state"] = _restore_state(accepted["fuel"]["state"])
    accepted["m3"]["fractional_state"] = _restore_state(
        accepted["m3"]["fractional_state"]
    )
    return accepted


def _load_checkpoint(result_dir: Path) -> tuple[dict[str, object], dict[str, object]]:
    cfg = _cfg()
    path = result_dir / str(cfg["checkpoint_name"])
    observed = legacy.sha256_file(path)
    if observed != cfg["checkpoint_sha256"]:
        raise RuntimeError("checkpointed C2 immutable checkpoint hash mismatch")
    payload = json.loads(path.read_text(encoding="utf-8"))
    frozen = payload.get("checkpoint_contract", {})
    checks = {
        "execution_status": payload.get("execution_status")
        == "TECHNICAL_CHECKPOINT_COMPLETE_NO_PHYSICS_VERDICT",
        "candidate_role": payload.get("candidate_interpretation_not_verdict")
        == "CHECKPOINT_ONLY_NO_PHYSICS_VERDICT",
        "source_hashes": payload.get("source_hashes") == source_hashes(),
        "identity": frozen.get("identity") == {"mode": "CDI", "k_Mpc_inverse": 0.005},
        "accepted": frozen.get("accepted") == list(_ACCEPTED),
        "audit": frozen.get("audit") == list(_AUDIT),
        "m1_depth": frozen.get("m1_depth") == _DEPTH,
        "checkpoint_complete": payload.get("checkpoint_complete") is True,
    }
    if not all(checks.values()):
        raise RuntimeError(f"checkpointed C2 checkpoint contract mismatch: {checks}")
    return payload, {"file": path.name, "sha256": observed, "checks": checks}


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = legacy.make_deadline(max_runtime_seconds)
    cfg = _cfg()
    ordering = _load_ordering(result_dir)
    checks = {
        "phase_exact": cfg["phase"] in {"checkpoint", "resume"},
        "ordering": ordering["sha256"] == cfg["prerequisite_sha256"],
        "contract_guard": contract_guard()["pass"],
        "canonical_name": atom_output_name("CDI", 0.005) == cfg["output_name"],
    }
    if cfg["phase"] == "resume":
        checkpoint, checkpoint_meta = _load_checkpoint(result_dir)
        restored = _restore_state(checkpoint["standard_state"])
        restored_accepted = _restore_accepted(checkpoint["accepted_solve"])
        checks.update({
            "checkpoint_hash": checkpoint_meta["sha256"] == cfg["checkpoint_sha256"],
            "integer_standard_power_keys": all(
                all(isinstance(power, int) for power in values) for values in restored.values()
            ),
            "integer_accepted_power_keys": all(
                all(isinstance(power, int) for power in values)
                for values in restored_accepted["m3"]["fractional_state"].values()
            ),
        })
    deadline()
    return {
        "run_id": cfg["run_id"],
        "mode": "SMOKE_NO_RESULT_FILE",
        "checks": checks,
        "passed": all(checks.values()),
    }


def _checkpoint(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    cfg = _cfg()
    started, deadline = legacy.make_deadline(max_runtime_seconds)
    ordering = _load_ordering(result_dir)
    prerequisites = legacy._load_c1(result_dir)
    guard = contract_guard()
    frozen_contract = legacy.physics.validate_frozen_contract()
    independent_contract = legacy.ra_contract.validate_contract(
        legacy.collective_contract.EXPECTED_STATE,
        legacy.collective_contract.EXPECTED_DRIVER,
        legacy.collective_contract.EXPECTED_HOLDOUT,
    )
    frozen_b1 = legacy.physics.b1_guard.build_contract_guard(
        max_runtime_seconds=min(1.0, max_runtime_seconds)
    )
    tca0 = legacy.physics.production_tca0_reduction_guard()
    inputs = legacy.physics._variant_inputs(legacy.VARIANT)
    standard, m1 = legacy._standard_depth("CDI", 0.005, _DEPTH, inputs, deadline)
    rfs = legacy._rfs_guard("CDI", standard, inputs)
    accepted = (
        legacy._solve_support("CDI", 0.005, _ACCEPTED, inputs, standard, deadline)
        if m1["pass"] else {"pass": False, "status": "NOT_RUN_M1_BOUNDARY"}
    )
    preconditions = {
        "contract": guard["pass"],
        "C1_prerequisites": len(prerequisites) == 5,
        "frozen_contract": frozen_contract["valid"],
        "independent_contract": independent_contract.valid,
        "frozen_B1": frozen_b1["execution_verdict"] == "PASS_R_A_B1_CONTRACT_GUARD_ONLY",
        "TCA0": tca0["pass"],
        "M1": m1["pass"],
        "R_fs": rfs["pass"],
        "accepted": accepted["pass"],
    }
    deadline()
    return {
        "test": "A2-K4 P5.3g7 C2 checkpoint: depth-9 M1 plus accepted support",
        "run_id": cfg["run_id"],
        "atom_id": "CDI/k=0.005/support_07/checkpoint_only",
        "execution_status": "TECHNICAL_CHECKPOINT_COMPLETE_NO_PHYSICS_VERDICT",
        "candidate_interpretation_not_verdict": "CHECKPOINT_ONLY_NO_PHYSICS_VERDICT",
        "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
        "ordering_prerequisite": ordering,
        "checkpoint_contract": {
            "identity": {"mode": "CDI", "k_Mpc_inverse": 0.005},
            "accepted": list(_ACCEPTED), "audit": list(_AUDIT), "m1_depth": _DEPTH,
            "thresholds": {"common": 1.0e-8, "tail": 1.0e-6,
                           "absolute_fallback": 1.0e-12, "background": 1.0e-12,
                           "driver": 1.0e-10, "holdout": 1.0e-9},
            "role": "IMMUTABLE_INTERMEDIATE_NO_PHYSICS_VERDICT",
        },
        "C1_prerequisites": prerequisites,
        "contract_guard": guard,
        "frozen_contract": frozen_contract,
        "independent_contract_valid": independent_contract.valid,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "M1": m1,
        "combined_R_fs_guard": rfs,
        "standard_state": standard,
        "accepted_solve": accepted,
        "checkpoint_preconditions": preconditions,
        "checkpoint_complete": all(preconditions.values()),
        "core_pass": None,
        "common_pass": None,
        "tail_pass": None,
        "background_guard": {"pass": None, "status": "DEFERRED_TO_RESUME"},
        "source_hashes": source_hashes(),
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE", "release_trigger": "NONE", "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE", "orchestrator_verdict": "NOT_APPLICABLE_CHECKPOINT",
    }


def _resume(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    cfg = _cfg()
    started, deadline = legacy.make_deadline(max_runtime_seconds)
    ordering = _load_ordering(result_dir)
    checkpoint, checkpoint_meta = _load_checkpoint(result_dir)
    standard = _restore_state(checkpoint["standard_state"])
    accepted = _restore_accepted(checkpoint["accepted_solve"])
    inputs = legacy.physics._variant_inputs(legacy.VARIANT)
    m1 = checkpoint["M1"]
    audit = legacy._solve_support("CDI", 0.005, _AUDIT, inputs, standard, deadline)
    common = {
        "F0": legacy._common_bridge(accepted["fuel"]["state"], audit["fuel"]["state"], _ACCEPTED),
        "M3": legacy._common_bridge(
            accepted["m3"]["fractional_state"], audit["m3"]["fractional_state"], _ACCEPTED
        ),
    }
    tails = {
        "F0": legacy._tail(
            audit["fuel"]["state"], tuple(sorted(audit["fuel"]["state"])), _ACCEPTED, _AUDIT
        ),
        "M3": legacy._tail(
            audit["m3"]["fractional_state"], tuple(legacy.ra_contract.AUTHORITATIVE_STATE),
            _ACCEPTED, _AUDIT,
        ),
    }
    s_c0 = legacy.support_tools.c1._s_c0_actual_coefficient_guard({
        "m3_primary": {"fractional_state": accepted["m3"]["fractional_state"]},
        "m3_extended": {"fractional_state": audit["m3"]["fractional_state"]},
    })
    background = legacy._background_guard(inputs, 0.005, _AUDIT[1])
    common_pass = all(row["pass"] for row in common.values())
    tail_pass = all(row["pass"] for row in tails.values())
    preconditions = checkpoint["checkpoint_preconditions"]
    core_pass = bool(all(preconditions.values()) and audit["pass"] and s_c0["pass"])
    if not m1["pass"]:
        candidate = "REVIEW_C2_M1_NUMERICAL_BOUNDARY"
    elif not core_pass:
        candidate = "REVIEW_C2_CORE_GATE_UNCLOSED"
    elif not common_pass:
        candidate = "REVIEW_C2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED"
    elif not tail_pass:
        candidate = "REVIEW_C2_CDI_K0p005_SUPPORT_09_11_REQUIRED"
    elif not background["pass"]:
        candidate = "STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY"
    else:
        candidate = "PASS_C2_CDI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY"
    deadline()
    payload = {
        "test": "A2-K4 P5.3g7 C2 checkpoint-resumed Fourier atom",
        "run_id": cfg["run_id"], "atom_id": "CDI/k=0.005/support_07_09/checkpoint_resume",
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
        "identity": {"mode": "CDI", "k_Mpc_inverse": 0.005, "variant": legacy.VARIANT},
        "scope": {"included": "one checkpoint-resumed C2 CDI/k=.005 support atom",
                  "excluded": "other atoms, C3, full hierarchy, ODE, G8/G9, data"},
        "ordering_prerequisite": ordering,
        "checkpoint_prerequisite": checkpoint_meta,
        "C1_prerequisites": checkpoint["C1_prerequisites"],
        "contract_guard": checkpoint["contract_guard"],
        "frozen_contract": checkpoint["frozen_contract"],
        "independent_contract_valid": checkpoint["independent_contract_valid"],
        "frozen_B1_left_null_Bianchi": checkpoint["frozen_B1_left_null_Bianchi"],
        "production_TCA0_bridge": checkpoint["production_TCA0_bridge"],
        "support_depth_spec": {"accepted": list(_ACCEPTED), "audit": list(_AUDIT),
                               "m1_depth": _DEPTH},
        "M1": m1,
        "combined_R_fs_guard": checkpoint["combined_R_fs_guard"],
        "accepted_solve": accepted, "audit_solve": audit,
        "common": common, "common_pass": common_pass,
        "tails": tails, "tail_pass": tail_pass,
        "S_C0_actual_guard": s_c0, "background_guard": background, "core_pass": core_pass,
        "source_hashes": source_hashes(),
        "thresholds": {"driver": legacy.physics.DRIVER_TOL,
                       "holdout": legacy.physics.HOLDOUT_TOL,
                       "common": legacy.physics.LOW_COEFFICIENT_TOL,
                       "tail": legacy.physics.TAIL_TOL,
                       "absolute_fallback": legacy.physics.ABS_FALLBACK_TOL,
                       "background_relative": legacy.physics.BACKGROUND_K_TOL},
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checkpoint_runtime_seconds": checkpoint["runtime_seconds"],
        "score_effect": "NONE", "release_trigger": "NONE", "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE", "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not legacy.finite_owner._all_finite(payload):
        raise FloatingPointError("non-finite value in checkpoint-resumed C2 atom")
    return payload


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    atom_output_name(mode, k_mpc)
    return (_checkpoint(max_runtime_seconds, result_dir)
            if _cfg()["phase"] == "checkpoint" else _resume(max_runtime_seconds, result_dir))


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("checkpointed C2 single atom has no aggregate scope")
