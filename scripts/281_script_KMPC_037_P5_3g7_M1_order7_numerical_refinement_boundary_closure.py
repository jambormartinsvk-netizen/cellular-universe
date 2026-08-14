"""Bounded runner for KMPC-037 numerical refinement and boundary closure."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
from typing import Any

import numpy as np


BASE_DIR = Path(__file__).resolve().parent / "baseScripts" / "p5_general_synchronous"
RESULT_DIR = Path(__file__).resolve().parent / "results" / "k_mpc_005"
CANONICAL_OUTPUT = (
    RESULT_DIR / "RUN_KMPC_037_P5_3G7_M1_ORDER7_NUMERICAL_REFINEMENT.json"
)
FAILURE_OUTPUT = (
    RESULT_DIR
    / "RUN_KMPC_037_P5_3G7_M1_ORDER7_NUMERICAL_REFINEMENT_TECHNICAL_FAILURE.json"
)
TEMP_OUTPUT = RESULT_DIR / f".tmp-{CANONICAL_OUTPUT.name}"
PREREQUISITE = (
    RESULT_DIR / "RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json"
)
EXPECTED_PREREQUISITE_HASH = (
    "39BB388669E74C9368BD823C5FF5C68A487B7FC1CD4F74EACBF64D9A08B7B497"
)
EXPECTED_SOURCE_HASHES = {
    "mode_resolved_puiseux.py": (
        "5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE"
    ),
    "mode_resolved_puiseux_v2_m1_anchored.py": (
        "5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455"
    ),
    "m1_order7_provenance.py": (
        "0B1EB4C76A7388D6A8F6D1E5DD933549043337381DEF6DE77539D3F84CA7BAC7"
    ),
    "m1_order7_numerical_refinement.py": (
        "CE29222FCE45DAA99A7B8E1FFCC06E9471D648A2B61C14DA05F653DBA9E7A80C"
    ),
}


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _output_conflicts() -> list[str]:
    return [str(path) for path in (CANONICAL_OUTPUT, FAILURE_OUTPUT, TEMP_OUTPUT) if path.exists()]


def _preimport_guard() -> dict[str, str]:
    conflicts = _output_conflicts()
    if conflicts:
        raise FileExistsError(f"immutable KMPC-037 output conflict: {conflicts}")
    actual = {name: _sha256_file(BASE_DIR / name) for name in EXPECTED_SOURCE_HASHES}
    if actual != EXPECTED_SOURCE_HASHES:
        raise RuntimeError("KMPC-037 exact pre-import source hash mismatch")
    if _sha256_file(PREREQUISITE) != EXPECTED_PREREQUISITE_HASH:
        raise RuntimeError("KMPC-037 immutable prerequisite hash mismatch")
    return actual


def _json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, np.ndarray):
        return [_json_safe(item) for item in value.tolist()]
    if isinstance(value, np.generic):
        return _json_safe(value.item())
    if isinstance(value, float) and not math.isfinite(value):
        raise FloatingPointError("non-finite value cannot be serialized")
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    raise TypeError(f"unsupported JSON scalar: {type(value).__name__}")


def _encode_json(payload: dict[str, Any]) -> str:
    return json.dumps(
        _json_safe(payload), indent=2, sort_keys=True, allow_nan=False
    ) + "\n"


def _write_atomic_exclusive(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.parent / f".tmp-{path.name}"
    if path.exists() or temporary.exists():
        raise FileExistsError(f"immutable publish collision: {path}")
    try:
        encoded = _encode_json(payload)
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.link(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _runtime_guard(value: float | None, expected: float) -> bool:
    if value is None or not math.isfinite(value) or value != expected:
        raise ValueError(f"KMPC-037 requires exactly {expected} runtime seconds")
    return True


def _runner_smoke_fixtures() -> dict[str, bool]:
    fixture_target = RESULT_DIR / ".KMPC037_publish_collision_fixture.json"
    fixture_temp = fixture_target.parent / f".tmp-{fixture_target.name}"
    if fixture_target.exists() or fixture_temp.exists():
        raise FileExistsError("stale KMPC-037 publish fixture")
    try:
        fixture_target.write_text("sentinel\n", encoding="utf-8")
        try:
            _write_atomic_exclusive(fixture_target, {"unexpected": True})
            collision_rejected = False
        except FileExistsError:
            collision_rejected = True
        collision_preserved = fixture_target.read_text(encoding="utf-8") == "sentinel\n"
        temp_cleaned = not fixture_temp.exists()
    finally:
        if fixture_temp.exists():
            fixture_temp.unlink()
        if fixture_target.exists():
            fixture_target.unlink()
    try:
        _runtime_guard(None, 4.8)
        missing_runtime_rejected = False
    except ValueError:
        missing_runtime_rejected = True
    try:
        _encode_json({"bad": object()})
        unsupported_scalar_rejected = False
    except TypeError:
        unsupported_scalar_rejected = True
    return {
        "publish_collision_rejected": collision_rejected,
        "publish_collision_preserved": collision_preserved,
        "publish_temp_cleaned": temp_cleaned,
        "missing_runtime_rejected": missing_runtime_rejected,
        "unsupported_json_scalar_rejected": unsupported_scalar_rejected,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Bounded KMPC-037 same-matrix numerical audit only; does not run "
            "CDI support step 3 or a native high-precision rebuild."
        )
    )
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--smoke", action="store_true")
    mode.add_argument("--audit", action="store_true")
    parser.add_argument("--output", type=Path)
    return parser


def main() -> int:
    args = _parser().parse_args()
    progress = {"phase": "argument_guard"}
    expected_runtime = 4.8 if args.smoke else 45.0
    try:
        _runtime_guard(args.max_runtime_seconds, expected_runtime)
        if args.smoke and args.output is not None:
            raise ValueError("smoke forbids --output")
        if args.audit:
            if args.output is None:
                raise ValueError("audit requires canonical --output")
            if args.output.resolve() != CANONICAL_OUTPUT.resolve():
                raise ValueError("noncanonical KMPC-037 output path")
        progress["phase"] = "preimport_guard"
        preimport = _preimport_guard()
        progress["phase"] = "guarded_import"
        from baseScripts.p5_general_synchronous import (
            m1_order7_numerical_refinement as audit,
        )

        if audit.source_hashes() != EXPECTED_SOURCE_HASHES:
            raise RuntimeError("KMPC-037 post-import source hash mismatch")
        if args.smoke:
            progress["phase"] = "runner_smoke"
            runner_fixtures = _runner_smoke_fixtures()
            if not all(runner_fixtures.values()):
                raise RuntimeError("KMPC-037 runner fixture failed")
            progress["phase"] = "base_smoke"
            payload = audit.run_smoke(args.max_runtime_seconds, RESULT_DIR)
            payload["runner_negative_fixtures"] = runner_fixtures
            safe = _json_safe(payload)
            json.dumps(safe, allow_nan=False)
            print(json.dumps(safe, sort_keys=True), flush=True)
            return 0
        progress["phase"] = "audit"
        payload = audit.run_audit(args.max_runtime_seconds, RESULT_DIR)
        if payload["source_hashes"] != preimport:
            raise RuntimeError("KMPC-037 payload source hash mismatch")
        progress["phase"] = "publish"
        _write_atomic_exclusive(CANONICAL_OUTPUT, payload)
        safe = _json_safe(payload)
        print(
            json.dumps(
                {
                    "run_id": safe["run_id"],
                    "execution_status": safe["execution_status"],
                    "candidate": safe["candidate_interpretation_not_verdict"],
                    "v0_pass": safe["v0"]["pass"],
                    "v2_driver_pass": safe["v2_single_bounded_refinement"]["driver_and_initial"]["pass"],
                    "v3_driver_pass": safe["v3_same_float64_matrix_high_precision"]["driver_and_initial_high_precision"]["pass"],
                    "output": str(CANONICAL_OUTPUT),
                },
                sort_keys=True,
            ),
            flush=True,
        )
        return 0
    except Exception as exc:
        failure = {
            "run_id": "KMPC-037",
            "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
            "phase": progress["phase"],
            "exception_type": type(exc).__name__,
            "message": str(exc),
            "source_hashes_expected": EXPECTED_SOURCE_HASHES,
            "immutable_prerequisite_expected": EXPECTED_PREREQUISITE_HASH,
            "score_effect": "NONE",
            "release_trigger": "NONE",
            "zenodo_trigger": "NONE",
            "prediction_table_effect": "NONE",
        }
        if not _output_conflicts():
            try:
                _write_atomic_exclusive(FAILURE_OUTPUT, failure)
            except FileExistsError:
                failure["failure_write_status"] = "PRESERVED_EXISTING_FAILURE_FILE"
        else:
            failure["failure_write_status"] = "PRESERVED_EXISTING_OUTPUT_CONFLICT"
        print(json.dumps(_json_safe(failure), sort_keys=True), file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
