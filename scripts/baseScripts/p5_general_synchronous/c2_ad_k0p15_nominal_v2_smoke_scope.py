"""KMPC-065 smoke-scope successor for the AD/k=.15 nominal atom.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from . import c2_ad_k0p15_nominal as v1


legacy = v1.legacy
parent = v1.prior
RUN_ID = "KMPC-065"
MODE = v1.MODE
K_MPC = v1.K_MPC
OUTPUT_NAME = "RUN_KMPC_065_P5_3G7_C2_AD_K0p15_NOMINAL.json"

_V1_SOURCE_HASHES = v1.source_hashes


def atom_output_name(mode: str, k_mpc: float) -> str:
    if mode != MODE or k_mpc != K_MPC:
        raise ValueError("KMPC-065 permits only AD/k=.15")
    return OUTPUT_NAME


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return atom_output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def source_hashes() -> dict[str, str]:
    hashes = dict(_V1_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_ad_k0p15_nominal_v2_smoke_scope.py"] = legacy.sha256_file(
        here / "c2_ad_k0p15_nominal_v2_smoke_scope.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    return v1.contract_guard()


@contextmanager
def _v1_hash_overlay() -> Iterator[None]:
    before = v1.source_hashes
    try:
        v1.source_hashes = source_hashes
        yield
    finally:
        v1.source_hashes = before


def _v1_owner_restored() -> bool:
    return v1.source_hashes is _V1_SOURCE_HASHES


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = legacy.make_deadline(max_runtime_seconds)
    prerequisite = v1._load_prior(result_dir)
    parent_payload = parent.run_smoke(max_runtime_seconds, result_dir)
    with _v1_hash_overlay():
        with v1._overlay():
            overlay_checks = {
                "run_id_owned": parent.RUN_ID == v1.RUN_ID,
                "contract_owned": parent.contract_guard()["pass"],
                "source_hash_owned": parent.source_hashes() == source_hashes(),
                "canonical_name": parent.atom_output_name(MODE, K_MPC) == v1.OUTPUT_NAME,
            }
    wrong_rejected = False
    try:
        atom_output_name(MODE, 0.005)
    except ValueError:
        wrong_rejected = True
    checks = {
        "parent_matrix_smoke": parent_payload["passed"],
        "ordering_prerequisite": prerequisite["sha256"] == v1.PRIOR_SHA256,
        "contract_guard": contract_guard()["pass"],
        "wrong_atom_rejected": wrong_rejected,
        "overlay_checks": all(overlay_checks.values()),
        "v1_hash_owner_restored": _v1_owner_restored(),
        "parent_owners_restored": v1._owners_restored(),
    }
    deadline()
    return {"run_id": RUN_ID, "mode": "SMOKE_NO_RESULT_FILE",
            "parent_matrix_smoke": parent_payload,
            "overlay_checks": overlay_checks, "checks": checks,
            "passed": all(checks.values())}


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if mode != MODE or k_mpc != K_MPC:
        raise ValueError("KMPC-065 permits only AD/k=.15")
    with _v1_hash_overlay():
        payload = v1.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _v1_owner_restored():
        raise RuntimeError("KMPC-065 V1 hash owner was not restored")
    payload["run_id"] = RUN_ID
    payload["candidate_interpretation_not_verdict"] = (
        "PASS_C2_AD_K0p15_SUPPORT_02_ADEQUATE_CANDIDATE_ONLY"
        if payload["candidate_interpretation_not_verdict"]
        == "PASS_C2_AD_K0p15_SUPPORT_02_ADEQUATE_CANDIDATE_ONLY"
        else payload["candidate_interpretation_not_verdict"]
    )
    payload["technical_successor"] = "PF-080 / SMOKE_SCOPE_ONLY"
    payload["overlay_owners_restored"] = True
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("KMPC-065 has no aggregate scope")
