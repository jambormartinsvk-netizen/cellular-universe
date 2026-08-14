#!/usr/bin/env python3
"""A2-K7.1a-K3.1 Onsager/noise positivity gate.

The expansion-driven part of the proposed reaction is a scalar-scalar
cross effect.  After normalising the two thermodynamic forces, write the
linear irreversible response as

    (reaction flux, bulk stress)^T = -L (affinity, expansion)^T,

with symmetric Onsager matrix

    L = [[ell, alpha], [alpha, zeta]].

The bare K3 mean ansatz keeps alpha!=0 but supplies neither a diagonal
reaction coefficient nor a bulk-viscous companion.  Its matrix
[[0,alpha],[alpha,0]] has eigenvalues +/-|alpha| and cannot be positive
semidefinite.  A thermodynamically admissible completion requires

    ell >= 0, zeta >= 0, ell*zeta-alpha^2 >= 0,

and a positive noise covariance proportional to L in a local thermal/KMS
limit.  This script checks the preregistered epsilon grid.  The numerical
normalisation ell=1 is illustrative only; it proves existence of a positive
completion, not its microphysical magnitude or units.
"""

from __future__ import annotations

import json

import numpy as np


DELTA = 0.02297
FRACTIONS = (0.01, 0.05, 0.10, 0.25, 0.50, 0.90)
SAFETY = 0.01
ELL = 1.0
TEMPERATURE_NORMALISED = 1.0


def row(fraction: float) -> dict:
    epsilon = fraction * DELTA
    alpha = epsilon * (1.0 - DELTA)

    bare = np.array([[0.0, alpha], [alpha, 0.0]])
    bare_eigenvalues = np.linalg.eigvalsh(bare)

    zeta_boundary = alpha * alpha / ELL
    zeta = (1.0 + SAFETY) * zeta_boundary
    completed = np.array([[ELL, alpha], [alpha, zeta]])
    completed_eigenvalues = np.linalg.eigvalsh(completed)
    noise = 2.0 * TEMPERATURE_NORMALISED * completed
    noise_eigenvalues = np.linalg.eigvalsh(noise)

    return {
        "epsilon_over_delta": fraction,
        "epsilon": epsilon,
        "normalised_cross_alpha": alpha,
        "bare_eigenvalues": [float(v) for v in bare_eigenvalues],
        "bare_positive_semidefinite": bool(np.all(bare_eigenvalues >= 0.0)),
        "ell_normalised": ELL,
        "zeta_positivity_boundary": zeta_boundary,
        "zeta_with_one_percent_margin": zeta,
        "completed_determinant": float(np.linalg.det(completed)),
        "completed_eigenvalues": [float(v) for v in completed_eigenvalues],
        "completed_positive_definite": bool(
            np.all(completed_eigenvalues > 0.0)
        ),
        "normalised_noise_eigenvalues": [float(v) for v in noise_eigenvalues],
        "noise_positive_definite": bool(np.all(noise_eigenvalues > 0.0)),
    }


def main() -> int:
    rows = [row(fraction) for fraction in FRACTIONS]
    bare_fails = all(not item["bare_positive_semidefinite"] for item in rows)
    completion_exists = all(
        item["completed_positive_definite"]
        and item["noise_positive_definite"]
        for item in rows
    )

    output = {
        "test": "A2-K7.1a-K3.1 Onsager and noise positivity gate",
        "force_normalisation_warning": (
            "ell=1 and T=1 are dimensionless force normalisations; "
            "only signs, determinant, and existence are audited"
        ),
        "rows": rows,
        "checks": {
            "bare_cross_only_operator_fails_every_grid_point": bare_fails,
            "positive_onsager_completion_exists_every_grid_point": completion_exists,
            "completion_requires_nonzero_diagonal_reaction": True,
            "completion_requires_bulk_viscous_companion": True,
            "local_KMS_completion_requires_noise": True,
            "microphysical_coefficients_derived": False,
            "bath_background_closed": False,
        },
        "verdicts": {
            "K7.1a-K3.1-K1_bare_cross_only": "DEAD_M014b",
            "K7.1a-K3.1-K2_completed_onsager": (
                "SURVIVES_THERMODYNAMIC_FORMULATION_ONLY"
            ),
            "parent_A2_K7": "REMAINS_30_OF_100",
        },
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if bare_fails and completion_exists else 1


if __name__ == "__main__":
    raise SystemExit(main())
