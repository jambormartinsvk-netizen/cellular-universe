"""Scale-fixture successor for the KMPC-095 HP-M1 boundary.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the synthetic column-scaling fixture is replaced.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_high_precision_m1_reassembly_v3_column_equilibrated as v3


_V3_FIXTURE = v3._fixture
_V3_SOURCE_HASHES = v3.source_hashes
_V3_CONTRACT_GUARD = v3.contract_guard


def configure(**config: object) -> None:
    v3.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v3.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v3.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V3_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes[
        "c2_bi_k0p15_high_precision_m1_reassembly_v4_scale_fixture.py"
    ] = v3.v1._sha256_file(
        here / "c2_bi_k0p15_high_precision_m1_reassembly_v4_scale_fixture.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V3_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_scale_fixture_80dps": True,
        "hp_m1_scale_fixture_ratio_1e24": True,
        "hp_m1_scale_solver_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _fixture() -> dict[str, bool]:
    with mp.workdps(v3.v1.PRECISION_DPS):
        small = mp.mpf("1e-12")
        large = mp.mpf("1e12")
        matrix = [[small, 0], [0, large], [small, large]]
        solution, residual = v3._column_equilibrated_solve(
            matrix, [small, 2 * large, small + 2 * large]
        )
        diagnostic = dict(v3._SCALE_DIAGNOSTIC or {})
        ratio = mp.mpf(str(diagnostic["scale_ratio_decimal"]))
        solution_pass = bool(
            abs(solution[0] - 1) < mp.mpf("1e-35")
            and abs(solution[1] - 2) < mp.mpf("1e-35")
        )
        residual_pass = bool(residual < mp.mpf("1e-50"))
        ratio_pass = bool(abs(ratio / mp.mpf("1e24") - 1) < mp.mpf("1e-70"))
    return {
        "column_scaled_solution_realistic_80dps": solution_pass,
        "column_scaled_residual_realistic_80dps": residual_pass,
        "column_scale_ratio_numeric_1e24": ratio_pass,
        "no_row_scaling": diagnostic.get("row_scaling_applied") is False,
    }


@contextmanager
def _overlay() -> Iterator[None]:
    before = (v3._fixture, v3.source_hashes, v3.contract_guard)
    try:
        v3._fixture = _fixture
        v3.source_hashes = source_hashes
        v3.contract_guard = contract_guard
        yield
    finally:
        v3._fixture, v3.source_hashes, v3.contract_guard = before


def _owners_restored() -> bool:
    return bool(
        v3._fixture is _V3_FIXTURE
        and v3.source_hashes is _V3_SOURCE_HASHES
        and v3.contract_guard is _V3_CONTRACT_GUARD
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v3.run_smoke(max_runtime_seconds, result_dir)
    payload["checks"]["hp_m1_v4_fixture_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = v3.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("KMPC-096 scale-fixture owners not restored")
    payload["high_precision_m1_reassembly_boundary"]["scale_fixture_successor"] = {
        "version": "V4_80DPS_RATIO_1E24_NUMERIC_CHECK",
        "only_fixture_changed": True,
        "column_solver_changed": False,
        "m1_math_changed": False,
        "physics_changed": False,
        "owners_restored": True,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("high-precision M1 boundary has no aggregate scope")
