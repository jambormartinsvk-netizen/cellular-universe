"""A2 diagnostic: barotropic closure of the fuel perturbations.

Purpose
-------
Test the principal (high-k) sound-speed term for a constant-w barotropic
fuel with the registered value w_f = -1 + delta.  For a barotropic fluid,
c_a^2 = dp/dρ = w_f.  A negative value changes the short-wavelength wave
equation into an exponential equation.

This script quantifies the instantaneous growth rate relative to H0 for
representative linear and mildly nonlinear comoving modes at z=0.  The
physical death verdict is analytic; this calculation only shows its scale.

No external data or third-party packages are used.
"""

from __future__ import annotations

import math


DELTA = 0.02297
W_FUEL = -1.0 + DELTA
CS2_BAROTROPIC = W_FUEL

H0_KM_S_MPC = 66.37
H = 0.6637
C_KM_S = 299_792.458

# Representative comoving wavenumbers in h/Mpc.
K_H_MPC = (0.01, 0.1, 1.0)


def main() -> int:
    if CS2_BAROTROPIC >= 0.0:
        raise AssertionError("This diagnostic expects a negative barotropic c_s^2.")

    abs_cs = math.sqrt(-CS2_BAROTROPIC)
    hubble_wavenumber_mpc = H0_KM_S_MPC / C_KM_S

    print("A2 BAROTROPIC FUEL GRADIENT DIAGNOSTIC")
    print(f"delta={DELTA:.8f}")
    print(f"w_f={W_FUEL:.8f}")
    print(f"c_s^2(barotropic)={CS2_BAROTROPIC:.8f}")
    print(f"|c_s|={abs_cs:.8f}")
    print(f"H0/c={hubble_wavenumber_mpc:.12e} 1/Mpc")
    print()
    print("k[h/Mpc] | k[1/Mpc] | mu/H0 | one e-fold time [H0^-1]")

    ratios: list[float] = []
    for k_h_mpc in K_H_MPC:
        k_mpc = k_h_mpc * H
        mu_over_h0 = abs_cs * k_mpc / hubble_wavenumber_mpc
        ratios.append(mu_over_h0)
        efold_hubble_time = 1.0 / mu_over_h0
        print(
            f"{k_h_mpc:8.3f} | {k_mpc:8.6f} | "
            f"{mu_over_h0:9.3f} | {efold_hubble_time:16.6e}"
        )

    print()
    print("principal_equation: delta_k'' + c_s^2 k^2 delta_k = 0")
    print("negative_cs2_solution: delta_k proportional exp(|c_s| k eta)")

    kill = CS2_BAROTROPIC < 0.0 and all(ratio > 1.0 for ratio in ratios)
    print(f"kill_condition_negative_cs2_subhorizon={str(kill).upper()}")
    print("VERDICT=MRTVA_BAROTROPIC_CLOSURE" if kill else "VERDICT=REQUIRES_REVIEW")

    return 0 if kill else 1


if __name__ == "__main__":
    raise SystemExit(main())

