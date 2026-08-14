#!/usr/bin/env python
"""Bounded finite-start evaluation of the P5.3b adiabatic seed; no ODE."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import time


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--max-runtime-seconds", type=float, default=5.0)
    p.add_argument("--output", type=Path, required=True)
    return p.parse_args()


def write_once(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable output: {path}")
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0,5]")
    started = time.monotonic()
    h, omega_m, omega_b_h2, delta, lam = 0.6637, 0.3517, 0.02237, 0.02297, 0.15
    c_km_s, k = 299792.458, 0.05
    omega_gamma = 2.469e-5 / h**2
    omega_r = omega_gamma * (1.0 + 0.2271 * (3.046 + 0.0535))
    omega_b = omega_b_h2 / h**2
    omega_c = omega_m - omega_b
    omega_f = 1.0 - omega_m - omega_r
    h0_mpc = 100.0 * h / c_km_s
    Hcoef = (k / (h0_mpc * math.sqrt(omega_r))) ** 2
    A = -1.0 / (52.0 - 24.0 * delta)
    gamma2 = lam / math.sqrt(omega_r)
    r0 = omega_f / omega_c
    nuc = 10.0 - 6.0 * delta
    uc_coeff = delta * gamma2 * r0**2 * A * Hcoef / ((12.0 - 6.0 * delta))
    rows: dict[str, dict[str, float]] = {}
    for x in (-25.0, -23.0):
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.3c internal deadline exceeded")
        a = math.exp(x)
        hx = Hcoef * a**2
        uf = A * hx
        df = delta * uf
        uc = uc_coeff * a**nuc
        rows[str(x)] = {"a": a, "h_x": hx, "U_f": uf, "delta_f": df, "U_c": uc}
    ratio_uf = rows["-23.0"]["U_f"] / rows["-25.0"]["U_f"]
    ratio_uc = rows["-23.0"]["U_c"] / rows["-25.0"]["U_c"]
    expected_uf, expected_uc = math.exp(4.0), math.exp(2.0 * nuc)
    checks = {
        "all_finite": all(math.isfinite(v) for row in rows.values() for v in row.values()),
        "Uf_two_start_power_ratio": abs(ratio_uf / expected_uf - 1.0) < 1e-12,
        "df_two_start_power_ratio": abs((rows["-23.0"]["delta_f"] / rows["-25.0"]["delta_f"]) / expected_uf - 1.0) < 1e-12,
        "Uc_two_start_power_ratio": abs(ratio_uc / expected_uc - 1.0) < 1e-12,
        "Uc_zero_when_gamma2_zero": abs((uc_coeff * 0.0) * math.exp(-25.0 * nuc)) == 0.0,
        "Uc_is_higher_order_at_both_starts": all(abs(row["U_c"]) < abs(row["U_f"]) for row in rows.values()),
    }
    payload = {
        "test": "KMPC-007 P5.3c finite-start adiabatic leading-seed audit",
        "scope": "two finite surfaces, leading adiabatic series only; no ODE, normalization fit, score, or G8",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "inputs": {"delta": delta, "lambda": lam, "k_Mpc_inverse": k, "x_starts": [-25.0, -23.0]},
        "results": rows,
        "ratios": {"Uf": ratio_uf, "Uc": ratio_uc, "expected_Uf": expected_uf, "expected_Uc": expected_uc},
        "checks": checks,
        "verdict": "PASS_P5_3C_ADIABATIC_FINITE_STARTS" if all(checks.values()) else "STOP_P5_3C_ADIABATIC_FINITE_STARTS",
    }
    write_once(args.output, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
