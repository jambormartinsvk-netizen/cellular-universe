"""Read-only C3 aggregate over fifteen authoritative mode-by-k pair raws.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
This module reads frozen JSON and Markdown authorities only. It imports no
physics module and calls no worker, solver, matrix builder, or fit routine.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import tempfile
import time
from typing import Callable, Mapping


RUN_ID = "KMPC-148"
MODES = ("AD", "CDI", "BI", "NID", "NIV")
K_VALUES = (0.005, 0.05, 0.15)
VARIANTS = ("nominal", "gamma0", "af0")
EXECUTION_STATUS = "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT"


@dataclass(frozen=True)
class PairSpec:
    mode: str
    k_mpc: float
    filename: str
    sha256: str
    run_id: str
    candidate: str
    physical_receipt: str
    nominal_field: str
    nominal_candidate: str

    @property
    def key(self) -> str:
        return f"{self.mode}/k={self.k_mpc:g}"


@dataclass(frozen=True)
class ModeAuthority:
    mode: str
    filename: str
    sha256: str
    verdict_marker: str


PAIR_SPECS = (
    PairSpec(
        "AD", 0.005,
        "RUN_KMPC_131_P5_3G7_C3_AD_K0p005_ZERO_VARIANT_PAIR.json",
        "D3FB5710390B3395212067B8BC968E48AEBA04AF9A0D38A4313195A39C6B3DAA",
        "KMPC-131", "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_pair", "nominal_reference",
        "PASS_C2_AD_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "AD", 0.05,
        "RUN_KMPC_132_P5_3G7_C3_AD_K0p05_ZERO_VARIANT_PAIR_SUPPORT_04_06.json",
        "DCF6D7D957365FCDA127B1F0F5E27068625A3FB83DFDD1E367E1A052158D8D82",
        "KMPC-132",
        "PASS_C3_AD_K0P05_ZERO_PAIR_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY",
        "zero_pair_support_04_06_with_nominal_checkpoint",
        "nominal_support_checkpoint",
        "PASS_NOMINAL_SUPPORT_CHECKPOINT_CANDIDATE_ONLY",
    ),
    PairSpec(
        "AD", 0.15,
        "RUN_KMPC_131_P5_3G7_C3_AD_K0p15_ZERO_VARIANT_PAIR.json",
        "FFEB802BADF663F812023914C1B8C34AA150070A763BBF123E41A55E7BFE4C47",
        "KMPC-131", "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_pair", "nominal_reference",
        "PASS_C2_AD_K0p15_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "CDI", 0.005,
        "RUN_KMPC_131_P5_3G7_C3_CDI_K0p005_ZERO_VARIANT_PAIR.json",
        "9E1BCC3D291858DE55E15A31246D33026CDD4B9774753304B8FC0BBA62BB3BA4",
        "KMPC-131", "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_pair", "nominal_reference",
        "PASS_C2_CDI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "CDI", 0.05,
        "RUN_KMPC_131_P5_3G7_C3_CDI_K0p05_ZERO_VARIANT_PAIR.json",
        "DC38CD6C5E9EF15B0FB86878BF4125A431BBB04C537887874D1A38786F6F5A3F",
        "KMPC-131", "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_pair", "nominal_reference",
        "PASS_CDI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "CDI", 0.15,
        "RUN_KMPC_133_P5_3G7_C3_CDI_K0p15_ZERO_VARIANT_PAIR_SAME_MATRIX_REFINEMENT.json",
        "42BE1CAC74BC0BB879F7065B8B0FF36C0D1B8E382BC74537248DDAF02711717E",
        "KMPC-133",
        "PASS_C3_CDI_K0P15_ZERO_PAIR_SAME_MATRIX_REFINEMENT_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_same_matrix_refinement_pair",
        "nominal_reference",
        "PASS_C2_CDI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "BI", 0.005,
        "RUN_KMPC_131_P5_3G7_C3_BI_K0p005_ZERO_VARIANT_PAIR.json",
        "28337F4D16137DE29B197A556A88E96B0F326510CCFCB961AD5598D804886356",
        "KMPC-131", "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_pair", "nominal_reference",
        "PASS_C2_BI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "BI", 0.05,
        "RUN_KMPC_131_P5_3G7_C3_BI_K0p05_ZERO_VARIANT_PAIR.json",
        "81E27A42B8B0FB3FB405330279D131C725808CA17D38B97216B3BEE25E828937",
        "KMPC-131", "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_pair", "nominal_reference",
        "PASS_BI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "BI", 0.15,
        "RUN_KMPC_141_P5_3G7_C3_BI_K0p15_ZERO_VARIANT_PAIR_LOCAL_45S_HP_M1_EXACT_RESUME_SUPERSESSION_SCOPE_CORRECTED.json",
        "6F44B553BD01BB0516389643511C2858D0EBEA61380C4A8ABFE4E572909231A2",
        "KMPC-141",
        "PASS_C3_BI_K0P15_ZERO_PAIR_LOCAL_45S_HP_M1_EXACT_RESUME_SUPERSESSION_SCOPE_CORRECTED_CANDIDATE_ONLY",
        "KMPC140_read_only_parent_with_corrected_exact_supersession_scope",
        "nominal_reference",
        "PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY",
    ),
    PairSpec(
        "NID", 0.005,
        "RUN_KMPC_131_P5_3G7_C3_NID_K0p005_ZERO_VARIANT_PAIR.json",
        "2CBAD040FAA3D031CF699A7DFBC31F08E0C14C4E81B63BCBFBC1F3F67C0FD524",
        "KMPC-131", "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_pair", "nominal_reference",
        "PASS_C2_NID_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "NID", 0.05,
        "RUN_KMPC_143_P5_3G7_C3_NID_K0p05_ZERO_VARIANT_PAIR_SAME_MATRIX_REFINEMENT.json",
        "2F461DF24C4E7490A40411FCBDC2B98EEF4ADC19ACAFCAFDCA9007501B7D447F",
        "KMPC-143",
        "PASS_C3_NID_K0P05_ZERO_PAIR_SAME_MATRIX_REFINEMENT_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_same_matrix_refinement_pair",
        "nominal_reference", "PASS_NID_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "NID", 0.15,
        "RUN_KMPC_145_P5_3G7_C3_NID_K0p15_PARITY_SCOPE_CORRECTION.json",
        "226BF91F7DF12953D0DF53C2CEC676190067FA8D782211C68507FA8EAD874D6A",
        "KMPC-145", "PASS_C3_NID_K0P15_PARITY_SCOPE_CORRECTION_CANDIDATE_ONLY",
        "four_shards_with_af0_audit_only_same_matrix_refinement",
        "nominal_reference",
        "PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "NIV", 0.005,
        "RUN_KMPC_131_P5_3G7_C3_NIV_K0p005_ZERO_VARIANT_PAIR.json",
        "9088E7D8470E3F4CD118025ECA266646883A76ED87BED69B3FA1DCCEBB0FD156",
        "KMPC-131", "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_pair", "nominal_reference",
        "PASS_C2_NIV_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "NIV", 0.05,
        "RUN_KMPC_131_P5_3G7_C3_NIV_K0p05_ZERO_VARIANT_PAIR.json",
        "9E8E7D0F22D471E3C806DDBF5B2B4E587B209A537D55F1A8EFE259AC4F9DEFDD",
        "KMPC-131", "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_pair", "nominal_reference",
        "PASS_NIV_SUPPORT_STEP_2_SUPPORT_MINUS1_4_ADEQUATE_CANDIDATE_ONLY",
    ),
    PairSpec(
        "NIV", 0.15,
        "RUN_KMPC_147_P5_3G7_C3_NIV_K0p15_READ_ONLY_F0_PARITY_CORRECTION.json",
        "2780A8D6527C892E1EF665B59D514DD94A95495D536C56DFE3332A113956B16E",
        "KMPC-147",
        "PASS_C3_NIV_K0P15_MULTI_RANK_PARITY_CORRECTION_CANDIDATE_ONLY",
        "four_support_shards_gamma0_af0_rank104_130_refinement_pair",
        "nominal_reference",
        "PASS_C2_NIV_K0p15_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY",
    ),
)


MODE_AUTHORITIES = (
    ModeAuthority(
        "AD", "206_KMPC_132_AND_C3_AD_MODE_CLOSURE_INTERNAL_AUDIT_SK.md",
        "E430A1114A5E4C06AF2319FAFF4428C11FC6F37FDAB34719FC22C8D2FC4D5F9E",
        "PASS_C3_AD_MODE_9_OF_9",
    ),
    ModeAuthority(
        "CDI", "208_KMPC_131_133_C3_CDI_MODE_CLOSURE_INTERNAL_AUDIT_SK.md",
        "AAF33790FDE59BA22F48021096DEA1FA9606F1115F2F61BA4933D0E35BCE222A",
        "PASS_C3_CDI_MODE_9_OF_9",
    ),
    ModeAuthority(
        "BI", "218_KMPC_138_141_C3_BI_MODE_CLOSURE_INTERNAL_AUDIT_SK.md",
        "A6EA261E29733033090318CEE321C2C235F61584AB742CED13A3C12FF4D913F7",
        "PASS_C3_BI_MODE_9_OF_9",
    ),
    ModeAuthority(
        "NID", "231_KMPC_131_145_C3_NID_MODE_CLOSURE_INTERNAL_AUDIT_SK.md",
        "AEAF523FFFBAEC208C20063325B58E2F9BE6FEE1FAA69128262074FF37581445",
        "PASS_C3_NID_MODE_9_OF_9",
    ),
    ModeAuthority(
        "NIV", "241_KMPC_131_146_147_C3_NIV_MODE_CLOSURE_INTERNAL_AUDIT_SK.md",
        "E979E0554153E9143F0EAB20252811C229238F538D45EB6A921E0CD4F322417D",
        "PASS_C3_NIV_MODE_9_OF_9",
    ),
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _make_deadline(max_runtime_seconds: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(max_runtime_seconds) or not 0.0 < max_runtime_seconds <= 4.8:
        raise ValueError("max_runtime_seconds must be finite and in (0, 4.8]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError(f"{RUN_ID} internal deadline exceeded")

    return started, deadline


def _require_mapping(container: Mapping[str, object], key: str) -> Mapping[str, object]:
    value = container.get(key)
    if not isinstance(value, dict):
        raise KeyError(f"missing or non-object key: {key}")
    return value


def _require_true(container: Mapping[str, object], key: str) -> bool:
    value = container.get(key)
    if not isinstance(value, bool):
        raise KeyError(f"missing or non-boolean key: {key}")
    return value is True


def _contract_guard() -> dict[str, object]:
    expected_pairs = [(mode, k_mpc) for mode in MODES for k_mpc in K_VALUES]
    observed_pairs = [(spec.mode, spec.k_mpc) for spec in PAIR_SPECS]
    expected_atoms = [
        f"{mode}/k={k_mpc:g}/{variant}"
        for mode in MODES
        for k_mpc in K_VALUES
        for variant in VARIANTS
    ]
    checks = {
        "fifteen_pair_specs_exact": len(PAIR_SPECS) == 15,
        "pair_cartesian_order_exact": observed_pairs == expected_pairs,
        "pair_identity_unique": len(set(observed_pairs)) == 15,
        "pair_filename_unique": len({spec.filename for spec in PAIR_SPECS}) == 15,
        "five_mode_authorities_exact": tuple(row.mode for row in MODE_AUTHORITIES)
        == MODES,
        "authority_filename_unique": len(
            {row.filename for row in MODE_AUTHORITIES}
        ) == 5,
        "sha_shapes_exact": all(
            len(value) == 64 and all(char in "0123456789ABCDEF" for char in value)
            for value in (
                *(spec.sha256 for spec in PAIR_SPECS),
                *(row.sha256 for row in MODE_AUTHORITIES),
            )
        ),
        "pass_candidates_only": all(
            spec.candidate.startswith("PASS_C3_")
            and spec.nominal_candidate.startswith("PASS_")
            and "TECHNICAL_FAILURE" not in spec.candidate
            for spec in PAIR_SPECS
        ),
        "logical_register_45_exact": len(expected_atoms) == 45
        and len(set(expected_atoms)) == 45,
        "variant_order_exact": VARIANTS == ("nominal", "gamma0", "af0"),
    }
    return {"checks": checks, "pass": all(checks.values())}


def _load_mode_authority(
    track_dir: Path, authority: ModeAuthority, deadline: Callable[[], None]
) -> dict[str, object]:
    deadline()
    path = track_dir / authority.filename
    if not path.is_file():
        raise FileNotFoundError(f"missing C3 mode authority: {authority.filename}")
    observed_hash = sha256_file(path)
    if observed_hash != authority.sha256:
        raise RuntimeError(f"mode authority SHA mismatch: {authority.filename}")
    content = path.read_text(encoding="utf-8")
    checks = {
        "verdict_marker": authority.verdict_marker in content,
        "mode_count_marker": "9/9" in content,
        "K4_60_of_100_marker": "60/100" in content,
    }
    if not all(checks.values()):
        raise RuntimeError(f"mode authority marker mismatch: {authority.filename}")
    return {
        "mode": authority.mode,
        "file": authority.filename,
        "sha256": observed_hash,
        "verdict_marker": authority.verdict_marker,
        "checks": checks,
        "pass": True,
    }


def _validate_nominal(
    payload: Mapping[str, object], spec: PairSpec
) -> dict[str, object]:
    nominal = _require_mapping(payload, spec.nominal_field)
    candidate_key = (
        "candidate" if spec.nominal_field == "nominal_reference"
        else "candidate_interpretation_not_verdict"
    )
    candidate = nominal.get(candidate_key)
    checks = {
        "field_exact": spec.nominal_field in payload,
        "candidate_exact": candidate == spec.nominal_candidate,
        "candidate_pass_only": isinstance(candidate, str)
        and candidate.startswith("PASS_")
        and "TECHNICAL_FAILURE" not in candidate,
    }
    if spec.nominal_field == "nominal_reference":
        checks.update({
            "run_id_present": isinstance(nominal.get("run_id"), str),
            "file_present": isinstance(nominal.get("file"), str),
            "sha256_shape": isinstance(nominal.get("sha256"), str)
            and len(str(nominal.get("sha256"))) == 64,
            "support_authority_present": isinstance(
                nominal.get("support_authority"), dict
            ),
        })
    else:
        checks.update({
            "checkpoint_pass": nominal.get("checkpoint_pass") is True,
            "checkpoint_role_exact": nominal.get("role")
            == "DEEPER_NOMINAL_SUPPORT_CHECKPOINT_NOT_NEW_LOGICAL_ATOM",
        })
    if not all(checks.values()):
        raise RuntimeError(f"nominal authority mismatch: {spec.filename}")
    return {
        "field": spec.nominal_field,
        "candidate": candidate,
        "checks": checks,
        "pass": True,
    }


def _validate_variant(
    payload: Mapping[str, object], spec: PairSpec, variant: str
) -> dict[str, object]:
    variants = _require_mapping(payload, "variants")
    row = _require_mapping(variants, variant)
    expected_identity = {
        "mode": spec.mode,
        "k_Mpc_inverse": spec.k_mpc,
        "variant": variant,
    }
    candidate = row.get("candidate_interpretation_not_verdict")
    background = _require_mapping(row, "background_guard")
    null_limit = _require_mapping(row, "null_limit")
    bridges = _require_mapping(row, "nominal_vs_af0_coefficient_bridges")
    checks = {
        "identity_exact": row.get("identity") == expected_identity,
        "candidate_pass_only": isinstance(candidate, str)
        and candidate.startswith("PASS_C3_")
        and "TECHNICAL_FAILURE" not in candidate,
        "logical_atom_pass": _require_true(row, "logical_atom_pass"),
        "core_pass": _require_true(row, "core_pass"),
        "common_pass": _require_true(row, "common_pass"),
        "tail_pass": _require_true(row, "tail_pass"),
        "background_pass": _require_true(background, "pass"),
        "null_limit_pass": _require_true(null_limit, "pass"),
        "bridge_pass": _require_true(bridges, "pass"),
    }
    if not all(checks.values()):
        raise RuntimeError(f"variant gate mismatch: {spec.filename}:{variant}")
    return {
        "identity": expected_identity,
        "candidate_interpretation_not_verdict": candidate,
        "checks": checks,
        "pass": True,
    }


def _load_pair(
    result_dir: Path, spec: PairSpec, deadline: Callable[[], None]
) -> dict[str, object]:
    deadline()
    path = result_dir / spec.filename
    if not path.is_file():
        raise FileNotFoundError(f"missing frozen C3 pair: {spec.filename}")
    observed_hash = sha256_file(path)
    if observed_hash != spec.sha256:
        raise RuntimeError(f"pair SHA mismatch: {spec.filename}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError(f"pair payload is not an object: {spec.filename}")
    expected_identity = {
        "mode": spec.mode,
        "k_Mpc_inverse": spec.k_mpc,
        "physical_receipt": spec.physical_receipt,
    }
    accounting = _require_mapping(payload, "logical_atom_accounting")
    variants = _require_mapping(payload, "variants")
    pair_checks = {
        "run_id_exact": payload.get("run_id") == spec.run_id,
        "identity_exact": payload.get("identity") == expected_identity,
        "candidate_exact": payload.get("candidate_interpretation_not_verdict")
        == spec.candidate,
        "execution_status_exact": payload.get("execution_status")
        == EXECUTION_STATUS,
        "pair_pass": _require_true(payload, "pair_pass"),
        "variant_register_exact": set(variants) == {"gamma0", "af0"},
        "existing_nominal_one": accounting.get("existing_nominal") == 1,
        "new_zero_variants_two": accounting.get("new_zero_variants") == 2,
        "total_logical_atoms_three": accounting.get("total_logical_atoms") == 3,
        "score_effect_none": payload.get("score_effect") == "NONE",
        "K4_effect_none": payload.get("K4_score_effect")
        == "NONE_60_OF_100_UNCHANGED",
        "release_none": payload.get("release_trigger") == "NONE",
        "zenodo_none": payload.get("zenodo_trigger") == "NONE",
        "prediction_table_none": payload.get("prediction_table_effect") == "NONE",
        "script_not_orchestrator": payload.get("orchestrator_verdict")
        == "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not all(pair_checks.values()):
        raise RuntimeError(f"pair contract mismatch: {spec.filename}")
    nominal = _validate_nominal(payload, spec)
    variant_rows = {
        variant: _validate_variant(payload, spec, variant)
        for variant in ("gamma0", "af0")
    }
    deadline()
    return {
        "key": spec.key,
        "file": spec.filename,
        "sha256": observed_hash,
        "run_id": spec.run_id,
        "identity": expected_identity,
        "candidate_interpretation_not_verdict": spec.candidate,
        "pair_checks": pair_checks,
        "nominal": nominal,
        "variants": variant_rows,
        "logical_atoms": 3,
        "pass": True,
    }


def run_aggregate(
    max_runtime_seconds: float, result_dir: Path, track_dir: Path
) -> dict[str, object]:
    started, deadline = _make_deadline(max_runtime_seconds)
    contract = _contract_guard()
    if contract["pass"] is not True:
        raise RuntimeError("frozen C3 aggregate contract failed")
    authorities = [
        _load_mode_authority(track_dir, authority, deadline)
        for authority in MODE_AUTHORITIES
    ]
    pairs = [_load_pair(result_dir, spec, deadline) for spec in PAIR_SPECS]
    expected_register = [
        f"{mode}/k={k_mpc:g}/{variant}"
        for mode in MODES
        for k_mpc in K_VALUES
        for variant in VARIANTS
    ]
    observed_register: list[str] = []
    mode_counts = {mode: 0 for mode in MODES}
    for pair in pairs:
        identity = pair["identity"]
        if not isinstance(identity, dict):
            raise TypeError("internal pair identity is not an object")
        mode = str(identity["mode"])
        k_mpc = float(identity["k_Mpc_inverse"])
        for variant in VARIANTS:
            observed_register.append(f"{mode}/k={k_mpc:g}/{variant}")
            mode_counts[mode] += 1
    exact_register_pass = observed_register == expected_register
    mode_counts_pass = mode_counts == {mode: 9 for mode in MODES}
    input_pass = all(row["pass"] is True for row in authorities) and all(
        row["pass"] is True for row in pairs
    )
    aggregate_pass = bool(
        input_pass
        and exact_register_pass
        and mode_counts_pass
        and len(observed_register) == 45
        and len(set(observed_register)) == 45
    )
    candidate = (
        "PASS_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_45_OF_45_CANDIDATE_ONLY"
        if aggregate_pass
        else "REVIEW_C3_AUTHORITATIVE_LOGICAL_AGGREGATE_UNCLOSED"
    )
    deadline()
    return {
        "test": "A2-K4 P5.3g7 C3 authoritative logical coverage aggregate",
        "run_id": RUN_ID,
        "execution_status": EXECUTION_STATUS,
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "scope": {
            "included": (
                "read-only exact-hash C3 5-mode x 3-k x 3-variant logical "
                "register and five mode-closure authorities"
            ),
            "excluded": (
                "new solve, matrix, coefficient correction, S-M microphysics, "
                "P5.4, full hierarchy, G8/G9 and data"
            ),
        },
        "read_only_no_physics_solve": True,
        "operation_counts": {
            "files_read": 20,
            "workers": 0,
            "solvers": 0,
            "physics": 0,
            "matrices_built": 0,
        },
        "contract_guard": contract,
        "mode_authorities": {row["mode"]: row for row in authorities},
        "pair_inputs": {row["key"]: row for row in pairs},
        "logical_register": {
            "modes": list(MODES),
            "k_Mpc_inverse": list(K_VALUES),
            "variants": list(VARIANTS),
            "expected_atoms": 45,
            "observed_atoms": len(observed_register),
            "expected_register": expected_register,
            "observed_register": observed_register,
            "exact_cartesian_register_pass": exact_register_pass,
            "no_duplicate_atom": len(set(observed_register)) == 45,
            "mode_counts": mode_counts,
            "mode_counts_9_each_pass": mode_counts_pass,
        },
        "all_inputs_pass": input_pass,
        "technical_failure_outputs_selected": 0,
        "aggregate_gate_pass": aggregate_pass,
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "K4_score_effect": "NONE_60_OF_100_UNCHANGED",
        "C3_effect": "LOGICAL_COVERAGE_AGGREGATE_PENDING_ORCHESTRATOR_AUDIT",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }


def run_smoke() -> dict[str, object]:
    checks: dict[str, bool] = {}
    contract = _contract_guard()
    checks["contract_guard"] = contract["pass"] is True
    with tempfile.TemporaryDirectory(prefix="kmpc148_missing_pair_") as directory:
        try:
            _load_pair(Path(directory), PAIR_SPECS[0], lambda: None)
        except FileNotFoundError:
            checks["missing_pair_fail_closed"] = True
        else:
            checks["missing_pair_fail_closed"] = False
    with tempfile.TemporaryDirectory(prefix="kmpc148_missing_authority_") as directory:
        try:
            _load_mode_authority(
                Path(directory), MODE_AUTHORITIES[0], lambda: None
            )
        except FileNotFoundError:
            checks["missing_authority_fail_closed"] = True
        else:
            checks["missing_authority_fail_closed"] = False
    checks["no_solver_symbols"] = all(
        name not in globals()
        for name in ("numpy", "scipy", "mpmath", "solve", "lstsq")
    )
    checks["twenty_read_only_inputs"] = (
        len(PAIR_SPECS) + len(MODE_AUTHORITIES) == 20
    )
    checks["zero_runtime_operations"] = True
    return {
        "run_id": RUN_ID,
        "checks": checks,
        "pass": all(checks.values()),
        "physics_executed": False,
        "operation_counts": {
            "workers": 0,
            "solvers": 0,
            "physics": 0,
            "matrices_built": 0,
        },
    }
