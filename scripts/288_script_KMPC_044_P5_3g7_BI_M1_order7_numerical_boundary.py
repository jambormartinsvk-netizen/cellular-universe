"""Bounded runner for KMPC-044 BI M1 order-7 numerical boundary closure."""

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


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR / "baseScripts" / "p5_general_synchronous"
RESULT_DIR = SCRIPT_DIR / "results" / "k_mpc_005"
CANONICAL_OUTPUT = RESULT_DIR / "RUN_KMPC_044_P5_3G7_BI_M1_ORDER7_NUMERICAL_BOUNDARY.json"
FAILURE_OUTPUT = RESULT_DIR / "RUN_KMPC_044_P5_3G7_BI_M1_ORDER7_NUMERICAL_BOUNDARY_TECHNICAL_FAILURE.json"
TEMP_OUTPUT = RESULT_DIR / f".tmp-{CANONICAL_OUTPUT.name}"
PREREQUISITE = RESULT_DIR / "RUN_KMPC_043_P5_3G7_BI_M1_ORDER7_PROVENANCE_GATE.json"
EXPECTED_PREREQUISITE_HASH = "B02D1D16CFAE4331378B68F12258142F84A424419BB9D3A52AAEE87D0CC61EB0"
MPMATH_LINALG = Path(sys.prefix) / "Lib" / "site-packages" / "mpmath" / "matrices" / "linalg.py"
EXPECTED_MPMATH_LINALG_HASH = "D380B78A3CCC1689BBA1BE5F5C10837F23CF768DC121BA08784F31D80EAFA85D"
EXPECTED_SOURCE_HASHES = {
    "mode_resolved_puiseux.py": "5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE",
    "mode_resolved_puiseux_v2_m1_anchored.py": "5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455",
    "m1_order7_provenance.py": "0B1EB4C76A7388D6A8F6D1E5DD933549043337381DEF6DE77539D3F84CA7BAC7",
    "bi_m1_order7_provenance.py": "69C65F408635E71B455FBF2135FB5057E0DA01B8E4895B5B5D96733AC4AF03C2",
    "m1_order7_numerical_refinement.py": "CE29222FCE45DAA99A7B8E1FFCC06E9471D648A2B61C14DA05F653DBA9E7A80C",
    "m1_order7_numerical_refinement_v2_householder.py": "81D7EA664677158E98340E39F395DE2EE0DAB6EEFCFFA785089F51E62434193A",
    "m1_order7_numerical_refinement_v3_context_owner.py": "1E35D147049F981F901B9A2B72C76EBE5705F5D19A04447E742AE978A9BC5278",
    "bi_m1_order7_numerical_boundary.py": "FBB920976CAF5FAF2DDA87D1286573E91155A0688C23EB8E2A5AB0EE3B70BFAD",
}


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _output_conflicts() -> list[str]:
    return [
        str(path)
        for path in (CANONICAL_OUTPUT, FAILURE_OUTPUT, TEMP_OUTPUT)
        if path.exists()
    ]


def _preimport_guard() -> dict[str, str]:
    conflicts = _output_conflicts()
    if conflicts:
        raise FileExistsError(f"immutable KMPC-044 output conflict: {conflicts}")
    actual = {name: _sha256_file(BASE_DIR / name) for name in EXPECTED_SOURCE_HASHES}
    if actual != EXPECTED_SOURCE_HASHES:
        different = sorted(
            name
            for name, expected in EXPECTED_SOURCE_HASHES.items()
            if actual.get(name) != expected
        )
        raise RuntimeError(f"KMPC-044 exact pre-import source hash mismatch: {different}")
    if _sha256_file(PREREQUISITE) != EXPECTED_PREREQUISITE_HASH:
        raise RuntimeError("KMPC-044 immutable KMPC-043 prerequisite hash mismatch")
    if _sha256_file(MPMATH_LINALG) != EXPECTED_MPMATH_LINALG_HASH:
        raise RuntimeError("KMPC-044 mpmath linalg hash mismatch")
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


def _write_atomic_exclusive(path: Path, payload: dict[str, Any]) -> None:
    if not path.parent.is_dir():
        raise FileNotFoundError(f"canonical result directory missing: {path.parent}")
    temporary = path.parent / f".tmp-{path.name}"
    if path.exists() or temporary.exists():
        raise FileExistsError(f"immutable publish collision: {path}")
    try:
        encoded = (
            json.dumps(_json_safe(payload), indent=2, sort_keys=True, allow_nan=False)
            + "\n"
        )
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.link(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _runtime_guard(value: float | None, expected: float) -> None:
    if value is None or not math.isfinite(value) or value != expected:
        raise ValueError(f"KMPC-044 requires exactly {expected} runtime seconds")


def _runner_fixtures() -> dict[str, bool]:
    fixture = RESULT_DIR / ".KMPC044_publish_collision_fixture.json"
    temporary = fixture.parent / f".tmp-{fixture.name}"
    if fixture.exists() or temporary.exists():
        raise FileExistsError("stale KMPC-044 publish fixture")
    collision_rejected = False
    preserved = False
    cleaned = False
    try:
        fixture.write_text("sentinel\n", encoding="utf-8")
        try:
            _write_atomic_exclusive(fixture, {"unexpected": True})
        except FileExistsError:
            collision_rejected = True
        preserved = fixture.read_text(encoding="utf-8") == "sentinel\n"
        cleaned = not temporary.exists()
    finally:
        if temporary.exists():
            temporary.unlink()
        if fixture.exists():
            fixture.unlink()
    try:
        _runtime_guard(None, 12.0)
        missing_runtime_rejected = False
    except ValueError:
        missing_runtime_rejected = True
    try:
        _json_safe(float("inf"))
        nonfinite_rejected = False
    except FloatingPointError:
        nonfinite_rejected = True
    return {
        "publish_collision_rejected": collision_rejected,
        "publish_collision_preserved": preserved,
        "publish_temp_cleaned": cleaned,
        "missing_runtime_rejected": missing_runtime_rejected,
        "nonfinite_JSON_rejected": nonfinite_rejected,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Bounded KMPC-044 BI same-matrix numerical boundary closure only: "
            "one correction and one 80-dps QR solve; no support calculation."
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
    expected_runtime = 12.0 if args.smoke else 45.0
    try:
        _runtime_guard(args.max_runtime_seconds, expected_runtime)
        if args.smoke and args.output is not None:
            raise ValueError("smoke forbids --output")
        if args.audit:
            if args.output is None:
                raise ValueError("audit requires canonical --output")
            requested = (
                args.output
                if args.output.is_absolute()
                else SCRIPT_DIR.parent / args.output
            )
            if requested.resolve() != CANONICAL_OUTPUT.resolve():
                raise ValueError("audit requires canonical KMPC-044 --output")
        progress["phase"] = "preimport_guard"
        preimport = _preimport_guard()
        progress["phase"] = "guarded_import"
        from baseScripts.p5_general_synchronous import (
            bi_m1_order7_numerical_boundary as audit,
        )

        if audit.source_hashes() != EXPECTED_SOURCE_HASHES:
            raise RuntimeError("KMPC-044 post-import source hash mismatch")
        if args.smoke:
            progress["phase"] = "runner_smoke"
            runner = _runner_fixtures()
            if not all(runner.values()):
                raise RuntimeError("KMPC-044 runner fixture failed")
            progress["phase"] = "base_exact_matrix_smoke"
            payload = audit.run_smoke(args.max_runtime_seconds, RESULT_DIR)
            payload["runner_negative_fixtures"] = runner
            safe = _json_safe(payload)
            json.dumps(safe, allow_nan=False)
            print(json.dumps(safe, sort_keys=True), flush=True)
            return 0
        progress["phase"] = "audit"
        payload = audit.run_audit(args.max_runtime_seconds, RESULT_DIR)
        if payload["source_hashes"] != preimport:
            raise RuntimeError("KMPC-044 payload source hash mismatch")
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
                    "v2_holdout_pass": safe["v2_single_bounded_refinement"]["holdout"]["pass"],
                    "v3_driver_pass": safe["v3_same_float64_matrix_high_precision"]["driver_and_initial_high_precision"]["pass"],
                    "v3_holdout_pass": safe["v3_same_float64_matrix_high_precision"]["holdout_high_precision"]["pass"],
                    "output": str(CANONICAL_OUTPUT),
                },
                sort_keys=True,
            ),
            flush=True,
        )
        return 0
    except Exception as exc:
        failure = {
            "run_id": "KMPC-044",
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
