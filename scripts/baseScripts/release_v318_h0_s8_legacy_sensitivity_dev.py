"""DEV implementation of the frozen v3.18 PT1 legacy H0/S8 sensitivity.

This module is not an observational likelihood and does not close K4, G8 or
G9.  The scientific Delta-N_eff/grid cells are evaluated only by the explicit
official entry point in the runner.  ``synthetic_self_test`` uses no
scientific fixture.
"""

from __future__ import annotations

import json
import hashlib
import math
import os
import time
import tempfile
import uuid
from pathlib import Path
from typing import Any, Callable

import numpy as np
from scipy.integrate import quad


CONTRACT_SHA256 = "865033E55783EFC48E8C67A8DF71ACE4798ED0E2DF01172F118894B706D07780"
SHARDED_ADDENDUM_SHA256 = "C2AAB58C565530DEA8CFC6FB7719B9B662706341A399FBAB0CC5736FD1D9C768"
GRID_CELL_ADDENDUM_SHA256 = "DC6E8CC12172BD9AF4805870722AA9516A5A48F3824A05FD7A0D5956513E54F7"
N8000_STAGED_ADDENDUM_SHA256 = "5E2A35D1E1A6EB64D200D4F18488A31849CB16079249DFB8407559A6D3925D42"
N8000_BISECTION_ADDENDUM_SHA256 = "6706912598C536099A1E230D20650D8A792943AF87FB36C283DF4F1449CCB3A1"
C_KM_S = 299792.458
OMEGA_B = 0.02237
OMEGA_M = 0.1430
OMEGA_GAMMA = 2.469e-5
NEFF_STANDARD = 3.046
Z_STAR = 1089.9
X_STAR = -math.log1p(Z_STAR)
H_REF = 0.673
LAMBDA = 0.15
DELTA = 0.02297
SIGMA8_LCDM = 0.811
X_MIN = -7.8
H_BRACKET = (0.55, 0.80)
SCIENCE_DELTA_NEFF = (0.0, 0.02675, 0.0535)
SCIENCE_GRIDS = (2000, 4000, 8000)
SHARD_DELTA_NEFF = {"null": 0.0, "half": 0.02675, "full": 0.0535}
GRID_CELL_SPECS = {
    f"{shard_id}-n{grid_n}": (shard_id, delta_neff, grid_n)
    for shard_id, delta_neff in SHARD_DELTA_NEFF.items()
    for grid_n in SCIENCE_GRIDS
}
GRID_CELL_FILENAMES = {
    cell_id: f"RUN_V318_PT1_H0_S8_CELL_{shard_id.upper()}_N{grid_n}.json"
    for cell_id, (shard_id, _delta_neff, grid_n) in GRID_CELL_SPECS.items()
}
N8000_MODEL_STAGE_FILENAMES = {
    shard_id: f"RUN_V318_PT1_H0_S8_CELL_{shard_id.upper()}_N8000_MODEL_STAGE.json"
    for shard_id in SHARD_DELTA_NEFF
}
N8000_BISECTION_STAGE_FILENAMES = {
    (shard_id, segment): (
        f"RUN_V318_PT1_H0_S8_CELL_{shard_id.upper()}_N8000_BISECT_{segment}.json"
    )
    for shard_id in SHARD_DELTA_NEFF
    for segment in ("A", "B")
}


class DeadlineExceeded(RuntimeError):
    """Internal bounded-runtime failure; never a scientific result."""


class GuardFailure(RuntimeError):
    """Complete execution that cannot satisfy a frozen numerical guard."""


class InvalidBackgroundOrRoot(GuardFailure):
    """Frozen scientific REVIEW condition for background/root validity."""

    verdict = "REVIEW_INVALID_BACKGROUND_OR_ROOT"

    def __init__(self, stage: str, message: str, context: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.stage = stage
        self.context = {} if context is None else _native(context)


class NumericalConvergenceReview(GuardFailure):
    """Frozen scientific REVIEW condition for numerical convergence."""

    verdict = "REVIEW_NUMERICAL_CONVERGENCE"

    def __init__(self, stage: str, message: str, context: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.stage = stage
        self.context = {} if context is None else _native(context)


class Deadline:
    def __init__(self, seconds: float) -> None:
        if not math.isfinite(seconds) or seconds <= 0.0 or seconds > 45.0:
            raise ValueError("max runtime must be finite, positive and <=45 s")
        self.started = time.monotonic()
        self.ends = self.started + seconds

    def check(self) -> None:
        if time.monotonic() > self.ends:
            raise DeadlineExceeded("internal scientific deadline exceeded")

    def elapsed(self) -> float:
        return time.monotonic() - self.started


def _native(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _native(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_native(item) for item in value]
    if isinstance(value, np.ndarray):
        return [_native(item) for item in value.tolist()]
    if isinstance(value, (np.floating, np.integer)):
        value = value.item()
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("non-finite float cannot enter JSON evidence")
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    raise TypeError(f"unsupported JSON evidence type: {type(value).__name__}")


def _non_delta_input_projection(n: int) -> dict[str, Any]:
    return {
        "c_km_s": C_KM_S,
        "omega_b": OMEGA_B,
        "omega_m": OMEGA_M,
        "omega_gamma": OMEGA_GAMMA,
        "N_eff_standard": NEFF_STANDARD,
        "z_star": Z_STAR,
        "h_ref": H_REF,
        "lambda": LAMBDA,
        "delta": DELTA,
        "sigma8_LCDM": SIGMA8_LCDM,
        "x_min": X_MIN,
        "h_bracket": list(H_BRACKET),
        "grid_n": n,
    }


def _projection_fingerprint(projection: dict[str, Any]) -> str:
    canonical = json.dumps(_native(projection), sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest().upper()


def omega_r(delta_neff: float) -> float:
    return OMEGA_GAMMA * (1.0 + 0.2271 * (NEFF_STANDARD + delta_neff))


def _quad_checked(function: Callable[[float], float], low: float, high: float) -> tuple[float, float]:
    result = quad(function, low, high, epsabs=1.0e-12, epsrel=1.0e-11, limit=400)
    value, error = float(result[0]), float(result[1])
    if not math.isfinite(value) or not math.isfinite(error) or value <= 0.0:
        raise NumericalConvergenceReview("adaptive_quadrature", "invalid adaptive quadrature result")
    relative_error = error / abs(value)
    return value, relative_error


def sound_horizon(delta_neff: float, deadline: Deadline) -> tuple[float, float]:
    radiation = omega_r(delta_neff)
    omega_lambda = H_REF**2 - OMEGA_M - radiation
    if omega_lambda <= 0.0:
        raise InvalidBackgroundOrRoot("reference_background", "non-positive reference omega_L")

    def integrand(a: float) -> float:
        rb = 3.0 * OMEGA_B * a / (4.0 * OMEGA_GAMMA)
        hubble = 100.0 * math.sqrt(
            OMEGA_M * a**-3 + radiation * a**-4 + omega_lambda
        )
        return C_KM_S / (math.sqrt(3.0 * (1.0 + rb)) * a**2 * hubble)

    deadline.check()
    value, relative_error = _quad_checked(integrand, 1.0e-9, 1.0 / (1.0 + Z_STAR))
    deadline.check()
    return value, relative_error


def theta_reference(deadline: Deadline) -> tuple[float, dict[str, float]]:
    radiation = omega_r(0.0)
    omega_lambda = H_REF**2 - OMEGA_M - radiation
    if omega_lambda <= 0.0:
        raise InvalidBackgroundOrRoot("theta_reference_background", "non-positive theta-reference omega_L")

    def distance_integrand(a: float) -> float:
        hubble = 100.0 * math.sqrt(
            OMEGA_M * a**-3 + radiation * a**-4 + omega_lambda
        )
        return C_KM_S / (a**2 * hubble)

    rs, rs_error = sound_horizon(0.0, deadline)
    dm, dm_error = _quad_checked(distance_integrand, 1.0 / (1.0 + Z_STAR), 1.0)
    deadline.check()
    return rs / dm, {
        "rs_reference_Mpc": rs,
        "dm_reference_Mpc": dm,
        "rs_quadrature_relative_error": rs_error,
        "dm_quadrature_relative_error": dm_error,
    }


def background(
    h: float,
    omega_m0: float,
    lam: float,
    delta: float,
    delta_neff: float,
    n: int,
    deadline: Deadline,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    radiation0 = omega_r(delta_neff) / h**2
    fuel0 = 1.0 - omega_m0 - radiation0
    if min(fuel0, omega_m0, radiation0) <= 0.0:
        raise InvalidBackgroundOrRoot(
            "present_background_positivity",
            "non-positive present-day background component",
            {"h": h, "omega_m0": omega_m0, "delta_neff": delta_neff},
        )
    xs = np.linspace(0.0, X_MIN, n, dtype=float)
    step = float(xs[1] - xs[0])
    states = np.empty((n, 3), dtype=float)
    states[0] = (fuel0, omega_m0, radiation0)
    minimum = min(fuel0, omega_m0, radiation0)

    def rhs(state: np.ndarray) -> np.ndarray:
        fuel, matter, radiation = (float(item) for item in state)
        total = fuel + matter + radiation
        if min(fuel, matter, radiation, total) <= 0.0:
            raise InvalidBackgroundOrRoot(
                "background_RK4_positivity", "non-positive background during RK4"
            )
        expansion = math.sqrt(total)
        transfer = lam * fuel / expansion
        return np.array(
            (-3.0 * delta * fuel - transfer, -3.0 * matter + transfer, -4.0 * radiation),
            dtype=float,
        )

    for index in range(n - 1):
        if index % 128 == 0:
            deadline.check()
        state = states[index]
        k1 = rhs(state)
        k2 = rhs(state + 0.5 * step * k1)
        k3 = rhs(state + 0.5 * step * k2)
        k4 = rhs(state + step * k3)
        states[index + 1] = state + step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        minimum = min(minimum, float(np.min(states[index + 1])))
    totals = np.sum(states, axis=1)
    if minimum <= 0.0 or float(np.min(totals)) <= 0.0 or not np.all(np.isfinite(states)):
        raise InvalidBackgroundOrRoot(
            "background_trajectory_positivity", "background positivity/finite guard failed"
        )
    return xs, states, np.sqrt(totals), minimum


def solve_inner_matter(
    h: float,
    lam: float,
    delta: float,
    delta_neff: float,
    n: int,
    deadline: Deadline,
) -> dict[str, Any]:
    omega_m0 = 0.30
    target = OMEGA_M * math.exp(-3.0 * X_STAR) / h**2
    last: tuple[np.ndarray, np.ndarray, np.ndarray, float] | None = None
    residual = math.inf
    for iteration in range(1, 41):
        last = background(h, omega_m0, lam, delta, delta_neff, n, deadline)
        xs, states, expansion, minimum = last
        matter_star = float(np.interp(X_STAR, xs[::-1], states[::-1, 1]))
        residual = abs(matter_star / target - 1.0)
        if residual <= 1.0e-10:
            return {
                "omega_m0": omega_m0,
                "xs": xs,
                "states": states,
                "expansion": expansion,
                "minimum_component": minimum,
                "matter_relative_residual": residual,
                "inner_iterations": iteration,
            }
        omega_m0 *= target / matter_star
        if not math.isfinite(omega_m0) or omega_m0 <= 0.0:
            raise InvalidBackgroundOrRoot(
                "inner_matter_physical_domain", "inner matter iteration left physical domain"
            )
    raise NumericalConvergenceReview(
        "inner_matter_convergence",
        f"inner matter residual did not converge: {residual:.6e}",
        {"relative_residual": residual, "max_iterations": 40},
    )


def model_distance(solution: dict[str, Any], h: float) -> float:
    xs = solution["xs"]
    expansion = solution["expansion"]
    mask = xs >= X_STAR
    integral = float(np.trapezoid((np.exp(-xs[mask]) / expansion[mask])[::-1], xs[mask][::-1]))
    value = C_KM_S * integral / (100.0 * h)
    if not math.isfinite(value) or value <= 0.0:
        raise InvalidBackgroundOrRoot("model_distance", "invalid model distance")
    return value


def _anchor_residual(
    h: float,
    *,
    lam: float,
    delta: float,
    delta_neff: float,
    n: int,
    target_distance: float,
    deadline: Deadline,
) -> tuple[float, dict[str, Any], float]:
    solution = solve_inner_matter(h, lam, delta, delta_neff, n, deadline)
    distance = model_distance(solution, h)
    return distance - target_distance, solution, distance


def _advance_bisection(
    *,
    low: float,
    high: float,
    low_residual: float,
    high_residual: float,
    completed_iterations: int,
    additional_iterations: int,
    residual: Callable[[float], tuple[float, dict[str, Any], float]],
    deadline: Deadline,
    stop_width: float = 5.0e-10,
) -> tuple[dict[str, Any], tuple[float, dict[str, Any], float, float] | None]:
    """Advance the frozen midpoint sequence without changing operation order."""
    last: tuple[float, dict[str, Any], float, float] | None = None
    iteration = completed_iterations
    for iteration in range(
        completed_iterations + 1, completed_iterations + additional_iterations + 1
    ):
        deadline.check()
        mid = 0.5 * (low + high)
        mid_residual, solution, distance = residual(mid)
        last = (mid, solution, distance, mid_residual)
        if low_residual * mid_residual > 0.0:
            low, low_residual = mid, mid_residual
        else:
            high, high_residual = mid, mid_residual
        if high - low <= stop_width:
            break
    return {
        "low": low,
        "high": high,
        "low_residual": low_residual,
        "high_residual": high_residual,
        "completed_midpoint_iterations": iteration,
    }, last


def solve_anchor(
    delta_neff: float,
    n: int,
    theta_ref: float,
    deadline: Deadline,
    lam: float = LAMBDA,
    delta: float = DELTA,
) -> dict[str, Any]:
    rs, rs_error = sound_horizon(delta_neff, deadline)
    target_distance = rs / theta_ref

    def residual(h: float) -> tuple[float, dict[str, Any], float]:
        return _anchor_residual(
            h,
            lam=lam,
            delta=delta,
            delta_neff=delta_neff,
            n=n,
            target_distance=target_distance,
            deadline=deadline,
        )

    low, high = H_BRACKET
    low_residual, _, _ = residual(low)
    high_residual, _, _ = residual(high)
    initial_low_residual = low_residual
    initial_high_residual = high_residual
    if low_residual == 0.0 or high_residual == 0.0 or low_residual * high_residual >= 0.0:
        raise InvalidBackgroundOrRoot(
            "H0_root_sign_change",
            "H0 root bracket has no strict sign change",
            {
                "h_low": low,
                "h_high": high,
                "residual_low": low_residual,
                "residual_high": high_residual,
            },
        )
    state, last = _advance_bisection(
        low=low,
        high=high,
        low_residual=low_residual,
        high_residual=high_residual,
        completed_iterations=0,
        additional_iterations=40,
        residual=residual,
        deadline=deadline,
    )
    low = state["low"]
    high = state["high"]
    iteration = state["completed_midpoint_iterations"]
    if last is None or high - low > 5.0e-10:
        raise NumericalConvergenceReview(
            "H0_bisection_convergence",
            "H0 bisection width did not converge",
            {"final_width": high - low, "threshold": 5.0e-10, "max_iterations": 40},
        )
    h, solution, distance, distance_residual = last
    angular_residual = abs((rs / distance) / theta_ref - 1.0)
    return {
        **solution,
        "delta_for_growth": delta,
        "h": h,
        "H0_km_s_Mpc": 100.0 * h,
        "sound_horizon_Mpc": rs,
        "sound_horizon_quadrature_relative_error": rs_error,
        "distance_Mpc": distance,
        "distance_target_Mpc": target_distance,
        "distance_residual_Mpc": distance_residual,
        "theta_relative_residual": angular_residual,
        "root_initial_residual_low": initial_low_residual,
        "root_initial_residual_high": initial_high_residual,
        "root_initial_sign_change": initial_low_residual * initial_high_residual < 0.0,
        "bisection_width": high - low,
        "outer_iterations": iteration,
    }


def growth(solution: dict[str, Any], deadline: Deadline) -> float:
    xs = np.asarray(solution["xs"])[::-1]
    states = np.asarray(solution["states"])[::-1]
    expansion = np.asarray(solution["expansion"])[::-1]
    start = -math.log(1001.0)
    later = xs[xs > start]
    grid = np.concatenate(([start], later))
    matter_fraction = states[:, 1] / expansion**2
    delta = float(solution["delta_for_growth"])
    dln_e = 0.5 * (
        -3.0 * delta * states[:, 0] - 3.0 * states[:, 1] - 4.0 * states[:, 2]
    ) / expansion**2

    def coefficients(x: float) -> tuple[float, float]:
        return (
            float(np.interp(x, xs, dln_e)),
            float(np.interp(x, xs, matter_fraction)),
        )

    state = np.array((math.exp(start), -math.exp(start)), dtype=float)

    def derivative(x: float, value: np.ndarray) -> np.ndarray:
        slope, matter = coefficients(x)
        density, theta = value
        return np.array((-theta, -(2.0 + slope) * theta - 1.5 * matter * density))

    for index in range(len(grid) - 1):
        if index % 256 == 0:
            deadline.check()
        x = float(grid[index])
        step = float(grid[index + 1] - x)
        k1 = derivative(x, state)
        k2 = derivative(x + 0.5 * step, state + 0.5 * step * k1)
        k3 = derivative(x + 0.5 * step, state + 0.5 * step * k2)
        k4 = derivative(x + step, state + step * k3)
        state += step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    if not np.all(np.isfinite(state)) or state[0] <= 0.0:
        raise NumericalConvergenceReview(
            "growth_integration", "growth integration failed finite/positive guard"
        )
    return float(state[0])


def _public_point(solution: dict[str, Any], reference_growth: float, n: int) -> dict[str, Any]:
    model_growth = float(solution["growth"])
    sigma8 = SIGMA8_LCDM * model_growth / reference_growth
    omega_m0 = float(solution["omega_m0"])
    s8 = sigma8 * math.sqrt(omega_m0 / 0.3)
    projection = _non_delta_input_projection(n)
    return {
        "grid_n": n,
        "H0_km_s_Mpc": solution["H0_km_s_Mpc"],
        "Omega_m0": omega_m0,
        "sigma8_conditional": sigma8,
        "S8_conditional": s8,
        "growth_D": model_growth,
        "lcdm_growth_D": reference_growth,
        "sound_horizon_Mpc": solution["sound_horizon_Mpc"],
        "distance_Mpc": solution["distance_Mpc"],
        "theta_relative_residual": solution["theta_relative_residual"],
        "matter_relative_residual": solution["matter_relative_residual"],
        "inner_iterations": solution["inner_iterations"],
        "outer_iterations": solution["outer_iterations"],
        "bisection_width": solution["bisection_width"],
        "quadrature_relative_error": solution["sound_horizon_quadrature_relative_error"],
        "minimum_component": solution["minimum_component"],
        "floor_or_clip_activations": 0,
        "root_initial_sign_change": solution["root_initial_sign_change"],
        "non_delta_input_projection": projection,
        "non_delta_input_fingerprint_sha256": _projection_fingerprint(projection),
    }


def _convergence_diagnostic(coarse: float, medium: float, high: float) -> dict[str, Any]:
    coarse_to_medium_signed = medium - coarse
    medium_to_high_signed = high - medium
    coarse_to_medium_abs = abs(coarse_to_medium_signed)
    medium_to_high_abs = abs(medium_to_high_signed)
    if medium_to_high_abs == 0.0:
        ratio = None
        ratio_status = "UNDEFINED_ZERO_MEDIUM_TO_HIGH_DIFFERENCE"
    else:
        ratio = coarse_to_medium_abs / medium_to_high_abs
        ratio_status = "FINITE"
    return _native({
        "coarse_to_medium_signed": coarse_to_medium_signed,
        "coarse_to_medium_abs": coarse_to_medium_abs,
        "medium_to_high_signed": medium_to_high_signed,
        "medium_to_high_abs": medium_to_high_abs,
        "coarse_to_medium_over_medium_to_high_abs_ratio": ratio,
        "ratio_status": ratio_status,
    })


def _assemble_convergence_diagnostics(
    levels: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    diagnostics: list[dict[str, Any]] = []
    for coarse_point, medium_point, high_point in zip(
        levels["2000"], levels["4000"], levels["8000"], strict=True
    ):
        if not (
            coarse_point["Delta_N_eff"]
            == medium_point["Delta_N_eff"]
            == high_point["Delta_N_eff"]
        ):
            raise ValueError("convergence diagnostic Delta_N_eff ordering mismatch")
        diagnostics.append({
            "Delta_N_eff": high_point["Delta_N_eff"],
            "H0_km_s_Mpc": _convergence_diagnostic(
                coarse_point["H0_km_s_Mpc"],
                medium_point["H0_km_s_Mpc"],
                high_point["H0_km_s_Mpc"],
            ),
            "S8_conditional": _convergence_diagnostic(
                coarse_point["S8_conditional"],
                medium_point["S8_conditional"],
                high_point["S8_conditional"],
            ),
        })
    return _native(diagnostics)


def _build_success_output(
    *,
    runtime_seconds: float,
    theta_ref: float,
    theta_evidence: dict[str, Any],
    levels: dict[str, list[dict[str, Any]]],
    guards: dict[str, bool],
    verdict: str,
) -> dict[str, Any]:
    null, half, full = levels["8000"]
    return _native({
        "schema": "v318_pt1_h0_s8_three_point_legacy_sensitivity_v1",
        "claim": "THREE_POINT_LEGACY_ANCHOR_H0_S8_SENSITIVITY",
        "scope": "legacy_sampled_conditional_not_current_theory_range_or_likelihood",
        "contract_sha256": CONTRACT_SHA256,
        "runtime_seconds": runtime_seconds,
        "theta_reference": theta_ref,
        "theta_reference_evidence": theta_evidence,
        "grid_results": levels,
        "convergence_diagnostics": _assemble_convergence_diagnostics(levels),
        "high_grid_summary": [null, half, full],
        "endpoint_deltas": {
            "H0_full_minus_null_km_s_Mpc": full["H0_km_s_Mpc"] - null["H0_km_s_Mpc"],
            "S8_full_minus_null": full["S8_conditional"] - null["S8_conditional"],
            "H0_material_at_one_decimal": abs(full["H0_km_s_Mpc"] - null["H0_km_s_Mpc"]) >= 0.05,
            "S8_material_at_two_decimals": abs(full["S8_conditional"] - null["S8_conditional"]) >= 0.005,
        },
        "checks": guards,
        "execution_verdict": verdict,
        "nonclaims": [
            "not a confidence or credible interval",
            "not a continuous envelope",
            "not a current v3.18 hard prediction",
            "does not close P5.4, G8 or G9",
            "S8 uses a simplified growth propagator and fixed sigma8_LCDM comparator",
        ],
    })


def _build_shard_success_output(
    *,
    shard_id: str,
    delta_neff: float,
    runtime_seconds: float,
    theta_ref: float,
    theta_evidence: dict[str, Any],
    levels: dict[str, list[dict[str, Any]]],
    guards: dict[str, bool],
) -> dict[str, Any]:
    high_point = levels["8000"][0]
    return _native({
        "schema": "v318_pt1_h0_s8_one_point_shard_v2",
        "claim": "ONE_POINT_SHARD_OF_THREE_POINT_LEGACY_ANCHOR_H0_S8_SENSITIVITY",
        "scope": "legacy_sampled_conditional_shard_not_range_or_likelihood",
        "parent_contract_sha256": CONTRACT_SHA256,
        "sharded_addendum_sha256": SHARDED_ADDENDUM_SHA256,
        "shard_id": shard_id,
        "Delta_N_eff": delta_neff,
        "runtime_seconds": runtime_seconds,
        "theta_reference": theta_ref,
        "theta_reference_evidence": theta_evidence,
        "grid_results": levels,
        "convergence_diagnostics": _assemble_convergence_diagnostics(levels),
        "high_grid_point": high_point,
        "non_delta_input_fingerprint_by_grid": {
            level: points[0]["non_delta_input_fingerprint_sha256"]
            for level, points in levels.items()
        },
        "checks": guards,
        "execution_verdict": (
            "PASS_ONE_POINT_SHARD_NUMERICS"
            if all(guards.values())
            else "REVIEW_NUMERICAL_CONVERGENCE"
        ),
        "full_steam_comparator_applicable": shard_id == "full",
        "nonclaims": [
            "one shard is not the three-point sampled range",
            "not a confidence or credible interval",
            "not a continuous envelope",
            "not a current v3.18 hard prediction",
            "does not close P5.4, G8 or G9",
            "S8 uses a simplified growth propagator and fixed sigma8_LCDM comparator",
        ],
    })


def _build_grid_cell_success_output(
    *,
    cell_id: str,
    shard_id: str,
    delta_neff: float,
    grid_n: int,
    runtime_seconds: float,
    theta_ref: float,
    theta_evidence: dict[str, Any],
    point: dict[str, Any],
    guards: dict[str, bool],
    full_steam_comparator_applicable: bool,
) -> dict[str, Any]:
    return _native({
        "schema": "v318_pt1_h0_s8_grid_cell_v3",
        "claim": "GRID_CELL_OF_THREE_POINT_LEGACY_ANCHOR_H0_S8_SENSITIVITY",
        "scope": "legacy_sampled_conditional_grid_cell_not_range_or_likelihood",
        "parent_contract_sha256": CONTRACT_SHA256,
        "sharded_addendum_sha256": SHARDED_ADDENDUM_SHA256,
        "grid_cell_addendum_sha256": GRID_CELL_ADDENDUM_SHA256,
        "cell_id": cell_id,
        "shard_id": shard_id,
        "Delta_N_eff": delta_neff,
        "grid_n": grid_n,
        "runtime_seconds": runtime_seconds,
        "theta_reference": theta_ref,
        "theta_reference_evidence": theta_evidence,
        "point": point,
        "non_delta_input_fingerprint_sha256": point[
            "non_delta_input_fingerprint_sha256"
        ],
        "checks": guards,
        "execution_verdict": (
            "PASS_GRID_CELL_INTRINSIC"
            if all(guards.values())
            else "REVIEW_NUMERICAL_CONVERGENCE"
        ),
        "grid_convergence_status": "DEFERRED_CROSS_CELL",
        "full_steam_comparator_applicable": full_steam_comparator_applicable,
        "nonclaims": [
            "one grid cell is not a convergence result or sampled range",
            "not a confidence or credible interval",
            "not a continuous envelope",
            "not a current v3.18 hard prediction",
            "does not close P5.4, G8 or G9",
            "S8 uses a simplified growth propagator and fixed sigma8_LCDM comparator",
        ],
    })


def _point_intrinsic_guards(point: dict[str, Any]) -> dict[str, bool]:
    key = f"dneff_{point['Delta_N_eff']}_n_{point['grid_n']}"
    return {
        f"{key}_theta": point["theta_relative_residual"] <= 1.0e-8,
        f"{key}_matter": point["matter_relative_residual"] <= 1.0e-10,
        f"{key}_quadrature": point["quadrature_relative_error"] <= 1.0e-8,
        f"{key}_positive": point["minimum_component"] > 0.0,
        f"{key}_no_floor": point["floor_or_clip_activations"] == 0,
        f"{key}_root_sign_change": point["root_initial_sign_change"],
        f"{key}_projection_rehash": (
            point["non_delta_input_fingerprint_sha256"]
            == _projection_fingerprint(point["non_delta_input_projection"])
        ),
    }


def _require_exact_sha(actual: str, expected: str, label: str) -> None:
    if actual.upper() != expected.upper():
        raise ValueError(f"{label} SHA256 mismatch: expected {expected}, got {actual}")


REFERENCE_DIAGNOSTIC_KEYS = {
    "H0_km_s_Mpc",
    "sound_horizon_Mpc",
    "distance_Mpc",
    "distance_target_Mpc",
    "distance_residual_Mpc",
    "theta_relative_residual",
    "matter_relative_residual",
    "quadrature_relative_error",
    "minimum_component",
    "root_initial_residual_low",
    "root_initial_residual_high",
    "root_initial_sign_change",
    "bisection_width",
    "inner_iterations",
    "outer_iterations",
}


def _n8000_reference_frozen_input_ledger() -> dict[str, Any]:
    return {
        **_frozen_input_ledger(),
        "stage_parameters": {
            "lambda": 0.0,
            "delta": 0.0,
            "Delta_N_eff": 0.0,
            "grid_n": 8000,
        },
    }


def _n8000_model_frozen_input_ledger(delta_neff: float) -> dict[str, Any]:
    return {
        **_frozen_input_ledger(),
        "stage_parameters": {
            "lambda": LAMBDA,
            "delta": DELTA,
            "Delta_N_eff": delta_neff,
            "grid_n": 8000,
        },
    }


def _build_n8000_reference_stage_success_output(
    *,
    runtime_seconds: float,
    theta_ref: float,
    theta_evidence: dict[str, Any],
    reference_growth: float,
    diagnostics: dict[str, Any],
    checks: dict[str, bool],
) -> dict[str, Any]:
    if set(diagnostics) != REFERENCE_DIAGNOSTIC_KEYS:
        raise ValueError("reference diagnostics do not match the frozen complete evidence schema")
    return _native({
        "schema": "v318_pt1_h0_s8_n8000_reference_stage_v4",
        "claim": "TECHNICAL_REFERENCE_STAGE_FOR_GRID_CELL_N8000",
        "scope": "legacy_execution_stage_not_scientific_cell_or_range",
        "grid_n": 8000,
        "v3_addendum_sha256": GRID_CELL_ADDENDUM_SHA256,
        "v4_addendum_sha256": N8000_STAGED_ADDENDUM_SHA256,
        "runtime_seconds": runtime_seconds,
        "theta_reference": theta_ref,
        "theta_reference_evidence": theta_evidence,
        "reference_growth_D": reference_growth,
        "reference_diagnostics": diagnostics,
        "frozen_input_ledger": _n8000_reference_frozen_input_ledger(),
        "checks": checks,
        "execution_verdict": (
            "PASS_N8000_REFERENCE_STAGE_INTRINSIC"
            if all(checks.values())
            else "REVIEW_NUMERICAL_CONVERGENCE"
        ),
        "nonclaims": [
            "not a model Delta-N_eff point",
            "not a convergence result or sampled range",
            "does not close P5.4, G8 or G9",
        ],
    })


def run_n8000_reference_stage(max_runtime_seconds: float) -> dict[str, Any]:
    deadline = Deadline(max_runtime_seconds)
    theta_ref, theta_evidence = theta_reference(deadline)
    if max(
        theta_evidence["rs_quadrature_relative_error"],
        theta_evidence["dm_quadrature_relative_error"],
    ) > 1.0e-8:
        raise NumericalConvergenceReview(
            "reference_quadrature_threshold",
            "reference adaptive quadrature error exceeds threshold",
            theta_evidence,
        )
    reference = solve_anchor(0.0, 8000, theta_ref, deadline, lam=0.0, delta=0.0)
    reference_growth = growth(reference, deadline)
    diagnostics = {
        "H0_km_s_Mpc": reference["H0_km_s_Mpc"],
        "sound_horizon_Mpc": reference["sound_horizon_Mpc"],
        "distance_Mpc": reference["distance_Mpc"],
        "distance_target_Mpc": reference["distance_target_Mpc"],
        "distance_residual_Mpc": reference["distance_residual_Mpc"],
        "theta_relative_residual": reference["theta_relative_residual"],
        "matter_relative_residual": reference["matter_relative_residual"],
        "quadrature_relative_error": reference["sound_horizon_quadrature_relative_error"],
        "minimum_component": reference["minimum_component"],
        "root_initial_residual_low": reference["root_initial_residual_low"],
        "root_initial_residual_high": reference["root_initial_residual_high"],
        "root_initial_sign_change": reference["root_initial_sign_change"],
        "bisection_width": reference["bisection_width"],
        "inner_iterations": reference["inner_iterations"],
        "outer_iterations": reference["outer_iterations"],
    }
    checks = {
        "reference_theta": diagnostics["theta_relative_residual"] <= 1.0e-8,
        "reference_matter": diagnostics["matter_relative_residual"] <= 1.0e-10,
        "reference_quadrature": diagnostics["quadrature_relative_error"] <= 1.0e-8,
        "reference_positive": diagnostics["minimum_component"] > 0.0,
        "reference_no_floor": True,
        "reference_root_sign_change": diagnostics["root_initial_sign_change"],
    }
    return _build_n8000_reference_stage_success_output(
        runtime_seconds=deadline.elapsed(),
        theta_ref=theta_ref,
        theta_evidence=theta_evidence,
        reference_growth=reference_growth,
        diagnostics=diagnostics,
        checks=checks,
    )


def _validate_n8000_reference_stage(
    reference_payload: dict[str, Any],
    reference_actual_sha256: str,
    reference_expected_sha256: str,
) -> None:
    _require_exact_sha(reference_actual_sha256, reference_expected_sha256, "reference stage")
    if (
        reference_payload.get("schema") != "v318_pt1_h0_s8_n8000_reference_stage_v4"
        or reference_payload.get("execution_verdict")
        != "PASS_N8000_REFERENCE_STAGE_INTRINSIC"
        or reference_payload.get("grid_n") != 8000
        or reference_payload.get("v3_addendum_sha256") != GRID_CELL_ADDENDUM_SHA256
        or reference_payload.get("v4_addendum_sha256") != N8000_STAGED_ADDENDUM_SHA256
    ):
        raise ValueError("reference stage schema/lineage/verdict mismatch")


def _bisection_segment_payload(
    *,
    shard_id: str,
    delta_neff: float,
    segment: str,
    reference_actual_sha256: str,
    predecessor_sha256: str | None,
    theta_reference: float,
    reference_growth: float,
    sound_horizon_mpc: float,
    quadrature_relative_error: float,
    target_distance_mpc: float,
    initial_low_residual: float,
    initial_high_residual: float,
    state: dict[str, Any],
    last: tuple[float, dict[str, Any], float, float],
    runtime_seconds: float,
) -> dict[str, Any]:
    expected_iterations = {"A": 10, "B": 20}[segment]
    width = float(state["high"] - state["low"])
    checks = {
        "finite_state": all(
            math.isfinite(float(value))
            for value in (
                state["low"], state["high"], state["low_residual"],
                state["high_residual"], last[0], last[2], last[3],
            )
        ),
        "strict_bracket_sign_change": (
            float(state["low_residual"]) * float(state["high_residual"]) < 0.0
        ),
        "completed_iteration_count_exact": (
            state["completed_midpoint_iterations"] == expected_iterations
        ),
        "positive_bracket_width": width > 0.0,
    }
    return _native({
        "schema": "v318_pt1_h0_s8_n8000_bisection_segment_v5",
        "claim": "TECHNICAL_BISECTION_CONTINUATION_FOR_GRID_CELL_N8000",
        "scope": "legacy_execution_segment_not_final_model_cell_or_range",
        "shard_id": shard_id,
        "Delta_N_eff": delta_neff,
        "grid_n": 8000,
        "segment": segment,
        "v3_addendum_sha256": GRID_CELL_ADDENDUM_SHA256,
        "v4_addendum_sha256": N8000_STAGED_ADDENDUM_SHA256,
        "v5_addendum_sha256": N8000_BISECTION_ADDENDUM_SHA256,
        "reference_stage_sha256": reference_actual_sha256.upper(),
        "theta_reference": theta_reference,
        "reference_growth_D": reference_growth,
        "frozen_input_ledger": _n8000_model_frozen_input_ledger(delta_neff),
        "predecessor_segment_sha256": (
            None if predecessor_sha256 is None else predecessor_sha256.upper()
        ),
        "sound_horizon_Mpc": sound_horizon_mpc,
        "sound_horizon_quadrature_relative_error": quadrature_relative_error,
        "distance_target_Mpc": target_distance_mpc,
        "root_initial_residual_low": initial_low_residual,
        "root_initial_residual_high": initial_high_residual,
        "bisection_state": state,
        "last_evaluation": {
            "h": last[0], "distance_Mpc": last[2], "distance_residual_Mpc": last[3]
        },
        "runtime_seconds": runtime_seconds,
        "checks": checks,
        "execution_verdict": (
            "PASS_N8000_BISECTION_SEGMENT_INTRINSIC"
            if all(checks.values())
            else "REVIEW_NUMERICAL_CONVERGENCE"
        ),
        "nonclaims": [
            "segment is not an H0 or S8 result",
            "not a convergence result or sampled range",
            "does not close P5.4, G8 or G9",
        ],
    })


def _validate_n8000_bisection_predecessor(
    *,
    payload: dict[str, Any],
    actual_sha256: str,
    expected_sha256: str,
    shard_id: str,
    delta_neff: float,
    expected_segment: str,
    expected_iterations: int,
    reference_actual_sha256: str,
    reference_payload: dict[str, Any],
) -> None:
    _require_exact_sha(actual_sha256, expected_sha256, f"bisection segment {expected_segment}")
    state = payload.get("bisection_state", {})
    if (
        payload.get("schema") != "v318_pt1_h0_s8_n8000_bisection_segment_v5"
        or payload.get("execution_verdict")
        != "PASS_N8000_BISECTION_SEGMENT_INTRINSIC"
        or payload.get("v3_addendum_sha256") != GRID_CELL_ADDENDUM_SHA256
        or payload.get("v4_addendum_sha256") != N8000_STAGED_ADDENDUM_SHA256
        or payload.get("v5_addendum_sha256") != N8000_BISECTION_ADDENDUM_SHA256
        or payload.get("reference_stage_sha256") != reference_actual_sha256.upper()
        or payload.get("theta_reference") != float(reference_payload["theta_reference"])
        or payload.get("reference_growth_D")
        != float(reference_payload["reference_growth_D"])
        or payload.get("frozen_input_ledger")
        != _n8000_model_frozen_input_ledger(delta_neff)
        or payload.get("shard_id") != shard_id
        or payload.get("Delta_N_eff") != delta_neff
        or payload.get("grid_n") != 8000
        or payload.get("segment") != expected_segment
        or state.get("completed_midpoint_iterations") != expected_iterations
    ):
        raise ValueError("bisection predecessor schema/lineage/verdict/mapping mismatch")


def run_n8000_bisection_stage(
    *,
    shard_id: str,
    segment: str,
    reference_payload: dict[str, Any],
    reference_actual_sha256: str,
    reference_expected_sha256: str,
    max_runtime_seconds: float,
    predecessor_payload: dict[str, Any] | None = None,
    predecessor_actual_sha256: str | None = None,
    predecessor_expected_sha256: str | None = None,
) -> dict[str, Any]:
    if shard_id not in SHARD_DELTA_NEFF or segment not in ("A", "B", "C"):
        raise ValueError("unknown frozen n8000 bisection shard/segment")
    _validate_n8000_reference_stage(
        reference_payload, reference_actual_sha256, reference_expected_sha256
    )
    deadline = Deadline(max_runtime_seconds)
    delta_neff = SHARD_DELTA_NEFF[shard_id]
    theta_ref = float(reference_payload["theta_reference"])

    if segment == "A":
        if any(
            value is not None
            for value in (
                predecessor_payload, predecessor_actual_sha256, predecessor_expected_sha256
            )
        ):
            raise ValueError("segment A must not receive a predecessor")
        rs, rs_error = sound_horizon(delta_neff, deadline)
        target_distance = rs / theta_ref
        low, high = H_BRACKET

        def residual(h: float) -> tuple[float, dict[str, Any], float]:
            return _anchor_residual(
                h, lam=LAMBDA, delta=DELTA, delta_neff=delta_neff, n=8000,
                target_distance=target_distance, deadline=deadline,
            )

        low_residual, _, _ = residual(low)
        high_residual, _, _ = residual(high)
        initial_low_residual = low_residual
        initial_high_residual = high_residual
        if low_residual == 0.0 or high_residual == 0.0 or low_residual * high_residual >= 0.0:
            raise InvalidBackgroundOrRoot(
                "H0_root_sign_change", "H0 root bracket has no strict sign change",
                {"h_low": low, "h_high": high, "residual_low": low_residual,
                 "residual_high": high_residual},
            )
        state, last = _advance_bisection(
            low=low, high=high, low_residual=low_residual,
            high_residual=high_residual, completed_iterations=0,
            additional_iterations=10, residual=residual, deadline=deadline,
        )
        predecessor_sha = None
    else:
        if (
            predecessor_payload is None
            or predecessor_actual_sha256 is None
            or predecessor_expected_sha256 is None
        ):
            raise ValueError(f"segment {segment} requires an exact predecessor")
        expected_predecessor = "A" if segment == "B" else "B"
        expected_iterations = 10 if segment == "B" else 20
        _validate_n8000_bisection_predecessor(
            payload=predecessor_payload,
            actual_sha256=predecessor_actual_sha256,
            expected_sha256=predecessor_expected_sha256,
            shard_id=shard_id,
            delta_neff=delta_neff,
            expected_segment=expected_predecessor,
            expected_iterations=expected_iterations,
            reference_actual_sha256=reference_actual_sha256,
            reference_payload=reference_payload,
        )
        rs = float(predecessor_payload["sound_horizon_Mpc"])
        rs_error = float(predecessor_payload["sound_horizon_quadrature_relative_error"])
        target_distance = float(predecessor_payload["distance_target_Mpc"])
        initial_low_residual = float(predecessor_payload["root_initial_residual_low"])
        initial_high_residual = float(predecessor_payload["root_initial_residual_high"])
        prior = predecessor_payload["bisection_state"]

        def residual(h: float) -> tuple[float, dict[str, Any], float]:
            return _anchor_residual(
                h, lam=LAMBDA, delta=DELTA, delta_neff=delta_neff, n=8000,
                target_distance=target_distance, deadline=deadline,
            )

        state, last = _advance_bisection(
            low=float(prior["low"]), high=float(prior["high"]),
            low_residual=float(prior["low_residual"]),
            high_residual=float(prior["high_residual"]),
            completed_iterations=expected_iterations,
            additional_iterations=10 if segment == "B" else 9,
            residual=residual, deadline=deadline,
        )
        predecessor_sha = predecessor_actual_sha256

    if last is None:
        raise NumericalConvergenceReview(
            "H0_bisection_segment_empty", "bisection segment produced no midpoint"
        )
    if segment != "C":
        return _bisection_segment_payload(
            shard_id=shard_id, delta_neff=delta_neff, segment=segment,
            reference_actual_sha256=reference_actual_sha256,
            predecessor_sha256=predecessor_sha,
            theta_reference=theta_ref,
            reference_growth=float(reference_payload["reference_growth_D"]),
            sound_horizon_mpc=rs, quadrature_relative_error=rs_error,
            target_distance_mpc=target_distance,
            initial_low_residual=initial_low_residual,
            initial_high_residual=initial_high_residual,
            state=state, last=last, runtime_seconds=deadline.elapsed(),
        )

    if (
        state["completed_midpoint_iterations"] != 29
        or state["high"] - state["low"] > 5.0e-10
    ):
        raise NumericalConvergenceReview(
            "H0_bisection_convergence", "H0 bisection width did not converge after 29 steps",
            {"final_width": state["high"] - state["low"], "threshold": 5.0e-10,
             "completed_midpoint_iterations": state["completed_midpoint_iterations"]},
        )
    h, solution, distance, distance_residual = last
    solution.update({
        "delta_for_growth": DELTA,
        "h": h,
        "H0_km_s_Mpc": 100.0 * h,
        "sound_horizon_Mpc": rs,
        "sound_horizon_quadrature_relative_error": rs_error,
        "distance_Mpc": distance,
        "distance_target_Mpc": target_distance,
        "distance_residual_Mpc": distance_residual,
        "theta_relative_residual": abs((rs / distance) / theta_ref - 1.0),
        "root_initial_residual_low": initial_low_residual,
        "root_initial_residual_high": initial_high_residual,
        "root_initial_sign_change": initial_low_residual * initial_high_residual < 0.0,
        "bisection_width": state["high"] - state["low"],
        "outer_iterations": state["completed_midpoint_iterations"],
    })
    solution["growth"] = growth(solution, deadline)
    point = {
        "Delta_N_eff": delta_neff,
        **_public_point(solution, float(reference_payload["reference_growth_D"]), 8000),
    }
    checks = _point_intrinsic_guards(point)
    checks["completed_midpoint_iterations_exact"] = (
        state["completed_midpoint_iterations"] == 29
    )
    return _native({
        "schema": "v318_pt1_h0_s8_n8000_model_stage_v4",
        "claim": "TECHNICAL_MODEL_STAGE_FOR_GRID_CELL_N8000",
        "scope": "legacy_execution_stage_not_final_cell_or_range",
        "shard_id": shard_id,
        "Delta_N_eff": delta_neff,
        "grid_n": 8000,
        "v3_addendum_sha256": GRID_CELL_ADDENDUM_SHA256,
        "v4_addendum_sha256": N8000_STAGED_ADDENDUM_SHA256,
        "v5_addendum_sha256": N8000_BISECTION_ADDENDUM_SHA256,
        "reference_stage_sha256": reference_actual_sha256.upper(),
        "theta_reference": theta_ref,
        "reference_growth_D": float(reference_payload["reference_growth_D"]),
        "frozen_input_ledger": _n8000_model_frozen_input_ledger(delta_neff),
        "predecessor_segment_sha256": predecessor_actual_sha256.upper(),
        "completed_midpoint_iterations": state["completed_midpoint_iterations"],
        "runtime_seconds": deadline.elapsed(),
        "point": point,
        "checks": checks,
        "execution_verdict": (
            "PASS_N8000_MODEL_STAGE_INTRINSIC"
            if all(checks.values()) else "REVIEW_NUMERICAL_CONVERGENCE"
        ),
        "nonclaims": [
            "stage raw is not the final V3 grid cell",
            "not a convergence result or sampled range",
            "does not close P5.4, G8 or G9",
        ],
    })


def run_n8000_model_stage(
    shard_id: str,
    reference_payload: dict[str, Any],
    reference_actual_sha256: str,
    reference_expected_sha256: str,
    max_runtime_seconds: float,
) -> dict[str, Any]:
    if shard_id not in SHARD_DELTA_NEFF:
        raise ValueError(f"unknown frozen n8000 model shard: {shard_id}")
    _require_exact_sha(reference_actual_sha256, reference_expected_sha256, "reference stage")
    if (
        reference_payload.get("schema") != "v318_pt1_h0_s8_n8000_reference_stage_v4"
        or reference_payload.get("execution_verdict")
        != "PASS_N8000_REFERENCE_STAGE_INTRINSIC"
        or reference_payload.get("grid_n") != 8000
        or reference_payload.get("v3_addendum_sha256") != GRID_CELL_ADDENDUM_SHA256
        or reference_payload.get("v4_addendum_sha256") != N8000_STAGED_ADDENDUM_SHA256
    ):
        raise ValueError("reference stage schema/lineage/verdict mismatch")
    deadline = Deadline(max_runtime_seconds)
    delta_neff = SHARD_DELTA_NEFF[shard_id]
    solution = solve_anchor(
        delta_neff, 8000, float(reference_payload["theta_reference"]), deadline
    )
    solution["growth"] = growth(solution, deadline)
    point = {
        "Delta_N_eff": delta_neff,
        **_public_point(
            solution, float(reference_payload["reference_growth_D"]), 8000
        ),
    }
    checks = _point_intrinsic_guards(point)
    return _native({
        "schema": "v318_pt1_h0_s8_n8000_model_stage_v4",
        "claim": "TECHNICAL_MODEL_STAGE_FOR_GRID_CELL_N8000",
        "scope": "legacy_execution_stage_not_final_cell_or_range",
        "shard_id": shard_id,
        "Delta_N_eff": delta_neff,
        "grid_n": 8000,
        "v3_addendum_sha256": GRID_CELL_ADDENDUM_SHA256,
        "v4_addendum_sha256": N8000_STAGED_ADDENDUM_SHA256,
        "reference_stage_sha256": reference_actual_sha256.upper(),
        "runtime_seconds": deadline.elapsed(),
        "point": point,
        "checks": checks,
        "execution_verdict": (
            "PASS_N8000_MODEL_STAGE_INTRINSIC"
            if all(checks.values())
            else "REVIEW_NUMERICAL_CONVERGENCE"
        ),
        "nonclaims": [
            "stage raw is not the final V3 grid cell",
            "not a convergence result or sampled range",
            "does not close P5.4, G8 or G9",
        ],
    })


def _build_staged_grid_cell_from_validated(
    *,
    cell_id: str,
    shard_id: str,
    delta_neff: float,
    grid_n: int,
    theta_ref: float,
    theta_evidence: dict[str, Any],
    point: dict[str, Any],
    reference_sha_match: bool,
    model_sha_match: bool,
    runtime_seconds: float,
    comparator_applicable: bool,
) -> dict[str, Any]:
    guards = _point_intrinsic_guards(point)
    guards["reference_stage_sha256_match"] = reference_sha_match
    guards["model_stage_sha256_match"] = model_sha_match
    if comparator_applicable:
        guards["full_steam_H0_comparator"] = (
            abs(point["H0_km_s_Mpc"] - 66.37) <= 0.05
        )
        guards["full_steam_S8_comparator"] = (
            abs(point["S8_conditional"] - 0.8745) <= 0.002
        )
    return _build_grid_cell_success_output(
        cell_id=cell_id,
        shard_id=shard_id,
        delta_neff=delta_neff,
        grid_n=grid_n,
        runtime_seconds=runtime_seconds,
        theta_ref=theta_ref,
        theta_evidence=theta_evidence,
        point=point,
        guards=guards,
        full_steam_comparator_applicable=comparator_applicable,
    )


def aggregate_n8000_cell(
    shard_id: str,
    reference_payload: dict[str, Any],
    reference_actual_sha256: str,
    reference_expected_sha256: str,
    model_payload: dict[str, Any],
    model_actual_sha256: str,
    model_expected_sha256: str,
    max_runtime_seconds: float,
) -> dict[str, Any]:
    if shard_id not in SHARD_DELTA_NEFF:
        raise ValueError(f"unknown frozen n8000 aggregate shard: {shard_id}")
    deadline = Deadline(max_runtime_seconds)
    _require_exact_sha(reference_actual_sha256, reference_expected_sha256, "reference stage")
    _require_exact_sha(model_actual_sha256, model_expected_sha256, "model stage")
    delta_neff = SHARD_DELTA_NEFF[shard_id]
    if (
        reference_payload.get("schema") != "v318_pt1_h0_s8_n8000_reference_stage_v4"
        or reference_payload.get("execution_verdict")
        != "PASS_N8000_REFERENCE_STAGE_INTRINSIC"
        or reference_payload.get("v4_addendum_sha256") != N8000_STAGED_ADDENDUM_SHA256
        or reference_payload.get("v3_addendum_sha256") != GRID_CELL_ADDENDUM_SHA256
        or reference_payload.get("grid_n") != 8000
    ):
        raise ValueError("reference stage schema/lineage/verdict mismatch")
    if (
        model_payload.get("schema") != "v318_pt1_h0_s8_n8000_model_stage_v4"
        or model_payload.get("execution_verdict") != "PASS_N8000_MODEL_STAGE_INTRINSIC"
        or model_payload.get("v4_addendum_sha256") != N8000_STAGED_ADDENDUM_SHA256
        or model_payload.get("v3_addendum_sha256") != GRID_CELL_ADDENDUM_SHA256
        or model_payload.get("v5_addendum_sha256") != N8000_BISECTION_ADDENDUM_SHA256
        or model_payload.get("reference_stage_sha256") != reference_actual_sha256.upper()
        or model_payload.get("theta_reference") != float(reference_payload["theta_reference"])
        or model_payload.get("reference_growth_D")
        != float(reference_payload["reference_growth_D"])
        or model_payload.get("frozen_input_ledger")
        != _n8000_model_frozen_input_ledger(delta_neff)
        or model_payload.get("completed_midpoint_iterations") != 29
        or model_payload.get("shard_id") != shard_id
        or model_payload.get("Delta_N_eff") != delta_neff
        or model_payload.get("grid_n") != 8000
    ):
        raise ValueError("model stage schema/lineage/verdict/mapping mismatch")
    point = model_payload["point"]
    if point.get("Delta_N_eff") != delta_neff or point.get("grid_n") != 8000:
        raise ValueError("model point mapping mismatch")
    deadline.check()
    return _build_staged_grid_cell_from_validated(
        cell_id=f"{shard_id}-n8000",
        shard_id=shard_id,
        delta_neff=delta_neff,
        grid_n=8000,
        theta_ref=float(reference_payload["theta_reference"]),
        theta_evidence=reference_payload["theta_reference_evidence"],
        point=point,
        reference_sha_match=True,
        model_sha_match=True,
        runtime_seconds=deadline.elapsed(),
        comparator_applicable=shard_id == "full",
    )


def run_grid_cell(cell_id: str, max_runtime_seconds: float) -> dict[str, Any]:
    if cell_id not in GRID_CELL_SPECS:
        raise ValueError(f"unknown frozen grid cell: {cell_id}")
    shard_id, delta_neff, grid_n = GRID_CELL_SPECS[cell_id]
    deadline = Deadline(max_runtime_seconds)
    theta_ref, theta_evidence = theta_reference(deadline)
    if max(
        theta_evidence["rs_quadrature_relative_error"],
        theta_evidence["dm_quadrature_relative_error"],
    ) > 1.0e-8:
        raise NumericalConvergenceReview(
            "reference_quadrature_threshold",
            "reference adaptive quadrature error exceeds threshold",
            theta_evidence,
        )

    reference = solve_anchor(0.0, grid_n, theta_ref, deadline, lam=0.0, delta=0.0)
    reference["growth"] = growth(reference, deadline)
    solution = solve_anchor(delta_neff, grid_n, theta_ref, deadline)
    solution["growth"] = growth(solution, deadline)
    point = {
        "Delta_N_eff": delta_neff,
        **_public_point(solution, float(reference["growth"]), grid_n),
    }
    guards = _point_intrinsic_guards(point)
    comparator_applicable = cell_id == "full-n8000"
    if comparator_applicable:
        guards["full_steam_H0_comparator"] = (
            abs(point["H0_km_s_Mpc"] - 66.37) <= 0.05
        )
        guards["full_steam_S8_comparator"] = (
            abs(point["S8_conditional"] - 0.8745) <= 0.002
        )
    return _build_grid_cell_success_output(
        cell_id=cell_id,
        shard_id=shard_id,
        delta_neff=delta_neff,
        grid_n=grid_n,
        runtime_seconds=deadline.elapsed(),
        theta_ref=theta_ref,
        theta_evidence=theta_evidence,
        point=point,
        guards=guards,
        full_steam_comparator_applicable=comparator_applicable,
    )


def run_one_point(shard_id: str, max_runtime_seconds: float) -> dict[str, Any]:
    if shard_id not in SHARD_DELTA_NEFF:
        raise ValueError(f"unknown frozen shard_id: {shard_id}")
    delta_neff = SHARD_DELTA_NEFF[shard_id]
    deadline = Deadline(max_runtime_seconds)
    theta_ref, theta_evidence = theta_reference(deadline)
    if max(
        theta_evidence["rs_quadrature_relative_error"],
        theta_evidence["dm_quadrature_relative_error"],
    ) > 1.0e-8:
        raise NumericalConvergenceReview(
            "reference_quadrature_threshold",
            "reference adaptive quadrature error exceeds threshold",
            theta_evidence,
        )
    levels: dict[str, list[dict[str, Any]]] = {}
    for n in SCIENCE_GRIDS:
        reference = solve_anchor(0.0, n, theta_ref, deadline, lam=0.0, delta=0.0)
        reference["growth"] = growth(reference, deadline)
        solution = solve_anchor(delta_neff, n, theta_ref, deadline)
        solution["growth"] = growth(solution, deadline)
        levels[str(n)] = [{
            "Delta_N_eff": delta_neff,
            **_public_point(solution, float(reference["growth"]), n),
        }]

    guards: dict[str, bool] = {}
    for level_points in levels.values():
        point = level_points[0]
        key = f"dneff_{point['Delta_N_eff']}_n_{point['grid_n']}"
        guards[f"{key}_theta"] = point["theta_relative_residual"] <= 1.0e-8
        guards[f"{key}_matter"] = point["matter_relative_residual"] <= 1.0e-10
        guards[f"{key}_quadrature"] = point["quadrature_relative_error"] <= 1.0e-8
        guards[f"{key}_positive"] = point["minimum_component"] > 0.0
        guards[f"{key}_no_floor"] = point["floor_or_clip_activations"] == 0
        guards[f"{key}_root_sign_change"] = point["root_initial_sign_change"]
        guards[f"{key}_projection_rehash"] = (
            point["non_delta_input_fingerprint_sha256"]
            == _projection_fingerprint(point["non_delta_input_projection"])
        )
    medium = levels["4000"][0]
    high = levels["8000"][0]
    guards["H0_medium_high_grid"] = (
        abs(high["H0_km_s_Mpc"] - medium["H0_km_s_Mpc"]) <= 0.005
    )
    guards["S8_medium_high_grid"] = (
        abs(high["S8_conditional"] - medium["S8_conditional"]) <= 0.0005
    )
    if shard_id == "full":
        guards["full_steam_H0_comparator"] = abs(high["H0_km_s_Mpc"] - 66.37) <= 0.05
        guards["full_steam_S8_comparator"] = abs(high["S8_conditional"] - 0.8745) <= 0.002
    return _build_shard_success_output(
        shard_id=shard_id,
        delta_neff=delta_neff,
        runtime_seconds=deadline.elapsed(),
        theta_ref=theta_ref,
        theta_evidence=theta_evidence,
        levels=levels,
        guards=guards,
    )


def run_three_point(max_runtime_seconds: float) -> dict[str, Any]:
    deadline = Deadline(max_runtime_seconds)
    theta_ref, theta_evidence = theta_reference(deadline)
    if max(theta_evidence["rs_quadrature_relative_error"], theta_evidence["dm_quadrature_relative_error"]) > 1.0e-8:
        raise NumericalConvergenceReview(
            "reference_quadrature_threshold",
            "reference adaptive quadrature error exceeds threshold",
            theta_evidence,
        )
    levels: dict[str, list[dict[str, Any]]] = {}
    for n in SCIENCE_GRIDS:
        reference = solve_anchor(0.0, n, theta_ref, deadline, lam=0.0, delta=0.0)
        reference["growth"] = growth(reference, deadline)
        points: list[dict[str, Any]] = []
        for delta_neff in SCIENCE_DELTA_NEFF:
            solution = solve_anchor(delta_neff, n, theta_ref, deadline)
            solution["growth"] = growth(solution, deadline)
            points.append({
                "Delta_N_eff": delta_neff,
                **_public_point(solution, float(reference["growth"]), n),
            })
        levels[str(n)] = points

    guards: dict[str, bool] = {}
    for level_points in levels.values():
        for point in level_points:
            key = f"dneff_{point['Delta_N_eff']}_n_{point['grid_n']}"
            guards[f"{key}_theta"] = point["theta_relative_residual"] <= 1.0e-8
            guards[f"{key}_matter"] = point["matter_relative_residual"] <= 1.0e-10
            guards[f"{key}_quadrature"] = point["quadrature_relative_error"] <= 1.0e-8
            guards[f"{key}_positive"] = point["minimum_component"] > 0.0
            guards[f"{key}_no_floor"] = point["floor_or_clip_activations"] == 0
            guards[f"{key}_root_sign_change"] = point["root_initial_sign_change"]
    medium = levels["4000"]
    high = levels["8000"]
    coarse = levels["2000"]
    for coarse_point, medium_point, high_point in zip(coarse, medium, high, strict=True):
        label = str(high_point["Delta_N_eff"])
        guards[f"dneff_{label}_H0_grid"] = abs(high_point["H0_km_s_Mpc"] - medium_point["H0_km_s_Mpc"]) <= 0.005
        guards[f"dneff_{label}_S8_grid"] = abs(high_point["S8_conditional"] - medium_point["S8_conditional"]) <= 0.0005
    full = high[-1]
    guards["full_steam_H0_comparator"] = abs(full["H0_km_s_Mpc"] - 66.37) <= 0.05
    guards["full_steam_S8_comparator"] = abs(full["S8_conditional"] - 0.8745) <= 0.002
    guards["identical_non_delta_inputs"] = all(
        tuple(point["Delta_N_eff"] for point in level_points) == SCIENCE_DELTA_NEFF
        and len({point["non_delta_input_fingerprint_sha256"] for point in level_points}) == 1
        and all(
            point["non_delta_input_fingerprint_sha256"]
            == _projection_fingerprint(point["non_delta_input_projection"])
            for point in level_points
        )
        for level_points in levels.values()
    )
    all_pass = all(guards.values())
    verdict = "PASS_THREE_POINT_LEGACY_SENSITIVITY" if all_pass else "REVIEW_NUMERICAL_CONVERGENCE"
    return _build_success_output(
        runtime_seconds=deadline.elapsed(),
        theta_ref=theta_ref,
        theta_evidence=theta_evidence,
        levels=levels,
        guards=guards,
        verdict=verdict,
    )


def _frozen_input_ledger() -> dict[str, Any]:
    return {
        "c_km_s": C_KM_S,
        "omega_b": OMEGA_B,
        "omega_m": OMEGA_M,
        "omega_gamma": OMEGA_GAMMA,
        "N_eff_standard": NEFF_STANDARD,
        "z_star": Z_STAR,
        "h_ref": H_REF,
        "lambda": LAMBDA,
        "delta": DELTA,
        "sigma8_LCDM": SIGMA8_LCDM,
        "x_min": X_MIN,
        "h_bracket": list(H_BRACKET),
        "Delta_N_eff_points": list(SCIENCE_DELTA_NEFF),
        "background_grids": list(SCIENCE_GRIDS),
    }


def _review_payload(error: GuardFailure, runtime_seconds: float) -> dict[str, Any]:
    if not isinstance(error, (InvalidBackgroundOrRoot, NumericalConvergenceReview)):
        raise TypeError("only frozen scientific REVIEW exceptions may become evidence")
    return _native({
        "schema": "v318_pt1_h0_s8_three_point_legacy_sensitivity_v1",
        "claim": "THREE_POINT_LEGACY_ANCHOR_H0_S8_SENSITIVITY",
        "scope": "legacy_sampled_conditional_not_current_theory_range_or_likelihood",
        "contract_sha256": CONTRACT_SHA256,
        "runtime_seconds": runtime_seconds,
        "execution_verdict": error.verdict,
        "results_status": "NOT_COMPUTED_OR_PARTIAL_RESULTS_DISCARDED",
        "failure": {
            "exception_class": type(error).__name__,
            "stage": error.stage,
            "message": str(error),
            "context": error.context,
        },
        "frozen_input_ledger": _frozen_input_ledger(),
        "checks": {
            "background_or_root_valid": (
                "FAIL"
                if error.verdict == "REVIEW_INVALID_BACKGROUND_OR_ROOT"
                else "NOT_EVALUATED"
            ),
            "numerical_convergence_complete": (
                "FAIL"
                if error.verdict == "REVIEW_NUMERICAL_CONVERGENCE"
                else "NOT_EVALUATED"
            ),
            "unexpected_technical_exception": "NOT_APPLICABLE_TO_CAPTURED_SCIENTIFIC_REVIEW",
        },
        "nonclaims": [
            "no H0 or S8 value is inferred from this REVIEW payload",
            "not a confidence or credible interval",
            "not a current v3.18 hard prediction",
            "does not close P5.4, G8 or G9",
        ],
    })


def execute_three_point_with_review(
    max_runtime_seconds: float,
    computation: Callable[[float], dict[str, Any]] | None = None,
) -> dict[str, Any]:
    started = time.monotonic()
    selected = run_three_point if computation is None else computation
    try:
        return selected(max_runtime_seconds)
    except (InvalidBackgroundOrRoot, NumericalConvergenceReview) as error:
        return _review_payload(error, time.monotonic() - started)


def execute_one_point_with_review(shard_id: str, max_runtime_seconds: float) -> dict[str, Any]:
    started = time.monotonic()
    try:
        return run_one_point(shard_id, max_runtime_seconds)
    except (InvalidBackgroundOrRoot, NumericalConvergenceReview) as error:
        payload = _review_payload(error, time.monotonic() - started)
        payload["schema"] = "v318_pt1_h0_s8_one_point_shard_v2"
        payload["claim"] = "ONE_POINT_SHARD_OF_THREE_POINT_LEGACY_ANCHOR_H0_S8_SENSITIVITY"
        payload["scope"] = "legacy_sampled_conditional_shard_review_not_range_or_likelihood"
        payload["parent_contract_sha256"] = CONTRACT_SHA256
        payload["sharded_addendum_sha256"] = SHARDED_ADDENDUM_SHA256
        payload["shard_id"] = shard_id
        payload["Delta_N_eff"] = SHARD_DELTA_NEFF[shard_id]
        return _native(payload)


def execute_grid_cell_with_review(cell_id: str, max_runtime_seconds: float) -> dict[str, Any]:
    if cell_id not in GRID_CELL_SPECS:
        raise ValueError(f"unknown frozen grid cell: {cell_id}")
    shard_id, delta_neff, grid_n = GRID_CELL_SPECS[cell_id]
    started = time.monotonic()
    try:
        return run_grid_cell(cell_id, max_runtime_seconds)
    except (InvalidBackgroundOrRoot, NumericalConvergenceReview) as error:
        payload = _review_payload(error, time.monotonic() - started)
        payload["schema"] = "v318_pt1_h0_s8_grid_cell_v3"
        payload["claim"] = "GRID_CELL_OF_THREE_POINT_LEGACY_ANCHOR_H0_S8_SENSITIVITY"
        payload["scope"] = "legacy_sampled_conditional_grid_cell_review_not_range_or_likelihood"
        payload["parent_contract_sha256"] = CONTRACT_SHA256
        payload["sharded_addendum_sha256"] = SHARDED_ADDENDUM_SHA256
        payload["grid_cell_addendum_sha256"] = GRID_CELL_ADDENDUM_SHA256
        payload["cell_id"] = cell_id
        payload["shard_id"] = shard_id
        payload["Delta_N_eff"] = delta_neff
        payload["grid_n"] = grid_n
        payload["grid_convergence_status"] = "DEFERRED_CROSS_CELL"
        payload["full_steam_comparator_applicable"] = cell_id == "full-n8000"
        return _native(payload)


def execute_n8000_reference_stage_with_review(max_runtime_seconds: float) -> dict[str, Any]:
    started = time.monotonic()
    try:
        return run_n8000_reference_stage(max_runtime_seconds)
    except (InvalidBackgroundOrRoot, NumericalConvergenceReview) as error:
        payload = _review_payload(error, time.monotonic() - started)
        payload.update({
            "schema": "v318_pt1_h0_s8_n8000_reference_stage_v4",
            "claim": "TECHNICAL_REFERENCE_STAGE_FOR_GRID_CELL_N8000",
            "scope": "legacy_execution_stage_review_not_scientific_cell_or_range",
            "grid_n": 8000,
            "v3_addendum_sha256": GRID_CELL_ADDENDUM_SHA256,
            "v4_addendum_sha256": N8000_STAGED_ADDENDUM_SHA256,
        })
        return _native(payload)


def execute_n8000_model_stage_with_review(
    shard_id: str,
    reference_payload: dict[str, Any],
    reference_actual_sha256: str,
    reference_expected_sha256: str,
    max_runtime_seconds: float,
) -> dict[str, Any]:
    started = time.monotonic()
    try:
        return run_n8000_model_stage(
            shard_id,
            reference_payload,
            reference_actual_sha256,
            reference_expected_sha256,
            max_runtime_seconds,
        )
    except (InvalidBackgroundOrRoot, NumericalConvergenceReview) as error:
        payload = _review_payload(error, time.monotonic() - started)
        payload.update({
            "schema": "v318_pt1_h0_s8_n8000_model_stage_v4",
            "claim": "TECHNICAL_MODEL_STAGE_FOR_GRID_CELL_N8000",
            "scope": "legacy_execution_stage_review_not_final_cell_or_range",
            "shard_id": shard_id,
            "Delta_N_eff": SHARD_DELTA_NEFF[shard_id],
            "grid_n": 8000,
            "v3_addendum_sha256": GRID_CELL_ADDENDUM_SHA256,
            "v4_addendum_sha256": N8000_STAGED_ADDENDUM_SHA256,
            "reference_stage_sha256": reference_actual_sha256.upper(),
        })
        return _native(payload)


def execute_n8000_bisection_stage_with_review(
    *,
    shard_id: str,
    segment: str,
    reference_payload: dict[str, Any],
    reference_actual_sha256: str,
    reference_expected_sha256: str,
    max_runtime_seconds: float,
    predecessor_payload: dict[str, Any] | None = None,
    predecessor_actual_sha256: str | None = None,
    predecessor_expected_sha256: str | None = None,
) -> dict[str, Any]:
    started = time.monotonic()
    try:
        return run_n8000_bisection_stage(
            shard_id=shard_id,
            segment=segment,
            reference_payload=reference_payload,
            reference_actual_sha256=reference_actual_sha256,
            reference_expected_sha256=reference_expected_sha256,
            max_runtime_seconds=max_runtime_seconds,
            predecessor_payload=predecessor_payload,
            predecessor_actual_sha256=predecessor_actual_sha256,
            predecessor_expected_sha256=predecessor_expected_sha256,
        )
    except (InvalidBackgroundOrRoot, NumericalConvergenceReview) as error:
        payload = _review_payload(error, time.monotonic() - started)
        payload.update({
            "schema": (
                "v318_pt1_h0_s8_n8000_model_stage_v4"
                if segment == "C"
                else "v318_pt1_h0_s8_n8000_bisection_segment_v5"
            ),
            "claim": (
                "TECHNICAL_MODEL_STAGE_FOR_GRID_CELL_N8000"
                if segment == "C"
                else "TECHNICAL_BISECTION_CONTINUATION_FOR_GRID_CELL_N8000"
            ),
            "scope": "legacy_execution_stage_review_not_final_cell_or_range",
            "shard_id": shard_id,
            "Delta_N_eff": SHARD_DELTA_NEFF[shard_id],
            "grid_n": 8000,
            "segment": segment,
            "v3_addendum_sha256": GRID_CELL_ADDENDUM_SHA256,
            "v4_addendum_sha256": N8000_STAGED_ADDENDUM_SHA256,
            "v5_addendum_sha256": N8000_BISECTION_ADDENDUM_SHA256,
            "reference_stage_sha256": reference_actual_sha256.upper(),
            "predecessor_segment_sha256": (
                None if predecessor_actual_sha256 is None
                else predecessor_actual_sha256.upper()
            ),
        })
        return _native(payload)


def synthetic_self_test(max_runtime_seconds: float = 5.0) -> dict[str, Any]:
    deadline = Deadline(max_runtime_seconds)
    # A synthetic scalar RK4 convergence identity, unrelated to the theory.
    def integrate(steps: int) -> float:
        step = 1.0 / steps
        value = 1.0
        for index in range(steps):
            deadline.check()
            x = index * step
            rhs = lambda _x, y: y
            k1 = rhs(x, value)
            k2 = rhs(x + step / 2.0, value + step * k1 / 2.0)
            k3 = rhs(x + step / 2.0, value + step * k2 / 2.0)
            k4 = rhs(x + step, value + step * k3)
            value += step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        return value

    coarse = integrate(8)
    fine = integrate(16)
    error = abs(fine - math.e)
    native_probe = _native({"numpy_float": np.float64(1.25), "numpy_int": np.int64(2)})
    projection_a = _non_delta_input_projection(17)
    projection_b = dict(projection_a)
    projection_b["lambda"] = projection_a["lambda"] + 1.0e-6
    with tempfile.TemporaryDirectory(prefix="v318_pt1_publish_selftest_") as directory:
        collision_target = Path(directory) / "evidence.json"
        sentinel = "foreign-evidence-must-survive\n"

        def create_racing_target() -> None:
            collision_target.write_text(sentinel, encoding="utf-8")

        collision_detected = False
        try:
            _publish_exclusive_payload(
                {"synthetic": True}, collision_target, before_link=create_racing_target
            )
        except FileExistsError:
            collision_detected = True
        collision_target_unchanged = collision_target.read_text(encoding="utf-8") == sentinel
        no_temp_residue = not list(Path(directory).glob(".*.tmp"))

    def synthetic_invalid_background(_seconds: float) -> dict[str, Any]:
        raise InvalidBackgroundOrRoot(
            "synthetic_root_sign", "synthetic no-sign-change", {"sentinel": 7}
        )

    invalid_review = execute_three_point_with_review(1.0, synthetic_invalid_background)

    def synthetic_numerical_review(_seconds: float) -> dict[str, Any]:
        raise NumericalConvergenceReview(
            "synthetic_grid_convergence", "synthetic convergence failure", {"sentinel": 11}
        )

    numerical_review = execute_three_point_with_review(1.0, synthetic_numerical_review)
    synthetic_labels = (-2.0, 4.0, 9.0)

    def synthetic_aggregate_point(
        label: float, h0_value: float, s8_value: float, grid_n: int
    ) -> dict[str, Any]:
        synthetic_projection = {"fixture": "non_scientific", "grid_n": grid_n}
        return {
            "Delta_N_eff": label,
            "H0_km_s_Mpc": h0_value,
            "S8_conditional": s8_value,
            "non_delta_input_fingerprint_sha256": _projection_fingerprint(
                synthetic_projection
            ),
        }

    synthetic_levels: dict[str, list[dict[str, Any]]] = {
        "2000": [
            synthetic_aggregate_point(point, 3.0 + index, 1.0 + index, 2000)
            for index, point in enumerate(synthetic_labels)
        ],
        "4000": [
            synthetic_aggregate_point(point, 2.0 + index, 1.5 + index, 4000)
            for index, point in enumerate(synthetic_labels)
        ],
        "8000": [
            synthetic_aggregate_point(point, 1.75 + index, 1.5 + index, 8000)
            for index, point in enumerate(synthetic_labels)
        ],
    }
    synthetic_success = _build_success_output(
        runtime_seconds=0.0,
        theta_ref=1.0,
        theta_evidence={"synthetic": True},
        levels=synthetic_levels,
        guards={"synthetic_only": True},
        verdict="PASS_THREE_POINT_LEGACY_SENSITIVITY",
    )
    synthetic_convergence = synthetic_success["convergence_diagnostics"][0]["H0_km_s_Mpc"]
    synthetic_zero_denominator = synthetic_success["convergence_diagnostics"][0]["S8_conditional"]
    expected_top_level_keys = {
        "schema", "claim", "scope", "contract_sha256", "runtime_seconds",
        "theta_reference", "theta_reference_evidence", "grid_results",
        "convergence_diagnostics", "high_grid_summary", "endpoint_deltas",
        "checks", "execution_verdict", "nonclaims",
    }
    expected_metric_keys = {
        "coarse_to_medium_signed", "coarse_to_medium_abs",
        "medium_to_high_signed", "medium_to_high_abs",
        "coarse_to_medium_over_medium_to_high_abs_ratio", "ratio_status",
    }
    synthetic_shard_levels = {
        level: [points[0]] for level, points in synthetic_levels.items()
    }
    synthetic_shard = _build_shard_success_output(
        shard_id="synthetic-not-production",
        delta_neff=synthetic_labels[0],
        runtime_seconds=0.0,
        theta_ref=1.0,
        theta_evidence={"synthetic": True},
        levels=synthetic_shard_levels,
        guards={"synthetic_only": True},
    )
    expected_shard_keys = {
        "schema", "claim", "scope", "parent_contract_sha256",
        "sharded_addendum_sha256", "shard_id", "Delta_N_eff",
        "runtime_seconds", "theta_reference", "theta_reference_evidence",
        "grid_results", "convergence_diagnostics", "high_grid_point",
        "non_delta_input_fingerprint_by_grid", "checks", "execution_verdict",
        "full_steam_comparator_applicable", "nonclaims",
    }
    synthetic_cell_point = {
        **synthetic_shard_levels["2000"][0],
        "non_delta_input_projection": {"fixture": "non_scientific", "grid_n": 17},
    }
    synthetic_cell_point["non_delta_input_fingerprint_sha256"] = (
        _projection_fingerprint(synthetic_cell_point["non_delta_input_projection"])
    )
    synthetic_cell = _build_grid_cell_success_output(
        cell_id="synthetic-cell",
        shard_id="synthetic",
        delta_neff=synthetic_labels[0],
        grid_n=17,
        runtime_seconds=0.0,
        theta_ref=1.0,
        theta_evidence={"synthetic": True},
        point=synthetic_cell_point,
        guards={"synthetic_only": True},
        full_steam_comparator_applicable=False,
    )
    expected_cell_keys = {
        "schema", "claim", "scope", "parent_contract_sha256",
        "sharded_addendum_sha256", "grid_cell_addendum_sha256", "cell_id",
        "shard_id", "Delta_N_eff", "grid_n", "runtime_seconds",
        "theta_reference", "theta_reference_evidence", "point",
        "non_delta_input_fingerprint_sha256", "checks", "execution_verdict",
        "grid_convergence_status", "full_steam_comparator_applicable", "nonclaims",
    }
    synthetic_staged_point = {
        **synthetic_cell_point,
        "grid_n": 17,
        "Delta_N_eff": synthetic_labels[0],
        "theta_relative_residual": 0.0,
        "matter_relative_residual": 0.0,
        "quadrature_relative_error": 0.0,
        "minimum_component": 1.0,
        "floor_or_clip_activations": 0,
        "root_initial_sign_change": True,
    }
    synthetic_staged_point["non_delta_input_projection"] = {
        "fixture": "non_scientific_staged", "grid_n": 17
    }
    synthetic_staged_point["non_delta_input_fingerprint_sha256"] = (
        _projection_fingerprint(synthetic_staged_point["non_delta_input_projection"])
    )
    synthetic_staged = _build_staged_grid_cell_from_validated(
        cell_id="synthetic-staged-cell",
        shard_id="synthetic",
        delta_neff=synthetic_labels[0],
        grid_n=17,
        theta_ref=1.0,
        theta_evidence={"synthetic": True},
        point=synthetic_staged_point,
        reference_sha_match=True,
        model_sha_match=True,
        runtime_seconds=0.0,
        comparator_applicable=False,
    )
    synthetic_sha_mismatch_rejected = False
    try:
        _require_exact_sha("A" * 64, "B" * 64, "synthetic upstream")
    except ValueError:
        synthetic_sha_mismatch_rejected = True
    synthetic_reference_diagnostics = {
        key: (True if key == "root_initial_sign_change" else 1)
        for key in REFERENCE_DIAGNOSTIC_KEYS
    }
    synthetic_reference = _build_n8000_reference_stage_success_output(
        runtime_seconds=0.0,
        theta_ref=1.0,
        theta_evidence={"synthetic": True},
        reference_growth=1.0,
        diagnostics=synthetic_reference_diagnostics,
        checks={"synthetic_only": True},
    )

    def synthetic_unexpected_error(_seconds: float) -> dict[str, Any]:
        raise ValueError("synthetic unexpected technical error")

    unexpected_propagated = False
    try:
        execute_three_point_with_review(1.0, synthetic_unexpected_error)
    except ValueError:
        unexpected_propagated = True

    synthetic_root = 0.123456789

    def synthetic_bisection_residual(
        value: float,
    ) -> tuple[float, dict[str, Any], float]:
        return value - synthetic_root, {"synthetic": True}, value

    one_shot_state, one_shot_last = _advance_bisection(
        low=0.0, high=1.0, low_residual=-synthetic_root,
        high_residual=1.0 - synthetic_root, completed_iterations=0,
        additional_iterations=29, residual=synthetic_bisection_residual,
        deadline=deadline,
    )
    segment_a_state, segment_a_last = _advance_bisection(
        low=0.0, high=1.0, low_residual=-synthetic_root,
        high_residual=1.0 - synthetic_root, completed_iterations=0,
        additional_iterations=10, residual=synthetic_bisection_residual,
        deadline=deadline,
    )
    segment_b_state, segment_b_last = _advance_bisection(
        low=segment_a_state["low"], high=segment_a_state["high"],
        low_residual=segment_a_state["low_residual"],
        high_residual=segment_a_state["high_residual"], completed_iterations=10,
        additional_iterations=10, residual=synthetic_bisection_residual,
        deadline=deadline,
    )
    segment_c_state, segment_c_last = _advance_bisection(
        low=segment_b_state["low"], high=segment_b_state["high"],
        low_residual=segment_b_state["low_residual"],
        high_residual=segment_b_state["high_residual"], completed_iterations=20,
        additional_iterations=9, residual=synthetic_bisection_residual,
        deadline=deadline,
    )
    synthetic_segment_payload = _bisection_segment_payload(
        shard_id="synthetic", delta_neff=-2.0, segment="A",
        reference_actual_sha256="C" * 64,
        predecessor_sha256=None, sound_horizon_mpc=1.0,
        theta_reference=0.25, reference_growth=0.75,
        quadrature_relative_error=0.0, target_distance_mpc=1.0,
        initial_low_residual=-synthetic_root,
        initial_high_residual=1.0 - synthetic_root,
        state=segment_a_state, last=segment_a_last, runtime_seconds=0.0,
    )
    predecessor_counter_rejected = False
    wrong_counter_payload = json.loads(json.dumps(synthetic_segment_payload))
    wrong_counter_payload["bisection_state"]["completed_midpoint_iterations"] = 9
    synthetic_predecessor_reference = {
        "theta_reference": 0.25, "reference_growth_D": 0.75
    }
    try:
        _validate_n8000_bisection_predecessor(
            payload=wrong_counter_payload, actual_sha256="A" * 64,
            expected_sha256="A" * 64, shard_id="synthetic", delta_neff=-2.0,
            expected_segment="A",
            expected_iterations=10, reference_actual_sha256="C" * 64,
            reference_payload=synthetic_predecessor_reference,
        )
    except ValueError:
        predecessor_counter_rejected = True
    checks = {
        "rk4_synthetic_error_below_1e-6": error < 1.0e-6,
        "rk4_refinement_improves": abs(fine - math.e) < abs(coarse - math.e),
        "native_json_roundtrip": json.loads(json.dumps(native_probe)) == {"numpy_float": 1.25, "numpy_int": 2},
        "science_points_not_evaluated": (
            synthetic_labels != SCIENCE_DELTA_NEFF
            and all(
                tuple(point["Delta_N_eff"] for point in synthetic_levels[level])
                == synthetic_labels
                for level in ("2000", "4000", "8000")
            )
        ),
        "non_delta_projection_identical_positive_control": (
            _projection_fingerprint(projection_a) == _projection_fingerprint(dict(projection_a))
        ),
        "non_delta_projection_mismatch_negative_control": (
            _projection_fingerprint(projection_a) != _projection_fingerprint(projection_b)
        ),
        "exclusive_publish_race_collision_detected": collision_detected,
        "exclusive_publish_race_target_unchanged": collision_target_unchanged,
        "exclusive_publish_race_no_temp_residue": no_temp_residue,
        "invalid_background_routes_to_frozen_review": (
            invalid_review["execution_verdict"] == "REVIEW_INVALID_BACKGROUND_OR_ROOT"
            and invalid_review["failure"]["stage"] == "synthetic_root_sign"
            and invalid_review["results_status"] == "NOT_COMPUTED_OR_PARTIAL_RESULTS_DISCARDED"
            and invalid_review["checks"]["background_or_root_valid"] == "FAIL"
            and invalid_review["checks"]["numerical_convergence_complete"] == "NOT_EVALUATED"
        ),
        "invalid_background_review_exports_frozen_inputs": (
            invalid_review["frozen_input_ledger"] == _frozen_input_ledger()
        ),
        "unexpected_exception_remains_technical": unexpected_propagated,
        "numerical_review_uses_not_evaluated_background_semantics": (
            numerical_review["execution_verdict"] == "REVIEW_NUMERICAL_CONVERGENCE"
            and numerical_review["failure"]["stage"] == "synthetic_grid_convergence"
            and numerical_review["checks"]["background_or_root_valid"] == "NOT_EVALUATED"
            and numerical_review["checks"]["numerical_convergence_complete"] == "FAIL"
        ),
        "review_payload_never_passes_unreached_guard_class": all(
            value != "PASS"
            for payload in (invalid_review, numerical_review)
            for value in payload["checks"].values()
        ),
        "convergence_schema_reports_both_differences_and_ratio": (
            synthetic_convergence["coarse_to_medium_signed"] == -1.0
            and synthetic_convergence["medium_to_high_signed"] == -0.25
            and synthetic_convergence["coarse_to_medium_abs"] == 1.0
            and synthetic_convergence["medium_to_high_abs"] == 0.25
            and synthetic_convergence["coarse_to_medium_over_medium_to_high_abs_ratio"] == 4.0
            and synthetic_convergence["ratio_status"] == "FINITE"
        ),
        "convergence_schema_zero_denominator_is_explicit": (
            synthetic_zero_denominator["coarse_to_medium_over_medium_to_high_abs_ratio"] is None
            and synthetic_zero_denominator["ratio_status"]
            == "UNDEFINED_ZERO_MEDIUM_TO_HIGH_DIFFERENCE"
        ),
        "aggregate_schema_exact_and_contains_three_diagnostics": (
            set(synthetic_success) == expected_top_level_keys
            and len(synthetic_success["convergence_diagnostics"]) == 3
            and [row["Delta_N_eff"] for row in synthetic_success["convergence_diagnostics"]]
            == list(synthetic_labels)
            and all(
                set(row) == {"Delta_N_eff", "H0_km_s_Mpc", "S8_conditional"}
                and set(row["H0_km_s_Mpc"]) == expected_metric_keys
                and set(row["S8_conditional"]) == expected_metric_keys
                for row in synthetic_success["convergence_diagnostics"]
            )
        ),
        "aggregate_diagnostics_are_not_decision_checks": (
            synthetic_success["checks"] == {"synthetic_only": True}
            and "convergence_diagnostics" not in synthetic_success["checks"]
        ),
        "aggregate_schema_is_native_json": (
            json.loads(json.dumps(synthetic_success, allow_nan=False)) == synthetic_success
        ),
        "shard_schema_uses_shared_three_grid_diagnostics": (
            set(synthetic_shard) == expected_shard_keys
            and synthetic_shard["shard_id"] == "synthetic-not-production"
            and synthetic_shard["Delta_N_eff"] == synthetic_labels[0]
            and len(synthetic_shard["convergence_diagnostics"]) == 1
            and synthetic_shard["high_grid_point"]
            == synthetic_shard_levels["8000"][0]
            and synthetic_shard["checks"] == {"synthetic_only": True}
            and synthetic_shard["execution_verdict"] == "PASS_ONE_POINT_SHARD_NUMERICS"
            and synthetic_shard["full_steam_comparator_applicable"] is False
            and synthetic_shard["non_delta_input_fingerprint_by_grid"]
            == {
                level: synthetic_shard_levels[level][0][
                    "non_delta_input_fingerprint_sha256"
                ]
                for level in ("2000", "4000", "8000")
            }
        ),
        "shard_schema_is_native_json": (
            json.loads(json.dumps(synthetic_shard, allow_nan=False)) == synthetic_shard
        ),
        "grid_cell_schema_is_exact_intrinsic_and_deferred": (
            set(synthetic_cell) == expected_cell_keys
            and synthetic_cell["cell_id"] == "synthetic-cell"
            and synthetic_cell["point"] == synthetic_cell_point
            and synthetic_cell["non_delta_input_fingerprint_sha256"]
            == synthetic_cell_point["non_delta_input_fingerprint_sha256"]
            and synthetic_cell["checks"] == {"synthetic_only": True}
            and synthetic_cell["execution_verdict"] == "PASS_GRID_CELL_INTRINSIC"
            and synthetic_cell["grid_convergence_status"] == "DEFERRED_CROSS_CELL"
            and synthetic_cell["full_steam_comparator_applicable"] is False
        ),
        "grid_cell_schema_is_native_json": (
            json.loads(json.dumps(synthetic_cell, allow_nan=False)) == synthetic_cell
        ),
        "staged_aggregate_uses_no_science_fixture_and_preserves_v3_schema": (
            synthetic_staged["cell_id"] == "synthetic-staged-cell"
            and synthetic_staged["grid_n"] == 17
            and synthetic_staged["Delta_N_eff"] == synthetic_labels[0]
            and synthetic_staged["point"] == synthetic_staged_point
            and synthetic_staged["execution_verdict"] == "PASS_GRID_CELL_INTRINSIC"
            and synthetic_staged["checks"]["reference_stage_sha256_match"]
            and synthetic_staged["checks"]["model_stage_sha256_match"]
            and synthetic_staged["grid_convergence_status"] == "DEFERRED_CROSS_CELL"
        ),
        "staged_upstream_sha_mismatch_is_fail_closed": synthetic_sha_mismatch_rejected,
        "staged_aggregate_schema_is_native_json": (
            json.loads(json.dumps(synthetic_staged, allow_nan=False)) == synthetic_staged
        ),
        "reference_success_exports_complete_evidence_and_stage_ledger": (
            set(synthetic_reference["reference_diagnostics"])
            == REFERENCE_DIAGNOSTIC_KEYS
            and synthetic_reference["frozen_input_ledger"]["stage_parameters"]
            == {
                "lambda": 0.0,
                "delta": 0.0,
                "Delta_N_eff": 0.0,
                "grid_n": 8000,
            }
            and synthetic_reference["execution_verdict"]
            == "PASS_N8000_REFERENCE_STAGE_INTRINSIC"
        ),
        "bisection_29_equals_segmented_10_10_9_exactly": (
            one_shot_state == segment_c_state
            and one_shot_last == segment_c_last
            and segment_a_state["completed_midpoint_iterations"] == 10
            and segment_b_state["completed_midpoint_iterations"] == 20
            and segment_c_state["completed_midpoint_iterations"] == 29
        ),
        "bisection_predecessor_wrong_counter_fails_closed": predecessor_counter_rejected,
        "bisection_segment_schema_is_native_json": (
            json.loads(json.dumps(synthetic_segment_payload, allow_nan=False))
            == synthetic_segment_payload
        ),
        "bisection_segment_carries_contract_state": (
            synthetic_segment_payload["theta_reference"] == 0.25
            and synthetic_segment_payload["reference_growth_D"] == 0.75
            and synthetic_segment_payload["frozen_input_ledger"]["stage_parameters"]
            == {
                "lambda": LAMBDA,
                "delta": DELTA,
                "Delta_N_eff": -2.0,
                "grid_n": 8000,
            }
        ),
    }
    return _native({
        "test": "offline_synthetic_DEV_self_test",
        "checks": checks,
        "all_pass": all(checks.values()),
        "runtime_seconds": deadline.elapsed(),
    })


def _publish_exclusive_payload(
    payload: dict[str, Any],
    target: Path,
    before_link: Callable[[], None] | None = None,
) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"official target already exists: {target}")
    temporary = target.with_name(f".{target.name}.{uuid.uuid4().hex}.tmp")
    linked = False
    try:
        with temporary.open("x", encoding="utf-8", newline="\n") as stream:
            json.dump(_native(payload), stream, indent=2, sort_keys=True, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        if before_link is not None:
            before_link()
        os.link(temporary, target)
        linked = True
    finally:
        temporary.unlink(missing_ok=True)
        if not linked and target.exists():
            # Only remove a target created by this failed link path; os.link is
            # atomic, so normally this branch is unreachable.
            pass


def publish_exclusive(payload: dict[str, Any], target: Path) -> None:
    _publish_exclusive_payload(payload, target)
