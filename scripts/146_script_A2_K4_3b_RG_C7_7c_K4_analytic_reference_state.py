#!/usr/bin/env python
"""C7.7c-K4 immutable third-surface extension of registered state 132.

The x_reference surface is evaluated by the already audited coefficient
engine.  It is exported only for preregistered numerical scaling and is not
an evolved endpoint or an endpoint-agreement test.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "132_script_A2_K4_3b_RG_BR3C_a_registered_zero_projection.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\nextended = source_text"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 132 analytic-reference extension marker is not unique")

addition = r'''    (
        "analytic_reference_parser",
        '    parser.add_argument("--fuel-fraction-coefficient", type=float, default=1.0)',
        '    parser.add_argument("--fuel-fraction-coefficient", type=float, default=1.0)\n'
        '    parser.add_argument("--x-reference", type=float, default=-18.0)',
    ),
    (
        "analytic_reference_validation",
        '    if not 0.0 < args.fuel_fraction_coefficient <= 1.0:\n'
        '        parser.error("fuel fraction coefficient must be in (0,1]")',
        '    if not 0.0 < args.fuel_fraction_coefficient <= 1.0:\n'
        '        parser.error("fuel fraction coefficient must be in (0,1]")\n'
        '    if not -19.0 <= args.x_reference <= -18.0:\n'
        '        parser.error("x_reference must be in [-19,-18]")\n'
        '    if not args.x_reference > args.x_shallow:\n'
        '        parser.error("x_reference must be later than x_shallow")',
    ),
    (
        "analytic_reference_surface",
        '        for surface_name, x_value in (("deep", args.x_deep),\n'
        '                                      ("shallow", args.x_shallow)):',
        '        for surface_name, x_value in (("deep", args.x_deep),\n'
        '                                      ("shallow", args.x_shallow),\n'
        '                                      ("reference", args.x_reference)):',
    ),
    (
        "analytic_reference_order_check",
        '        checks[f"{mode}_same_series_used_on_both_surfaces"] = True',
        '        checks[f"{mode}_same_series_used_on_both_surfaces"] = True\n'
        '        checks[f"{mode}_analytic_reference_later_than_starts"] = (\n'
        '            z_values["shallow"] < z_values["reference"] < 0.1)\n'
        '        checks[f"{mode}_same_series_used_for_reference_scale"] = True',
    ),
    (
        "analytic_reference_identity",
        '"test":"A2-K4.3b-RG-BR3C-a registered-zero projected state export"',
        '"test":"A2-K4.3b-RG C7.7c-K4 analytic-reference state export"',
    ),
    (
        "analytic_reference_execution",
        '"execution_verdict":"PASS_BR3C_A_REGISTERED_ZERO_STATE" if passed else "REVIEW_BR3C_A_PROJECTED_STATE_UNCLOSED"',
        '"execution_verdict":"PASS_C7_7C_K4_ANALYTIC_REFERENCE_STATE" if passed else "REVIEW_C7_7C_K4_REFERENCE_UNCLOSED"',
    ),
    (
        "analytic_reference_physical_scope",
        '"physical_verdict":"K4 survives corrected C7.7a state construction" if passed else "no death verdict; audit first failed row"',
        '"physical_verdict":"analytic reference exported for scaling only; no evolution claim" if passed else "no death verdict; audit first failed row"',
    ),
'''

extended = source_text.replace(MARKER, addition + "'''\n\nextended = source_text", 1)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

