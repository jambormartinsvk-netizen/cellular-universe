"""Standalone M1 matrix-provenance diagnostic for BI/k=.15.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
This successor deliberately stops before F0, M3, holdout attribution and all
physics gates.  It answers only whether the native 80-dps M1 assembly and the
frozen binary64 M1 assembly have the same projected rank and coefficients.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
import time
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_high_precision_m1_reassembly_v6_combined_register as v6


v5 = v6.v5
base = v5.base
_V6_SOURCE_HASHES = v6.source_hashes
_V6_CONTRACT_GUARD = v6.contract_guard
_BASE_SOLVE = base._solve_reduced


def configure(**config: object) -> None:
    v6.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v6.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v6.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V6_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = "c2_bi_k0p15_high_precision_m1_reassembly_v7_standalone_provenance.py"
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V6_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v7_standalone_scope": True,
        "hp_m1_v7_no_f0_m3_attribution": True,
        "hp_m1_v7_no_physics_gate": True,
        "hp_m1_v7_no_authoritative_hp_solve": True,
        "hp_m1_v7_v5_provenance_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


@contextmanager
def _diagnostic_overlay() -> Iterator[None]:
    before = (
        base._solve_reduced,
        base._M1_SOLVE_COUNT,
        base._M1_BOUNDARY,
        v5._PROVENANCE,
        v5.v3._SCALE_DIAGNOSTIC,
    )
    base._M1_SOLVE_COUNT = 0
    base._M1_BOUNDARY = None
    v5._PROVENANCE = None
    try:
        base._solve_reduced = v5._matrix_provenance_bridge
        yield
    finally:
        (
            base._solve_reduced,
            base._M1_SOLVE_COUNT,
            base._M1_BOUNDARY,
            v5._PROVENANCE,
            v5.v3._SCALE_DIAGNOSTIC,
        ) = before


def _owners_restored() -> bool:
    return base._solve_reduced is _BASE_SOLVE


def _fixture() -> dict[str, bool]:
    frozen, rhs, rows, columns, identity = v5._frozen_float64_rebuild()
    return {
        "frozen_shape_121x98": frozen.shape == base.EXPECTED_REDUCED_SHAPE,
        "rhs_rows_121": rhs.shape == (base.EXPECTED_REDUCED_SHAPE[0],),
        "labels_complete": len(rows) == 121 and len(columns) == 98,
        "identity_bi_k0p15_order7": (
            identity["mode"] == "BI"
            and identity["k_Mpc_inverse"] == 0.15
            and identity["order"] == 7
        ),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    checks = {
        "contract_guard": bool(contract_guard()["pass"]),
        **{f"standalone_{name}": value for name, value in _fixture().items()},
        "owners_initial": _owners_restored(),
        "no_result_file_written": True,
    }
    return {
        "run_id": "KMPC-099",
        "mode": "SMOKE_NO_RESULT_FILE",
        "checks": checks,
        "passed": all(checks.values()),
    }


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != (base.MODE, base.K_MPC):
        raise ValueError("KMPC-099 standalone atom identity mismatch")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("KMPC-099 standalone M1 deadline exceeded")

    inputs = base.legacy.FrozenInputs()
    reference_legacy, _, reference_metadata = (
        base.physics.m1_anchor.solve_standard_seed_anchored(
            mode, k_mpc, inputs, deadline, order=base.ORDER
        )
    )
    reference_standard = {
        target: dict(reference_legacy[source])
        for target, source in base.physics.STATE_TO_LEGACY.items()
    }
    with mp.workdps(base.PRECISION_DPS):
        with _diagnostic_overlay():
            _, boundary = base._m1_reassembly(inputs, reference_standard)
            provenance = dict(v5._PROVENANCE or {})
    if not _owners_restored() or not provenance:
        raise RuntimeError("KMPC-099 standalone provenance lifecycle incomplete")
    deadline()

    native_rank = int(provenance["native_projected_rank"])
    frozen_rank = int(provenance["frozen_rank"])
    expected_rank = int(provenance["expected_full_column_rank"])
    if native_rank == frozen_rank == expected_rank:
        interpretation = "PROJECTED_SYSTEMS_BOTH_FULL_COLUMN_RANK"
    elif native_rank != frozen_rank:
        interpretation = "PROJECTED_RANK_DIFFERENCE_REQUIRES_ASSEMBLY_AUDIT"
    else:
        interpretation = "PROJECTED_SYSTEMS_SHARE_RANK_DEFICIENCY"

    pipeline_completed = bool(boundary["driver_and_initial"]["pass_driver_and_initial"])
    boundary.update({
        "solver": "DIAGNOSTIC_BINARY64_BRIDGE_NOT_HP_M1_SOLVE",
        "high_precision_m1_solve_count": 0,
        "authoritative_high_precision_m1_solve_count": 0,
        "diagnostic_bridge_solve_count": 1,
        "frozen_reference_binary64_solve_count": 1,
        "diagnostic_pipeline_completed": pipeline_completed,
        "pass": False,
        "pass_c2_atom_candidate": False,
        "matrix_provenance_diagnostic": provenance,
    })
    checks = {
        "contract_guard": bool(contract_guard()["pass"]),
        "matrix_provenance_created": bool(provenance),
        "matrix_shapes_expected": (
            provenance["shape_native"] == [121, 98]
            and provenance["shape_frozen"] == [121, 98]
        ),
        "diagnostic_bridge_disclosed": (
            provenance["diagnostic_bridge"]["authoritative_high_precision_solve"]
            is False
        ),
        "no_authoritative_hp_m1_solve": (
            boundary["authoritative_high_precision_m1_solve_count"] == 0
        ),
        "owners_restored": _owners_restored(),
    }
    return {
        "test": "KMPC-099 standalone HP-M1 matrix-provenance diagnostic",
        "run_id": "KMPC-099",
        "execution_status": "COMPLETED_DIAGNOSTIC_ONLY",
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "order": base.ORDER},
        "scope": (
            "M1_ASSEMBLY_AND_MATRIX_PROVENANCE_ONLY; NO_F0; NO_M3; "
            "NO_HOLDOUT_ATTRIBUTION; NO_C2_PHYSICS_GATE"
        ),
        "source_hashes": source_hashes(),
        "contract_guard": contract_guard(),
        "frozen_reference_standard": {
            "method": "LIVE_FROZEN_BINARY64_HARD_ANCHORED_M1",
            "solve_count": 1,
            "metadata": reference_metadata,
        },
        "high_precision_m1_reassembly_boundary": boundary,
        "matrix_provenance_interpretation": interpretation,
        "checks": checks,
        "passed_diagnostic_contract": all(checks.values()),
        "candidate_interpretation_not_verdict": (
            "REVIEW_C2_BI_K0p15_HP_M1_MATRIX_PROVENANCE_DIAGNOSTIC_COMPLETE"
        ),
        "physics_verdict_role": "DIAGNOSTIC_ONLY",
        "score_effect": "NONE_DIAGNOSTIC_ONLY_PENDING_INTERNAL_AUDIT",
        "prediction_table_effect": "NONE",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("standalone M1 provenance has no aggregate scope")
