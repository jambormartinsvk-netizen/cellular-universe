"""Numerical audit of Q8, track K1: decoherence plus a durable record.

The script checks what a simple qubit dephasing channel can and cannot provide.
It tests complete trace preservation through a Kraus representation, positivity,
coherence suppression, entropy growth for an initially coherent state, and
no-signalling under a local channel on one half of an entangled pair.

This is deliberately not presented as a microscopic model of domain I.  Its
purpose is to isolate a logical boundary: decoherence can create an effective
classical mixture and a stable record basis, but it does not select one unique
objective outcome by itself.
"""

from __future__ import annotations

import json
import math
from typing import Iterable

import numpy as np


TOL = 1.0e-12


def dephasing_kraus(p: float) -> list[np.ndarray]:
    """Return Kraus operators for rho -> (1-p) rho + p dephase(rho)."""
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must be in [0, 1]")
    identity = np.eye(2, dtype=complex)
    proj0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    proj1 = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)
    return [math.sqrt(1.0 - p) * identity, math.sqrt(p) * proj0, math.sqrt(p) * proj1]


def apply_channel(rho: np.ndarray, kraus: Iterable[np.ndarray]) -> np.ndarray:
    return sum((operator @ rho @ operator.conj().T for operator in kraus), np.zeros_like(rho))


def von_neumann_entropy(rho: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvalsh(rho).real
    eigenvalues = eigenvalues[eigenvalues > TOL]
    return float(-np.sum(eigenvalues * np.log2(eigenvalues)))


def partial_trace_a(rho_ab: np.ndarray) -> np.ndarray:
    """Trace out the first qubit A from a two-qubit density matrix."""
    reshaped = rho_ab.reshape(2, 2, 2, 2)
    return np.trace(reshaped, axis1=0, axis2=2)


def apply_local_channel_a(rho_ab: np.ndarray, kraus: Iterable[np.ndarray]) -> np.ndarray:
    identity_b = np.eye(2, dtype=complex)
    full_kraus = [np.kron(operator, identity_b) for operator in kraus]
    return apply_channel(rho_ab, full_kraus)


def matrix_is_positive(rho: np.ndarray) -> bool:
    return bool(np.min(np.linalg.eigvalsh(rho).real) >= -TOL)


def main() -> int:
    ket_plus = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    rho_plus = np.outer(ket_plus, ket_plus.conj())

    channel_checks = []
    all_checks_pass = True
    for p in (0.0, 0.2, 0.5, 1.0):
        kraus = dephasing_kraus(p)
        completeness = sum(
            (operator.conj().T @ operator for operator in kraus),
            np.zeros((2, 2), dtype=complex),
        )
        rho_out = apply_channel(rho_plus, kraus)
        checks = {
            "p": p,
            "kraus_completeness_error": float(np.max(np.abs(completeness - np.eye(2)))),
            "trace_error": float(abs(np.trace(rho_out) - 1.0)),
            "hermiticity_error": float(np.max(np.abs(rho_out - rho_out.conj().T))),
            "minimum_eigenvalue": float(np.min(np.linalg.eigvalsh(rho_out).real)),
            "off_diagonal_magnitude": float(abs(rho_out[0, 1])),
            "entropy_bits": von_neumann_entropy(rho_out),
            "positive": matrix_is_positive(rho_out),
        }
        passed = (
            checks["kraus_completeness_error"] < TOL
            and checks["trace_error"] < TOL
            and checks["hermiticity_error"] < TOL
            and checks["positive"]
        )
        checks["channel_check"] = "PASS" if passed else "FAIL"
        all_checks_pass = all_checks_pass and passed
        channel_checks.append(checks)

    p_repeat = 0.2
    repeated = rho_plus.copy()
    repeated_steps = []
    for step in range(1, 11):
        repeated = apply_channel(repeated, dephasing_kraus(p_repeat))
        expected = 0.5 * (1.0 - p_repeat) ** step
        repeated_steps.append(
            {
                "step": step,
                "off_diagonal_magnitude": float(abs(repeated[0, 1])),
                "analytic_expected": expected,
                "absolute_error": float(abs(abs(repeated[0, 1]) - expected)),
            }
        )

    bell = np.array([1.0, 0.0, 0.0, 1.0], dtype=complex) / math.sqrt(2.0)
    rho_bell = np.outer(bell, bell.conj())
    rho_b_before = partial_trace_a(rho_bell)
    rho_b_after = partial_trace_a(apply_local_channel_a(rho_bell, dephasing_kraus(1.0)))
    no_signalling_error = float(np.max(np.abs(rho_b_before - rho_b_after)))
    no_signalling_pass = no_signalling_error < TOL
    all_checks_pass = all_checks_pass and no_signalling_pass

    fully_dephased = apply_channel(rho_plus, dephasing_kraus(1.0))
    eigenvalues = np.linalg.eigvalsh(fully_dephased).real
    final_purity = float(np.trace(fully_dephased @ fully_dephased).real)
    final_rank = int(np.sum(eigenvalues > TOL))

    output = {
        "track": "Q8-K1_open_system_decoherence_plus_record",
        "channel_checks": channel_checks,
        "repeated_dephasing_p_0_2": repeated_steps,
        "local_channel_no_signalling": {
            "maximum_change_in_remote_reduced_state": no_signalling_error,
            "status": "PASS" if no_signalling_pass else "FAIL",
        },
        "fully_dephased_plus_state": {
            "density_matrix_real": fully_dephased.real.tolist(),
            "eigenvalues": eigenvalues.tolist(),
            "purity": final_purity,
            "rank": final_rank,
            "interpretation": "mixed state, not one selected objective outcome",
        },
        "mathematical_channel_status": "PASS" if all_checks_pass else "FAIL",
        "effective_classical_record_status": "SUPPORTED_IN_THE_CHOSEN_BASIS",
        "unique_objective_collapse_status": "NOT_PROVIDED",
        "born_rule_single_event_status": "NOT_PROVIDED",
        "microscopic_domain_I_status": "NOT_TESTED",
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if all_checks_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
