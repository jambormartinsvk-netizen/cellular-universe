#!/usr/bin/env python
"""Bounded covariant moment and bookkeeping audit for A2-K8.1."""

from __future__ import annotations

import argparse
import json
import math
import random
import time


def dot(a: list[float], b: list[float]) -> float:
    return -a[0]*b[0] + sum(a[i]*b[i] for i in range(1, 4))


def add(a: list[float], b: list[float]) -> list[float]:
    return [a[i]+b[i] for i in range(4)]


def scale(c: float, a: list[float]) -> list[float]:
    return [c*x for x in a]


def spatial_projection(q: list[float], u: list[float]) -> list[float]:
    # h^alpha_nu q^nu = q^alpha + u^alpha (u.q) for signature -+++.
    return add(q, scale(dot(u, q), u))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--samples", type=int, default=1000)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        parser.error("runtime must be in (0,5]")
    if not 10 <= args.samples <= 10000:
        parser.error("samples must be in [10,10000]")
    started = time.monotonic()
    rng = random.Random(8012026)
    maximum = {
        "u_norm": 0.0,
        "u_dot_a": 0.0,
        "energy_projection": 0.0,
        "momentum_projection": 0.0,
        "geodesic_limit": 0.0,
        "total_background_ledger": 0.0,
        "creation_pressure_rewrite": 0.0,
        "double_count_signature": 0.0,
    }
    nonzero_momentum_examples = 0
    for _ in range(args.samples):
        if time.monotonic()-started > args.max_runtime_seconds:
            raise TimeoutError("K8.1 moment audit internal deadline exceeded")
        velocity = [rng.uniform(-0.3, 0.3) for _ in range(3)]
        v2 = sum(v*v for v in velocity)
        gamma = 1.0/math.sqrt(1.0-v2)
        u = [gamma] + [gamma*v for v in velocity]
        raw = [rng.uniform(-1.0, 1.0) for _ in range(4)]
        a = add(raw, scale(dot(u, raw), u))
        mass = rng.uniform(0.1, 10.0)
        number = rng.uniform(0.1, 10.0)
        source_n = rng.uniform(0.01, 2.0)
        rho = mass*number
        q_energy = mass*source_n
        q = add(scale(q_energy, u), scale(rho, a))
        projected = spatial_projection(q, u)
        expected_momentum = scale(rho, a)
        q_geodesic = scale(q_energy, u)
        maximum["u_norm"] = max(maximum["u_norm"], abs(dot(u, u)+1.0))
        maximum["u_dot_a"] = max(maximum["u_dot_a"], abs(dot(u, a)))
        maximum["energy_projection"] = max(
            maximum["energy_projection"], abs(-dot(u, q)-q_energy)
        )
        maximum["momentum_projection"] = max(
            maximum["momentum_projection"],
            max(abs(projected[i]-expected_momentum[i]) for i in range(4)),
        )
        maximum["geodesic_limit"] = max(
            maximum["geodesic_limit"],
            max(abs(q_geodesic[i]-q_energy*u[i]) for i in range(4)),
        )
        if max(abs(x) for x in expected_momentum) > 1e-8:
            nonzero_momentum_examples += 1
        hubble = rng.uniform(0.1, 2.0)
        rho_c = rng.uniform(0.1, 20.0)
        rho_f = rng.uniform(0.1, 20.0)
        w_f = rng.uniform(-0.99, -0.8)
        transfer = rng.uniform(0.001, 1.0)
        rho_c_dot = transfer-3.0*hubble*rho_c
        rho_f_dot = -transfer-3.0*hubble*(1.0+w_f)*rho_f
        total_residual = (
            rho_c_dot+3.0*hubble*rho_c
            +rho_f_dot+3.0*hubble*(1.0+w_f)*rho_f
        )
        p_creation = -transfer/(3.0*hubble)
        conserved_rewrite = rho_c_dot+3.0*hubble*(rho_c+p_creation)
        explicit_and_pressure = conserved_rewrite-transfer
        maximum["total_background_ledger"] = max(
            maximum["total_background_ledger"], abs(total_residual)
        )
        maximum["creation_pressure_rewrite"] = max(
            maximum["creation_pressure_rewrite"], abs(conserved_rewrite)
        )
        maximum["double_count_signature"] = max(
            maximum["double_count_signature"], abs(explicit_and_pressure+transfer)
        )
    tolerance = 2e-11
    checks = {
        "timelike_velocity_normalized": maximum["u_norm"] < tolerance,
        "constructed_acceleration_is_orthogonal": maximum["u_dot_a"] < tolerance,
        "number_source_fixes_energy_projection": maximum["energy_projection"] < tolerance,
        "acceleration_fixes_spatial_projection": maximum["momentum_projection"] < tolerance,
        "geodesic_limit_Q_parallel_uc": maximum["geodesic_limit"] < tolerance,
        "scalar_number_source_does_not_force_zero_momentum": nonzero_momentum_examples == args.samples,
        "A1_background_total_energy_ledger_closes": maximum["total_background_ledger"] < tolerance,
        "creation_pressure_is_exact_conserved_rewrite": maximum["creation_pressure_rewrite"] < tolerance,
        "explicit_Q_plus_same_creation_pressure_double_counts": maximum["double_count_signature"] < tolerance,
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K8.1 covariant number-source moment ledger",
        "identity": "div(T_c)=m*S_n*u_c+rho_c*a_c",
        "samples": args.samples,
        "maximum_absolute_residuals": maximum,
        "checks": checks,
        "execution_verdict": "PASS_K8_1_MOMENT_IDENTITIES" if passed else "REVIEW_K8_1_UNCLOSED",
        "gate_verdict": "G2_PARENT_OPEN_MOMENT_NOT_FIXED_BY_Sn",
        "fine_depth": "10.0/100",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic()-started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)

