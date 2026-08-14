"""CLI runner for the KMPC-142 NID/.05 exact identity-schema adapter.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Process architecture is delegated to the frozen KMPC-131 runner.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

from baseScripts.p5_general_synchronous import (
    c3_zero_variant_parallel_v4_nid_k0p05_identity_adapter as c3,
)


RUN_ID = "KMPC-142"
EXPECTED_BASE_SHA256 = (
    "7151201BE9007263D8345FD63C54129BE2A1B2898C5D5CF02D0C9F4322853354"
)
_LEGACY_RUNNER_PATH = Path(__file__).with_name(
    "375_script_KMPC_131_P5_3g7_C3_four_support_shards.py"
)
_SPEC = importlib.util.spec_from_file_location(
    "_kmpc131_four_support_shards_frozen", _LEGACY_RUNNER_PATH
)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError("cannot load frozen KMPC-131 runner")
_LEGACY = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_LEGACY)

# Redirect only module ownership and run identity. The implementation body,
# four-worker process architecture, limits and aggregate gates remain frozen.
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
