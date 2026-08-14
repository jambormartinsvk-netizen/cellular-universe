"""Bounded runner for KMPC-036 GLOBAL_C1 / M1_ORDER7_PROVENANCE_GATE."""

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
CANONICAL_OUTPUT = RESULT_DIR / "RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json"
FAILURE_OUTPUT = RESULT_DIR / "RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE_TECHNICAL_FAILURE.json"
EXPECTED_SOURCE_HASHES = {
    "mode_resolved_puiseux.py": "5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE",
    "mode_resolved_puiseux_v2_m1_anchored.py": "5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455",
    "m1_order7_provenance.py": "0B1EB4C76A7388D6A8F6D1E5DD933549043337381DEF6DE77539D3F84CA7BAC7",
}


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _preimport_hashes() -> dict[str, str]:
    actual = {name: _sha256_file(BASE_DIR / name) for name in EXPECTED_SOURCE_HASHES}
    if actual != EXPECTED_SOURCE_HASHES:
        raise RuntimeError("KMPC-036 exact pre-import source hash mismatch")
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
    return value


def _write_atomic_exclusive(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.parent / f".tmp-{path.name}"
    if temporary.exists():
        raise FileExistsError(f"stale temporary artifact exists: {temporary}")
    safe = _json_safe(payload)
    encoded = json.dumps(safe, indent=2, sort_keys=True, allow_nan=False)
    with temporary.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(encoded)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.link(temporary, path)
    temporary.unlink()


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Bounded KMPC-036 GLOBAL_C1 / M1_ORDER7_PROVENANCE_GATE only; "
            "does not run CDI support step 3."
        )
    )
    parser.add_argument("--max-runtime-seconds", type=float, default=4.8)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--smoke", action="store_true")
    mode.add_argument("--audit", action="store_true")
    parser.add_argument("--output", type=Path)
    return parser


def main() -> int:
    args = _parser().parse_args()
    progress = {"phase": "argument_guard"}
    if args.max_runtime_seconds != 4.8:
        raise SystemExit("KMPC-036 requires exactly --max-runtime-seconds 4.8")
    if args.smoke and args.output is not None:
        raise SystemExit("smoke forbids --output")
    if args.audit:
        if args.output is None:
            raise SystemExit("audit requires canonical --output")
        if args.output.resolve() != CANONICAL_OUTPUT.resolve():
            raise SystemExit("noncanonical KMPC-036 output path")
    try:
        progress["phase"] = "preimport_hash"
        preimport = _preimport_hashes()
        progress["phase"] = "guarded_import"
        from baseScripts.p5_general_synchronous import m1_order7_provenance as audit

        if audit.source_hashes() != EXPECTED_SOURCE_HASHES:
            raise RuntimeError("KMPC-036 post-import source hash mismatch")
        if args.smoke:
            progress["phase"] = "smoke"
            payload = audit.run_smoke(args.max_runtime_seconds, RESULT_DIR)
            safe = _json_safe(payload)
            json.dumps(safe, allow_nan=False)
            print(json.dumps(safe, sort_keys=True), flush=True)
            return 0
        progress["phase"] = "audit"
        payload = audit.run_audit(args.max_runtime_seconds, RESULT_DIR)
        if payload["source_hashes"] != preimport:
            raise RuntimeError("KMPC-036 payload source hash mismatch")
        progress["phase"] = "publish"
        _write_atomic_exclusive(CANONICAL_OUTPUT, payload)
        safe = _json_safe(payload)
        print(
            json.dumps(
                {
                    "run_id": safe["run_id"],
                    "execution_status": safe["execution_status"],
                    "candidate": safe["candidate_interpretation_not_verdict"],
                    "regression_pass": safe["regression_pass"],
                    "core_pass": safe["core_pass"],
                    "output": str(CANONICAL_OUTPUT),
                },
                sort_keys=True,
            ),
            flush=True,
        )
        return 0
    except Exception as exc:
        failure = {
            "run_id": "KMPC-036",
            "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
            "phase": progress["phase"],
            "exception_type": type(exc).__name__,
            "message": str(exc),
            "source_hashes_expected": EXPECTED_SOURCE_HASHES,
            "score_effect": "NONE",
            "release_trigger": "NONE",
            "zenodo_trigger": "NONE",
            "prediction_table_effect": "NONE",
        }
        try:
            _write_atomic_exclusive(FAILURE_OUTPUT, failure)
        except FileExistsError:
            failure["failure_write_status"] = "PRESERVED_EXISTING_FAILURE_FILE"
        print(json.dumps(_json_safe(failure), sort_keys=True), file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
