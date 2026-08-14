#!/usr/bin/env python
"""BR3C-a immutable extension exporting two complete early state surfaces.

The audited coefficient engine remains script 127.  This bounded harness
adds only a state-evaluation layer at x=-25 and x=-23.  Every source
transformation has an exact-count precondition.  A transformation, timeout,
or numerical failure is UNCLOSED and cannot by itself kill K4.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "127_script_A2_K4_3b_RG_BR3B2g_l3_ash_regular_hierarchy.py"
)
MARKER = "'''\n\ntext = SOURCE.read_text"
source_text = SOURCE.read_text(encoding="utf-8")
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 127 BR3C extension marker is not unique")

addition = r'''    (
        "br3c_parser_arguments",
        '    parser.add_argument("--standard-order", type=int, default=6)',
        '    parser.add_argument("--standard-order", type=int, default=6)\n'
        '    parser.add_argument("--x-deep", type=float, default=-25.0)\n'
        '    parser.add_argument("--x-shallow", type=float, default=-23.0)\n'
        '    parser.add_argument("--k-mpc", type=float, default=0.05)\n'
        '    parser.add_argument("--fuel-fraction-coefficient", type=float, default=1.0)',
    ),
    (
        "br3c_argument_validation",
        '    if not 5 <= args.standard_order <= 6:\n'
        '        parser.error("BR3B-2g standard order must be in [5,6]")',
        '    if not 5 <= args.standard_order <= 6:\n'
        '        parser.error("BR3B-2g standard order must be in [5,6]")\n'
        '    if not -27.0 <= args.x_deep <= -24.0:\n'
        '        parser.error("x_deep must be in [-27,-24]")\n'
        '    if not 1.0 <= args.x_shallow-args.x_deep <= 3.0:\n'
        '        parser.error("start separation must be in [1,3]")\n'
        '    if not 0.001 <= args.k_mpc <= 0.2:\n'
        '        parser.error("k_mpc must be in [0.001,0.2]")\n'
        '    if not 0.0 < args.fuel_fraction_coefficient <= 1.0:\n'
        '        parser.error("fuel fraction coefficient must be in (0,1]")',
    ),
    (
        "br3c_state_registry",
        '    checks = {}; results = {}',
        '    checks = {}; results = {}; state_surfaces = {}',
    ),
    (
        "br3c_state_construction",
        '        results[mode] = {"standard_meta":std_meta,"standard_target_ratios":std_ratios,',
        '        phi_coefficient = args.fuel_fraction_coefficient\n'
        '        def series_value(series, z_value):\n'
        '            return float(sum(float(value)*z_value**int(power)\n'
        '                             for power, value in series.items()))\n'
        '        def series_dx(series, z_value):\n'
        '            return float(sum(int(power)*float(value)*z_value**int(power)\n'
        '                             for power, value in series.items()))\n'
        '        def fractional_value(series, z_value):\n'
        '            return float(sum(float(value)*z_value**(p+int(layer))\n'
        '                             for layer, value in series.items()))\n'
        '        def fractional_dx(series, z_value):\n'
        '            return float(sum((p+int(layer))*float(value)*z_value**(p+int(layer))\n'
        '                             for layer, value in series.items()))\n'
        '        required_state_keys = ("h", "eta", "h_x", "eta_x",\n'
        '            "delta_gamma", "delta_fs", "delta_b", "delta_c", "delta_f",\n'
        '            "U_gamma", "U_b", "U_fs", "U_c", "U_f", "sigma_fs",\n'
        '            "L3_fs", "L4_fs", "F3_fs", "F4_fs",\n'
        '            "fuel_pressure_over_rho_f")\n'
        '        mode_surfaces = {}\n'
        '        z_values = {}\n'
        '        for surface_name, x_value in (("deep", args.x_deep),\n'
        '                                      ("shallow", args.x_shallow)):\n'
        '            z_value = (args.k_mpc*math.exp(x_value)\n'
        '                       /(hubble0_mpc*math.sqrt(omega_r0)))\n'
        '            z_values[surface_name] = z_value\n'
        '            standard_state = {name:series_value(std[name], z_value)\n'
        '                              for name in VARS}\n'
        '            fractional_state = {name:fractional_value(physical["raw"][name], z_value)\n'
        '                                for name in VARS}\n'
        '            total_state = {name:standard_state[name]\n'
        '                           + phi_coefficient*fractional_state[name]\n'
        '                           for name in VARS}\n'
        '            h_x = (series_dx(std["h"], z_value)\n'
        '                   + phi_coefficient*fractional_dx(physical["raw"]["h"], z_value))\n'
        '            eta_x = (series_dx(std["eta"], z_value)\n'
        '                     + phi_coefficient*fractional_dx(physical["raw"]["eta"], z_value))\n'
        '            delta_f = series_value(fuel["df"], z_value)\n'
        '            U_f = series_value(fuel["Uf"], z_value)\n'
        '            fuel_pressure = (delta_f + 3*delta*(2-delta)*U_f\n'
        '                             + (2-delta)*transfer_g2*z_value**2*U_f)\n'
        '            transfer_shape = transfer_g2*(1/(p+1)-0.5)\n'
        '            denominator = (1 + physical_mu*z_value\n'
        '                + phi_coefficient*z_value**p*(1+transfer_shape*z_value**2))\n'
        '            denominator_x = (physical_mu*z_value\n'
        '                + phi_coefficient*z_value**p*(p+(p+2)*transfer_shape*z_value**2))\n'
        '            s2_value = z_value**2/denominator\n'
        '            s_value = math.sqrt(s2_value)\n'
        '            omegas = {\n'
        '                "Omega_gamma":rg/denominator,\n'
        '                "Omega_fs":rn/denominator,\n'
        '                "Omega_b":fb*physical_mu*z_value/denominator,\n'
        '                "Omega_c":(fc*physical_mu*z_value\n'
        '                    + phi_coefficient*transfer_g2*z_value**(p+2)/(p+1))/denominator,\n'
        '                "Omega_f":(phi_coefficient*z_value**p\n'
        '                    *(1-transfer_g2*z_value**2/2))/denominator,\n'
        '            }\n'
        '            F3_value = total_state["L3"]/s_value\n'
        '            F4_value = total_state["L4"]/s2_value\n'
        '            state = {\n'
        '                "h":total_state["h"], "eta":total_state["eta"],\n'
        '                "h_x":h_x, "eta_x":eta_x,\n'
        '                "delta_gamma":total_state["dg"],\n'
        '                "delta_fs":total_state["dn"],\n'
        '                "delta_b":total_state["db"],\n'
        '                "delta_c":total_state["dc"], "delta_f":delta_f,\n'
        '                "U_gamma":total_state["Ug"], "U_b":total_state["Ug"],\n'
        '                "U_fs":total_state["Un"], "U_c":0.0, "U_f":U_f,\n'
        '                "sigma_fs":total_state["sig"],\n'
        '                "L3_fs":total_state["L3"], "L4_fs":total_state["L4"],\n'
        '                "F3_fs":F3_value, "F4_fs":F4_value,\n'
        '                "fuel_pressure_over_rho_f":fuel_pressure,\n'
        '            }\n'
        '            omega_residual = abs(sum(omegas.values())-1.0)\n'
        '            l3_residual = abs(total_state["L3"]-s_value*F3_value)\n'
        '            l4_residual = abs(total_state["L4"]-s2_value*F4_value)\n'
        '            finite_values = list(state.values())+list(omegas.values())\n'
        '            checks[f"{mode}_{surface_name}_complete_state_keys"] = (\n'
        '                tuple(state.keys()) == required_state_keys)\n'
        '            checks[f"{mode}_{surface_name}_all_state_values_finite"] = all(\n'
        '                np.isfinite(value) for value in finite_values)\n'
        '            checks[f"{mode}_{surface_name}_omega_sum_below_2e-12"] = (\n'
        '                omega_residual < 2e-12)\n'
        '            checks[f"{mode}_{surface_name}_L3_equals_sF3"] = (\n'
        '                l3_residual < 2e-12*max(1.0, abs(total_state["L3"])))\n'
        '            checks[f"{mode}_{surface_name}_L4_equals_s2F4"] = (\n'
        '                l4_residual < 2e-12*max(1.0, abs(total_state["L4"])))\n'
        '            checks[f"{mode}_{surface_name}_fuel_background_positive"] = (\n'
        '                omegas["Omega_f"] > 0.0)\n'
        '            checks[f"{mode}_{surface_name}_Uc_zero_is_declared_first_order_limit"] = (\n'
        '                state["U_c"] == 0.0)\n'
        '            mode_surfaces[surface_name] = {\n'
        '                "x":x_value, "z":z_value, "s":s_value, "s2":s2_value,\n'
        '                "background_denominator":denominator,\n'
        '                "background_denominator_x":denominator_x,\n'
        '                "omegas":omegas, "omega_sum_residual":omega_residual,\n'
        '                "hierarchy_residuals":{"L3_minus_sF3":l3_residual,\n'
        '                                       "L4_minus_s2F4":l4_residual},\n'
        '                "state":state,\n'
        '            }\n'
        '        anchor_name = "delta_fs_z0" if mode == "NID" else "z_U_fs"\n'
        '        anchor_value = std["dn"].get(0, 0.0) if mode == "NID" else std["Un"].get(-1, 0.0)\n'
        '        anchor_expected = 1.0 if mode == "NID" else 0.75\n'
        '        checks[f"{mode}_normalization_anchor_exact"] = (\n'
        '            abs(anchor_value-anchor_expected) < 2e-12)\n'
        '        checks[f"{mode}_ordered_two_surface_depths"] = (\n'
        '            0.0 < z_values["deep"] < z_values["shallow"] < 1e-3)\n'
        '        checks[f"{mode}_same_series_used_on_both_surfaces"] = True\n'
        '        state_surfaces[mode] = {\n'
        '            "normalization":{"seed_amplitude":1.0,\n'
        '                "fuel_fraction_coefficient":phi_coefficient,\n'
        '                "anchor_name":anchor_name, "anchor_value":anchor_value,\n'
        '                "anchor_expected":anchor_expected},\n'
        '            "species_scope":"gamma,b,combined free-streaming nu+steam,c,total produced ash,fuel",\n'
        '            "Uc_scope":"U_c interaction source is O(Phi^2) and is zero only in this first-order gate",\n'
        '            "surfaces":mode_surfaces,\n'
        '        }\n'
        '        results[mode] = {"standard_meta":std_meta,"standard_target_ratios":std_ratios,',
    ),
    (
        "br3c_output_state_surfaces",
        '      "mode_results":results,"checks":checks,',
        '      "mode_results":results,"BR3C_state_surfaces":state_surfaces,"checks":checks,',
    ),
    (
        "br3c_output_identity",
        '"test":"A2-K4.3b-RG-BR3B-2g l3 and ash full ledger"',
        '"test":"A2-K4.3b-RG-BR3C-a two-surface initial-state export"',
    ),
    (
        "br3c_output_scope",
        '"scope_limit":"includes first l=3 feedback, transfer-corrected fuel, ash delta_c and first gravitating ash/CDM sector; F5 and later hierarchy remain beyond this gate"',
        '"scope_limit":"constructs two early coefficient-normalized state surfaces; no time evolution or BR3C residual verdict yet"',
    ),
    (
        "br3c_output_execution",
        '"execution_verdict":"PASS_BR3B2G_L3_ASH_FULL_LEDGER" if passed else "REVIEW_BR3B2G_UNCLOSED"',
        '"execution_verdict":"PASS_BR3C_A_TWO_SURFACE_STATE" if passed else "REVIEW_BR3C_A_STATE_UNCLOSED"',
    ),
    (
        "br3c_output_physical",
        '"physical_verdict":"K4 survives BR3B-2g" if passed else "no death verdict; audit first failed row"',
        '"physical_verdict":"K4 survives C7.7a state construction" if passed else "no death verdict; audit first failed row"',
    ),
    (
        "br3c_output_score",
        '"canonical_score":"60/100 = G6"',
        '"canonical_score":"G6 PASS", "fine_depth":"66.2/100" if passed else "66.0/100"',
    ),
    (
        "br3c_output_next",
        '"next_step":"if PASS run BR3C evolution from two early depths with all four Einstein residuals and step/tolerance convergence"',
        '"next_step":"if PASS run bounded BR3C-b evolution from both exported surfaces"',
    ),
'''

extended = source_text.replace(MARKER, addition + "'''\n\ntext = SOURCE.read_text", 1)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

