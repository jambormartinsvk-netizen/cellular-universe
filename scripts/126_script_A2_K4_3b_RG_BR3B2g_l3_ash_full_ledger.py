#!/usr/bin/env python
"""BR3B-2g immutable extension of the audited BR3B-2f-5 solver.

The verified coefficient engine lives in script 119 and is never modified.
This harness performs an explicit, checked source transformation which:

* repairs the two technical defects already documented by scripts 121/124;
* uses the species-local free-streaming velocity in the legacy shear oracle;
* adds the rescaled massless hierarchy variables
  L3=(k/Hconf)F3 and L4=(k/Hconf)^2 F4;
* adds the first-order transfer background, fuel-depletion, ash-production,
  fuel-perturbation, and CDM perturbation terms fixed by g=Gamma/H;
* extends NID through p+5 and NIV through p+4.

All replacements have exact-count preconditions.  A precondition, syntax,
timeout, or numerical failure is UNCLOSED and cannot kill K4.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "119_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py"
)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"BR3B-2g transform precondition {label!r}: expected 1, got {count}"
        )
    return text.replace(old, new, 1)


text = SOURCE.read_text(encoding="utf-8")

replacements = [
    (
        "technical_bracket",
        'vector[fuel_index[("df", 0)]], vector[fuel_index[("Uf", 0)]])',
        'vector[fuel_index[("df", 0)]], vector[fuel_index[("Uf", 0)]]])',
    ),
    (
        "json_bool",
        '    passed = bool(checks) and all(checks.values())',
        '    checks = {key: bool(value) for key, value in checks.items()}\n'
        '    passed = bool(checks) and all(checks.values())',
    ),
    (
        "species_local_oracle",
        'jns = 8/15*(uge-ugl)',
        'jns = 8/15*(une-unl)',
    ),
    (
        "variables",
        'VARS = ("h", "eta", "dg", "dn", "db", "dc", "Ug", "Un", "sig")',
        'VARS = ("h", "eta", "dg", "dn", "db", "dc", "Ug", "Un", "sig", "L3", "L4")',
    ),
    (
        "core_rows",
        'CORE_ROWS = ("gamma_continuity", "gamma_Euler", "nu_continuity",\n'
        '             "nu_shear", "nu_Euler", "Einstein_00", "Einstein_0i",\n'
        '             "Einstein_trace", "Einstein_traceless")',
        'CORE_ROWS = ("gamma_continuity", "gamma_Euler", "nu_continuity",\n'
        '             "nu_shear", "nu_Euler", "nu_l3", "nu_l4",\n'
        '             "Einstein_00", "Einstein_0i",\n'
        '             "Einstein_trace", "Einstein_traceless")',
    ),
    (
        "default_order",
        'parser.add_argument("--standard-order", type=int, default=4)',
        'parser.add_argument("--standard-order", type=int, default=6)',
    ),
    (
        "allowed_order",
        '    if not 4 <= args.standard_order <= 6:\n'
        '        parser.error("standard order must be in [4,6]")',
        '    if not 5 <= args.standard_order <= 6:\n'
        '        parser.error("BR3B-2g standard order must be in [5,6]")',
    ),
    (
        "transfer_scale",
        '    physical_mu = omega_parameter / 0.05\n',
        '    physical_mu = omega_parameter / 0.05\n'
        '    lambda_transfer = 0.15\n'
        '    transfer_g2 = lambda_transfer * (hubble0_mpc / 0.05)**2 * math.sqrt(omega_r0)\n',
    ),
    (
        "standard_hierarchy_rows",
        '            "nu_shear": sadd(sscale(sdx(v["sig"]), 2), sscale(hx, -4/15),\n'
        '                              sscale(etax, -8/5), sscale(smul(bg["s2"], v["Un"]), -8/15)),\n'
        '            "nu_Euler": sadd(sdx(v["Un"]), sscale(smul(bg["q"], v["Un"]), -1),\n'
        '                              sscale(v["dn"], -0.25), v["sig"]),',
        '            "nu_shear": sadd(sscale(sdx(v["sig"]), 2), sscale(hx, -4/15),\n'
        '                              sscale(etax, -8/5), sscale(smul(bg["s2"], v["Un"]), -8/15),\n'
        '                              sscale(v["L3"], 3/5)),\n'
        '            "nu_Euler": sadd(sdx(v["Un"]), sscale(smul(bg["q"], v["Un"]), -1),\n'
        '                              sscale(v["dn"], -0.25), v["sig"]),\n'
        '            "nu_l3": sadd(sdx(v["L3"]), smul(bg["q"], v["L3"]),\n'
        '                            sscale(smul(bg["s2"], v["sig"]), -6/7),\n'
        '                            sscale(v["L4"], 4/7)),\n'
        '            "nu_l4": sadd(sdx(v["L4"]), sscale(smul(bg["q"], v["L4"]), 2),\n'
        '                            sscale(smul(bg["s2"], v["L3"]), -4/9)),',
    ),
    (
        "NID_initial_hierarchy",
        '                           "Un": 0.25, "sig": 0.0}',
        '                           "Un": 0.25, "sig": 0.0, "L3": 0.0, "L4": 0.0}',
    ),
    (
        "NIV_initial_hierarchy",
        '            for name in ("h", "eta", "dg", "dn", "db", "dc", "sig"):',
        '            for name in ("h", "eta", "dg", "dn", "db", "dc", "sig", "L3", "L4"):',
    ),
    (
        "fuel_signature",
        '    def solve_fuel(standard, bg):',
        '    def solve_fuel(standard, bg, local_g2):',
    ),
    (
        "fuel_g_series",
        '        hx = sdx(standard["h"])\n',
        '        hx = sdx(standard["h"])\n'
        '        g_series = {2: local_g2}\n',
    ),
    (
        "fuel_transfer_equations",
        '            r1 = sadd(sdx(f["df"]), sscale(f["df"], 3*(2-delta)),\n'
        '                      sscale(smul(bg["s2"], f["Uf"]), delta), sscale(hx, delta/2),\n'
        '                      sscale(f["Uf"], 9*delta*(2-delta)))\n'
        '            r2 = sadd(sdx(f["Uf"]), sscale(smul(sadd(bg["q"], {0: 2.0}), f["Uf"]), -1),\n'
        '                      sscale(f["df"], -1/delta))',
        '            r1 = sadd(sdx(f["df"]), sscale(f["df"], 3*(2-delta)),\n'
        '                      sscale(smul(bg["s2"], f["Uf"]), delta), sscale(hx, delta/2),\n'
        '                      sscale(f["Uf"], 9*delta*(2-delta)),\n'
        '                      sscale(smul(g_series, f["Uf"]), 3*(2-delta)))\n'
        '            r2 = sadd(sdx(f["Uf"]), sscale(smul(sadd(bg["q"], {0: 2.0}), f["Uf"]), -1),\n'
        '                      sscale(f["df"], -1/delta),\n'
        '                      sscale(smul(g_series, f["Uf"]), -2/delta))',
    ),
    (
        "fractional_signature",
        '    def solve_fractional(mode, mu, standard, fuel, f_min, f_max):',
        '    def solve_fractional(mode, mu, standard, fuel, f_min, f_max, local_g2):',
    ),
    (
        "transfer_background",
        '        D = ({0: 1.0, 1: mu}, {0: 1.0})\n'
        '        invD = pinv(D)\n'
        '        Dx = pdx(D)\n'
        '        q = padd(({0: -1.0}, {}), pscale(pmul(Dx, invD), 0.5))\n'
        '        s2 = pmul(({2: 1.0}, {}), invD)\n'
        '        Og, On = pscale(invD, rg), pscale(invD, rn)\n'
        '        Ob = pmul(({1: fb*mu}, {}), invD)\n'
        '        Oc = pmul(({1: fc*mu}, {}), invD)\n'
        '        Of = pmul(({}, {0: 1.0}), invD)\n',
        '        fuel_numerator = ({}, {0: 1.0, 2: -local_g2/2})\n'
        '        ash_numerator = ({}, {2: local_g2/(p+1)})\n'
        '        D = ({0: 1.0, 1: mu},\n'
        '             {0: 1.0, 2: local_g2*(1/(p+1)-0.5)})\n'
        '        invD = pinv(D)\n'
        '        Dx = pdx(D)\n'
        '        q = padd(({0: -1.0}, {}), pscale(pmul(Dx, invD), 0.5))\n'
        '        s2 = pmul(({2: 1.0}, {}), invD)\n'
        '        Og, On = pscale(invD, rg), pscale(invD, rn)\n'
        '        Ob = pmul(({1: fb*mu}, {}), invD)\n'
        '        Oc = pmul(padd(({1: fc*mu}, {}), ash_numerator), invD)\n'
        '        Of = pmul(fuel_numerator, invD)\n'
        '        gr_coefficient = (local_g2/(fc*mu)\n'
        '                          if local_g2 != 0.0 and mu != 0.0 else 0.0)\n'
        '        gr = ({}, {1: gr_coefficient})\n',
    ),
    (
        "fuel_pressure_transfer",
        '        fuel_pf = (sadd(fuel["df"], sscale(fuel["Uf"], 3*delta*(2-delta))), {})',
        '        fuel_pf = (sadd(fuel["df"], sscale(fuel["Uf"], 3*delta*(2-delta)),\n'
        '                              sscale(smul({2: local_g2}, fuel["Uf"]), 2-delta)), {})',
    ),
    (
        "fractional_hierarchy_rows",
        '                "nu_shear": padd(pscale(pdx(v["sig"]), 2), pscale(hx, -4/15),\n'
        '                                  pscale(etax, -8/5), pscale(pmul(s2, v["Un"]), -8/15)),\n'
        '                "nu_Euler": padd(pdx(v["Un"]), pscale(pmul(q, v["Un"]), -1),\n'
        '                                  pscale(v["dn"], -0.25), v["sig"]),',
        '                "nu_shear": padd(pscale(pdx(v["sig"]), 2), pscale(hx, -4/15),\n'
        '                                  pscale(etax, -8/5), pscale(pmul(s2, v["Un"]), -8/15),\n'
        '                                  pscale(v["L3"], 3/5)),\n'
        '                "nu_Euler": padd(pdx(v["Un"]), pscale(pmul(q, v["Un"]), -1),\n'
        '                                  pscale(v["dn"], -0.25), v["sig"]),\n'
        '                "nu_l3": padd(pdx(v["L3"]), pmul(q, v["L3"]),\n'
        '                                pscale(pmul(s2, v["sig"]), -6/7),\n'
        '                                pscale(v["L4"], 4/7)),\n'
        '                "nu_l4": padd(pdx(v["L4"]), pscale(pmul(q, v["L4"]), 2),\n'
        '                                pscale(pmul(s2, v["L3"]), -4/9)),',
    ),
    (
        "cdm_transfer_row",
        '                "cdm_continuity": padd(pdx(v["dc"]), pscale(hx, 0.5)),',
        '                "cdm_continuity": padd(pdx(v["dc"]), pscale(hx, 0.5),\n'
        '                                          pscale(pmul(gr, padd(fuel_df, pscale(v["dc"], -1))), -1)),',
    ),
    (
        "layer_hierarchy_output",
        '                              "U_fs": frac["Un"][j], "sigma_fs": frac["sig"][j]}',
        '                              "U_fs": frac["Un"][j], "sigma_fs": frac["sig"][j],\n'
        '                              "L3_fs": frac["L3"][j], "L4_fs": frac["L4"][j]}',
    ),
    (
        "component_ledger",
        '        return {"rank": int(rank), "unknowns": count,\n'
        '                "condition": float(singular[0]/singular[-1]),',
        '        solved_v = variables(solution)\n'
        '        component_pairs = {\n'
        '            "cdm_density": pmul(Oc, solved_v["dc"]),\n'
        '            "fuel_density": pmul(Of, fuel_df),\n'
        '            "fuel_pressure": pmul(Of, fuel_pf),\n'
        '            "fuel_momentum": pmul(Of, fuel_uf),\n'
        '        }\n'
        '        component_layers = {name: {str(j): float(pair[1].get(j, 0.0))\n'
        '                                   for j in frac_exponents}\n'
        '                            for name, pair in component_pairs.items()}\n'
        '        return {"rank": int(rank), "unknowns": count,\n'
        '                "condition": float(singular[0]/singular[-1]),',
    ),
    (
        "component_return",
        '                "layers": layers, "raw": frac, "matrix_shape": list(matrix.shape)}',
        '                "layers": layers, "raw": frac,\n'
        '                "component_layers": component_layers,\n'
        '                "matrix_shape": list(matrix.shape)}',
    ),
    (
        "fuel_physical_call",
        '        fuel, fuel_meta = solve_fuel(std, bg)',
        '        fuel, fuel_meta = solve_fuel(std, bg, transfer_g2)',
    ),
    (
        "extended_solves",
        '        physical = solve_fractional(mode, physical_mu, std, fuel, fmin, n)\n'
        '        std0, bg0, _ = solve_standard(mode, 0.0); fuel0, _ = solve_fuel(std0, bg0)\n'
        '        zero_matter = solve_fractional(mode, 0.0, std0, fuel0, fmin, n)',
        '        physical = solve_fractional(mode, physical_mu, std, fuel, fmin, n+2, transfer_g2)\n'
        '        fuel_no_transfer, _ = solve_fuel(std, bg, 0.0)\n'
        '        no_transfer = solve_fractional(mode, physical_mu, std, fuel_no_transfer,\n'
        '                                       fmin, n+2, 0.0)\n'
        '        std0, bg0, _ = solve_standard(mode, 0.0)\n'
        '        fuel0, _ = solve_fuel(std0, bg0, 0.0)\n'
        '        zero_matter = solve_fractional(mode, 0.0, std0, fuel0, fmin, n+2, 0.0)',
    ),
    (
        "late_checks_before_common",
        '        common = physical["layers"][str(n)]\n'
        '        checks[f"{mode}_common_layer_finite"] = all(np.isfinite(v) for v in common.values())',
        '        common = physical["layers"][str(n)]\n'
        '        checks[f"{mode}_common_layer_finite"] = all(np.isfinite(v) for v in common.values())\n'
        '        checks[f"{mode}_no_transfer_full_rank"] = no_transfer["rank"] == no_transfer["unknowns"]\n'
        '        checks[f"{mode}_no_transfer_scaled_residual_below_1e-11"] = no_transfer["scaled_residual"] < 1e-11\n'
        '        late_l3_j, ash_gravity_j = n+1, n+2\n'
        '        l3_feedback = (3/5)*no_transfer["layers"][str(late_l3_j)]["L3_fs"]\n'
        '        checks[f"{mode}_first_l3_feedback_nonzero"] = abs(l3_feedback) > 1e-12\n'
        '        checks[f"{mode}_L4_feedback_beyond_scope"] = max(\n'
        '            abs(no_transfer["layers"][str(j)]["L4_fs"])\n'
        '            for j in range(fmin, ash_gravity_j+1)) < 1e-10\n'
        '        ash_dc_delta = (physical["layers"][str(late_l3_j)]["delta_c"]\n'
        '                        - no_transfer["layers"][str(late_l3_j)]["delta_c"])\n'
        '        earlier_ash_dc = max(abs(physical["layers"][str(j)]["delta_c"]\n'
        '                                 - no_transfer["layers"][str(j)]["delta_c"])\n'
        '                             for j in range(fmin, late_l3_j))\n'
        '        checks[f"{mode}_ash_delta_c_first_at_n_plus_1"] = (\n'
        '            abs(ash_dc_delta) > 1e-14 and earlier_ash_dc < 1e-12)\n'
        '        cdm_stress_delta = (\n'
        '            physical["component_layers"]["cdm_density"][str(ash_gravity_j)]\n'
        '            - no_transfer["component_layers"]["cdm_density"][str(ash_gravity_j)])\n'
        '        earlier_cdm_stress = max(abs(\n'
        '            physical["component_layers"]["cdm_density"][str(j)]\n'
        '            - no_transfer["component_layers"]["cdm_density"][str(j)])\n'
        '            for j in range(fmin, ash_gravity_j))\n'
        '        checks[f"{mode}_ash_cdm_stress_first_at_n_plus_2"] = (\n'
        '            abs(cdm_stress_delta) > 1e-15 and earlier_cdm_stress < 1e-12)\n'
        '        reference_common = {\n'
        '            "NID": {"h_x":-0.001081563541813167,"eta":-0.0003115955487512795,\n'
        '                    "delta_gamma":0.00637333421224085,"delta_fs":-0.007952772734348947,\n'
        '                    "U_gamma":-0.0002540108506643697,"U_fs":0.0007096736673529544,\n'
        '                    "sigma_fs":0.0013412781078687892},\n'
        '            "NIV": {"h_x":-0.00728218539635547,"eta":-0.0020552001854648562,\n'
        '                    "delta_gamma":0.01673435502524719,"delta_fs":-0.019315658907765074,\n'
        '                    "U_gamma":-0.004732416468329659,"U_fs":0.008919815134812914,\n'
        '                    "sigma_fs":0.0022189716331811457},\n'
        '        }\n'
        '        common_no_transfer = no_transfer["layers"][str(n)]\n'
        '        common_reproduction_error = max(\n'
        '            abs(common_no_transfer[key]-value)\n'
        '            for key,value in reference_common[mode].items())\n'
        '        checks[f"{mode}_lambda_zero_reproduces_script124_common"] = common_reproduction_error < 2e-10',
    ),
    (
        "result_diagnostics",
        '                         "missing_layer_max_norm_zero_matter":zero_missing_norm}',
        '                         "missing_layer_max_norm_zero_matter":zero_missing_norm,\n'
        '                         "BR3B2g_diagnostics":{\n'
        '                            "first_l3_feedback_j":late_l3_j,\n'
        '                            "first_l3_feedback":l3_feedback,\n'
        '                            "ash_delta_c_j":late_l3_j,\n'
        '                            "ash_delta_c_difference":ash_dc_delta,\n'
        '                            "earlier_ash_delta_c_max":earlier_ash_dc,\n'
        '                            "ash_gravity_j":ash_gravity_j,\n'
        '                            "ash_cdm_density_stress_difference":cdm_stress_delta,\n'
        '                            "earlier_cdm_stress_difference_max":earlier_cdm_stress,\n'
        '                            "lambda_zero_common_max_error":common_reproduction_error,\n'
        '                            "no_transfer_rank":no_transfer["rank"],\n'
        '                            "no_transfer_unknowns":no_transfer["unknowns"],\n'
        '                            "no_transfer_scaled_residual":no_transfer["scaled_residual"]}}',
    ),
    (
        "output_identity",
        '"test":"A2-K4.3b-RG-BR3B-2f-5 full mixed Puiseux chain"',
        '"test":"A2-K4.3b-RG-BR3B-2g l3 and ash full ledger"',
    ),
    (
        "output_scope",
        '"scope_limit":"fractional l=3 feedback and gravitating ash enter after common fuel and remain BR3B-2g"',
        '"scope_limit":"includes first l=3 feedback, transfer-corrected fuel, ash delta_c and first gravitating ash/CDM sector; F5 and later hierarchy remain beyond this gate"',
    ),
    (
        "output_execution",
        '"execution_verdict":"PASS_FULL_MIXED_CHAIN_THROUGH_COMMON_FUEL" if passed else "REVIEW_FULL_MIXED_CHAIN_UNCLOSED"',
        '"execution_verdict":"PASS_BR3B2G_L3_ASH_FULL_LEDGER" if passed else "REVIEW_BR3B2G_UNCLOSED"',
    ),
    (
        "output_physical",
        '"physical_verdict":"K4 survives BR3B-2f-5" if passed else "no death verdict; audit first failed row"',
        '"physical_verdict":"K4 survives BR3B-2g" if passed else "no death verdict; audit first failed row"',
    ),
    (
        "output_gate",
        '"K4_3b_RG_verdict":"NEUZAVRETA_BR3B2G_L3_AND_ASH_THEN_BR3C" if passed else "NEUZAVRETA_BR3B2F5"',
        '"K4_3b_RG_verdict":"NEUZAVRETA_BR3C_TWO_DEPTH_EVOLUTION" if passed else "NEUZAVRETA_BR3B2G"',
    ),
    (
        "output_next",
        '"next_step":"if PASS add first later fractional l=3 feedback and ash-gravity ledger, then BR3C two-depth residual evolution"',
        '"next_step":"if PASS run BR3C evolution from two early depths with all four Einstein residuals and step/tolerance convergence"',
    ),
]

for label, old, new in replacements:
    text = replace_once(text, old, new, label)

code = compile(text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
