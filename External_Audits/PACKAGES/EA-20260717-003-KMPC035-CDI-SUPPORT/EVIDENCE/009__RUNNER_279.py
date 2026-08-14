"""Bounded KMPC-035 GLOBAL_C1 / CDI_SUPPORT_STEP_2 runner.

The historical filename token ``C2`` does not denote the global Fourier C2 gate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

BASE_DIR = ROOT / "scripts" / "baseScripts" / "p5_general_synchronous"
RESULT_DIR = ROOT / "scripts" / "results" / "k_mpc_005"
CANONICAL_OUTPUT = RESULT_DIR / "RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json"
FAILURE_OUTPUT = RESULT_DIR / "RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER_TECHNICAL_FAILURE.json"

EXPECTED_SOURCE_HASHES = {
    "full_ra_b1_preflight.py": "62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D",
    "full_ra_b1_preflight_v2.py": "27C0D6ADA828CA2F59C0D128EB6339074D5940F294272CDABE8127CB84867C7C",
    "full_ra_contract.py": "F3839DA931D24939FA9C5925FD29B1484E722D1A0F24117DC91EBE5F4436D464",
    "full_ra_m3_seed.py": "070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2",
    "mode_resolved_puiseux.py": "5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE",
    "mode_resolved_puiseux_v2_m1_anchored.py": "5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455",
    "s1_collective_contract.py": "F535EE15137BBD6F9C0379821C9CC94DED8EC56037B6105B75BEF65A5884EE68",
    "s_c0_coefficient_passport.py": "C370B610815AFAC345C990E3CFE516D616873F39598F468A5ADBF2C65A2A6B95",
    "s_c0_coefficient_passport_v2_numpy_scalar.py": "06EE03C939FBCCFA6FA130421EEF98D0B8CC7571937EF02A7A46A57367534C11",
    "cdi_c1_coverage.py": "D57CA8CA5571A07440A987F4FB0DDA08A40DAF7EA8C95AF929FC5C936F2FCE0F",
    "cdi_support_ladder.py": "A8257E2195E2AB61B5C4195B80EA44EE7669B5A52F9C8440BA5F5244190E3068",
}


def _json_safe(value: Any) -> Any:
    if isinstance(value, np.generic):
        return _json_safe(value.item())
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, float):
        if not math.isfinite(value):
            raise FloatingPointError("non-finite value rejected before JSON export")
        return value
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    raise TypeError(f"unsupported JSON value type: {type(value).__name__}")


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _independent_source_hashes() -> dict[str, str]:
    return {name: _sha256_file(BASE_DIR / name) for name in EXPECTED_SOURCE_HASHES}


def _write_atomic_exclusive(path: Path, payload: Any) -> None:
    if not path.parent.is_dir():
        raise FileNotFoundError(f"canonical result directory missing: {path.parent}")
    temporary = path.with_name(path.name + ".tmp-KMPC-035")
    with temporary.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(_json_safe(payload), handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.link(temporary, path)
    temporary.unlink()


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Bounded KMPC-035 GLOBAL_C1 / CDI_SUPPORT_STEP_2 [0,3] to [0,5] "
            "ladder (legacy filename token C2; NOT_GLOBAL_C2_FOURIER_GATE)."
        )
    )
    parser.add_argument("--max-runtime-seconds", type=float, default=4.8)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--smoke", action="store_true")
    mode.add_argument("--audit", action="store_true")
    parser.add_argument("--output", type=Path)
    return parser


def main() -> int:
    args = _parser().parse_args()
    progress = {"phase": "PREIMPORT_GUARDS"}
    try:
        if args.max_runtime_seconds != 4.8:
            raise ValueError("KMPC-035 requires exactly --max-runtime-seconds 4.8")
        if args.smoke and args.output is not None:
            raise ValueError("--output is forbidden in smoke mode")
        requested_output = CANONICAL_OUTPUT
        if args.output is not None:
            requested_output = args.output if args.output.is_absolute() else ROOT / args.output
        if requested_output.resolve() != CANONICAL_OUTPUT.resolve():
            raise ValueError("KMPC-035 output must equal the canonical immutable path")

        progress["phase"] = "INDEPENDENT_PREIMPORT_SOURCE_HASH_GUARD"
        preimport_hashes = _independent_source_hashes()
        if preimport_hashes != EXPECTED_SOURCE_HASHES:
            raise RuntimeError(
                "independent pre-import source hash mismatch: "
                f"different={sorted(name for name in EXPECTED_SOURCE_HASHES if preimport_hashes.get(name) != EXPECTED_SOURCE_HASHES[name])}"
            )

        progress["phase"] = "GUARDED_IMPORT"
        from scripts.baseScripts.p5_general_synchronous import cdi_support_ladder as audit

        progress["phase"] = "POSTIMPORT_SOURCE_HASH_GUARD"
        observed_hashes = audit.source_hashes()
        if observed_hashes != EXPECTED_SOURCE_HASHES:
            raise RuntimeError(
                "source hash set mismatch: "
                f"missing={sorted(set(EXPECTED_SOURCE_HASHES)-set(observed_hashes))}, "
                f"extra={sorted(set(observed_hashes)-set(EXPECTED_SOURCE_HASHES))}, "
                f"different={sorted(name for name in EXPECTED_SOURCE_HASHES if observed_hashes.get(name) != EXPECTED_SOURCE_HASHES[name])}"
            )
        if args.smoke:
            progress["phase"] = "SMOKE"
            payload = audit.run_smoke(args.max_runtime_seconds, RESULT_DIR)
            if not payload["passed"]:
                raise RuntimeError("KMPC-035 smoke checks failed")
            _json_safe(payload)
            nonfinite_rejected = False
            try:
                _json_safe(float("inf"))
            except FloatingPointError:
                nonfinite_rejected = True
            if not nonfinite_rejected:
                raise RuntimeError("runner JSON guard did not reject non-finite fixture")
            print(json.dumps({"run_id": audit.RUN_ID, "smoke_pass": True}, sort_keys=True), flush=True)
            return 0

        progress["phase"] = "AUDIT"
        payload = audit.run_audit(args.max_runtime_seconds, RESULT_DIR)
        if payload["source_hashes"] != EXPECTED_SOURCE_HASHES:
            raise RuntimeError("post-audit source hash mismatch")
        safe = _json_safe(payload)
        progress["phase"] = "IMMUTABLE_WRITE"
        _write_atomic_exclusive(CANONICAL_OUTPUT, safe)
        print(
            json.dumps(
                {
                    "candidate": safe["candidate_interpretation_not_verdict"],
                    "common_pass": safe["common_coefficient_pass"],
                    "core_pass": safe["core_pass"],
                    "execution_status": safe["execution_status"],
                    "output": str(CANONICAL_OUTPUT.resolve()),
                    "regression_pass": safe["regression_against_C1"]["pass"],
                    "tail_pass": safe["pure_tail_pass"],
                },
                sort_keys=True,
            ),
            flush=True,
        )
        return 0
    except Exception as exc:
        failure = {
            "run_id": "KMPC-035",
            "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
            "phase": progress["phase"],
            "exception_type": type(exc).__name__,
            "message": str(exc),
            "source_hashes_expected": EXPECTED_SOURCE_HASHES,
            "score_effect": "NONE",
            "release_trigger": "NONE",
            "zenodo_trigger": "NONE",
            "prediction_table_effect": "NONE",
        }
        try:
            _write_atomic_exclusive(FAILURE_OUTPUT, failure)
        except FileExistsError:
            failure["failure_write_status"] = "PRESERVED_EXISTING_FAILURE_FILE"
        print(json.dumps(_json_safe(failure), sort_keys=True), file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
