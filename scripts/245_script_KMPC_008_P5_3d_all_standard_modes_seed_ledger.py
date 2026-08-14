#!/usr/bin/env python
"""Bounded symbolic leading P5 seed ledger for five standard modes; no ODE."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

import sympy as sp


MODES = {
    "adiabatic": 2,
    "cdm_density_isocurvature": 1,
    "baryon_density_isocurvature": 1,
    "neutrino_density_isocurvature": 3,
    "neutrino_velocity_isocurvature": 2,
}


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
    delta, H, gamma2, r0, a = sp.symbols("delta H gamma2 r0 a", positive=True)
    checks: dict[str, bool] = {}
    rows: dict[str, object] = {}
    for mode, n_int in MODES.items():
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.3d internal deadline exceeded")
        n = sp.Integer(n_int)
        denom = (n - 1) * (n + 6 - 3 * delta) + 9 * (2 - delta)
        A = -1 / (2 * denom)
        uf = A * H * a**n
        df = delta * (n - 1) * uf
        fc = n * df + 3 * (2 - delta) * df + delta * H * a**n / 2 + 9 * delta * (2 - delta) * uf
        fe = n * uf - uf - df / delta
        nuc = n + 8 - 6 * delta
        uc = delta * gamma2 * r0**2 * A * H * a**nuc / (nuc + 2)
        ue = nuc * uc + 2 * uc - delta * gamma2 * r0**2 * uf * a**(8 - 6 * delta)
        reduced = {"fuel_continuity": sp.simplify(fc), "fuel_euler": sp.simplify(fe), "uc_euler": sp.simplify(ue)}
        for key, value in reduced.items():
            checks[f"{mode}_{key}"] = bool(value == 0)
        checks[f"{mode}_uf_regular"] = bool(sp.limit(uf, a, 0, dir="+") == 0)
        checks[f"{mode}_df_regular"] = bool(sp.limit(df, a, 0, dir="+") == 0)
        checks[f"{mode}_uc_gamma_zero"] = bool(sp.simplify(uc.subs(gamma2, 0)) == 0)
        checks[f"{mode}_uc_higher_order_at_frozen_delta"] = bool(float(nuc.subs(delta, sp.Rational(2297, 100000))) > n_int)
        rows[mode] = {"n": n_int, "Uf_over_H": str(A), "deltaf_over_Uf": str(delta * (n - 1)), "Uc_power": str(nuc), "residuals": {k: str(v) for k, v in reduced.items()}}
    payload = {
        "test": "KMPC-008 P5.3d five-standard-mode leading seed ledger",
        "scope": "leading standard-mode radiation series only; no amplitude matching, higher orders, gauge proof, ODE, score, or G8",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "mode_results": rows,
        "verdict": "PASS_P5_3D_STANDARD_MODE_LEADING_SEEDS" if all(checks.values()) else "STOP_P5_3D_STANDARD_MODE_LEADING_SEEDS",
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
