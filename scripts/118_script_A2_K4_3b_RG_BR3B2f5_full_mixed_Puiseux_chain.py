#!/usr/bin/env python
"""BR3B-2f-5: full mixed matter/fuel Puiseux chain through common fuel.

The calculation is first order in the early fuel fraction Phi*z**p, but exact
in the retained integer matter series.  It solves, in x=ln(a), the standard
NID/NIV seed, the regular fuel test field, and the induced fractional response
for nine radiation/Einstein rows plus carried baryon and CDM continuities.

NID layers: p, p+1, p+2, p+3.
NIV layers: p-1, p, p+1, p+2.

The zero-matter limit is compared with scripts 104 and 108.  Ash transfer and
the fractional l=3 feedback enter after the common-fuel layer and are outside
this bounded step, as proven by script 116.  Any numerical problem is
UNCLOSED, never a physical death verdict.
"""

from __future__ import annotations

import argparse
import json
import math
import time

import numpy as np


VARS = ("h", "eta", "dg", "dn", "db", "dc", "Ug", "Un", "sig")
CORE_ROWS = ("gamma_continuity", "gamma_Euler", "nu_continuity",
             "nu_shear", "nu_Euler", "Einstein_00", "Einstein_0i",
             "Einstein_trace", "Einstein_traceless")
CARRY_ROWS = ("baryon_continuity", "cdm_continuity")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=15.0)
    parser.add_argument("--standard-order", type=int, default=4)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 20.0:
        parser.error("runtime must be in (0,20]")
    if not 4 <= args.standard_order <= 6:
        parser.error("standard order must be in [4,6]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("BR3B-2f-5 deadline exceeded")

    delta = 0.02297
    p = 4 - 3 * delta
    h0 = 0.6637
    omega_m0 = 0.3517
    ombh2 = 0.02237
    total_matter_h2 = omega_m0 * h0**2
    fb = ombh2 / total_matter_h2
    fc = 1 - fb
    neff = 3.046 + 0.0535
    rn = 0.2271 * neff / (1 + 0.2271 * neff)
    rg = 1 - rn
    omega_gamma_h2 = 2.47282e-5
    omega_r0 = omega_gamma_h2 * (1 + 0.2271 * neff) / h0**2
    hubble0_mpc = 100 * h0 / 299792.458
    omega_parameter = hubble0_mpc * omega_m0 / math.sqrt(omega_r0)
    physical_mu = omega_parameter / 0.05

    s_lo, s_hi = -2, args.standard_order + 4

    def clean(series, lo=s_lo, hi=s_hi):
        return {int(k): float(v) for k, v in series.items()
                if lo <= k <= hi and abs(v) > 1e-300}

    def sadd(*items):
        out = {}
        for item in items:
            for k, v in item.items():
                if s_lo <= k <= s_hi:
                    out[k] = out.get(k, 0.0) + v
        return clean(out)

    def sscale(item, factor):
        return clean({k: factor * v for k, v in item.items()})

    def smul(first, second):
        out = {}
        for i, a in first.items():
            for j, b in second.items():
                if s_lo <= i + j <= s_hi:
                    out[i + j] = out.get(i + j, 0.0) + a * b
        return clean(out)

    def sdx(item):
        return clean({k: k * v for k, v in item.items()})

    def sinv(item):
        entries = [(k, v) for k, v in item.items() if abs(v) > 1e-15]
        if not entries:
            raise ZeroDivisionError("zero standard series")
        lead_k, lead = min(entries)
        out = {-lead_k: 1 / lead}
        for n in range(1, s_hi + lead_k + 1):
            total = sum(item.get(lead_k + j, 0.0)
                        * out.get(-lead_k + n - j, 0.0)
                        for j in range(1, n + 1))
            out[-lead_k + n] = -total / lead
        return clean(out)

    def scoef(item, k):
        return float(item.get(k, 0.0))

    def standard_background(mu):
        denominator = {0: 1.0, 1: mu}
        invd = sinv(denominator)
        q = sadd({0: -1.0}, sscale(smul({1: mu}, invd), 0.5))
        s2 = smul({2: 1.0}, invd)
        og, on = sscale(invd, rg), sscale(invd, rn)
        ob = sscale(smul({1: mu}, invd), fb)
        oc = sscale(smul({1: mu}, invd), fc)
        loading = {1: 3 * fb * mu / (4 * rg)}
        inv1r = sinv(sadd({0: 1.0}, loading))
        load_fraction = smul(loading, inv1r)
        return {"D": denominator, "invD": invd, "q": q, "s2": s2,
                "Og": og, "On": on, "Ob": ob, "Oc": oc,
                "loading": loading, "inv1R": inv1r,
                "load_fraction": load_fraction}

    def standard_rows(v, bg):
        hx, etax = sdx(v["h"]), sdx(v["eta"])
        hxx, etaxx = sdx(hx), sdx(etax)
        density = sadd(smul(bg["Og"], v["dg"]), smul(bg["On"], v["dn"]),
                       smul(bg["Ob"], v["db"]), smul(bg["Oc"], v["dc"]))
        rows = {
            "gamma_continuity": sadd(sdx(v["dg"]), sscale(smul(bg["s2"], v["Ug"]), 4/3), sscale(hx, 2/3)),
            "gamma_Euler": sadd(sdx(v["Ug"]), sscale(smul(bg["q"], v["Ug"]), -1),
                                 smul(bg["load_fraction"], v["Ug"]),
                                 sscale(smul(bg["inv1R"], v["dg"]), -0.25)),
            "nu_continuity": sadd(sdx(v["dn"]), sscale(smul(bg["s2"], v["Un"]), 4/3), sscale(hx, 2/3)),
            "nu_shear": sadd(sscale(sdx(v["sig"]), 2), sscale(hx, -4/15),
                              sscale(etax, -8/5), sscale(smul(bg["s2"], v["Un"]), -8/15)),
            "nu_Euler": sadd(sdx(v["Un"]), sscale(smul(bg["q"], v["Un"]), -1),
                              sscale(v["dn"], -0.25), v["sig"]),
            "baryon_continuity": sadd(sdx(v["db"]), smul(bg["s2"], v["Ug"]), sscale(hx, 0.5)),
            "cdm_continuity": sadd(sdx(v["dc"]), sscale(hx, 0.5)),
            "Einstein_00": sadd(sscale(hx, -0.5), sscale(density, 1.5), smul(bg["s2"], v["eta"])),
            "Einstein_0i": sadd(etax, sscale(smul(bg["Og"], v["Ug"]), -2),
                                 sscale(smul(bg["On"], v["Un"]), -2),
                                 sscale(smul(bg["Ob"], v["Ug"]), -1.5)),
            "Einstein_trace": sadd(hxx, smul(sadd(bg["q"], {0: 2.0}), hx),
                                    sscale(smul(bg["s2"], v["eta"]), -2),
                                    sscale(smul(bg["Og"], v["dg"]), 3),
                                    sscale(smul(bg["On"], v["dn"]), 3)),
            "Einstein_traceless": sadd(hxx, smul(sadd(bg["q"], {0: 2.0}), hx),
                                        sscale(sadd(etaxx, smul(sadd(bg["q"], {0: 2.0}), etax)), 6),
                                        sscale(smul(bg["s2"], v["eta"]), -2),
                                        sscale(smul(bg["On"], v["sig"]), 12)),
        }
        return rows

    std_exponents = list(range(-1, args.standard_order + 1))
    std_index = {(name, k): i for i, (name, k) in enumerate(
        (pair for name in VARS for pair in ((name, e) for e in std_exponents)))}
    std_unknowns = len(std_index)

    def vector_to_standard(vector):
        return {name: {e: vector[std_index[(name, e)]] for e in std_exponents}
                for name in VARS}

    def solve_standard(mode, mu):
        bg = standard_background(mu)
        initial = []
        if mode == "NID":
            values_minus = {name: 0.0 for name in VARS}
            values_zero = {"h": 0.0, "eta": 0.0, "dg": -rn/rg, "dn": 1.0,
                           "db": 0.0, "dc": 0.0, "Ug": -rn/(4*rg),
                           "Un": 0.25, "sig": 0.0}
            initial.extend((name, -1, value) for name, value in values_minus.items())
            initial.extend((name, 0, value) for name, value in values_zero.items())
        else:
            values_minus = {name: 0.0 for name in VARS}
            values_minus.update({"Ug": -3*rn/(4*rg), "Un": 0.75})
            initial.extend((name, -1, value) for name, value in values_minus.items())
            for name in ("h", "eta", "dg", "dn", "db", "dc", "sig"):
                initial.append((name, 0, 0.0))

        def ledger(vector):
            rows = standard_rows(vector_to_standard(vector), bg)
            out = []
            for row in CORE_ROWS + CARRY_ROWS:
                out.extend(scoef(rows[row], e) for e in std_exponents)
            out.extend(vector[std_index[(name, e)]] - value for name, e, value in initial)
            return np.asarray(out, float)

        zero = np.zeros(std_unknowns); constant = ledger(zero)
        matrix = np.empty((constant.size, std_unknowns))
        for column in range(std_unknowns):
            basis = np.zeros(std_unknowns); basis[column] = 1.0
            matrix[:, column] = ledger(basis) - constant
        rhs = -constant
        solution, _, rank, singular = np.linalg.lstsq(matrix, rhs, rcond=None)
        residual = matrix @ solution - rhs
        scale = max(np.max(np.abs(matrix) * np.maximum(np.abs(solution)[None, :], 1e-300)),
                    np.max(np.abs(rhs)), 1e-300)
        standard = vector_to_standard(solution)
        target = 3 if mode == "NID" else 2
        _, _, vh = np.linalg.svd(matrix, full_matrices=False)
        null = vh[-1] if rank < std_unknowns else np.zeros(std_unknowns)
        lower_null = max(abs(null[std_index[(name, e)]])
                         for name in VARS for e in std_exponents if e <= target)
        return standard, bg, {"rank": int(rank), "unknowns": std_unknowns,
                              "condition_resolved": float(singular[0]/singular[max(rank-1, 0)]),
                              "scaled_residual": float(np.max(np.abs(residual))/scale),
                              "lower_null_max": float(lower_null)}

    def solve_fuel(standard, bg):
        fuel_index = {(name, e): i for i, (name, e) in enumerate(
            (pair for name in ("df", "Uf") for pair in ((name, x) for x in std_exponents)))}
        count = len(fuel_index)
        hx = sdx(standard["h"])

        def unpack(vector):
            return {name: {e: vector[fuel_index[(name, e)]] for e in std_exponents}
                    for name in ("df", "Uf")}

        def ledger(vector):
            f = unpack(vector)
            r1 = sadd(sdx(f["df"]), sscale(f["df"], 3*(2-delta)),
                      sscale(smul(bg["s2"], f["Uf"]), delta), sscale(hx, delta/2),
                      sscale(f["Uf"], 9*delta*(2-delta)))
            r2 = sadd(sdx(f["Uf"]), sscale(smul(sadd(bg["q"], {0: 2.0}), f["Uf"]), -1),
                      sscale(f["df"], -1/delta))
            out = [scoef(row, e) for row in (r1, r2) for e in std_exponents]
            out.extend([vector[fuel_index[("df", -1)]], vector[fuel_index[("Uf", -1)]],
                        vector[fuel_index[("df", 0)]], vector[fuel_index[("Uf", 0)]])
            return np.asarray(out, float)

        zero = np.zeros(count); constant = ledger(zero)
        matrix = np.empty((constant.size, count))
        for col in range(count):
            basis = np.zeros(count); basis[col] = 1
            matrix[:, col] = ledger(basis) - constant
        solution, _, rank, singular = np.linalg.lstsq(matrix, -constant, rcond=None)
        residual = matrix @ solution + constant
        scale = max(np.max(np.abs(matrix) * np.maximum(np.abs(solution)[None, :], 1e-300)),
                    np.max(np.abs(constant)), 1e-300)
        return unpack(solution), {"rank": int(rank), "unknowns": count,
                                  "scaled_residual": float(np.max(np.abs(residual))/scale),
                                  "condition": float(singular[0]/singular[-1])}

    # Pair algebra: (integer standard series, first-order Phi*z**(p+j) series).
    def solve_fractional(mode, mu, standard, fuel, f_min, f_max):
        f_lo, f_hi = f_min - 3, f_max + 3

        def fclean(item):
            return {int(k): float(v) for k, v in item.items()
                    if f_lo <= k <= f_hi and abs(v) > 1e-300}

        def fadd(*items):
            out = {}
            for item in items:
                for k, v in item.items():
                    if f_lo <= k <= f_hi:
                        out[k] = out.get(k, 0.0) + v
            return fclean(out)

        def fscale(item, factor):
            return fclean({k: factor*v for k, v in item.items()})

        def sfmul(std, frac):
            out = {}
            for i, a in std.items():
                for j, b in frac.items():
                    if f_lo <= i+j <= f_hi:
                        out[i+j] = out.get(i+j, 0.0) + a*b
            return fclean(out)

        def padd(*pairs):
            return (sadd(*(q[0] for q in pairs)), fadd(*(q[1] for q in pairs)))

        def pscale(pair, factor):
            return (sscale(pair[0], factor), fscale(pair[1], factor))

        def pmul(a, b):
            return (smul(a[0], b[0]), fadd(sfmul(a[0], b[1]), sfmul(b[0], a[1])))

        def pinv(pair):
            si = sinv(pair[0])
            fi = fscale(sfmul(si, sfmul(si, pair[1])), -1)
            return si, fi

        def pdx(pair):
            return sdx(pair[0]), fclean({j: (p+j)*v for j, v in pair[1].items()})

        D = ({0: 1.0, 1: mu}, {0: 1.0})
        invD = pinv(D)
        Dx = pdx(D)
        q = padd(({0: -1.0}, {}), pscale(pmul(Dx, invD), 0.5))
        s2 = pmul(({2: 1.0}, {}), invD)
        Og, On = pscale(invD, rg), pscale(invD, rn)
        Ob = pmul(({1: fb*mu}, {}), invD)
        Oc = pmul(({1: fc*mu}, {}), invD)
        Of = pmul(({}, {0: 1.0}), invD)
        loading = ({1: 3*fb*mu/(4*rg)}, {})
        inv1r = pinv(padd(({0: 1.0}, {}), loading))
        load_fraction = pmul(loading, inv1r)
        fuel_df = (fuel["df"], {})
        fuel_uf = (fuel["Uf"], {})
        fuel_pf = (sadd(fuel["df"], sscale(fuel["Uf"], 3*delta*(2-delta))), {})

        frac_exponents = list(range(f_min, f_max+1))
        findex = {(name, j): i for i, (name, j) in enumerate(
            (pair for name in VARS for pair in ((name, e) for e in frac_exponents)))}
        count = len(findex)

        def variables(vector):
            return {name: (standard[name], {j: vector[findex[(name, j)]] for j in frac_exponents})
                    for name in VARS}

        def row_pairs(vector):
            v = variables(vector)
            hx, etax = pdx(v["h"]), pdx(v["eta"])
            hxx, etaxx = pdx(hx), pdx(etax)
            density = padd(pmul(Og, v["dg"]), pmul(On, v["dn"]),
                           pmul(Ob, v["db"]), pmul(Oc, v["dc"]), pmul(Of, fuel_df))
            return {
                "gamma_continuity": padd(pdx(v["dg"]), pscale(pmul(s2, v["Ug"]), 4/3), pscale(hx, 2/3)),
                "gamma_Euler": padd(pdx(v["Ug"]), pscale(pmul(q, v["Ug"]), -1),
                                     pmul(load_fraction, v["Ug"]), pscale(pmul(inv1r, v["dg"]), -0.25)),
                "nu_continuity": padd(pdx(v["dn"]), pscale(pmul(s2, v["Un"]), 4/3), pscale(hx, 2/3)),
                "nu_shear": padd(pscale(pdx(v["sig"]), 2), pscale(hx, -4/15),
                                  pscale(etax, -8/5), pscale(pmul(s2, v["Un"]), -8/15)),
                "nu_Euler": padd(pdx(v["Un"]), pscale(pmul(q, v["Un"]), -1),
                                  pscale(v["dn"], -0.25), v["sig"]),
                "baryon_continuity": padd(pdx(v["db"]), pmul(s2, v["Ug"]), pscale(hx, 0.5)),
                "cdm_continuity": padd(pdx(v["dc"]), pscale(hx, 0.5)),
                "Einstein_00": padd(pscale(hx, -0.5), pscale(density, 1.5), pmul(s2, v["eta"])),
                "Einstein_0i": padd(etax, pscale(pmul(Og, v["Ug"]), -2),
                                     pscale(pmul(On, v["Un"]), -2),
                                     pscale(pmul(Ob, v["Ug"]), -1.5),
                                     pscale(pmul(Of, fuel_uf), -1.5*delta)),
                "Einstein_trace": padd(hxx, pmul(padd(q, ({0: 2.0}, {})), hx),
                                        pscale(pmul(s2, v["eta"]), -2),
                                        pscale(pmul(Og, v["dg"]), 3),
                                        pscale(pmul(On, v["dn"]), 3),
                                        pscale(pmul(Of, fuel_pf), 9)),
                "Einstein_traceless": padd(hxx, pmul(padd(q, ({0: 2.0}, {})), hx),
                                            pscale(padd(etaxx, pmul(padd(q, ({0: 2.0}, {})), etax)), 6),
                                            pscale(pmul(s2, v["eta"]), -2),
                                            pscale(pmul(On, v["sig"]), 12)),
            }

        def ledger(vector, split=False):
            rows = row_pairs(vector)
            if split:
                return {row: np.asarray([rows[row][1].get(j, 0.0) for j in frac_exponents], float)
                        for row in CORE_ROWS + CARRY_ROWS}
            return np.asarray([rows[row][1].get(j, 0.0)
                               for row in CORE_ROWS + CARRY_ROWS for j in frac_exponents], float)

        zero = np.zeros(count); constant = ledger(zero)
        matrix = np.empty((constant.size, count))
        for col in range(count):
            basis = np.zeros(count); basis[col] = 1
            matrix[:, col] = ledger(basis) - constant
        rhs = -constant
        solution, _, rank, singular = np.linalg.lstsq(matrix, rhs, rcond=None)
        residual = matrix @ solution - rhs
        scale = max(np.max(np.abs(matrix) * np.maximum(np.abs(solution)[None, :], 1e-300)),
                    np.max(np.abs(rhs)), 1e-300)
        row_residuals = ledger(solution, split=True)
        frac = {name: {j: solution[findex[(name, j)]] for j in frac_exponents}
                for name in VARS}
        layers = {}
        for j in frac_exponents:
            layers[str(j)] = {"power": p+j, "h_x": (p+j)*frac["h"][j],
                              "eta": frac["eta"][j], "delta_gamma": frac["dg"][j],
                              "delta_fs": frac["dn"][j], "delta_b": frac["db"][j],
                              "delta_c": frac["dc"][j], "U_gamma": frac["Ug"][j],
                              "U_fs": frac["Un"][j], "sigma_fs": frac["sig"][j]}
        return {"rank": int(rank), "unknowns": count,
                "condition": float(singular[0]/singular[-1]),
                "scaled_residual": float(np.max(np.abs(residual))/scale),
                "row_max_abs_residuals": {row: float(np.max(np.abs(vals)))
                                           for row, vals in row_residuals.items()},
                "layers": layers, "raw": frac, "matrix_shape": list(matrix.shape)}

    def expected_108(mode):
        m = 2 if mode == "NID" else 1
        r = p + m
        if mode == "NID":
            dg, dn = rn/(6*rg), -1/6
            ugl, unl = -rn/(4*rg), 1/4
            sig, eta = 1/(2*(4*rn+15)), -rn/(6*(4*rn+15))
        else:
            dg, dn = rn/rg, -1.0
            ugl, unl = -3*rn/(4*rg), 0.75
            sig, eta = 1/(4*rn+5), -rn/(4*rn+5)
        etax = m*eta
        ugm = dg/(4*(m+1)); unm = (dn/4-sig)/(m+1)
        early = p+m-2; factor = p/(2*(early+1))
        uge, une = factor*ugl, factor*unl
        jgc, jnc = 4/3*(ugl-uge), 4/3*(unl-une)
        jge, jne = p*ugm/2, p*unm/2
        jns = 8/15*(uge-ugl)
        A = np.array([
          [2/3,0,r,0,0,0,0], [0,0,-1/4,0,r+1,0,0],
          [2/3,0,0,r,0,0,0], [-4/15,-8/5*r,0,0,0,0,2*r],
          [0,0,0,-1/4,0,r+1,1], [-1/2,0,1.5*rg,1.5*rn,0,0,0],
          [0,r,0,0,-2*rg,-2*rn,0], [r+1,0,3*rg,3*rn,0,0,0],
          [r+1,6*r*(r+1),0,0,0,0,12*rn]], float)
        b = np.array([jgc,jge,jnc,jns,jne,0,-etax,0,-3*p*etax+12*rn*sig], float)
        return np.linalg.lstsq(A,b,rcond=None)[0]

    checks = {}; results = {}
    reference_115 = {
        "NID": {"eta_x_over_hx": 1.1610070337533902,
                "U_gamma_over_hx": -0.7500183459312861,
                "U_fs_over_hx": 0.8005345632321309},
        "NIV": {"eta_x_over_hx": 0.86562563393663,
                "U_gamma_over_hx": -0.428967091735373,
                "U_fs_over_hx": -0.07221830142410335},
    }
    for mode in ("NID", "NIV"):
        n = 3 if mode == "NID" else 2
        fmin = 0 if mode == "NID" else -1
        std, bg, std_meta = solve_standard(mode, physical_mu)
        fuel, fuel_meta = solve_fuel(std, bg)
        hx_n = n*std["h"].get(n, 0.0)
        std_ratios = {"eta_x_over_hx": n*std["eta"].get(n,0.0)/hx_n,
                      "U_gamma_over_hx": std["Ug"].get(n,0.0)/hx_n,
                      "U_fs_over_hx": std["Un"].get(n,0.0)/hx_n}
        Dn = (n-1)*(n+6-3*delta)+9*(2-delta)
        expected_uf = -1/(2*Dn); expected_df = -delta*(n-1)/(2*Dn)
        checks[f"{mode}_standard_residual_below_1e-11"] = std_meta["scaled_residual"] < 1e-11
        checks[f"{mode}_standard_lower_null_below_1e-10"] = std_meta["lower_null_max"] < 1e-10
        checks[f"{mode}_standard_ratios_match_115"] = all(
            abs(std_ratios[k]-reference_115[mode][k]) < 2e-8 for k in std_ratios)
        checks[f"{mode}_fuel_residual_below_1e-11"] = fuel_meta["scaled_residual"] < 1e-11
        checks[f"{mode}_fuel_coefficients_match_BR3A"] = (
            abs(fuel["Uf"].get(n,0.0)/hx_n-expected_uf) < 2e-8 and
            abs(fuel["df"].get(n,0.0)/hx_n-expected_df) < 2e-8)

        physical = solve_fractional(mode, physical_mu, std, fuel, fmin, n)
        std0, bg0, _ = solve_standard(mode, 0.0); fuel0, _ = solve_fuel(std0, bg0)
        zero_matter = solve_fractional(mode, 0.0, std0, fuel0, fmin, n)
        checks[f"{mode}_physical_full_rank"] = physical["rank"] == physical["unknowns"]
        checks[f"{mode}_physical_scaled_residual_below_1e-11"] = physical["scaled_residual"] < 1e-11
        checks[f"{mode}_all_11_rows_below_1e-10"] = max(physical["row_max_abs_residuals"].values()) < 1e-10
        missing_j = 1 if mode == "NID" else 0
        missing_norm = max(abs(v) for k,v in physical["layers"][str(missing_j)].items()
                           if k not in ("power",))
        zero_missing_norm = max(abs(v) for k,v in zero_matter["layers"][str(missing_j)].items()
                                if k not in ("power",))
        checks[f"{mode}_missing_matter_layer_nonzero_physical"] = missing_norm > 1e-10
        checks[f"{mode}_missing_matter_layer_zero_when_mu_zero"] = zero_missing_norm < 1e-10
        earliest_j = 0 if mode == "NID" else -1
        u_power = 0 if mode == "NID" else -1
        ug0 = -rn/(4*rg) if mode == "NID" else -3*rn/(4*rg)
        un0 = 0.25 if mode == "NID" else 0.75
        earliest = p + u_power
        expected_ug = (p*ug0/2)/(earliest+1)
        expected_un = (p*un0/2)/(earliest+1)
        early_layer = zero_matter["layers"][str(earliest_j)]
        checks[f"{mode}_zero_matter_earliest_matches_104"] = (
            abs(early_layer["U_gamma"]-expected_ug) < 2e-10 and
            abs(early_layer["U_fs"]-expected_un) < 2e-10)
        shear_j = 2 if mode == "NID" else 1
        got108 = zero_matter["layers"][str(shear_j)]
        vector_got = np.array([got108["h_x"],got108["eta"],got108["delta_gamma"],
                               got108["delta_fs"],got108["U_gamma"],got108["U_fs"],
                               got108["sigma_fs"]])
        vector_expected = expected_108(mode)
        checks[f"{mode}_zero_matter_shear_matches_108"] = bool(
            np.max(np.abs(vector_got-vector_expected)) < 2e-9)
        common = physical["layers"][str(n)]
        checks[f"{mode}_common_layer_finite"] = all(np.isfinite(v) for v in common.values())
        results[mode] = {"standard_meta":std_meta,"standard_target_ratios":std_ratios,
                         "fuel_meta":fuel_meta,"fuel_target_ratios":{
                            "delta_f_over_hx":fuel["df"].get(n,0.0)/hx_n,
                            "U_f_over_hx":fuel["Uf"].get(n,0.0)/hx_n},
                         "physical_mixed_chain":physical,"zero_matter_chain":zero_matter,
                         "missing_layer_max_norm_physical":missing_norm,
                         "missing_layer_max_norm_zero_matter":zero_missing_norm}
        deadline()

    passed = bool(checks) and all(checks.values())
    output = {"test":"A2-K4.3b-RG-BR3B-2f-5 full mixed Puiseux chain",
      "normalization":"first order per unit coefficient of rho_f/rho_r = Phi*z^p; z=k a/(H0 sqrt(Omega_r))",
      "included_rows":list(CORE_ROWS),"carried_rows":list(CARRY_ROWS),
      "scope_limit":"fractional l=3 feedback and gravitating ash enter after common fuel and remain BR3B-2g",
      "mode_results":results,"checks":checks,
      "execution_verdict":"PASS_FULL_MIXED_CHAIN_THROUGH_COMMON_FUEL" if passed else "REVIEW_FULL_MIXED_CHAIN_UNCLOSED",
      "physical_verdict":"K4 survives BR3B-2f-5" if passed else "no death verdict; audit first failed row",
      "K4_3b_RG_verdict":"NEUZAVRETA_BR3B2G_L3_AND_ASH_THEN_BR3C" if passed else "NEUZAVRETA_BR3B2F5",
      "canonical_score":"60/100 = G6",
      "next_step":"if PASS add first later fractional l=3 feedback and ash-gravity ledger, then BR3C two-depth residual evolution",
      "runtime_limit_seconds":args.max_runtime_seconds,"runtime_seconds":time.monotonic()-started}
    print(json.dumps(output,indent=2,sort_keys=True)); return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)})); raise SystemExit(124)
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)})); raise SystemExit(2)
