"""CLI runner for the frozen v3.18 PT1 legacy H0/S8 sensitivity DEV source."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

BASE_DIRECTORY = Path(__file__).resolve().parent / "baseScripts"
if str(BASE_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(BASE_DIRECTORY))

from release_v318_h0_s8_legacy_sensitivity_dev import (  # noqa: E402
    GRID_CELL_FILENAMES,
    N8000_BISECTION_STAGE_FILENAMES,
    N8000_MODEL_STAGE_FILENAMES,
    aggregate_n8000_cell,
    execute_grid_cell_with_review,
    execute_n8000_bisection_stage_with_review,
    execute_n8000_reference_stage_with_review,
    publish_exclusive,
    synthetic_self_test,
)


RESULT_DIRECTORY = Path(__file__).resolve().parent / "results" / "release_v318_h0_s8"
GRID_CELL_TARGETS = {
    cell_id: RESULT_DIRECTORY / filename
    for cell_id, filename in GRID_CELL_FILENAMES.items()
}
DIRECT_GRID_CELL_TARGETS = {
    cell_id: target
    for cell_id, target in GRID_CELL_TARGETS.items()
    if not cell_id.endswith("-n8000")
}
N8000_REFERENCE_TARGET = RESULT_DIRECTORY / "RUN_V318_PT1_H0_S8_N8000_REFERENCE_STAGE.json"
N8000_MODEL_STAGE_TARGETS = {
    shard_id: RESULT_DIRECTORY / filename
    for shard_id, filename in N8000_MODEL_STAGE_FILENAMES.items()
}
N8000_BISECTION_STAGE_TARGETS = {
    key: RESULT_DIRECTORY / filename
    for key, filename in N8000_BISECTION_STAGE_FILENAMES.items()
}


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _load_bound_payload(path: Path, expected_sha256: str, label: str) -> tuple[dict, str]:
    if not path.is_file():
        raise FileNotFoundError(f"{label} input is absent: {path}")
    actual = _sha256_file(path)
    if actual != expected_sha256.upper():
        raise ValueError(f"{label} SHA256 mismatch: expected {expected_sha256}, got {actual}")
    with path.open("r", encoding="utf-8") as stream:
        payload = json.load(stream)
    if not isinstance(payload, dict):
        raise ValueError(f"{label} payload is not a JSON object")
    return payload, actual


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Bounded DEV/official runner for a legacy sampled H0/S8 sensitivity."
    )
    mode = result.add_mutually_exclusive_group(required=True)
    mode.add_argument("--self-test", action="store_true", help="run only offline synthetic DEV tests")
    mode.add_argument(
        "--official-cell",
        choices=tuple(DIRECT_GRID_CELL_TARGETS),
        help="run exactly one frozen Delta-N_eff/grid cell",
    )
    mode.add_argument(
        "--official-n8000-reference",
        action="store_true",
        help="run the frozen staged n8000 LCDM reference",
    )
    mode.add_argument(
        "--official-n8000-bisect-a", choices=tuple(N8000_MODEL_STAGE_TARGETS),
        help="run midpoint iterations 1..10 for one frozen n8000 model",
    )
    mode.add_argument(
        "--official-n8000-bisect-b", choices=tuple(N8000_MODEL_STAGE_TARGETS),
        help="continue midpoint iterations 11..20 for one frozen n8000 model",
    )
    mode.add_argument(
        "--official-n8000-bisect-c", choices=tuple(N8000_MODEL_STAGE_TARGETS),
        help="continue midpoint iterations 21..29 and finish one frozen n8000 model",
    )
    mode.add_argument(
        "--official-n8000-aggregate",
        choices=tuple(N8000_MODEL_STAGE_TARGETS),
        help="aggregate one frozen staged n8000 model into its V3 cell raw",
    )
    result.add_argument("--reference-sha256")
    result.add_argument("--model-sha256")
    result.add_argument("--predecessor-sha256")
    result.add_argument("--max-runtime-seconds", type=float, default=45.0)
    return result


def main() -> int:
    arguments = parser().parse_args()
    if arguments.self_test:
        payload = synthetic_self_test(min(arguments.max_runtime_seconds, 5.0))
        print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
        return 0 if payload["all_pass"] else 1
    if arguments.official_n8000_reference:
        target = N8000_REFERENCE_TARGET
        if target.exists():
            raise FileExistsError(f"official reference-stage target already exists: {target}")
        payload = execute_n8000_reference_stage_with_review(arguments.max_runtime_seconds)
        publish_exclusive(payload, target)
        print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
        return 0 if payload["execution_verdict"] == "PASS_N8000_REFERENCE_STAGE_INTRINSIC" else 2
    bisection_request = next(
        (
            (segment, shard_id)
            for segment, shard_id in (
                ("A", arguments.official_n8000_bisect_a),
                ("B", arguments.official_n8000_bisect_b),
                ("C", arguments.official_n8000_bisect_c),
            )
            if shard_id is not None
        ),
        None,
    )
    if bisection_request is not None:
        if not arguments.reference_sha256:
            parser().error("n8000 bisection stages require --reference-sha256")
        segment, shard_id = bisection_request
        reference_payload, reference_actual = _load_bound_payload(
            N8000_REFERENCE_TARGET, arguments.reference_sha256, "reference stage"
        )
        predecessor_payload = None
        predecessor_actual = None
        predecessor_expected = None
        if segment != "A":
            if not arguments.predecessor_sha256:
                parser().error(f"n8000 bisection segment {segment} requires --predecessor-sha256")
            predecessor_segment = "A" if segment == "B" else "B"
            predecessor_payload, predecessor_actual = _load_bound_payload(
                N8000_BISECTION_STAGE_TARGETS[(shard_id, predecessor_segment)],
                arguments.predecessor_sha256,
                f"bisection segment {predecessor_segment}",
            )
            predecessor_expected = arguments.predecessor_sha256
        target = (
            N8000_MODEL_STAGE_TARGETS[shard_id]
            if segment == "C"
            else N8000_BISECTION_STAGE_TARGETS[(shard_id, segment)]
        )
        if target.exists():
            raise FileExistsError(f"official bisection-stage target already exists: {target}")
        payload = execute_n8000_bisection_stage_with_review(
            shard_id=shard_id,
            segment=segment,
            reference_payload=reference_payload,
            reference_actual_sha256=reference_actual,
            reference_expected_sha256=arguments.reference_sha256,
            max_runtime_seconds=arguments.max_runtime_seconds,
            predecessor_payload=predecessor_payload,
            predecessor_actual_sha256=predecessor_actual,
            predecessor_expected_sha256=predecessor_expected,
        )
        publish_exclusive(payload, target)
        print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
        expected_verdict = (
            "PASS_N8000_MODEL_STAGE_INTRINSIC"
            if segment == "C"
            else "PASS_N8000_BISECTION_SEGMENT_INTRINSIC"
        )
        return 0 if payload["execution_verdict"] == expected_verdict else 2
    if arguments.official_n8000_aggregate:
        if not arguments.reference_sha256 or not arguments.model_sha256:
            parser().error(
                "--official-n8000-aggregate requires --reference-sha256 and --model-sha256"
            )
        shard_id = arguments.official_n8000_aggregate
        reference_payload, reference_actual = _load_bound_payload(
            N8000_REFERENCE_TARGET, arguments.reference_sha256, "reference stage"
        )
        model_payload, model_actual = _load_bound_payload(
            N8000_MODEL_STAGE_TARGETS[shard_id], arguments.model_sha256, "model stage"
        )
        target = GRID_CELL_TARGETS[f"{shard_id}-n8000"]
        if target.exists():
            raise FileExistsError(f"official aggregated grid-cell target already exists: {target}")
        payload = aggregate_n8000_cell(
            shard_id,
            reference_payload,
            reference_actual,
            arguments.reference_sha256,
            model_payload,
            model_actual,
            arguments.model_sha256,
            min(arguments.max_runtime_seconds, 5.0),
        )
        publish_exclusive(payload, target)
        print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
        return 0 if payload["execution_verdict"] == "PASS_GRID_CELL_INTRINSIC" else 2
    target = DIRECT_GRID_CELL_TARGETS[arguments.official_cell]
    if target.exists():
        raise FileExistsError(f"official grid-cell target already exists before computation: {target}")
    payload = execute_grid_cell_with_review(arguments.official_cell, arguments.max_runtime_seconds)
    publish_exclusive(payload, target)
    print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
    return 0 if payload["execution_verdict"] == "PASS_GRID_CELL_INTRINSIC" else 2


if __name__ == "__main__":
    raise SystemExit(main())
