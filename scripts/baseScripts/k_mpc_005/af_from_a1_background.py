"""Shared, bounded A1-K1 background utilities for the K_MPC=0.05 audit."""

from __future__ import annotations

from dataclasses import dataclass
import math
import time


@dataclass(frozen=True)
class FrozenA1:
    h: float = 0.6637
    omega_m0: float = 0.3517
    lam: float = 0.15
    delta: float = 0.02297
    delta_neff: float = 0.0535
    omega_b: float = 0.02237
    omega_gamma: float = 2.469e-5
    neff_standard: float = 3.046


def omega_r0(p: FrozenA1) -> float:
    return p.omega_gamma * (1.0 + 0.2271 * (p.neff_standard + p.delta_neff)) / p.h**2


def initial_state(p: FrozenA1) -> tuple[float, float, float]:
    xr = omega_r0(p)
    xf = 1.0 - p.omega_m0 - xr
    if min(xf, p.omega_m0, xr) <= 0.0:
        raise ValueError("frozen A1 present-day densities are not positive")
    return xf, p.omega_m0, xr


def rhs(state: tuple[float, float, float], p: FrozenA1) -> tuple[float, float, float]:
    xf, xm, xr = state
    e2 = xf + xm + xr
    if not math.isfinite(e2) or e2 <= 0.0:
        raise FloatingPointError("A1 background reached non-positive/non-finite E^2")
    transfer = p.lam * xf / math.sqrt(e2)
    return (-3.0 * p.delta * xf - transfer, -3.0 * xm + transfer, -4.0 * xr)


def add(state: tuple[float, float, float], slope: tuple[float, float, float], factor: float) -> tuple[float, float, float]:
    return tuple(v + factor * dv for v, dv in zip(state, slope))  # type: ignore[return-value]


def rk4_step(state: tuple[float, float, float], dx: float, p: FrozenA1) -> tuple[float, float, float]:
    k1 = rhs(state, p)
    k2 = rhs(add(state, k1, 0.5 * dx), p)
    k3 = rhs(add(state, k2, 0.5 * dx), p)
    k4 = rhs(add(state, k3, dx), p)
    return tuple(v + dx * (a + 2*b + 2*c + d) / 6.0 for v, a, b, c, d in zip(state, k1, k2, k3, k4))  # type: ignore[return-value]


def integrate_af(p: FrozenA1, x_min: float, abs_step: float, deadline_seconds: float) -> dict[str, object]:
    if x_min >= 0.0 or abs_step <= 0.0 or deadline_seconds <= 0.0:
        raise ValueError("invalid integration limits")
    started = time.monotonic()
    n_steps = int(round(abs(x_min) / abs_step))
    if n_steps < 1 or not math.isclose(n_steps * abs_step, abs(x_min), rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("x_min must be an integer multiple of abs_step")
    dx = -abs_step
    state = initial_state(p)
    p_exponent = 4.0 - 3.0 * p.delta
    checkpoints = {-12.0, -14.0, -16.0, x_min}
    samples: dict[str, float] = {}
    min_density = min(state)
    min_e2 = sum(state)
    for index in range(n_steps):
        if index % 256 == 0 and time.monotonic() - started > deadline_seconds:
            raise TimeoutError("K_MPC A_f internal deadline exceeded")
        state = rk4_step(state, dx, p)
        if not all(math.isfinite(v) and v > 0.0 for v in state):
            raise FloatingPointError("non-finite or non-positive A1 density")
        min_density = min(min_density, *state)
        min_e2 = min(min_e2, sum(state))
        x = (index + 1) * dx
        for checkpoint in checkpoints:
            if abs(x - checkpoint) <= 0.5 * abs_step:
                af = (state[0] / state[2]) / math.exp(p_exponent * x)
                samples[f"x={checkpoint:.1f}"] = af
    af_final = (state[0] / state[2]) / math.exp(p_exponent * x_min)
    return {
        "af_final": af_final,
        "samples": samples,
        "min_density": min_density,
        "min_e2": min_e2,
        "steps": n_steps,
        "runtime_seconds": time.monotonic() - started,
        "p_exponent": p_exponent,
        "omega_r0": omega_r0(p),
        "x_f0": initial_state(p)[0],
    }


def integrate_samples(
    p: FrozenA1,
    x_min: float,
    abs_step: float,
    sample_x: tuple[float, ...],
    deadline_seconds: float,
) -> dict[str, object]:
    """Bounded backwards A1 integration returning background values at named x."""
    if x_min >= 0.0 or abs_step <= 0.0 or deadline_seconds <= 0.0:
        raise ValueError("invalid integration limits")
    started = time.monotonic()
    n_steps = int(round(abs(x_min) / abs_step))
    if n_steps < 1 or not math.isclose(n_steps * abs_step, abs(x_min), rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("x_min must be an integer multiple of abs_step")
    # Backward integration visits -2, -4, ... before -18.  Keeping the
    # smallest target at the list end makes pop() follow that physical order.
    targets = sorted(sample_x)
    state = initial_state(p)
    samples: dict[str, dict[str, float]] = {}
    min_density = min(state)
    min_e2 = sum(state)
    for index in range(n_steps):
        if index % 256 == 0 and time.monotonic() - started > deadline_seconds:
            raise TimeoutError("K_MPC A1 trajectory internal deadline exceeded")
        state = rk4_step(state, -abs_step, p)
        if not all(math.isfinite(v) and v > 0.0 for v in state):
            raise FloatingPointError("non-finite or non-positive A1 density")
        min_density = min(min_density, *state)
        min_e2 = min(min_e2, sum(state))
        x = -(index + 1) * abs_step
        while targets and abs(x - targets[-1]) <= 0.5 * abs_step:
            sample = targets.pop()
            xf, xm, xr = state
            a = math.exp(sample)
            samples[f"x={sample:.1f}"] = {
                "a": a,
                "D_a1": (xf + xm + xr) * a**4 / omega_r0(p),
                "X_f": xf,
                "X_m": xm,
                "X_r": xr,
            }
    return {
        "samples": samples,
        "min_density": min_density,
        "min_e2": min_e2,
        "steps": n_steps,
        "runtime_seconds": time.monotonic() - started,
    }
