"""Serialization-aware validation successor for KMPC-089.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the decimal round-trip validation of KMPC-088 is changed.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_coefficient_attribution as v1


_V1_ATTRIBUTION = v1._coefficient_attribution
_V1_SOURCE_HASHES = v1.source_hashes
_V1_CONTRACT_GUARD = v1.contract_guard


def configure(**config: object) -> None:
    v1.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v1.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v1.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V1_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_bi_k0p15_coefficient_attribution_v2_serialization_bound.py"] = (
        v1.prior.prior.v2.hash_owner.sha256_file(
            here / "c2_bi_k0p15_coefficient_attribution_v2_serialization_bound.py"
        )
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V1_CONTRACT_GUARD()
    guard["checks"].update({
        "serialization_bound_dynamic": True,
        "serialization_bound_two_ulp": True,
        "physics_thresholds_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _serialized_two_ulp(text: str) -> tuple[mp.mpf, int, mp.mpf]:
    normalized = text.strip().lower()
    mantissa = normalized.split("e", 1)[0].lstrip("+-")
    digits = "".join(char for char in mantissa if char.isdigit()).lstrip("0")
    significant_digits = len(digits)
    value = abs(mp.mpf(normalized))
    if significant_digits == 0 or value == 0:
        raise ValueError("serialized nonzero decimal required")
    exponent = int(mp.floor(mp.log10(value)))
    one_ulp = mp.power(10, exponent - significant_digits + 1)
    return 2 * one_ulp, significant_digits, one_ulp


def _coefficient_attribution(
    k_mpc: float,
    inputs: object,
    standard: dict[str, dict[int, float]],
    solution: list[mp.mpf],
    support: tuple[int, int],
    stored_holdout: dict[str, object],
) -> dict[str, object]:
    result = _V1_ATTRIBUTION(
        k_mpc, inputs, standard, solution, support, stored_holdout
    )
    stored = stored_holdout["Einstein_0i_7"]
    residual_reference = str(stored["residual_decimal"])
    norm_reference = str(stored["affine_term_norm_decimal"])
    residual_tolerance, residual_digits, residual_ulp = _serialized_two_ulp(
        residual_reference
    )
    norm_tolerance, norm_digits, norm_ulp = _serialized_two_ulp(norm_reference)
    residual_error = mp.mpf(result["residual_reconstruction_error_decimal"])
    norm_error = mp.mpf(result["affine_norm_reconstruction_error_decimal"])
    checks = result["checks"]
    checks.pop("residual_reconstruction_le_1e70", None)
    checks.pop("affine_norm_reconstruction_le_1e70", None)
    checks.update({
        "residual_reconstruction_within_two_serialized_ulp": (
            residual_error <= residual_tolerance
        ),
        "affine_norm_reconstruction_within_two_serialized_ulp": (
            norm_error <= norm_tolerance
        ),
    })
    result["serialization_aware_validation"] = {
        "rule": "2*10^(floor(log10(abs(x)))-significant_digits+1)",
        "residual_reference_original": residual_reference,
        "residual_significant_digits": residual_digits,
        "residual_one_ulp_decimal": v1._decimal(residual_ulp),
        "residual_tolerance_decimal": v1._decimal(residual_tolerance),
        "residual_error_decimal": v1._decimal(residual_error),
        "norm_reference_original": norm_reference,
        "norm_significant_digits": norm_digits,
        "norm_one_ulp_decimal": v1._decimal(norm_ulp),
        "norm_tolerance_decimal": v1._decimal(norm_tolerance),
        "norm_error_decimal": v1._decimal(norm_error),
        "physics_thresholds_changed": False,
    }
    false_checks = sorted(name for name, passed in checks.items() if not passed)
    if false_checks:
        raise RuntimeError(
            "KMPC-089 attribution false_checks=" + ",".join(false_checks)
        )
    return result


@contextmanager
def _overlay() -> Iterator[None]:
    before = (v1._coefficient_attribution, v1.source_hashes, v1.contract_guard)
    try:
        v1._coefficient_attribution = _coefficient_attribution
        v1.source_hashes = source_hashes
        v1.contract_guard = contract_guard
        yield
    finally:
        v1._coefficient_attribution, v1.source_hashes, v1.contract_guard = before


def _owners_restored() -> bool:
    return bool(
        v1._coefficient_attribution is _V1_ATTRIBUTION
        and v1.source_hashes is _V1_SOURCE_HASHES
        and v1.contract_guard is _V1_CONTRACT_GUARD
    )


def _fixture() -> dict[str, bool]:
    with mp.workdps(v1.PRECISION_DPS):
        residual_bound, residual_digits, residual_ulp = _serialized_two_ulp(
            "-5.4970171428314830742597821434761704494880966333399e-17"
        )
        norm_bound, norm_digits, norm_ulp = _serialized_two_ulp(
            "0.000000018203510784855356980175752053710493850249660287834"
        )
    return {
        "residual_digits_50": residual_digits == 50,
        "norm_digits_50": norm_digits == 50,
        "residual_two_ulp": residual_bound == 2 * residual_ulp,
        "norm_two_ulp": norm_bound == 2 * norm_ulp,
        "different_magnitude_bounds": residual_bound < norm_bound,
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v1.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"].update({
            f"serialization_{key}": value for key, value in _fixture().items()
        })
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["serialization_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = v1.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("KMPC-089 serialization owners not restored")
    payload["coefficient_attribution_boundary"]["serialization_successor"] = {
        "version": "V2_SERIALIZATION_BOUND",
        "only_validation_changed": True,
        "physics_thresholds_changed": False,
        "owners_restored": True,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("coefficient attribution has no aggregate scope")
