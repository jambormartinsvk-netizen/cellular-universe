#!/usr/bin/env python
"""JSON-type-fixed execution alias for script 91.

The numerical source remains script 91.  This wrapper only teaches the
standard JSON encoder to serialize numpy.bool_ as a native bool, then executes
script 91 with the original command-line arguments.
"""

from __future__ import annotations

import json
from pathlib import Path
import runpy

import numpy as np


_original_default = json.JSONEncoder.default


def _numpy_bool_default(self, value):
    if isinstance(value, np.bool_):
        return bool(value)
    return _original_default(self, value)


json.JSONEncoder.default = _numpy_bool_default
runpy.run_path(
    str(Path(__file__).with_name("91_script_A2_K4_3b_RG_BR2_Omega_conditioned_DAE.py")),
    run_name="__main__",
)
