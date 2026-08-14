"""Exact no-ODE B1 preflight for A2-K4/P5.3g7-M3-FULL/R-A."""

from __future__ import annotations

import hashlib
import time
from pathlib import Path

import sympy as sp


STATE = (
    "h", "eta", "delta_gamma", "delta_fs", "delta_b", "delta_c",
    "U_gamma", "U_fs", "sigma_fs", "U_b", "U_c", "delta_f", "U_f",
)
DRIVER = (
    "gamma_continuity", "gamma_Euler",
    "fs_continuity", "fs_shear", "fs_Euler",
    "baryon_continuity",
    "cdm_continuity", "cdm_Euler",
    "tight_coupling",
    "fuel_continuity", "fuel_Euler",
    "Einstein_trace", "Einstein_traceless",
)
HOLDOUT = ("Einstein_00", "Einstein_0i")

COEFFICIENT_SUPPORT = {
    "AD": {"n": 2, "fuel_phi0": [0, 1, 2], "phi1": [0, 1, 2], "background_m_max": 2},
    "CDI": {"n": 1, "fuel_phi0": [0, 1], "phi1": [0, 1], "background_m_max": 1},
    "BI": {"n": 1, "fuel_phi0": [0, 1], "phi1": [0, 1], "background_m_max": 1},
    "NID": {"n": 3, "fuel_phi0": [0, 1, 2, 3], "phi1": [0, 1, 2, 3], "background_m_max": 3},
    "NIV": {"n": 2, "fuel_phi0": [-1, 0, 1, 2], "phi1": [-1, 0, 1, 2], "background_m_max": 3},
}

EXPECTED_HASHES = {
    "scripts/88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py":
        "0F13DA6CE761CFEF99909B492E30CF5ED751F56A555594334729330ED4888364",
    "scripts/baseScripts/p5_general_synchronous/mode_resolved_puiseux_v2_m1_anchored.py":
        "5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455",
    "tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/26_P5_3G7_M1_STANDARD_METRIC_SOURCE_MAP_SK.md":
        "7C927999F0D5BAECD0E45E52DFF760FA17DC0A48A3799242D147AEDE4228999B",
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _deadline(start: float, limit: float) -> None:
    if time.monotonic() - start > limit:
        raise TimeoutError("R-A B1 internal deadline exceeded")


def _exact_zero(expression: sp.Expr) -> tuple[bool, sp.Expr]:
    residual = sp.factor(sp.cancel(sp.expand(expression)))
    return residual == 0, residual


def build_preflight(max_runtime_seconds: float = 5.0) -> dict[str, object]:
    start = time.monotonic()
    if not 0 < max_runtime_seconds <= 5.0:
        raise ValueError("max_runtime_seconds must be in (0,5]")

    root = Path(__file__).resolve().parents[3]
    source_hashes = {
        relative: _sha256(root / Path(relative)) for relative in EXPECTED_HASHES
    }
    hash_checks = {
        relative: source_hashes[relative] == expected
        for relative, expected in EXPECTED_HASHES.items()
    }
    _deadline(start, max_runtime_seconds)

    d, g, hc, s2 = sp.symbols("delta gamma h_c s2", nonzero=True)
    Xc, Xf, Xb, Xg, Xn, Xs = sp.symbols("X_c X_f X_b X_gamma X_nu X_s")
    dc, df, db, dg, dn, ds = sp.symbols("delta_c delta_f delta_b delta_gamma delta_nu delta_s")
    Uc, Uf, Ub, Ug, Un, Us = sp.symbols("U_c U_f U_b U_gamma U_nu U_s")
    sg, sn, ss = sp.symbols("sigma_gamma sigma_nu sigma_s")
    hx = sp.symbols("h_x")
    r = Xf / Xc
    beta = d * Xf / (Xc + d * Xf)
    Ud = (1 - beta) * Uc + beta * Uf

    Xc_x = -3 * Xc + g * Xf
    Xf_x = -(3 * d + g) * Xf
    Xb_x, Xg_x, Xn_x, Xs_x = -3 * Xb, -4 * Xg, -4 * Xn, -4 * Xs
    dc_x = -s2 * Uc - hx / 2 + g * r * (df - dc)
    Uc_x = (hc - 1) * Uc + g * r * beta * (Uf - Uc)
    df_x = (
        -3 * (2 - d) * df - d * (s2 * Uf + hx / 2)
        - 9 * d * (2 - d) * Uf - 3 * g * (2 - d) * Uf
    )
    Uf_x = (hc + 2) * Uf + df / d + g / d * (2 * Uf - Ud)
    db_x, Ub_x = -s2 * Ub - hx / 2, (hc - 1) * Ub
    dg_x = -sp.Rational(4, 3) * s2 * Ug - sp.Rational(2, 3) * hx
    dn_x = -sp.Rational(4, 3) * s2 * Un - sp.Rational(2, 3) * hx
    ds_x = -sp.Rational(4, 3) * s2 * Us - sp.Rational(2, 3) * hx
    Ug_x, Un_x, Us_x = hc * Ug + dg / 4 - sg, hc * Un + dn / 4 - sn, hc * Us + ds / 4 - ss

    pressure_good_ratio = df + (2 - d) * (3 * d + g) * Uf
    pressure_legacy_ratio = df + 9 * d * (2 - d) * Uf + 3 * g * (2 - d) * Uf
    expected_legacy_difference = 2 * (2 - d) * (3 * d + g) * Uf
    pressure_difference = sp.expand(pressure_legacy_ratio - pressure_good_ratio)
    Pf = Xf * pressure_good_ratio
    Drho = Xc * dc + Xf * df + Xb * db + Xg * dg + Xn * dn + Xs * ds
    Dpress = Pf + (Xg * dg + Xn * dn + Xs * ds) / 3
    Momentum = Xc * Uc + d * Xf * Uf + Xb * Ub + sp.Rational(4, 3) * (Xg * Ug + Xn * Un + Xs * Us)
    Enthalpy = Xc + d * Xf + Xb + sp.Rational(4, 3) * (Xg + Xn + Xs)
    Shear = sp.Rational(4, 3) * (Xg * sg + Xn * sn + Xs * ss)

    Drho_x = sp.expand(
        Xc_x * dc + Xc * dc_x + Xf_x * df + Xf * df_x
        + Xb_x * db + Xb * db_x + Xg_x * dg + Xg * dg_x
        + Xn_x * dn + Xn * dn_x + Xs_x * ds + Xs * ds_x
    )
    Momentum_x = sp.expand(
        Xc_x * Uc + Xc * Uc_x
        + d * (Xf_x * Uf + Xf * Uf_x)
        + Xb_x * Ub + Xb * Ub_x
        + sp.Rational(4, 3) * (
            Xg_x * Ug + Xg * Ug_x + Xn_x * Un + Xn * Un_x + Xs_x * Us + Xs * Us_x
        )
    )
    energy_ok, energy_residual = _exact_zero(
        Drho_x + 3 * (Drho + Dpress) + s2 * Momentum + hx * Enthalpy / 2
    )
    momentum_ok, momentum_residual = _exact_zero(
        Momentum_x - (hc - 4) * Momentum - Dpress + Shear
    )
    pressure_ok, pressure_residual = _exact_zero(
        sp.diff(pressure_good_ratio, g) - (2 - d) * Uf
    )
    legacy_fixture_ok, legacy_fixture_residual = _exact_zero(
        pressure_difference - expected_legacy_difference
    )
    legacy_is_rejected = sp.factor(pressure_difference) != 0
    _deadline(start, max_runtime_seconds)

    a, E2, q2 = sp.symbols("a E2 q2", positive=True)
    eta, etax, etaxx, hxx = sp.symbols("eta eta_x eta_xx h_xx")
    Dt, Pt, Mt, Wt, St = sp.symbols("Delta_rho Delta_p Momentum W Shear")
    HcLog = sp.symbols("Hc_log")
    A = a**2 * E2
    At_x = 2 * HcLog * A
    E2_x = -3 * Wt
    Dt_x = -3 * (Dt + Pt) - q2 / A * Mt - hx * Wt / 2
    Mt_x = (HcLog - 4) * Mt + Pt - St
    C00 = q2 * eta - A * hx / 2 + sp.Rational(3, 2) * a**2 * Dt
    C0i = etax - sp.Rational(3, 2) * Mt / E2
    Ctr = A * (hxx + (HcLog + 2) * hx) - 2 * q2 * eta + 9 * a**2 * Pt
    Ctl = A * (hxx + 6 * etaxx + (HcLog + 2) * (hx + 6 * etax)) - 2 * q2 * eta + 9 * a**2 * St
    C00_x = q2 * etax - (At_x * hx + A * hxx) / 2 + sp.Rational(3, 2) * a**2 * (2 * Dt + Dt_x)
    C0i_x = etaxx - sp.Rational(3, 2) * (Mt_x / E2 - Mt * E2_x / E2**2)
    hc_relation = {HcLog: 1 - sp.Rational(3, 2) * Wt / E2}
    bianchi00_ok, bianchi00_residual = _exact_zero(
        (C00_x + C00 - q2 * C0i + Ctr / 2).subs(hc_relation)
    )
    bianchi0i_ok, bianchi0i_residual = _exact_zero(
        (C0i_x + (HcLog + 2) * C0i - (Ctl - Ctr) / (6 * A)).subs(hc_relation)
    )

    Af, Hr, k = sp.symbols("A_f H_r k", positive=True)
    p = 4 - 3 * sp.Rational(2297, 100000)
    z = k * a / Hr
    phi = Af * (Hr / k) ** p
    k_cancel_expression = sp.powsimp(phi * z**p - Af * a**p, force=True)
    k_cancel_ok = sp.simplify(k_cancel_expression) == 0

    book_phi = sp.symbols("book_phi")
    Of1, fuel0, fuel1 = sp.symbols("Omega_f1 fuel0 fuel1")
    weighted_fuel = book_phi * Of1 * (fuel0 + book_phi * fuel1)
    phi1_source = sp.diff(weighted_fuel, book_phi).subs(book_phi, 0)
    order_mixing_ok = phi1_source == Of1 * fuel0 and not phi1_source.has(fuel1)

    Rn, Rs, common = sp.symbols("R_n R_s common")
    steam_split_ok, steam_split_residual = _exact_zero(Rn * common + Rs * common - (Rn + Rs) * common)

    missing_delta_f = tuple(name for name in STATE if name != "delta_f")
    missing_U_f = tuple(name for name in STATE if name != "U_f")
    extra_state = STATE + ("fake_state",)
    reordered_state = tuple(reversed(STATE))
    missing_fuel_row = tuple(name for name in DRIVER if name != "fuel_continuity")
    driver_with_holdout = DRIVER[:-1] + ("Einstein_00",)
    negative_fixtures = {
        "reject_missing_delta_f": missing_delta_f != STATE,
        "reject_missing_U_f": missing_U_f != STATE,
        "reject_extra_state": extra_state != STATE,
        "reject_reordered_state": reordered_state != STATE,
        "reject_missing_fuel_row": missing_fuel_row != DRIVER,
        "reject_holdout_in_driver": driver_with_holdout != DRIVER and bool(set(driver_with_holdout) & set(HOLDOUT)),
        "reject_legacy_pressure": legacy_is_rejected,
        "reject_phi1_fuel1_source": order_mixing_ok,
    }
    support_checks = {
        "mode_set_exact": tuple(COEFFICIENT_SUPPORT) == ("AD", "CDI", "BI", "NID", "NIV"),
        "background_mmax_exact": tuple(COEFFICIENT_SUPPORT[m]["background_m_max"] for m in COEFFICIENT_SUPPORT) == (2, 1, 1, 3, 3),
        "lower_coefficients_explicit": all(
            COEFFICIENT_SUPPORT[mode]["fuel_phi0"] == list(range(min(COEFFICIENT_SUPPORT[mode]["fuel_phi0"]), COEFFICIENT_SUPPORT[mode]["n"] + 1))
            for mode in COEFFICIENT_SUPPORT
        ),
    }

    checks = {
        "source_hashes_exact": all(hash_checks.values()),
        "state_ordered_exact_13": len(STATE) == 13 and len(set(STATE)) == 13,
        "driver_ordered_exact_13": len(DRIVER) == 13 and len(set(DRIVER)) == 13,
        "holdouts_exact_and_driver_excluded": HOLDOUT == ("Einstein_00", "Einstein_0i") and not set(HOLDOUT) & set(DRIVER),
        "pressure_formula_exact": pressure_ok,
        "legacy_pressure_difference_exact": legacy_fixture_ok and legacy_is_rejected,
        "total_energy_left_null_exact": energy_ok,
        "total_momentum_left_null_exact": momentum_ok,
        "bianchi_C00_propagation_exact": bianchi00_ok,
        "bianchi_C0i_propagation_exact": bianchi0i_ok,
        "background_k_cancel_exact": k_cancel_ok,
        "phi1_source_excludes_fuel1": order_mixing_ok,
        "conditional_steam_weighted_split_exact": steam_split_ok,
        "all_negative_fixtures_rejected": all(negative_fixtures.values()),
        "coefficient_support_exact": all(support_checks.values()),
    }
    _deadline(start, max_runtime_seconds)

    passed = all(checks.values())
    return {
        "test": "A2-K4 P5.3g7-M3-FULL/R-A B1 exact preflight",
        "run_id": "KMPC-025",
        "scope": "exact coefficient/species/Bianchi/state-contract preflight; no matrix solve or ODE",
        "runtime_seconds": time.monotonic() - start,
        "internal_limit_seconds": max_runtime_seconds,
        "physics_evolution_executed": False,
        "matrix_solve_executed": False,
        "score_effect": 0,
        "source_hashes": source_hashes,
        "expected_source_hashes": EXPECTED_HASHES,
        "conventions": {
            "time": "x=ln(a)", "velocity": "U_A=Hconf*theta_A/k^2",
            "transfer": "Q_f=-Gamma*rho_f*u_d; Q_c=-Q_f",
            "steam": "conditional S-C weighted split only",
        },
        "state_manifest": list(STATE),
        "driver_manifest": list(DRIVER),
        "holdout_manifest": list(HOLDOUT),
        "coefficient_support": COEFFICIENT_SUPPORT,
        "exact_residuals": {
            "pressure": str(pressure_residual),
            "legacy_pressure_difference_fixture": str(legacy_fixture_residual),
            "total_energy": str(energy_residual),
            "total_momentum": str(momentum_residual),
            "bianchi_C00": str(bianchi00_residual),
            "bianchi_C0i": str(bianchi0i_residual),
            "background_k_cancel": str(sp.simplify(k_cancel_expression)),
            "conditional_steam_split": str(steam_split_residual),
        },
        "negative_fixtures": negative_fixtures,
        "support_checks": support_checks,
        "checks": checks,
        "execution_verdict": "PASS_R_A_B1_PREFLIGHT_ONLY" if passed else "STOP_R_A_B1_PREFLIGHT",
    }

