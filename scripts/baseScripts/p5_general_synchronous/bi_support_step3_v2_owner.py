"""KMPC-046 owner-only successor for KMPC-045 / PF-074."""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
from typing import Iterator

from . import bi_support_step3 as v1


RUN_ID = "KMPC-046"
HELPER_NAME = "_s_c0_actual_coefficient_guard"


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    hashes = v1.source_hashes()
    path = Path(__file__).resolve()
    hashes[path.name] = _sha256_file(path)
    return hashes


def _source_helper() -> object:
    owner = v1.step2.bi1.c1
    helper = getattr(owner, HELPER_NAME, None)
    if helper is None or not callable(helper):
        raise RuntimeError("KMPC-046 S-C0 source helper missing or not callable")
    if getattr(helper, "__module__", None) != owner.__name__:
        raise RuntimeError("KMPC-046 S-C0 helper module owner mismatch")
    return helper


def _owner_guard() -> bool:
    target = v1.step2.bi1
    helper = _source_helper()
    return bool(
        not hasattr(target, HELPER_NAME)
        and v1.step2.bi1.c1 is not target
        and getattr(helper, "__name__", None) == HELPER_NAME
    )


@contextmanager
def _helper_owner_bridge() -> Iterator[None]:
    target = v1.step2.bi1
    helper = _source_helper()
    if not _owner_guard():
        raise RuntimeError("KMPC-046 unexpected pre-bridge S-C0 owner state")
    setattr(target, HELPER_NAME, helper)
    try:
        if getattr(target, HELPER_NAME, None) is not helper:
            raise RuntimeError("KMPC-046 S-C0 helper bridge attach failed")
        yield
    finally:
        if hasattr(target, HELPER_NAME):
            delattr(target, HELPER_NAME)
        if hasattr(target, HELPER_NAME) or not _owner_guard():
            raise RuntimeError("KMPC-046 S-C0 helper owner was not restored")


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if max_runtime_seconds != 4.8:
        raise ValueError("KMPC-046 smoke requires exactly 4.8 seconds")
    owner_before = _owner_guard()
    helper = _source_helper()
    with _helper_owner_bridge():
        attached = getattr(v1.step2.bi1, HELPER_NAME, None) is helper
    restored = _owner_guard()
    base_payload = v1.run_smoke(max_runtime_seconds, result_dir)
    fixtures = {
        "source_owner_chain_exact": owner_before,
        "helper_callable_identity": bool(
            callable(helper)
            and getattr(helper, "__name__", None) == HELPER_NAME
            and getattr(helper, "__module__", None) == v1.step2.bi1.c1.__name__
        ),
        "bridge_attached_exact_callable": attached,
        "bridge_removed_after_context": not hasattr(v1.step2.bi1, HELPER_NAME),
        "owner_restored": restored,
        "wrong_direct_owner_rejected": v1.step2.bi1 is not v1.step2.bi1.c1,
    }
    if not all(fixtures.values()) or not base_payload["passed"]:
        raise RuntimeError("KMPC-046 owner bridge smoke failed")
    base_payload["run_id"] = RUN_ID
    base_payload["owner_bridge_fixtures"] = fixtures
    base_payload["technical_successor"] = {
        "predecessor": "KMPC-045 / PF-074",
        "only_base_change": "explicit bi_c1_coverage.c1 S-C0 helper owner bridge",
    }
    return base_payload


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if max_runtime_seconds != 4.8:
        raise ValueError("KMPC-046 audit requires exactly 4.8 seconds")
    with _helper_owner_bridge():
        payload = v1.run_audit(max_runtime_seconds, result_dir)
    payload["run_id"] = RUN_ID
    payload["test"] = (
        "A2-K4 P5.3g7 GLOBAL_C1 BI_SUPPORT_STEP_3 OWNER_SUCCESSOR "
        "support [0,5] to [0,7]"
    )
    payload["technical_successor"] = {
        "predecessor": "KMPC-045 / PF-074",
        "only_base_change": "explicit bi_c1_coverage.c1 S-C0 helper owner bridge",
        "physics_equations_changed": False,
        "support_or_threshold_changed": False,
        "partial_KMPC045_payload_reused": False,
        "helper_owner_restored": _owner_guard(),
    }
    payload["source_hashes"] = source_hashes()
    return payload
