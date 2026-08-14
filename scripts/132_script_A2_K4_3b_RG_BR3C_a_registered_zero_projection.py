#!/usr/bin/env python
"""BR3C-a correction projecting only preregistered exact-zero slots.

Scripts 130/131 are preserved as REVIEW.  This immutable extension does not
apply a magnitude threshold.  It projects only initial-condition and
hierarchy slots that scripts 119/127 explicitly constrain to exact zero.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "130_script_A2_K4_3b_RG_BR3C_a_two_surface_state_export.py"
)
MARKER = "'''\n\nextended = source_text"
source_text = SOURCE.read_text(encoding="utf-8")
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 130 registered-zero extension marker is not unique")

addition = r'''    (
        "br3c_registered_zero_projection",
        '        phi_coefficient = args.fuel_fraction_coefficient\n'
        '        def series_value(series, z_value):',
        '        phi_coefficient = args.fuel_fraction_coefficient\n'
        '        state_std = {name:dict(series) for name, series in std.items()}\n'
        '        state_fuel = {name:dict(series) for name, series in fuel.items()}\n'
        '        state_frac = {name:dict(series) for name, series in physical["raw"].items()}\n'
        '        projection_ledger = []\n'
        '        def project_zero(container, component, power, scope):\n'
        '            before = float(container[component].get(power, 0.0))\n'
        '            container[component][power] = 0.0\n'
        '            projection_ledger.append({"scope":scope, "component":component,\n'
        '                "power":int(power), "value_before":before, "value_after":0.0})\n'
        '        if mode == "NID":\n'
        '            for component in VARS:\n'
        '                project_zero(state_std, component, -1, "NID initial minus-one")\n'
        '            for component in ("h", "eta", "db", "dc", "sig", "L3", "L4"):\n'
        '                project_zero(state_std, component, 0, "NID exact zero anchor")\n'
        '        else:\n'
        '            for component in ("h", "eta", "dg", "dn", "db", "dc", "sig", "L3", "L4"):\n'
        '                project_zero(state_std, component, -1, "NIV exact zero minus-one")\n'
        '                project_zero(state_std, component, 0, "NIV exact zero anchor")\n'
        '        hierarchy_m = 2 if mode == "NID" else 1\n'
        '        for exponent in std_exponents:\n'
        '            if 1 <= exponent < hierarchy_m+2:\n'
        '                project_zero(state_std, "L3", exponent, "standard L3 regularity")\n'
        '            if 1 <= exponent < hierarchy_m+4:\n'
        '                project_zero(state_std, "L4", exponent, "standard L4 regularity")\n'
        '        for component in ("df", "Uf"):\n'
        '            project_zero(state_fuel, component, -1, "fuel initial condition")\n'
        '            project_zero(state_fuel, component, 0, "fuel initial condition")\n'
        '        first_l3 = 4 if mode == "NID" else 3\n'
        '        first_l4 = first_l3+2\n'
        '        for layer in list(state_frac["L3"]):\n'
        '            if int(layer) < first_l3:\n'
        '                project_zero(state_frac, "L3", int(layer), "fractional L3 regularity")\n'
        '        for layer in list(state_frac["L4"]):\n'
        '            if int(layer) < first_l4:\n'
        '                project_zero(state_frac, "L4", int(layer), "fractional L4 regularity")\n'
        '        checks[f"{mode}_projection_has_only_registered_slots"] = all(\n'
        '            item["scope"] in {"NID initial minus-one", "NID exact zero anchor",\n'
        '                "NIV exact zero minus-one", "NIV exact zero anchor",\n'
        '                "standard L3 regularity", "standard L4 regularity",\n'
        '                "fuel initial condition", "fractional L3 regularity",\n'
        '                "fractional L4 regularity"} for item in projection_ledger)\n'
        '        def series_value(series, z_value):',
    ),
    (
        "br3c_use_projected_standard_state",
        '            standard_state = {name:series_value(std[name], z_value)\n',
        '            standard_state = {name:series_value(state_std[name], z_value)\n',
    ),
    (
        "br3c_use_projected_fractional_state",
        '            fractional_state = {name:fractional_value(physical["raw"][name], z_value)\n',
        '            fractional_state = {name:fractional_value(state_frac[name], z_value)\n',
    ),
    (
        "br3c_use_projected_h_derivative",
        '            h_x = (series_dx(std["h"], z_value)\n'
        '                   + phi_coefficient*fractional_dx(physical["raw"]["h"], z_value))',
        '            h_x = (series_dx(state_std["h"], z_value)\n'
        '                   + phi_coefficient*fractional_dx(state_frac["h"], z_value))',
    ),
    (
        "br3c_use_projected_eta_derivative",
        '            eta_x = (series_dx(std["eta"], z_value)\n'
        '                     + phi_coefficient*fractional_dx(physical["raw"]["eta"], z_value))',
        '            eta_x = (series_dx(state_std["eta"], z_value)\n'
        '                     + phi_coefficient*fractional_dx(state_frac["eta"], z_value))',
    ),
    (
        "br3c_use_projected_fuel",
        '            delta_f = series_value(fuel["df"], z_value)\n'
        '            U_f = series_value(fuel["Uf"], z_value)',
        '            delta_f = series_value(state_fuel["df"], z_value)\n'
        '            U_f = series_value(state_fuel["Uf"], z_value)',
    ),
    (
        "br3c_use_projected_anchor",
        '        anchor_value = std["dn"].get(0, 0.0) if mode == "NID" else std["Un"].get(-1, 0.0)',
        '        anchor_value = state_std["dn"].get(0, 0.0) if mode == "NID" else state_std["Un"].get(-1, 0.0)',
    ),
    (
        "br3c_projection_output",
        '            "surfaces":mode_surfaces,\n'
        '        }',
        '            "surfaces":mode_surfaces,\n'
        '            "registered_zero_projection":projection_ledger,\n'
        '            "maximum_projected_absolute_value":max(abs(item["value_before"]) for item in projection_ledger),\n'
        '        }',
    ),
    (
        "br3c_projected_test_identity",
        '"test":"A2-K4.3b-RG-BR3C-a two-surface initial-state export"',
        '"test":"A2-K4.3b-RG-BR3C-a registered-zero projected state export"',
    ),
    (
        "br3c_projected_execution",
        '"execution_verdict":"PASS_BR3C_A_TWO_SURFACE_STATE" if passed else "REVIEW_BR3C_A_STATE_UNCLOSED"',
        '"execution_verdict":"PASS_BR3C_A_REGISTERED_ZERO_STATE" if passed else "REVIEW_BR3C_A_PROJECTED_STATE_UNCLOSED"',
    ),
    (
        "br3c_projected_physical",
        '"physical_verdict":"K4 survives C7.7a state construction" if passed else "no death verdict; audit first failed row"',
        '"physical_verdict":"K4 survives corrected C7.7a state construction" if passed else "no death verdict; audit first failed row"',
    ),
'''

extended = source_text.replace(MARKER, addition + "'''\n\nextended = source_text", 1)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

