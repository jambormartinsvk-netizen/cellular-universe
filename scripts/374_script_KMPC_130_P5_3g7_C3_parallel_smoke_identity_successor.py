"""Thin KMPC-130 identity/smoke successor over frozen runner 373.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

from baseScripts.p5_general_synchronous import (
    c3_zero_variant_parallel_v2_smoke_identity as c3,
)


RUN_ID = "KMPC-130"
EXPECTED_BASE_SHA256 = (
    "C2ECBAF99CDCCE5CCDB9B3F5EAD8C19528687E0CA19E9021B707F453B7AA59C6"
)
LEGACY_RUNNER = Path(__file__).resolve().with_name(
    "373_script_KMPC_129_P5_3g7_C3_parallel_zero_variant_pair.py"
)
EXPECTED_LEGACY_RUNNER_SHA256 = (
    "8B04AEFF533F70A2D13B6D4772F2743BD956877B00332B37F65FA7200A241803"
)


def _load_frozen_runner() -> object:
    observed = c3.sha256_file(LEGACY_RUNNER)
    if observed != EXPECTED_LEGACY_RUNNER_SHA256:
        raise RuntimeError(
            f"frozen KMPC-129 runner SHA mismatch: {observed}"
        )
    spec = importlib.util.spec_from_file_location("kmpc129_frozen_runner", LEGACY_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen KMPC-129 runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.c3 = c3
    module.RUN_ID = RUN_ID
    module.EXPECTED_BASE_SHA256 = EXPECTED_BASE_SHA256
    module.__file__ = __file__
    return module


def main(argv: list[str] | None = None) -> int:
    runner = _load_frozen_runner()
    return runner.main(argv)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(
            f"{RUN_ID} pre-output technical failure: {type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        raise SystemExit(2)
