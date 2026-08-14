#!/usr/bin/env python
"""Bounded 80-digit K7b coefficient, constraint, and projected-RHS audit.

The registered float64 Puiseux coefficients are exported by script 165 after
the exact-zero projection.  This script evaluates them with mpmath, constructs
D and M from the independent metric series, checks species sums and
reconstruction, and compares all 13 projected RHS components with analytic
series derivatives.  It performs no ODE integration.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import subprocess
import sys
import time

import mpmath as mp


HERE = Path(__file__).resolve().parent
STANDARD_NAMES = ("h", "eta", "dg", "dn", "db", "dc", "Ug", "Un", "sig", "L3", "L4")
FUEL_NAMES = ("df", "Uf")
PROJECTED_NAMES = (
    "h", "eta", "delta_gamma", "D", "delta_b", "delta_c",
    "U_gamma", "M", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    parser.add_argument("--source-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--mode", choices=("NID", "NIV"), required=True)
    parser.add_argument("--surface", choices=("deep", "shallow"), required=True)
    parser.add_argument("--dps", type=int, default=80)
    return parser


def parse_json(text: str) -> dict[str, object]:
    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError("coefficient exporter returned no JSON")
    return json.loads(text[start:end+1])


def main() -> int:
    args = build_parser().parse_args()
    if not 2.0 <= args.max_runtime_seconds <= 15.0:
        raise SystemExit("max-runtime-seconds must be in [2,15]")
    if not 1.0 <= args.source_runtime_seconds <= 8.0:
        raise SystemExit("source-runtime-seconds must be in [1,8]")
    if args.dps != 80:
        raise SystemExit("K7b.1 preregistration requires exactly 80 dps")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic()-started > args.max_runtime_seconds:
            raise TimeoutError("K7b.1 coefficient audit deadline exceeded")

    source_command = [
        sys.executable,
        str(HERE/"165_script_A2_K4_C7_7c_K7b_registered_coefficient_export.py"),
        "--max-runtime-seconds", str(args.source_runtime_seconds),
        "--standard-order", "6",
        "--x-deep", "-25",
        "--x-shallow", "-23",
        "--x-reference", "-18",
        "--k-mpc", "0.05",
        "--fuel-fraction-coefficient", "1",
    ]
    child = subprocess.run(
        source_command,
        capture_output=True,
        text=True,
        timeout=args.source_runtime_seconds+1.0,
        check=False,
    )
    source = parse_json(child.stdout)
    deadline()

    mp.mp.dps = args.dps

    def m(value: object) -> mp.mpf:
        return mp.mpf(str(value))

    registry_all = dict(source.get("K7b_coefficient_registry", {}))
    registry = dict(registry_all.get(args.mode, {}))
    standard = dict(registry.get("standard", {}))
    fractional = dict(registry.get("fractional", {}))
    fuel = dict(registry.get("fuel", {}))

    def evaluate(series: dict[str, object], z: mp.mpf, offset: mp.mpf, order: int) -> mp.mpf:
        terms = []
        for raw_power, raw_coefficient in series.items():
            exponent = m(raw_power)+offset
            coefficient = m(raw_coefficient)
            terms.append(coefficient*(exponent**order)*(z**exponent))
        return mp.fsum(terms)

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
    omega_r0 = mp.mpf("2.47282e-5")*(1+mp.mpf("0.2271")*neff)/h0**2
    hubble0_mpc = 100*h0/mp.mpf("299792.458")
    k_mpc = mp.mpf("0.05")
    mu = hubble0_mpc*omega_m0/mp.sqrt(omega_r0)/k_mpc
    g2 = mp.mpf("0.15")*(hubble0_mpc/k_mpc)**2*mp.sqrt(omega_r0)
    transfer_shape = g2*(1/(p+1)-mp.mpf("0.5"))
    x = mp.mpf("-25") if args.surface == "deep" else mp.mpf("-23")
    z = k_mpc*mp.e**x/(hubble0_mpc*mp.sqrt(omega_r0))
    fuel_piece = z**p
    denominator = 1+mu*z+fuel_piece*(1+transfer_shape*z**2)
    denominator_x = mu*z+fuel_piece*(p+(p+2)*transfer_shape*z**2)
    ell = denominator_x/denominator
    q = -1+ell/2
    s2 = z**2/denominator
    s2_x = (2-ell)*s2
    Og = rg/denominator
    On = rn/denominator
    Ob = fb*mu*z/denominator
    Oc = (fc*mu*z+g2*z**(p+2)/(p+1))/denominator
    Of = fuel_piece*(1-g2*z**2/2)/denominator
    loading = 3*fb*mu*z/(4*rg)
    inv1r = 1/(1+loading)
    load_fraction = loading*inv1r
    g = g2*z**2
    gr = g2/(fc*mu)*z**(p+1)
    c_numerator = fc*mu*z+g2*z**(p+2)/(p+1)
    beta_c = (fc*mu*z+(p+2)*g2*z**(p+2)/(p+1))/c_numerator
    beta_f = p-g/(1-g/2)

    def total(name: str, order: int = 0) -> mp.mpf:
        return evaluate(dict(standard[name]), z, mp.mpf("0"), order) + evaluate(
            dict(fractional[name]), z, p, order
        )

    def fuel_value(name: str, order: int = 0) -> mp.mpf:
        return evaluate(dict(fuel[name]), z, mp.mpf("0"), order)

    h, eta = total("h"), total("eta")
    dg, dn, db, dc = total("dg"), total("dn"), total("db"), total("dc")
    Ug, Un = total("Ug"), total("Un")
    sig, L3, L4 = total("sig"), total("L3"), total("L4")
    df, Uf = fuel_value("df"), fuel_value("Uf")
    hx, etax = total("h", 1), total("eta", 1)
    hxx, etaxx = total("h", 2), total("eta", 2)

    D_metric = (hx-2*s2*eta)/3
    M_metric = etax
    density_terms = (Og*dg, On*dn, Ob*db, Oc*dc, Of*df)
    momentum_terms = (
        (2*Og+mp.mpf("1.5")*Ob)*Ug,
        2*On*Un,
        mp.mpf("1.5")*delta*Of*Uf,
    )
    D_species = mp.fsum(density_terms)
    M_species = mp.fsum(momentum_terms)
    density_scale = max(mp.fsum(abs(value) for value in density_terms), abs(D_metric), mp.mpf("1e-300"))
    momentum_scale = max(mp.fsum(abs(value) for value in momentum_terms), abs(M_metric), mp.mpf("1e-300"))
    density_scaled_residual = abs(D_species-D_metric)/density_scale
    momentum_scaled_residual = abs(M_species-M_metric)/momentum_scale

    Wg = 2*Og+mp.mpf("1.5")*Ob
    Wf = mp.mpf("1.5")*delta*Of
    dn_reconstructed = (D_metric-Og*dg-Ob*db-Oc*dc-Of*df)/On
    Un_reconstructed = (M_metric-Wg*Ug-Wf*Uf)/(2*On)
    dn_reconstruction_error = abs(dn_reconstructed-dn)/max(1, abs(dn))
    Un_reconstruction_error = abs(Un_reconstructed-Un)/max(1, abs(Un))

    metric_00_residual = abs(hx-(3*D_metric+2*s2*eta))
    metric_0i_residual = abs(etax-M_metric)

    Ah = mp.mpf("2")/3*(Og+On)+mp.mpf("0.5")*(Ob+Oc)+mp.mpf("0.5")*delta*Of
    projected = (h, eta, dg, D_metric, db, dc, Ug, M_metric, sig, L3, L4, df, Uf)
    hp, etap, dgp, Dp, dbp, dcp, Ugp, Mp, sigp, L3p, L4p, dfp, Ufp = projected
    dnp = (Dp-Og*dgp-Ob*dbp-Oc*dcp-Of*dfp)/On
    Unp = (Mp-Wg*Ugp-Wf*Ufp)/(2*On)
    hx_rhs = 3*Dp+2*s2*etap
    eta_rhs = Mp
    dg_rhs = -mp.mpf("4")/3*s2*Ugp-mp.mpf("2")/3*hx_rhs
    D_rhs = (
        -ell*Dp+Ob*dbp+beta_c*Oc*dcp+beta_f*Of*dfp
        -mp.mpf("2")/3*s2*Mp-Ah*hx_rhs+Oc*gr*(dfp-dcp)
        +Of*(-3*(2-delta)*dfp-9*delta*(2-delta)*Ufp-3*(2-delta)*g*Ufp)
    )
    db_rhs = -s2*Ugp-hx_rhs/2
    dc_rhs = -hx_rhs/2+gr*(dfp-dcp)
    Ug_rhs = q*Ugp-load_fraction*Ugp+mp.mpf("0.25")*inv1r*dgp
    M_rhs = (
        (-q-2)*Mp+Dp/2+(mp.mpf("1.5")*Ob-Wg*load_fraction)*Ugp
        +(mp.mpf("0.25")*Wg*inv1r-mp.mpf("0.5")*Og)*dgp
        -mp.mpf("0.5")*Ob*dbp-mp.mpf("0.5")*Oc*dcp+Of*dfp
        -2*On*sigp+(mp.mpf("1.5")*delta*Of*(beta_f+2)+3*Of*g)*Ufp
    )
    sig_rhs = mp.mpf("2")/15*hx_rhs+mp.mpf("4")/5*eta_rhs+mp.mpf("4")/15*s2*Unp-mp.mpf("3")/10*L3p
    L3_rhs = -q*L3p+mp.mpf("6")/7*s2*sigp-mp.mpf("4")/7*L4p
    L4_rhs = -2*q*L4p+mp.mpf("4")/9*s2*L3p
    df_rhs = -3*(2-delta)*dfp-delta*s2*Ufp-delta*hx_rhs/2-9*delta*(2-delta)*Ufp-3*(2-delta)*g*Ufp
    Uf_rhs = (q+2)*Ufp+dfp/delta+2*g*Ufp/delta
    rhs_values = (
        hx_rhs, eta_rhs, dg_rhs, D_rhs, db_rhs, dc_rhs, Ug_rhs,
        M_rhs, sig_rhs, L3_rhs, L4_rhs, df_rhs, Uf_rhs,
    )

    D_series_x = (hxx-2*(s2_x*eta+s2*etax))/3
    derivative_values = (
        hx, etax, total("dg", 1), D_series_x, total("db", 1),
        total("dc", 1), total("Ug", 1), etaxx, total("sig", 1),
        total("L3", 1), total("L4", 1), fuel_value("df", 1),
        fuel_value("Uf", 1),
    )
    rhs_audit: dict[str, dict[str, object]] = {}
    worst_rhs_ratio = mp.mpf("0")
    for name, rhs_value, derivative_value in zip(PROJECTED_NAMES, rhs_values, derivative_values):
        residual = abs(rhs_value-derivative_value)
        allowance = mp.mpf("5e-12")+mp.mpf("5e-8")*max(abs(rhs_value), abs(derivative_value))
        ratio = residual/allowance
        worst_rhs_ratio = max(worst_rhs_ratio, ratio)
        rhs_audit[name] = {
            "rhs": mp.nstr(rhs_value, 20),
            "series_derivative": mp.nstr(derivative_value, 20),
            "absolute_residual": mp.nstr(residual, 20),
            "allowance": mp.nstr(allowance, 20),
            "residual_over_allowance": float(ratio),
            "pass": bool(ratio < 1),
        }

    surfaces = dict(source.get("BR3C_state_surfaces", {}))
    mode_surfaces = dict(dict(surfaces.get(args.mode, {})).get("surfaces", {}))
    exported_surface = dict(mode_surfaces.get(args.surface, {}))
    exported_state = dict(exported_surface.get("state", {}))
    source_z_relative = abs(z-m(exported_surface.get("z", "nan")))/max(abs(z), mp.mpf("1e-300"))
    evaluated_state = {
        "h": h, "eta": eta, "delta_gamma": dg, "delta_fs": dn,
        "delta_b": db, "delta_c": dc, "U_gamma": Ug, "U_fs": Un,
        "sigma_fs": sig, "L3_fs": L3, "L4_fs": L4, "delta_f": df,
        "U_f": Uf, "h_x": hx, "eta_x": etax,
    }
    state_comparison: dict[str, dict[str, object]] = {}
    worst_state_ratio = mp.mpf("0")
    for name, value in evaluated_state.items():
        exported = m(exported_state.get(name, "nan"))
        residual = abs(value-exported)
        allowance = mp.mpf("5e-14")+mp.mpf("5e-12")*max(abs(value), abs(exported))
        ratio = residual/allowance
        worst_state_ratio = max(worst_state_ratio, ratio)
        state_comparison[name] = {
            "high_precision": mp.nstr(value, 20),
            "exported_float64": mp.nstr(exported, 20),
            "residual_over_allowance": float(ratio),
            "pass": bool(ratio < 1),
        }

    finite_values = list(projected)+list(rhs_values)+list(derivative_values)+[
        D_species, M_species, dn_reconstructed, Un_reconstructed,
    ]
    exact_standard_names = set(standard) == set(STANDARD_NAMES)
    exact_fractional_names = set(fractional) == set(STANDARD_NAMES)
    exact_fuel_names = set(fuel) == set(FUEL_NAMES)
    checks = {
        "source_child_exit_zero": child.returncode == 0,
        "source_export_pass": source.get("execution_verdict") == "PASS_C7_7C_K4_ANALYTIC_REFERENCE_STATE",
        "registered_standard_names_exact": exact_standard_names,
        "registered_fractional_names_exact": exact_fractional_names,
        "registered_fuel_names_exact": exact_fuel_names,
        "source_z_relative_below_5e-14": source_z_relative < mp.mpf("5e-14"),
        "state_reconstruction_within_registered_tolerance": worst_state_ratio < 1,
        "density_species_constraint_scaled_below_5e-12": density_scaled_residual < mp.mpf("5e-12"),
        "momentum_species_constraint_scaled_below_5e-12": momentum_scaled_residual < mp.mpf("5e-12"),
        "delta_fs_reconstruction_scaled_below_5e-12": dn_reconstruction_error < mp.mpf("5e-12"),
        "U_fs_reconstruction_scaled_below_5e-12": Un_reconstruction_error < mp.mpf("5e-12"),
        "metric_00_identity_below_1e-60": metric_00_residual < mp.mpf("1e-60"),
        "metric_0i_identity_below_1e-60": metric_0i_residual < mp.mpf("1e-60"),
        "all_13_projected_rhs_components_within_allowance": worst_rhs_ratio < 1,
        "all_values_finite": all(mp.isfinite(value) for value in finite_values),
    }
    passed = all(bool(value) for value in checks.values())
    deadline()

    payload = {
        "test": "A2-K4 C7.7c-K7b.1 high-precision coefficient and constraint audit",
        "profile_request": {"mode": args.mode, "surface": args.surface, "x": float(x)},
        "source": {
            "script": "165_script_A2_K4_C7_7c_K7b_registered_coefficient_export.py",
            "return_code": child.returncode,
            "execution_verdict": source.get("execution_verdict"),
            "coefficient_precision_scope": "registered float64 coefficients evaluated and summed at 80 dps",
        },
        "background": {
            "z_80_digit": mp.nstr(z, 25),
            "source_z_relative_error": float(source_z_relative),
            "ell_safe": mp.nstr(ell, 25),
            "Omega_fs": mp.nstr(On, 25),
        },
        "projected_seeds": {
            "D_metric": mp.nstr(D_metric, 25),
            "D_species": mp.nstr(D_species, 25),
            "density_scaled_residual": float(density_scaled_residual),
            "density_cancellation_condition": mp.nstr(density_scale/max(abs(D_metric), mp.mpf("1e-300")), 12),
            "M_metric": mp.nstr(M_metric, 25),
            "M_species": mp.nstr(M_species, 25),
            "momentum_scaled_residual": float(momentum_scaled_residual),
            "momentum_cancellation_condition": mp.nstr(momentum_scale/max(abs(M_metric), mp.mpf("1e-300")), 12),
            "delta_fs_reconstruction_error": float(dn_reconstruction_error),
            "U_fs_reconstruction_error": float(Un_reconstruction_error),
            "metric_00_absolute_residual": mp.nstr(metric_00_residual, 12),
            "metric_0i_absolute_residual": mp.nstr(metric_0i_residual, 12),
        },
        "state_comparison": state_comparison,
        "projected_rhs_audit": rhs_audit,
        "worst_state_residual_over_allowance": float(worst_state_ratio),
        "worst_rhs_residual_over_allowance": float(worst_rhs_ratio),
        "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7B1_COEFFICIENT_CONSTRAINT_AUDIT"
            if passed else "REVIEW_C7_7C_K7B1_COEFFICIENT_CONSTRAINT_UNCLOSED"
        ),
        "physical_verdict": "coefficient and initial-constraint gate only; no ODE evolution",
        "fine_depth": "66.5/100",
        "runtime_limits_seconds": {
            "total": args.max_runtime_seconds,
            "source": args.source_runtime_seconds,
        },
        "runtime_seconds": time.monotonic()-started,
        "source_stderr_tail": child.stderr[-500:],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

