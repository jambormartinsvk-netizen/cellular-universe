"""Bounded G8 S2 direct-versus-tight-coupling operator screen.

This is deliberately narrower than a Boltzmann/recombination solver.  It
uses the frozen K4 background from script 213 and compares the separated
photon/baryon momentum block with its registered K7 tight-coupling limit.
"""

from __future__ import annotations

import hashlib
import math
from pathlib import Path
import time

import numpy as np
from scipy.integrate import solve_ivp


ROOT = Path(__file__).resolve().parents[3]
SOURCE_213 = ROOT / "scripts" / "213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py"
EXPECTED_SOURCE_213_SHA256 = "8726BAE5E3F8C06C74D2053BF9B7430F22B73FA867534C9B421A228AEC8FDC39"

# Frozen copy of the K4 background constants/formula in script 213.
P_EXPONENT = 3.93109
H0 = 0.6637
OMEGA_M0 = 0.3517
OMBH2 = 0.02237
FB = OMBH2 / (OMEGA_M0 * H0**2)
FC = 1.0 - FB
NEFF = 3.046 + 0.0535
RN = 0.2271 * NEFF / (1.0 + 0.2271 * NEFF)
RG = 1.0 - RN
OMEGA_R0 = 2.47282e-5 * (1.0 + 0.2271 * NEFF) / H0**2
HUBBLE0_MPC = 100.0 * H0 / 299792.458
K_MPC = 0.05
MU = HUBBLE0_MPC * OMEGA_M0 / math.sqrt(OMEGA_R0) / K_MPC
G2 = 0.15 * (HUBBLE0_MPC / K_MPC) ** 2 * math.sqrt(OMEGA_R0)
TRANSFER_SHAPE = G2 * (1.0 / (P_EXPONENT + 1.0) - 0.5)

X_START = -23.0
X_FINAL = -22.0
CHI = 100.0
DELTA_GAMMA_SOURCE = 1.0e-6
RHS_CAP = 100_000
SAFETY_CAP = 1.0e6


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def background_k4(x: float) -> dict[str, float]:
    """Exact scalar background expressions copied from frozen script 213."""
    z = K_MPC * math.exp(x) / (HUBBLE0_MPC * math.sqrt(OMEGA_R0))
    fuel_piece = z**P_EXPONENT
    denominator = 1.0 + MU * z + fuel_piece * (1.0 + TRANSFER_SHAPE * z**2)
    denominator_x = MU * z + fuel_piece * (
        P_EXPONENT + (P_EXPONENT + 2.0) * TRANSFER_SHAPE * z**2
    )
    ell = denominator_x / denominator
    loading = 3.0 * FB * MU * z / (4.0 * RG)
    if not (math.isfinite(loading) and loading > 0.0 and denominator > 0.0):
        raise FloatingPointError("nonphysical K4 background during S2")
    return {
        "z": z,
        "q": -1.0 + ell / 2.0,
        "R": loading,
        "load_fraction": loading / (1.0 + loading),
        "inv1r": 1.0 / (1.0 + loading),
    }


def _finite_within_cap(values: np.ndarray) -> bool:
    return bool(np.all(np.isfinite(values)) and np.max(np.abs(values)) <= SAFETY_CAP)


def run_s2(max_runtime_seconds: float) -> dict[str, object]:
    """Perform one bounded direct/TCA overlap integration."""
    if not (0.0 < max_runtime_seconds <= 45.0):
        raise ValueError("max_runtime_seconds must be in (0, 45]")
    started = time.monotonic()
    if not SOURCE_213.is_file():
        raise FileNotFoundError(f"missing frozen K4 source: {SOURCE_213}")
    source_hash = sha256_file(SOURCE_213)
    if source_hash != EXPECTED_SOURCE_213_SHA256:
        raise RuntimeError("script 213 SHA-256 differs from frozen K7d source")

    direct_calls = 0
    tca_calls = 0
    grid = np.linspace(X_START, X_FINAL, 41)

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("G8 S2 internal TCA/direct deadline exceeded")

    def direct_rhs(x: float, y: np.ndarray) -> np.ndarray:
        nonlocal direct_calls
        direct_calls += 1
        deadline()
        if direct_calls > RHS_CAP:
            raise RuntimeError("G8 S2 direct RHS cap exceeded")
        if not _finite_within_cap(y):
            raise FloatingPointError("G8 S2 direct safety cap/nonfinite state")
        U_gamma, U_b = map(float, y)
        b = background_k4(x)
        return np.asarray((
            b["q"] * U_gamma + DELTA_GAMMA_SOURCE / 4.0 + CHI * (U_b - U_gamma),
            (b["q"] - 1.0) * U_b + CHI / b["R"] * (U_gamma - U_b),
        ), dtype=float)

    def tca_rhs(x: float, y: np.ndarray) -> np.ndarray:
        nonlocal tca_calls
        tca_calls += 1
        deadline()
        if tca_calls > RHS_CAP:
            raise RuntimeError("G8 S2 TCA RHS cap exceeded")
        if not _finite_within_cap(y):
            raise FloatingPointError("G8 S2 TCA safety cap/nonfinite state")
        U = float(y[0])
        b = background_k4(x)
        return np.asarray((
            b["q"] * U - b["load_fraction"] * U
            + DELTA_GAMMA_SOURCE * b["inv1r"] / 4.0,
        ), dtype=float)

    direct = solve_ivp(
        direct_rhs, (X_START, X_FINAL), np.zeros(2), method="Radau", t_eval=grid,
        rtol=1.0e-10, atol=1.0e-16, max_step=0.02,
    )
    deadline()
    tca = solve_ivp(
        tca_rhs, (X_START, X_FINAL), np.zeros(1), method="DOP853", t_eval=grid,
        rtol=1.0e-11, atol=1.0e-16, max_step=0.02,
    )
    deadline()
    if direct.y.shape != (2, len(grid)) or tca.y.shape != (1, len(grid)):
        raise RuntimeError("G8 S2 solver returned unexpected state shape")

    U_gamma, U_b = direct.y[0], direct.y[1]
    U_tca = tca.y[0]
    scale = max(float(np.max(np.abs(U_tca))), 1.0e-300)
    direct_tca_overlap = float(np.max(np.abs(U_gamma - U_tca)) / scale)
    direct_slip = float(np.max(np.abs(U_b - U_gamma)) / max(float(np.max(np.abs(U_gamma))), 1.0e-300))
    background_rows = [background_k4(float(x)) for x in grid]
    epsilon_tca = max(1.0 / (CHI * (1.0 + 1.0 / row["R"])) for row in background_rows)
    arrays_finite_cap = _finite_within_cap(direct.y) and _finite_within_cap(tca.y)
    checks = {
        "frozen_K7d_source_hash_exact": source_hash == EXPECTED_SOURCE_213_SHA256,
        "direct_solver_success_and_endpoint": bool(direct.success and abs(float(direct.t[-1]) - X_FINAL) < 1e-14),
        "tca_solver_success_and_endpoint": bool(tca.success and abs(float(tca.t[-1]) - X_FINAL) < 1e-14),
        "states_finite_and_under_safety_cap": arrays_finite_cap,
        "direct_rhs_under_cap": direct_calls <= RHS_CAP,
        "tca_rhs_under_cap": tca_calls <= RHS_CAP,
        "effective_tca_parameter_le_1e6_inverse": bool(epsilon_tca <= 1.0e-6),
        "direct_tca_overlap_le_1e4_inverse": bool(direct_tca_overlap <= 1.0e-4),
        "direct_photon_baryon_slip_le_1e6_inverse": bool(direct_slip <= 1.0e-6),
    }
    passed = all(checks.values())
    return {
        "test": "A2-K4 C7.7c K7 G8 SCREEN-S2 bounded direct/TCA operator overlap",
        "scope": "K4-background momentum-block screen only; not recombination or full hierarchy",
        "physics_executed": "bounded linear momentum-block evolution only",
        "ode_executed": True,
        "score_effect": 0,
        "source_213_sha256": source_hash,
        "expected_source_213_sha256": EXPECTED_SOURCE_213_SHA256,
        "configuration": {
            "x_start": X_START, "x_final": X_FINAL, "chi_dimensionless": CHI,
            "delta_gamma_source": DELTA_GAMMA_SOURCE, "direct_solver": "Radau",
            "tca_solver": "DOP853", "rtol_direct": 1.0e-10, "rtol_tca": 1.0e-11,
            "atol": 1.0e-16, "max_step": 0.02, "rhs_cap_each": RHS_CAP,
            "safety_cap": SAFETY_CAP,
        },
        "diagnostics": {
            "direct_tca_overlap": direct_tca_overlap,
            "direct_photon_baryon_slip": direct_slip,
            "effective_tca_parameter_max": float(epsilon_tca),
            "R_start": background_rows[0]["R"], "R_end": background_rows[-1]["R"],
            "q_start": background_rows[0]["q"], "q_end": background_rows[-1]["q"],
            "U_gamma_final": float(U_gamma[-1]), "U_b_final": float(U_b[-1]),
            "U_tca_final": float(U_tca[-1]),
            "direct_nfev": int(direct.nfev), "tca_nfev": int(tca.nfev),
            "direct_rhs_calls": direct_calls, "tca_rhs_calls": tca_calls,
        },
        "checks": checks,
        "verdict": "PASS_G8_SCREEN_S2_TCA_DIRECT" if passed else "STOP_G8_TCA_DIRECT_MISMATCH",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
