"""KMPC-142 exact identity-schema adapter for the KMPC-053 NID/.05 raw.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
All scientific solves and aggregate gates remain delegated to frozen KMPC-131.
"""

from __future__ import annotations

import json
from pathlib import Path

from . import c3_zero_variant_parallel_v3_support_shards as legacy


RUN_ID = "KMPC-142"
MODES = ("NID",)
K_VALUES = (0.05,)
VARIANTS = legacy.VARIANTS
SHARDS = legacy.SHARDS
scientific = legacy.scientific
_ORIGINAL_LOAD_NOMINAL_REFERENCE = scientific._load_nominal_reference


def sha256_file(path: Path) -> str:
    return legacy.sha256_file(path)


def _load_nominal_reference_schema_exact(
    result_dir: Path, mode: str, k_mpc: float
) -> dict[str, object]:
    """Accept exactly the frozen six-field KMPC-053 identity schema."""
    if (mode, k_mpc) != ("NID", 0.05):
        return _ORIGINAL_LOAD_NOMINAL_REFERENCE(result_dir, mode, k_mpc)

    support = scientific.SUPPORTS[(mode, k_mpc)]
    spec = scientific._nominal_spec(mode, k_mpc)
    if (
        spec.filename != "RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json"
        or spec.sha256
        != "625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD"
        or spec.run_id != "KMPC-053"
        or spec.candidate != "PASS_NID_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY"
        or spec.schema != "solved_supports"
        or spec.accepted_key != "05"
        or spec.audit_key != "07"
    ):
        raise RuntimeError("KMPC-142 frozen NID/.05 nominal spec mismatch")
    if support.accepted != (0, 5) or support.audit != (0, 7) or support.m1_depth != 7:
        raise RuntimeError("KMPC-142 frozen NID/.05 support/depth mismatch")

    # Keep the inherited KMPC-127 aggregate as the mandatory global C2 gate.
    scientific._load_c2_aggregate(result_dir)
    path = result_dir / spec.filename
    if not path.is_file():
        raise FileNotFoundError(f"missing nominal reference: {spec.filename}")
    observed_hash = sha256_file(path)
    if observed_hash != spec.sha256:
        raise RuntimeError(f"nominal reference SHA mismatch: {spec.filename}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError("nominal reference is not an object")

    expected_identity = {
        "M1_depth": 7,
        "audit_support": [0, 7],
        "candidate_support": [0, 5],
        "k_Mpc_inverse": 0.05,
        "mode": "NID",
        "variant": "nominal",
    }
    if payload.get("identity") != expected_identity:
        raise RuntimeError(f"nominal identity mismatch: {spec.filename}")
    if payload.get("run_id") != spec.run_id:
        raise RuntimeError(f"nominal run_id mismatch: {spec.filename}")
    if payload.get("candidate_interpretation_not_verdict") != spec.candidate:
        raise RuntimeError(f"nominal candidate mismatch: {spec.filename}")

    states = scientific._extract_nominal_states(payload, spec, support)
    return {
        "file": spec.filename,
        "sha256": observed_hash,
        "run_id": spec.run_id,
        "candidate": spec.candidate,
        "schema": spec.schema,
        "support_authority": {
            "type": "C1_DIRECT_SCOPED_PASS",
            "file": spec.filename,
            "sha256": spec.sha256,
            "candidate": spec.candidate,
            "identity_schema": "EXACT_SIX_FIELD_KMPC_053",
        },
        "states": states,
    }


# The overlay is process-local. Frozen files are never edited.
scientific._load_nominal_reference = _load_nominal_reference_schema_exact
legacy.RUN_ID = RUN_ID


def shard_key(variant: str, level: str) -> str:
    return legacy.shard_key(variant, level)


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) != ("NID", 0.05):
        raise ValueError("KMPC-142 is scoped only to NID/k=0.05")
    return "RUN_KMPC_142_P5_3G7_C3_NID_K0p05_ZERO_VARIANT_PAIR.json"


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def run_support_worker(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != ("NID", 0.05):
        raise ValueError("KMPC-142 worker is scoped only to NID/k=0.05")
    payload = legacy.run_support_worker(
        mode, k_mpc, variant, level, max_runtime_seconds, result_dir
    )
    payload["source_hashes"][Path(__file__).name] = sha256_file(
        Path(__file__).resolve()
    )
    return payload


run_worker_smoke = legacy.run_worker_smoke
aggregate_smoke_shards = legacy.aggregate_smoke_shards
aggregate_shards = legacy.aggregate_shards
