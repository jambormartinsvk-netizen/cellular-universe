#!/usr/bin/env python
"""Immutable zero-integration diagnostic extension of script 179."""

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
diagnostic = '''    zero_state = np.zeros(13, dtype=float)
    zero_rhs = physical_rhs(x_start, zero_state)
    physical_operator = np.column_stack([
        physical_rhs(x_start, np.eye(13, dtype=float)[:, column])-zero_rhs
        for column in range(13)
    ])
    scaled_operator = (
        physical_operator*scale[np.newaxis, :]/scale[:, np.newaxis]
    )
    initial_physical_rhs = physical_rhs(x_start, y0)
    initial_normalized_rhs = initial_physical_rhs/scale
    reconstructed_rhs = physical_operator@y0+zero_rhs
    rhs_reconstruction_scaled = float(np.max(np.abs(
        reconstructed_rhs-initial_physical_rhs
    ))/max(float(np.max(np.abs(initial_physical_rhs))), 1e-300))
    physical_eigenvalues = np.linalg.eigvals(physical_operator)
    scaled_eigenvalues = np.linalg.eigvals(scaled_operator)
    physical_rho = float(np.max(np.abs(physical_eigenvalues)))
    scaled_rho = float(np.max(np.abs(scaled_eigenvalues)))
    rho_relative_difference = abs(scaled_rho-physical_rho)/max(
        physical_rho, 1e-300
    )
    couplings = []
    for row in range(13):
        for column in range(13):
            couplings.append({
                "row":NAMES[row], "column":NAMES[column],
                "value":float(scaled_operator[row,column]),
                "absolute_value":float(abs(scaled_operator[row,column])),
            })
    couplings.sort(key=lambda item:item["absolute_value"], reverse=True)
    checks = {
        "source_exit_zero":child.returncode == 0,
        "source_seed_handoff_pass":source.get("execution_verdict") ==
            "PASS_C7_7C_K7C2_HIGH_PRECISION_SEED_HANDOFF",
        "source_names_exact":set(source.get("projected_state_names",())) == set(NAMES),
        "zero_rhs_below_1e-14":float(np.max(np.abs(zero_rhs))) < 1e-14,
        "operators_and_rhs_finite":bool(
            np.all(np.isfinite(physical_operator)) and
            np.all(np.isfinite(scaled_operator)) and
            np.all(np.isfinite(initial_normalized_rhs))
        ),
        "rhs_reconstruction_scaled_below_1e-12":rhs_reconstruction_scaled < 1e-12,
        "spectral_radius_similarity_below_1e-10":rho_relative_difference < 1e-10,
        "no_ODE_executed":True,
    }
    passed = bool(checks) and all(checks.values())
    output = {
        "test":"A2-K4 C7.7c-K7c.3a exact linear-operator profile",
        "profile_request":{"mode":"NID","surface":"deep","x":x_start},
        "state_names":list(NAMES),
        "method":"exact basis-column evaluation f(e_j)-f(0); no finite-difference step",
        "integration_scale":dict(zip(NAMES,map(float,scale))),
        "scale_span_max_over_min":float(np.max(scale)/np.min(scale)),
        "initial_state":dict(zip(NAMES,map(float,y0))),
        "initial_physical_rhs":dict(zip(NAMES,map(float,initial_physical_rhs))),
        "initial_normalized_rhs":dict(zip(NAMES,map(float,initial_normalized_rhs))),
        "initial_normalized_rhs_max_abs":float(np.max(np.abs(initial_normalized_rhs))),
        "physical_operator_max_abs":float(np.max(np.abs(physical_operator))),
        "scaled_operator_max_abs":float(np.max(np.abs(scaled_operator))),
        "physical_spectral_radius":physical_rho,
        "scaled_spectral_radius":scaled_rho,
        "spectral_radius_relative_difference":rho_relative_difference,
        "rhs_reconstruction_scaled_residual":rhs_reconstruction_scaled,
        "top_scaled_couplings":couplings[:10],
        "checks":checks,
        "execution_verdict":(
            "PASS_C7_7C_K7C3A_EXACT_LINEAR_OPERATOR_PROFILE"
            if passed else "REVIEW_C7_7C_K7C3A_OPERATOR_PROFILE_UNCLOSED"
        ),
        "physical_verdict":(
            "diagnostic only; classify error-control coordinates before next ODE"
            if passed else "no physical death verdict; audit failed operator check"
        ),
        "fine_depth":"66.5/100",
        "scope_limit":"zero integration; no FD Jacobian, SVD condition proxy, or ODE claim",
        "runtime_limits_seconds":{"total":args.max_runtime_seconds,
            "seed_source":args.source_runtime_seconds,
            "seed_source_children":args.source_child_runtime_seconds},
        "runtime_seconds":time.monotonic()-started,
    }
    print(json.dumps(output,indent=2,sort_keys=True))
    return 0 if passed else 1

'''
source_text = source_text.replace(marker, diagnostic + marker, 1)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
