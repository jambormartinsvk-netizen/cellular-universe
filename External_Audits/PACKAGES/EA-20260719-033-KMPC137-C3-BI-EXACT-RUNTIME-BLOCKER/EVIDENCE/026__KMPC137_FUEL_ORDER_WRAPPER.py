"""KMPC-137 thin fuel-owner order wrapper over frozen KMPC-136.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only JSON-roundtripped fuel owner insertion order is restored before the
frozen two-wave exact-resume merge.
"""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
from typing import Iterator, Mapping

from . import c3_zero_variant_parallel_v8_bi_k0p15_two_wave_exact_resume as v8


RUN_ID = "KMPC-137"
TARGET = v8.TARGET
SHARDS = v8.SHARDS
EXPECTED_V8_SHA256 = (
    "3313C8861856289CFAC44B336B73D3AC4C7E153913DCFFFC3B1F3EFA6BA2802F"
)
FUEL_OWNER_ORDER = ("delta_f", "U_f")
_FROZEN_MERGE = v8.v11._merge_m1_and_fuel
_ORDER_DIAGNOSTIC: dict[str, object] | None = None

sha256_file = v8.sha256_file
shard_key = v8.shard_key
handoff_hash = v8.handoff_hash


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) != TARGET:
        raise ValueError("KMPC-137 is frozen to BI/k=0.15")
    return (
        "RUN_KMPC_137_P5_3G7_C3_BI_K0p15_ZERO_VARIANT_PAIR_"
        "FUEL_ORDERED_TWO_WAVE_HP_M1_EXACT_RESUME.json"
    )


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def _v8_hash_frozen() -> bool:
    return sha256_file(Path(v8.__file__).resolve()) == EXPECTED_V8_SHA256


@contextmanager
def _identity_overlay() -> Iterator[None]:
    before = v8.RUN_ID
    v8.RUN_ID = RUN_ID
    try:
        yield
    finally:
        v8.RUN_ID = before


def _ordered_fuel(
    fuel: Mapping[str, Mapping[int, object]],
) -> tuple[dict[str, dict[int, object]], dict[str, object]]:
    if set(fuel) != set(FUEL_OWNER_ORDER):
        raise ValueError("KMPC-137 fuel owner set mismatch")
    before_fingerprint = v8.v11._state_fingerprint(
        dict(fuel), FUEL_OWNER_ORDER
    )
    ordered = {name: dict(fuel[name]) for name in FUEL_OWNER_ORDER}
    after_fingerprint = v8.v11._state_fingerprint(ordered, FUEL_OWNER_ORDER)
    diagnostic = {
        "observed_owner_order": list(fuel),
        "restored_owner_order": list(ordered),
        "expected_owner_order": list(FUEL_OWNER_ORDER),
        "value_fingerprint_before": before_fingerprint,
        "value_fingerprint_after": after_fingerprint,
        "values_unchanged": before_fingerprint == after_fingerprint,
        "order_restored": tuple(ordered) == FUEL_OWNER_ORDER,
    }
    diagnostic["pass"] = bool(
        diagnostic["values_unchanged"] and diagnostic["order_restored"]
    )
    return ordered, diagnostic


@contextmanager
def _merge_order_overlay() -> Iterator[None]:
    global _ORDER_DIAGNOSTIC
    original = v8.v11._merge_m1_and_fuel
    _ORDER_DIAGNOSTIC = None

    def ordered_merge(hp_m1, fuel):
        global _ORDER_DIAGNOSTIC
        ordered, diagnostic = _ordered_fuel(fuel)
        _ORDER_DIAGNOSTIC = diagnostic
        return original(hp_m1, ordered)

    v8.v11._merge_m1_and_fuel = ordered_merge
    try:
        yield
    finally:
        v8.v11._merge_m1_and_fuel = original


def run_support_worker(*args, **kwargs) -> dict[str, object]:
    if not _v8_hash_frozen():
        raise RuntimeError("KMPC-137 frozen KMPC-136 base hash mismatch")
    with _identity_overlay():
        return v8.run_support_worker(*args, **kwargs)


def run_exact_worker(*args, **kwargs) -> dict[str, object]:
    if not _v8_hash_frozen():
        raise RuntimeError("KMPC-137 frozen KMPC-136 base hash mismatch")
    with _identity_overlay(), _merge_order_overlay():
        payload = v8.run_exact_worker(*args, **kwargs)
    owner_restored = v8.v11._merge_m1_and_fuel is _FROZEN_MERGE
    if _ORDER_DIAGNOSTIC is None:
        raise RuntimeError("KMPC-137 fuel-order diagnostic missing")
    payload["fuel_order_roundtrip"] = _ORDER_DIAGNOSTIC
    payload["technical_checks"]["fuel_owner_order_restored"] = bool(
        _ORDER_DIAGNOSTIC["order_restored"]
    )
    payload["technical_checks"]["fuel_values_unchanged_by_reorder"] = bool(
        _ORDER_DIAGNOSTIC["values_unchanged"]
    )
    payload["technical_checks"]["merge_owner_restored"] = owner_restored
    payload["technical_checks"]["frozen_KMPC136_base_hash"] = _v8_hash_frozen()
    payload["technical_pass"] = all(payload["technical_checks"].values())
    return payload


def run_worker_smoke(*args, **kwargs) -> dict[str, object]:
    with _identity_overlay():
        payload = v8.run_worker_smoke(*args, **kwargs)
    payload["checks"]["frozen_KMPC136_base_hash"] = _v8_hash_frozen()
    payload["pass"] = all(payload["checks"].values())
    return payload


def run_exact_worker_smoke(*args, **kwargs) -> dict[str, object]:
    with _identity_overlay():
        payload = v8.run_exact_worker_smoke(*args, **kwargs)
    original = {
        "delta_f": {0: 1.25, 1: -2.5},
        "U_f": {0: 3.75, 1: -4.5},
    }
    roundtripped = json.loads(json.dumps(original, sort_keys=True))
    restored_input = {
        name: {int(power): value for power, value in coefficients.items()}
        for name, coefficients in roundtripped.items()
    }
    ordered, diagnostic = _ordered_fuel(restored_input)
    payload["fuel_order_roundtrip_fixture"] = diagnostic
    payload["checks"].update({
        "json_roundtrip_reorders_fuel_owners": tuple(restored_input)
        == ("U_f", "delta_f"),
        "adapter_restores_frozen_fuel_order": tuple(ordered)
        == FUEL_OWNER_ORDER,
        "adapter_preserves_fuel_values": bool(diagnostic["values_unchanged"]),
        "frozen_KMPC136_base_hash": _v8_hash_frozen(),
    })
    payload["pass"] = all(payload["checks"].values())
    return payload


def aggregate_shards(*args, **kwargs) -> dict[str, object]:
    with _identity_overlay():
        payload = v8.aggregate_shards(*args, **kwargs)
    wrapper_path = Path(__file__).resolve()
    payload["source_hashes"][wrapper_path.name] = sha256_file(wrapper_path)
    payload["process_architecture"]["fuel_owner_order_roundtrip"] = {
        "expected_owner_order": list(FUEL_OWNER_ORDER),
        "values_may_change": False,
        "frozen_KMPC136_base_sha256": EXPECTED_V8_SHA256,
    }
    if payload["pair_pass"]:
        payload["candidate_interpretation_not_verdict"] = (
            "PASS_C3_BI_K0P15_ZERO_PAIR_FUEL_ORDERED_TWO_WAVE_"
            "HP_M1_EXACT_RESUME_CANDIDATE_ONLY"
        )
    return payload


def aggregate_smoke_shards(*args, **kwargs) -> dict[str, object]:
    with _identity_overlay():
        payload = v8.aggregate_smoke_shards(*args, **kwargs)
    payload["checks"]["frozen_KMPC136_base_hash"] = _v8_hash_frozen()
    payload["pass"] = all(payload["checks"].values())
    return payload
