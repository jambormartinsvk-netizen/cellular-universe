#!/usr/bin/env python
"""Final bounded RERUN2: hard-anchor the accepted M1 standard seed."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from baseScripts.p5_general_synchronous.mode_resolved_puiseux_v2_m1_anchored import (
    FrozenInputs,
    run_m3_tca0_anchored,
    solve_hard_anchored_linear_system,
    solve_standard_seed_anchored,
    symbolic_identities,
)


ROOT = Path(__file__).resolve().parents[1]
RUNNER = Path(__file__).resolve()
BASE_DIR = Path(__file__).with_name("baseScripts") / "p5_general_synchronous"
BASE_V1 = BASE_DIR / "mode_resolved_puiseux.py"
BASE_V2 = BASE_DIR / "mode_resolved_puiseux_v2_m1_anchored.py"
PREREG = ROOT / "tracks" / "A1" / "A1K1" / "A2" / "A2K4" / "SUBTRACKS" / "P5" / "P5_3_SEEDS" / "29_P5_3G7_M3_TCA0_RERUN2_M1_ANCHOR_PREREGISTRATION_SK.md"
PREVIOUS_RUNNER = Path(__file__).with_name(
    "261_script_KMPC_023_P5_3g7_mode_resolved_full_seed_audit_rerun1.py"
)
PREVIOUS_REVIEW = ROOT / "Audit" / "A2_K4_P5_3G7_M3_TCA0_RERUN1_REVIEW_2026-07-16.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument(
        "--phase",
        choices=("m3-tca0", "full-finite-opacity"),
        default="m3-tca0",
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def to_builtin(value: object) -> object:
    if isinstance(value, dict):
        return {str(key): to_builtin(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_builtin(item) for item in value]
    if isinstance(value, np.generic):
        return value.item()
    return value


def write_once(path: Path, payload: dict[str, object]) -> None:
    encoded = json.dumps(to_builtin(payload), indent=2, sort_keys=True) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable output: {path}")
    path.write_text(encoded, encoding="utf-8")


def smoke_payload(started: float) -> dict[str, object]:
    exact = symbolic_identities(FrozenInputs())
    matrix = np.asarray([[1.0, 1.0], [2.0, 2.0]])
    constant = np.zeros(2)
    solution, reduced_rank, _ = solve_hard_anchored_linear_system(
        matrix, constant, anchor_index=0, anchor_value=3.0
    )
    _, _, real_metadata = solve_standard_seed_anchored(
        "AD", 0.05, FrozenInputs(), lambda: None
    )
    fixture = to_builtin(
        {"numpy_bool": np.bool_(True), "nested": [np.int64(2), np.float64(1.25)]}
    )
    json.dumps(fixture)
    checks = {
        **{f"exact_{key}": bool(value == 0) for key, value in exact.items()},
        "rank_deficient_fixture_reduced_full_rank": reduced_rank == 1,
        "rank_deficient_fixture_anchor_exact": solution[0] == 3.0,
        "rank_deficient_fixture_residual": float(np.max(np.abs(matrix @ solution + constant))) < 1.0e-14,
        "real_AD_reduced_rank_76_of_76": (
            real_metadata["rank"] == real_metadata["unknowns"] == 76
        ),
        "real_AD_M1_anchor_exact": real_metadata["hard_anchor_absolute_difference"] < 1.0e-14,
        "recursive_numpy_json_conversion": (
            isinstance(fixture["numpy_bool"], bool)
            and isinstance(fixture["nested"][0], int)
            and isinstance(fixture["nested"][1], float)
        ),
    }
    return {
        "test": "KMPC-024 RERUN2 hard-M1 smoke",
        "checks": checks,
        "verdict": "SMOKE_PASS" if all(checks.values()) else "SMOKE_STOP",
        "runtime_seconds": time.monotonic() - started,
    }


def main() -> int:
    args = parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0,5]")
    for required in (
        RUNNER,
        BASE_V1,
        BASE_V2,
        PREREG,
        PREVIOUS_RUNNER,
        PREVIOUS_REVIEW,
    ):
        if not required.is_file():
            raise FileNotFoundError(f"required source is missing: {required}")
    started = time.monotonic()
    if args.smoke:
        payload = smoke_payload(started)
        print(json.dumps(to_builtin(payload), indent=2, sort_keys=True))
        return 0 if payload["verdict"] == "SMOKE_PASS" else 1
    if args.output is None:
        raise ValueError("--output is required outside --smoke")
    if args.phase == "full-finite-opacity":
        payload = {
            "test": "KMPC-024 P5.3g7 full finite-opacity gate",
            "phase": "FULL-FINITE-OPACITY",
            "verdict": "REVIEW_BLOCKED_MISSING_DERIVED_NE0_SIGMA_T",
            "physical_calculation_executed": False,
            "reason": "finite-start opacity normalization remains underived",
            "runtime_limit_seconds": args.max_runtime_seconds,
            "runtime_seconds": time.monotonic() - started,
        }
        write_once(args.output, payload)
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 3

    payload = run_m3_tca0_anchored(args.max_runtime_seconds)
    payload["rerun_reason"] = (
        "PF-056/AR50 exact M1 column elimination; PF-057 run-label correction"
    )
    payload["source_sha256"] = {
        "runner": sha256(RUNNER),
        "base_v1_review_only": sha256(BASE_V1),
        "base_v2_m1_anchored": sha256(BASE_V2),
        "preregistration": sha256(PREREG),
        "previous_runner_review_only": sha256(PREVIOUS_RUNNER),
        "previous_result_review": sha256(PREVIOUS_REVIEW),
    }
    native = to_builtin(payload)
    write_once(args.output, native)
    failed = [name for name, passed in native["checks"].items() if not passed]
    print(
        json.dumps(
            {
                "test": native["test"],
                "verdict": native["verdict"],
                "P5_3g7_verdict": native["P5_3g7_verdict"],
                "failed_check_count": len(failed),
                "failed_checks": failed,
                "output": str(args.output),
                "runtime_seconds": native["runtime_seconds"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if native["verdict"] == "PASS_M3_TCA0_CONDITIONAL" else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)

