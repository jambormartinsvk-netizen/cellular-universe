"""CLI runner for KMPC-144 NID/.15 af0/audit-only refinement.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Process architecture is delegated to the frozen KMPC-131 runner.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

from baseScripts.p5_general_synchronous import (
    c3_zero_variant_parallel_v6_nid_k0p15_af0_same_matrix_refinement as c3,
)


RUN_ID = "KMPC-144"
EXPECTED_BASE_SHA256 = (
    "B84A51D466ED4667A35653859B6E842C5529443A76EBF86BD22B1FDEA8272646"
)
_LEGACY_RUNNER_PATH = Path(__file__).with_name(
    "375_script_KMPC_131_P5_3g7_C3_four_support_shards.py"
)
_SPEC = importlib.util.spec_from_file_location(
    "_kmpc131_four_support_shards_frozen_for_kmpc144", _LEGACY_RUNNER_PATH
)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError("cannot load frozen KMPC-131 runner")
_LEGACY = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_LEGACY)

_LEGACY.c3 = c3
_LEGACY.RUN_ID = RUN_ID
_LEGACY.EXPECTED_BASE_SHA256 = EXPECTED_BASE_SHA256
_LEGACY.SHARD_CHOICES = tuple(c3.shard_key(*shard) for shard in c3.SHARDS)
_LEGACY.__file__ = __file__


def main(argv: list[str] | None = None) -> int:
    return _LEGACY.main(argv)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(
            f"{RUN_ID} pre-output technical failure: "
            f"{type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        raise SystemExit(2)
