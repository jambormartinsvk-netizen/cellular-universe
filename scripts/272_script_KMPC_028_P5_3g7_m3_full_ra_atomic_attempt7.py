"""Bounded atomic runner for preregistered KMPC-028 attempt 7."""

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
WRAPPER_PATH = (
    ROOT
    / "scripts"
    / "baseScripts"
    / "p5_general_synchronous"
    / "full_ra_m3_seed_attempt7_atomic.py"
)
EXPECTED_WRAPPER_HASH = "977082FF118645F8A7CD024EE6AE411D0F8995DA6F00552C0B53F19B520623F9"
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
    parser.add_argument("--aggregate", action="store_true")
    parser.add_argument("--mode", choices=("AD", "CDI", "BI", "NID", "NIV"))
    parser.add_argument("--k", type=float, choices=(0.005, 0.05, 0.15))
    parser.add_argument("--variant", choices=("nominal", "gamma0", "af0"))
    parser.add_argument("--output", type=Path)
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
    result_root = RESULT_DIR.resolve()
    if result_root not in path.parents:
        raise ValueError("output must stay inside scripts/results/k_mpc_005")
    if path.exists():
        raise FileExistsError(f"immutable result already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(
            _json_safe(payload),
            indent=2,
            sort_keys=True,
            allow_nan=False,
        )
        + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _validate_cli(args: argparse.Namespace) -> None:
    if args.max_runtime_seconds != 4.8:
        raise ValueError("preregistered internal runtime must equal 4.8 seconds")
    atom_fields = (args.mode, args.k, args.variant)
    if args.aggregate:
        if any(value is not None for value in atom_fields):
            raise ValueError("--aggregate cannot be combined with atom fields")
    elif any(value is None for value in atom_fields):
        raise ValueError("atom run requires --mode, --k, and --variant")


def main() -> int:
    args = parse_args()
    progress = {
        "last_completed_phase": "CLI_PARSED",
        "current_phase": "CLI_VALIDATION",
    }
    try:
        _validate_cli(args)
        progress["last_completed_phase"] = "CLI_VALIDATION"
        from scripts.baseScripts.p5_general_synchronous import (
            full_ra_m3_seed as physics,
        )
        from scripts.baseScripts.p5_general_synchronous import (
            full_ra_m3_seed_attempt7_atomic as atomic,
        )

        progress["current_phase"] = "SOURCE_HASH_VALIDATION"
        observed_source_hashes = physics.source_hashes()
        if observed_source_hashes != EXPECTED_SOURCE_HASHES:
            raise RuntimeError(
                "frozen source hash mismatch: "
                f"expected={EXPECTED_SOURCE_HASHES}, "
                f"observed={observed_source_hashes}"
            )
        observed_wrapper_hash = _hash(WRAPPER_PATH)
        if observed_wrapper_hash != EXPECTED_WRAPPER_HASH:
            raise RuntimeError(
                "atomic wrapper hash mismatch: "
                f"expected={EXPECTED_WRAPPER_HASH}, "
                f"observed={observed_wrapper_hash}"
            )
        progress["last_completed_phase"] = "SOURCE_HASH_VALIDATION"

        if args.aggregate:
            progress["current_phase"] = "ATOMIC_AGGREGATION"
            payload = atomic.aggregate_atoms(
                RESULT_DIR,
                EXPECTED_SOURCE_HASHES,
                EXPECTED_WRAPPER_HASH,
                observed_wrapper_hash,
                _hash,
                args.max_runtime_seconds,
            )
            output = args.output or (RESULT_DIR / atomic.AGGREGATE_NAME)
        else:
            payload = atomic.run_atom(
                args.mode,
                args.k,
                args.variant,
                args.max_runtime_seconds,
                progress,
            )
            output = args.output or (
                RESULT_DIR / atomic.atom_name(args.mode, args.k, args.variant)
            )
        progress["current_phase"] = "IMMUTABLE_WRITE"
        _write_new(output, payload)
        progress["last_completed_phase"] = "IMMUTABLE_WRITE"
        print(
            json.dumps(
                {"output": str(output), "verdict": payload["verdict"]},
                sort_keys=True,
            )
        )
        if args.aggregate:
            return (
                0
                if payload.get("execution_status")
                == "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_NUMERICAL_AUDIT"
                else 2
            )
        return 0 if str(payload["verdict"]).startswith("PASS_") else 2
    except Exception as error:
        mode = args.mode or "AGGREGATE"
        k_token = "NA" if args.k is None else str(args.k).replace(".", "p")
        variant = (args.variant or "NA").upper()
        label = f"{mode}_K{k_token}_{variant}"
        failure_path = (
            RESULT_DIR
            / f"RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_{label}_TECHNICAL_FAILURE.json"
        )
        failure = {
            "test": "KMPC-028 attempt-7 technical failure evidence",
            "run_id": "KMPC-028",
            "mode": args.mode,
            "k_Mpc_inverse": args.k,
            "variant": args.variant,
            "last_completed_phase": progress["last_completed_phase"],
            "current_phase": progress["current_phase"],
            "error_type": type(error).__name__,
            "error_message": str(error),
            "traceback": traceback.format_exc(limit=16),
            "physics_verdict": "NONE_TECHNICAL_FAILURE",
        }
        if not failure_path.exists():
            _write_new(failure_path, failure)
        print(
            json.dumps(
                _json_safe(failure),
                indent=2,
                sort_keys=True,
                allow_nan=False,
            )
        )
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
