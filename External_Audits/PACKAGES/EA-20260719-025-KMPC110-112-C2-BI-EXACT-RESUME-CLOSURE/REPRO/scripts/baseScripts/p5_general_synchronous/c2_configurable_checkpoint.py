"""Configurable hash-bound checkpoint wrapper for one deep C2 atom.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only execution identity, segmentation and state-order restoration are adapted;
all equations, solvers, supports and thresholds remain owned by the frozen C2
lineage.
"""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
from typing import Iterator

from . import c2_checkpointed_single_atom as v1
from . import c2_checkpointed_single_atom_v3_phase_order as phase_order


_CONFIG: dict[str, object] | None = None
_V1_SOURCE_HASHES = v1.source_hashes
_V1_CONTRACT_GUARD = v1.contract_guard
_V1_LOAD_CHECKPOINT = v1._load_checkpoint
_V1_RESTORE_STATE = v1._restore_state
_OLD_STANDARD_DEPTH = v1.legacy._standard_depth
_OLD_RFS_GUARD = v1.legacy._rfs_guard
_OLD_SOLVE_SUPPORT = v1.legacy._solve_support
_OLD_BACKGROUND_GUARD = v1.legacy._background_guard
_OLD_ACCEPTED = v1._ACCEPTED
_OLD_AUDIT = v1._AUDIT
_OLD_DEPTH = v1._DEPTH


def configure(**config: object) -> None:
    global _CONFIG
    required = {
        "run_id", "phase", "mode", "k_mpc", "accepted", "audit", "m1_depth",
        "output_name", "checkpoint_name", "checkpoint_sha256",
        "prerequisite_name", "prerequisite_sha256", "prerequisite_candidate",
    }
    if set(config) != required or _CONFIG is not None:
        raise RuntimeError("configurable checkpoint configuration is not exact or already set")
    accepted = tuple(config["accepted"])
    audit = tuple(config["audit"])
    mode = str(config["mode"])
    k_mpc = float(config["k_mpc"])
    if mode not in v1.legacy.MODES or k_mpc not in v1.legacy.K_VALUES:
        raise ValueError("unsupported C2 checkpoint identity")
    if audit != (accepted[0], accepted[1] + 2) or int(config["m1_depth"]) != audit[1]:
        raise ValueError("checkpoint support ladder or depth mismatch")
    _CONFIG = dict(config)
    _CONFIG.update({"accepted": accepted, "audit": audit, "mode": mode, "k_mpc": k_mpc})
    v1.configure(**{name: config[name] for name in (
        "run_id", "phase", "output_name", "checkpoint_name", "checkpoint_sha256",
        "prerequisite_name", "prerequisite_sha256", "prerequisite_candidate",
    )})


def _cfg() -> dict[str, object]:
    if _CONFIG is None:
        raise RuntimeError("configurable checkpoint is not configured")
    return _CONFIG


def atom_output_name(mode: str, k_mpc: float) -> str:
    cfg = _cfg()
    if mode != cfg["mode"] or k_mpc != cfg["k_mpc"]:
        raise ValueError("atom differs from configured checkpoint identity")
    return str(cfg["output_name"])


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return atom_output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def source_hashes() -> dict[str, str]:
    hashes = dict(_V1_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_checkpointed_single_atom_v3_phase_order.py"] = v1.legacy.sha256_file(
        here / "c2_checkpointed_single_atom_v3_phase_order.py"
    )
    hashes["c2_configurable_checkpoint.py"] = v1.legacy.sha256_file(
        here / "c2_configurable_checkpoint.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    cfg = _cfg()
    accepted = tuple(cfg["accepted"])
    audit = tuple(cfg["audit"])
    checks = {
        "identity_exact": cfg["mode"] in v1.legacy.MODES and cfg["k_mpc"] in v1.legacy.K_VALUES,
        "C1_baseline_exact": v1._C1_BASELINE == {
            mode: tuple(spec["accepted"]) for mode, spec in v1.legacy.SUPPORTS.items()
        },
        "support_exact": accepted == (0, 7) and audit == (0, 9),
        "audit_is_plus2": audit == (accepted[0], accepted[1] + 2),
        "M1_depth_covers_audit": cfg["m1_depth"] == audit[1],
        "surfaces_exact": tuple(v1.legacy.physics.Z_SURFACES) == (1.0e-4, 1.0e-2),
        "thresholds_exact": bool(
            v1.legacy.physics.LOW_COEFFICIENT_TOL == 1.0e-8
            and v1.legacy.physics.TAIL_TOL == 1.0e-6
            and v1.legacy.physics.ABS_FALLBACK_TOL == 1.0e-12
            and v1.legacy.physics.BACKGROUND_K_TOL == 1.0e-12
            and v1.legacy.physics.DRIVER_TOL == 1.0e-10
            and v1.legacy.physics.HOLDOUT_TOL == 1.0e-9
        ),
    }
    return {"checks": checks, "pass": all(checks.values()),
            "C1_baseline": v1._C1_BASELINE,
            "ladder_spec": {"accepted": accepted, "audit": audit,
                            "m1_depth": cfg["m1_depth"]}}


def _translate_mode(mode: str, k_mpc: float) -> tuple[str, float]:
    if mode != "CDI" or k_mpc != 0.005:
        raise RuntimeError("unexpected legacy checkpoint call identity")
    cfg = _cfg()
    return str(cfg["mode"]), float(cfg["k_mpc"])


def _standard_depth(mode, k_mpc, depth, inputs, deadline):
    mapped_mode, mapped_k = _translate_mode(mode, k_mpc)
    if depth != _cfg()["m1_depth"]:
        raise RuntimeError("legacy checkpoint depth differs from configuration")
    return _OLD_STANDARD_DEPTH(mapped_mode, mapped_k, depth, inputs, deadline)


def _rfs_guard(mode, standard, inputs):
    mapped_mode, _ = _translate_mode(mode, 0.005)
    return _OLD_RFS_GUARD(mapped_mode, standard, inputs)


def _solve_support(mode, k_mpc, support, inputs, standard, deadline):
    mapped_mode, mapped_k = _translate_mode(mode, k_mpc)
    return _OLD_SOLVE_SUPPORT(mapped_mode, mapped_k, support, inputs, standard, deadline)


def _background_guard(inputs, k_mpc, depth):
    _, mapped_k = _translate_mode("CDI", k_mpc)
    return _OLD_BACKGROUND_GUARD(inputs, mapped_k, depth)


def _load_checkpoint(result_dir: Path) -> tuple[dict[str, object], dict[str, object]]:
    cfg = _cfg()
    path = result_dir / str(cfg["checkpoint_name"])
    observed = v1.legacy.sha256_file(path)
    if observed != cfg["checkpoint_sha256"]:
        raise RuntimeError("configurable C2 immutable checkpoint hash mismatch")
    payload = json.loads(path.read_text(encoding="utf-8"))
    frozen = payload.get("checkpoint_contract", {})
    checks = {
        "execution_status": payload.get("execution_status")
        == "TECHNICAL_CHECKPOINT_COMPLETE_NO_PHYSICS_VERDICT",
        "candidate_role": payload.get("candidate_interpretation_not_verdict")
        == "CHECKPOINT_ONLY_NO_PHYSICS_VERDICT",
        "source_hashes": payload.get("source_hashes") == source_hashes(),
        "identity": frozen.get("identity") == {
            "mode": cfg["mode"], "k_Mpc_inverse": cfg["k_mpc"]
        },
        "accepted": frozen.get("accepted") == list(cfg["accepted"]),
        "audit": frozen.get("audit") == list(cfg["audit"]),
        "m1_depth": frozen.get("m1_depth") == cfg["m1_depth"],
        "checkpoint_complete": payload.get("checkpoint_complete") is True,
    }
    if not all(checks.values()):
        raise RuntimeError(f"configurable C2 checkpoint contract mismatch: {checks}")
    return payload, {"file": path.name, "sha256": observed, "checks": checks}


@contextmanager
def _overlay() -> Iterator[None]:
    before = (v1.source_hashes, v1.contract_guard, v1._load_checkpoint,
              v1._restore_state, v1._ACCEPTED, v1._AUDIT, v1._DEPTH,
              v1.legacy._standard_depth, v1.legacy._rfs_guard,
              v1.legacy._solve_support, v1.legacy._background_guard)
    cfg = _cfg()
    try:
        v1.source_hashes = source_hashes
        v1.contract_guard = contract_guard
        v1._load_checkpoint = _load_checkpoint
        v1._restore_state = phase_order._restore_state
        v1._ACCEPTED, v1._AUDIT, v1._DEPTH = (
            tuple(cfg["accepted"]), tuple(cfg["audit"]), int(cfg["m1_depth"])
        )
        v1.legacy._standard_depth = _standard_depth
        v1.legacy._rfs_guard = _rfs_guard
        v1.legacy._solve_support = _solve_support
        v1.legacy._background_guard = _background_guard
        yield
    finally:
        (v1.source_hashes, v1.contract_guard, v1._load_checkpoint,
         v1._restore_state, v1._ACCEPTED, v1._AUDIT, v1._DEPTH,
         v1.legacy._standard_depth, v1.legacy._rfs_guard,
         v1.legacy._solve_support, v1.legacy._background_guard) = before


def _owners_restored() -> bool:
    return bool(v1.source_hashes is _V1_SOURCE_HASHES
                and v1.contract_guard is _V1_CONTRACT_GUARD
                and v1._load_checkpoint is _V1_LOAD_CHECKPOINT
                and v1._restore_state is _V1_RESTORE_STATE
                and v1._ACCEPTED == _OLD_ACCEPTED and v1._AUDIT == _OLD_AUDIT
                and v1._DEPTH == _OLD_DEPTH
                and v1.legacy._standard_depth is _OLD_STANDARD_DEPTH
                and v1.legacy._rfs_guard is _OLD_RFS_GUARD
                and v1.legacy._solve_support is _OLD_SOLVE_SUPPORT
                and v1.legacy._background_guard is _OLD_BACKGROUND_GUARD)


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    cfg = _cfg()
    _, deadline = v1.legacy.make_deadline(max_runtime_seconds)
    ordering = v1._load_ordering(result_dir)
    checks = {"ordering": ordering["sha256"] == cfg["prerequisite_sha256"],
              "contract_guard": contract_guard()["pass"],
              "canonical_name": atom_output_name(str(cfg["mode"]), float(cfg["k_mpc"]))
              == cfg["output_name"]}
    if cfg["phase"] == "resume":
        with _overlay():
            checkpoint, meta = _load_checkpoint(result_dir)
            standard = phase_order._restore_state(checkpoint["standard_state"])
        authoritative = tuple(v1.legacy.ra_contract.AUTHORITATIVE_STATE)
        combined = tuple(standard) + ("delta_f", "U_f")
        checks.update({"checkpoint_hash": meta["sha256"] == cfg["checkpoint_sha256"],
                       "standard_11_state_order": len(standard) == 11,
                       "combined_13_state_order": combined == authoritative})
    wrong_rejected = False
    try:
        atom_output_name(str(cfg["mode"]), 0.15 if cfg["k_mpc"] == 0.005 else 0.005)
    except ValueError:
        wrong_rejected = True
    checks["wrong_atom_rejected"] = wrong_rejected
    checks["owners_restored"] = _owners_restored()
    deadline()
    return {"run_id": cfg["run_id"], "mode": "SMOKE_NO_RESULT_FILE",
            "checks": checks, "passed": all(checks.values())}


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float,
             result_dir: Path) -> dict[str, object]:
    cfg = _cfg()
    atom_output_name(mode, k_mpc)
    with _overlay():
        payload = (v1._checkpoint(max_runtime_seconds, result_dir)
                   if cfg["phase"] == "checkpoint"
                   else v1._resume(max_runtime_seconds, result_dir))
    if not _owners_restored():
        raise RuntimeError("configurable checkpoint overlay owners were not restored")
    identity = {"mode": cfg["mode"], "k_Mpc_inverse": cfg["k_mpc"]}
    payload["atom_id"] = f"{cfg['mode']}/k={cfg['k_mpc']}/support_07_09/{cfg['phase']}"
    if cfg["phase"] == "checkpoint":
        payload["checkpoint_contract"]["identity"] = identity
        payload["source_hashes"] = source_hashes()
    else:
        payload["identity"].update(identity)
        payload["scope"]["included"] = (
            f"one checkpoint-resumed C2 {cfg['mode']}/k={cfg['k_mpc']} support atom"
        )
        if payload["core_pass"] and payload["common_pass"] and payload["tail_pass"]:
            token = v1.legacy.k_token(float(cfg["k_mpc"]))
            payload["candidate_interpretation_not_verdict"] = (
                f"PASS_C2_{cfg['mode']}_K{token}_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY"
            )
        elif payload["core_pass"] and payload["common_pass"] and not payload["tail_pass"]:
            token = v1.legacy.k_token(float(cfg["k_mpc"]))
            payload["candidate_interpretation_not_verdict"] = (
                f"REVIEW_C2_{cfg['mode']}_K{token}_SUPPORT_09_11_REQUIRED"
            )
        observed = tuple(payload["audit_solve"]["m3"]["diagnostics"]
                         ["production_contract"]["implemented_state"])
        authoritative = tuple(v1.legacy.ra_contract.AUTHORITATIVE_STATE)
        payload["state_order_successor"] = {
            "authoritative_tuple": list(authoritative),
            "observed_tuple": list(observed),
            "pass": observed == authoritative,
            "delta": "CONFIGURABLE_PHASE_AWARE_EXECUTION_ONLY",
        }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("configurable checkpoint has no aggregate scope")
