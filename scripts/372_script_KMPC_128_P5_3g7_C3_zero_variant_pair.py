"""CLI runner for KMPC-128 C3 gamma0/af0 pair receipts.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import traceback

from baseScripts.p5_general_synchronous import c3_zero_variant_pair as c3


RUN_ID = "KMPC-128"
EXPECTED_BASE_SHA256 = (
    "45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0"
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run one frozen C3 mode-k gamma0/af0 pair receipt."
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--smoke", action="store_true")
    action.add_argument("--audit", action="store_true")
    parser.add_argument("--mode", choices=c3.MODES, required=True)
    parser.add_argument("--k", type=float, choices=c3.K_VALUES, required=True)
    parser.add_argument("--result-dir", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-runtime-seconds", type=float, default=4.8)
    return parser


def _native(value: object) -> object:
    if isinstance(value, dict):
        return {str(key): _native(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_native(item) for item in value]
    if hasattr(value, "item") and callable(getattr(value, "item")):
        return _native(value.item())
    return value


def _write_immutable_json(path: Path, payload: dict[str, object]) -> None:
    if path.exists():
        raise FileExistsError(f"immutable output already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    if temporary.exists():
        raise FileExistsError(f"stale temporary output exists: {temporary}")
    try:
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(
                _native(payload), handle, indent=2, sort_keys=True, allow_nan=False
            )
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
    base_path = Path(c3.__file__).resolve()
    observed_base_hash = c3.sha256_file(base_path)
    if observed_base_hash != EXPECTED_BASE_SHA256:
        raise RuntimeError(
            f"base SHA-256 mismatch: {observed_base_hash} != {EXPECTED_BASE_SHA256}"
        )
    result_dir = (
        args.result_dir.resolve()
        if args.result_dir is not None
        else (script_dir / "results" / "k_mpc_005").resolve()
    )
    if args.smoke:
        payload = c3.run_smoke(args.mode, args.k, result_dir)
        payload["source_hashes"] = {
            "base": observed_base_hash,
            "runner": c3.sha256_file(script_path),
        }
        print(json.dumps(_native(payload), indent=2, sort_keys=True, allow_nan=False))
        return 0 if payload["pass"] is True else 2

    expected_name = c3.output_name(args.mode, args.k)
    output = (
        args.output.resolve()
        if args.output is not None
        else (result_dir / expected_name).resolve()
    )
    if output.parent != result_dir or output.name != expected_name:
        raise ValueError("official output must use the frozen name inside result-dir")
    if output.exists():
        raise FileExistsError(f"immutable output already exists: {output}")
    progress: dict[str, str] = {"last_completed_phase": "CLI_AND_HASH_GUARD"}
    try:
        payload = c3.run_pair(
            args.mode,
            args.k,
            args.max_runtime_seconds,
            result_dir,
            progress,
        )
        payload["source_hashes"]["runner"] = c3.sha256_file(script_path)
        _write_immutable_json(output, payload)
    except Exception as exc:
        failure = result_dir / c3.failure_name(args.mode, args.k)
        failure_payload = {
            "run_id": RUN_ID,
            "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
            "physics_verdict": "NONE_TECHNICAL_FAILURE",
            "authorship": {
                "theory_author": "Martin Jambor",
                "script_creator": "Codex (OpenAI)",
            },
            "identity": {
                "mode": args.mode,
                "k_Mpc_inverse": args.k,
                "physical_receipt": "gamma0_af0_pair",
            },
            "last_completed_phase": progress.get("last_completed_phase", "NONE"),
            "current_phase": progress.get("current_phase", "UNKNOWN"),
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "traceback": traceback.format_exc(),
            "source_hashes": {
                "base": observed_base_hash,
                "runner": c3.sha256_file(script_path),
            },
            "score_effect": "NONE",
            "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
        }
        _write_immutable_json(failure, failure_payload)
        print(
            f"{RUN_ID} technical failure receipt: {failure}",
            file=sys.stderr,
        )
        return 3
    print(json.dumps({
        "run_id": RUN_ID,
        "output": str(output),
        "candidate_interpretation_not_verdict": (
            payload["candidate_interpretation_not_verdict"]
        ),
        "pair_pass": payload["pair_pass"],
        "runtime_seconds": payload["runtime_seconds"],
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
