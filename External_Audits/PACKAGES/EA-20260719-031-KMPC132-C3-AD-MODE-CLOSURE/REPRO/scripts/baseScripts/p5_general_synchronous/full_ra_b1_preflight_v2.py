"""PF-064 repair: independent contract guard around the frozen B1 algebra."""

from __future__ import annotations

import hashlib
import time
from pathlib import Path

from .full_ra_b1_preflight import build_preflight as build_frozen_algebra
from .full_ra_contract import (
    AUTHORITATIVE_DRIVER,
    AUTHORITATIVE_HOLDOUT,
    AUTHORITATIVE_STATE,
    validate_contract,
)


FROZEN_ALGEBRA_SHA256 = "62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _deadline(start: float, limit: float) -> None:
    if time.monotonic() - start > limit:
        raise TimeoutError("R-A B1 v2 internal deadline exceeded")


def build_contract_guard(max_runtime_seconds: float = 5.0) -> dict[str, object]:
    start = time.monotonic()
    if not 0 < max_runtime_seconds <= 5.0:
        raise ValueError("max_runtime_seconds must be in (0,5]")

    algebra_path = Path(__file__).with_name("full_ra_b1_preflight.py")
    algebra_hash = _sha256(algebra_path)
    algebra = build_frozen_algebra(max_runtime_seconds)
    _deadline(start, max_runtime_seconds)

    production = validate_contract(
        algebra["state_manifest"], algebra["driver_manifest"], algebra["holdout_manifest"]
    )

    fixtures = {
        "missing_delta_f": (
            tuple(name for name in AUTHORITATIVE_STATE if name != "delta_f"),
            AUTHORITATIVE_DRIVER,
            AUTHORITATIVE_HOLDOUT,
        ),
        "missing_U_f": (
            tuple(name for name in AUTHORITATIVE_STATE if name != "U_f"),
            AUTHORITATIVE_DRIVER,
            AUTHORITATIVE_HOLDOUT,
        ),
        "same_count_fake_state": (
            AUTHORITATIVE_STATE[:-1] + ("fake_state",),
            AUTHORITATIVE_DRIVER,
            AUTHORITATIVE_HOLDOUT,
        ),
        "reordered_state": (
            AUTHORITATIVE_STATE[:-2] + (AUTHORITATIVE_STATE[-1], AUTHORITATIVE_STATE[-2]),
            AUTHORITATIVE_DRIVER,
            AUTHORITATIVE_HOLDOUT,
        ),
        "missing_fuel_continuity": (
            AUTHORITATIVE_STATE,
            tuple(name for name in AUTHORITATIVE_DRIVER if name != "fuel_continuity"),
            AUTHORITATIVE_HOLDOUT,
        ),
        "same_count_fake_driver": (
            AUTHORITATIVE_STATE,
            AUTHORITATIVE_DRIVER[:-1] + ("fake_driver",),
            AUTHORITATIVE_HOLDOUT,
        ),
        "reordered_driver": (
            AUTHORITATIVE_STATE,
            AUTHORITATIVE_DRIVER[:-2] + (AUTHORITATIVE_DRIVER[-1], AUTHORITATIVE_DRIVER[-2]),
            AUTHORITATIVE_HOLDOUT,
        ),
        "holdout_in_driver": (
            AUTHORITATIVE_STATE,
            AUTHORITATIVE_DRIVER[:-1] + ("Einstein_00",),
            AUTHORITATIVE_HOLDOUT,
        ),
        "reordered_holdout": (
            AUTHORITATIVE_STATE,
            AUTHORITATIVE_DRIVER,
            tuple(reversed(AUTHORITATIVE_HOLDOUT)),
        ),
    }
    fixture_results: dict[str, dict[str, object]] = {}
    for name, arguments in fixtures.items():
        validation = validate_contract(*arguments)
        fixture_results[name] = {
            "rejected": not validation.valid,
            "errors": list(validation.errors),
        }

    core_algebra_keys = (
        "source_hashes_exact",
        "pressure_formula_exact",
        "legacy_pressure_difference_exact",
        "total_energy_left_null_exact",
        "total_momentum_left_null_exact",
        "bianchi_C00_propagation_exact",
        "bianchi_C0i_propagation_exact",
        "background_k_cancel_exact",
        "phi1_source_excludes_fuel1",
        "conditional_steam_weighted_split_exact",
        "coefficient_support_exact",
    )
    exact_zero_keys = (
        "pressure", "legacy_pressure_difference_fixture", "total_energy",
        "total_momentum", "bianchi_C00", "bianchi_C0i",
        "background_k_cancel", "conditional_steam_split",
    )
    checks = {
        "frozen_algebra_hash_exact": algebra_hash == FROZEN_ALGEBRA_SHA256,
        "production_contract_exact": production.valid,
        "authoritative_state_count_13": len(AUTHORITATIVE_STATE) == 13,
        "authoritative_driver_count_13": len(AUTHORITATIVE_DRIVER) == 13,
        "all_negative_fixtures_rejected_by_validator": all(
            result["rejected"] and result["errors"] for result in fixture_results.values()
        ),
        "frozen_core_algebra_regression": all(algebra["checks"][key] for key in core_algebra_keys),
        "all_exact_residuals_zero": all(algebra["exact_residuals"][key] == "0" for key in exact_zero_keys),
        "no_solve_or_ode": not algebra["matrix_solve_executed"] and not algebra["physics_evolution_executed"],
        "score_effect_zero": algebra["score_effect"] == 0,
    }
    _deadline(start, max_runtime_seconds)
    passed = all(checks.values())

    return {
        "test": "A2-K4 P5.3g7-M3-FULL/R-A B1 independent contract guard",
        "run_id": "KMPC-026",
        "scope": "PF-064 repair; exact-set validator plus frozen algebra regression; no solve or ODE",
        "runtime_seconds": time.monotonic() - start,
        "internal_limit_seconds": max_runtime_seconds,
        "physics_evolution_executed": False,
        "matrix_solve_executed": False,
        "score_effect": 0,
        "frozen_algebra_source": str(algebra_path),
        "frozen_algebra_sha256": algebra_hash,
        "expected_frozen_algebra_sha256": FROZEN_ALGEBRA_SHA256,
        "authoritative_contract": {
            "state": list(AUTHORITATIVE_STATE),
            "driver": list(AUTHORITATIVE_DRIVER),
            "holdout": list(AUTHORITATIVE_HOLDOUT),
        },
        "production_validation": {
            "valid": production.valid,
            "errors": list(production.errors),
        },
        "negative_fixtures": fixture_results,
        "frozen_algebra_exact_residuals": algebra["exact_residuals"],
        "checks": checks,
        "execution_verdict": "PASS_R_A_B1_CONTRACT_GUARD_ONLY" if passed else "STOP_R_A_B1_CONTRACT_GUARD",
    }

