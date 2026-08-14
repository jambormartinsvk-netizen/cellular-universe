"""Read-only Einstein_0i[7] coefficient attribution for KMPC-088.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
The frozen KMPC-087 system is rerun unchanged; this successor only exports a
complete convolution ledger for the independent holdout row.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_high_precision_driver_assembly as prior


assembly = prior.assembly
contract = prior.contract
PRECISION_DPS = prior.PRECISION_DPS
AUDIT_SUPPORT = prior.AUDIT_SUPPORT
TARGET_POWER = 7
EXPECTED_DRIVER_SHA256 = "CEBB46C42D2E7D57B23240490BCD48238D3471144531F71FD77DB9D65C743EF2"
EXPECTED_HOLDOUT_SHA256 = "2DE8C982469FE21931DC1E97E0C393AC04F136C7834EA121559CC6B4E906E2DE"
RECONSTRUCTION_TOL = mp.mpf("1e-70")

_PRIOR_SOURCE_HASHES = prior.source_hashes
_PRIOR_EXACT_BOUNDARY = prior._exact_driver_boundary
_ASSEMBLY_HOLDOUT = assembly._holdout_affine
_CAPTURE: dict[str, object] | None = None
_LEDGER: dict[str, object] | None = None


def configure(**config: object) -> None:
    prior.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return prior.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return prior.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_PRIOR_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_bi_k0p15_coefficient_attribution.py"] = (
        prior.prior.v2.hash_owner.sha256_file(
            here / "c2_bi_k0p15_coefficient_attribution.py"
        )
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = prior.contract_guard()
    guard["checks"].update({
        "attribution_target_exact": TARGET_POWER == 7,
        "attribution_support_exact": AUDIT_SUPPORT == (0, 7),
        "attribution_holdout_nonfit": not set(contract.AUTHORITATIVE_DRIVER)
        & set(contract.AUTHORITATIVE_HOLDOUT),
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _decimal(value: mp.mpf) -> str:
    return mp.nstr(value, 60)


def _term(
    *,
    label: str,
    owner: str,
    species: str,
    factor: mp.mpf,
    weight_power: int | None,
    weight_coefficient: mp.mpf | None,
    state_power: int,
    state_coefficient: mp.mpf,
    contribution: mp.mpf,
) -> dict[str, object]:
    return {
        "label": label,
        "owner": owner,
        "species": species,
        "equation_factor_decimal": _decimal(factor),
        "weight_power": weight_power,
        "weight_coefficient_decimal": (
            _decimal(weight_coefficient) if weight_coefficient is not None else None
        ),
        "state_power": state_power,
        "state_coefficient_decimal": _decimal(state_coefficient),
        "signed_contribution": float(contribution),
        "signed_contribution_decimal": _decimal(contribution),
        "absolute_contribution": float(abs(contribution)),
        "absolute_contribution_decimal": _decimal(abs(contribution)),
    }


def _coefficient_attribution(
    k_mpc: float,
    inputs: object,
    standard: dict[str, dict[int, float]],
    solution: list[mp.mpf],
    support: tuple[int, int],
    stored_holdout: dict[str, object],
) -> dict[str, object]:
    if support != AUDIT_SUPPORT or len(solution) != prior.EXPECTED_COLUMNS:
        raise ValueError("KMPC-088 attribution identity mismatch")
    lo, hi = support
    exponents = tuple(range(lo, hi + 1))
    series = assembly._MPSeries(min(-8, lo - 8), hi + 12)
    pair = assembly._MPPairSeries(series, inputs.p, lo - 8, hi + 8)
    bg = assembly._background(k_mpc, inputs, hi, series, pair)
    names = tuple(contract.AUTHORITATIVE_STATE)
    index = {
        (name, power): position
        for position, (name, power) in enumerate(
            item for name in names for item in ((name, e) for e in exponents)
        )
    }
    standard_mp = {name: assembly._mp_dict(standard[name]) for name in names}
    fractional = {
        name: {power: solution[index[(name, power)]] for power in exponents}
        for name in names
    }
    terms: list[dict[str, object]] = []

    eta_coefficient = fractional["eta"][TARGET_POWER]
    eta_factor = assembly._mp(inputs.p) + assembly._mp(TARGET_POWER)
    eta_contribution = eta_factor * eta_coefficient
    terms.append(_term(
        label="eta_x::eta_fractional[7]",
        owner="EXACT_DRIVER_M3",
        species="eta",
        factor=eta_factor,
        weight_power=None,
        weight_coefficient=None,
        state_power=TARGET_POWER,
        state_coefficient=eta_coefficient,
        contribution=eta_contribution,
    ))

    weights = (
        ("gamma", "Og", "U_gamma", assembly._mp(2), "M1"),
        ("fs", "Ofs", "U_fs", assembly._mp(2), "M1"),
        ("baryon", "Ob", "U_b", assembly._mp("1.5"), "M1"),
        ("cdm", "Oc", "U_c", assembly._mp("1.5"), "M1"),
        (
            "fuel", "Of", "U_f",
            assembly._mp("1.5") * assembly._mp(inputs.delta), "F0",
        ),
    )
    for species, weight_name, state_name, factor, standard_owner in weights:
        standard_weight, fractional_weight = bg[weight_name]
        for weight_power, weight_coefficient in standard_weight.items():
            state_power = TARGET_POWER - weight_power
            if state_power not in fractional[state_name]:
                continue
            state_coefficient = fractional[state_name][state_power]
            contribution = -factor * weight_coefficient * state_coefficient
            if contribution == 0:
                continue
            terms.append(_term(
                label=(
                    f"-{factor}*{weight_name}_standard[{weight_power}]"
                    f"*{state_name}_fractional[{state_power}]"
                ),
                owner="BACKGROUND_STANDARD_X_EXACT_DRIVER_M3",
                species=species,
                factor=-factor,
                weight_power=weight_power,
                weight_coefficient=weight_coefficient,
                state_power=state_power,
                state_coefficient=state_coefficient,
                contribution=contribution,
            ))
        for weight_power, weight_coefficient in fractional_weight.items():
            state_power = TARGET_POWER - weight_power
            state_coefficient = standard_mp[state_name].get(state_power)
            if state_coefficient is None:
                continue
            contribution = -factor * weight_coefficient * state_coefficient
            if contribution == 0:
                continue
            terms.append(_term(
                label=(
                    f"-{factor}*{weight_name}_fractional[{weight_power}]"
                    f"*{state_name}_standard[{state_power}]"
                ),
                owner=f"BACKGROUND_FRACTIONAL_X_{standard_owner}",
                species=species,
                factor=-factor,
                weight_power=weight_power,
                weight_coefficient=weight_coefficient,
                state_power=state_power,
                state_coefficient=state_coefficient,
                contribution=contribution,
            ))

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
    stored = stored_holdout["Einstein_0i_7"]
    stored_residual = mp.mpf(str(stored["residual_decimal"]))
    stored_norm = mp.mpf(str(stored["affine_term_norm_decimal"]))
    residual_error = abs(reconstructed - stored_residual)
    norm_error = abs(affine_norm - stored_norm)

    owner_subtotals: dict[str, str] = {}
    for owner in sorted({str(item["owner"]) for item in terms}):
        owner_subtotals[owner] = _decimal(mp.fsum(
            contribution(item) for item in terms if item["owner"] == owner
        ))
    species_subtotals: dict[str, str] = {}
    for species in sorted({str(item["species"]) for item in terms}):
        species_subtotals[species] = _decimal(mp.fsum(
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

    return {
        "target": "Einstein_0i[7]",
        "equation": "eta_x - 2*Og*U_gamma - 2*Ofs*U_fs - 1.5*Ob*U_b - 1.5*Oc*U_c - 1.5*delta*Of*U_f",
        "precision_dps": PRECISION_DPS,
        "term_count": len(terms),
        "term_fingerprint_sha256": digest.hexdigest().upper(),
        "terms_sorted_by_absolute_contribution": ordered,
        "owner_subtotals_decimal": owner_subtotals,
        "species_subtotals_decimal": species_subtotals,
        "exact_driver_subtotal_decimal": _decimal(exact_subtotal),
        "upstream_constant_subtotal_decimal": _decimal(upstream_subtotal),
        "reconstructed_residual_decimal": _decimal(reconstructed),
        "stored_residual_decimal": _decimal(stored_residual),
        "residual_reconstruction_error_decimal": _decimal(residual_error),
        "physical_absolute_term_sum_decimal": _decimal(physical_abs_sum),
        "affine_term_norm_reconstructed_decimal": _decimal(affine_norm),
        "stored_affine_term_norm_decimal": _decimal(stored_norm),
        "affine_norm_reconstruction_error_decimal": _decimal(norm_error),
        "cancellation_factor_physical_abs_over_residual": float(
            physical_abs_sum / abs(reconstructed)
        ),
        "cancellation_factor_physical_abs_over_residual_decimal": _decimal(
            physical_abs_sum / abs(reconstructed)
        ),
        "checks": {
            "residual_reconstruction_le_1e70": residual_error <= RECONSTRUCTION_TOL,
            "affine_norm_reconstruction_le_1e70": norm_error <= RECONSTRUCTION_TOL,
            "every_term_has_power_sum_7": all(
                item["weight_power"] is None
                or int(item["weight_power"]) + int(item["state_power"])
                == TARGET_POWER
                for item in terms
            ),
            "owners_exact": set(owner_subtotals) == {
                "BACKGROUND_FRACTIONAL_X_F0",
                "BACKGROUND_FRACTIONAL_X_M1",
                "BACKGROUND_STANDARD_X_EXACT_DRIVER_M3",
                "EXACT_DRIVER_M3",
            },
            "species_exact": set(species_subtotals)
            == {"baryon", "cdm", "eta", "fs", "fuel", "gamma"},
        },
    }


def _capture_holdout(
    k_mpc: float,
    inputs: object,
    standard: dict[str, dict[int, float]],
    solution: list[mp.mpf],
    support: tuple[int, int],
) -> dict[str, object]:
    global _CAPTURE
    if _CAPTURE is not None:
        raise RuntimeError("more than one exact-driver holdout capture")
    _CAPTURE = {
        "k_mpc": k_mpc,
        "inputs": inputs,
        "standard": standard,
        "solution": list(solution),
        "support": support,
    }
    return _ASSEMBLY_HOLDOUT(k_mpc, inputs, standard, solution, support)


def _exact_driver_boundary(
    k_mpc: float,
    inputs: object,
    standard: dict[str, dict[int, float]],
    support: tuple[int, int],
) -> dict[str, object]:
    global _CAPTURE, _LEDGER
    before = assembly._holdout_affine
    _CAPTURE = None
    try:
        assembly._holdout_affine = _capture_holdout
        result = _PRIOR_EXACT_BOUNDARY(k_mpc, inputs, standard, support)
    finally:
        assembly._holdout_affine = before
    if _CAPTURE is None:
        raise RuntimeError("exact-driver solution capture unavailable")
    with mp.workdps(PRECISION_DPS):
        _LEDGER = _coefficient_attribution(
            _CAPTURE["k_mpc"],
            _CAPTURE["inputs"],
            _CAPTURE["standard"],
            _CAPTURE["solution"],
            _CAPTURE["support"],
            result["holdout"],
        )
    result["Einstein_0i_7_coefficient_attribution"] = _LEDGER
    return result


@contextmanager
def _overlay() -> Iterator[None]:
    global _CAPTURE, _LEDGER
    before = (prior._exact_driver_boundary, prior.source_hashes, prior.contract_guard)
    _CAPTURE = _LEDGER = None
    try:
        prior._exact_driver_boundary = _exact_driver_boundary
        prior.source_hashes = source_hashes
        prior.contract_guard = contract_guard
        yield
    finally:
        prior._exact_driver_boundary, prior.source_hashes, prior.contract_guard = before


def _owners_restored() -> bool:
    return bool(
        prior._exact_driver_boundary is _PRIOR_EXACT_BOUNDARY
        and prior.source_hashes is _PRIOR_SOURCE_HASHES
        and assembly._holdout_affine is _ASSEMBLY_HOLDOUT
    )


def _fixture() -> dict[str, bool]:
    terms = [
        {"owner": "EXACT", "value": mp.mpf("2")},
        {"owner": "UPSTREAM", "value": mp.mpf("-1.5")},
        {"owner": "UPSTREAM", "value": mp.mpf("-0.5")},
    ]
    exact = mp.fsum(item["value"] for item in terms if item["owner"] == "EXACT")
    upstream = mp.fsum(
        item["value"] for item in terms if item["owner"] == "UPSTREAM"
    )
    return {
        "signed_reconstruction": exact + upstream == 0,
        "affine_grouping": abs(upstream) + abs(exact) == 4,
        "holdout_nonfit": not set(contract.AUTHORITATIVE_DRIVER)
        & set(contract.AUTHORITATIVE_HOLDOUT),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = prior.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"].update({
            f"attribution_{key}": value for key, value in _fixture().items()
        })
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["attribution_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = prior.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored() or _LEDGER is None:
        raise RuntimeError("coefficient-attribution lifecycle incomplete")
    boundary = payload["high_precision_driver_assembly_boundary"]
    checks = dict(_LEDGER["checks"])
    checks.update({
        "driver_fingerprint_matches_KMPC087": (
            boundary["driver"]["matrix_constant_sha256"] == EXPECTED_DRIVER_SHA256
        ),
        "holdout_fingerprint_matches_KMPC087": (
            boundary["holdout"]["matrix_constant_sha256"] == EXPECTED_HOLDOUT_SHA256
        ),
        "two_high_precision_solves_exact": (
            boundary["total_high_precision_solve_count"] == 2
        ),
        "holdout_rows_added_zero": (
            boundary["holdout"]["rows_added_to_driver_solve"] == 0
        ),
        "owners_restored": _owners_restored(),
    })
    passed = all(checks.values())
    payload["coefficient_attribution_boundary"] = {
        "scope": "READ_ONLY_EINSTEIN_0i_7_TERM_LEDGER_ON_FROZEN_KMPC087_SYSTEM",
        "ledger": _LEDGER,
        "checks": checks,
        "pass": passed,
        "physics_verdict_role": "DIAGNOSTIC_ONLY",
    }
    if not passed:
        raise RuntimeError("KMPC-088 attribution reconstruction failed")
    payload["candidate_interpretation_not_verdict"] = (
        "REVIEW_C2_BI_K0p15_UPSTREAM_ATTRIBUTION_COMPLETE"
    )
    payload["score_effect"] = "NONE_DIAGNOSTIC_ONLY"
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("coefficient attribution has no aggregate scope")
