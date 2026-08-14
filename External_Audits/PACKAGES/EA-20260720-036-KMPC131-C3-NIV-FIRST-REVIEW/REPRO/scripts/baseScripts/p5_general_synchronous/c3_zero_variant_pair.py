"""KMPC-128 C3 gamma0/af0 pair receipts over frozen C1/C2 nominal atoms.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
The module preserves 45 logical atoms while writing 15 mode-by-k pair files.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import time
from typing import Callable, Mapping

from . import c2_fourier_coverage as c2
from . import full_ra_m3_seed as physics


RUN_ID = "KMPC-128"
MODES = ("AD", "CDI", "BI", "NID", "NIV")
K_VALUES = (0.005, 0.05, 0.15)
VARIANTS = ("gamma0", "af0")
C2_AGGREGATE_NAME = (
    "RUN_KMPC_127_P5_3G7_C2_FOURIER_COVERAGE_AUTHORITATIVE_AGGREGATE.json"
)
C2_AGGREGATE_SHA256 = (
    "CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F"
)
AD_SUPPORT_AUTHORITY_NAME = (
    "RUN_KMPC_031_P5_3G7_M3_FULL_RA_DEEP_TAIL_BRANCH_PROVENANCE.json"
)
AD_SUPPORT_AUTHORITY_SHA256 = (
    "C547F818E3918CD844CA06BEA32814279A9D4A20D662A9166114410645792FF6"
)


@dataclass(frozen=True)
class SupportSpec:
    accepted: tuple[int, int]
    audit: tuple[int, int]
    m1_depth: int


@dataclass(frozen=True)
class NominalSpec:
    mode: str
    k_mpc: float
    filename: str
    sha256: str
    run_id: str
    candidate: str | None
    schema: str
    accepted_key: str = ""
    audit_key: str = ""


SUPPORTS: dict[tuple[str, float], SupportSpec] = {
    ("AD", 0.005): SupportSpec((0, 6), (0, 8), 8),
    ("AD", 0.05): SupportSpec((0, 2), (0, 4), 5),
    ("AD", 0.15): SupportSpec((0, 4), (0, 6), 6),
    ("CDI", 0.005): SupportSpec((0, 7), (0, 9), 9),
    ("CDI", 0.05): SupportSpec((0, 5), (0, 7), 7),
    ("CDI", 0.15): SupportSpec((0, 5), (0, 7), 7),
    ("BI", 0.005): SupportSpec((0, 7), (0, 9), 9),
    ("BI", 0.05): SupportSpec((0, 5), (0, 7), 7),
    ("BI", 0.15): SupportSpec((0, 5), (0, 7), 7),
    ("NID", 0.005): SupportSpec((0, 7), (0, 9), 9),
    ("NID", 0.05): SupportSpec((0, 5), (0, 7), 7),
    ("NID", 0.15): SupportSpec((0, 5), (0, 7), 7),
    ("NIV", 0.005): SupportSpec((-1, 6), (-1, 8), 8),
    ("NIV", 0.05): SupportSpec((-1, 4), (-1, 6), 6),
    ("NIV", 0.15): SupportSpec((-1, 6), (-1, 8), 8),
}


NOMINAL_SPECS = (
    NominalSpec(
        "AD", 0.005,
        "RUN_KMPC_063_P5_3G7_C2_AD_K0p005_SUPPORT_06_08.json",
        "CB0CEA5DD92BF85F0F0066FAD8DE77D5F8247B02B864FACF92FA374E0FBC85BD",
        "KMPC-063", "PASS_C2_AD_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY",
        "accepted_audit",
    ),
    NominalSpec(
        "AD", 0.05,
        "RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_AD_K0p05_NOMINAL.json",
        "2294E8623675B49F2D5A814005306D4E98E3CBDF4A1A66BD3AE1A9C0331EFC83",
        "KMPC-028", None, "attempt7",
    ),
    NominalSpec(
        "AD", 0.15,
        "RUN_KMPC_066_P5_3G7_C2_AD_K0p15_SUPPORT_04_06.json",
        "81370874BCF25123565FBB117EDFEB4D51F12560CCC04BDC8CCDFC0DF8FDE816",
        "KMPC-066", "PASS_C2_AD_K0p15_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY",
        "accepted_audit",
    ),
    NominalSpec(
        "CDI", 0.005,
        "RUN_KMPC_073_P5_3G7_C2_CDI_K0p005_SUPPORT_07_09_PHASE_ORDER_SUCCESSOR.json",
        "B7B2B7231E20D90D7EA71F1934B795296B7B0C2772148988C0FCFB2CF96E8498",
        "KMPC-073", "PASS_C2_CDI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY",
        "accepted_audit",
    ),
    NominalSpec(
        "CDI", 0.05, "RUN_KMPC_040_P5_3G7_CDI_SUPPORT_STEP_3_05_07.json",
        "69C78F70ECD851D8B8A48E4E09445181C0D4559E9BD2E90A7BA19933351BD219",
        "KMPC-040", "PASS_CDI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
        "solved_supports", "05", "07",
    ),
    NominalSpec(
        "CDI", 0.15, "RUN_KMPC_075_P5_3G7_C2_CDI_K0p15_SAME_MATRIX_REFINEMENT.json",
        "19F5F0B38CFE62C6E2ECA277EE5F959D866967027C5AF721CF4B2E1A30B999B9",
        "KMPC-075", "PASS_C2_CDI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
        "accepted_audit",
    ),
    NominalSpec(
        "BI", 0.005,
        "RUN_KMPC_078_P5_3G7_C2_BI_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json",
        "F24894A043B531825DD36A424637D1E70244F89B66678AF945EA6C135918A359",
        "KMPC-078", "PASS_C2_BI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY",
        "accepted_audit",
    ),
    NominalSpec(
        "BI", 0.05, "RUN_KMPC_046_P5_3G7_BI_SUPPORT_STEP_3_OWNER_SUCCESSOR.json",
        "60EC5A801FDDBAFFBA6CE184EBB3BC154879928385E6E37FB118781118615FB1",
        "KMPC-046", "PASS_BI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
        "solved_supports", "05", "07",
    ),
    NominalSpec(
        "BI", 0.15,
        "RUN_KMPC_112_P5_3G7_C2_BI_K0p15_HP_M1_CHECKPOINT_EXACT_RESUME_JSON_PARITY_SUCCESSOR.json",
        "FAF52256489BA7C105F9125C1ED9A68358C0187E5F7B8B1164E1BA036A6507A1",
        "KMPC-112", "PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY",
        "accepted_from_audit",
    ),
    NominalSpec(
        "NID", 0.005,
        "RUN_KMPC_115_P5_3G7_C2_NID_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json",
        "7D7B9BC1F2874A20E0CB8116D657F7C0419D03B284D0161CFFDF89112B4E0851",
        "KMPC-115", "PASS_C2_NID_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY",
        "accepted_audit",
    ),
    NominalSpec(
        "NID", 0.05, "RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json",
        "625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD",
        "KMPC-053", "PASS_NID_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
        "solved_supports", "05", "07",
    ),
    NominalSpec(
        "NID", 0.15, "RUN_KMPC_117_P5_3G7_C2_NID_K0p15_SAME_MATRIX_REFINEMENT.json",
        "F9BE1AC95575B0A71E73596384360ADC382C651EE4C8BA067DD4313C4BE6C7C4",
        "KMPC-117", "PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY",
        "accepted_audit",
    ),
    NominalSpec(
        "NIV", 0.005,
        "RUN_KMPC_120_P5_3G7_C2_NIV_K0p005_SUPPORT_06_08_CHECKPOINT_RESUME.json",
        "D6350636F9BA27C541EF8CDC2585ED370E2F1E2EB35495E01198A8BAA47AB136",
        "KMPC-120", "PASS_C2_NIV_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY",
        "accepted_audit",
    ),
    NominalSpec(
        "NIV", 0.05,
        "RUN_KMPC_056_P5_3G7_NIV_SUPPORT_STEP_2_FINITE_OWNER_SUCCESSOR.json",
        "9AF6410513C2B0A6142DA9B08E8A1D115670C644171B102683568E64D645C332",
        "KMPC-056", "PASS_NIV_SUPPORT_STEP_2_SUPPORT_MINUS1_4_ADEQUATE_CANDIDATE_ONLY",
        "niv_depth6", "candidate_minus1_4", "audit_minus1_6",
    ),
    NominalSpec(
        "NIV", 0.15,
        "RUN_KMPC_126_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_MULTI_RANK_REFINEMENT.json",
        "1D46AFD1CDEB650A7787A5E6FE9E2304A5212FF1FE9AA47657BEAAAA557B8AA0",
        "KMPC-126", "PASS_C2_NIV_K0p15_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY",
        "accepted_audit",
    ),
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def k_token(k_mpc: float) -> str:
    tokens = {0.005: "0p005", 0.05: "0p05", 0.15: "0p15"}
    if k_mpc not in tokens:
        raise ValueError(f"unsupported C3 k={k_mpc}")
    return tokens[k_mpc]


def output_name(mode: str, k_mpc: float) -> str:
    if mode not in MODES:
        raise ValueError(f"unsupported C3 mode={mode}")
    return f"RUN_KMPC_128_P5_3G7_C3_{mode}_K{k_token(k_mpc)}_ZERO_VARIANT_PAIR.json"


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def _make_deadline(limit: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(limit) or not 0.0 < limit <= 4.8:
        raise ValueError("KMPC-128 runtime must be finite and in (0, 4.8]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-128 pair internal deadline exceeded")

    return started, deadline


def _nominal_spec(mode: str, k_mpc: float) -> NominalSpec:
    matches = [spec for spec in NOMINAL_SPECS if (spec.mode, spec.k_mpc) == (mode, k_mpc)]
    if len(matches) != 1:
        raise RuntimeError(f"nominal spec cardinality is {len(matches)} for {mode}/k={k_mpc}")
    return matches[0]


def _get(container: Mapping[str, object], *path: str) -> object:
    current: object = container
    for key in path:
        if not isinstance(current, dict) or key not in current:
            raise KeyError("missing JSON path: " + ".".join(path))
        current = current[key]
    return current


def _restore_state(value: object, label: str) -> dict[str, dict[int, float]]:
    if not isinstance(value, dict):
        raise TypeError(f"{label} is not a state object")
    restored: dict[str, dict[int, float]] = {}
    for state_name, series in value.items():
        if not isinstance(state_name, str) or not isinstance(series, dict):
            raise TypeError(f"{label} has invalid state entry")
        powers: dict[int, float] = {}
        for power, coefficient in series.items():
            try:
                integer_power = int(power)
            except (TypeError, ValueError) as exc:
                raise TypeError(f"{label} has non-integer power {power!r}") from exc
            if isinstance(coefficient, bool) or not isinstance(coefficient, (int, float)):
                raise TypeError(f"{label}.{state_name}.{power} is not numeric")
            number = float(coefficient)
            if not math.isfinite(number):
                raise FloatingPointError(f"{label}.{state_name}.{power} is non-finite")
            powers[integer_power] = number
        restored[state_name] = powers
    return restored


def _filter_support(
    state: Mapping[str, Mapping[int, float]], support: tuple[int, int]
) -> dict[str, dict[int, float]]:
    powers = range(support[0], support[1] + 1)
    return {name: {power: float(values[power]) for power in powers} for name, values in state.items()}


def _validate_state_pair(
    accepted: Mapping[str, Mapping[int, float]],
    audit: Mapping[str, Mapping[int, float]],
    support: SupportSpec,
    expected_state_count: int,
    label: str,
) -> None:
    accepted_powers = tuple(range(support.accepted[0], support.accepted[1] + 1))
    audit_powers = tuple(range(support.audit[0], support.audit[1] + 1))
    if set(accepted) != set(audit) or len(accepted) != expected_state_count:
        raise RuntimeError(f"{label} state register mismatch")
    if any(tuple(values) != accepted_powers for values in accepted.values()):
        raise RuntimeError(f"{label} accepted power register mismatch")
    if any(tuple(values) != audit_powers for values in audit.values()):
        raise RuntimeError(f"{label} audit power register mismatch")


def _extract_nominal_states(
    payload: Mapping[str, object], spec: NominalSpec, support: SupportSpec
) -> dict[str, dict[str, dict[str, dict[int, float]]]]:
    if spec.schema == "attempt7":
        accepted_f0 = _restore_state(_get(payload, "result", "fuel_primary", "state"), "nominal.accepted.F0")
        accepted_m3 = _restore_state(_get(payload, "result", "m3_primary", "fractional_state"), "nominal.accepted.M3")
        audit_f0 = _restore_state(_get(payload, "result", "fuel_extended", "state"), "nominal.audit.F0")
        audit_m3 = _restore_state(_get(payload, "result", "m3_extended", "fractional_state"), "nominal.audit.M3")
    elif spec.schema == "accepted_audit":
        accepted_f0 = _restore_state(_get(payload, "accepted_solve", "fuel", "state"), "nominal.accepted.F0")
        accepted_m3 = _restore_state(_get(payload, "accepted_solve", "m3", "fractional_state"), "nominal.accepted.M3")
        audit_f0 = _restore_state(_get(payload, "audit_solve", "fuel", "state"), "nominal.audit.F0")
        audit_m3 = _restore_state(_get(payload, "audit_solve", "m3", "fractional_state"), "nominal.audit.M3")
    elif spec.schema == "solved_supports":
        accepted_f0 = _restore_state(_get(payload, "solved_supports", spec.accepted_key, "fuel", "state"), "nominal.accepted.F0")
        accepted_m3 = _restore_state(_get(payload, "solved_supports", spec.accepted_key, "m3", "fractional_state"), "nominal.accepted.M3")
        audit_f0 = _restore_state(_get(payload, "solved_supports", spec.audit_key, "fuel", "state"), "nominal.audit.F0")
        audit_m3 = _restore_state(_get(payload, "solved_supports", spec.audit_key, "m3", "fractional_state"), "nominal.audit.M3")
    elif spec.schema == "niv_depth6":
        accepted_f0 = _restore_state(_get(payload, "depth6_solved_supports", spec.accepted_key, "fuel", "state"), "nominal.accepted.F0")
        accepted_m3 = _restore_state(_get(payload, "depth6_solved_supports", spec.accepted_key, "m3", "fractional_state"), "nominal.accepted.M3")
        audit_f0 = _restore_state(_get(payload, "depth6_solved_supports", spec.audit_key, "fuel", "state"), "nominal.audit.F0")
        audit_m3 = _restore_state(_get(payload, "depth6_solved_supports", spec.audit_key, "m3", "fractional_state"), "nominal.audit.M3")
    elif spec.schema == "accepted_from_audit":
        audit_f0 = _restore_state(_get(payload, "audit_solve", "fuel", "state"), "nominal.audit.F0")
        audit_m3 = _restore_state(_get(payload, "audit_solve", "m3", "fractional_state"), "nominal.audit.M3")
        accepted_f0 = _filter_support(audit_f0, support.accepted)
        accepted_m3 = _filter_support(audit_m3, support.accepted)
    else:
        raise RuntimeError(f"unsupported nominal schema {spec.schema}")
    _validate_state_pair(accepted_f0, audit_f0, support, 2, "F0")
    _validate_state_pair(accepted_m3, audit_m3, support, len(c2.ra_contract.AUTHORITATIVE_STATE), "M3")
    if set(accepted_m3) != set(c2.ra_contract.AUTHORITATIVE_STATE):
        raise RuntimeError("nominal M3 authoritative state register mismatch")
    return {
        "accepted": {"F0": accepted_f0, "M3": accepted_m3},
        "audit": {"F0": audit_f0, "M3": audit_m3},
    }


def _load_c2_aggregate(result_dir: Path) -> Mapping[str, object]:
    path = result_dir / C2_AGGREGATE_NAME
    if not path.is_file() or sha256_file(path) != C2_AGGREGATE_SHA256:
        raise RuntimeError("immutable KMPC-127 C2 aggregate missing or hash-mismatched")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError("KMPC-127 aggregate is not an object")
    if payload.get("aggregate_gate_pass") is not True or payload.get("candidate_interpretation_not_verdict") != "PASS_C2_FOURIER_COVERAGE_10_OF_10_CANDIDATE_ONLY":
        raise RuntimeError("KMPC-127 aggregate PASS authority mismatch")
    return payload


def _load_nominal_reference(
    result_dir: Path, mode: str, k_mpc: float
) -> dict[str, object]:
    support = SUPPORTS[(mode, k_mpc)]
    spec = _nominal_spec(mode, k_mpc)
    aggregate = _load_c2_aggregate(result_dir)
    path = result_dir / spec.filename
    if not path.is_file():
        raise FileNotFoundError(f"missing nominal reference: {spec.filename}")
    observed_hash = sha256_file(path)
    if observed_hash != spec.sha256:
        raise RuntimeError(f"nominal reference SHA mismatch: {spec.filename}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError("nominal reference is not an object")
    identity = payload.get("identity")
    if spec.schema == "attempt7":
        identity = {
            "mode": payload.get("mode"),
            "k_Mpc_inverse": payload.get("k_Mpc_inverse"),
            "variant": payload.get("variant"),
        }
    if identity != {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": "nominal"}:
        raise RuntimeError(f"nominal identity mismatch: {spec.filename}")
    if payload.get("run_id") != spec.run_id:
        raise RuntimeError(f"nominal run_id mismatch: {spec.filename}")
    if spec.candidate is not None and payload.get("candidate_interpretation_not_verdict") != spec.candidate:
        raise RuntimeError(f"nominal candidate mismatch: {spec.filename}")
    authority: dict[str, object]
    if k_mpc in (0.005, 0.15):
        atom = _get(aggregate, "atoms", f"{mode}/k={k_mpc}")
        if not isinstance(atom, dict) or atom.get("file") != spec.filename or atom.get("sha256") != spec.sha256 or atom.get("all_required_gates_pass") is not True:
            raise RuntimeError(f"KMPC-127 atom authority mismatch: {mode}/k={k_mpc}")
        authority = {"type": "KMPC-127_C2_AGGREGATE", "file": C2_AGGREGATE_NAME, "sha256": C2_AGGREGATE_SHA256}
    elif mode == "AD":
        support_path = result_dir / AD_SUPPORT_AUTHORITY_NAME
        if not support_path.is_file() or sha256_file(support_path) != AD_SUPPORT_AUTHORITY_SHA256:
            raise RuntimeError("KMPC-031 AD support authority missing or hash-mismatched")
        support_payload = json.loads(support_path.read_text(encoding="utf-8"))
        if support_payload.get("candidate_interpretation_not_verdict") != "CANDIDATE_SUPPORT_TRUNCATION_CLOSED_J4_SENTINEL_SCOPE":
            raise RuntimeError("KMPC-031 AD support authority candidate mismatch")
        authority = {"type": "KMPC-031_AD_SUPPORT_CLOSURE", "file": AD_SUPPORT_AUTHORITY_NAME, "sha256": AD_SUPPORT_AUTHORITY_SHA256}
    else:
        authority = {"type": "C1_DIRECT_SCOPED_PASS", "file": spec.filename, "sha256": spec.sha256, "candidate": spec.candidate}
    states = _extract_nominal_states(payload, spec, support)
    return {
        "file": spec.filename,
        "sha256": observed_hash,
        "run_id": spec.run_id,
        "candidate": spec.candidate,
        "schema": spec.schema,
        "support_authority": authority,
        "states": states,
    }


def contract_guard() -> dict[str, object]:
    identities = [(spec.mode, spec.k_mpc) for spec in NOMINAL_SPECS]
    expected = [(mode, k_mpc) for mode in MODES for k_mpc in K_VALUES]
    checks = {
        "fifteen_nominal_specs_exact": identities == expected and len(set(identities)) == 15,
        "fifteen_support_specs_exact": set(SUPPORTS) == set(expected),
        "audit_is_accepted_plus2": all(spec.audit == (spec.accepted[0], spec.accepted[1] + 2) for spec in SUPPORTS.values()),
        "M1_depth_covers_audit": all(spec.m1_depth >= spec.audit[1] for spec in SUPPORTS.values()),
        "variant_set_exact": VARIANTS == ("gamma0", "af0"),
        "surfaces_exact": tuple(physics.Z_SURFACES) == (1.0e-4, 1.0e-2),
        "background_surfaces_exact": tuple(physics.A_VALUES_BACKGROUND) == (1.0e-8, 3.0e-8),
        "thresholds_exact": bool(
            physics.DRIVER_TOL == 1.0e-10
            and physics.HOLDOUT_TOL == 1.0e-9
            and physics.LOW_COEFFICIENT_TOL == 1.0e-8
            and physics.TAIL_TOL == 1.0e-6
            and physics.ABS_FALLBACK_TOL == 1.0e-12
            and physics.BACKGROUND_K_TOL == 1.0e-12
        ),
    }
    return {"checks": checks, "pass": all(checks.values())}


def _null_limit(
    variant: str,
    inputs: object,
    k_mpc: float,
    audit_hi: int,
    standard: Mapping[str, Mapping[int, float]],
    accepted: Mapping[str, object],
    audit: Mapping[str, object],
) -> dict[str, object]:
    accepted_m3 = _get(accepted, "m3")
    if not isinstance(accepted_m3, dict):
        raise TypeError("accepted M3 solve is not an object")
    background = _get(accepted_m3, "background")
    if not isinstance(background, dict):
        raise TypeError("accepted M3 background is not an object")
    if variant == "gamma0":
        def maximum(name: str) -> float:
            series = background.get(name)
            if not isinstance(series, dict):
                raise KeyError(f"missing gamma0 background series {name}")
            return max((abs(float(value)) for value in series.values()), default=0.0)

        fuel = background.get("fuel")
        if not isinstance(fuel, dict):
            raise KeyError("missing gamma0 fuel background")
        fuel0 = float(fuel.get(0, 0.0))
        checks = {
            "ash_max_abs": maximum("ash"),
            "transfer_max_abs": maximum("transfer_gr"),
            "gamma_max_abs": maximum("gamma"),
            "fuel_background_unit_coefficient_difference": abs(fuel0 - 1.0),
        }
        checks["pass"] = all(value <= physics.ABS_FALLBACK_TOL for value in checks.values())
        return checks
    if variant != "af0":
        raise ValueError(variant)
    accepted_fuel = _get(accepted, "fuel", "state")
    accepted_fractional = _get(accepted, "m3", "fractional_state")
    if not isinstance(accepted_fuel, dict) or not isinstance(accepted_fractional, dict):
        raise TypeError("af0 accepted state schema mismatch")
    combined = {name: dict(values) for name, values in standard.items()}
    combined.update({name: dict(values) for name, values in accepted_fuel.items()})
    seed_differences: dict[str, float] = {}
    for z in physics.Z_SURFACES:
        m1_value = physics._physical_standard_state(combined, z)
        full_value = m1_value + physics._physical_fractional_state(
            accepted_fractional, inputs, k_mpc, z
        )
        seed_differences[str(z)] = float(max(abs(full_value - m1_value)))
    background_differences: dict[str, dict[str, float]] = {}
    for a in physics.A_VALUES_BACKGROUND:
        observed = physics._physical_background(inputs, k_mpc, a, audit_hi)
        expected_d = 1.0 + inputs.matter_ratio_a * a
        expected_h = inputs.h0_mpc * math.sqrt(inputs.omega_r0) * math.sqrt(expected_d) / a**2
        background_differences[str(a)] = {
            "D": abs(observed["D"] - expected_d),
            "H_Mpc_inverse": abs(observed["H_Mpc_inverse"] - expected_h),
            "rho_f_over_rho_r": abs(observed["rho_f_over_rho_r"]),
            "rho_ash_over_rho_r": abs(observed["rho_ash_over_rho_r"]),
        }
    max_seed = max(seed_differences.values())
    max_background = max(value for row in background_differences.values() for value in row.values())
    rows_unknowns = []
    for solve in (accepted, audit):
        for sector in ("fuel", "m3"):
            diagnostics = _get(solve, sector, "diagnostics")
            if not isinstance(diagnostics, dict):
                raise TypeError("af0 diagnostics schema mismatch")
            rows_unknowns.append((int(diagnostics["rows"]), int(diagnostics["unknowns"])))
    nontrivial = all(rows > 0 and unknowns > 0 for rows, unknowns in rows_unknowns)
    return {
        "full_seed_minus_M1_max_abs_by_z": seed_differences,
        "full_seed_minus_M1_max_abs": max_seed,
        "background_minus_M1_by_a": background_differences,
        "background_minus_M1_max_abs": max_background,
        "coefficient_solve_rows_unknowns": [list(pair) for pair in rows_unknowns],
        "coefficient_solve_nontrivial": nontrivial,
        "pass": bool(nontrivial and max_seed <= physics.ABS_FALLBACK_TOL and max_background <= physics.ABS_FALLBACK_TOL),
    }


def _nominal_af0_bridges(
    nominal_states: Mapping[str, object],
    accepted: Mapping[str, object],
    audit: Mapping[str, object],
    support: SupportSpec,
) -> dict[str, object]:
    rows: dict[str, object] = {}
    for level, solve, expected_support in (
        ("accepted", accepted, support.accepted),
        ("audit", audit, support.audit),
    ):
        nominal_level = nominal_states.get(level)
        if not isinstance(nominal_level, dict):
            raise TypeError(f"nominal {level} state missing")
        f0 = c2._common_bridge(
            nominal_level["F0"], _get(solve, "fuel", "state"), expected_support
        )
        m3 = c2._common_bridge(
            nominal_level["M3"], _get(solve, "m3", "fractional_state"), expected_support
        )
        rows[level] = {"F0": f0, "M3": m3, "pass": bool(f0["pass"] and m3["pass"])}
    return {"by_support": rows, "pass": all(row["pass"] for row in rows.values())}


def _variant_candidate(
    core_pass: bool,
    common_pass: bool,
    tail_pass: bool,
    background_pass: bool,
    null_pass: bool,
    bridge_pass: bool,
    variant: str,
) -> str:
    if not core_pass:
        return "REVIEW_C3_CORE_GATE_UNCLOSED"
    if not common_pass or (variant == "af0" and not bridge_pass):
        return "REVIEW_C3_COEFFICIENT_BRIDGE_UNCLOSED"
    if not tail_pass:
        return "REVIEW_C3_SUPPORT_EXTENSION_REQUIRED"
    if not background_pass:
        return "STOP_C3_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY"
    if not null_pass:
        return "REVIEW_C3_NULL_LIMIT_UNCLOSED"
    return f"PASS_C3_{variant.upper()}_ATOM_CANDIDATE_ONLY"


def _solve_variant(
    mode: str,
    k_mpc: float,
    variant: str,
    support: SupportSpec,
    standard: Mapping[str, Mapping[int, float]],
    m1: Mapping[str, object],
    nominal: Mapping[str, object],
    shared_checks: Mapping[str, bool],
    deadline: Callable[[], None],
) -> dict[str, object]:
    variant_started = time.monotonic()
    inputs = physics._variant_inputs(variant)
    rfs = c2._rfs_guard(mode, standard, inputs)
    accepted = c2._solve_support(mode, k_mpc, support.accepted, inputs, standard, deadline)
    audit = c2._solve_support(mode, k_mpc, support.audit, inputs, standard, deadline)
    common = {
        "F0": c2._common_bridge(accepted["fuel"]["state"], audit["fuel"]["state"], support.accepted),
        "M3": c2._common_bridge(accepted["m3"]["fractional_state"], audit["m3"]["fractional_state"], support.accepted),
    }
    tails = {
        "F0": c2._tail(audit["fuel"]["state"], tuple(sorted(audit["fuel"]["state"])), support.accepted, support.audit),
        "M3": c2._tail(audit["m3"]["fractional_state"], tuple(c2.ra_contract.AUTHORITATIVE_STATE), support.accepted, support.audit),
    }
    s_c0 = c2.support_tools.c1._s_c0_actual_coefficient_guard({
        "m3_primary": {"fractional_state": accepted["m3"]["fractional_state"]},
        "m3_extended": {"fractional_state": audit["m3"]["fractional_state"]},
    })
    background = c2._background_guard(inputs, k_mpc, support.audit[1])
    null_limit = _null_limit(variant, inputs, k_mpc, support.audit[1], standard, accepted, audit)
    bridges = {"applicable": variant == "af0", "pass": True}
    if variant == "af0":
        nominal_states = nominal.get("states")
        if not isinstance(nominal_states, dict):
            raise TypeError("nominal state bundle missing")
        bridges = {"applicable": True, **_nominal_af0_bridges(nominal_states, accepted, audit, support)}
    common_pass = all(row["pass"] for row in common.values())
    tail_pass = all(row["pass"] for row in tails.values())
    core_checks = {
        **shared_checks,
        "M1": bool(m1["pass"]),
        "combined_R_fs": bool(rfs["pass"]),
        "accepted_solve": bool(accepted["pass"]),
        "audit_solve": bool(audit["pass"]),
        "S_C0_actual": bool(s_c0["pass"]),
    }
    core_pass = all(core_checks.values())
    candidate = _variant_candidate(
        core_pass, common_pass, tail_pass, bool(background["pass"]),
        bool(null_limit["pass"]), bool(bridges["pass"]), variant,
    )
    deadline()
    return {
        "logical_atom_id": f"{mode}/k={k_mpc}/{variant}",
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": variant},
        "candidate_interpretation_not_verdict": candidate,
        "inputs": {"lam": inputs.lam, "af": inputs.af},
        "core_checks": core_checks,
        "core_pass": core_pass,
        "combined_R_fs_guard": rfs,
        "accepted_solve": accepted,
        "audit_solve": audit,
        "common": common,
        "common_pass": common_pass,
        "tails": tails,
        "tail_pass": tail_pass,
        "S_C0_actual_guard": s_c0,
        "background_guard": background,
        "null_limit": null_limit,
        "nominal_vs_af0_coefficient_bridges": bridges,
        "logical_atom_pass": candidate.startswith("PASS_C3_"),
        "runtime_seconds": time.monotonic() - variant_started,
    }


def run_pair(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
    progress: dict[str, str] | None = None,
) -> dict[str, object]:
    if (mode, k_mpc) not in SUPPORTS:
        raise ValueError("KMPC-128 pair identity outside frozen matrix")
    progress = progress if progress is not None else {}
    started, deadline = _make_deadline(max_runtime_seconds)
    progress["current_phase"] = "NOMINAL_REFERENCE"
    nominal = _load_nominal_reference(result_dir, mode, k_mpc)
    progress["last_completed_phase"] = "NOMINAL_REFERENCE"
    deadline()
    progress["current_phase"] = "FROZEN_SHARED_GUARDS"
    guard = contract_guard()
    frozen_contract = physics.validate_frozen_contract()
    independent_contract = c2.ra_contract.validate_contract(
        c2.collective_contract.EXPECTED_STATE,
        c2.collective_contract.EXPECTED_DRIVER,
        c2.collective_contract.EXPECTED_HOLDOUT,
    )
    frozen_b1 = physics.b1_guard.build_contract_guard(max_runtime_seconds=min(1.0, max_runtime_seconds))
    tca0 = physics.production_tca0_reduction_guard()
    shared_checks = {
        "C3_contract": bool(guard["pass"]),
        "nominal_reference": True,
        "frozen_contract": bool(frozen_contract["valid"]),
        "independent_contract": bool(independent_contract.valid),
        "B1_left_null_Bianchi": frozen_b1["execution_verdict"] == "PASS_R_A_B1_CONTRACT_GUARD_ONLY",
        "production_TCA0_bridge": bool(tca0["pass"]),
    }
    support = SUPPORTS[(mode, k_mpc)]
    standard, m1 = c2._standard_depth(
        mode, k_mpc, support.m1_depth, physics._variant_inputs("nominal"), deadline
    )
    progress["last_completed_phase"] = "FROZEN_SHARED_GUARDS_AND_M1"
    variants: dict[str, object] = {}
    for variant in VARIANTS:
        progress["current_phase"] = f"SOLVE_{variant.upper()}"
        variants[variant] = _solve_variant(
            mode, k_mpc, variant, support, standard, m1, nominal,
            shared_checks, deadline,
        )
        progress["last_completed_phase"] = f"SOLVE_{variant.upper()}"
    pair_pass = all(row["logical_atom_pass"] for row in variants.values())
    candidate = (
        "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY"
        if pair_pass else "REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED"
    )
    progress["current_phase"] = "COMPLETE"
    progress["last_completed_phase"] = "COMPLETE"
    payload = {
        "test": "A2-K4 P5.3g7 C3 gamma0/af0 pair receipt",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "physical_receipt": "gamma0_af0_pair"},
        "logical_atom_accounting": {"existing_nominal": 1, "new_zero_variants": 2, "total": 3},
        "scope": {
            "included": "one mode-k C3 pair with exact nominal prerequisite, gamma0 and af0",
            "excluded": "other mode-k pairs, S-M, finite opacity, full hierarchy, P5.4, G8/G9 and data",
        },
        "nominal_reference": {key: value for key, value in nominal.items() if key != "states"},
        "contract_guard": guard,
        "frozen_contract": frozen_contract,
        "independent_contract_valid": independent_contract.valid,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "support_depth_spec": {
            "accepted": list(support.accepted), "audit": list(support.audit), "M1_depth": support.m1_depth,
        },
        "M1": m1,
        "variants": variants,
        "pair_pass": pair_pass,
        "thresholds": {
            "driver": physics.DRIVER_TOL,
            "holdout": physics.HOLDOUT_TOL,
            "common": physics.LOW_COEFFICIENT_TOL,
            "tail": physics.TAIL_TOL,
            "absolute_fallback": physics.ABS_FALLBACK_TOL,
            "background_relative": physics.BACKGROUND_K_TOL,
        },
        "source_hashes": {
            "full_ra_m3_seed.py": sha256_file(Path(physics.__file__).resolve()),
            "c2_fourier_coverage.py": sha256_file(Path(c2.__file__).resolve()),
            "c3_zero_variant_pair.py": sha256_file(Path(__file__).resolve()),
        },
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "K4_score_effect": "NONE_60_OF_100_UNCHANGED",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not c2.finite_owner._all_finite(payload):
        raise FloatingPointError("non-finite value in KMPC-128 pair receipt")
    return payload


def run_smoke(mode: str, k_mpc: float, result_dir: Path) -> dict[str, object]:
    nominal = _load_nominal_reference(result_dir, mode, k_mpc)
    gamma0 = physics._variant_inputs("gamma0")
    af0 = physics._variant_inputs("af0")
    checks = {
        "contract_guard": bool(contract_guard()["pass"]),
        "nominal_reference_loaded": nominal["sha256"] == _nominal_spec(mode, k_mpc).sha256,
        "gamma0_exact": gamma0.lam == 0.0 and gamma0.af != 0.0,
        "af0_exact": af0.af == 0.0 and af0.lam != 0.0,
        "unique_pair_name": output_name(mode, k_mpc).endswith("_ZERO_VARIANT_PAIR.json"),
        "no_physics_solve": True,
    }
    return {"run_id": RUN_ID, "identity": {"mode": mode, "k_Mpc_inverse": k_mpc}, "checks": checks, "pass": all(checks.values()), "physics_executed": False}
