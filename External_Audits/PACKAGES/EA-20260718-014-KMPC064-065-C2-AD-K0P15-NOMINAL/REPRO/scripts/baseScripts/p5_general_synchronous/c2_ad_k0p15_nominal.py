"""KMPC-064 atom-local C2 AD/k=.15 nominal audit.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
from typing import Iterator

from . import c2_fourier_coverage_v4_guard_semantics as prior


legacy = prior.legacy
RUN_ID = "KMPC-064"
MODE = "AD"
K_MPC = 0.15
OUTPUT_NAME = "RUN_KMPC_064_P5_3G7_C2_AD_K0p15_NOMINAL.json"
PRIOR_NAME = "RUN_KMPC_063_P5_3G7_C2_AD_K0p005_SUPPORT_06_08.json"
PRIOR_SHA256 = "CB0CEA5DD92BF85F0F0066FAD8DE77D5F8247B02B864FACF92FA374E0FBC85BD"
PRIOR_CANDIDATE = "PASS_C2_AD_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY"
LADDER_SPEC = {"accepted": (0, 2), "audit": (0, 4), "m1_depth": 5}

_PRIOR_RUN_ID = prior.RUN_ID
_PRIOR_CONTRACT_GUARD = prior.contract_guard
_PRIOR_SOURCE_HASHES = prior.source_hashes
_PRIOR_ATOM_OUTPUT_NAME = prior.atom_output_name
_PRIOR_ATOM_FAILURE_NAME = prior.atom_failure_name


def atom_output_name(mode: str, k_mpc: float) -> str:
    if mode != MODE or k_mpc != K_MPC:
        raise ValueError("KMPC-064 permits only AD/k=.15")
    return OUTPUT_NAME


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return atom_output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def source_hashes() -> dict[str, str]:
    hashes = dict(_PRIOR_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_ad_k0p15_nominal.py"] = legacy.sha256_file(here / "c2_ad_k0p15_nominal.py")
    return hashes


def _load_prior(result_dir: Path) -> dict[str, object]:
    path = result_dir / PRIOR_NAME
    observed_hash = legacy.sha256_file(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    if observed_hash != PRIOR_SHA256 or payload.get("candidate_interpretation_not_verdict") != PRIOR_CANDIDATE:
        raise RuntimeError("immutable KMPC-063 ordering prerequisite mismatch")
    if payload.get("support_ladder_scope") != {"candidate": [0, 6], "audit": [0, 8]}:
        raise RuntimeError("KMPC-063 support identity mismatch")
    return {"file": PRIOR_NAME, "sha256": observed_hash, "candidate": PRIOR_CANDIDATE,
            "role": "ORDERING_ONLY_NOT_PHYSICS_TRANSFER"}


def contract_guard() -> dict[str, object]:
    guard = _PRIOR_CONTRACT_GUARD()
    checks = dict(guard["checks"])
    checks.update({
        "atom_exact_AD_k0p15": MODE == "AD" and K_MPC == 0.15,
        "AD_candidate_support_exact_02": tuple(prior.SUPPORTS[MODE]["accepted"]) == (0, 2),
        "AD_audit_support_exact_04": tuple(prior.SUPPORTS[MODE]["audit"]) == (0, 4),
        "AD_M1_depth_exact_5": prior.SUPPORTS[MODE]["m1_depth"] == 5,
    })
    return {"derived": guard["derived"], "checks": checks, "pass": all(checks.values()),
            "ladder_spec": LADDER_SPEC}


@contextmanager
def _overlay() -> Iterator[None]:
    before = (prior.RUN_ID, prior.contract_guard, prior.source_hashes,
              prior.atom_output_name, prior.atom_failure_name)
    try:
        prior.RUN_ID = RUN_ID
        prior.contract_guard = contract_guard
        prior.source_hashes = source_hashes
        prior.atom_output_name = atom_output_name
        prior.atom_failure_name = atom_failure_name
        yield
    finally:
        (prior.RUN_ID, prior.contract_guard, prior.source_hashes,
         prior.atom_output_name, prior.atom_failure_name) = before


def _owners_restored() -> bool:
    return bool(
        prior.RUN_ID == _PRIOR_RUN_ID
        and prior.contract_guard is _PRIOR_CONTRACT_GUARD
        and prior.source_hashes is _PRIOR_SOURCE_HASHES
        and prior.atom_output_name is _PRIOR_ATOM_OUTPUT_NAME
        and prior.atom_failure_name is _PRIOR_ATOM_FAILURE_NAME
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = legacy.make_deadline(max_runtime_seconds)
    prerequisite = _load_prior(result_dir)
    with _overlay():
        payload = prior.run_smoke(max_runtime_seconds, result_dir)
        canonical_name = prior.atom_output_name(MODE, K_MPC)
    wrong_rejected = False
    try:
        atom_output_name(MODE, 0.005)
    except ValueError:
        wrong_rejected = True
    checks = {
        "ordering_prerequisite": prerequisite["sha256"] == PRIOR_SHA256,
        "contract_guard": contract_guard()["pass"],
        "canonical_name": canonical_name == OUTPUT_NAME,
        "wrong_atom_rejected": wrong_rejected,
        "owners_restored": _owners_restored(),
    }
    deadline()
    payload["KMPC064_checks"] = checks
    payload["passed"] = bool(payload["passed"] and all(checks.values()))
    return payload


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if mode != MODE or k_mpc != K_MPC:
        raise ValueError("KMPC-064 permits only AD/k=.15")
    prerequisite = _load_prior(result_dir)
    with _overlay():
        payload = prior.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("KMPC-064 owner overlay was not restored")
    if payload["candidate_interpretation_not_verdict"] == "PASS_C2_FOURIER_ATOM_CANDIDATE_ONLY":
        candidate = "PASS_C2_AD_K0p15_SUPPORT_02_ADEQUATE_CANDIDATE_ONLY"
    elif not payload["tail_pass"] and payload["core_pass"] and payload["common_pass"]:
        candidate = "REVIEW_C2_AD_K0p15_SUPPORT_04_06_REQUIRED"
    else:
        candidate = payload["candidate_interpretation_not_verdict"]
    payload["candidate_interpretation_not_verdict"] = candidate
    payload["KMPC063_ordering_prerequisite"] = prerequisite
    payload["support_ladder_scope"] = {"candidate": [0, 2], "audit": [0, 4]}
    payload["overlay_owners_restored"] = True
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("KMPC-064 has no aggregate scope")
