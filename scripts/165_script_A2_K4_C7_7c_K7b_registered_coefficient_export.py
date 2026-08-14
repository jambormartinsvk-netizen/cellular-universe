#!/usr/bin/env python
"""Immutable K7b export of post-projection registered Puiseux coefficients.

The numerical coefficient solver is not rerun at higher precision.  This
extension exposes its already registered float64 coefficients after the exact
zero projection so that a separate bounded script can evaluate powers and
compensated sums with mpmath.  No ODE is integrated and no score is awarded.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "146_script_A2_K4_3b_RG_C7_7c_K4_analytic_reference_state.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\nextended = source_text"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 146 K7b coefficient-export marker is not unique")

addition = r'''    (
        "K7b_coefficient_registry_initialization",
        '    checks = {}; results = {}; state_surfaces = {}',
        '    checks = {}; results = {}; state_surfaces = {}; coefficient_registry = {}',
    ),
    (
        "K7b_post_projection_coefficient_registry",
        '        state_surfaces[mode] = {\n',
        '        coefficient_registry[mode] = {\n'
        '            "standard": {name:{str(power):float(value)\n'
        '                for power,value in series.items()}\n'
        '                for name,series in state_std.items()},\n'
        '            "fractional": {name:{str(power):float(value)\n'
        '                for power,value in series.items()}\n'
        '                for name,series in state_frac.items()},\n'
        '            "fuel": {name:{str(power):float(value)\n'
        '                for power,value in series.items()}\n'
        '                for name,series in state_fuel.items()},\n'
        '        }\n'
        '        state_surfaces[mode] = {\n',
    ),
    (
        "K7b_coefficient_registry_output",
        '      "mode_results":results,"BR3C_state_surfaces":state_surfaces,"checks":checks,',
        '      "mode_results":results,"BR3C_state_surfaces":state_surfaces,\n'
        '      "K7b_coefficient_registry":coefficient_registry,"checks":checks,',
    ),
    (
        "K7b_coefficient_export_identity",
        '"test":"A2-K4.3b-RG C7.7c-K4 analytic-reference state export"',
        '"test":"A2-K4 C7.7c-K7b registered coefficient export"',
    ),
    (
        "K7b_coefficient_export_scope",
        '"physical_verdict":"analytic reference exported for scaling only; no evolution claim" if passed else "no death verdict; audit first failed row"',
        '"physical_verdict":"registered coefficients exported for high-precision K7b evaluation; no evolution claim" if passed else "no death verdict; audit first failed row"',
    ),
'''

extended = source_text.replace(MARKER, addition + "'''\n\nextended = source_text", 1)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

