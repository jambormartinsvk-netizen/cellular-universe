"""Mode-resolved first-order P5 Puiseux seed algebra.

The module works in z=k*a/(H0*sqrt(Omega_r0)).  The homogeneous fuel
amplitude is Phi(k)=A_f*q**(-p), q=k/(H0*sqrt(Omega_r0)), so reconstructed
background quantities are functions of physical a only.  Trace and
traceless Einstein equations are drivers; 00 and 0i are holdouts.

Only the strict early tight-coupling limit is implemented here.  A finite
opacity run must remain blocked until n_e0*sigma_T is supplied by a separate
audited derivation.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import time
from typing import Callable

import numpy as np
import sympy as sp


VARS = (
    "h", "eta", "dg", "dfs", "db", "dc", "Ug", "Ufs", "sigfs",
    "Ub", "Uc",
)
DRIVER_ROWS = (
    "gamma_continuity", "gamma_Euler", "fs_continuity", "fs_shear",
    "fs_Euler", "baryon_continuity", "cdm_continuity", "cdm_Euler",
    "tight_coupling", "Einstein_trace", "Einstein_traceless",
)
HOLDOUT_ROWS = ("Einstein_00", "Einstein_0i")
MODE_SPECS = {
    "AD": {"n": 2, "f_min": 0, "f_max": 2, "leading_j": 2},
    "CDI": {"n": 1, "f_min": 0, "f_max": 1, "leading_j": 1},
    "BI": {"n": 1, "f_min": 0, "f_max": 1, "leading_j": 1},
    "NID": {"n": 3, "f_min": 0, "f_max": 3, "leading_j": 0},
    "NIV": {"n": 2, "f_min": -1, "f_max": 2, "leading_j": -1},
}


@dataclass(frozen=True)
class FrozenInputs:
    delta: float = 0.02297
    lam: float = 0.15
    h: float = 0.6637
    omega_m0: float = 0.3517
    ombh2: float = 0.02237
    neff_nu: float = 3.046
    neff_steam: float = 0.0535
    omega_gamma_h2: float = 2.47282e-5
    af: float = 7809.270101963506

    @property
    def p(self) -> float:
        return 4.0 - 3.0 * self.delta

    @property
    def omega_r0(self) -> float:
        total = self.neff_nu + self.neff_steam
        return self.omega_gamma_h2 * (1.0 + 0.2271 * total) / self.h**2

    @property
    def h0_mpc(self) -> float:
        return 100.0 * self.h / 299792.458

    @property
    def hr0(self) -> float:
        return self.h0_mpc * math.sqrt(self.omega_r0)

    @property
    def omega_parameter(self) -> float:
        return self.h0_mpc * self.omega_m0 / math.sqrt(self.omega_r0)

    @property
    def matter_ratio_a(self) -> float:
        return self.omega_m0 / self.omega_r0

    @property
    def fb(self) -> float:
        return self.ombh2 / (self.omega_m0 * self.h**2)

    @property
    def fc(self) -> float:
        return 1.0 - self.fb

    @property
    def radiation_weights(self) -> tuple[float, float, float, float]:
        denom = 1.0 + 0.2271 * (self.neff_nu + self.neff_steam)
        rg = 1.0 / denom
        rnu = 0.2271 * self.neff_nu / denom
        rs = 0.2271 * self.neff_steam / denom
        return rg, rnu + rs, rnu, rs


class Series:
    """Small integer-power Laurent-series helper."""

    def __init__(self, lo: int = -4, hi: int = 10) -> None:
        self.lo = lo
        self.hi = hi

    def clean(self, item: dict[int, float]) -> dict[int, float]:
        return {
            int(k): float(v) for k, v in item.items()
            if self.lo <= int(k) <= self.hi and abs(v) > 1.0e-300
        }

    def add(self, *items: dict[int, float]) -> dict[int, float]:
        out: dict[int, float] = {}
        for item in items:
            for key, value in item.items():
                if self.lo <= key <= self.hi:
                    out[key] = out.get(key, 0.0) + value
        return self.clean(out)

    def scale(self, item: dict[int, float], factor: float) -> dict[int, float]:
        return self.clean({key: factor * value for key, value in item.items()})

    def mul(self, first: dict[int, float], second: dict[int, float]) -> dict[int, float]:
        out: dict[int, float] = {}
        for i, left in first.items():
            for j, right in second.items():
                if self.lo <= i + j <= self.hi:
                    out[i + j] = out.get(i + j, 0.0) + left * right
        return self.clean(out)

    def dx(self, item: dict[int, float]) -> dict[int, float]:
        return self.clean({key: key * value for key, value in item.items()})

    def inv(self, item: dict[int, float]) -> dict[int, float]:
        entries = sorted((key, value) for key, value in item.items() if abs(value) > 1.0e-15)
        if not entries:
            raise ZeroDivisionError("zero standard series")
        lead_key, lead = entries[0]
        out = {-lead_key: 1.0 / lead}
        for n in range(1, self.hi + lead_key + 1):
            total = sum(
                item.get(lead_key + j, 0.0) * out.get(-lead_key + n - j, 0.0)
                for j in range(1, n + 1)
            )
            out[-lead_key + n] = -total / lead
        return self.clean(out)

    @staticmethod
    def coef(item: dict[int, float], key: int) -> float:
        return float(item.get(key, 0.0))


def _standard_background(k_mpc: float, inputs: FrozenInputs, series: Series) -> dict[str, object]:
    mu = inputs.omega_parameter / k_mpc
    denominator = {0: 1.0, 1: mu}
    invd = series.inv(denominator)
    hc = series.add({0: -1.0}, series.scale(series.mul({1: mu}, invd), 0.5))
    s2 = series.mul({2: 1.0}, invd)
    rg, rfs, _, _ = inputs.radiation_weights
    og, ofs = series.scale(invd, rg), series.scale(invd, rfs)
    ob = series.scale(series.mul({1: inputs.fb * mu}, invd), 1.0)
    oc = series.scale(series.mul({1: inputs.fc * mu}, invd), 1.0)
    loading = {1: 3.0 * inputs.fb * mu / (4.0 * rg)}
    inv1r = series.inv(series.add({0: 1.0}, loading))
    load_fraction = series.mul(loading, inv1r)
    return {
        "mu": mu, "D": denominator, "invD": invd, "hc": hc, "s2": s2,
        "Og": og, "Ofs": ofs, "Ob": ob, "Oc": oc,
        "loading": loading, "inv1R": inv1r, "load_fraction": load_fraction,
    }


def _standard_rows(
    state: dict[str, dict[int, float]],
    bg: dict[str, object],
    series: Series,
) -> dict[str, dict[int, float]]:
    hx = series.dx(state["h"])
    etax = series.dx(state["eta"])
    hxx = series.dx(hx)
    etaxx = series.dx(etax)
    density = series.add(
        series.mul(bg["Og"], state["dg"]),
        series.mul(bg["Ofs"], state["dfs"]),
        series.mul(bg["Ob"], state["db"]),
        series.mul(bg["Oc"], state["dc"]),
    )
    momentum = series.add(
        series.scale(series.mul(bg["Og"], state["Ug"]), 2.0),
        series.scale(series.mul(bg["Ofs"], state["Ufs"]), 2.0),
        series.scale(series.mul(bg["Ob"], state["Ub"]), 1.5),
        series.scale(series.mul(bg["Oc"], state["Uc"]), 1.5),
    )
    return {
        "gamma_continuity": series.add(
            series.dx(state["dg"]),
            series.scale(series.mul(bg["s2"], state["Ug"]), 4.0 / 3.0),
            series.scale(hx, 2.0 / 3.0),
        ),
        "gamma_Euler": series.add(
            series.dx(state["Ug"]),
            series.scale(series.mul(bg["hc"], state["Ug"]), -1.0),
            series.mul(bg["load_fraction"], state["Ug"]),
            series.scale(series.mul(bg["inv1R"], state["dg"]), -0.25),
        ),
        "fs_continuity": series.add(
            series.dx(state["dfs"]),
            series.scale(series.mul(bg["s2"], state["Ufs"]), 4.0 / 3.0),
            series.scale(hx, 2.0 / 3.0),
        ),
        "fs_shear": series.add(
            series.scale(series.dx(state["sigfs"]), 2.0),
            series.scale(hx, -4.0 / 15.0),
            series.scale(etax, -8.0 / 5.0),
            series.scale(series.mul(bg["s2"], state["Ufs"]), -8.0 / 15.0),
        ),
        "fs_Euler": series.add(
            series.dx(state["Ufs"]),
            series.scale(series.mul(bg["hc"], state["Ufs"]), -1.0),
            series.scale(state["dfs"], -0.25),
            state["sigfs"],
        ),
        "baryon_continuity": series.add(
            series.dx(state["db"]), series.mul(bg["s2"], state["Ub"]),
            series.scale(hx, 0.5),
        ),
        "cdm_continuity": series.add(
            series.dx(state["dc"]), series.mul(bg["s2"], state["Uc"]),
            series.scale(hx, 0.5),
        ),
        "cdm_Euler": series.add(
            series.dx(state["Uc"]),
            series.scale(series.mul(series.add(bg["hc"], {0: -1.0}), state["Uc"]), -1.0),
        ),
        "tight_coupling": series.add(state["Ub"], series.scale(state["Ug"], -1.0)),
        "Einstein_00": series.add(
            series.scale(hx, -0.5), series.scale(density, 1.5),
            series.mul(bg["s2"], state["eta"]),
        ),
        "Einstein_0i": series.add(etax, series.scale(momentum, -1.0)),
        "Einstein_trace": series.add(
            hxx, series.mul(series.add(bg["hc"], {0: 2.0}), hx),
            series.scale(series.mul(bg["s2"], state["eta"]), -2.0),
            series.scale(series.mul(bg["Og"], state["dg"]), 3.0),
            series.scale(series.mul(bg["Ofs"], state["dfs"]), 3.0),
        ),
        "Einstein_traceless": series.add(
            hxx, series.mul(series.add(bg["hc"], {0: 2.0}), hx),
            series.scale(
                series.add(etaxx, series.mul(series.add(bg["hc"], {0: 2.0}), etax)),
                6.0,
            ),
            series.scale(series.mul(bg["s2"], state["eta"]), -2.0),
            series.scale(series.mul(bg["Ofs"], state["sigfs"]), 12.0),
        ),
    }


def _initial_constraints(mode: str, rn: float, rg: float) -> list[tuple[str, int, float]]:
    initial: list[tuple[str, int, float]] = []
    minus = {name: 0.0 for name in VARS}
    zero = {name: 0.0 for name in VARS}
    if mode == "AD":
        zero["eta"] = 1.0
    elif mode == "CDI":
        zero["dc"] = 1.0
    elif mode == "BI":
        zero["db"] = 1.0
    elif mode == "NID":
        zero.update({
            "dg": -rn / rg, "dfs": 1.0,
            "Ug": -rn / (4.0 * rg), "Ufs": 0.25,
            "Ub": -rn / (4.0 * rg),
        })
    elif mode == "NIV":
        minus.update({
            "Ug": -3.0 * rn / (4.0 * rg), "Ufs": 0.75,
            "Ub": -3.0 * rn / (4.0 * rg),
        })
    else:
        raise ValueError(mode)
    initial.extend((name, -1, value) for name, value in minus.items())
    if mode == "NIV":
        for name in ("h", "eta", "dg", "dfs", "db", "dc", "sigfs", "Uc"):
            initial.append((name, 0, 0.0))
    else:
        initial.extend((name, 0, value) for name, value in zero.items())
    return initial


def _m1_expected_h(mode: str, bg: dict[str, object], inputs: FrozenInputs) -> tuple[int, float]:
    mu = float(bg["mu"])
    rg, rfs, _, _ = inputs.radiation_weights
    if mode == "AD":
        return 2, 0.5
    if mode == "CDI":
        return 1, inputs.fc * mu
    if mode == "BI":
        return 1, inputs.fb * mu
    if mode == "NID":
        return 3, inputs.fb * mu * rfs / (40.0 * rg)
    if mode == "NIV":
        return 2, 9.0 * inputs.fb * mu * rfs / (32.0 * rg)
    raise ValueError(mode)


def solve_standard_seed(
    mode: str,
    k_mpc: float,
    inputs: FrozenInputs,
    deadline: Callable[[], None],
    order: int = 5,
) -> tuple[dict[str, dict[int, float]], dict[str, object], dict[str, object]]:
    series = Series(-4, order + 5)
    exponents = list(range(-1, order + 1))
    bg = _standard_background(k_mpc, inputs, series)
    index = {(name, power): i for i, (name, power) in enumerate(
        (pair for name in VARS for pair in ((name, exponent) for exponent in exponents))
    )}
    count = len(index)

    def unpack(vector: np.ndarray) -> dict[str, dict[int, float]]:
        return {name: {power: vector[index[(name, power)]] for power in exponents} for name in VARS}

    initial = _initial_constraints(mode, inputs.radiation_weights[1], inputs.radiation_weights[0])

    def ledger(vector: np.ndarray) -> np.ndarray:
        rows = _standard_rows(unpack(vector), bg, series)
        out = [series.coef(rows[row], power) for row in DRIVER_ROWS for power in exponents]
        out.extend(vector[index[(name, power)]] - value for name, power, value in initial)
        return np.asarray(out, float)

    zero = np.zeros(count)
    constant = ledger(zero)
    matrix = np.empty((constant.size, count))
    for column in range(count):
        basis = np.zeros(count)
        basis[column] = 1.0
        matrix[:, column] = ledger(basis) - constant
    solution, _, rank, singular = np.linalg.lstsq(matrix, -constant, rcond=None)
    state = unpack(solution)
    rows = _standard_rows(state, bg, series)
    target_power, expected_h = _m1_expected_h(mode, bg, inputs)
    checked_hi = max(target_power, MODE_SPECS[mode]["f_max"])
    driver_max = max(
        abs(series.coef(rows[row], power))
        for row in DRIVER_ROWS for power in exponents if power <= checked_hi
    )
    holdout_max = max(
        abs(series.coef(rows[row], power))
        for row in HOLDOUT_ROWS for power in exponents if power <= checked_hi
    )
    scale = max(
        max(abs(value) for values in state.values() for value in values.values()),
        abs(expected_h), 1.0e-14,
    )
    metadata = {
        "rank": int(rank), "unknowns": count,
        "condition_resolved": float(singular[0] / singular[max(rank - 1, 0)]),
        "driver_scaled_residual": float(driver_max / scale),
        "holdout_scaled_residual": float(holdout_max / scale),
        "m1_h_power": target_power,
        "m1_expected_h_coefficient": expected_h,
        "m1_observed_h_coefficient": state["h"].get(target_power, 0.0),
        "m1_h_relative_difference": abs(state["h"].get(target_power, 0.0) - expected_h) / max(abs(expected_h), 1.0e-14),
    }
    deadline()
    return state, bg, metadata


def _fractional_background(
    k_mpc: float,
    max_j: int,
    inputs: FrozenInputs,
) -> dict[str, object]:
    qmode = k_mpc / inputs.hr0
    mu = inputs.omega_parameter / k_mpc
    g2 = (inputs.lam / math.sqrt(inputs.omega_r0)) / qmode**2
    gamma: dict[int, float] = {}
    binomial = 1.0
    for m in range(0, max_j + 3):
        if m > 0:
            binomial *= (-0.5 - (m - 1)) / m
        gamma[2 + m] = g2 * binomial * mu**m
    fuel = {0: 1.0, 1: 0.0}
    ash = {0: 0.0, 1: 0.0}
    for j in range(2, max_j + 1):
        source = sum(gamma.get(ell, 0.0) * fuel.get(j - ell, 0.0) for ell in range(2, j + 1))
        fuel[j] = -source / j
        ash[j] = source / (inputs.p + j - 1.0)
    total = {j: fuel.get(j, 0.0) + ash.get(j, 0.0) for j in range(0, max_j + 1)}
    transfer = {}
    for ell, gvalue in gamma.items():
        for m, fvalue in fuel.items():
            j = ell + m - 1
            if -4 <= j <= max_j + 4:
                transfer[j] = transfer.get(j, 0.0) + gvalue * fvalue / (inputs.fc * mu)
    return {
        "qmode": qmode, "mu": mu, "g2": g2, "gamma": gamma,
        "fuel": fuel, "ash": ash, "D1": total, "gr": transfer,
    }


class PairSeries:
    """First order pair: integer standard series plus Phi*z**p series."""

    def __init__(self, standard: Series, p: float, f_lo: int, f_hi: int) -> None:
        self.s = standard
        self.p = p
        self.f_lo = f_lo
        self.f_hi = f_hi

    def fclean(self, item: dict[int, float]) -> dict[int, float]:
        return {int(k): float(v) for k, v in item.items() if self.f_lo <= k <= self.f_hi and abs(v) > 1.0e-300}

    def fadd(self, *items: dict[int, float]) -> dict[int, float]:
        out: dict[int, float] = {}
        for item in items:
            for key, value in item.items():
                if self.f_lo <= key <= self.f_hi:
                    out[key] = out.get(key, 0.0) + value
        return self.fclean(out)

    def fscale(self, item: dict[int, float], factor: float) -> dict[int, float]:
        return self.fclean({key: factor * value for key, value in item.items()})

    def sfmul(self, standard: dict[int, float], fractional: dict[int, float]) -> dict[int, float]:
        out: dict[int, float] = {}
        for i, left in standard.items():
            for j, right in fractional.items():
                if self.f_lo <= i + j <= self.f_hi:
                    out[i + j] = out.get(i + j, 0.0) + left * right
        return self.fclean(out)

    def add(self, *pairs: tuple[dict[int, float], dict[int, float]]) -> tuple[dict[int, float], dict[int, float]]:
        return self.s.add(*(pair[0] for pair in pairs)), self.fadd(*(pair[1] for pair in pairs))

    def scale(self, pair: tuple[dict[int, float], dict[int, float]], factor: float) -> tuple[dict[int, float], dict[int, float]]:
        return self.s.scale(pair[0], factor), self.fscale(pair[1], factor)

    def mul(self, left: tuple[dict[int, float], dict[int, float]], right: tuple[dict[int, float], dict[int, float]]) -> tuple[dict[int, float], dict[int, float]]:
        return self.s.mul(left[0], right[0]), self.fadd(self.sfmul(left[0], right[1]), self.sfmul(right[0], left[1]))

    def inv(self, pair: tuple[dict[int, float], dict[int, float]]) -> tuple[dict[int, float], dict[int, float]]:
        inv_standard = self.s.inv(pair[0])
        fractional = self.fscale(self.sfmul(inv_standard, self.sfmul(inv_standard, pair[1])), -1.0)
        return inv_standard, fractional

    def dx(self, pair: tuple[dict[int, float], dict[int, float]]) -> tuple[dict[int, float], dict[int, float]]:
        return self.s.dx(pair[0]), self.fclean({j: (self.p + j) * value for j, value in pair[1].items()})


def solve_fractional_seed(
    mode: str,
    k_mpc: float,
    standard: dict[str, dict[int, float]],
    inputs: FrozenInputs,
    deadline: Callable[[], None],
) -> dict[str, object]:
    spec = MODE_SPECS[mode]
    f_min, f_max = int(spec["f_min"]), int(spec["f_max"])
    series = Series(-4, 10)
    pair = PairSeries(series, inputs.p, f_min - 4, f_max + 4)
    bg0 = _standard_background(k_mpc, inputs, series)
    bg1 = _fractional_background(k_mpc, f_max + 4, inputs)
    rg, rfs, _, _ = inputs.radiation_weights

    denominator = (bg0["D"], bg1["D1"])
    invd = pair.inv(denominator)
    dx_denominator = pair.dx(denominator)
    hc = pair.add(({0: -1.0}, {}), pair.scale(pair.mul(dx_denominator, invd), 0.5))
    s2 = pair.mul(({2: 1.0}, {}), invd)
    og = pair.scale(invd, rg)
    ofs = pair.scale(invd, rfs)
    ob = pair.mul(({1: inputs.fb * float(bg0["mu"])}, {}), invd)
    oc = pair.mul(({1: inputs.fc * float(bg0["mu"])}, bg1["ash"]), invd)
    of = pair.mul(({}, bg1["fuel"]), invd)
    loading = ({1: 3.0 * inputs.fb * float(bg0["mu"]) / (4.0 * rg)}, {})
    inv1r = pair.inv(pair.add(({0: 1.0}, {}), loading))
    load_fraction = pair.mul(loading, inv1r)
    gr = ({}, bg1["gr"])

    n = int(spec["n"])
    hx_n = n * standard["h"].get(n, 0.0)
    denom_f = (n - 1.0) * (n + 6.0 - 3.0 * inputs.delta) + 9.0 * (2.0 - inputs.delta)
    uf_coeff = -hx_n / (2.0 * denom_f)
    fuel_uf = {n: uf_coeff}
    fuel_df = {n: inputs.delta * (n - 1.0) * uf_coeff}
    gamma_series = bg1["gamma"]
    fuel_pf = series.add(
        fuel_df,
        series.scale(fuel_uf, 9.0 * inputs.delta * (2.0 - inputs.delta)),
        series.scale(series.mul(gamma_series, fuel_uf), 3.0 * (2.0 - inputs.delta)),
    )

    exponents = list(range(f_min, f_max + 1))
    index = {(name, power): i for i, (name, power) in enumerate(
        (item for name in VARS for item in ((name, exponent) for exponent in exponents))
    )}
    count = len(index)

    def variables(vector: np.ndarray) -> dict[str, tuple[dict[int, float], dict[int, float]]]:
        return {
            name: (standard[name], {power: vector[index[(name, power)]] for power in exponents})
            for name in VARS
        }

    def rows(vector: np.ndarray) -> dict[str, tuple[dict[int, float], dict[int, float]]]:
        state = variables(vector)
        hx = pair.dx(state["h"])
        etax = pair.dx(state["eta"])
        hxx = pair.dx(hx)
        etaxx = pair.dx(etax)
        density = pair.add(
            pair.mul(og, state["dg"]), pair.mul(ofs, state["dfs"]),
            pair.mul(ob, state["db"]), pair.mul(oc, state["dc"]),
            pair.mul(of, (fuel_df, {})),
        )
        momentum = pair.add(
            pair.scale(pair.mul(og, state["Ug"]), 2.0),
            pair.scale(pair.mul(ofs, state["Ufs"]), 2.0),
            pair.scale(pair.mul(ob, state["Ub"]), 1.5),
            pair.scale(pair.mul(oc, state["Uc"]), 1.5),
            pair.scale(pair.mul(of, (fuel_uf, {})), 1.5 * inputs.delta),
        )
        cdm_transfer = pair.mul(gr, pair.add((fuel_df, {}), pair.scale(state["dc"], -1.0)))
        return {
            "gamma_continuity": pair.add(pair.dx(state["dg"]), pair.scale(pair.mul(s2, state["Ug"]), 4.0 / 3.0), pair.scale(hx, 2.0 / 3.0)),
            "gamma_Euler": pair.add(pair.dx(state["Ug"]), pair.scale(pair.mul(hc, state["Ug"]), -1.0), pair.mul(load_fraction, state["Ug"]), pair.scale(pair.mul(inv1r, state["dg"]), -0.25)),
            "fs_continuity": pair.add(pair.dx(state["dfs"]), pair.scale(pair.mul(s2, state["Ufs"]), 4.0 / 3.0), pair.scale(hx, 2.0 / 3.0)),
            "fs_shear": pair.add(pair.scale(pair.dx(state["sigfs"]), 2.0), pair.scale(hx, -4.0 / 15.0), pair.scale(etax, -8.0 / 5.0), pair.scale(pair.mul(s2, state["Ufs"]), -8.0 / 15.0)),
            "fs_Euler": pair.add(pair.dx(state["Ufs"]), pair.scale(pair.mul(hc, state["Ufs"]), -1.0), pair.scale(state["dfs"], -0.25), state["sigfs"]),
            "baryon_continuity": pair.add(pair.dx(state["db"]), pair.mul(s2, state["Ub"]), pair.scale(hx, 0.5)),
            "cdm_continuity": pair.add(pair.dx(state["dc"]), pair.mul(s2, state["Uc"]), pair.scale(hx, 0.5), pair.scale(cdm_transfer, -1.0)),
            "cdm_Euler": pair.add(pair.dx(state["Uc"]), pair.scale(pair.mul(pair.add(hc, ({0: -1.0}, {})), state["Uc"]), -1.0)),
            "tight_coupling": pair.add(state["Ub"], pair.scale(state["Ug"], -1.0)),
            "Einstein_00": pair.add(pair.scale(hx, -0.5), pair.scale(density, 1.5), pair.mul(s2, state["eta"])),
            "Einstein_0i": pair.add(etax, pair.scale(momentum, -1.0)),
            "Einstein_trace": pair.add(hxx, pair.mul(pair.add(hc, ({0: 2.0}, {})), hx), pair.scale(pair.mul(s2, state["eta"]), -2.0), pair.scale(pair.mul(og, state["dg"]), 3.0), pair.scale(pair.mul(ofs, state["dfs"]), 3.0), pair.scale(pair.mul(of, (fuel_pf, {})), 9.0)),
            "Einstein_traceless": pair.add(hxx, pair.mul(pair.add(hc, ({0: 2.0}, {})), hx), pair.scale(pair.add(etaxx, pair.mul(pair.add(hc, ({0: 2.0}, {})), etax)), 6.0), pair.scale(pair.mul(s2, state["eta"]), -2.0), pair.scale(pair.mul(ofs, state["sigfs"]), 12.0)),
        }

    def ledger(vector: np.ndarray, selected: tuple[str, ...]) -> np.ndarray:
        row_map = rows(vector)
        return np.asarray([row_map[row][1].get(power, 0.0) for row in selected for power in exponents], float)

    zero = np.zeros(count)
    constant = ledger(zero, DRIVER_ROWS)
    matrix = np.empty((constant.size, count))
    for column in range(count):
        basis = np.zeros(count)
        basis[column] = 1.0
        matrix[:, column] = ledger(basis, DRIVER_ROWS) - constant
    solution, _, rank, singular = np.linalg.lstsq(matrix, -constant, rcond=None)
    driver_residual = matrix @ solution + constant
    holdout = ledger(solution, HOLDOUT_ROWS)
    state = {name: {power: solution[index[(name, power)]] for power in exponents} for name in VARS}
    coefficient_scale = max(
        np.max(np.abs(matrix) * np.maximum(np.abs(solution)[None, :], 1.0e-300)),
        np.max(np.abs(constant)), 1.0e-14,
    )
    forbidden = [power for power in exponents if power < int(spec["leading_j"])]
    forbidden_max = max(
        [abs(state[name].get(power, 0.0)) for name in VARS for power in forbidden] or [0.0]
    )
    deadline()
    return {
        "rank": int(rank), "unknowns": count,
        "condition": float(singular[0] / singular[-1]),
        "driver_scaled_residual": float(np.max(np.abs(driver_residual)) / coefficient_scale),
        "holdout_scaled_residual": float(np.max(np.abs(holdout)) / coefficient_scale),
        "holdout_by_row": {
            row: float(max(abs(rows(solution)[row][1].get(power, 0.0)) for power in exponents))
            for row in HOLDOUT_ROWS
        },
        "forbidden_earlier_layer_max_abs": float(forbidden_max),
        "fractional_state": state,
        "fuel_leading": {"Uf": fuel_uf, "delta_f": fuel_df, "pressure": fuel_pf},
        "background_fractional": {"fuel": bg1["fuel"], "ash": bg1["ash"], "D1": bg1["D1"]},
        "qmode": bg1["qmode"], "mu": bg1["mu"], "g2": bg1["g2"],
    }


def symbolic_identities(inputs: FrozenInputs) -> dict[str, sp.Expr]:
    q, a, af, g2a, mua = sp.symbols("q a A_f gamma2 mu_a", positive=True)
    delta = sp.Rational(2297, 100000)
    p = 4 - 3 * delta
    phi = af / q**p
    z = q * a
    g2 = g2a / q**2
    mu = mua / q
    d2 = g2 * (-sp.Rational(1, 2) + 1 / (p + 1))
    g3 = -g2 * mu / 2
    d3 = g3 * (-sp.Rational(1, 3) + 1 / (p + 2))
    n = sp.symbols("n", integer=True, positive=True)
    denom = (n - 1) * (n + 6 - 3 * delta) + 9 * (2 - delta)
    fuel_a = -1 / (2 * denom)
    nuc = n + 8 - 6 * delta
    r0 = sp.symbols("r0", positive=True)
    uc_coeff = delta * g2a * r0**2 * fuel_a / (nuc + 2)
    uc_euler = sp.simplify((nuc + 2) * uc_coeff - delta * g2a * r0**2 * fuel_a)
    return {
        "Phi_zp_minus_Af_ap": sp.simplify(phi * z**p - af * a**p),
        "D1_j2_k_cancellation": sp.simplify(phi * d2 * z**(p + 2) - af * g2a * (-sp.Rational(1, 2) + 1 / (p + 1)) * a**(p + 2)),
        "D1_j3_k_cancellation": sp.simplify(phi * d3 * z**(p + 3) - af * (-g2a * mua / 2) * (-sp.Rational(1, 3) + 1 / (p + 2)) * a**(p + 3)),
        "Uc_second_order_Euler": uc_euler,
        "Uc_lambda_zero": sp.simplify(uc_coeff.subs(g2a, 0)),
    }


def _evaluate_fractional_state(
    result: dict[str, object],
    inputs: FrozenInputs,
    k_mpc: float,
    a: float,
) -> np.ndarray:
    qmode = k_mpc / inputs.hr0
    phi = inputs.af / qmode**inputs.p
    z = qmode * a
    state = result["fractional_state"]
    return np.asarray([
        phi * sum(value * z**(inputs.p + power) for power, value in state[name].items())
        for name in VARS
    ], float)


def _evaluate_background_fraction(
    result: dict[str, object],
    inputs: FrozenInputs,
    k_mpc: float,
    a: float,
) -> float:
    qmode = k_mpc / inputs.hr0
    phi = inputs.af / qmode**inputs.p
    z = qmode * a
    d1 = result["background_fractional"]["D1"]
    return float(phi * sum(value * z**(inputs.p + power) for power, value in d1.items()))


def run_m3_tca0(
    max_runtime_seconds: float,
    k_values: tuple[float, ...] = (0.005, 0.05, 0.15),
    a_values: tuple[float, float] = (1.0e-6, 1.0e-4),
) -> dict[str, object]:
    started = time.monotonic()
    inputs = FrozenInputs()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("P5.3g7 M3-TCA0 internal deadline exceeded")

    exact = symbolic_identities(inputs)
    checks: dict[str, bool] = {f"exact_{key}": bool(value == 0) for key, value in exact.items()}
    results: dict[str, object] = {}
    backgrounds: dict[str, list[float]] = {str(a): [] for a in a_values}
    rg, rfs, rnu, rs = inputs.radiation_weights
    steam_split_residual = abs(rnu + rs - rfs)
    checks["conditional_steam_weight_split"] = steam_split_residual < 1.0e-14

    for k_mpc in k_values:
        by_mode: dict[str, object] = {}
        for mode in MODE_SPECS:
            standard, _, standard_meta = solve_standard_seed(mode, k_mpc, inputs, deadline)
            fractional = solve_fractional_seed(mode, k_mpc, standard, inputs, deadline)
            checks[f"{k_mpc}_{mode}_standard_driver"] = standard_meta["driver_scaled_residual"] < 1.0e-10
            checks[f"{k_mpc}_{mode}_standard_holdout"] = standard_meta["holdout_scaled_residual"] < 1.0e-10
            checks[f"{k_mpc}_{mode}_M1_h_map"] = standard_meta["m1_h_relative_difference"] < 1.0e-6
            checks[f"{k_mpc}_{mode}_fractional_full_rank"] = fractional["rank"] == fractional["unknowns"]
            checks[f"{k_mpc}_{mode}_fractional_driver"] = fractional["driver_scaled_residual"] < 1.0e-10
            checks[f"{k_mpc}_{mode}_00_0i_holdout"] = fractional["holdout_scaled_residual"] < 1.0e-9
            checks[f"{k_mpc}_{mode}_forbidden_layers"] = fractional["forbidden_earlier_layer_max_abs"] < 1.0e-10
            deep = _evaluate_fractional_state(fractional, inputs, k_mpc, a_values[0])
            shallow = _evaluate_fractional_state(fractional, inputs, k_mpc, a_values[1])
            finite = bool(np.all(np.isfinite(deep)) and np.all(np.isfinite(shallow)))
            observed_ratio = float(np.linalg.norm(shallow) / max(np.linalg.norm(deep), 1.0e-300))
            expected_ratio = (a_values[1] / a_values[0]) ** (inputs.p + MODE_SPECS[mode]["leading_j"])
            power_difference = abs(observed_ratio / expected_ratio - 1.0)
            checks[f"{k_mpc}_{mode}_two_start_finite"] = finite
            checks[f"{k_mpc}_{mode}_two_start_power"] = power_difference < 1.0e-6
            by_mode[mode] = {
                "standard": standard_meta,
                "fractional": fractional,
                "two_start": {
                    "a_deep": a_values[0], "a_shallow": a_values[1],
                    "deep_norm": float(np.linalg.norm(deep)),
                    "shallow_norm": float(np.linalg.norm(shallow)),
                    "observed_ratio": observed_ratio,
                    "expected_leading_ratio": expected_ratio,
                    "relative_difference": power_difference,
                },
            }
        reference_mode = by_mode["AD"]["fractional"]
        for a in a_values:
            backgrounds[str(a)].append(_evaluate_background_fraction(reference_mode, inputs, k_mpc, a))
        results[str(k_mpc)] = by_mode
        deadline()

    background_differences: dict[str, float] = {}
    for a, values in backgrounds.items():
        relative = (max(values) - min(values)) / max(max(abs(v) for v in values), 1.0e-300)
        background_differences[a] = float(abs(relative))
        checks[f"background_k_independence_a_{a}"] = abs(relative) < 1.0e-12

    passed = bool(checks) and all(checks.values())
    return {
        "test": "KMPC-022 P5.3g7 M3 mode-resolved exact-A1 Puiseux seed",
        "phase": "M3-TCA0",
        "scope": "strict early tight-coupling limit; trace/traceless plus species drivers; 00/0i holdouts; no ODE, finite opacity, P5.4, G8, score, or S-M claim",
        "inputs": {
            "delta": inputs.delta, "lambda": inputs.lam, "A_f": inputs.af,
            "p": inputs.p, "k_Mpc_inverse": list(k_values),
            "a_surfaces": list(a_values), "N_eff_nu": inputs.neff_nu,
            "Delta_N_eff_steam": inputs.neff_steam,
        },
        "exact_residuals": {key: str(value) for key, value in exact.items()},
        "steam_conditional_split": {"R_gamma": rg, "R_fs": rfs, "R_nu": rnu, "R_steam": rs, "weight_residual": steam_split_residual},
        "background_k_relative_differences": background_differences,
        "mode_results": results,
        "checks": checks,
        "verdict": "PASS_M3_TCA0_CONDITIONAL" if passed else "REVIEW_M3_TCA0_UNCLOSED",
        "P5_3g7_verdict": "REVIEW_BLOCKED_FINITE_OPACITY_AND_S_M" if passed else "REVIEW_BLOCKED_M3",
        "canonical_depth": "60/100",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
