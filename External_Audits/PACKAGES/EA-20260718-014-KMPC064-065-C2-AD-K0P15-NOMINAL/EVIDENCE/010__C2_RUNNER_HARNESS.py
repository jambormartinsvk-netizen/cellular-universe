"""Stable CLI/publish harness for versioned C2 Fourier audit modules.

This module contains no physics. It centralizes exact-hash guards, immutable
publication, CLI validation, smoke fixtures and technical-failure reporting.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import math
import os
from pathlib import Path
import sys
from types import ModuleType
from typing import Any, Mapping

import numpy as np


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, np.ndarray):
        return json_safe(value.tolist())
    if isinstance(value, np.generic):
        return json_safe(value.item())
    if isinstance(value, float) and not math.isfinite(value):
        raise FloatingPointError("non-finite value cannot be serialized")
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    raise TypeError(f"unsupported JSON scalar: {type(value).__name__}")


def write_exclusive(path: Path, payload: dict[str, Any]) -> None:
    temporary = path.parent / f".tmp-{path.name}"
    if not path.parent.is_dir():
        raise FileNotFoundError(path.parent)
    if path.exists() or temporary.exists():
        raise FileExistsError(f"immutable publish collision: {path}")
    try:
        encoded = json.dumps(json_safe(payload), indent=2, sort_keys=True, allow_nan=False) + "\n"
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.link(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _parser(run_id: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=f"{run_id} C2 Fourier atomic audit harness.")
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--smoke", action="store_true")
    action.add_argument("--atom", action="store_true")
    action.add_argument("--aggregate", action="store_true")
    parser.add_argument("--mode", choices=("AD", "CDI", "BI", "NID", "NIV"))
    parser.add_argument("--k-mpc", type=float)
    parser.add_argument("--output", type=Path)
    return parser


def _validate_args(args: argparse.Namespace, run_id: str) -> None:
    if args.max_runtime_seconds != 4.8 or not math.isfinite(args.max_runtime_seconds):
        raise ValueError(f"{run_id} requires exactly 4.8 runtime seconds")
    if args.smoke and any(value is not None for value in (args.mode, args.k_mpc, args.output)):
        raise ValueError("smoke forbids mode/k/output")
    if args.atom and any(value is None for value in (args.mode, args.k_mpc, args.output)):
        raise ValueError("atom requires mode/k/output")
    if args.aggregate and (args.mode is not None or args.k_mpc is not None or args.output is None):
        raise ValueError("aggregate forbids mode/k and requires output")


def _static_hash_guard(
    base_dir: Path,
    result_dir: Path,
    expected_source_hashes: Mapping[str, str],
    expected_prerequisites: Mapping[str, str],
    expected_harness_hash: str,
) -> dict[str, str]:
    if sha256_file(Path(__file__).resolve()) != expected_harness_hash:
        raise RuntimeError("C2 runner harness hash mismatch")
    actual = {name: sha256_file(base_dir / name) for name in expected_source_hashes}
    if actual != dict(expected_source_hashes):
        different = sorted(name for name in expected_source_hashes if actual.get(name) != expected_source_hashes[name])
        raise RuntimeError(f"exact audit source hash mismatch: {different}")
    for name, expected in expected_prerequisites.items():
        if sha256_file(result_dir / name) != expected:
            raise RuntimeError(f"prerequisite hash mismatch: {name}")
    return actual


def _target_guard(target: Path) -> None:
    failure = target.with_name(target.stem + "_TECHNICAL_FAILURE.json")
    temporary = target.parent / f".tmp-{target.name}"
    conflicts = [str(path) for path in (target, failure, temporary) if path.exists()]
    if conflicts:
        raise FileExistsError(f"immutable output conflict: {conflicts}")


def _runner_fixtures(result_dir: Path, run_id: str) -> dict[str, bool]:
    fixture = result_dir / f".{run_id.replace('-', '')}_publish_collision_fixture.json"
    temporary = fixture.parent / f".tmp-{fixture.name}"
    if fixture.exists() or temporary.exists():
        raise FileExistsError(f"stale {run_id} publish fixture")
    collision_rejected = preserved = False
    try:
        fixture.write_text("sentinel\n", encoding="utf-8")
        try:
            write_exclusive(fixture, {"unexpected": True})
        except FileExistsError:
            collision_rejected = True
        preserved = fixture.read_text(encoding="utf-8") == "sentinel\n"
    finally:
        if temporary.exists():
            temporary.unlink()
        if fixture.exists():
            fixture.unlink()
    return {"collision_rejected": collision_rejected, "target_preserved": preserved,
            "temporary_cleaned": not temporary.exists()}


def _resolve_target(
    args: argparse.Namespace, audit: ModuleType, result_dir: Path, aggregate_name: str
) -> Path | None:
    if args.atom:
        return result_dir / audit.atom_output_name(args.mode, args.k_mpc)
    if args.aggregate:
        return result_dir / aggregate_name
    return None


def run_cli(
    *,
    run_id: str,
    audit_module: str,
    aggregate_name: str,
    expected_source_hashes: Mapping[str, str],
    expected_prerequisites: Mapping[str, str],
    expected_harness_hash: str,
    script_dir: Path,
) -> int:
    args = _parser(run_id).parse_args()
    base_dir = script_dir / "baseScripts" / "p5_general_synchronous"
    result_dir = script_dir / "results" / "k_mpc_005"
    progress = {"phase": "argument_guard", "mode": args.mode, "k_mpc": args.k_mpc}
    target: Path | None = None
    try:
        _validate_args(args, run_id)
        progress["phase"] = "static_hash_guard"
        preimport = _static_hash_guard(
            base_dir, result_dir, expected_source_hashes, expected_prerequisites, expected_harness_hash
        )
        progress["phase"] = "guarded_import"
        audit = importlib.import_module(audit_module)
        target = _resolve_target(args, audit, result_dir, aggregate_name)
        if target is not None:
            _target_guard(target)
            requested = args.output if args.output.is_absolute() else script_dir.parent / args.output
            if requested.resolve() != target.resolve():
                raise ValueError(f"output path differs from canonical {run_id} target")
        if audit.source_hashes() != preimport:
            raise RuntimeError(f"{run_id} post-import source hash mismatch")
        if args.smoke:
            runner_checks = _runner_fixtures(result_dir, run_id)
            payload = audit.run_smoke(args.max_runtime_seconds, result_dir)
            payload["runner_checks"] = runner_checks
            if not payload["passed"] or not all(runner_checks.values()):
                raise RuntimeError(f"{run_id} smoke failed: {payload}")
            print(json.dumps(json_safe(payload), sort_keys=True), flush=True)
            return 0
        progress["phase"] = "audit"
        payload = (audit.run_atom(args.mode, args.k_mpc, args.max_runtime_seconds, result_dir)
                   if args.atom else audit.run_aggregate(args.max_runtime_seconds, result_dir))
        if payload["source_hashes"] != preimport:
            raise RuntimeError(f"{run_id} payload source hash mismatch")
        progress["phase"] = "publish"
        write_exclusive(target, payload)
        safe = json_safe(payload)
        summary = {"run_id": safe["run_id"], "candidate": safe["candidate_interpretation_not_verdict"],
                   "output": str(target)}
        if args.atom:
            summary.update({"atom_id": safe["atom_id"], "M1_pass": safe["M1"]["pass"],
                            "core_pass": safe["core_pass"], "common_pass": safe["common_pass"],
                            "tail_pass": safe["tail_pass"], "background_pass": safe["background_guard"]["pass"]})
        else:
            summary.update({"observed_atoms": safe["matrix"]["observed_atoms"],
                            "all_atoms_pass": safe["all_atoms_pass"],
                            "background_spread_pass": safe["background_spread_pass"]})
        print(json.dumps(summary, sort_keys=True), flush=True)
        return 0
    except Exception as exc:
        failure = {"run_id": run_id, "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
                   "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
                   "phase": progress["phase"], "mode": args.mode, "k_Mpc_inverse": args.k_mpc,
                   "exception_type": type(exc).__name__, "message": str(exc),
                   "source_hashes_expected": dict(expected_source_hashes), "score_effect": "NONE",
                   "release_trigger": "NONE", "zenodo_trigger": "NONE", "prediction_table_effect": "NONE"}
        if target is not None:
            failure_path = target.with_name(target.stem + "_TECHNICAL_FAILURE.json")
            temporary = target.parent / f".tmp-{target.name}"
            if not any(path.exists() for path in (target, failure_path, temporary)):
                write_exclusive(failure_path, failure)
        print(json.dumps(json_safe(failure), sort_keys=True), file=sys.stderr, flush=True)
        return 2
