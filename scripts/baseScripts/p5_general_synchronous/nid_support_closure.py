"""KMPC-053 NID support-[0,5] closure after depth-7 boundary audit.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

import json
from pathlib import Path
import time
from typing import Callable, Mapping

from . import nid_depth7_numerical_boundary as k52


k51 = k52.k51
k50 = k52.k50
v1 = k52.v1
physics = k52.physics
nid_step = v1.step2
RUN_ID = "KMPC-053"
SUPPORT03 = (0, 3)
SUPPORT05 = (0, 5)
SUPPORT07 = (0, 7)
KMPC052 = (
    "RUN_KMPC_052_P5_3G7_NID_DEPTH7_NUMERICAL_BOUNDARY.json",
    "FDEE962EED16EDF459D7D8504833AB1206AEF1BFC8178A356A88A121CF196C4C",
)
KMPC048 = (
    "RUN_KMPC_048_P5_3G7_NID_SUPPORT_STEP_2_05_07.json",
    "B4F320F5D850DCF78FD9EC2A5BDDEBDA87D590DA2988CF505FA7D5B25B49BF32",
)


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(k52.source_hashes())
    hashes["nid_support_closure.py"] = v1.sha256_file(here / "nid_support_closure.py")
    return hashes


def _load(path: Path, expected: str) -> tuple[dict[str, object], str]:
    observed = v1.sha256_file(path)
    if observed != expected:
        raise RuntimeError(f"immutable prerequisite hash mismatch: {path.name}")
    return json.loads(path.read_text(encoding="utf-8")), observed


def _prerequisites(result_dir: Path) -> tuple[dict[str, object], str, dict[str, object], str]:
    k52_payload, k52_hash = _load(result_dir / KMPC052[0], KMPC052[1])
    k48_payload, k48_hash = _load(result_dir / KMPC048[0], KMPC048[1])
    if k52_payload.get("candidate_interpretation_not_verdict") != (
        "PASS_NID_DEPTH7_FLOAT64_SOLVER_FLOOR_CANDIDATE_ONLY"
    ):
        raise RuntimeError("KMPC-052 candidate mismatch")
    return k52_payload, k52_hash, k48_payload, k48_hash


def _regression(
    immutable: Mapping[str, object],
    solved: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    details: dict[str, object] = {}
    for support in ("03", "05"):
        old = immutable["solved_supports"][support]
        details[f"support_{support}_F0"] = v1.regression_tools._regression_metric(
            v1.regression_tools._restore_series(old["fuel"]["state"]),
            solved[support]["fuel"]["state"],
        )
        details[f"support_{support}_M3"] = v1.regression_tools._regression_metric(
            v1.regression_tools._restore_series(old["m3"]["fractional_state"]),
            solved[support]["m3"]["fractional_state"],
        )
    return {
        "details": details,
        "pass": all(bool(row["pass"]) for row in details.values()),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = v1.make_deadline(max_runtime_seconds)
    k52_payload, k52_hash, _, k48_hash = _prerequisites(result_dir)
    checks = {
        "immutable_KMPC052_hash": k52_hash == KMPC052[1],
        "immutable_KMPC048_hash": k48_hash == KMPC048[1],
        "KMPC052_V0_V2_V3_pass": bool(
            k52_payload["V0_reference_parity"]["pass"]
            and k52_payload["V2_single_bounded_refinement"]["pass"]
            and k52_payload["V3_single_80dps_same_matrix_QR"]["pass"]
        ),
        "supports_exact": (SUPPORT03, SUPPORT05, SUPPORT07)
        == ((0, 3), (0, 5), (0, 7)),
        "tail_contract_exact": nid_step.CANDIDATE_SUPPORT == SUPPORT05
        and nid_step.AUDIT_SUPPORT == SUPPORT07
        and physics.TAIL_TOL == 1.0e-6,
        "correction_cap_exact": k52.CORRECTION_ABS_MAX == 1.0e-14,
    }
    deadline()
    return {
        "run_id": RUN_ID,
        "mode": "SMOKE_NO_RESULT_FILE",
        "checks": checks,
        "passed": all(checks.values()),
    }


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = v1.make_deadline(max_runtime_seconds)
    k52_payload, k52_hash, k48_payload, k48_hash = _prerequisites(result_dir)
    inputs = physics._variant_inputs(v1.VARIANT)
    standard, m1meta = k51._standard_depth(7, inputs, deadline)
    solved03 = nid_step._solve_support(SUPPORT03, inputs, standard, deadline)
    solved05 = nid_step._solve_support(SUPPORT05, inputs, standard, deadline)
    solved07, captured07 = k50._capture_support(inputs, standard, deadline)
    refined, refinement = k52._equilibrated_correction(
        captured07["driver_matrix"],
        captured07["driver_constant"],
        captured07["solution"],
    )
    refined_state = k52._vector_state(refined)
    refined_driver = k52._float_rows(
        captured07["driver_matrix"],
        captured07["driver_constant"],
        refined,
        captured07["driver_labels"],
        physics.DRIVER_TOL,
    )
    refined_holdout = k52._float_rows(
        captured07["holdout_matrix"],
        captured07["holdout_constant"],
        refined,
        captured07["holdout_labels"],
        physics.HOLDOUT_TOL,
    )
    solved = {"03": solved03, "05": solved05, "07": solved07}
    solved07["m3"]["fractional_state"] = refined_state
    regression = _regression(k48_payload, solved)
    common = {
        "F0": nid_step._common_bridge(
            solved05["fuel"]["state"], solved07["fuel"]["state"]
        ),
        "M3": nid_step._common_bridge(
            solved05["m3"]["fractional_state"], refined_state
        ),
    }
    common_pass = all(bool(row["pass"]) for row in common.values())
    tails = {
        "F0": nid_step._pure_tail(
            solved07["fuel"]["state"], tuple(sorted(solved07["fuel"]["state"]))
        ),
        "M3": nid_step._pure_tail(
            refined_state, tuple(physics.contract.AUTHORITATIVE_STATE)
        ),
    }
    tail_pass = all(bool(row["pass"]) for row in tails.values())
    s_c0 = nid_step.step2.c1._s_c0_actual_coefficient_guard(
        {
            "m3_primary": {"fractional_state": solved05["m3"]["fractional_state"]},
            "m3_extended": {"fractional_state": refined_state},
        }
    )
    support07_checks = dict(solved07["checks"])
    support07_checks["M3_driver"] = refined_driver["pass"]
    support07_checks["M3_independent_00_0i_holdout"] = refined_holdout["pass"]
    support07_checks["all_coefficients_and_diagnostics_finite"] = bool(
        k52._all_finite(
            {
                "fuel": solved07["fuel"],
                "refined_state": refined_state,
                "driver": refined_driver,
                "holdout": refined_holdout,
            }
        )
    )
    support07_refined_pass = all(bool(value) for value in support07_checks.values())
    correction_parity = bool(
        refinement["correction_max_abs"]
        == k52_payload["V2_single_bounded_refinement"]["correction_max_abs"]
        and refinement["rank"]
        == k52_payload["V2_single_bounded_refinement"]["rank"]
    )
    core_checks = {
        "M1_depth7": m1meta["rank_count_anchor_pass"],
        "support_03_core": solved03["pass"],
        "support_05_core": solved05["pass"],
        "support_07_refined_core": support07_refined_pass,
        "KMPC052_correction_parity": correction_parity,
        "correction_cap": refinement["correction_max_abs"] <= k52.CORRECTION_ABS_MAX,
        "NID_combined_R_fs_compensation": nid_step.nid1._combined_rfs_guard(
            standard, inputs
        )["pass"],
        "conditional_S_C0_actual_05_07": s_c0["pass"],
        "finite": k52._all_finite(
            {
                "solved": solved,
                "common": common,
                "tails": tails,
                "refinement": refinement,
            }
        ),
    }
    core_pass = all(bool(value) for value in core_checks.values())
    reference_pass = bool(
        regression["pass"]
        and k52_payload["V0_reference_parity"]["pass"]
        and k52_payload["V2_single_bounded_refinement"]["pass"]
        and k52_payload["V3_single_80dps_same_matrix_QR"]["pass"]
    )
    if not reference_pass:
        candidate = "REVIEW_NID_SUPPORT_CLOSURE_REFERENCE_UNCLOSED"
    elif not core_pass:
        candidate = "REVIEW_NID_SUPPORT_CLOSURE_CORE_UNCLOSED"
    elif not common_pass:
        candidate = "REVIEW_NID_SUPPORT_CLOSURE_COMMON_UNCLOSED"
    elif not tail_pass:
        candidate = "REVIEW_NID_SUPPORT_05_REMAINDER_UNCLOSED"
    else:
        candidate = "PASS_NID_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY"
    deadline()
    return {
        "test": "A2-K4 P5.3g7 KMPC-053 NID support-[0,5] closure",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "identity": {
            "mode": v1.MODE,
            "k_Mpc_inverse": v1.K_MPC,
            "variant": v1.VARIANT,
            "M1_depth": 7,
            "candidate_support": list(SUPPORT05),
            "audit_support": list(SUPPORT07),
        },
        "immutable_prerequisites": {
            "KMPC052": {"file": KMPC052[0], "sha256": k52_hash},
            "KMPC048": {"file": KMPC048[0], "sha256": k48_hash},
        },
        "scope": {
            "included": "NID regression [0,3]/[0,5], depth-7 candidate [0,5], refined audit [0,7], common 0..5, tail 6,7",
            "excluded": "[0,9], NIV, other k/variants, S-M, full hierarchy, ODE, P5.4, G8/G9",
        },
        "M1_depth7": m1meta,
        "regression": regression,
        "reference_pass": reference_pass,
        "refinement": refinement,
        "refined_driver": refined_driver,
        "refined_holdout": refined_holdout,
        "support07_refined_checks": support07_checks,
        "core_checks": core_checks,
        "core_pass": core_pass,
        "common": common,
        "common_pass": common_pass,
        "tails": tails,
        "tail_pass": tail_pass,
        "S_C0_guard": s_c0,
        "solved_supports": solved,
        "source_hashes": source_hashes(),
        "thresholds": {
            "common_relative": 1.0e-8,
            "tail_relative": physics.TAIL_TOL,
            "driver_relative": physics.DRIVER_TOL,
            "holdout_relative": physics.HOLDOUT_TOL,
            "absolute_fallback": physics.ABS_FALLBACK_TOL,
            "correction_absolute_max": k52.CORRECTION_ABS_MAX,
        },
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "zenodo_trigger": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
