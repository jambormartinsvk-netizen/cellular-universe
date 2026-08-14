"""CLI extension for one 45-second C2 high-precision boundary.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
This module changes only the runtime argument contract of the stable harness.
"""

from __future__ import annotations

import math
from pathlib import Path

from . import c2_atomic_runner_harness as stable


SMOKE_SECONDS = 4.8
AUDIT_SECONDS = 45.0


def _validate_args(args, run_id: str) -> None:
    expected = SMOKE_SECONDS if args.smoke else AUDIT_SECONDS
    if not math.isfinite(args.max_runtime_seconds) or args.max_runtime_seconds != expected:
        raise ValueError(f"{run_id} requires exactly {expected} runtime seconds")
    if args.smoke and any(value is not None for value in (args.mode, args.k_mpc, args.output)):
        raise ValueError("smoke forbids mode/k/output")
    if args.atom and any(value is None for value in (args.mode, args.k_mpc, args.output)):
        raise ValueError("atom requires mode/k/output")
    if args.aggregate:
        raise ValueError("high-precision boundary forbids aggregate")


def run_cli(*, expected_high_precision_harness_hash: str, **kwargs) -> int:
    observed = stable.sha256_file(Path(__file__).resolve())
    if observed != expected_high_precision_harness_hash:
        raise RuntimeError("high-precision C2 harness hash mismatch")
    original = stable._validate_args
    try:
        stable._validate_args = _validate_args
        return stable.run_cli(**kwargs)
    finally:
        stable._validate_args = original
