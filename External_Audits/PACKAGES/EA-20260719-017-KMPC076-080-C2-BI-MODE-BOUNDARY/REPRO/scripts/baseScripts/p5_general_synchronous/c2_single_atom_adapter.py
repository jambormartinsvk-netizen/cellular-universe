"""Reusable configured adapter for one immutable C2 Fourier atom.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
This module owns no equations or thresholds.
"""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
from typing import Iterator

from . import c2_fourier_coverage as legacy


_CONFIG: dict[str, object] | None = None
_C1_BASELINE = {
    "AD": (0, 2), "CDI": (0, 5), "BI": (0, 5), "NID": (0, 5), "NIV": (-1, 4)
}
_LEGACY_RUN_ID = legacy.RUN_ID
_LEGACY_SUPPORTS = legacy.SUPPORTS
_LEGACY_CONTRACT_GUARD = legacy.contract_guard
_LEGACY_SOURCE_HASHES = legacy.source_hashes
_LEGACY_ATOM_OUTPUT_NAME = legacy.atom_output_name
_LEGACY_ATOM_FAILURE_NAME = legacy.atom_failure_name


def configure(**config: object) -> None:
    global _CONFIG
    required = {
        "run_id", "mode", "k_mpc", "output_name", "accepted", "audit", "m1_depth",
        "prerequisite_name", "prerequisite_sha256", "prerequisite_candidate",
    }
    if set(config) != required or _CONFIG is not None:
        raise RuntimeError("C2 single-atom adapter configuration is not exact or already set")
    accepted = tuple(config["accepted"])
    audit = tuple(config["audit"])
    mode = str(config["mode"])
    k_mpc = float(config["k_mpc"])
    if mode not in legacy.MODES or k_mpc not in legacy.K_VALUES:
        raise ValueError("unsupported C2 atom identity")
    if audit != (accepted[0], accepted[1] + 2) or int(config["m1_depth"]) != audit[1]:
        raise ValueError("support ladder or M1 depth mismatch")
    _CONFIG = dict(config)
    _CONFIG["accepted"] = accepted
    _CONFIG["audit"] = audit


def _cfg() -> dict[str, object]:
    if _CONFIG is None:
        raise RuntimeError("C2 single-atom adapter is not configured")
    return _CONFIG


def atom_output_name(mode: str, k_mpc: float) -> str:
    cfg = _cfg()
    if mode != cfg["mode"] or k_mpc != cfg["k_mpc"]:
        raise ValueError("atom differs from configured C2 identity")
    return str(cfg["output_name"])


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return atom_output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def source_hashes() -> dict[str, str]:
    hashes = dict(_LEGACY_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_single_atom_adapter.py"] = legacy.sha256_file(here / "c2_single_atom_adapter.py")
    return hashes


def _load_prerequisite(result_dir: Path) -> dict[str, object]:
    cfg = _cfg()
    path = result_dir / str(cfg["prerequisite_name"])
    observed = legacy.sha256_file(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    candidate = payload.get("candidate_interpretation_not_verdict")
    if observed != cfg["prerequisite_sha256"] or candidate != cfg["prerequisite_candidate"]:
        raise RuntimeError("immutable ordering prerequisite mismatch")
    return {"file": path.name, "sha256": observed, "candidate": candidate,
            "role": "ORDERING_ONLY_NOT_PHYSICS_TRANSFER"}


def contract_guard() -> dict[str, object]:
    cfg = _cfg()
    checks = {
        "identity_supported": cfg["mode"] in legacy.MODES and cfg["k_mpc"] in legacy.K_VALUES,
        "C1_baseline_exact": _C1_BASELINE == {
            mode: tuple(spec["accepted"]) for mode, spec in _LEGACY_SUPPORTS.items()
        },
        "audit_is_plus2": cfg["audit"] == (cfg["accepted"][0], cfg["accepted"][1] + 2),
        "M1_depth_covers_audit": cfg["m1_depth"] == cfg["audit"][1],
        "surfaces_exact": tuple(legacy.physics.Z_SURFACES) == (1.0e-4, 1.0e-2),
        "thresholds_exact": bool(
            legacy.physics.LOW_COEFFICIENT_TOL == 1.0e-8
            and legacy.physics.TAIL_TOL == 1.0e-6
            and legacy.physics.ABS_FALLBACK_TOL == 1.0e-12
            and legacy.physics.BACKGROUND_K_TOL == 1.0e-12
        ),
    }
    return {"checks": checks, "pass": all(checks.values()),
            "C1_baseline": _C1_BASELINE,
            "ladder_spec": {"accepted": cfg["accepted"], "audit": cfg["audit"],
                            "m1_depth": cfg["m1_depth"]}}


@contextmanager
def _overlay() -> Iterator[None]:
    cfg = _cfg()
    supports = {mode: dict(spec) for mode, spec in _LEGACY_SUPPORTS.items()}
    supports[str(cfg["mode"])] = {
        "accepted": cfg["accepted"], "audit": cfg["audit"], "m1_depth": cfg["m1_depth"]
    }
    before = (legacy.RUN_ID, legacy.SUPPORTS, legacy.contract_guard, legacy.source_hashes,
              legacy.atom_output_name, legacy.atom_failure_name)
    try:
        legacy.RUN_ID = str(cfg["run_id"])
        legacy.SUPPORTS = supports
        legacy.contract_guard = contract_guard
        legacy.source_hashes = source_hashes
        legacy.atom_output_name = atom_output_name
        legacy.atom_failure_name = atom_failure_name
        yield
    finally:
        (legacy.RUN_ID, legacy.SUPPORTS, legacy.contract_guard, legacy.source_hashes,
         legacy.atom_output_name, legacy.atom_failure_name) = before


def _owners_restored() -> bool:
    return bool(
        legacy.RUN_ID == _LEGACY_RUN_ID and legacy.SUPPORTS is _LEGACY_SUPPORTS
        and legacy.contract_guard is _LEGACY_CONTRACT_GUARD
        and legacy.source_hashes is _LEGACY_SOURCE_HASHES
        and legacy.atom_output_name is _LEGACY_ATOM_OUTPUT_NAME
        and legacy.atom_failure_name is _LEGACY_ATOM_FAILURE_NAME
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    cfg = _cfg()
    _, deadline = legacy.make_deadline(max_runtime_seconds)
    prerequisite = _load_prerequisite(result_dir)
    with _overlay():
        overlay_pass = legacy.contract_guard()["pass"]
        name = legacy.atom_output_name(str(cfg["mode"]), float(cfg["k_mpc"]))
    wrong_rejected = False
    try:
        atom_output_name(str(cfg["mode"]), 0.15 if cfg["k_mpc"] == 0.005 else 0.005)
    except ValueError:
        wrong_rejected = True
    checks = {"prerequisite": prerequisite["sha256"] == cfg["prerequisite_sha256"],
              "contract_guard": contract_guard()["pass"], "overlay_guard": overlay_pass,
              "canonical_name": name == cfg["output_name"], "wrong_atom_rejected": wrong_rejected,
              "owners_restored": _owners_restored()}
    deadline()
    return {"run_id": cfg["run_id"], "mode": "SMOKE_NO_RESULT_FILE",
            "checks": checks, "passed": all(checks.values())}


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    cfg = _cfg()
    if mode != cfg["mode"] or k_mpc != cfg["k_mpc"]:
        raise ValueError("atom differs from configured C2 identity")
    prerequisite = _load_prerequisite(result_dir)
    with _overlay():
        payload = legacy.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("C2 single-atom owners were not restored")
    token = legacy.k_token(k_mpc).replace("0p", "0p")
    end = int(cfg["accepted"][1])
    audit_end = int(cfg["audit"][1])
    if payload["candidate_interpretation_not_verdict"] == "PASS_C2_FOURIER_ATOM_CANDIDATE_ONLY":
        candidate = f"PASS_C2_{mode}_K{token}_SUPPORT_{end:02d}_ADEQUATE_CANDIDATE_ONLY"
    elif not payload["tail_pass"] and payload["core_pass"] and payload["common_pass"]:
        candidate = f"REVIEW_C2_{mode}_K{token}_SUPPORT_{audit_end:02d}_{audit_end + 2:02d}_REQUIRED"
    else:
        candidate = payload["candidate_interpretation_not_verdict"]
    payload["candidate_interpretation_not_verdict"] = candidate
    payload["ordering_prerequisite"] = prerequisite
    payload["support_ladder_scope"] = {"candidate": list(cfg["accepted"]),
                                       "audit": list(cfg["audit"])}
    payload["overlay_owners_restored"] = True
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("configured C2 single atom has no aggregate scope")
