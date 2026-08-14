"""Exact first-order tight-coupling algebra in the declared MB collision basis.

This module deliberately contains no background, opacity history, or ODE solver.
It only solves the collision-dominated photon/polarization block used by the
P5.3g4 structural seed audit.
"""

from __future__ import annotations

import sympy as sp


def collision_block() -> sp.Matrix:
    """Return the audited collision block for [F_gamma2, G_gamma0, G_gamma2]."""
    return sp.Matrix(
        [
            [-sp.Rational(9, 10), sp.Rational(1, 10), sp.Rational(1, 10)],
            [sp.Rational(1, 2), -sp.Rational(1, 2), sp.Rational(1, 2)],
            [sp.Rational(1, 10), sp.Rational(1, 10), -sp.Rational(9, 10)],
        ]
    )


def first_order_solution() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, tuple[sp.Symbol, ...]]:
    """Solve C X + epsilon D = 0 for the first nonzero TCA multipoles.

    The source D is the l=2 free-streaming/metric drive retained at first TCA
    order.  l=3 and higher multipoles are intentionally excluded and must be
    added in the later full-hierarchy seed gate.
    """
    epsilon, k, q_gamma, shear = sp.symbols("epsilon k q_gamma shear")
    matrix = collision_block()
    drive = sp.Matrix([
        sp.Rational(2, 5) * k * q_gamma + sp.Rational(8, 15) * k * shear,
        0,
        0,
    ])
    solution = sp.simplify(-epsilon * matrix.inv() * drive)
    return matrix, drive, solution, (epsilon, k, q_gamma, shear)
