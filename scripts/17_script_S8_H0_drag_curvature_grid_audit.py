"""Independent reproduction audit of the proposed v3.18 drag/curvature grids.

This script extends the equations of script 09 in two explicit ways:

* drag: a positive constant gamma_drag is added to the coefficient of D'
  in the linear growth equation, from z=1000 to today;
* curvature: Omega_K a^-2 is added to E^2 and the FLRW transverse comoving
  distance S_K(chi) is used for the CMB angular-scale anchor.

It also reconstructs the local 'chi2_3front' exactly as used in script 09 and
demonstrates its sensitivity to the omitted w0-wa covariance.  The score is a
diagnostic of three compressed anchors, not a cosmological likelihood.
"""

from __future__ import annotations

import json
import math

import numpy as np
from scipy.integrate import quad


C_KM = 299792.458
OM_B = 0.02237
OM_M_STAR = 0.1430
OM_GAMMA = 2.469e-5
Z_STAR = 1089.9
X_STAR = -math.log1p(Z_STAR)
LAMBDA = 0.15
DELTA = 0.02297
DELTA_NEFF = 0.0535

W0_ANCHOR = -0.75
W0_SIGMA = 0.06
WA_ANCHOR = -0.86
WA_SIGMA = 0.25
S8_ANCHOR = 0.815
S8_SIGMA = 0.019


DRAG_GRID_REPORTED = {
    0.00: (66.373, 0.8745, 18.75),
    0.01: (66.373, 0.8526, 12.85),
    0.02: (66.373, 0.8313, 9.67),
    0.03: (66.373, 0.8107, 8.99),
    0.04: (66.373, 0.7906, 10.58),
    0.05: (66.373, 0.7712, 14.26),
    0.06: (66.373, 0.7523, 19.84),
}

CURVATURE_GRID_REPORTED = {
    -0.005: (64.293, 0.9173, 38.02),
    -0.003: (65.097, 0.9004, 29.17),
    -0.001: (65.938, 0.8832, 21.84),
    0.000: (66.373, 0.8745, 18.75),
    0.001: (66.818, 0.8658, 16.07),
    0.002: (67.275, 0.8570, 13.79),
    0.003: (67.742, 0.8481, 11.93),
    0.005: (68.714, 0.8302, 9.50),
}


def om_r_total(delta_neff: float) -> float:
    return OM_GAMMA * (1.0 + 0.2271 * (3.046 + delta_neff))


def background(
    h: float,
    omega_m0: float,
    omega_k0: float,
    lam: float = LAMBDA,
    delta: float = DELTA,
    delta_neff: float = DELTA_NEFF,
    xmin: float = -7.8,
    n: int = 3500,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    omega_r0 = om_r_total(delta_neff) / h**2
    omega_f0 = 1.0 - omega_m0 - omega_r0 - omega_k0
    xs = np.linspace(0.0, xmin, n)
    dx = float(xs[1] - xs[0])
    states = np.zeros((n, 3))
    states[0] = [omega_f0, omega_m0, omega_r0]

    def derivative(x: float, state: np.ndarray) -> np.ndarray:
        fuel, matter, radiation = state
        curvature = omega_k0 * math.exp(-2.0 * x)
        e = math.sqrt(max(fuel + matter + radiation + curvature, 1.0e-30))
        return np.array(
            [
                -3.0 * delta * fuel - lam * fuel / e,
                -3.0 * matter + lam * fuel / e,
                -4.0 * radiation,
            ]
        )

    for index in range(n - 1):
        x = float(xs[index])
        state = states[index]
        k1 = derivative(x, state)
        k2 = derivative(x + dx / 2.0, state + dx * k1 / 2.0)
        k3 = derivative(x + dx / 2.0, state + dx * k2 / 2.0)
        k4 = derivative(x + dx, state + dx * k3)
        states[index + 1] = state + dx * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0

    curvature = omega_k0 * np.exp(-2.0 * xs)
    e = np.sqrt(np.maximum(np.sum(states, axis=1) + curvature, 1.0e-30))
    return xs, states, e


def transverse_factor(radial_dimensionless: float, omega_k0: float) -> float:
    if abs(omega_k0) < 1.0e-14:
        return radial_dimensionless
    root = math.sqrt(abs(omega_k0))
    if omega_k0 > 0.0:
        return math.sinh(root * radial_dimensionless) / root
    return math.sin(root * radial_dimensionless) / root


def sound_horizon(h: float, delta_neff: float, omega_k0: float) -> float:
    om_r0 = om_r_total(delta_neff)
    om_k0_physical = h**2 * omega_k0
    om_lambda = h**2 - OM_M_STAR - om_r0 - om_k0_physical

    def hubble(a: float) -> float:
        value = (
            OM_M_STAR * a**-3
            + om_r0 * a**-4
            + om_k0_physical * a**-2
            + max(om_lambda, 0.0)
        )
        return 100.0 * math.sqrt(value)

    def integrand(a: float) -> float:
        rb = (3.0 * OM_B / (4.0 * OM_GAMMA)) * a
        sound_speed = C_KM / math.sqrt(3.0 * (1.0 + rb))
        return sound_speed / (a**2 * hubble(a))

    return float(quad(integrand, 1.0e-9, 1.0 / (1.0 + Z_STAR), limit=400)[0])


def flat_theta_target() -> float:
    h = 0.673
    om_r0 = om_r_total(0.0)
    om_lambda = h**2 - OM_M_STAR - om_r0

    def hubble(a: float) -> float:
        return 100.0 * math.sqrt(OM_M_STAR * a**-3 + om_r0 * a**-4 + om_lambda)

    radial = quad(
        lambda a: C_KM / (a**2 * hubble(a)),
        1.0 / (1.0 + Z_STAR),
        1.0,
        limit=400,
    )[0]
    return sound_horizon(h, 0.0, 0.0) / radial


THETA_TARGET = flat_theta_target()


def anchor(omega_k0: float) -> tuple[float, float, np.ndarray, np.ndarray, np.ndarray, float]:
    low, high = 0.55, 0.80
    last = None
    for _ in range(22):
        h = (low + high) / 2.0
        omega_m0 = 0.30
        for _ in range(6):
            xs, states, e = background(h, omega_m0, omega_k0)
            matter_star = float(np.interp(X_STAR, xs[::-1], states[::-1, 1]))
            target = OM_M_STAR * math.exp(-3.0 * X_STAR) / h**2
            omega_m0 *= target / matter_star

        mask = xs >= X_STAR
        integrand = np.exp(-xs[mask]) / e[mask]
        radial_dimensionless = float(np.trapezoid(integrand[::-1], xs[mask][::-1]))
        dm = C_KM / (100.0 * h) * transverse_factor(radial_dimensionless, omega_k0)
        rs = sound_horizon(h, DELTA_NEFF, omega_k0)
        dm_target = rs / THETA_TARGET
        if dm > dm_target:
            low = h
        else:
            high = h
        last = (h, omega_m0, xs, states, e, rs)
    assert last is not None
    return last


def cpl_fit(
    xs: np.ndarray,
    states: np.ndarray,
    e: np.ndarray,
    omega_m0: float,
    omega_r0: float,
    omega_k0: float,
) -> tuple[float, float]:
    x = xs
    effective_de = (
        e**2
        - omega_m0 * np.exp(-3.0 * x)
        - omega_r0 * np.exp(-4.0 * x)
        - omega_k0 * np.exp(-2.0 * x)
    )
    z = np.exp(-x) - 1.0
    mask = (z > 0.0) & (z < 1.0) & (effective_de > 1.0e-6)
    log_density = np.log(effective_de[mask])
    w = -1.0 - np.gradient(log_density, x[mask]) / 3.0
    a = np.exp(x[mask])
    weights = effective_de[mask]
    design = np.vstack([np.ones_like(a), 1.0 - a]).T
    coefficients = np.linalg.lstsq(design * weights[:, None], w * weights, rcond=None)[0]
    return float(coefficients[0]), float(coefficients[1])


def growth(
    xs: np.ndarray,
    states: np.ndarray,
    e: np.ndarray,
    gamma_drag: float,
) -> float:
    x = xs[::-1]
    matter = states[::-1, 1]
    ee = e[::-1]
    dln_e = np.gradient(np.log(ee), x)
    start = -math.log(1001.0)
    index0 = int(np.searchsorted(x, start))
    density_contrast = math.exp(float(x[index0]))
    theta = -density_contrast

    for index in range(index0, len(x) - 1):
        step = float(x[index + 1] - x[index])

        def derivative(state: np.ndarray, grid_index: int) -> np.ndarray:
            delta_m, velocity = state
            return np.array(
                [
                    -velocity,
                    -(2.0 + dln_e[grid_index] + gamma_drag) * velocity
                    - 1.5 * matter[grid_index] / ee[grid_index] ** 2 * delta_m,
                ]
            )

        state = np.array([density_contrast, theta])
        k1 = derivative(state, index)
        k2 = derivative(state + step * k1 / 2.0, index)
        k3 = derivative(state + step * k2 / 2.0, index)
        k4 = derivative(state + step * k3, min(index + 1, len(x) - 1))
        state += step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        density_contrast, theta = state
    return float(density_contrast)


def chi2_3front(w0: float, wa: float, s8: float) -> float:
    return (
        ((w0 - W0_ANCHOR) / W0_SIGMA) ** 2
        + ((wa - WA_ANCHOR) / WA_SIGMA) ** 2
        + ((s8 - S8_ANCHOR) / S8_SIGMA) ** 2
    )


def correlated_w_chi2(w0: float, wa: float, correlation: float) -> float:
    x = (w0 - W0_ANCHOR) / W0_SIGMA
    y = (wa - WA_ANCHOR) / WA_SIGMA
    return (x * x - 2.0 * correlation * x * y + y * y) / (1.0 - correlation**2)


def lcdm_reference() -> tuple[float, float, float]:
    # Same validation construction as script 09, with no fuel metabolism.
    h = 0.673
    omega_m = OM_M_STAR / h**2
    xs = np.linspace(-7.8, 0.0, 3500)
    omega_r0 = om_r_total(0.0) / h**2
    omega_lambda = 1.0 - omega_m - omega_r0
    matter = omega_m * np.exp(-3.0 * xs)
    radiation = omega_r0 * np.exp(-4.0 * xs)
    fuel = np.full_like(xs, omega_lambda)
    states = np.vstack([fuel, matter, radiation]).T
    e = np.sqrt(np.sum(states, axis=1))
    d = growth(xs[::-1], states[::-1], e[::-1], 0.0)
    return h, omega_m, d


def compare_row(computed: tuple[float, float, float], reported: tuple[float, float, float]) -> dict:
    names = ("H0", "S8", "chi2_3front")
    return {
        name: {
            "computed": float(computed[index]),
            "reported": float(reported[index]),
            "difference": float(computed[index] - reported[index]),
        }
        for index, name in enumerate(names)
    }


def main() -> int:
    lcdm_h, lcdm_omega_m, lcdm_growth = lcdm_reference()
    lcdm_s8 = 0.811 * math.sqrt(lcdm_omega_m / 0.3)
    lcdm_pseudo_chi2 = chi2_3front(-1.0, 0.0, lcdm_s8)

    # Background is independent of drag, so solve it once.
    h0, omega_m0, xs, states, e, rs = anchor(0.0)
    omega_r0 = om_r_total(DELTA_NEFF) / h0**2
    w0, wa = cpl_fit(xs, states, e, omega_m0, omega_r0, 0.0)

    drag_results = {}
    for gamma, reported in DRAG_GRID_REPORTED.items():
        d = growth(xs, states, e, gamma)
        sigma8 = 0.811 * d / lcdm_growth
        s8 = sigma8 * math.sqrt(omega_m0 / 0.3)
        pseudo = chi2_3front(w0, wa, s8)
        computed = (100.0 * h0, s8, pseudo)
        drag_results[str(gamma)] = compare_row(computed, reported)

    curvature_results = {}
    for omega_k0, reported in CURVATURE_GRID_REPORTED.items():
        h, omega_m, cx, cstates, ce, crs = anchor(omega_k0)
        omega_r = om_r_total(DELTA_NEFF) / h**2
        cw0, cwa = cpl_fit(cx, cstates, ce, omega_m, omega_r, omega_k0)
        d = growth(cx, cstates, ce, 0.0)
        sigma8 = 0.811 * d / lcdm_growth
        s8 = sigma8 * math.sqrt(omega_m / 0.3)
        pseudo = chi2_3front(cw0, cwa, s8)
        computed = (100.0 * h, s8, pseudo)
        curvature_results[str(omega_k0)] = {
            **compare_row(computed, reported),
            "Omega_m": omega_m,
            "w0": cw0,
            "wa": cwa,
            "sound_horizon_Mpc": crs,
        }

    covariance_sensitivity = {}
    for correlation in (-0.95, -0.90, -0.80, -0.50, 0.0, 0.50, 0.80, 0.90, 0.95):
        model_w = correlated_w_chi2(w0, wa, correlation)
        lcdm_w = correlated_w_chi2(-1.0, 0.0, correlation)
        covariance_sensitivity[str(correlation)] = {
            "model_w0_wa_chi2": model_w,
            "lcdm_w0_wa_chi2": lcdm_w,
            "model_minus_lcdm": model_w - lcdm_w,
        }

    output = {
        "scope": "reproduction_of_script09_extension_not_full_likelihood",
        "base_model": {
            "H0": 100.0 * h0,
            "Omega_m": omega_m0,
            "w0": w0,
            "wa": wa,
            "sound_horizon_Mpc": rs,
        },
        "lcdm_reference": {
            "H0": 100.0 * lcdm_h,
            "Omega_m": lcdm_omega_m,
            "S8": lcdm_s8,
            "chi2_3front": lcdm_pseudo_chi2,
        },
        "drag_grid_comparison": drag_results,
        "curvature_grid_comparison": curvature_results,
        "w0_wa_covariance_sensitivity": covariance_sensitivity,
        "score_warnings": [
            "chi2_3front contains no H0 term",
            "chi2_3front assumes zero covariance between w0 and wa",
            "chi2_3front is not evaluated on original BAO/SN/CMB/lensing data",
            "parameter-count and look-elsewhere penalties are absent",
        ],
    }
    print(json.dumps(output, indent=2, sort_keys=True))

    checks = [
        abs(100.0 * h0 - 66.37) < 0.10,
        abs(w0 + 0.919) < 0.01,
        abs(wa + 0.612) < 0.02,
        drag_results["0.03"]["S8"]["computed"] < drag_results["0.0"]["S8"]["computed"],
        curvature_results["0.005"]["H0"]["computed"] > curvature_results["0.0"]["H0"]["computed"],
    ]
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
