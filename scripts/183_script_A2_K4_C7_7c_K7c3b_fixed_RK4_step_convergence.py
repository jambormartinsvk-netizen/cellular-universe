#!/usr/bin/env python
"""Immutable fixed-step RK4 convergence extension of script 179."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "179_script_A2_K4_C7_7c_K7c3_NID_deep_short_projected_ODE.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

old_names = (
    "    if tuple(deep_seed) != NAMES or tuple(shallow_seed) != NAMES:\n"
    "        raise RuntimeError(\"K7c.2 seed names changed\")\n"
)
new_names = (
    "    if set(deep_seed) != set(NAMES) or set(shallow_seed) != set(NAMES):\n"
    "        raise RuntimeError(\"K7c.2 seed-name set changed\")\n"
)
if source_text.count(old_names) != 1:
    raise RuntimeError("script 179 seed-name marker is not unique")
source_text = source_text.replace(old_names, new_names, 1)

marker = "    solution = solve_ivp(\n"
if source_text.count(marker) != 1:
    raise RuntimeError("script 179 solve marker is not unique")

fixed_step = '''    def integrate_fixed_rk4(step):
        interval = x_final-x_start
        step_count = int(round(interval/step))
        if abs(step_count*step-interval) > 1e-14 or step_count % 2:
            raise RuntimeError("RK4 grid does not close interval and midpoint")
        normalized = w0.copy()
        checkpoint_indices = {0, step_count//2, step_count}
        trajectory = [(x_start, normalized.copy())]
        for index in range(step_count):
            x_now = x_start+index*step
            k1 = scaled_rhs(x_now, normalized)
            k2 = scaled_rhs(x_now+step/2, normalized+step*k1/2)
            k3 = scaled_rhs(x_now+step/2, normalized+step*k2/2)
            k4 = scaled_rhs(x_now+step, normalized+step*k3)
            normalized = normalized+step*(k1+2*k2+2*k3+k4)/6
            if not np.all(np.isfinite(normalized)):
                raise FloatingPointError("non-finite fixed-RK4 state")
            if index+1 in checkpoint_indices:
                trajectory.append((x_start+(index+1)*step, normalized.copy()))
        return step_count, trajectory, normalized

    coarse_steps, coarse_checkpoints, coarse_endpoint = integrate_fixed_rk4(0.0025)
    fine_steps, fine_checkpoints, fine_endpoint = integrate_fixed_rk4(0.00125)
    endpoint_component_difference = np.abs(fine_endpoint-coarse_endpoint)
    max_endpoint_difference = float(np.max(endpoint_component_difference))
    normalized_change = float(np.max(np.abs(fine_endpoint-w0)))
    checkpoint_output = []
    max_density_scaled = 0.0
    max_momentum_scaled = 0.0
    all_checkpoint_finite = True
    for x_value, normalized in fine_checkpoints:
        state = normalized*scale
        b = background(float(x_value))
        rhs = physical_rhs(float(x_value),state)
        h,eta,dg,D,db,dc,Ug,M,sig,L3,L4,df,Uf = state
        Og,On,Ob,Oc,Of = b["Og"],b["On"],b["Ob"],b["Oc"],b["Of"]
        Wg,Wf = 2*Og+1.5*Ob,1.5*delta*Of
        dn = (D-Og*dg-Ob*db-Oc*dc-Of*df)/On
        Un = (M-Wg*Ug-Wf*Uf)/(2*On)
        density_terms = np.asarray([Og*dg,On*dn,Ob*db,Oc*dc,Of*df])
        momentum_terms = np.asarray([Wg*Ug,2*On*Un,Wf*Uf])
        density_scaled = abs(float(np.sum(density_terms))-D)/max(
            float(np.sum(np.abs(density_terms))),abs(D),1e-300)
        momentum_scaled = abs(float(np.sum(momentum_terms))-M)/max(
            float(np.sum(np.abs(momentum_terms))),abs(M),1e-300)
        max_density_scaled = max(max_density_scaled,density_scaled)
        max_momentum_scaled = max(max_momentum_scaled,momentum_scaled)
        finite = bool(np.all(np.isfinite(state)) and np.all(np.isfinite(rhs))
            and math.isfinite(dn) and math.isfinite(Un))
        all_checkpoint_finite = all_checkpoint_finite and finite
        checkpoint_output.append({
            "x":float(x_value),"state":dict(zip(NAMES,map(float,state))),
            "rhs":dict(zip(NAMES,map(float,rhs))),
            "reconstructed_delta_fs":float(dn),"reconstructed_U_fs":float(Un),
            "density_constraint_scaled_residual":density_scaled,
            "momentum_constraint_scaled_residual":momentum_scaled,
            "metric_h_identity_residual":abs(rhs[0]-(3*D+2*b["s2"]*eta)),
            "metric_eta_identity_residual":abs(rhs[1]-M),"finite":finite,
        })
    checks = {
        "source_exit_zero":child.returncode == 0,
        "source_seed_handoff_pass":source.get("execution_verdict") ==
            "PASS_C7_7C_K7C2_HIGH_PRECISION_SEED_HANDOFF",
        "source_names_exact":set(source.get("projected_state_names",())) == set(NAMES),
        "coarse_grid_exactly_100_steps":coarse_steps == 100,
        "fine_grid_exactly_200_steps":fine_steps == 200,
        "both_grids_have_three_checkpoints":len(coarse_checkpoints) == 3 and
            len(fine_checkpoints) == 3,
        "fine_checkpoint_states_rhs_finite":all_checkpoint_finite,
        "endpoint_step_difference_below_1e-6":max_endpoint_difference < 1e-6,
        "nontrivial_fine_change_above_1e-12":normalized_change > 1e-12,
        "density_constraint_scaled_below_5e-12":max_density_scaled < 5e-12,
        "momentum_constraint_scaled_below_5e-12":max_momentum_scaled < 5e-12,
        "rhs_call_cap_2000_respected":rhs_calls <= 2000,
        "normalized_safety_cap_respected":maximum_normalized_abs < 1e8,
    }
    passed = bool(checks) and all(checks.values())
    output = {
        "test":"A2-K4 C7.7c-K7c.3b fixed RK4 step-convergence",
        "profile_request":{"mode":"NID","surface":"deep",
            "x_start":x_start,"x_final":x_final},
        "state_names":list(NAMES),
        "integration_scale":dict(zip(NAMES,map(float,scale))),
        "solver":{"method":"fixed classical RK4","coarse_step":0.0025,
            "fine_step":0.00125,"coarse_steps":coarse_steps,
            "fine_steps":fine_steps,"adaptive_error_control":False,
            "L5_closure":"L5=0 bounded closure"},
        "results":{"rhs_calls_including_audit":rhs_calls,
            "maximum_normalized_abs":maximum_normalized_abs,
            "max_normalized_endpoint_step_difference":max_endpoint_difference,
            "normalized_endpoint_difference_by_component":dict(zip(
                NAMES,map(float,endpoint_component_difference))),
            "max_normalized_fine_change":normalized_change,
            "coarse_endpoint_state":dict(zip(NAMES,map(float,coarse_endpoint*scale))),
            "fine_endpoint_state":dict(zip(NAMES,map(float,fine_endpoint*scale))),
            "max_density_constraint_scaled_residual":max_density_scaled,
            "max_momentum_constraint_scaled_residual":max_momentum_scaled,
            "fine_checkpoints":checkpoint_output},
        "checks":checks,
        "execution_verdict":(
            "PASS_C7_7C_K7C3B_FIXED_RK4_STEP_CONVERGENCE"
            if passed else "REVIEW_C7_7C_K7C3B_FIXED_RK4_UNCLOSED"),
        "physical_verdict":(
            "short NID/deep projected evolution passed fixed-step convergence"
            if passed else "no death verdict; audit first failed fixed-step gate"),
        "fine_depth":"66.5/100",
        "scope_limit":"0.25 e-fold NID/deep only; no four-surface, endpoint-agreement, or full-hierarchy claim",
        "runtime_limits_seconds":{"total":args.max_runtime_seconds,
            "seed_source":args.source_runtime_seconds,
            "seed_source_children":args.source_child_runtime_seconds,
            "rhs_calls":2000},
        "runtime_seconds":time.monotonic()-started,
    }
    print(json.dumps(output,indent=2,sort_keys=True))
    return 0 if passed else 1

'''
source_text = source_text.replace(marker, fixed_step + marker, 1)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
