"""Bounded runner for preregistered KMPC-030 one-refinement audit."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import traceback


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
RESULT_DIR = ROOT / "scripts" / "results" / "k_mpc_005"
BASE_DIR = ROOT / "scripts" / "baseScripts" / "p5_general_synchronous"
WRAPPER_PATH = BASE_DIR / "full_ra_m3_seed_attempt9_refinement.py"
LADDER_PATH = BASE_DIR / "full_ra_m3_seed_attempt8_ladder.py"
EXPECTED_WRAPPER_HASH = "A8E2EA26B6960F23298259EFBECFFC9806ECF10F0207AE4D2B2AD0C2713DA0AB"
EXPECTED_LADDER_HASH = "934AE0E9663A6D8CFD92DE2843E59D7A94065D277227EECC73F9B6646B6EE475"
EXPECTED_SOURCE_HASHES = {
    "full_ra_contract.py": "F3839DA931D24939FA9C5925FD29B1484E722D1A0F24117DC91EBE5F4436D464",
    "full_ra_b1_preflight.py": "62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D",
    "full_ra_b1_preflight_v2.py": "27C0D6ADA828CA2F59C0D128EB6339074D5940F294272CDABE8127CB84867C7C",
    "mode_resolved_puiseux.py": "5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE",
    "mode_resolved_puiseux_v2_m1_anchored.py": "5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455",
    "full_ra_m3_seed.py": "070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-runtime-seconds", type=float, default=4.8)
    parser.add_argument("--audit", action="store_true")
    return parser.parse_args()


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _json_safe(value: object) -> object:
    if isinstance(value, float) and not math.isfinite(value):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    return value


def _write_new(path: Path, payload: dict[str, object]) -> None:
    path = path.resolve()
    if RESULT_DIR.resolve() not in path.parents:
        raise ValueError("output must stay inside scripts/results/k_mpc_005")
    if path.exists():
        raise FileExistsError(f"immutable result already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(_json_safe(payload), indent=2, sort_keys=True, allow_nan=False)
        + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def main() -> int:
    args = parse_args()
    progress = {
        "last_completed_phase": "CLI_PARSED",
        "current_phase": "CLI_VALIDATION",
    }
    try:
        if not args.audit:
            raise ValueError("preregistered run requires --audit")
        if args.max_runtime_seconds != 4.8:
            raise ValueError("preregistered internal runtime must equal 4.8 seconds")
        progress["last_completed_phase"] = "CLI_VALIDATION"
        from scripts.baseScripts.p5_general_synchronous import (
            full_ra_m3_seed as physics,
        )
        from scripts.baseScripts.p5_general_synchronous import (
            full_ra_m3_seed_attempt9_refinement as audit,
        )

        progress["current_phase"] = "SOURCE_HASH_VALIDATION"
        if physics.source_hashes() != EXPECTED_SOURCE_HASHES:
            raise RuntimeError("frozen physics source hash mismatch")
        observed_ladder_hash = _hash(LADDER_PATH)
        if observed_ladder_hash != EXPECTED_LADDER_HASH:
            raise RuntimeError("attempt-8 ladder wrapper hash mismatch")
        observed_wrapper_hash = _hash(WRAPPER_PATH)
        if observed_wrapper_hash != EXPECTED_WRAPPER_HASH:
            raise RuntimeError(
                "attempt-9 wrapper hash mismatch: "
                f"expected={EXPECTED_WRAPPER_HASH}, observed={observed_wrapper_hash}"
            )
        progress["last_completed_phase"] = "SOURCE_HASH_VALIDATION"
        payload = audit.run_audit(
            RESULT_DIR,
            EXPECTED_SOURCE_HASHES,
            EXPECTED_LADDER_HASH,
            observed_ladder_hash,
            EXPECTED_WRAPPER_HASH,
            observed_wrapper_hash,
            args.max_runtime_seconds,
            progress,
        )
        output = RESULT_DIR / audit.OUTPUT_NAME
        progress["current_phase"] = "IMMUTABLE_WRITE"
        _write_new(output, payload)
        progress["last_completed_phase"] = "IMMUTABLE_WRITE"
        print(
            json.dumps(
                {
                    "output": str(output),
                    "execution_status": payload["execution_status"],
                    "candidate": payload["candidate_interpretation_not_verdict"],
                },
                sort_keys=True,
            )
        )
        return (
            0
            if payload["execution_status"]
            == "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT"
            else 2
        )
    except Exception as error:
        failure_path = RESULT_DIR / (
            "RUN_KMPC_030_P5_3G7_M3_FULL_RA_J8_ONE_REFINEMENT_AUDIT_"
            "TECHNICAL_FAILURE.json"
        )
        failure = {
            "test": "KMPC-030 attempt-9 technical failure evidence",
            "run_id": "KMPC-030",
            "last_completed_phase": progress["last_completed_phase"],
            "current_phase": progress["current_phase"],
            "error_type": type(error).__name__,
            "error_message": str(error),
            "traceback": traceback.format_exc(limit=18),
            "physics_verdict": "NONE_TECHNICAL_FAILURE",
        }
        if not failure_path.exists():
            _write_new(failure_path, failure)
        print(json.dumps(_json_safe(failure), indent=2, sort_keys=True))
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
