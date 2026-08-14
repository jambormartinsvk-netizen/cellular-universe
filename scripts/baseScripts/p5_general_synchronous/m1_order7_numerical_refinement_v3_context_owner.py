"""KMPC-039 owner-corrected wrapper for the frozen KMPC-038 overlay."""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
from typing import Iterator

import mpmath as mpmath_module

from . import m1_order7_numerical_refinement as v1
from . import m1_order7_numerical_refinement_v2_householder as v2


RUN_ID = "KMPC-039"


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    hashes = v2.source_hashes()
    path = Path(__file__).resolve()
    hashes[path.name] = _sha256_file(path)
    return hashes


def _owner_guard(module: object, context: object) -> bool:
    callable_object = getattr(context, "householder", None)
    return bool(
        not hasattr(module, "householder")
        and callable_object is not None
        and getattr(callable_object, "__self__", None) is context
        and v2._callable_guard(callable_object)
    )


@contextmanager
def _context_owner_bridge() -> Iterator[None]:
    module_owner = v2.mp
    context_owner = mpmath_module.mp
    if module_owner is not mpmath_module:
        raise RuntimeError("unexpected KMPC-038 overlay module owner")
    if not _owner_guard(module_owner, context_owner):
        raise RuntimeError("unexpected mpmath context householder owner")
    v2.mp = context_owner
    try:
        yield
    finally:
        v2.mp = module_owner
        if v2.mp is not mpmath_module:
            raise RuntimeError("KMPC-039 mpmath module owner was not restored")


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if max_runtime_seconds != v1.SMOKE_LIMIT_SECONDS:
        raise ValueError("KMPC-039 smoke requires exactly 4.8 seconds")
    success = result_dir / "RUN_KMPC_039_P5_3G7_M1_ORDER7_CONTEXT_OWNER.json"
    failure = result_dir / "RUN_KMPC_039_P5_3G7_M1_ORDER7_CONTEXT_OWNER_TECHNICAL_FAILURE.json"
    if success.exists() or failure.exists():
        raise FileExistsError("KMPC-039 immutable output already exists")
    module_owner = v2.mp
    owner_guard_pass = _owner_guard(module_owner, mpmath_module.mp)
    with _context_owner_bridge():
        context = v2.mp
        original_function = getattr(context.householder, "__func__", context.householder)
        with context.workdps(v1.PRECISION_DPS):
            zero_diagonal = context.matrix([[0, 1], [1, 0], [1, 1]])
            exact_rhs = context.matrix([2, 1, 3])
            try:
                context.qr_solve(zero_diagonal, exact_rhs)
                original_zero_diagonal_rejected = False
            except (ValueError, ZeroDivisionError):
                original_zero_diagonal_rejected = True
            repaired_solution, repaired_residual = v2._solve_with_overlay(
                zero_diagonal, exact_rhs
            )
            repaired_fixture_pass = bool(
                abs(repaired_solution[0] - 1) < context.mpf("1e-70")
                and abs(repaired_solution[1] - 2) < context.mpf("1e-70")
                and repaired_residual < context.mpf("1e-70")
            )
            regular_matrix = context.matrix([[1, 0], [0, 1], [1, 1]])
            regular_rhs = context.matrix([1, 2, 3])
            original_regular, _ = context.qr_solve(regular_matrix, regular_rhs)
            repaired_regular, _ = v2._solve_with_overlay(
                regular_matrix, regular_rhs
            )
            regular_parity = bool(
                max(
                    abs(original_regular[index] - repaired_regular[index])
                    for index in range(2)
                )
                < context.mpf("1e-70")
            )
        restored_function = getattr(context.householder, "__func__", context.householder)
        callable_restored = restored_function is original_function
    owner_restored = v2.mp is module_owner
    fixtures = {
        "context_owner_guard": owner_guard_pass,
        "original_zero_diagonal_rejected": original_zero_diagonal_rejected,
        "repaired_zero_diagonal_pass": repaired_fixture_pass,
        "nonzero_diagonal_parity": regular_parity,
        "householder_callable_restored": callable_restored,
        "module_owner_restored": owner_restored,
        "wrong_owner_rejected": not _owner_guard(mpmath_module.mp, mpmath_module),
        "second_solve_rejected": not v2._operation_guard(2, 1),
    }
    if not all(fixtures.values()):
        raise RuntimeError("KMPC-039 context-owner smoke fixture failed")
    return {
        "run_id": RUN_ID,
        "smoke_pass": True,
        "fixtures": fixtures,
        "precision_dps": v1.PRECISION_DPS,
        "mpmath_linalg_expected_sha256": v2.EXPECTED_MPMATH_LINALG_HASH,
    }


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if max_runtime_seconds != v1.AUDIT_LIMIT_SECONDS:
        raise ValueError("KMPC-039 audit requires exactly 45 seconds")
    with _context_owner_bridge():
        payload = v2.run_audit(max_runtime_seconds, result_dir)
    payload["run_id"] = RUN_ID
    payload["test"] = (
        "A2-K4 P5.3g7 GLOBAL_C1 M1_ORDER7_NUMERICAL_REFINEMENT_"
        "HOUSEHOLDER_CONTEXT_OWNER_SUCCESSOR_AUDIT"
    )
    payload["technical_successor"]["predecessor"] = "KMPC-038 / PF-073"
    payload["technical_successor"]["owner_bridge"] = (
        "mpmath module export to mpmath.mp context owner"
    )
    payload["operation_counts"]["context_owner_bridges"] = 1
    payload["source_hashes"] = source_hashes()
    return payload
