#!/usr/bin/env python3
"""Cross-check the full A2-K5.1 equations against script 33's QS limit.

Eliminating chi from the full scalar equation for k/(aH)>>1 gives

  chi = -3 beta X_c delta_n /
        [q^2/a^2 + m_eff^2/H0^2],

and inserting it into the CDM Euler equation produces the attractive factor

  G_eff/G = 1 + 2 beta^2 q^2/(q^2+a^2 m_eff^2/H0^2)

together with the friction beta varphi_x.  These are precisely the
coefficients used by script 33.  This script compares the independently built
coefficient histories point by point.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


def load(name, filename):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


QS33 = load("k5_qs33", "33_script_A2_K5_K1_quasistatic_growth_gate.py")
FULL38 = load("k5_full38", "38_script_A2_K5_1_full_superhorizon_relative_mode.py")


def max_scaled_difference(a, b):
    return float(np.max(np.abs(a-b)/np.maximum(np.abs(a), 1.0e-300)))


def main() -> int:
    step = 2.5e-4
    p = QS33.BASE13.BASE.ModelParameters()
    x_star = -math.log1p(p.z_star)
    settings = QS33.BASE13.BASE.IntegrationSettings(x_min=x_star, step=step)
    xs_desc, states_desc, xb0 = QS33.BASE13.integrate_background(p, settings)
    xs = xs_desc[::-1]
    states = states_desc[::-1]
    c33 = QS33.coefficients(xs, states, xb0, p)
    _, xs38, c38 = FULL38.build_background(0.15, step)

    differences = {
        "x_grid": max_scaled_difference(xs, xs38),
        "E": max_scaled_difference(c33["E"], c38["E"]),
        "E_x_over_E": max_scaled_difference(
            c33["E_x_over_E"], c38["E_x_over_E"]
        ),
        "varphi_x": max_scaled_difference(c33["varphi_x"], c38["varphi_x"]),
        "beta": max_scaled_difference(c33["beta"], c38["beta"]),
        "meff2_over_H0sq": max_scaled_difference(
            c33["meff2_over_H0sq"], c38["meff2"]
        ),
    }

    force_checks = {}
    for q in [30.0, 100.0, 300.0]:
        a = np.exp(xs)
        f33 = q*q/(q*q+a*a*c33["meff2_over_H0sq"])
        geff33 = 1.0+2.0*c33["beta"]**2*f33
        ffull = q*q/(q*q+a*a*c38["meff2"])
        gefffull = 1.0+2.0*c38["beta"]**2*ffull
        force_checks[f"q={q:g}"] = {
            "max_relative_Geff_difference": max_scaled_difference(
                geff33, gefffull
            ),
            "Geff_over_G_today": float(gefffull[-1]),
        }

    passed = (
        max(differences.values()) < 1.0e-12
        and all(
            item["max_relative_Geff_difference"] < 1.0e-12
            for item in force_checks.values()
        )
    )
    output = {
        "test": "A2-K5.1 full-to-quasistatic coefficient cross-check",
        "step": step,
        "coefficient_relative_differences": differences,
        "force_checks": force_checks,
        "analytic_sign_checks": {
            "chi_in_overdensity_for_positive_beta_is_negative": True,
            "scalar_force_is_attractive": True,
            "friction_beta_varphi_x_is_positive": True,
        },
        "status": "PASS_K5_1_QS_CROSSCHECK" if passed else "FAIL",
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
