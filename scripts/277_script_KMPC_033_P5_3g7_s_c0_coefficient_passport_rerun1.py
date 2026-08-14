"""Bounded PF-069-only rerun of the S-C0 coefficient passport."""

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
EXPECTED_BASE_HASHES = {
    "full_ra_contract.py": "F3839DA931D24939FA9C5925FD29B1484E722D1A0F24117DC91EBE5F4436D464",
    "full_ra_m3_seed.py": "070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2",
    "mode_resolved_puiseux.py": "5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE",
    "mode_resolved_puiseux_v2_m1_anchored.py": "5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455",
    "s1_collective_contract.py": "F535EE15137BBD6F9C0379821C9CC94DED8EC56037B6105B75BEF65A5884EE68",
    "s_c0_coefficient_passport.py": "C370B610815AFAC345C990E3CFE516D616873F39598F468A5ADBF2C65A2A6B95",
    "s_c0_coefficient_passport_v2_numpy_scalar.py": "06EE03C939FBCCFA6FA130421EEF98D0B8CC7571937EF02A7A46A57367534C11",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-runtime-seconds", type=float, default=4.8)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--smoke", action="store_true")
    group.add_argument("--audit", action="store_true")
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
    if path.parent != RESULT_DIR.resolve():
        raise ValueError("output must be directly inside canonical result directory")
    if path.exists():
        raise FileExistsError(f"immutable result already exists: {path}")
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(_json_safe(payload), indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _validate_hashes() -> dict[str, str]:
    observed = {name: _hash(BASE_DIR / name) for name in EXPECTED_BASE_HASHES}
    if observed != EXPECTED_BASE_HASHES:
        raise RuntimeError(f"frozen KMPC-033 base hash mismatch: {observed}")
    return observed


def main() -> int:
    args = parse_args()
    progress = {"last_completed_phase": "CLI_PARSED", "current_phase": "CLI_VALIDATION"}
    try:
        if args.max_runtime_seconds != 4.8:
            raise ValueError("preregistered internal runtime must equal 4.8 seconds")
        if args.smoke and args.output is not None:
            raise ValueError("smoke must not write a result JSON")
        if args.audit and args.output is None:
            raise ValueError("audit requires --output")
        progress["last_completed_phase"] = "CLI_VALIDATION"

        from scripts.baseScripts.p5_general_synchronous import (
            s_c0_coefficient_passport_v2_numpy_scalar as audit,
        )

        progress["current_phase"] = "SOURCE_HASH_VALIDATION"
        observed_hashes = _validate_hashes()
        progress["last_completed_phase"] = "SOURCE_HASH_VALIDATION"

        if args.smoke:
            progress["current_phase"] = "SMOKE"
            payload = audit.run_smoke(args.max_runtime_seconds)
            progress["last_completed_phase"] = "SMOKE"
            print(json.dumps({"run_id": audit.RUN_ID, "smoke_pass": payload["passed"]}, sort_keys=True))
            return 0 if payload["passed"] else 2

        expected_output = (RESULT_DIR / audit.OUTPUT_NAME).resolve()
        if args.output.resolve() != expected_output:
            raise ValueError(f"audit output must equal {expected_output}")
        progress["current_phase"] = "AUDIT"
        payload = audit.run_audit(args.max_runtime_seconds)
        payload["runner_frozen_base_hashes"] = observed_hashes
        progress["last_completed_phase"] = "AUDIT"
        progress["current_phase"] = "IMMUTABLE_WRITE"
        _write_new(expected_output, payload)
        progress["last_completed_phase"] = "IMMUTABLE_WRITE"
        print(json.dumps({
            "output": str(expected_output),
            "execution_status": payload["execution_status"],
            "candidate": payload["candidate_interpretation_not_verdict"],
            "all_checks_pass": payload["all_checks_pass"],
        }, sort_keys=True))
        return 0 if payload["all_checks_pass"] else 2
    except Exception as error:
        failure_path = RESULT_DIR / (
            "RUN_KMPC_033_P5_3G7_S_C0_COEFFICIENT_PASSPORT_RERUN1_"
            "TECHNICAL_FAILURE.json"
        )
        failure = {
            "test": "KMPC-033 S-C0 coefficient passport RERUN1 technical failure",
            "run_id": "KMPC-033",
            "last_completed_phase": progress["last_completed_phase"],
            "current_phase": progress["current_phase"],
            "error_type": type(error).__name__,
            "error_message": str(error),
            "traceback": traceback.format_exc(limit=18),
            "physics_verdict": "NONE_TECHNICAL_FAILURE",
            "correction_scope": "PF-069_NUMPY_REAL_TO_BUILTIN_FLOAT_ONLY",
        }
        if not failure_path.exists():
            _write_new(failure_path, failure)
        print(json.dumps(_json_safe(failure), indent=2, sort_keys=True))
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
