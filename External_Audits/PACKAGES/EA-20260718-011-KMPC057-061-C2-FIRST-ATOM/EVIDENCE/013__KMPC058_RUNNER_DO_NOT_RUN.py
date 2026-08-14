"""Runner for the KMPC-058 PF-077 C2 support-guard successor.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
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


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR / "baseScripts" / "p5_general_synchronous"
RESULT_DIR = SCRIPT_DIR / "results" / "k_mpc_005"
AGGREGATE_NAME = "RUN_KMPC_058_P5_3G7_C2_FOURIER_COVERAGE_AGGREGATE.json"
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
    "nid_c1_coverage.py": "EEEE74848B6F4413914F0CC60230CC824982C7E485A38C77C4495F807975A2CD",
    "niv_c1_coverage.py": "B222554E8F6E664DAC674E394FED02A02ECBEE432ADEDC9A9682DFA6BB746E9D",
    "cdi_support_ladder.py": "A8257E2195E2AB61B5C4195B80EA44EE7669B5A52F9C8440BA5F5244190E3068",
    "niv_support_step2.py": "2B41B11E2C27B1FB5462AF0629C0478BBFF6A1343C317D7F6E6C045C0260F680",
    "niv_support_step2_v2_finite_owner.py": "F920F51313B44450DABC5A526769C42CD9A3988CBEB011A7954A0F88A4A7006D",
    "c2_fourier_coverage.py": "757F97E14657CC7046177C2D33115CA87639B9C92E89BDABE2BFF3B4380DF3FC",
    "c2_fourier_coverage_v2_c1_closed_support.py": "B563B919436B129E9B3C52AC011DC3190C6BA4773BD2B8094C35671AEE1B8A15",
}
EXPECTED_PREREQUISITES = {
    "RUN_KMPC_031_P5_3G7_M3_FULL_RA_DEEP_TAIL_BRANCH_PROVENANCE.json": "C547F818E3918CD844CA06BEA32814279A9D4A20D662A9166114410645792FF6",
    "RUN_KMPC_040_P5_3G7_CDI_SUPPORT_STEP_3_05_07.json": "69C78F70ECD851D8B8A48E4E09445181C0D4559E9BD2E90A7BA19933351BD219",
    "RUN_KMPC_046_P5_3G7_BI_SUPPORT_STEP_3_OWNER_SUCCESSOR.json": "60EC5A801FDDBAFFBA6CE184EBB3BC154879928385E6E37FB118781118615FB1",
    "RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json": "625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD",
    "RUN_KMPC_056_P5_3G7_NIV_SUPPORT_STEP_2_FINITE_OWNER_SUCCESSOR.json": "9AF6410513C2B0A6142DA9B08E8A1D115670C644171B102683568E64D645C332",
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, np.ndarray):
        return _json_safe(value.tolist())
    if isinstance(value, np.generic):
        return _json_safe(value.item())
    if isinstance(value, float) and not math.isfinite(value):
        raise FloatingPointError("non-finite value cannot be serialized")
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    raise TypeError(f"unsupported JSON scalar: {type(value).__name__}")


def _write_exclusive(path: Path, payload: dict[str, Any]) -> None:
    temporary = path.parent / f".tmp-{path.name}"
    if not path.parent.is_dir():
        raise FileNotFoundError(path.parent)
    if path.exists() or temporary.exists():
        raise FileExistsError(f"immutable publish collision: {path}")
    try:
        encoded = json.dumps(_json_safe(payload), indent=2, sort_keys=True, allow_nan=False) + "\n"
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.link(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _preimport_guard(target: Path | None) -> dict[str, str]:
    if target is not None:
        failure = target.with_name(target.stem + "_TECHNICAL_FAILURE.json")
        temporary = target.parent / f".tmp-{target.name}"
        conflicts = [str(path) for path in (target, failure, temporary) if path.exists()]
        if conflicts:
            raise FileExistsError(f"immutable KMPC-058 output conflict: {conflicts}")
    actual = {name: _sha256(BASE_DIR / name) for name in EXPECTED_SOURCE_HASHES}
    if actual != EXPECTED_SOURCE_HASHES:
        different = sorted(name for name in EXPECTED_SOURCE_HASHES if actual.get(name) != EXPECTED_SOURCE_HASHES[name])
        raise RuntimeError(f"KMPC-058 exact source hash mismatch: {different}")
    for name, expected in EXPECTED_PREREQUISITES.items():
        if _sha256(RESULT_DIR / name) != expected:
            raise RuntimeError(f"KMPC-058 prerequisite hash mismatch: {name}")
    return actual


def _runner_fixtures() -> dict[str, bool]:
    fixture = RESULT_DIR / ".KMPC058_publish_collision_fixture.json"
    temporary = fixture.parent / f".tmp-{fixture.name}"
    if fixture.exists() or temporary.exists():
        raise FileExistsError("stale KMPC-058 publish fixture")
    collision_rejected = preserved = False
    try:
        fixture.write_text("sentinel\n", encoding="utf-8")
        try:
            _write_exclusive(fixture, {"unexpected": True})
        except FileExistsError:
            collision_rejected = True
        preserved = fixture.read_text(encoding="utf-8") == "sentinel\n"
    finally:
        if temporary.exists():
            temporary.unlink()
        if fixture.exists():
            fixture.unlink()
    return {"collision_rejected": collision_rejected, "target_preserved": preserved,
            "temporary_cleaned": not temporary.exists()}


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="KMPC-058 C2 Fourier PF-077 guard successor.")
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--smoke", action="store_true")
    action.add_argument("--atom", action="store_true")
    action.add_argument("--aggregate", action="store_true")
    parser.add_argument("--mode", choices=("AD", "CDI", "BI", "NID", "NIV"))
    parser.add_argument("--k-mpc", type=float)
    parser.add_argument("--output", type=Path)
    return parser


def main() -> int:
    args = _parser().parse_args()
    progress = {"phase": "argument_guard", "mode": args.mode, "k_mpc": args.k_mpc}
    target: Path | None = None
    try:
        if args.max_runtime_seconds != 4.8 or not math.isfinite(args.max_runtime_seconds):
            raise ValueError("KMPC-058 requires exactly 4.8 runtime seconds")
        if args.smoke and any(value is not None for value in (args.mode, args.k_mpc, args.output)):
            raise ValueError("smoke forbids mode/k/output")
        if args.atom and any(value is None for value in (args.mode, args.k_mpc, args.output)):
            raise ValueError("atom requires mode/k/output")
        if args.aggregate and (args.mode is not None or args.k_mpc is not None or args.output is None):
            raise ValueError("aggregate forbids mode/k and requires output")
        progress["phase"] = "guarded_import"
        from baseScripts.p5_general_synchronous import c2_fourier_coverage_v2_c1_closed_support as audit
        if args.atom:
            target = RESULT_DIR / audit.atom_output_name(args.mode, args.k_mpc)
        elif args.aggregate:
            target = RESULT_DIR / AGGREGATE_NAME
        if target is not None:
            requested = args.output if args.output.is_absolute() else SCRIPT_DIR.parent / args.output
            if requested.resolve() != target.resolve():
                raise ValueError("output path differs from canonical KMPC-058 target")
        progress["phase"] = "preimport_guard"
        preimport = _preimport_guard(target)
        if audit.source_hashes() != EXPECTED_SOURCE_HASHES:
            raise RuntimeError("KMPC-058 post-import source hash mismatch")
        if args.smoke:
            runner_checks = _runner_fixtures()
            payload = audit.run_smoke(args.max_runtime_seconds, RESULT_DIR)
            payload["runner_checks"] = runner_checks
            if not payload["passed"] or not all(runner_checks.values()):
                raise RuntimeError(f"KMPC-058 smoke failed: {payload}")
            print(json.dumps(_json_safe(payload), sort_keys=True), flush=True)
            return 0
        progress["phase"] = "audit"
        payload = (audit.run_atom(args.mode, args.k_mpc, args.max_runtime_seconds, RESULT_DIR)
                   if args.atom else audit.run_aggregate(args.max_runtime_seconds, RESULT_DIR))
        if payload["source_hashes"] != preimport:
            raise RuntimeError("KMPC-058 payload source hash mismatch")
        progress["phase"] = "publish"
        _write_exclusive(target, payload)
        safe = _json_safe(payload)
        summary = {"run_id": safe["run_id"], "candidate": safe["candidate_interpretation_not_verdict"],
                   "output": str(target)}
        if args.atom:
            summary.update({"atom_id": safe["atom_id"], "M1_pass": safe["M1"]["pass"],
                            "core_pass": safe["core_pass"], "common_pass": safe["common_pass"],
                            "tail_pass": safe["tail_pass"], "background_pass": safe["background_guard"]["pass"]})
        else:
            summary.update({"observed_atoms": safe["matrix"]["observed_atoms"],
                            "all_atoms_pass": safe["all_atoms_pass"],
                            "background_spread_pass": safe["background_spread_pass"]})
        print(json.dumps(summary, sort_keys=True), flush=True)
        return 0
    except Exception as exc:
        failure = {"run_id": "KMPC-058", "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
                   "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
                   "phase": progress["phase"], "mode": args.mode, "k_Mpc_inverse": args.k_mpc,
                   "exception_type": type(exc).__name__, "message": str(exc),
                   "source_hashes_expected": EXPECTED_SOURCE_HASHES, "score_effect": "NONE",
                   "release_trigger": "NONE", "zenodo_trigger": "NONE", "prediction_table_effect": "NONE"}
        if target is not None:
            failure_path = target.with_name(target.stem + "_TECHNICAL_FAILURE.json")
            temporary = target.parent / f".tmp-{target.name}"
            if not any(path.exists() for path in (target, failure_path, temporary)):
                _write_exclusive(failure_path, failure)
        print(json.dumps(_json_safe(failure), sort_keys=True), file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
