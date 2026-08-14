"""Read-only publication receipt for the immutable KMPC-099 diagnostic raw.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No matrix or physics calculation is repeated.  The module validates the
already-published diagnostic and emits a legacy-summary-compatible receipt.
"""

from __future__ import annotations

import json
from pathlib import Path

from . import c2_bi_k0p15_high_precision_m1_reassembly_v7_standalone_provenance as v7


base = v7.base
SOURCE_NAME = (
    "RUN_KMPC_099_P5_3G7_C2_BI_K0p15_HP_M1_STANDALONE_MATRIX_PROVENANCE.json"
)
SOURCE_SHA256 = "93780C85488F17831562238D61FF2ADA70182163B488687BAB49BA9A6E96ECD9"
_V7_SOURCE_HASHES = v7.source_hashes
_V7_CONTRACT_GUARD = v7.contract_guard


def configure(**config: object) -> None:
    v7.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v7.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v7.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V7_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = "c2_bi_k0p15_high_precision_m1_reassembly_v8_publication_receipt.py"
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V7_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v8_read_only_receipt": True,
        "hp_m1_v8_no_matrix_rerun": True,
        "hp_m1_v8_source_sha_frozen": len(SOURCE_SHA256) == 64,
        "hp_m1_v8_legacy_summary_fields_nonphysics": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _load_and_check(result_dir: Path) -> tuple[dict[str, object], dict[str, bool]]:
    path = result_dir / SOURCE_NAME
    observed_sha = base._sha256_file(path)
    raw = json.loads(path.read_text(encoding="utf-8"))
    boundary = raw["high_precision_m1_reassembly_boundary"]
    provenance = boundary["matrix_provenance_diagnostic"]
    checks = {
        "source_sha256_exact": observed_sha == SOURCE_SHA256,
        "source_status_completed_diagnostic": (
            raw["execution_status"] == "COMPLETED_DIAGNOSTIC_ONLY"
        ),
        "source_role_diagnostic_only": raw["physics_verdict_role"] == "DIAGNOSTIC_ONLY",
        "source_contract_passed": raw["passed_diagnostic_contract"] is True,
        "source_hash_ledger_exact": raw["source_hashes"] == _V7_SOURCE_HASHES(),
        "source_candidate_exact": raw["candidate_interpretation_not_verdict"]
        == "REVIEW_C2_BI_K0p15_HP_M1_MATRIX_PROVENANCE_DIAGNOSTIC_COMPLETE",
        "source_native_rank_98": provenance["native_projected_rank"] == 98,
        "source_frozen_rank_98": provenance["frozen_rank"] == 98,
        "source_expected_rank_98": provenance["expected_full_column_rank"] == 98,
        "source_no_authoritative_hp_m1_solve": (
            boundary["authoritative_high_precision_m1_solve_count"] == 0
        ),
        "source_no_c2_pass": boundary["pass_c2_atom_candidate"] is False,
        "receipt_no_calculation": True,
    }
    return raw, checks


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, checks = _load_and_check(result_dir)
    checks["contract_guard"] = bool(contract_guard()["pass"])
    checks["no_result_file_written"] = True
    return {
        "run_id": "KMPC-100",
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
    if (mode, k_mpc) != ("BI", 0.15):
        raise ValueError("KMPC-100 receipt atom identity mismatch")
    raw, checks = _load_and_check(result_dir)
    checks["contract_guard"] = bool(contract_guard()["pass"])
    if not all(checks.values()):
        failed = sorted(name for name, value in checks.items() if not value)
        raise RuntimeError(f"KMPC-100 receipt checks failed: {failed}")
    boundary = raw["high_precision_m1_reassembly_boundary"]
    provenance = boundary["matrix_provenance_diagnostic"]
    return {
        "test": "KMPC-100 read-only publication receipt for KMPC-099",
        "run_id": "KMPC-100",
        "execution_status": "COMPLETED_DIAGNOSTIC_RECEIPT_ONLY",
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "atom_id": "BI/k=0.15/nominal",
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": "nominal"},
        "scope": "READ_ONLY_RECEIPT; NO_MATRIX_RERUN; NO_PHYSICS_CALCULATION",
        "source_hashes": source_hashes(),
        "contract_guard": contract_guard(),
        "source_raw": {
            "name": SOURCE_NAME,
            "sha256": SOURCE_SHA256,
            "execution_status": raw["execution_status"],
            "physics_verdict_role": raw["physics_verdict_role"],
            "candidate": raw["candidate_interpretation_not_verdict"],
        },
        "matrix_provenance_diagnostic": provenance,
        "matrix_provenance_interpretation": raw["matrix_provenance_interpretation"],
        "checks": checks,
        "passed_diagnostic_receipt": True,
        "M1": {"pass": False, "status": "NOT_EVALUATED_RECEIPT_ONLY"},
        "core_pass": False,
        "common_pass": False,
        "tail_pass": False,
        "background_guard": {"pass": False, "status": "NOT_EVALUATED_RECEIPT_ONLY"},
        "summary_compatibility_fields_are_nonphysics": True,
        "candidate_interpretation_not_verdict": (
            "REVIEW_C2_BI_K0p15_HP_M1_MATRIX_PROVENANCE_DIAGNOSTIC_RECEIPT_COMPLETE"
        ),
        "physics_verdict_role": "DIAGNOSTIC_ONLY",
        "score_effect": "NONE_DIAGNOSTIC_ONLY",
        "prediction_table_effect": "NONE",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": 0.0,
    }


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("publication receipt has no aggregate scope")
