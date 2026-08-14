#!/usr/bin/env python
"""JSON numpy.bool_ serialization alias for unchanged script 93."""

from __future__ import annotations

import json
from pathlib import Path
import runpy

import numpy as np

_old = json.JSONEncoder.default


def _default(self, value):
    if isinstance(value, np.bool_):
        return bool(value)
    return _old(self, value)


json.JSONEncoder.default = _default
runpy.run_path(
    str(Path(__file__).with_name("93_script_A2_K4_3b_RG_BR2_velocity_roundoff_condition_gate.py")),
    run_name="__main__",
)
