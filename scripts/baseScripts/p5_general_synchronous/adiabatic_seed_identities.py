"""Leading radiation-era P5 adiabatic seed identities; no evolution."""

from __future__ import annotations

import sympy as sp


def build_adiabatic_seed_identities() -> tuple[dict[str, sp.Expr], dict[str, sp.Expr]]:
    delta, H, gamma2, r0, a = sp.symbols("delta H gamma2 r0 a", positive=True)
    n = sp.Integer(2)
    A = -1 / (52 - 24 * delta)
    uf = A * H * a**n
    df = delta * uf
    # h_c=-1 and the leading gradient/interaction corrections are higher order.
    fuel_continuity = n * df + 3 * (2 - delta) * df + delta * H * a**n / 2 + 9 * delta * (2 - delta) * uf
    fuel_euler = n * uf - uf - df / delta
    n_uc = 10 - 6 * delta
    uc_coeff = delta * gamma2 * r0**2 * A * H / (n_uc + 2)
    uc = uc_coeff * a**n_uc
    uc_euler = n_uc * uc + 2 * uc - delta * gamma2 * r0**2 * uf * a**(8 - 6 * delta)
    identities = {
        "fuel_continuity_leading": fuel_continuity,
        "fuel_euler_leading": fuel_euler,
        "fuel_density_to_velocity_relation": df - delta * uf,
        "uc_energy_frame_forced_leading": uc_euler,
        "uc_vanishes_gamma_zero": uc.subs(gamma2, 0),
        "uf_regular_as_a_to_zero": sp.limit(uf, a, 0, dir="+"),
        "df_regular_as_a_to_zero": sp.limit(df, a, 0, dir="+"),
    }
    metadata = {
        "A": A,
        "uf": uf,
        "df": df,
        "uc": uc,
        "uc_power": n_uc,
        "uc_coefficient": uc_coeff,
    }
    return identities, metadata
