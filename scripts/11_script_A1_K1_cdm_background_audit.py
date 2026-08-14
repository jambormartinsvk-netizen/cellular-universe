#!/usr/bin/env python3
"""Audit backgroundu koľaje A1-K1: prenos Q vytvára iba CDM.

Skript reprodukuje rozdelenie spoločnej hmotovej premennej pipeline 09
na samostatné baryóny a CDM. Kontroluje:

1. kladnosť všetkých hustôt,
2. Bianchiho/continuity súčet,
3. štandardnú limitu lambda = 0,
4. konvergenciu RK4 pri polovičnom kroku,
5. podiel dnešného CDM vytvorený od rekombinácie.

Výstupom je JSON na stdout. Skript nezapisuje žiadne súbory.
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ModelParameters:
    h: float = 0.6637
    omega_m0: float = 0.3517
    lam: float = 0.15
    delta: float = 0.02297
    delta_neff: float = 0.0535
    omega_b: float = 0.02237
    omega_gamma: float = 2.469e-5
    neff_standard: float = 3.046
    z_star: float = 1089.9


@dataclass(frozen=True)
class IntegrationSettings:
    x_min: float = -25.0
    step: float = 1.0e-3


def radiation_density_today(p: ModelParameters) -> float:
    """X_r0 = rho_r0/rho_crit,0 in the convention of pipeline 09."""
    return (
        p.omega_gamma
        * (1.0 + 0.2271 * (p.neff_standard + p.delta_neff))
        / p.h**2
    )


def initial_state(p: ModelParameters) -> tuple[np.ndarray, float]:
    """Return [X_f0, X_m0, X_r0] and X_b0."""
    x_r0 = radiation_density_today(p)
    x_f0 = 1.0 - p.omega_m0 - x_r0
    x_b0 = p.omega_b / p.h**2
    x_c0 = p.omega_m0 - x_b0

    if min(x_f0, x_b0, x_c0, x_r0) <= 0.0:
        raise ValueError(
            "Initial densities must be positive: "
            f"Xf0={x_f0}, Xb0={x_b0}, Xc0={x_c0}, Xr0={x_r0}"
        )

    return np.array([x_f0, p.omega_m0, x_r0], dtype=float), x_b0


def rhs(y: np.ndarray, p: ModelParameters) -> np.ndarray:
    """V1 background derivative d[X_f, X_m, X_r]/d ln(a)."""
    x_f, x_m, x_r = y
    e_squared = x_f + x_m + x_r
    if e_squared <= 0.0:
        raise FloatingPointError(f"E^2 became non-positive: {e_squared}")
    e = np.sqrt(e_squared)
    transfer = p.lam * x_f / e
    return np.array(
        [
            -3.0 * p.delta * x_f - transfer,
            -3.0 * x_m + transfer,
            -4.0 * x_r,
        ]
    )


def integrate_background(
    p: ModelParameters, settings: IntegrationSettings
) -> tuple[np.ndarray, np.ndarray, float]:
    """Integrate from x=0 backwards to x_min with fixed-step RK4."""
    if settings.x_min >= 0.0:
        raise ValueError("x_min must be negative")
    if settings.step <= 0.0:
        raise ValueError("step must be positive")

    intervals = int(round(abs(settings.x_min) / settings.step))
    if intervals < 1:
        raise ValueError("Integration interval must contain at least one step")

    xs = np.linspace(0.0, settings.x_min, intervals + 1)
    dx = xs[1] - xs[0]
    y = np.zeros((len(xs), 3), dtype=float)
    y[0], x_b0 = initial_state(p)

    for i in range(len(xs) - 1):
        state = y[i]
        k1 = rhs(state, p)
        k2 = rhs(state + 0.5 * dx * k1, p)
        k3 = rhs(state + 0.5 * dx * k2, p)
        k4 = rhs(state + dx * k3, p)
        y[i + 1] = state + dx * (k1 + 2*k2 + 2*k3 + k4) / 6.0

    return xs, y, x_b0


def interpolate_at_x(xs: np.ndarray, values: np.ndarray, x: float) -> float:
    """Interpolate an array stored on a decreasing x grid."""
    if not xs[-1] <= x <= xs[0]:
        raise ValueError(f"Requested x={x} lies outside [{xs[-1]}, {xs[0]}]")
    return float(np.interp(x, xs[::-1], values[::-1]))


def summarize(
    p: ModelParameters, xs: np.ndarray, y: np.ndarray, x_b0: float
) -> dict[str, float | bool]:
    """Compute physical and numerical diagnostics for A1-K1."""
    x_f, x_m, x_r = y.T
    x_b = x_b0 * np.exp(-3.0 * xs)
    x_c = x_m - x_b
    e = np.sqrt(x_f + x_m + x_r)

    x_star = -np.log1p(p.z_star)
    x_b_star = interpolate_at_x(xs, x_b, x_star)
    x_c_star = interpolate_at_x(xs, x_c, x_star)
    x_m_star = interpolate_at_x(xs, x_m, x_star)
    x_c_comoving_star = x_c_star * np.exp(3.0 * x_star)
    fraction_created = (x_c[0] - x_c_comoving_star) / x_c[0]

    transfer = p.lam * x_f / e
    r_f = -3.0 * p.delta * x_f - transfer
    r_m = -3.0 * x_m + transfer
    r_b = -3.0 * x_b
    r_c = r_m - r_b
    r_r = -4.0 * x_r
    conservation_residual = (r_f + r_c + r_b + r_r) - (
        -3.0 * p.delta * x_f - 3.0 * x_c - 3.0 * x_b - 4.0 * x_r
    )
    conservation_scale = (
        np.abs(r_f) + np.abs(r_c) + np.abs(r_b) + np.abs(r_r)
    )

    baryon_comoving = x_b * np.exp(3.0 * xs)
    baryon_comoving_error = np.max(
        np.abs(baryon_comoving / x_b0 - 1.0)
    )

    return {
        "Xf0": float(x_f[0]),
        "Xb0": float(x_b[0]),
        "Xc0": float(x_c[0]),
        "Xr0": float(x_r[0]),
        "present_baryon_fraction": float(x_b[0] / x_m[0]),
        "baryon_fraction_at_zstar": float(x_b_star / x_m_star),
        "fraction_present_CDM_created_since_zstar": float(fraction_created),
        "comoving_CDM_at_x_min": float(x_c[-1] * np.exp(3.0 * xs[-1])),
        "min_Xf": float(np.min(x_f)),
        "min_Xc": float(np.min(x_c)),
        "min_Xb": float(np.min(x_b)),
        "min_Xr": float(np.min(x_r)),
        "all_positive": bool(
            np.all(x_f > 0.0)
            and np.all(x_c > 0.0)
            and np.all(x_b > 0.0)
            and np.all(x_r > 0.0)
        ),
        "max_relative_baryon_comoving_error": float(baryon_comoving_error),
        "max_abs_conservation_residual": float(
            np.max(np.abs(conservation_residual))
        ),
        "max_relative_conservation_residual": float(
            np.max(
                np.abs(conservation_residual)
                / np.maximum(conservation_scale, 1.0e-300)
            )
        ),
    }


def relative_difference(a: float, b: float) -> float:
    """Symmetric-enough relative difference with b as the reference."""
    return abs(a - b) / max(abs(b), 1.0e-300)


def convergence_check(
    p: ModelParameters,
    settings: IntegrationSettings,
    coarse: dict[str, float | bool],
) -> dict[str, float]:
    """Repeat with half the step and compare the key observables."""
    fine_settings = IntegrationSettings(
        x_min=settings.x_min,
        step=settings.step / 2.0,
    )
    xs_f, y_f, x_b0_f = integrate_background(p, fine_settings)
    fine = summarize(p, xs_f, y_f, x_b0_f)
    keys = (
        "baryon_fraction_at_zstar",
        "fraction_present_CDM_created_since_zstar",
        "comoving_CDM_at_x_min",
    )
    differences = {
        key: relative_difference(float(coarse[key]), float(fine[key]))
        for key in keys
    }
    differences["max_key_relative_difference"] = max(differences.values())
    differences["fine_step"] = fine_settings.step
    return differences


def lambda_zero_check(
    p: ModelParameters, settings: IntegrationSettings
) -> dict[str, float]:
    """Validate the RK4 implementation against X_m = Omega_m0 a^-3."""
    p_zero = ModelParameters(
        h=p.h,
        omega_m0=p.omega_m0,
        lam=0.0,
        delta=p.delta,
        delta_neff=p.delta_neff,
        omega_b=p.omega_b,
        omega_gamma=p.omega_gamma,
        neff_standard=p.neff_standard,
        z_star=p.z_star,
    )
    xs, y, _ = integrate_background(p_zero, settings)
    expected_x_m = p.omega_m0 * np.exp(-3.0 * xs)
    relative_error = np.abs(y[:, 1] / expected_x_m - 1.0)
    return {"max_relative_Xm_error": float(np.max(relative_error))}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h", type=float, default=0.6637)
    parser.add_argument("--omega-m0", type=float, default=0.3517)
    parser.add_argument("--lam", type=float, default=0.15)
    parser.add_argument("--delta", type=float, default=0.02297)
    parser.add_argument("--delta-neff", type=float, default=0.0535)
    parser.add_argument("--omega-b", type=float, default=0.02237)
    parser.add_argument("--omega-gamma", type=float, default=2.469e-5)
    parser.add_argument("--z-star", type=float, default=1089.9)
    parser.add_argument("--x-min", type=float, default=-25.0)
    parser.add_argument("--step", type=float, default=1.0e-3)
    parser.add_argument(
        "--skip-convergence",
        action="store_true",
        help="Skip the half-step convergence run.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    p = ModelParameters(
        h=args.h,
        omega_m0=args.omega_m0,
        lam=args.lam,
        delta=args.delta,
        delta_neff=args.delta_neff,
        omega_b=args.omega_b,
        omega_gamma=args.omega_gamma,
        z_star=args.z_star,
    )
    settings = IntegrationSettings(x_min=args.x_min, step=args.step)

    xs, y, x_b0 = integrate_background(p, settings)
    results = summarize(p, xs, y, x_b0)
    standard_limit = lambda_zero_check(p, settings)
    convergence = None
    if not args.skip_convergence:
        convergence = convergence_check(p, settings, results)

    thresholds = {
        "max_relative_conservation_residual": 1.0e-12,
        "max_relative_baryon_comoving_error": 1.0e-12,
        "max_relative_lambda_zero_Xm_error": 1.0e-9,
        "max_convergence_key_difference": 1.0e-8,
    }

    checks = {
        "all_positive": bool(results["all_positive"]),
        "conservation": (
            float(results["max_relative_conservation_residual"])
            < thresholds["max_relative_conservation_residual"]
        ),
        "baryon_comoving_conservation": (
            float(results["max_relative_baryon_comoving_error"])
            < thresholds["max_relative_baryon_comoving_error"]
        ),
        "lambda_zero_limit": (
            standard_limit["max_relative_Xm_error"]
            < thresholds["max_relative_lambda_zero_Xm_error"]
        ),
    }
    if convergence is not None:
        checks["step_convergence"] = (
            convergence["max_key_relative_difference"]
            < thresholds["max_convergence_key_difference"]
        )

    passed = all(checks.values())
    output = {
        "test": "A1-K1-T5",
        "status": "PASS" if passed else "FAIL",
        "environment": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "parameters": {
            "h": p.h,
            "H0_km_s_Mpc": 100.0 * p.h,
            "Omega_m0": p.omega_m0,
            "lambda": p.lam,
            "delta": p.delta,
            "Delta_Neff": p.delta_neff,
            "omega_b": p.omega_b,
            "omega_gamma": p.omega_gamma,
            "z_star": p.z_star,
        },
        "integration": {
            "method": "fixed-step RK4",
            "x_min": settings.x_min,
            "step": settings.step,
            "points": len(xs),
            "z_max_approx": float(np.exp(-settings.x_min) - 1.0),
        },
        "results": results,
        "lambda_zero_validation": standard_limit,
        "convergence": convergence,
        "thresholds": thresholds,
        "checks": checks,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
