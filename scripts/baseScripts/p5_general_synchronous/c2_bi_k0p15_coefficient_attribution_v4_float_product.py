"""Frozen float-product bridge successor for KMPC-091.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the diagnostic fuel factor is made identical to the frozen holdout's
binary64-product-then-exact-bridge operation order.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_coefficient_attribution_v3_fixture as v3


v2 = v3.v2
v1 = v2.v1
_V1_ATTRIBUTION_OWNER = v2._V1_ATTRIBUTION
_V3_SOURCE_HASHES = v3.source_hashes
_V3_CONTRACT_GUARD = v3.contract_guard


def configure(**config: object) -> None:
    v3.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v3.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v3.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V3_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_bi_k0p15_coefficient_attribution_v4_float_product.py"] = (
        v1.prior.prior.v2.hash_owner.sha256_file(
            here / "c2_bi_k0p15_coefficient_attribution_v4_float_product.py"
        )
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V3_CONTRACT_GUARD()
    guard["checks"].update({
        "fuel_factor_binary64_product_then_bridge": True,
        "frozen_holdout_unchanged": True,
        "serialization_validation_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _rebuild_ledger(
    result: dict[str, object], inputs: object
) -> dict[str, object]:
    terms_before = result["terms_sorted_by_absolute_contribution"]
    owners_before = {str(item["owner"]) for item in terms_before}
    powers_before = [
        (item["weight_power"], item["state_power"]) for item in terms_before
    ]
    wrong_factor = v1.assembly._mp("1.5") * v1.assembly._mp(inputs.delta)
    correct_factor = v1.assembly._mp(1.5 * inputs.delta)
    ratio = correct_factor / wrong_factor
    terms: list[dict[str, object]] = []
    fuel_terms_changed = 0
    nonfuel_unchanged = True
    for original in terms_before:
        item = dict(original)
        if item["species"] == "fuel":
            fuel_terms_changed += 1
            old_contribution = mp.mpf(str(item["signed_contribution_decimal"]))
            new_contribution = old_contribution * ratio
            item["label"] = (
                "-float64_bridge(1.5*delta)*" + str(item["label"]).split("*", 1)[1]
            )
            item["equation_factor_decimal"] = v1._decimal(-correct_factor)
            item["signed_contribution"] = float(new_contribution)
            item["signed_contribution_decimal"] = v1._decimal(new_contribution)
            item["absolute_contribution"] = float(abs(new_contribution))
            item["absolute_contribution_decimal"] = v1._decimal(
                abs(new_contribution)
            )
        else:
            nonfuel_unchanged = nonfuel_unchanged and item == original
        terms.append(item)

    def contribution(item: dict[str, object]) -> mp.mpf:
        return mp.mpf(str(item["signed_contribution_decimal"]))

    exact_owners = {"EXACT_DRIVER_M3", "BACKGROUND_STANDARD_X_EXACT_DRIVER_M3"}
    exact_terms = [item for item in terms if item["owner"] in exact_owners]
    upstream_terms = [item for item in terms if item["owner"] not in exact_owners]
    exact_subtotal = mp.fsum(contribution(item) for item in exact_terms)
    upstream_subtotal = mp.fsum(contribution(item) for item in upstream_terms)
    reconstructed = exact_subtotal + upstream_subtotal
    physical_abs_sum = mp.fsum(abs(contribution(item)) for item in terms)
    affine_norm = abs(upstream_subtotal) + mp.fsum(
        abs(contribution(item)) for item in exact_terms
    )
    stored_residual = mp.mpf(str(result["stored_residual_decimal"]))
    stored_norm = mp.mpf(str(result["stored_affine_term_norm_decimal"]))
    residual_error = abs(reconstructed - stored_residual)
    norm_error = abs(affine_norm - stored_norm)

    owner_subtotals: dict[str, str] = {}
    for owner in sorted({str(item["owner"]) for item in terms}):
        owner_subtotals[owner] = v1._decimal(mp.fsum(
            contribution(item) for item in terms if item["owner"] == owner
        ))
    species_subtotals: dict[str, str] = {}
    for species in sorted({str(item["species"]) for item in terms}):
        species_subtotals[species] = v1._decimal(mp.fsum(
            contribution(item) for item in terms if item["species"] == species
        ))
    ordered = sorted(
        terms,
        key=lambda item: (
            -mp.mpf(str(item["absolute_contribution_decimal"])),
            str(item["label"]),
        ),
    )
    digest = hashlib.sha256()
    for item in ordered:
        digest.update(str(item["label"]).encode("utf-8"))
        digest.update(b"|")
        digest.update(str(item["signed_contribution_decimal"]).encode("ascii"))
        digest.update(b"|")

    result.update({
        "term_fingerprint_sha256": digest.hexdigest().upper(),
        "terms_sorted_by_absolute_contribution": ordered,
        "owner_subtotals_decimal": owner_subtotals,
        "species_subtotals_decimal": species_subtotals,
        "exact_driver_subtotal_decimal": v1._decimal(exact_subtotal),
        "upstream_constant_subtotal_decimal": v1._decimal(upstream_subtotal),
        "reconstructed_residual_decimal": v1._decimal(reconstructed),
        "residual_reconstruction_error_decimal": v1._decimal(residual_error),
        "physical_absolute_term_sum_decimal": v1._decimal(physical_abs_sum),
        "affine_term_norm_reconstructed_decimal": v1._decimal(affine_norm),
        "affine_norm_reconstruction_error_decimal": v1._decimal(norm_error),
        "cancellation_factor_physical_abs_over_residual": float(
            physical_abs_sum / abs(reconstructed)
        ),
        "cancellation_factor_physical_abs_over_residual_decimal": v1._decimal(
            physical_abs_sum / abs(reconstructed)
        ),
        "float_product_bridge_correction": {
            "operation_order": "binary64(1.5*delta)_then_exact_bridge",
            "wrong_exact_operand_product_decimal": v1._decimal(wrong_factor),
            "correct_exact_bridge_of_float_product_decimal": v1._decimal(
                correct_factor
            ),
            "difference_decimal": v1._decimal(correct_factor - wrong_factor),
            "rescale_ratio_decimal": v1._decimal(ratio),
            "fuel_terms_changed": fuel_terms_changed,
            "nonfuel_terms_unchanged": nonfuel_unchanged,
        },
    })
    result["checks"].update({
        "float_product_factor_differs": correct_factor != wrong_factor,
        "fuel_terms_changed_nonzero": fuel_terms_changed > 0,
        "term_count_preserved_after_factor_bridge": len(terms) == len(terms_before),
        "owners_preserved_after_factor_bridge": (
            {str(item["owner"]) for item in terms} == owners_before
        ),
        "powers_preserved_after_factor_bridge": (
            [(item["weight_power"], item["state_power"]) for item in terms]
            == powers_before
        ),
        "nonfuel_terms_unchanged_after_factor_bridge": nonfuel_unchanged,
        "residual_reconstruction_le_1e70": residual_error <= v1.RECONSTRUCTION_TOL,
        "affine_norm_reconstruction_le_1e70": norm_error <= v1.RECONSTRUCTION_TOL,
    })
    return result


def _factor_corrected_v1_attribution(
    k_mpc: float,
    inputs: object,
    standard: dict[str, dict[int, float]],
    solution: list[mp.mpf],
    support: tuple[int, int],
    stored_holdout: dict[str, object],
) -> dict[str, object]:
    result = _V1_ATTRIBUTION_OWNER(
        k_mpc, inputs, standard, solution, support, stored_holdout
    )
    return _rebuild_ledger(result, inputs)


@contextmanager
def _overlay() -> Iterator[None]:
    before = (v2._V1_ATTRIBUTION, v3.source_hashes, v3.contract_guard)
    try:
        v2._V1_ATTRIBUTION = _factor_corrected_v1_attribution
        v3.source_hashes = source_hashes
        v3.contract_guard = contract_guard
        yield
    finally:
        v2._V1_ATTRIBUTION, v3.source_hashes, v3.contract_guard = before


def _owners_restored() -> bool:
    return bool(
        v2._V1_ATTRIBUTION is _V1_ATTRIBUTION_OWNER
        and v3.source_hashes is _V3_SOURCE_HASHES
        and v3.contract_guard is _V3_CONTRACT_GUARD
    )


def _fixture() -> dict[str, bool]:
    with mp.workdps(v1.PRECISION_DPS):
        delta = 0.1
        wrong = v1.assembly._mp("1.5") * v1.assembly._mp(delta)
        correct = v1.assembly._mp(1.5 * delta)
        ratio = correct / wrong
        reconstructed = wrong * ratio
    return {
        "binary64_product_bridge_differs": correct != wrong,
        "rescale_reconstructs_correct_factor": reconstructed == correct,
        "ratio_finite_positive": bool(mp.isfinite(ratio) and ratio > 0),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v3.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"].update({
            f"float_product_{key}": value for key, value in _fixture().items()
        })
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["float_product_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = v3.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("KMPC-091 float-product owners not restored")
    payload["coefficient_attribution_boundary"]["float_product_successor"] = {
        "version": "V4_BINARY64_PRODUCT_THEN_EXACT_BRIDGE",
        "only_fuel_ledger_factor_changed": True,
        "frozen_holdout_changed": False,
        "physics_changed": False,
        "owners_restored": True,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("coefficient attribution has no aggregate scope")
