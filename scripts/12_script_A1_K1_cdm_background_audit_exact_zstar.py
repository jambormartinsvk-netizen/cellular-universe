#!/usr/bin/env python3
"""Corrected A1-K1 audit: integration grid contains recombination exactly.

This script deliberately imports the equations, diagnostics, CLI, and thresholds
from script 11. It replaces only the fixed uniform integration grid. The grid is
split at x_star = -ln(1 + z_star), so the created-CDM fraction is not limited by
linear interpolation error at recombination.

Script 11 is retained unchanged as the reproducible failed implementation.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np


BASE_PATH = Path(__file__).with_name("11_script_A1_K1_cdm_background_audit.py")
SPEC = importlib.util.spec_from_file_location("a1_k1_audit_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load base audit script: {BASE_PATH}")
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)


def integration_grid(p, settings) -> np.ndarray:
    """Return a decreasing grid with x_star included as an exact point."""
    x_star = -np.log1p(p.z_star)
    breakpoints = [0.0]
    if settings.x_min < x_star < 0.0:
        breakpoints.append(float(x_star))
    breakpoints.append(settings.x_min)

    segments: list[np.ndarray] = []
    for start, stop in zip(breakpoints[:-1], breakpoints[1:]):
        intervals = max(int(np.ceil(abs(stop - start) / settings.step)), 1)
        segment = np.linspace(start, stop, intervals + 1)
        if segments:
            segment = segment[1:]
        segments.append(segment)
    return np.concatenate(segments)


def integrate_background(p, settings):
    """Integrate with variable RK4 steps no larger than settings.step."""
    if settings.x_min >= 0.0:
        raise ValueError("x_min must be negative")
    if settings.step <= 0.0:
        raise ValueError("step must be positive")

    xs = integration_grid(p, settings)
    y = np.zeros((len(xs), 3), dtype=float)
    y[0], x_b0 = BASE.initial_state(p)

    for i in range(len(xs) - 1):
        state = y[i]
        dx = xs[i + 1] - xs[i]
        k1 = BASE.rhs(state, p)
        k2 = BASE.rhs(state + 0.5 * dx * k1, p)
        k3 = BASE.rhs(state + 0.5 * dx * k2, p)
        k4 = BASE.rhs(state + dx * k3, p)
        y[i + 1] = state + dx * (k1 + 2*k2 + 2*k3 + k4) / 6.0

    return xs, y, x_b0


# Patch only the integrator used by main, convergence, and lambda-zero checks.
BASE.integrate_background = integrate_background


if __name__ == "__main__":
    raise SystemExit(BASE.main())
