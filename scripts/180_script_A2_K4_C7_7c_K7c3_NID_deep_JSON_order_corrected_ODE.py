#!/usr/bin/env python
"""Immutable JSON-key-order correction of K7c.3 script 179."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "179_script_A2_K4_C7_7c_K7c3_NID_deep_short_projected_ODE.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
old = (
    "    if tuple(deep_seed) != NAMES or tuple(shallow_seed) != NAMES:\n"
    "        raise RuntimeError(\"K7c.2 seed names changed\")\n"
)
new = (
    "    if set(deep_seed) != set(NAMES) or set(shallow_seed) != set(NAMES):\n"
    "        raise RuntimeError(\"K7c.2 seed-name set changed\")\n"
)
if source_text.count(old) != 1:
    raise RuntimeError("script 179 seed-name marker is not unique")
source_text = source_text.replace(old, new, 1)
source_text = source_text.replace(
    "A2-K4 C7.7c-K7c.3 NID/deep short projected ODE smoke test",
    "A2-K4 C7.7c-K7c.3 NID/deep JSON-order-corrected projected ODE",
    1,
)
source_text = source_text.replace(
    "PASS_C7_7C_K7C3_NID_DEEP_SHORT_PROJECTED_ODE",
    "PASS_C7_7C_K7C3_NID_DEEP_JSON_ORDER_CORRECTED_ODE",
    1,
)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
