"""KMPC-062 AD/k=.005 support ladder [0,4] -> [0,6].

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from . import c2_fourier_coverage as legacy


RUN_ID = "KMPC-062"
MODE = "AD"
K_MPC = 0.005
VARIANT = "nominal"
OUTPUT_NAME = "RUN_KMPC_062_P5_3G7_C2_AD_K0p005_SUPPORT_04_06.json"
KMPC061_NAME = "RUN_KMPC_061_P5_3G7_C2_AD_K0p005_NOMINAL.json"
KMPC061_SHA256 = "0952AF08B1DE291D015F71396954F70EAE2F78A962E1EE1D3A08ECA48A1F5DCD"
KMPC061_CANDIDATE = "REVIEW_C2_SUPPORT_EXTENSION_REQUIRED"
LADDER_SPEC = {"accepted": (0, 4), "audit": (0, 6), "m1_depth": 6}
C1_BASELINE = {
    "AD": (0, 2), "CDI": (0, 5), "BI": (0, 5), "NID": (0, 5), "NIV": (-1, 4)
}

_LEGACY_RUN_ID = legacy.RUN_ID
_LEGACY_SUPPORTS = legacy.SUPPORTS
_LEGACY_CONTRACT_GUARD = legacy.contract_guard
_LEGACY_SOURCE_HASHES = legacy.source_hashes
_LEGACY_ATOM_OUTPUT_NAME = legacy.atom_output_name
_LEGACY_ATOM_FAILURE_NAME = legacy.atom_failure_name


def atom_output_name(mode: str, k_mpc: float) -> str:
    if mode != MODE or k_mpc != K_MPC:
        raise ValueError("KMPC-062 permits only AD/k=.005")
    return OUTPUT_NAME


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return atom_output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def source_hashes() -> dict[str, str]:
    hashes = dict(_LEGACY_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_ad_k0p005_support_04_06.py"] = legacy.sha256_file(
        here / "c2_ad_k0p005_support_04_06.py"
    )
    return hashes


def _load_kmpc061(result_dir: Path) -> dict[str, object]:
    path = result_dir / KMPC061_NAME
    observed_hash = legacy.sha256_file(path)
    import json
    payload = json.loads(path.read_text(encoding="utf-8"))
    candidate = payload.get("candidate_interpretation_not_verdict")
    identity = payload.get("identity")
    if observed_hash != KMPC061_SHA256 or candidate != KMPC061_CANDIDATE:
        raise RuntimeError("immutable KMPC-061 prerequisite mismatch")
    if identity != {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT}:
        raise RuntimeError("KMPC-061 identity mismatch")
    return {"file": KMPC061_NAME, "sha256": observed_hash, "candidate": candidate}


def contract_guard() -> dict[str, object]:
    checks = {
        "mode_exact": MODE == "AD",
        "k_exact": K_MPC == 0.005,
        "variant_exact": VARIANT == "nominal",
        "C1_baseline_exact": C1_BASELINE == {
            mode: tuple(spec["accepted"]) for mode, spec in _LEGACY_SUPPORTS.items()
        },
        "candidate_exact_04": tuple(LADDER_SPEC["accepted"]) == (0, 4),
        "audit_exact_06": tuple(LADDER_SPEC["audit"]) == (0, 6),
        "audit_is_plus2": LADDER_SPEC["audit"][1] == LADDER_SPEC["accepted"][1] + 2,
        "M1_depth6_covers_audit": LADDER_SPEC["m1_depth"] == 6,
        "surfaces_exact": tuple(legacy.physics.Z_SURFACES) == (1.0e-4, 1.0e-2),
        "thresholds_exact": bool(
            legacy.physics.LOW_COEFFICIENT_TOL == 1.0e-8
            and legacy.physics.TAIL_TOL == 1.0e-6
            and legacy.physics.ABS_FALLBACK_TOL == 1.0e-12
            and legacy.physics.BACKGROUND_K_TOL == 1.0e-12
        ),
    }
    return {"checks": checks, "pass": all(checks.values()),
            "C1_baseline": C1_BASELINE, "ladder_spec": LADDER_SPEC}


@contextmanager
def _overlay() -> Iterator[None]:
    supports = {mode: dict(spec) for mode, spec in _LEGACY_SUPPORTS.items()}
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
        legacy.RUN_ID == _LEGACY_RUN_ID and legacy.SUPPORTS is _LEGACY_SUPPORTS
        and legacy.contract_guard is _LEGACY_CONTRACT_GUARD
        and legacy.source_hashes is _LEGACY_SOURCE_HASHES
        and legacy.atom_output_name is _LEGACY_ATOM_OUTPUT_NAME
        and legacy.atom_failure_name is _LEGACY_ATOM_FAILURE_NAME
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = legacy.make_deadline(max_runtime_seconds)
    prerequisite = _load_kmpc061(result_dir)
    guard = contract_guard()
    with _overlay():
        overlay_guard = legacy.contract_guard()
        overlay_name = legacy.atom_output_name(MODE, K_MPC)
    wrong_atom_rejected = False
    try:
        atom_output_name(MODE, 0.15)
    except ValueError:
        wrong_atom_rejected = True
    checks = {"prerequisite": prerequisite["sha256"] == KMPC061_SHA256,
              "contract_guard": guard["pass"], "overlay_guard": overlay_guard["pass"],
              "canonical_name": overlay_name == OUTPUT_NAME,
              "wrong_atom_rejected": wrong_atom_rejected, "owners_restored": _owners_restored()}
    deadline()
    return {"run_id": RUN_ID, "mode": "SMOKE_NO_RESULT_FILE", "checks": checks,
            "passed": all(checks.values())}


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if mode != MODE or k_mpc != K_MPC:
        raise ValueError("KMPC-062 permits only AD/k=.005")
    prerequisite = _load_kmpc061(result_dir)
    with _overlay():
        payload = legacy.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("KMPC-062 owner overlay was not restored")
    if payload["candidate_interpretation_not_verdict"] == "PASS_C2_FOURIER_ATOM_CANDIDATE_ONLY":
        candidate = "PASS_C2_AD_K0p005_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY"
    elif not payload["tail_pass"] and payload["core_pass"] and payload["common_pass"]:
        candidate = "REVIEW_C2_AD_K0p005_FURTHER_SUPPORT_EXTENSION_REQUIRED"
    else:
        candidate = payload["candidate_interpretation_not_verdict"]
    payload["candidate_interpretation_not_verdict"] = candidate
    payload["KMPC061_prerequisite"] = prerequisite
    payload["support_ladder_scope"] = {"candidate": [0, 4], "audit": [0, 6]}
    payload["overlay_owners_restored"] = True
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("KMPC-062 has no aggregate scope")
