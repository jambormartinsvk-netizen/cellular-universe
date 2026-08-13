"""CLI runner for the KMPC-148 read-only C3 logical aggregate.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import traceback

from baseScripts.p5_general_synchronous import (
    c3_authoritative_logical_aggregate as audit,
)


RUN_ID = "KMPC-148"
OUTPUT_NAME = (
    "RUN_KMPC_148_P5_3G7_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_45_OF_45.json"
)
FAILURE_NAME = OUTPUT_NAME.replace(".json", "_TECHNICAL_FAILURE.json")
EXPECTED_BASE_SHA256 = "EE688EAEFC370163F6AE555E169AC61A78D03EFEECC635101DA06D4ECAC17505"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read-only exact-hash aggregate of 45 authoritative C3 atoms."
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--aggregate", action="store_true")
    action.add_argument("--smoke", action="store_true")
    parser.add_argument("--result-dir", type=Path)
    parser.add_argument("--track-dir", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-runtime-seconds", type=float, default=4.8)
    return parser


def _write_immutable_json(path: Path, payload: dict[str, object]) -> None:
    if path.exists():
        raise FileExistsError(f"immutable output already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    if temporary.exists():
        raise FileExistsError(f"stale temporary output exists: {temporary}")
    try:
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    except Exception:
        if temporary.exists():
            temporary.unlink()
        raise


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent
    base_path = Path(audit.__file__).resolve()
    observed_base_hash = audit.sha256_file(base_path)
    if observed_base_hash != EXPECTED_BASE_SHA256:
        raise RuntimeError(
            f"base SHA-256 mismatch: {observed_base_hash} != {EXPECTED_BASE_SHA256}"
        )
    if args.smoke:
        payload = audit.run_smoke()
        payload["source_hashes"] = {
            "base": observed_base_hash,
            "runner": audit.sha256_file(script_path),
        }
        print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
        return 0 if payload["pass"] is True else 2

    result_dir = (
        args.result_dir.resolve()
        if args.result_dir is not None
        else (script_path.parent / "results" / "k_mpc_005").resolve()
    )
    track_dir = (
        args.track_dir.resolve()
        if args.track_dir is not None
        else (
            project_root
            / "tracks"
            / "A1"
            / "A1K1"
            / "A2"
            / "A2K4"
            / "SUBTRACKS"
            / "P5"
            / "P5_3_SEEDS"
        ).resolve()
    )
    output = (
        args.output.resolve()
        if args.output is not None
        else (result_dir / OUTPUT_NAME).resolve()
    )
    if output.parent != result_dir or output.name != OUTPUT_NAME:
        raise ValueError("official output must use the frozen name inside result-dir")
    if output.exists():
        raise FileExistsError(f"immutable output already exists: {output}")
    try:
        payload = audit.run_aggregate(
            args.max_runtime_seconds, result_dir, track_dir
        )
        payload["source_hashes"] = {
            "base": observed_base_hash,
            "runner": audit.sha256_file(script_path),
        }
        _write_immutable_json(output, payload)
    except Exception as exc:
        failure = result_dir / FAILURE_NAME
        failure_payload = {
            "run_id": RUN_ID,
            "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
            "physics_verdict": "NONE_TECHNICAL_FAILURE",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "traceback": traceback.format_exc(),
            "operation_counts": {
                "workers": 0,
                "solvers": 0,
                "physics": 0,
                "matrices_built": 0,
            },
            "source_hashes": {
                "base": observed_base_hash,
                "runner": audit.sha256_file(script_path),
            },
            "score_effect": "NONE",
            "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
        }
        _write_immutable_json(failure, failure_payload)
        print(f"{RUN_ID} technical failure receipt: {failure}", file=sys.stderr)
        return 3
    print(json.dumps({
        "run_id": RUN_ID,
        "output": str(output),
        "candidate_interpretation_not_verdict": (
            payload["candidate_interpretation_not_verdict"]
        ),
        "aggregate_gate_pass": payload["aggregate_gate_pass"],
        "observed_atoms": payload["logical_register"]["observed_atoms"],
        "runtime_seconds": payload["runtime_seconds"],
        "operation_counts": payload["operation_counts"],
    }, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(
            f"{RUN_ID} pre-output technical failure: {type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        raise SystemExit(2)
