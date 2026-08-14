"""KMPC-063 AD/k=.005 support ladder [0,6] -> [0,8].

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
from typing import Iterator

from . import c2_ad_k0p005_support_04_06 as prior


legacy = prior.legacy
RUN_ID = "KMPC-063"
MODE = "AD"
K_MPC = 0.005
OUTPUT_NAME = "RUN_KMPC_063_P5_3G7_C2_AD_K0p005_SUPPORT_06_08.json"
PRIOR_NAME = "RUN_KMPC_062_P5_3G7_C2_AD_K0p005_SUPPORT_04_06.json"
PRIOR_SHA256 = "640057CB6AC3F059988D6BD6C0CBE65ABAC1712F18961A2FEAFA5E1341EA6760"
PRIOR_CANDIDATE = "REVIEW_C2_AD_K0p005_FURTHER_SUPPORT_EXTENSION_REQUIRED"
LADDER_SPEC = {"accepted": (0, 6), "audit": (0, 8), "m1_depth": 8}


def atom_output_name(mode: str, k_mpc: float) -> str:
    if mode != MODE or k_mpc != K_MPC:
        raise ValueError("KMPC-063 permits only AD/k=.005")
    return OUTPUT_NAME


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return atom_output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def source_hashes() -> dict[str, str]:
    hashes = dict(prior.source_hashes())
    here = Path(__file__).resolve().parent
    hashes["c2_ad_k0p005_support_06_08.py"] = legacy.sha256_file(
        here / "c2_ad_k0p005_support_06_08.py"
    )
    return hashes


def _load_prior(result_dir: Path) -> dict[str, object]:
    path = result_dir / PRIOR_NAME
    observed_hash = legacy.sha256_file(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    if observed_hash != PRIOR_SHA256 or payload.get("candidate_interpretation_not_verdict") != PRIOR_CANDIDATE:
        raise RuntimeError("immutable KMPC-062 prerequisite mismatch")
    if payload.get("support_ladder_scope") != {"candidate": [0, 4], "audit": [0, 6]}:
        raise RuntimeError("KMPC-062 support identity mismatch")
    return {"file": PRIOR_NAME, "sha256": observed_hash, "candidate": PRIOR_CANDIDATE}


def contract_guard() -> dict[str, object]:
    checks = {
        "mode_k_exact": MODE == "AD" and K_MPC == 0.005,
        "candidate_exact_06": tuple(LADDER_SPEC["accepted"]) == (0, 6),
        "audit_exact_08": tuple(LADDER_SPEC["audit"]) == (0, 8),
        "audit_is_plus2": LADDER_SPEC["audit"][1] == LADDER_SPEC["accepted"][1] + 2,
        "M1_depth8_covers_audit": LADDER_SPEC["m1_depth"] == 8,
        "surfaces_exact": tuple(legacy.physics.Z_SURFACES) == (1.0e-4, 1.0e-2),
        "thresholds_exact": bool(
            legacy.physics.LOW_COEFFICIENT_TOL == 1.0e-8
            and legacy.physics.TAIL_TOL == 1.0e-6
            and legacy.physics.ABS_FALLBACK_TOL == 1.0e-12
            and legacy.physics.BACKGROUND_K_TOL == 1.0e-12
        ),
    }
    return {"checks": checks, "pass": all(checks.values()), "ladder_spec": LADDER_SPEC}


@contextmanager
def _overlay() -> Iterator[None]:
    supports = {mode: dict(spec) for mode, spec in prior._LEGACY_SUPPORTS.items()}
    supports[MODE] = dict(LADDER_SPEC)
    before = (legacy.RUN_ID, legacy.SUPPORTS, legacy.contract_guard,
              legacy.source_hashes, legacy.atom_output_name, legacy.atom_failure_name)
    try:
        legacy.RUN_ID = RUN_ID
        legacy.SUPPORTS = supports
        legacy.contract_guard = contract_guard
        legacy.source_hashes = source_hashes
        legacy.atom_output_name = atom_output_name
        legacy.atom_failure_name = atom_failure_name
        yield
    finally:
        (legacy.RUN_ID, legacy.SUPPORTS, legacy.contract_guard,
         legacy.source_hashes, legacy.atom_output_name, legacy.atom_failure_name) = before


def _owners_restored() -> bool:
    return bool(
        legacy.RUN_ID == prior._LEGACY_RUN_ID and legacy.SUPPORTS is prior._LEGACY_SUPPORTS
        and legacy.contract_guard is prior._LEGACY_CONTRACT_GUARD
        and legacy.source_hashes is prior._LEGACY_SOURCE_HASHES
        and legacy.atom_output_name is prior._LEGACY_ATOM_OUTPUT_NAME
        and legacy.atom_failure_name is prior._LEGACY_ATOM_FAILURE_NAME
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = legacy.make_deadline(max_runtime_seconds)
    prerequisite = _load_prior(result_dir)
    with _overlay():
        overlay_pass = legacy.contract_guard()["pass"]
        name = legacy.atom_output_name(MODE, K_MPC)
    wrong_rejected = False
    try:
        atom_output_name(MODE, 0.15)
    except ValueError:
        wrong_rejected = True
    checks = {"prerequisite": prerequisite["sha256"] == PRIOR_SHA256,
              "contract_guard": contract_guard()["pass"], "overlay_guard": overlay_pass,
              "canonical_name": name == OUTPUT_NAME, "wrong_atom_rejected": wrong_rejected,
              "owners_restored": _owners_restored()}
    deadline()
    return {"run_id": RUN_ID, "mode": "SMOKE_NO_RESULT_FILE", "checks": checks,
            "passed": all(checks.values())}


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if mode != MODE or k_mpc != K_MPC:
        raise ValueError("KMPC-063 permits only AD/k=.005")
    prerequisite = _load_prior(result_dir)
    with _overlay():
        payload = legacy.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("KMPC-063 owner overlay was not restored")
    if payload["candidate_interpretation_not_verdict"] == "PASS_C2_FOURIER_ATOM_CANDIDATE_ONLY":
        candidate = "PASS_C2_AD_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY"
    elif not payload["tail_pass"] and payload["core_pass"] and payload["common_pass"]:
        candidate = "REVIEW_C2_AD_K0p005_SUPPORT_08_10_REQUIRED"
    else:
        candidate = payload["candidate_interpretation_not_verdict"]
    payload["candidate_interpretation_not_verdict"] = candidate
    payload["KMPC062_prerequisite"] = prerequisite
    payload["support_ladder_scope"] = {"candidate": [0, 6], "audit": [0, 8]}
    payload["overlay_owners_restored"] = True
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("KMPC-063 has no aggregate scope")
