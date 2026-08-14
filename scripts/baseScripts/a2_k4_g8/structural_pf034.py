"""PF-034 correction wrapper; preserves the original structural module."""

from __future__ import annotations

import sympy as sp

from .structural import exact_s0_s1_audit, state_names


def exact_s0_s1_audit_pf034(max_runtime_seconds: float) -> dict[str, object]:
    """Correct only the direction of the inv1r/load_fraction definition test."""
    payload = exact_s0_s1_audit(max_runtime_seconds)
    q, U_gamma, delta_gamma, R, load_fraction, inv1r = sp.symbols(
        "q U_gamma delta_gamma R load_fraction inv1r", nonzero=True
    )
    generic_k7 = q * U_gamma - load_fraction * U_gamma + delta_gamma * inv1r / 4
    explicit_k7 = q * U_gamma - R / (1 + R) * U_gamma + delta_gamma / (4 * (1 + R))
    residual = sp.simplify(generic_k7.subs({
        load_fraction: R / (1 + R), inv1r: 1 / (1 + R),
    }) - explicit_k7)
    name = "combined_Euler_to_K7_background_notation"
    payload["checks"][name] = bool(residual == 0)
    payload["symbolic_residuals"][name] = str(residual)
    payload["correction"] = (
        "PF-034: define generic load_fraction and inv1r before comparison; "
        "RUN-001 source/result retained unchanged"
    )
    payload["supersedes_technical_artifact"] = "RUN_001_G8_S0_S1_STRUCTURAL_RESULT.json"
    payload["verdict"] = (
        "PASS_G8_SCREEN_S0_S1_STRUCTURAL" if all(payload["checks"].values())
        else "STOP_G8_IMPLEMENTATION_MAPPING"
    )
    return payload
