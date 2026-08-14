#!/usr/bin/env python
"""Preregistered 80-digit audit of the K7a transformation derivative T'.

No perturbation state, Jacobian evolution, or ODE solver is used.  The script
re-evaluates the registered background weights with mpmath and compares the
analytic T' against three central-difference steps.  Runtime is hard bounded.
"""

from __future__ import annotations

import argparse
import json
import math
import time

import mpmath as mp
import numpy as np


N_STATE = 13


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--mode", choices=("NID", "NIV"), required=True)
    parser.add_argument("--surface", choices=("deep", "shallow"), required=True)
    parser.add_argument("--dps", type=int, default=80)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        parser.error("max runtime must be in (0,5]")
    if args.dps != 80:
        parser.error("this preregistered audit requires exactly dps=80")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("K7a-J2 high-precision Tprime deadline exceeded")

    mp.mp.dps = args.dps
    x = mp.mpf("-25") if args.surface == "deep" else mp.mpf("-23")
    delta = mp.mpf("0.02297")
    p = mp.mpf("3.93109")
    h0 = mp.mpf("0.6637")
    omega_m0 = mp.mpf("0.3517")
    ombh2 = mp.mpf("0.02237")
    total_matter_h2 = omega_m0*h0**2
    fb = ombh2/total_matter_h2
    fc = 1-fb
    neff = mp.mpf("3.046")+mp.mpf("0.0535")
    rn = mp.mpf("0.2271")*neff/(1+mp.mpf("0.2271")*neff)
    rg = 1-rn
    omega_gamma_h2 = mp.mpf("2.47282e-5")
    omega_r0 = omega_gamma_h2*(1+mp.mpf("0.2271")*neff)/h0**2
    hubble0_mpc = 100*h0/mp.mpf("299792.458")
    k_mpc = mp.mpf("0.05")
    mu = hubble0_mpc*omega_m0/mp.sqrt(omega_r0)/k_mpc
    g2 = mp.mpf("0.15")*(hubble0_mpc/k_mpc)**2*mp.sqrt(omega_r0)
    transfer_shape = g2*(1/(p+1)-mp.mpf("0.5"))

    def background_weights(x_value: mp.mpf) -> tuple[mp.mpf, ...]:
        z = k_mpc*mp.e**x_value/(hubble0_mpc*mp.sqrt(omega_r0))
        fuel_piece = z**p
        denominator = 1+mu*z+fuel_piece*(1+transfer_shape*z**2)
        denominator_x = mu*z+fuel_piece*(
            p+(p+2)*transfer_shape*z**2
        )
        q = -1+mp.mpf("0.5")*denominator_x/denominator
        Og = rg/denominator
        On = rn/denominator
        Ob = fb*mu*z/denominator
        Oc = (
            fc*mu*z+g2*z**(p+2)/(p+1)
        )/denominator
        Of = fuel_piece*(1-mp.mpf("0.5")*g2*z**2)/denominator
        return z, q, Og, On, Ob, Oc, Of

    def transformation(x_value: mp.mpf) -> mp.matrix:
        _, _, Og, On, Ob, Oc, Of = background_weights(x_value)
        T = mp.eye(N_STATE)
        for column in range(N_STATE):
            T[3, column] = 0
            T[7, column] = 0
        T[3, 2] = Og
        T[3, 3] = On
        T[3, 4] = Ob
        T[3, 5] = Oc
        T[3, 11] = Of
        T[7, 6] = 2*Og+mp.mpf("1.5")*Ob
        T[7, 7] = 2*On
        T[7, 12] = mp.mpf("1.5")*delta*Of
        return T

    def analytic_Tprime(x_value: mp.mpf) -> mp.matrix:
        z, q, Og, On, Ob, Oc, Of = background_weights(x_value)
        ell = 2*(q+1)
        c_numerator = fc*mu*z+g2*z**(p+2)/(p+1)
        beta_c = (
            fc*mu*z+(p+2)*g2*z**(p+2)/(p+1)
        )/c_numerator
        g = g2*z**2
        beta_f = p-g/(1-mp.mpf("0.5")*g)
        Op = (
            -ell*Og,
            -ell*On,
            (1-ell)*Ob,
            (beta_c-ell)*Oc,
            (beta_f-ell)*Of,
        )
        Tp = mp.zeros(N_STATE, N_STATE)
        Tp[3, 2] = Op[0]
        Tp[3, 3] = Op[1]
        Tp[3, 4] = Op[2]
        Tp[3, 5] = Op[3]
        Tp[3, 11] = Op[4]
        Tp[7, 6] = 2*Op[0]+mp.mpf("1.5")*Op[2]
        Tp[7, 7] = 2*Op[1]
        Tp[7, 12] = mp.mpf("1.5")*delta*Op[4]
        return Tp

    def frobenius(matrix: mp.matrix) -> mp.mpf:
        return mp.sqrt(mp.fsum(
            matrix[row, column]**2
            for row in range(matrix.rows)
            for column in range(matrix.cols)
        ))

    deadline()
    Tp = analytic_Tprime(x)
    Tp_norm = frobenius(Tp)
    step_results: list[dict[str, object]] = []
    relative_errors: list[mp.mpf] = []
    for step_text in ("1e-8", "1e-12", "1e-16"):
        deadline()
        step = mp.mpf(step_text)
        Tp_fd = (transformation(x+step)-transformation(x-step))/(2*step)
        difference = Tp_fd-Tp
        max_abs = max(
            abs(difference[row, column])
            for row in range(N_STATE)
            for column in range(N_STATE)
        )
        relative = frobenius(difference)/Tp_norm
        relative_errors.append(relative)
        step_results.append({
            "step": step_text,
            "max_abs_error": mp.nstr(max_abs, 25),
            "relative_frobenius_error": mp.nstr(relative, 25),
        })

    # Independent float re-evaluation of the same analytic formulas used by 159.
    xf = float(x)
    h0f = 0.6637
    omega_m0f = 0.3517
    ombh2f = 0.02237
    fbf = ombh2f/(omega_m0f*h0f**2)
    fcf = 1.0-fbf
    nefff = 3.046+0.0535
    rnf = 0.2271*nefff/(1.0+0.2271*nefff)
    rgf = 1.0-rnf
    omega_r0f = 2.47282e-5*(1.0+0.2271*nefff)/h0f**2
    hubble0f = 100.0*h0f/299792.458
    kf = 0.05
    muf = hubble0f*omega_m0f/math.sqrt(omega_r0f)/kf
    g2f = 0.15*(hubble0f/kf)**2*math.sqrt(omega_r0f)
    pf = 3.93109
    transferf = g2f*(1.0/(pf+1.0)-0.5)
    zf = kf*math.exp(xf)/(hubble0f*math.sqrt(omega_r0f))
    fuelf = zf**pf
    denf = 1.0+muf*zf+fuelf*(1.0+transferf*zf**2)
    denxf = muf*zf+fuelf*(pf+(pf+2.0)*transferf*zf**2)
    qf = -1.0+0.5*denxf/denf
    Ogf, Onf = rgf/denf, rnf/denf
    Obf = fbf*muf*zf/denf
    Ocf = (fcf*muf*zf+g2f*zf**(pf+2.0)/(pf+1.0))/denf
    Off = fuelf*(1.0-0.5*g2f*zf**2)/denf
    ellf = 2.0*(qf+1.0)
    cnumf = fcf*muf*zf+g2f*zf**(pf+2.0)/(pf+1.0)
    betacf = (
        fcf*muf*zf+(pf+2.0)*g2f*zf**(pf+2.0)/(pf+1.0)
    )/cnumf
    gf = g2f*zf**2
    betaff = pf-gf/(1.0-0.5*gf)
    Opf = np.asarray([
        -ellf*Ogf,
        -ellf*Onf,
        (1.0-ellf)*Obf,
        (betacf-ellf)*Ocf,
        (betaff-ellf)*Off,
    ])
    Tp_float = np.zeros((N_STATE, N_STATE))
    Tp_float[3, 2:6] = Opf[:4]
    Tp_float[3, 11] = Opf[4]
    Tp_float[7, 6] = 2.0*Opf[0]+1.5*Opf[2]
    Tp_float[7, 7] = 2.0*Opf[1]
    Tp_float[7, 12] = 1.5*0.02297*Opf[4]
    Tp_mp_float = np.asarray([
        [float(Tp[row, column]) for column in range(N_STATE)]
        for row in range(N_STATE)
    ])
    float_relative = float(
        np.linalg.norm(Tp_float-Tp_mp_float)
        /max(np.linalg.norm(Tp_mp_float), 1e-300)
    )

    below_1e8 = sum(error < mp.mpf("1e-8") for error in relative_errors)
    best_relative = min(relative_errors)
    checks = {
        "at_least_two_steps_below_1e-8": below_1e8 >= 2,
        "best_relative_below_1e-12": best_relative < mp.mpf("1e-12"),
        "double_analytic_agrees_below_1e-14": float_relative < 1e-14,
        "all_values_finite": bool(
            mp.isfinite(Tp_norm)
            and all(mp.isfinite(error) for error in relative_errors)
            and np.all(np.isfinite(Tp_float))
        ),
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K4 C7.7c-K7a-J2 80-digit Tprime audit",
        "mode_label": args.mode,
        "surface": args.surface,
        "x": str(x),
        "dps": args.dps,
        "Tprime_frobenius_norm": mp.nstr(Tp_norm, 25),
        "step_results": step_results,
        "best_relative_error": mp.nstr(best_relative, 25),
        "double_analytic_relative_error": float_relative,
        "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7A_J2_HIGH_PRECISION_TPRIME"
            if passed else "REVIEW_C7_7C_K7A_J2_TPRIME_UNCLOSED"
        ),
        "physical_verdict": "background-derivative audit only; no evolution",
        "fine_depth": "66.5/100",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic()-started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)
