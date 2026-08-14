"""Bounded runner for KMPC-048 GLOBAL_C1 / NID_SUPPORT_STEP_2.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

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
CANONICAL_OUTPUT = RESULT_DIR / "RUN_KMPC_048_P5_3G7_NID_SUPPORT_STEP_2_05_07.json"
FAILURE_OUTPUT = RESULT_DIR / "RUN_KMPC_048_P5_3G7_NID_SUPPORT_STEP_2_05_07_TECHNICAL_FAILURE.json"
TEMP_OUTPUT = RESULT_DIR / f".tmp-{CANONICAL_OUTPUT.name}"
EXPECTED_SOURCE_HASHES = {
    "full_ra_b1_preflight.py": "62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D",
    "full_ra_b1_preflight_v2.py": "27C0D6ADA828CA2F59C0D128EB6339074D5940F294272CDABE8127CB84867C7C",
    "full_ra_contract.py": "F3839DA931D24939FA9C5925FD29B1484E722D1A0F24117DC91EBE5F4436D464",
    "full_ra_m3_seed.py": "070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2",
    "mode_resolved_puiseux.py": "5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE",
    "mode_resolved_puiseux_v2_m1_anchored.py": "5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455",
    "s1_collective_contract.py": "F535EE15137BBD6F9C0379821C9CC94DED8EC56037B6105B75BEF65A5884EE68",
    "s_c0_coefficient_passport.py": "C370B610815AFAC345C990E3CFE516D616873F39598F468A5ADBF2C65A2A6B95",
    "s_c0_coefficient_passport_v2_numpy_scalar.py": "06EE03C939FBCCFA6FA130421EEF98D0B8CC7571937EF02A7A46A57367534C11",
    "cdi_c1_coverage.py": "D57CA8CA5571A07440A987F4FB0DDA08A40DAF7EA8C95AF929FC5C936F2FCE0F",
    "nid_c1_coverage.py": "EEEE74848B6F4413914F0CC60230CC824982C7E485A38C77C4495F807975A2CD",
    "cdi_support_ladder.py": "A8257E2195E2AB61B5C4195B80EA44EE7669B5A52F9C8440BA5F5244190E3068",
    "nid_support_step2.py": "7AFA5AD9022FA3EB8BDFB5F77D573939D60B2312A0FA29493D6505695958EE5B",
}
EXPECTED_PREREQUISITES = {
    "RUN_KMPC_047_P5_3G7_NID_C1_PRIMARY_EXTENDED_COVERAGE.json": "EED63396DB99C0818306C581413572BE647630CFD0433A8F05A1DCE704DC696A",
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
        raise FileExistsError(f"immutable KMPC-048 output conflict: {conflicts}")
    actual = {name: _sha256_file(BASE_DIR / name) for name in EXPECTED_SOURCE_HASHES}
    if actual != EXPECTED_SOURCE_HASHES:
        different = sorted(
            name for name, expected in EXPECTED_SOURCE_HASHES.items()
            if actual.get(name) != expected
        )
        raise RuntimeError(f"KMPC-048 exact pre-import source hash mismatch: {different}")
    for name, expected in EXPECTED_PREREQUISITES.items():
        if _sha256_file(RESULT_DIR / name) != expected:
            raise RuntimeError(f"KMPC-048 immutable prerequisite hash mismatch: {name}")
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
        encoded = json.dumps(_json_safe(payload), indent=2, sort_keys=True, allow_nan=False) + "\n"
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.link(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _runtime_guard(value: float | None) -> None:
    if value is None or not math.isfinite(value) or value != 4.8:
        raise ValueError("KMPC-048 requires exactly 4.8 runtime seconds")


def _runner_fixtures() -> dict[str, bool]:
    fixture = RESULT_DIR / ".KMPC048_publish_collision_fixture.json"
    temporary = fixture.parent / f".tmp-{fixture.name}"
    if fixture.exists() or temporary.exists():
        raise FileExistsError("stale KMPC-048 publish fixture")
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
        _runtime_guard(None)
        missing_runtime_rejected = False
    except ValueError:
        missing_runtime_rejected = True
    nonfinite_rejected = False
    try:
        _json_safe(float("inf"))
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
            "Bounded KMPC-048 NID support step 2: regression [0,3]/[0,5], "
            "candidate [0,5], audit [0,7], common 0..5, tail 6,7."
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
    try:
        _runtime_guard(args.max_runtime_seconds)
        if args.smoke and args.output is not None:
            raise ValueError("smoke forbids --output")
        if args.audit:
            if args.output is None:
                raise ValueError("audit requires canonical --output")
            requested = args.output if args.output.is_absolute() else SCRIPT_DIR.parent / args.output
            if requested.resolve() != CANONICAL_OUTPUT.resolve():
                raise ValueError("audit requires canonical KMPC-048 --output")
        progress["phase"] = "preimport_guard"
        preimport = _preimport_guard()
        progress["phase"] = "guarded_import"
        from baseScripts.p5_general_synchronous import nid_support_step2 as audit

        if audit.source_hashes() != EXPECTED_SOURCE_HASHES:
            raise RuntimeError("KMPC-048 post-import source hash mismatch")
        if args.smoke:
            progress["phase"] = "runner_smoke"
            runner = _runner_fixtures()
            if not all(runner.values()):
                raise RuntimeError("KMPC-048 runner fixture failed")
            progress["phase"] = "base_smoke"
            payload = audit.run_smoke(args.max_runtime_seconds, RESULT_DIR)
            if not payload["passed"]:
                raise RuntimeError("KMPC-048 base smoke failed")
            payload["runner_negative_fixtures"] = runner
            safe = _json_safe(payload)
            json.dumps(safe, allow_nan=False)
            print(json.dumps(safe, sort_keys=True), flush=True)
            return 0
        progress["phase"] = "audit"
        payload = audit.run_audit(args.max_runtime_seconds, RESULT_DIR)
        if payload["source_hashes"] != preimport:
            raise RuntimeError("KMPC-048 payload source hash mismatch")
        progress["phase"] = "publish"
        _write_atomic_exclusive(CANONICAL_OUTPUT, payload)
        safe = _json_safe(payload)
        print(
            json.dumps(
                {
                    "run_id": safe["run_id"],
                    "execution_status": safe["execution_status"],
                    "candidate": safe["candidate_interpretation_not_verdict"],
                    "regression_pass": safe["regression_against_KMPC047"]["pass"],
                    "core_pass": safe["core_pass"],
                    "common_pass": safe["common_coefficient_pass"],
                    "tail_pass": safe["pure_tail_pass"],
                    "output": str(CANONICAL_OUTPUT),
                },
                sort_keys=True,
            ),
            flush=True,
        )
        return 0
    except Exception as exc:
        failure = {
            "run_id": "KMPC-048",
            "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
            "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
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
