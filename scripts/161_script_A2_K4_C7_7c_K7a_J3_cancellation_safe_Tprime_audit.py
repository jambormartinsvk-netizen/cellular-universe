#!/usr/bin/env python
"""Bounded K7a-J3 audit of cancellation-safe T-prime coefficients.

No ODE is integrated.  The script compares two algebraically identical
float64 evaluations of ell=B'/B against an 80-digit reference:

legacy: ell = 2*(q+1), q=-1+0.5*B'/B
safe:   ell = denominator_x/denominator

The registered T-prime matrix is then assembled with each ell value.
"""

from __future__ import annotations

import argparse
import json
import math
import time

import mpmath as mp
import numpy as np


N_STATE = 13


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser()
    result.add_argument("--max-runtime-seconds", type=float, required=True)
    result.add_argument("--mode", choices=("NID", "NIV"), required=True)
    result.add_argument("--surface", choices=("deep", "shallow"), required=True)
    result.add_argument("--dps", type=int, default=80)
    return result


def main() -> int:
    args = parser().parse_args()
    if not 0.1 <= args.max_runtime_seconds <= 10.0:
        raise SystemExit("max-runtime-seconds must be in [0.1,10]")
    if args.dps != 80:
        raise SystemExit("J3 preregistration requires exactly 80 dps")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("K7a-J3 cancellation-safe Tprime deadline exceeded")

    mp.mp.dps = args.dps
    x = mp.mpf("-25") if args.surface == "deep" else mp.mpf("-23")
    delta = mp.mpf("0.02297")
    p = mp.mpf("3.93109")
    h0 = mp.mpf("0.6637")
    omega_m0 = mp.mpf("0.3517")
    ombh2 = mp.mpf("0.02237")
    fb = ombh2/(omega_m0*h0**2)
    fc = 1-fb
    neff = mp.mpf("3.046")+mp.mpf("0.0535")
    rn = mp.mpf("0.2271")*neff/(1+mp.mpf("0.2271")*neff)
    rg = 1-rn
    omega_r0 = (
        mp.mpf("2.47282e-5")*(1+mp.mpf("0.2271")*neff)/h0**2
    )
    hubble0_mpc = 100*h0/mp.mpf("299792.458")
    k_mpc = mp.mpf("0.05")
    mu = hubble0_mpc*omega_m0/mp.sqrt(omega_r0)/k_mpc
    g2 = mp.mpf("0.15")*(hubble0_mpc/k_mpc)**2*mp.sqrt(omega_r0)
    transfer_shape = g2*(1/(p+1)-mp.mpf("0.5"))

    z = k_mpc*mp.e**x/(hubble0_mpc*mp.sqrt(omega_r0))
    fuel = z**p
    den = 1+mu*z+fuel*(1+transfer_shape*z**2)
    denx = mu*z+fuel*(p+(p+2)*transfer_shape*z**2)
    ell_mp = denx/den
    Og, On = rg/den, rn/den
    Ob = fb*mu*z/den
    cnum = fc*mu*z+g2*z**(p+2)/(p+1)
    Oc = cnum/den
    Of = fuel*(1-mp.mpf("0.5")*g2*z**2)/den
    beta_c = (fc*mu*z+(p+2)*g2*z**(p+2)/(p+1))/cnum
    g = g2*z**2
    beta_f = p-g/(1-mp.mpf("0.5")*g)

    def tprime_mp(ell: mp.mpf) -> mp.matrix:
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

    reference = tprime_mp(ell_mp)
    reference_np = np.asarray([
        [float(reference[row, column]) for column in range(N_STATE)]
        for row in range(N_STATE)
    ])

    # Independent float64 re-evaluation of the same registered background.
    xf = float(x)
    h0f, omega_m0f, ombh2f = 0.6637, 0.3517, 0.02237
    fbf = ombh2f/(omega_m0f*h0f**2)
    fcf = 1.0-fbf
    nefff = 3.046+0.0535
    rnf = 0.2271*nefff/(1.0+0.2271*nefff)
    rgf = 1.0-rnf
    omega_r0f = 2.47282e-5*(1.0+0.2271*nefff)/h0f**2
    hubble0f = 100.0*h0f/299792.458
    kf, pf = 0.05, 3.93109
    muf = hubble0f*omega_m0f/math.sqrt(omega_r0f)/kf
    g2f = 0.15*(hubble0f/kf)**2*math.sqrt(omega_r0f)
    transferf = g2f*(1.0/(pf+1.0)-0.5)
    zf = kf*math.exp(xf)/(hubble0f*math.sqrt(omega_r0f))
    fuelf = zf**pf
    denf = 1.0+muf*zf+fuelf*(1.0+transferf*zf**2)
    denxf = muf*zf+fuelf*(pf+(pf+2.0)*transferf*zf**2)
    qf = -1.0+0.5*denxf/denf
    ell_legacy = 2.0*(qf+1.0)
    ell_safe = denxf/denf
    Ogf, Onf = rgf/denf, rnf/denf
    Obf = fbf*muf*zf/denf
    cnumf = fcf*muf*zf+g2f*zf**(pf+2.0)/(pf+1.0)
    Ocf = cnumf/denf
    Off = fuelf*(1.0-0.5*g2f*zf**2)/denf
    betacf = (
        fcf*muf*zf+(pf+2.0)*g2f*zf**(pf+2.0)/(pf+1.0)
    )/cnumf
    gf = g2f*zf**2
    betaff = pf-gf/(1.0-0.5*gf)

    def tprime_float(ell: float) -> np.ndarray:
        Op = np.asarray([
            -ell*Ogf,
            -ell*Onf,
            (1.0-ell)*Obf,
            (betacf-ell)*Ocf,
            (betaff-ell)*Off,
        ])
        Tp = np.zeros((N_STATE, N_STATE))
        Tp[3, 2:6] = Op[:4]
        Tp[3, 11] = Op[4]
        Tp[7, 6] = 2.0*Op[0]+1.5*Op[2]
        Tp[7, 7] = 2.0*Op[1]
        Tp[7, 12] = 1.5*0.02297*Op[4]
        return Tp

    legacy = tprime_float(ell_legacy)
    safe = tprime_float(ell_safe)
    reference_norm = max(float(np.linalg.norm(reference_np)), 1e-300)
    legacy_relative = float(np.linalg.norm(legacy-reference_np)/reference_norm)
    safe_relative = float(np.linalg.norm(safe-reference_np)/reference_norm)
    ell_reference = float(ell_mp)
    legacy_ell_relative = abs(ell_legacy-ell_reference)/max(abs(ell_reference), 1e-300)
    safe_ell_relative = abs(ell_safe-ell_reference)/max(abs(ell_reference), 1e-300)
    deadline()

    values = np.asarray([
        ell_reference, ell_legacy, ell_safe, legacy_relative, safe_relative,
        legacy_ell_relative, safe_ell_relative,
    ])
    checks = {
        "all_values_finite": bool(np.all(np.isfinite(values))),
        "safe_Tprime_relative_below_1e-14": safe_relative < 1e-14,
        "safe_ell_relative_below_1e-14": safe_ell_relative < 1e-14,
        "safe_path_better_than_legacy": safe_relative < legacy_relative,
        "legacy_deep_failure_reproduced": (
            legacy_relative > 1e-14 if args.surface == "deep" else True
        ),
    }
    passed = all(checks.values())
    payload = {
        "test": "A2-K4 C7.7c-K7a-J3 cancellation-safe Tprime audit",
        "mode_label": args.mode,
        "surface": args.surface,
        "x": float(x),
        "dps": args.dps,
        "ell": {
            "reference_80_digit": mp.nstr(ell_mp, 25),
            "legacy_q_plus_one": ell_legacy,
            "safe_denominator_ratio": ell_safe,
            "legacy_relative_error": legacy_ell_relative,
            "safe_relative_error": safe_ell_relative,
        },
        "Tprime": {
            "reference_frobenius_norm": reference_norm,
            "legacy_relative_error": legacy_relative,
            "safe_relative_error": safe_relative,
            "legacy_max_abs_error": float(np.max(np.abs(legacy-reference_np))),
            "safe_max_abs_error": float(np.max(np.abs(safe-reference_np))),
        },
        "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7A_J3_CANCELLATION_SAFE_TPRIME"
            if passed else "REVIEW_C7_7C_K7A_J3_TPRIME_UNCLOSED"
        ),
        "physical_verdict": "background-derivative audit only; no evolution",
        "fine_depth": "66.5/100",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic()-started,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

