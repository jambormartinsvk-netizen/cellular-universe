#!/usr/bin/env python3
"""Corrected successor to script 38 for the A2-K5.1 superhorizon test.

Script 38 multiplied the scalar enthalpy by X_f twice in the 0i Einstein
source and in the initial total-momentum cancellation.  The correct identity
is

  (rho_phi+p_phi)/(3 H0^2 Mpl^2)
      = E^2 varphi_x^2/3 = delta X_f.

No perturbation equation, initial-mode definition, or pass threshold changes.
Script 38 is preserved as the failed diagnostic that exposed the error.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


BASE_PATH = Path(__file__).with_name(
    "38_script_A2_K5_1_full_superhorizon_relative_mode.py"
)
SPEC = importlib.util.spec_from_file_location("k5_1_superhorizon_base38", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load script 38: {BASE_PATH}")
BASE38 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE38
SPEC.loader.exec_module(BASE38)


def corrected_phi_x_and_uphi(x, y, c):
    a = math.exp(x)
    uphi = y[BASE38.CHI]/(a*c["E"]*c["varphi_x"])
    scalar_enthalpy = c["E"]**2*c["varphi_x"]**2/3.0
    momentum = (
        c["xc"]*y[BASE38.UC]
        +c["xb"]*y[BASE38.UB]
        +(4.0/3.0)*c["xr"]*y[BASE38.UR]
        +scalar_enthalpy*uphi
    )
    phi_x = -y[BASE38.PHI]+1.5*a*momentum/c["E"]
    return phi_x, uphi


def corrected_initial_relative_mode(x0, c0):
    a = math.exp(x0)
    scalar_enthalpy = c0["E"]**2*c0["varphi_x"]**2/3.0
    inertia = c0["xc"]+scalar_enthalpy
    uphi = c0["xc"]/inertia
    uc = -scalar_enthalpy/inertia
    chi = uphi*a*c0["E"]*c0["varphi_x"]

    y = np.zeros(9, dtype=float)
    y[BASE38.UC] = uc
    y[BASE38.CHI] = chi
    y[BASE38.DN] = -c0["beta"]*chi
    y[BASE38.PIX] = -3.0*c0["Y_varphi"]*chi/(
        c0["E"]**2*c0["varphi_x"]
    )
    return y


BASE38.phi_x_and_uphi = corrected_phi_x_and_uphi
BASE38.initial_relative_mode = corrected_initial_relative_mode


def main() -> int:
    coupled_coarse = BASE38.run(1.25e-4, 1.0e-5, 0.15)
    coupled_fine = BASE38.run(6.25e-5, 1.0e-5, 0.15)
    coupled_half_k = BASE38.run(6.25e-5, 5.0e-6, 0.15)
    uncoupled_fine = BASE38.run(6.25e-5, 1.0e-5, 0.0)

    transfer = coupled_fine["absolute_relative_velocity_transfer"]
    null_transfer = uncoupled_fine["absolute_relative_velocity_transfer"]
    gain = transfer/max(null_transfer, 1.0e-300)
    log_coarse = math.log(max(
        coupled_coarse["absolute_relative_velocity_transfer"], 1.0e-300
    ))
    log_fine = math.log(max(transfer, 1.0e-300))
    step_conv = abs(log_coarse-log_fine)/max(abs(log_fine), 1.0)
    log_half_k = math.log(max(
        coupled_half_k["absolute_relative_velocity_transfer"], 1.0e-300
    ))
    k_conv = abs(log_half_k-log_fine)/max(abs(log_fine), 1.0)

    checks = {
        "all_runs_finite": all(r["all_finite"] for r in [
            coupled_coarse, coupled_fine, coupled_half_k, uncoupled_fine
        ]),
        "initial_constraint_satisfied": (
            coupled_fine["initial_abs_00_constraint"] < 1.0e-10
        ),
        "step_converged": step_conv < 1.0e-6,
        "superhorizon_k_converged": k_conv < 1.0e-6,
        "constraint_controlled": (
            coupled_fine["global_relative_00_constraint_residual"] < 1.0e-5
        ),
        "no_more_than_one_interaction_efold_relative_to_null": gain < math.e,
        "no_absolute_explosive_transfer": transfer < math.e,
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K5.1 corrected full first superhorizon relative mode",
        "successor_to": "38_script_A2_K5_1_full_superhorizon_relative_mode.py",
        "physics_change": "none",
        "implementation_fix": (
            "scalar enthalpy E^2 varphi_x^2/3; removed duplicated X_f"
        ),
        "coupled_coarse": coupled_coarse,
        "coupled_fine": coupled_fine,
        "coupled_half_k": coupled_half_k,
        "uncoupled_fine": uncoupled_fine,
        "coupled_to_null_transfer_gain": gain,
        "coupled_to_null_log_gain": math.log(max(gain, 1.0e-300)),
        "step_log_transfer_relative_difference": step_conv,
        "k_log_transfer_relative_difference": k_conv,
        "checks": checks,
        "verdict": "PASS_K5_1_SUPERHORIZON_GATE" if passed else "FAIL_OR_DEAD_REVIEW",
        "scope": (
            "Full scalar+CDM+baryon+perfect-radiation first-order test with "
            "00/0i Einstein constraints; not a Boltzmann likelihood."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
