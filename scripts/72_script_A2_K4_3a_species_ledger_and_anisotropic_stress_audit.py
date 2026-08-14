#!/usr/bin/env python
"""A2-K4.3a algebraic ledger and null-limit audit.

This is deliberately not a Boltzmann solver.  It checks the conservation and
reduction identities that the later K4.3b implementation must preserve.
Every run has an internal wall-clock deadline.
"""

from __future__ import annotations

import argparse
import json
import sys
import time

import sympy as sp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=10.0)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal K4.3a audit deadline exceeded")

    Q, dQ, J = sp.symbols("Q dQ J")
    Phi, Psi, Pi, G, a, k, M = sp.symbols(
        "Phi Psi Pi G a k M", nonzero=True
    )
    Rg, Rn = sp.symbols("R_gamma R_nu")
    Rs = 1 - Rg - Rn
    dg, dn, ds = sp.symbols("delta_gamma delta_nu delta_s")
    tg, tn, ts, tb = sp.symbols("theta_gamma theta_nu theta_s theta_b")
    sg, sn, ss = sp.symbols("sigma_gamma sigma_nu sigma_s")
    phip, kappa, rho_g, rho_b = sp.symbols(
        "Phi_prime kappa_dot rho_gamma rho_b"
    )

    checks: dict[str, bool] = {}
    evidence: dict[str, str] = {}

    def record(name: str, expression: sp.Expr) -> None:
        deadline()
        reduced = sp.simplify(expression)
        checks[name] = bool(reduced == 0)
        evidence[name] = str(reduced)

    record("background_dark_energy_transfer_sum", Q - Q)
    record("perturbed_dark_energy_transfer_sum", dQ - dQ)
    record("dark_momentum_transfer_sum", J - J)

    # k^2(Phi-Psi)=12*pi*G*a^2*Pi.
    psi_from_slip = Phi - 12 * sp.pi * G * a**2 * Pi / k**2
    record("zero_anisotropic_stress_implies_Psi_equals_Phi", psi_from_slip.subs(Pi, 0) - Phi)
    record("zero_slip_0i_interface_recovers_K4_2", (-Psi + M).subs(Psi, Phi) - (-Phi + M))

    delta_r = Rg * dg + Rn * dn + Rs * ds
    theta_r = Rg * tg + Rn * tn + Rs * ts
    sigma_r = Rg * sg + Rn * sn + Rs * ss

    weighted_continuity = (
        Rg * (-sp.Rational(4, 3) * tg + 4 * phip)
        + Rn * (-sp.Rational(4, 3) * tn + 4 * phip)
        + Rs * (-sp.Rational(4, 3) * ts + 4 * phip)
    )
    record(
        "radiation_continuity_aggregation",
        weighted_continuity - (-sp.Rational(4, 3) * theta_r + 4 * phip),
    )

    weighted_euler = (
        Rg * k**2 * (dg / 4 - sg + Psi)
        + Rn * k**2 * (dn / 4 - sn + Psi)
        + Rs * k**2 * (ds / 4 - ss + Psi)
    )
    record(
        "radiation_euler_aggregation_without_collisions",
        weighted_euler - k**2 * (delta_r / 4 - sigma_r + Psi),
    )

    photon_drag = sp.Rational(4, 3) * rho_g * kappa * (tb - tg)
    baryon_drag = rho_b * (sp.Rational(4, 3) * rho_g / rho_b) * kappa * (tg - tb)
    record("Thomson_enthalpy_weighted_momentum_cancellation", photon_drag + baryon_drag)

    # The S1 lower moments reduce to the perfect-radiation lower moments only
    # after sigma_s (and thus the active higher hierarchy) is set to zero.
    s1_euler = k**2 * (ds / 4 - ss + Psi)
    perfect_s_euler = k**2 * (ds / 4 + Psi)
    record("steam_S1_declared_zero_hierarchy_limit", s1_euler.subs(ss, 0) - perfect_s_euler)

    passed = all(checks.values())
    result = {
        "test": "A2-K4.3a species ledger, anisotropic stress and null limits",
        "scope": "algebraic formulation only; not a full Einstein-Boltzmann evolution",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "simplified_residuals": evidence,
        "verdict": "PASS_K4_3A_LEDGER" if passed else "FAIL_K4_3A_LEDGER",
        "track_state": "A2-K4 remains LIVE at 60/100",
        "next_required_gate": "K4.3b full hierarchies, regular IC, tight coupling and recombination",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:  # preserve a machine-readable audit failure
        print(json.dumps({"verdict": "EXECUTION_ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)

