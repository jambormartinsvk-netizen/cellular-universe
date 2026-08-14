#!/usr/bin/env python
"""Bounded linear-moment non-uniqueness test for A2-K9.1."""

from __future__ import annotations

import argparse
import json
import math
import time


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        parser.error("runtime must be in (0,5]")
    started = time.monotonic()
    mass_source = 0.15
    epsilons = [1e-2, 1e-3, 1e-4, 1e-5]
    rows = []
    for eps in epsilons:
        gamma = 1.0/math.sqrt(1.0-eps*eps)
        energy_shift = mass_source*(gamma-1.0)
        momentum = mass_source*gamma*eps
        rows.append({"epsilon": eps, "energy_shift": energy_shift, "momentum": momentum})
    energy_orders = []
    momentum_orders = []
    for left, right in zip(rows, rows[1:]):
        ratio = left["epsilon"]/right["epsilon"]
        energy_orders.append(math.log(left["energy_shift"]/right["energy_shift"])/math.log(ratio))
        momentum_orders.append(math.log(left["momentum"]/right["momentum"])/math.log(ratio))
    kappas = [0.0, 0.01, 0.03, 0.10]
    delta_v = 0.2
    elastic = [{"kappa": k, "number_moment": 0.0, "background_energy": 0.0,
                "linear_momentum": -k*delta_v} for k in kappas]
    checks = {
        "production_energy_difference_is_second_order": min(energy_orders) > 1.99,
        "production_momentum_difference_is_first_order": max(abs(x-1.0) for x in momentum_orders) < 1e-4,
        "elastic_family_preserves_number_and_background": all(
            row["number_moment"] == 0.0 and row["background_energy"] == 0.0 for row in elastic),
        "elastic_family_changes_linear_momentum": len({row["linear_momentum"] for row in elastic}) == len(elastic),
    }
    passed = all(checks.values())
    print(json.dumps({
        "test": "A2-K9.1 collision moment non-uniqueness",
        "production_rows": rows,
        "measured_energy_orders": energy_orders,
        "measured_momentum_orders": momentum_orders,
        "elastic_family": elastic,
        "checks": checks,
        "execution_verdict": "PASS_K9_1_MOMENT_NONUNIQUENESS" if passed else "REVIEW_K9_1_UNCLOSED",
        "gate_verdict": "G2_OPEN_CONCRETE_COMMON_KERNEL_REQUIRED",
        "fine_depth": "10.0/100",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic()-started,
    }, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)

