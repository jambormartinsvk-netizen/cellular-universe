"""CLI runner for the KMPC-127 read-only C2 authoritative atom aggregate.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from baseScripts.p5_general_synchronous import c2_authoritative_atom_aggregate as audit


RUN_ID = "KMPC-127"
OUTPUT_NAME = (
    "RUN_KMPC_127_P5_3G7_C2_FOURIER_COVERAGE_AUTHORITATIVE_AGGREGATE.json"
)
EXPECTED_BASE_SHA256 = (
    "69E0C35CDC871CEB5185C51D35A3F26D3B26FD4D6117DC443E6E16CB7EEE8EEC"
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read-only exact-hash aggregate of ten authoritative C2 atoms."
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--aggregate", action="store_true")
    action.add_argument("--smoke", action="store_true")
    parser.add_argument("--result-dir", type=Path)
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
    script_dir = script_path.parent
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
        else (script_dir / "results" / "k_mpc_005").resolve()
    )
    output = (
        args.output.resolve()
        if args.output is not None
        else (result_dir / OUTPUT_NAME).resolve()
    )
    if output.parent != result_dir or output.name != OUTPUT_NAME:
        raise ValueError("official output must be the frozen name inside result-dir")
    if output.exists():
        raise FileExistsError(f"immutable output already exists: {output}")
    payload = audit.run_aggregate(args.max_runtime_seconds, result_dir)
    payload["source_hashes"] = {
        "base": observed_base_hash,
        "runner": audit.sha256_file(script_path),
    }
    _write_immutable_json(output, payload)
    print(json.dumps({
        "run_id": RUN_ID,
        "output": str(output),
        "candidate_interpretation_not_verdict": (
            payload["candidate_interpretation_not_verdict"]
        ),
        "aggregate_gate_pass": payload["aggregate_gate_pass"],
        "runtime_seconds": payload["runtime_seconds"],
    }, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(
            f"{RUN_ID} technical failure: {type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        raise SystemExit(2)
