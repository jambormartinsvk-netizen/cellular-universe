#!/usr/bin/env python
"""Bounded term-by-term cancellation ledger for projected M-prime."""

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
SOURCE = HERE / "185_script_A2_K4_C7_7c_K7c3c_second_fixed_RK4_refinement.py"
TERM_NAMES = (
    "(-q-2)M", "D/2", "(1.5Ob-Wg*load)Ug",
    "(0.25Wg*inv1r-0.5Og)dg", "-0.5Ob*db", "-0.5Oc*dc",
    "Of*df", "-2On*sig", "fuel_Uf_term",
)


def parse_json(text: str) -> dict[str, object]:
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError("script 185 returned no JSON")
    return json.loads(text[start:end + 1])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    parser.add_argument("--child-runtime-seconds", type=float, default=20.0)
    args = parser.parse_args()
    if not 15 <= args.max_runtime_seconds <= 30:
        parser.error("max-runtime-seconds must be in [15,30]")
    if not 15 <= args.child_runtime_seconds <= 22:
        parser.error("child-runtime-seconds must be in [15,22]")
    started = time.monotonic()

    child = subprocess.run(
        [sys.executable, str(SOURCE), "--max-runtime-seconds", "20",
         "--source-runtime-seconds", "15", "--source-child-runtime-seconds", "6"],
        capture_output=True, text=True, timeout=args.child_runtime_seconds + 1,
        check=False,
    )
    payload = parse_json(child.stdout)
    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("K7c.3d deadline exceeded after child")

    mp.mp.dps = 80
    delta = mp.mpf("0.02297")
    p = mp.mpf("3.93109")
    h0 = mp.mpf("0.6637")
    omega_m0 = mp.mpf("0.3517")
    ombh2 = mp.mpf("0.02237")
    fb = ombh2 / (omega_m0 * h0**2)
    fc = 1 - fb
    neff = mp.mpf("3.046") + mp.mpf("0.0535")
    rn = mp.mpf("0.2271") * neff / (1 + mp.mpf("0.2271") * neff)
    rg = 1 - rn
    omega_r0 = mp.mpf("2.47282e-5") * (1 + mp.mpf("0.2271") * neff) / h0**2
    hubble0_mpc = 100 * h0 / mp.mpf("299792.458")
    k_mpc = mp.mpf("0.05")
    mu = hubble0_mpc * omega_m0 / mp.sqrt(omega_r0) / k_mpc
    g2 = mp.mpf("0.15") * (hubble0_mpc / k_mpc)**2 * mp.sqrt(omega_r0)
    transfer_shape = g2 * (1 / (p + 1) - mp.mpf("0.5"))

    def m(value: object) -> mp.mpf:
        return mp.mpf(str(value))

    # __K7C3D_CONTINUE__
