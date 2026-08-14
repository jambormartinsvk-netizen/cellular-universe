"""Attempt-6 full 13-state M3-TCA0 seed algebra.

This module implements only the preregistered conditional early-time seed
scope.  It deliberately imports the accepted M1 anchor helper but does not
call either legacy fractional solver.  Einstein 00 and 0i remain holdouts.
"""

from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import math
from pathlib import Path
import time
from typing import Callable, Iterable

import numpy as np

from . import full_ra_contract as contract
from . import full_ra_b1_preflight_v2 as b1_guard
from . import mode_resolved_puiseux as legacy
from . import mode_resolved_puiseux_v2_m1_anchored as m1_anchor


RUN_ID = "KMPC-027"
RCOND = 1.0e-12
PASS_SINGULAR_RATIO = 1.0e-10
DRIVER_TOL = 1.0e-10
HOLDOUT_TOL = 1.0e-9
ABS_FALLBACK_NORM = 1.0e-12
ABS_FALLBACK_TOL = 1.0e-12
LOW_COEFFICIENT_TOL = 1.0e-8
TAIL_TOL = 1.0e-6
BACKGROUND_K_TOL = 1.0e-12
BACKGROUND_MAX_J = 8
FORBIDDEN_TOL = 1.0e-10
LEADING_TOL = 1.0e-12
STEAM_SPLIT_TOL = 1.0e-14
Z_SURFACES = (1.0e-4, 1.0e-2)
Z_CAP = 5.0e-2
K_VALUES = (0.005, 0.05, 0.15)
A_VALUES_BACKGROUND = (1.0e-8, 3.0e-8)

MODE_SUPPORT = {
    "AD": (0, 2),
    "CDI": (0, 1),
    "BI": (0, 1),
    "NID": (0, 3),
    "NIV": (-1, 2),
}
EXPECTED_M1_ROWS = {"AD": 99, "CDI": 99, "BI": 99, "NID": 99, "NIV": 96}
EXPECTED_F0_PRIMARY = {"AD": 6, "CDI": 4, "BI": 4, "NID": 8, "NIV": 8}
EXPECTED_F0_EXTENDED = {"AD": 10, "CDI": 8, "BI": 8, "NID": 12, "NIV": 12}
EXPECTED_M3_PRIMARY = {"AD": 39, "CDI": 26, "BI": 26, "NID": 52, "NIV": 52}
EXPECTED_M3_EXTENDED = {"AD": 65, "CDI": 52, "BI": 52, "NID": 78, "NIV": 78}

STATE_TO_LEGACY = {
    "h": "h",
    "eta": "eta",
    "delta_gamma": "dg",
    "delta_fs": "dfs",
    "delta_b": "db",
    "delta_c": "dc",
    "U_gamma": "Ug",
    "U_fs": "Ufs",
    "sigma_fs": "sigfs",
    "U_b": "Ub",
    "U_c": "Uc",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    return {
        name: sha256_file(here / name)
        for name in (
            "full_ra_contract.py",
            "full_ra_b1_preflight.py",
            "full_ra_b1_preflight_v2.py",
            "mode_resolved_puiseux.py",
            "mode_resolved_puiseux_v2_m1_anchored.py",
            "full_ra_m3_seed.py",
        )
    }


def validate_frozen_contract() -> dict[str, object]:
    result = contract.validate_contract(
        contract.AUTHORITATIVE_STATE,
        contract.AUTHORITATIVE_DRIVER,
        contract.AUTHORITATIVE_HOLDOUT,
    )
    return {
        "valid": bool(result.valid),
        "errors": list(result.errors),
        "state": list(contract.AUTHORITATIVE_STATE),
        "driver": list(contract.AUTHORITATIVE_DRIVER),
        "holdout": list(contract.AUTHORITATIVE_HOLDOUT),
    }


def production_tca0_reduction_guard() -> dict[str, object]:
    """Exact bridge from separate photon/baryon Euler rows to production TCA0."""
    sp = legacy.sp
    ux, hc, velocity, delta_gamma, loading, thomson = sp.symbols(
        "U_x h_c U delta_gamma R T", finite=True
    )
    photon = ux - hc * velocity - delta_gamma / 4 + thomson
    baryon = ux - (hc - 1) * velocity - thomson / loading
    weighted_reference = (photon + loading * baryon) / (1 + loading)
    production = (
        ux
        - hc * velocity
        + loading * velocity / (1 + loading)
        - delta_gamma / (4 * (1 + loading))
    )
    reduction = sp.simplify(weighted_reference - production)
    thomson_cancellation = sp.simplify(thomson + loading * (-thomson / loading))
    return {
        "reference": "(photon Euler + R*baryon Euler)/(1+R), with U_b=U_gamma",
        "production": "U_x-h_c U+R/(1+R)U-delta_gamma/[4(1+R)]",
        "weighted_reduction_residual": str(reduction),
        "Thomson_momentum_cancellation_residual": str(thomson_cancellation),
        "pass": bool(reduction == 0 and thomson_cancellation == 0),
    }


def _series_ratio(singular: np.ndarray) -> float:
    if singular.size == 0 or singular[0] == 0.0:
        return 0.0
    return float(singular[-1] / singular[0])


def _affine_system(
    ledger: Callable[[np.ndarray], np.ndarray],
    count: int,
    deadline: Callable[[], None] | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    zero = np.zeros(count, dtype=float)
    constant = np.asarray(ledger(zero), dtype=float)
    matrix = np.empty((constant.size, count), dtype=float)
    for column in range(count):
        if deadline is not None:
            deadline()
        basis = np.zeros(count, dtype=float)
        basis[column] = 1.0
        matrix[:, column] = np.asarray(ledger(basis), dtype=float) - constant
    return matrix, constant


def _row_residual_metrics(
    matrix: np.ndarray,
    constant: np.ndarray,
    solution: np.ndarray,
    labels: list[str] | None = None,
) -> dict[str, object]:
    residual = matrix @ solution + constant
    term_norm = np.abs(constant) + np.sum(
        np.abs(matrix * solution[np.newaxis, :]), axis=1
    )
    relative_mask = term_norm > ABS_FALLBACK_NORM
    ratios = np.zeros_like(residual)
    ratios[relative_mask] = np.abs(residual[relative_mask]) / term_norm[relative_mask]
    relative_max = float(np.max(ratios[relative_mask])) if np.any(relative_mask) else 0.0
    absolute_max = (
        float(np.max(np.abs(residual[~relative_mask])))
        if np.any(~relative_mask)
        else 0.0
    )
    absolute_indices = np.flatnonzero(~relative_mask)
    relative_indices = np.flatnonzero(relative_mask)
    relative_worst = (
        int(relative_indices[np.argmax(ratios[relative_mask])])
        if relative_indices.size
        else None
    )
    absolute_worst = (
        int(absolute_indices[np.argmax(np.abs(residual[~relative_mask]))])
        if absolute_indices.size
        else None
    )
    return {
        "max_relative_residual": relative_max,
        "max_absolute_fallback_residual": absolute_max,
        "relative_row_count": int(np.sum(relative_mask)),
        "absolute_fallback_row_count": int(np.sum(~relative_mask)),
        "worst_relative_row": (
            labels[relative_worst] if labels is not None and relative_worst is not None else relative_worst
        ),
        "worst_absolute_fallback_row": (
            labels[absolute_worst] if labels is not None and absolute_worst is not None else absolute_worst
        ),
        "pass_driver": bool(
            relative_max <= DRIVER_TOL and absolute_max <= ABS_FALLBACK_TOL
        ),
    }


def _solve_equilibrated(
    matrix: np.ndarray,
    constant: np.ndarray,
    expected_rank: int,
    row_labels: list[str] | None = None,
    deadline: Callable[[], None] | None = None,
) -> tuple[np.ndarray, dict[str, object]]:
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[1] != expected_rank:
        raise ValueError(
            f"unexpected square-system shape {matrix.shape}; expected {expected_rank}"
        )
    raw_singular = np.linalg.svd(matrix, compute_uv=False)
    if deadline is not None:
        deadline()
    raw_rank = int(np.sum(raw_singular > RCOND * raw_singular[0])) if raw_singular.size else 0

    row_scale = np.maximum(
        np.maximum(np.max(np.abs(matrix), axis=1), np.abs(constant)), 1.0e-300
    )
    row_matrix = matrix / row_scale[:, np.newaxis]
    row_constant = constant / row_scale
    column_scale = np.maximum(np.max(np.abs(row_matrix), axis=0), 1.0e-300)
    equilibrated = row_matrix / column_scale[np.newaxis, :]
    singular = np.linalg.svd(equilibrated, compute_uv=False)
    cutoff = RCOND * singular[0] if singular.size else math.inf
    rank = int(np.sum(singular > cutoff)) if singular.size else 0
    y, _, _, _ = np.linalg.lstsq(equilibrated, -row_constant, rcond=RCOND)
    if deadline is not None:
        deadline()
    solution = y / column_scale
    metrics = _row_residual_metrics(matrix, constant, solution, row_labels)
    ratio = _series_ratio(singular)
    metrics.update(
        {
            "rows": int(matrix.shape[0]),
            "unknowns": int(matrix.shape[1]),
            "expected_rank": int(expected_rank),
            "raw_rank_rcond": raw_rank,
            "equilibrated_rank_rcond": rank,
            "raw_singular_ratio": _series_ratio(raw_singular),
            "equilibrated_singular_ratio": ratio,
            "rcond": RCOND,
            "pass_rank": bool(rank == expected_rank and ratio >= PASS_SINGULAR_RATIO),
            "row_scale_span": float(np.max(row_scale) / np.min(row_scale)),
            "column_scale_span": float(np.max(column_scale) / np.min(column_scale)),
        }
    )
    return solution, metrics


def _holdout_metrics(
    matrix: np.ndarray,
    constant: np.ndarray,
    solution: np.ndarray,
    labels: list[str] | None = None,
) -> dict[str, object]:
    residual = matrix @ solution + constant
    term_norm = np.abs(constant) + np.sum(
        np.abs(matrix * solution[np.newaxis, :]), axis=1
    )
    relative_mask = term_norm > ABS_FALLBACK_NORM
    ratios = np.zeros_like(residual)
    ratios[relative_mask] = np.abs(residual[relative_mask]) / term_norm[relative_mask]
    relative_max = float(np.max(ratios[relative_mask])) if np.any(relative_mask) else 0.0
    absolute_max = (
        float(np.max(np.abs(residual[~relative_mask])))
        if np.any(~relative_mask)
        else 0.0
    )
    absolute_indices = np.flatnonzero(~relative_mask)
    relative_indices = np.flatnonzero(relative_mask)
    relative_worst = (
        int(relative_indices[np.argmax(ratios[relative_mask])])
        if relative_indices.size
        else None
    )
    absolute_worst = (
        int(absolute_indices[np.argmax(np.abs(residual[~relative_mask]))])
        if absolute_indices.size
        else None
    )
    return {
        "rows": int(residual.size),
        "max_relative_residual": relative_max,
        "max_absolute_fallback_residual": absolute_max,
        "relative_row_count": int(np.sum(relative_mask)),
        "absolute_fallback_row_count": int(np.sum(~relative_mask)),
        "worst_relative_row": (
            labels[relative_worst] if labels is not None and relative_worst is not None else relative_worst
        ),
        "worst_absolute_fallback_row": (
            labels[absolute_worst] if labels is not None and absolute_worst is not None else absolute_worst
        ),
        "pass_holdout": bool(
            relative_max <= HOLDOUT_TOL and absolute_max <= ABS_FALLBACK_TOL
        ),
    }


def _standard_state(
    mode: str,
    k_mpc: float,
    inputs: legacy.FrozenInputs,
    deadline: Callable[[], None],
) -> tuple[dict[str, dict[int, float]], dict[str, object]]:
    legacy_state, _, metadata = m1_anchor.solve_standard_seed_anchored(
        mode, k_mpc, inputs, deadline, order=5
    )
    state = {
        target: dict(legacy_state[source]) for target, source in STATE_TO_LEGACY.items()
    }
    expected_rows = EXPECTED_M1_ROWS[mode]
    inverse_condition = 1.0 / max(float(metadata["condition_resolved"]), 1.0)
    metadata = dict(metadata)
    metadata.update(
        {
            "expected_matrix_shape_before_anchor": [expected_rows, 77],
            "expected_unknowns_after_anchor": 76,
            "inverse_resolved_condition": inverse_condition,
            "pass": bool(
                metadata["rank"] == metadata["unknowns"] == 76
                and metadata["driver_scaled_residual"] <= DRIVER_TOL
                and metadata["holdout_scaled_residual"] <= DRIVER_TOL
                and metadata["hard_anchor_absolute_difference"] <= ABS_FALLBACK_TOL
                and inverse_condition >= PASS_SINGULAR_RATIO
            ),
        }
    )
    return state, metadata


def _gamma_standard(
    k_mpc: float, hi: int, inputs: legacy.FrozenInputs
) -> tuple[dict[int, float], dict[str, object]]:
    background = legacy._fractional_background(k_mpc, hi, inputs)
    return dict(background["gamma"]), background


def _solve_fuel_zero(
    mode: str,
    k_mpc: float,
    inputs: legacy.FrozenInputs,
    standard: dict[str, dict[int, float]],
    support: tuple[int, int],
    deadline: Callable[[], None],
) -> tuple[dict[str, dict[int, float]], dict[str, object]]:
    lo, hi = support
    exponents = list(range(lo, hi + 1))
    series = legacy.Series(min(-6, lo - 6), hi + 10)
    background = legacy._standard_background(k_mpc, inputs, series)
    gamma, _ = _gamma_standard(k_mpc, hi + 10, inputs)
    index = {
        (name, power): position
        for position, (name, power) in enumerate(
            (item for name in ("delta_f", "U_f") for item in ((name, e) for e in exponents))
        )
    }
    primary = support == MODE_SUPPORT[mode]
    expected_count = (
        EXPECTED_F0_PRIMARY[mode] if primary else EXPECTED_F0_EXTENDED[mode]
    )
    if len(index) != expected_count:
        raise ValueError(
            f"{mode} F0 support {support} produced {len(index)} unknowns; expected {expected_count}"
        )

    def unpack(vector: np.ndarray) -> tuple[dict[int, float], dict[int, float]]:
        return (
            {e: float(vector[index[("delta_f", e)]]) for e in exponents},
            {e: float(vector[index[("U_f", e)]]) for e in exponents},
        )

    hx = series.dx(standard["h"])

    def rows(vector: np.ndarray) -> tuple[dict[int, float], dict[int, float]]:
        delta_f, u_f = unpack(vector)
        continuity = series.add(
            series.dx(delta_f),
            series.scale(delta_f, 3.0 * (2.0 - inputs.delta)),
            series.scale(series.mul(background["s2"], u_f), inputs.delta),
            series.scale(hx, 0.5 * inputs.delta),
            series.scale(u_f, 9.0 * inputs.delta * (2.0 - inputs.delta)),
            series.scale(series.mul(gamma, u_f), 3.0 * (2.0 - inputs.delta)),
        )
        euler = series.add(
            series.dx(u_f),
            series.scale(
                series.mul(series.add(background["hc"], {0: 2.0}), u_f), -1.0
            ),
            series.scale(delta_f, -1.0 / inputs.delta),
            series.scale(
                series.mul(
                    gamma,
                    series.add(series.scale(u_f, 2.0), series.scale(standard["U_c"], -1.0)),
                ),
                -1.0 / inputs.delta,
            ),
        )
        return continuity, euler

    def ledger(vector: np.ndarray) -> np.ndarray:
        continuity, euler = rows(vector)
        return np.asarray(
            [series.coef(item, e) for item in (continuity, euler) for e in exponents],
            dtype=float,
        )

    row_labels = [f"{row}[{e}]" for row in ("fuel_continuity", "fuel_Euler") for e in exponents]
    matrix, constant = _affine_system(ledger, len(index), deadline)
    solution, diagnostics = _solve_equilibrated(
        matrix, constant, len(index), row_labels, deadline
    )
    delta_f, u_f = unpack(solution)
    n = int(legacy.MODE_SPECS[mode]["n"])
    hx_n = n * standard["h"].get(n, 0.0)
    denominator = (n - 1.0) * (n + 6.0 - 3.0 * inputs.delta) + 9.0 * (
        2.0 - inputs.delta
    )
    expected_u = -hx_n / (2.0 * denominator)
    expected_delta = inputs.delta * (n - 1.0) * expected_u
    leading_difference = max(
        abs(u_f.get(n, 0.0) - expected_u),
        abs(delta_f.get(n, 0.0) - expected_delta),
    )
    diagnostics.update(
        {
            "support": [lo, hi],
            "leading_power": n,
            "leading_expected": {"U_f": expected_u, "delta_f": expected_delta},
            "leading_observed": {"U_f": u_f.get(n, 0.0), "delta_f": delta_f.get(n, 0.0)},
            "leading_max_absolute_difference": leading_difference,
            "pass_leading_postcheck": bool(leading_difference <= LEADING_TOL),
        }
    )
    deadline()
    return {"delta_f": delta_f, "U_f": u_f}, diagnostics


def _pair_background(
    k_mpc: float,
    inputs: legacy.FrozenInputs,
    series: legacy.Series,
    pair: legacy.PairSeries,
    hi: int,
) -> dict[str, object]:
    bg0 = legacy._standard_background(k_mpc, inputs, series)
    bg1 = legacy._fractional_background(k_mpc, hi + 10, inputs)
    denominator = (bg0["D"], bg1["D1"])
    invd = pair.inv(denominator)
    hc = pair.add(
        ({0: -1.0}, {}), pair.scale(pair.mul(pair.dx(denominator), invd), 0.5)
    )
    s2 = pair.mul(({2: 1.0}, {}), invd)
    rg, rfs, _, _ = inputs.radiation_weights
    og = pair.scale(invd, rg)
    ofs = pair.scale(invd, rfs)
    ob = pair.mul(({1: inputs.fb * float(bg0["mu"])}, {}), invd)
    oc = pair.mul(({1: inputs.fc * float(bg0["mu"])}, bg1["ash"]), invd)
    of = pair.mul(({}, bg1["fuel"]), invd)
    loading = ({1: 3.0 * inputs.fb * float(bg0["mu"]) / (4.0 * rg)}, {})
    inv1r = pair.inv(pair.add(({0: 1.0}, {}), loading))
    load_fraction = pair.mul(loading, inv1r)

    gamma0 = dict(bg1["gamma"])
    d1_over_d0 = pair.sfmul(dict(bg0["invD"]), dict(bg1["D1"]))
    gamma1 = pair.fscale(pair.sfmul(gamma0, d1_over_d0), -0.5)
    gamma = (gamma0, gamma1)

    fc_mu = inputs.fc * float(bg0["mu"])
    r1 = {power - 1: value / fc_mu for power, value in bg1["fuel"].items()}
    beta1 = {power: inputs.delta * value for power, value in r1.items()}
    r = ({}, pair.fclean(r1))
    beta = ({}, pair.fclean(beta1))
    return {
        "bg0": bg0,
        "bg1": bg1,
        "D": denominator,
        "invD": invd,
        "hc": hc,
        "s2": s2,
        "Og": og,
        "Ofs": ofs,
        "Ob": ob,
        "Oc": oc,
        "Of": of,
        "inv1R": inv1r,
        "load_fraction": load_fraction,
        "gamma": gamma,
        "r": r,
        "beta": beta,
    }


def _solve_m3(
    mode: str,
    k_mpc: float,
    inputs: legacy.FrozenInputs,
    standard: dict[str, dict[int, float]],
    support: tuple[int, int],
    deadline: Callable[[], None],
) -> tuple[dict[str, dict[int, float]], dict[str, object]]:
    lo, hi = support
    exponents = list(range(lo, hi + 1))
    series = legacy.Series(min(-8, lo - 8), hi + 12)
    pair = legacy.PairSeries(series, inputs.p, lo - 8, hi + 8)
    bg = _pair_background(k_mpc, inputs, series, pair, hi)
    names = tuple(contract.AUTHORITATIVE_STATE)
    index = {
        (name, power): position
        for position, (name, power) in enumerate(
            (item for name in names for item in ((name, e) for e in exponents))
        )
    }
    count = len(index)
    primary = support == MODE_SUPPORT[mode]
    expected_count = (
        EXPECTED_M3_PRIMARY[mode] if primary else EXPECTED_M3_EXTENDED[mode]
    )
    if count != expected_count:
        raise ValueError(
            f"{mode} M3 support {support} produced {count} unknowns; expected {expected_count}"
        )

    def state_pairs(vector: np.ndarray) -> dict[str, tuple[dict[int, float], dict[int, float]]]:
        return {
            name: (
                standard[name],
                {e: float(vector[index[(name, e)]]) for e in exponents},
            )
            for name in names
        }

    def all_rows(
        vector: np.ndarray,
    ) -> dict[str, tuple[dict[int, float], dict[int, float]]]:
        state = state_pairs(vector)
        hx = pair.dx(state["h"])
        etax = pair.dx(state["eta"])
        hxx = pair.dx(hx)
        etaxx = pair.dx(etax)
        u_difference = pair.add(state["U_f"], pair.scale(state["U_c"], -1.0))
        u_d = pair.add(state["U_c"], pair.mul(bg["beta"], u_difference))
        gamma_r = pair.mul(bg["gamma"], bg["r"])
        gamma_r_beta = pair.mul(gamma_r, bg["beta"])

        pressure_factor = pair.add(
            ({0: 3.0 * inputs.delta}, {}), bg["gamma"]
        )
        fuel_pressure = pair.add(
            state["delta_f"],
            pair.scale(pair.mul(pressure_factor, state["U_f"]), 2.0 - inputs.delta),
        )
        density = pair.add(
            pair.mul(bg["Og"], state["delta_gamma"]),
            pair.mul(bg["Ofs"], state["delta_fs"]),
            pair.mul(bg["Ob"], state["delta_b"]),
            pair.mul(bg["Oc"], state["delta_c"]),
            pair.mul(bg["Of"], state["delta_f"]),
        )
        momentum = pair.add(
            pair.scale(pair.mul(bg["Og"], state["U_gamma"]), 2.0),
            pair.scale(pair.mul(bg["Ofs"], state["U_fs"]), 2.0),
            pair.scale(pair.mul(bg["Ob"], state["U_b"]), 1.5),
            pair.scale(pair.mul(bg["Oc"], state["U_c"]), 1.5),
            pair.scale(pair.mul(bg["Of"], state["U_f"]), 1.5 * inputs.delta),
        )
        rows = {
            "gamma_continuity": pair.add(
                pair.dx(state["delta_gamma"]),
                pair.scale(pair.mul(bg["s2"], state["U_gamma"]), 4.0 / 3.0),
                pair.scale(hx, 2.0 / 3.0),
            ),
            "gamma_Euler": pair.add(
                pair.dx(state["U_gamma"]),
                pair.scale(pair.mul(bg["hc"], state["U_gamma"]), -1.0),
                pair.mul(bg["load_fraction"], state["U_gamma"]),
                pair.scale(pair.mul(bg["inv1R"], state["delta_gamma"]), -0.25),
            ),
            "fs_continuity": pair.add(
                pair.dx(state["delta_fs"]),
                pair.scale(pair.mul(bg["s2"], state["U_fs"]), 4.0 / 3.0),
                pair.scale(hx, 2.0 / 3.0),
            ),
            "fs_shear": pair.add(
                pair.scale(pair.dx(state["sigma_fs"]), 2.0),
                pair.scale(hx, -4.0 / 15.0),
                pair.scale(etax, -8.0 / 5.0),
                pair.scale(pair.mul(bg["s2"], state["U_fs"]), -8.0 / 15.0),
            ),
            "fs_Euler": pair.add(
                pair.dx(state["U_fs"]),
                pair.scale(pair.mul(bg["hc"], state["U_fs"]), -1.0),
                pair.scale(state["delta_fs"], -0.25),
                state["sigma_fs"],
            ),
            "baryon_continuity": pair.add(
                pair.dx(state["delta_b"]),
                pair.mul(bg["s2"], state["U_b"]),
                pair.scale(hx, 0.5),
            ),
            "cdm_continuity": pair.add(
                pair.dx(state["delta_c"]),
                pair.mul(bg["s2"], state["U_c"]),
                pair.scale(hx, 0.5),
                pair.scale(
                    pair.mul(
                        gamma_r,
                        pair.add(state["delta_f"], pair.scale(state["delta_c"], -1.0)),
                    ),
                    -1.0,
                ),
            ),
            "cdm_Euler": pair.add(
                pair.dx(state["U_c"]),
                pair.scale(
                    pair.mul(pair.add(bg["hc"], ({0: -1.0}, {})), state["U_c"]),
                    -1.0,
                ),
                pair.scale(pair.mul(gamma_r_beta, u_difference), -1.0),
            ),
            "tight_coupling": pair.add(
                state["U_b"], pair.scale(state["U_gamma"], -1.0)
            ),
            "fuel_continuity": pair.add(
                pair.dx(state["delta_f"]),
                pair.scale(state["delta_f"], 3.0 * (2.0 - inputs.delta)),
                pair.scale(pair.mul(bg["s2"], state["U_f"]), inputs.delta),
                pair.scale(hx, 0.5 * inputs.delta),
                pair.scale(state["U_f"], 9.0 * inputs.delta * (2.0 - inputs.delta)),
                pair.scale(
                    pair.mul(bg["gamma"], state["U_f"]),
                    3.0 * (2.0 - inputs.delta),
                ),
            ),
            "fuel_Euler": pair.add(
                pair.dx(state["U_f"]),
                pair.scale(
                    pair.mul(pair.add(bg["hc"], ({0: 2.0}, {})), state["U_f"]),
                    -1.0,
                ),
                pair.scale(state["delta_f"], -1.0 / inputs.delta),
                pair.scale(
                    pair.mul(
                        bg["gamma"],
                        pair.add(pair.scale(state["U_f"], 2.0), pair.scale(u_d, -1.0)),
                    ),
                    -1.0 / inputs.delta,
                ),
            ),
            "Einstein_trace": pair.add(
                hxx,
                pair.mul(pair.add(bg["hc"], ({0: 2.0}, {})), hx),
                pair.scale(pair.mul(bg["s2"], state["eta"]), -2.0),
                pair.scale(pair.mul(bg["Og"], state["delta_gamma"]), 3.0),
                pair.scale(pair.mul(bg["Ofs"], state["delta_fs"]), 3.0),
                pair.scale(pair.mul(bg["Of"], fuel_pressure), 9.0),
            ),
            "Einstein_traceless": pair.add(
                hxx,
                pair.mul(pair.add(bg["hc"], ({0: 2.0}, {})), hx),
                pair.scale(
                    pair.add(
                        etaxx,
                        pair.mul(pair.add(bg["hc"], ({0: 2.0}, {})), etax),
                    ),
                    6.0,
                ),
                pair.scale(pair.mul(bg["s2"], state["eta"]), -2.0),
                pair.scale(pair.mul(bg["Ofs"], state["sigma_fs"]), 12.0),
            ),
            "Einstein_00": pair.add(
                pair.scale(hx, -0.5),
                pair.scale(density, 1.5),
                pair.mul(bg["s2"], state["eta"]),
            ),
            "Einstein_0i": pair.add(etax, pair.scale(momentum, -1.0)),
        }
        return rows

    def ledger(vector: np.ndarray, selected: Iterable[str]) -> np.ndarray:
        rows = all_rows(vector)
        return np.asarray(
            [rows[row][1].get(e, 0.0) for row in selected for e in exponents],
            dtype=float,
        )

    zero_probe = all_rows(np.zeros(count, dtype=float))
    implemented_rows = tuple(zero_probe)
    implemented_holdout = tuple(
        name for name in implemented_rows if name in contract.AUTHORITATIVE_HOLDOUT
    )
    implemented_driver = tuple(
        name for name in implemented_rows if name not in contract.AUTHORITATIVE_HOLDOUT
    )
    production_contract = contract.validate_contract(
        tuple(standard), implemented_driver, implemented_holdout
    )
    driver_ledger = lambda vector: ledger(vector, implemented_driver)
    holdout_ledger = lambda vector: ledger(vector, implemented_holdout)
    driver_labels = [f"{row}[{e}]" for row in implemented_driver for e in exponents]
    holdout_labels = [f"{row}[{e}]" for row in implemented_holdout for e in exponents]
    matrix, constant = _affine_system(driver_ledger, count, deadline)
    solution, diagnostics = _solve_equilibrated(
        matrix, constant, count, driver_labels, deadline
    )
    holdout_matrix, holdout_constant = _affine_system(
        holdout_ledger, count, deadline
    )
    holdout = _holdout_metrics(
        holdout_matrix, holdout_constant, solution, holdout_labels
    )
    fractional = {
        name: {e: float(solution[index[(name, e)]]) for e in exponents}
        for name in names
    }
    leading_j = int(legacy.MODE_SPECS[mode]["leading_j"])
    forbidden = [e for e in exponents if e < leading_j]
    forbidden_max = max(
        [abs(fractional[name][e]) for name in names for e in forbidden] or [0.0]
    )
    # Structural order guard: Of has no Phi^0 part.  Therefore pure Phi^1
    # fuel perturbations cannot enter any Phi^1 Einstein source.  Their
    # generally non-zero product with Of[1] belongs to Phi^2.
    unit_fractional_fuel = {e: 1.0 for e in exponents}
    pure_delta = ({}, unit_fractional_fuel)
    pure_velocity = ({}, unit_fractional_fuel)
    forbidden_density = pair.mul(bg["Of"], pure_delta)[1]
    forbidden_momentum = pair.scale(
        pair.mul(bg["Of"], pure_velocity), 1.5 * inputs.delta
    )[1]
    pure_pressure_delta = pure_delta
    pure_pressure_velocity = pair.scale(
        pair.mul(
            pair.add(({0: 3.0 * inputs.delta}, {}), bg["gamma"]),
            pure_velocity,
        ),
        2.0 - inputs.delta,
    )
    forbidden_trace_delta = pair.scale(
        pair.mul(bg["Of"], pure_pressure_delta), 9.0
    )[1]
    forbidden_trace_velocity = pair.scale(
        pair.mul(bg["Of"], pure_pressure_velocity), 9.0
    )[1]
    forbidden_source_values = {
        "density_from_delta_f1": max([abs(v) for v in forbidden_density.values()] or [0.0]),
        "momentum_from_U_f1": max([abs(v) for v in forbidden_momentum.values()] or [0.0]),
        "trace_from_delta_f1": max([abs(v) for v in forbidden_trace_delta.values()] or [0.0]),
        "trace_from_U_f1": max([abs(v) for v in forbidden_trace_velocity.values()] or [0.0]),
    }
    forbidden_stress = max(forbidden_source_values.values())
    fuel_column_indices = [
        index[(name, e)] for name in ("delta_f", "U_f") for e in exponents
    ]
    fuel_driver_column_min_max_abs = min(
        float(np.max(np.abs(matrix[:, column]))) for column in fuel_column_indices
    )
    diagnostics.update(
        {
            "support": [lo, hi],
            "holdout": holdout,
            "production_contract": {
                "valid": bool(production_contract.valid),
                "errors": list(production_contract.errors),
                "implemented_state": list(standard),
                "implemented_driver": list(implemented_driver),
                "implemented_holdout": list(implemented_holdout),
            },
            "forbidden_earlier_layer_max_abs": float(forbidden_max),
            "forbidden_Omega_f1_times_fuel1_max_abs": float(forbidden_stress),
            "forbidden_Phi1_Einstein_source_sensitivities": forbidden_source_values,
            "fuel1_driver_column_min_max_abs": fuel_driver_column_min_max_abs,
            "pass_forbidden_layers": bool(forbidden_max <= FORBIDDEN_TOL),
            "pass_forbidden_stress_guard": bool(
                forbidden_stress <= FORBIDDEN_TOL
                and fuel_driver_column_min_max_abs > 0.0
            ),
            "pass_production_contract": bool(production_contract.valid),
            "Uc_lower_regular_max_abs": float(
                max([abs(fractional["U_c"][e]) for e in forbidden] or [0.0])
            ),
        }
    )
    deadline()
    background_export = {
        "fuel": dict(bg["bg1"]["fuel"]),
        "ash": dict(bg["bg1"]["ash"]),
        "D1": dict(bg["bg1"]["D1"]),
        "gamma": dict(bg["bg1"]["gamma"]),
        "transfer_gr": dict(bg["bg1"]["gr"]),
    }
    return fractional, {"diagnostics": diagnostics, "background": background_export}


def _coefficient_metrics(
    primary: dict[str, dict[int, float]], extended: dict[str, dict[int, float]]
) -> dict[str, object]:
    common = [
        (name, power)
        for name, values in primary.items()
        for power in values
        if power in extended[name]
    ]
    relative: list[tuple[float, str]] = []
    absolute: list[tuple[float, str]] = []
    for name, power in common:
        left, right = primary[name][power], extended[name][power]
        difference = abs(left - right)
        scale = max(abs(left), abs(right))
        label = f"{name}[{power}]"
        if scale > ABS_FALLBACK_NORM:
            relative.append((difference / scale, label))
        else:
            absolute.append((difference, label))
    worst_relative = max(relative, default=(0.0, "none"))
    worst_absolute = max(absolute, default=(0.0, "none"))
    return {
        "max_relative_difference": float(worst_relative[0]),
        "worst_relative_coefficient": worst_relative[1],
        "max_absolute_fallback_difference": float(worst_absolute[0]),
        "worst_absolute_fallback_coefficient": worst_absolute[1],
        "relative_count": len(relative),
        "absolute_fallback_count": len(absolute),
        "pass": bool(
            worst_relative[0] <= LOW_COEFFICIENT_TOL
            and worst_absolute[0] <= ABS_FALLBACK_TOL
        ),
    }


def _physical_fractional_state(
    fractional: dict[str, dict[int, float]],
    inputs: legacy.FrozenInputs,
    k_mpc: float,
    z: float,
    amplitude_override: float | None = None,
) -> np.ndarray:
    a = z / (k_mpc / inputs.hr0)
    amplitude = (
        inputs.af if amplitude_override is None else amplitude_override
    ) * a**inputs.p
    return np.asarray(
        [
            amplitude * sum(value * z**power for power, value in fractional[name].items())
            for name in contract.AUTHORITATIVE_STATE
        ],
        dtype=float,
    )


def _physical_standard_state(
    standard: dict[str, dict[int, float]], z: float
) -> np.ndarray:
    return np.asarray(
        [
            sum(value * z**power for power, value in standard[name].items())
            for name in contract.AUTHORITATIVE_STATE
        ],
        dtype=float,
    )


def _fractional_coefficient_state(
    fractional: dict[str, dict[int, float]], z: float
) -> np.ndarray:
    """Evaluate only the dimensionless Phi1 coefficient polynomial."""
    return np.asarray(
        [
            sum(value * z**power for power, value in fractional[name].items())
            for name in contract.AUTHORITATIVE_STATE
        ],
        dtype=float,
    )


def _truncation_metrics(
    mode: str,
    primary: dict[str, dict[int, float]],
    extended: dict[str, dict[int, float]],
    inputs: legacy.FrozenInputs,
    k_mpc: float,
) -> dict[str, object]:
    coefficient = _coefficient_metrics(primary, extended)
    tails: dict[str, dict[str, object]] = {}
    finite = True
    for z in Z_SURFACES:
        primary_value = _fractional_coefficient_state(primary, z)
        extended_value = _fractional_coefficient_state(extended, z)
        finite = finite and bool(
            np.all(np.isfinite(primary_value)) and np.all(np.isfinite(extended_value))
        )
        per_state: list[tuple[float, str, str]] = []
        for index, name in enumerate(contract.AUTHORITATIVE_STATE):
            difference = abs(extended_value[index] - primary_value[index])
            scale = max(abs(extended_value[index]), abs(primary_value[index]))
            if scale > ABS_FALLBACK_NORM:
                per_state.append((difference / scale, name, "relative"))
            else:
                per_state.append((difference, name, "absolute"))
        relative = [item for item in per_state if item[2] == "relative"]
        absolute = [item for item in per_state if item[2] == "absolute"]
        worst_relative = max(relative, default=(0.0, "none", "relative"))
        worst_absolute = max(absolute, default=(0.0, "none", "absolute"))
        tails[str(z)] = {
            "max_relative": float(worst_relative[0]),
            "worst_relative_state": worst_relative[1],
            "max_absolute_fallback": float(worst_absolute[0]),
            "worst_absolute_fallback_state": worst_absolute[1],
            "pass": bool(
                worst_relative[0] <= TAIL_TOL
                and worst_absolute[0] <= ABS_FALLBACK_TOL
            ),
        }
    deep = _physical_fractional_state(
        extended, inputs, k_mpc, Z_SURFACES[0], amplitude_override=1.0
    )
    shallow = _physical_fractional_state(
        extended, inputs, k_mpc, Z_SURFACES[1], amplitude_override=1.0
    )
    deep_norm = float(np.linalg.norm(deep))
    shallow_norm = float(np.linalg.norm(shallow))
    leading_j = int(legacy.MODE_SPECS[mode]["leading_j"])
    expected_power_ratio = (Z_SURFACES[1] / Z_SURFACES[0]) ** (
        inputs.p + leading_j
    )
    observed_power_ratio = shallow_norm / max(deep_norm, 1.0e-300)
    power_relative_difference = abs(
        observed_power_ratio / max(expected_power_ratio, 1.0e-300) - 1.0
    )
    max_tail = max(item["max_relative"] for item in tails.values())
    max_tail_absolute = max(item["max_absolute_fallback"] for item in tails.values())
    return {
        "common_low_coefficients": coefficient,
        "physical_tail_by_z": tails,
        "physical_tail_relative_max": max_tail,
        "physical_tail_absolute_fallback_max": max_tail_absolute,
        "surface_power": {
            "leading_j": leading_j,
            "deep_norm_unit_Af": deep_norm,
            "shallow_norm_unit_Af": shallow_norm,
            "observed_ratio": observed_power_ratio,
            "expected_ratio": expected_power_ratio,
            "relative_difference": power_relative_difference,
            "status": "DIAGNOSTIC_ONLY_SUBLEADING_TERMS_ALLOWED",
            "within_reference_1e-6": bool(power_relative_difference <= TAIL_TOL),
        },
        "z_cap": Z_CAP,
        "finite": finite,
        "pass": bool(
            finite
            and max(Z_SURFACES) <= Z_CAP
            and coefficient["pass"]
            and all(item["pass"] for item in tails.values())
        ),
    }


def _physical_background(
    inputs: legacy.FrozenInputs, k_mpc: float, a: float, hi: int
) -> dict[str, float]:
    fractional = legacy._fractional_background(k_mpc, hi + 10, inputs)
    z = (k_mpc / inputs.hr0) * a
    fuel = inputs.af * a**inputs.p * sum(
        value * z**power for power, value in fractional["fuel"].items()
    )
    ash = inputs.af * a**inputs.p * sum(
        value * z**power for power, value in fractional["ash"].items()
    )
    denominator = 1.0 + inputs.matter_ratio_a * a + fuel + ash
    hubble = inputs.h0_mpc * math.sqrt(inputs.omega_r0) * math.sqrt(denominator) / a**2
    return {"D": denominator, "H_Mpc_inverse": hubble, "rho_f_over_rho_r": fuel, "rho_ash_over_rho_r": ash}


def _spread(values: list[float]) -> float:
    return float((max(values) - min(values)) / max(max(abs(v) for v in values), 1.0e-300))


def _variant_inputs(name: str) -> legacy.FrozenInputs:
    base = legacy.FrozenInputs()
    if name == "nominal":
        return base
    if name == "gamma0":
        return replace(base, lam=0.0)
    if name == "af0":
        return replace(base, af=0.0)
    raise ValueError(name)


def _single_variant(
    mode: str,
    k_mpc: float,
    variant: str,
    standard: dict[str, dict[int, float]],
    deadline: Callable[[], None],
) -> dict[str, object]:
    inputs = _variant_inputs(variant)
    primary_support = MODE_SUPPORT[mode]
    extended_support = (primary_support[0], primary_support[1] + 2)
    fuel_primary, fuel_primary_diag = _solve_fuel_zero(
        mode, k_mpc, inputs, standard, primary_support, deadline
    )
    fuel_extended, fuel_extended_diag = _solve_fuel_zero(
        mode, k_mpc, inputs, standard, extended_support, deadline
    )
    standard_primary = dict(standard)
    standard_primary.update(fuel_primary)
    standard_extended = dict(standard)
    standard_extended.update(fuel_extended)
    fractional_primary, primary_meta = _solve_m3(
        mode, k_mpc, inputs, standard_primary, primary_support, deadline
    )
    fractional_extended, extended_meta = _solve_m3(
        mode, k_mpc, inputs, standard_extended, extended_support, deadline
    )
    truncation = _truncation_metrics(
        mode, fractional_primary, fractional_extended, inputs, k_mpc
    )
    diagnostics = [
        fuel_primary_diag,
        fuel_extended_diag,
        primary_meta["diagnostics"],
        extended_meta["diagnostics"],
    ]
    core_pass = all(
        item["pass_rank"] and item["pass_driver"] for item in diagnostics
    )
    core_pass = core_pass and fuel_primary_diag["pass_leading_postcheck"]
    core_pass = core_pass and fuel_extended_diag["pass_leading_postcheck"]
    for item in (primary_meta["diagnostics"], extended_meta["diagnostics"]):
        core_pass = core_pass and item["holdout"]["pass_holdout"]
        core_pass = core_pass and item["pass_forbidden_layers"]
        core_pass = core_pass and item["pass_forbidden_stress_guard"]
        core_pass = core_pass and item["pass_production_contract"]
        core_pass = core_pass and item["Uc_lower_regular_max_abs"] <= LEADING_TOL

    null_checks: dict[str, object] = {}
    if variant == "gamma0":
        ash_max = max([abs(v) for v in primary_meta["background"]["ash"].values()] or [0.0])
        transfer_max = max(
            [abs(v) for v in primary_meta["background"]["transfer_gr"].values()] or [0.0]
        )
        gamma_max = max(
            [abs(v) for v in primary_meta["background"]["gamma"].values()] or [0.0]
        )
        fuel_background_present = abs(primary_meta["background"]["fuel"].get(0, 0.0) - 1.0)
        null_checks = {
            "ash_max_abs": ash_max,
            "transfer_max_abs": transfer_max,
            "gamma_max_abs": gamma_max,
            "fuel_background_unit_coefficient_difference": fuel_background_present,
            "pass": bool(
                ash_max <= ABS_FALLBACK_TOL
                and transfer_max <= ABS_FALLBACK_TOL
                and gamma_max <= ABS_FALLBACK_TOL
                and fuel_background_present <= ABS_FALLBACK_TOL
            ),
        }
    elif variant == "af0":
        coefficient_values = [
            value for values in fractional_primary.values() for value in values.values()
        ]
        coefficients_finite = bool(np.all(np.isfinite(coefficient_values)))
        seed_differences: dict[str, float] = {}
        for z in Z_SURFACES:
            m1_value = _physical_standard_state(standard_primary, z)
            full_value = m1_value + _physical_fractional_state(
                fractional_primary, inputs, k_mpc, z
            )
            seed_differences[str(z)] = float(np.max(np.abs(full_value - m1_value)))
        background_differences: dict[str, dict[str, float]] = {}
        for a in A_VALUES_BACKGROUND:
            observed = _physical_background(inputs, k_mpc, a, BACKGROUND_MAX_J)
            expected_d = 1.0 + inputs.matter_ratio_a * a
            expected_h = (
                inputs.h0_mpc
                * math.sqrt(inputs.omega_r0)
                * math.sqrt(expected_d)
                / a**2
            )
            background_differences[str(a)] = {
                "D": abs(observed["D"] - expected_d),
                "H_Mpc_inverse": abs(observed["H_Mpc_inverse"] - expected_h),
                "rho_f_over_rho_r": abs(observed["rho_f_over_rho_r"]),
                "rho_ash_over_rho_r": abs(observed["rho_ash_over_rho_r"]),
            }
        max_seed_difference = max(seed_differences.values())
        max_background_difference = max(
            value for values in background_differences.values() for value in values.values()
        )
        null_checks = {
            "Phi1_coefficients_finite": coefficients_finite,
            "full_seed_minus_M1_max_abs_by_z": seed_differences,
            "full_seed_minus_M1_max_abs": max_seed_difference,
            "background_minus_M1_by_a": background_differences,
            "background_minus_M1_max_abs": max_background_difference,
            "coefficient_solve_rows": primary_meta["diagnostics"]["rows"],
            "coefficient_solve_unknowns": primary_meta["diagnostics"]["unknowns"],
            "pass": bool(
                coefficients_finite
                and max_seed_difference <= ABS_FALLBACK_TOL
                and max_background_difference <= ABS_FALLBACK_TOL
                and primary_meta["diagnostics"]["rows"] > 0
                and primary_meta["diagnostics"]["unknowns"] > 0
            ),
        }
    else:
        null_checks = {"pass": True}
    passed = bool(core_pass and truncation["pass"] and null_checks["pass"])
    deadline()
    return {
        "variant": variant,
        "inputs": asdict(inputs),
        "fuel_primary": {"state": fuel_primary, "diagnostics": fuel_primary_diag},
        "fuel_extended": {"state": fuel_extended, "diagnostics": fuel_extended_diag},
        "m3_primary": {"fractional_state": fractional_primary, **primary_meta},
        "m3_extended": {"fractional_state": fractional_extended, **extended_meta},
        "truncation": truncation,
        "null_limit": null_checks,
        "pass": passed,
    }


def run_smoke(max_runtime_seconds: float) -> dict[str, object]:
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("KMPC-027 smoke internal deadline exceeded")

    frozen = validate_frozen_contract()
    frozen_b1 = b1_guard.build_contract_guard(
        max_runtime_seconds=min(1.0, max_runtime_seconds)
    )
    tca0_bridge = production_tca0_reduction_guard()
    deadline()
    inputs = _variant_inputs("nominal")
    standard, standard_meta = _standard_state("AD", 0.05, inputs, deadline)
    fuel, fuel_meta = _solve_fuel_zero("AD", 0.05, inputs, standard, MODE_SUPPORT["AD"], deadline)
    standard.update(fuel)
    fractional, meta = _solve_m3("AD", 0.05, inputs, standard, MODE_SUPPORT["AD"], deadline)
    checks = {
        "contract": frozen["valid"],
        "frozen_B1_left_null_and_Bianchi_guard": (
            frozen_b1["execution_verdict"] == "PASS_R_A_B1_CONTRACT_GUARD_ONLY"
        ),
        "production_TCA0_weighted_Euler_and_Thomson_bridge": tca0_bridge["pass"],
        "M1": standard_meta["pass"],
        "F0_rank": fuel_meta["pass_rank"],
        "F0_driver": fuel_meta["pass_driver"],
        "M3_rank": meta["diagnostics"]["pass_rank"],
        "M3_driver": meta["diagnostics"]["pass_driver"],
        "holdout": meta["diagnostics"]["holdout"]["pass_holdout"],
        "production_contract": meta["diagnostics"]["pass_production_contract"],
        "Phi1_spectator_stress_guard": meta["diagnostics"]["pass_forbidden_stress_guard"],
        "finite": bool(
            np.all(np.isfinite(_physical_fractional_state(fractional, inputs, 0.05, Z_SURFACES[0])))
        ),
    }
    return {
        "test": "KMPC-027 attempt-6 smoke",
        "scope": "AD/k=0.05/nominal/primary only; no verdict",
        "checks": checks,
        "passed": bool(all(checks.values())),
        "runtime_seconds": time.monotonic() - started,
        "runtime_limit_seconds": max_runtime_seconds,
    }


def run_mode_shard(mode: str, max_runtime_seconds: float) -> dict[str, object]:
    if mode not in MODE_SUPPORT:
        raise ValueError(f"unsupported mode {mode}")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError(f"KMPC-027 {mode} internal deadline exceeded")

    frozen = validate_frozen_contract()
    frozen_b1 = b1_guard.build_contract_guard(
        max_runtime_seconds=min(1.0, max_runtime_seconds)
    )
    tca0_bridge = production_tca0_reduction_guard()
    deadline()
    results: dict[str, object] = {}
    background_by_a: dict[str, dict[str, list[float]]] = {
        str(a): {name: [] for name in ("D", "H_Mpc_inverse", "rho_f_over_rho_r", "rho_ash_over_rho_r")}
        for a in A_VALUES_BACKGROUND
    }
    checks: dict[str, bool] = {"frozen_contract": bool(frozen["valid"])}
    checks["frozen_B1_left_null_and_Bianchi_guard"] = (
        frozen_b1["execution_verdict"] == "PASS_R_A_B1_CONTRACT_GUARD_ONLY"
    )
    checks["production_TCA0_weighted_Euler_and_Thomson_bridge"] = bool(
        tca0_bridge["pass"]
    )
    for k_mpc in K_VALUES:
        standard, standard_meta = _standard_state(
            mode, k_mpc, _variant_inputs("nominal"), deadline
        )
        checks[f"k={k_mpc}:M1"] = bool(standard_meta["pass"])
        variants: dict[str, object] = {}
        for variant in ("nominal", "gamma0", "af0"):
            result = _single_variant(mode, k_mpc, variant, standard, deadline)
            variants[variant] = result
            checks[f"k={k_mpc}:{variant}"] = bool(result["pass"])
        af0_coefficient_bridge = _coefficient_metrics(
            variants["nominal"]["m3_primary"]["fractional_state"],
            variants["af0"]["m3_primary"]["fractional_state"],
        )
        af0_fuel_bridge = _coefficient_metrics(
            variants["nominal"]["fuel_primary"]["state"],
            variants["af0"]["fuel_primary"]["state"],
        )
        checks[f"k={k_mpc}:af0_new_solve_coefficient_bridge"] = bool(
            af0_coefficient_bridge["pass"] and af0_fuel_bridge["pass"]
        )
        for a in A_VALUES_BACKGROUND:
            values = _physical_background(
                _variant_inputs("nominal"), k_mpc, a, BACKGROUND_MAX_J
            )
            for name, value in values.items():
                background_by_a[str(a)][name].append(value)
        results[str(k_mpc)] = {
            "M1": standard_meta,
            "variants": variants,
            "af0_new_solve_bridge": {
                "M3_coefficients": af0_coefficient_bridge,
                "F0_coefficients": af0_fuel_bridge,
            },
        }
        deadline()

    background_spreads: dict[str, dict[str, float]] = {}
    for a, by_quantity in background_by_a.items():
        background_spreads[a] = {name: _spread(values) for name, values in by_quantity.items()}
        for name, spread in background_spreads[a].items():
            checks[f"background_k_independence:a={a}:{name}"] = bool(
                spread <= BACKGROUND_K_TOL
            )
    rg, rfs, rnu, rsteam = _variant_inputs("nominal").radiation_weights
    split_residual = abs(rnu + rsteam - rfs)
    checks["conditional_S_C_weight_split"] = bool(split_residual <= STEAM_SPLIT_TOL)
    passed = bool(checks) and all(checks.values())
    return {
        "test": f"KMPC-027 attempt-6 {mode} shard",
        "run_id": RUN_ID,
        "mode": mode,
        "scope": "conditional Phi1 M3-TCA0 seed only; no Phi2 CDM recoil, k->0/rho_c->0/delta->0 boundary closure, ODE, finite opacity, full hierarchy, CMB, S8, or S-M claim",
        "contract": frozen,
        "frozen_B1_left_null_Bianchi_guard": frozen_b1,
        "production_TCA0_reduction_guard": tca0_bridge,
        "source_hashes": source_hashes(),
        "thresholds": {
            "rcond": RCOND,
            "pass_singular_ratio": PASS_SINGULAR_RATIO,
            "driver": DRIVER_TOL,
            "holdout": HOLDOUT_TOL,
            "absolute_fallback_norm": ABS_FALLBACK_NORM,
            "absolute_fallback": ABS_FALLBACK_TOL,
            "low_coefficient": LOW_COEFFICIENT_TOL,
            "tail": TAIL_TOL,
            "background_k": BACKGROUND_K_TOL,
        },
        "k_Mpc_inverse": list(K_VALUES),
        "z_surfaces": list(Z_SURFACES),
        "background_a_surfaces": list(A_VALUES_BACKGROUND),
        "conditional_steam_split": {
            "R_gamma": rg,
            "R_fs": rfs,
            "R_nu": rnu,
            "R_steam": rsteam,
            "residual": split_residual,
        },
        "background_k_relative_spreads": background_spreads,
        "background_physical_values_by_a": background_by_a,
        "results": results,
        "checks": checks,
        "verdict": (
            "PASS_M3_TCA0_SEED_CONDITIONAL_SHARD"
            if passed
            else "REVIEW_M3_TCA0_SEED_SHARD_UNCLOSED"
        ),
        "canonical_depth": "60/100",
        "score_effect": "NONE_UNTIL_WHOLE_G7_CLOSES",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
