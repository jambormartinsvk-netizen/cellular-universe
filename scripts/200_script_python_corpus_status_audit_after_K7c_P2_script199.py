#!/usr/bin/env python
"""Bounded, non-executing audit of the Python script corpus.

The target scripts are read and compiled as source text only.  They are never
imported or launched.  The quarantine is keyed by full filename because script
numbers are not unique in this repository.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent
SELF = Path(__file__).name
EXPECTED_CORPUS_EXCLUDING_SELF = 204
EXPECTED_SYNTAX_FAILURE_PREFIXES = {"118_", "119_"}


def item(status: str, reason: str, successor: str = "none") -> dict[str, str]:
    return {"status": status, "reason": reason, "successor": successor}


QUARANTINE: dict[str, dict[str, str]] = {
    "28_script_A2_K4_full_superhorizon_relative_mode.py": item(
        "DO_NOT_RUN_TECHNICAL", "numpy.bool_ JSON failure after integration", "29_script_A2_K4_full_superhorizon_relative_mode_serialized.py"),
    "29_script_A2_K4_full_superhorizon_relative_mode_serialized.py": item(
        "RUNNABLE_REVIEW_ONLY", "serialization fixed, but convergence and pointwise constraint gates failed", "later K4.1/K4.2 chain"),
    "43_script_A2_K5_1_delta_zero_singular_limit.py": item(
        "DO_NOT_RUN_TECHNICAL", "AttributeError from a non-exported helper", "44_script_A2_K5_1_delta_zero_singular_limit_fixed.py"),
    "45_script_A2_K11_S8_K1b_superhorizon_instability_test.py": item(
        "DO_NOT_USE_PHYSICS", "printed PASS rejected: wrong/incomplete equations and failed Einstein constraint", "new covariant K11 operator required"),
    "46_script_A2_K11_S8_K1b_rigorous_amplitude_scaling_test.py": item(
        "DO_NOT_USE_PHYSICS", "inherits the non-authoritative K11 equation system", "new covariant K11 operator required"),
    "47_script_A2_K11_S8_K1b_fully_consistent_einstein_test.py": item(
        "DO_NOT_USE_PHYSICS", "later audit rejects its physical/constraint interpretation", "68_script_A2_K11_script47_physics_and_constraint_audit.py"),
    "51_script_A2_K11_script45_equation_and_sign_audit.py": item(
        "DO_NOT_RUN_TECHNICAL", "historical long/overflowing anti-damping branch; partial results preserved", "52_script_A2_K11_script45_recoverable_runs.py"),
    "52_script_A2_K11_script45_recoverable_runs.py": item(
        "RUNNABLE_REVIEW_ONLY", "recoverable branches only; no converged or constraint-valid physical PASS", "54_script_A2_K11_script45_constraint_and_scaling_audit.py"),
    "53_script_A2_K11_solver_floor_and_amplitude_scaling.py": item(
        "RUNNABLE_REVIEW_ONLY", "documented numerical-resolution failure", "54_script_A2_K11_script45_constraint_and_scaling_audit.py"),
    "54_script_A2_K11_script45_constraint_and_scaling_audit.py": item(
        "RUNNABLE_REVIEW_ONLY", "audit diagnostic; current K11 requires a new operator before evolution", "none"),
    "61_script_A2_K7_K3_1_K2_2_K1b_spin2_coupling_scale_gate_PRE_ERRATUM_OVERBROAD.py": item(
        "DO_NOT_USE_PHYSICS", "pre-erratum overbroad spin-2 conclusion", "61_script_A2_K7_K3_1_K2_2_K1b_spin2_coupling_scale_gate.py"),
    "75_script_A2_K4_3b_exact_CAMB_hierarchy_coefficient_crosscheck.py": item(
        "SUPERSEDED", "J2/G2 alias mapping was not converted", "76_script_A2_K4_3b_exact_CAMB_hierarchy_coefficients_alias_fixed.py"),
    "78_script_A2_K4_3b_RG_collective_CAMB_regular_seed_active_start_fixed.py": item(
        "ENVIRONMENT_BLOCKED", "symbolic pi_r path requires unavailable Fortran compiler", "79_script_A2_K4_3b_RG_collective_CAMB_regular_seed_precompiled_only.py"),
    "89_script_A2_K4_3b_RG_BR2_backreacted_superhorizon_evolution.py": item(
        "RUNNABLE_REVIEW_ONLY", "raw eta second derivative is ill-conditioned in deep radiation era", "90/92/94 conditioned chain"),
    "90_script_A2_K4_3b_RG_BR2_conditioned_DAE_constraint_audit.py": item(
        "RUNNABLE_REVIEW_ONLY", "species variables remained cancellation-prone", "92/94 conditioned chain"),
    "91_script_A2_K4_3b_RG_BR2_Omega_conditioned_DAE.py": item(
        "DO_NOT_RUN_TECHNICAL", "numpy.bool_ JSON serialization failure", "92_script_A2_K4_3b_RG_BR2_Omega_conditioned_DAE_json_fixed_alias.py"),
    "92_script_A2_K4_3b_RG_BR2_Omega_conditioned_DAE_json_fixed_alias.py": item(
        "RUNNABLE_REVIEW_ONLY", "density passed but two velocity modes remained above fixed tolerance", "94_script_A2_K4_3b_RG_BR2_velocity_roundoff_condition_gate_json_alias.py"),
    "93_script_A2_K4_3b_RG_BR2_velocity_roundoff_condition_gate.py": item(
        "DO_NOT_RUN_TECHNICAL", "numpy.bool_ JSON serialization failure", "94_script_A2_K4_3b_RG_BR2_velocity_roundoff_condition_gate_json_alias.py"),
    "101_script_A2_K4_3b_RG_BR3B2d_NID_NIV_power_ordering.py": item(
        "DO_NOT_RUN_TECHNICAL", "SymPy BooleanTrue JSON serialization failure", "102_script_A2_K4_3b_RG_BR3B2d_NID_NIV_power_ordering_fixed.py"),
    "105_script_A2_K4_3b_RG_BR3B2e2_NIV_shear_CAMB_constraint_crosscheck.py": item(
        "ENVIRONMENT_BLOCKED", "symbolic CAMB output requires unavailable Fortran compiler", "106_script_A2_K4_3b_RG_BR3B2e2_NIV_shear_CAMB_precompiled_crosscheck.py"),
    "107_script_A2_K4_3b_RG_BR3B2e2_NID_NIV_shear_sector_solution.py": item(
        "SUPERSEDED", "exact linsolve repeatedly exceeded the bounded runtime", "108_script_A2_K4_3b_RG_BR3B2e2_NID_NIV_shear_sector_solution_bounded.py"),
    "110_script_A2_K4_3b_RG_BR3B2f_CAMB_mode_coefficients_in_a.py": item(
        "RUNNABLE_REVIEW_ONLY", "NID/NIV regression unstable for high coefficients", "115/116/124 chain"),
    "111_script_A2_K4_3b_RG_BR3B2f2_NID_NIV_baryon_fraction_difference.py": item(
        "RUNNABLE_REVIEW_ONLY", "time-window dependence remained", "115/116/124 chain"),
    "112_script_A2_K4_3b_RG_BR3B2f3_exact_Frobenius_standard_NID_NIV.py": item(
        "SUPERSEDED", "symbolic series exceeded external timeout", "115_script_A2_K4_3b_RG_BR3B2f3_Frobenius_null_direction_audit_fixed.py"),
    "113_script_A2_K4_3b_RG_BR3B2f3_Frobenius_bounded_coefficients.py": item(
        "RUNNABLE_REVIEW_ONLY", "leading coefficients passed but full-rank/k-independence gates were not valid", "115/116 chain"),
    "114_script_A2_K4_3b_RG_BR3B2f3_Frobenius_null_direction_audit.py": item(
        "DO_NOT_RUN_TECHNICAL", "unexecuted duplicate after patch-helper failure", "115_script_A2_K4_3b_RG_BR3B2f3_Frobenius_null_direction_audit_fixed.py"),
    "118_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py": item(
        "DO_NOT_RUN_TECHNICAL", "preserved SyntaxError: missing parenthesis in solve_fuel", "124_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain_audited.py"),
    "119_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py": item(
        "DO_NOT_RUN_TECHNICAL", "preserved SyntaxError: outer list still unclosed", "124_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain_audited.py"),
    "120_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py": item(
        "DO_NOT_RUN_TECHNICAL", "numpy.bool_ JSON serialization failure after equations", "121/124 corrected chain"),
    "121_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py": item(
        "RUNNABLE_REVIEW_ONLY", "legacy shear oracle was wrong; result localized but not authoritative", "124_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain_audited.py"),
    "126_script_A2_K4_3b_RG_BR3B2g_l3_ash_full_ledger.py": item(
        "RUNNABLE_REVIEW_ONLY", "homogeneous L3/L4 modes contaminated early coefficients", "127_script_A2_K4_3b_RG_BR3B2g_l3_ash_regular_hierarchy.py"),
    "131_script_A2_K4_3b_RG_BR3C_a_order5_order6_state_audit.py": item(
        "RUNNABLE_REVIEW_ONLY", "division of round-off zero slots made F3/F4 unstable", "132/134 chain"),
    "133_script_A2_K4_3b_RG_BR3C_a_projected_order_audit.py": item(
        "DO_NOT_RUN_TECHNICAL", "source-verdict marker had two matches", "134_script_A2_K4_3b_RG_BR3C_a_projected_order_audit_fixed.py"),
    "140_script_A2_K4_3b_RG_BR3C_c_species_mode_activity_audit.py": item(
        "SUPERSEDED", "key handling corrected by explicit fixed-keys successor", "141_script_A2_K4_3b_RG_BR3C_c_species_mode_activity_audit_fixed_keys.py"),
    "142_script_A2_K4_3b_RG_C7_7c_K2_normalized_component_evolution.py": item(
        "SUPERSEDED", "normalized DOP853 numerical subtrack timed out", "K7 projected-basis chain"),
    "143_script_A2_K4_3b_RG_C7_7c_K2_normalized_activity_audit.py": item(
        "SUPERSEDED", "audit wrapper of timed-out K2 subtrack", "K7 projected-basis chain"),
    "144_script_A2_K4_3b_RG_C7_7c_K3_normalized_Radau_evolution.py": item(
        "SUPERSEDED", "Radau subtrack timed out/failed on scaling", "K7 projected-basis chain"),
    "145_script_A2_K4_3b_RG_C7_7c_K3_normalized_Radau_activity_audit.py": item(
        "SUPERSEDED", "audit wrapper of dead K3 numerical subtrack", "K7 projected-basis chain"),
    "147_script_A2_K4_3b_RG_C7_7c_K4_analytic_envelope_evolution.py": item(
        "SUPERSEDED", "analytic-envelope evolution hit internal deadline", "K7 projected-basis chain"),
    "148_script_A2_K4_3b_RG_C7_7c_K4_analytic_envelope_activity_audit.py": item(
        "SUPERSEDED", "activity gate unclosed because child timed out", "K7 projected-basis chain"),
    "150_script_A2_K4_C7_7c_segment_profiler.py": item(
        "RUNNABLE_REVIEW_ONLY", "historical profiler only; no physical or score verdict", "later K7 diagnostics"),
    "151_script_A2_K4_C7_7c_initial_scaled_jacobian_profile.py": item(
        "RUNNABLE_REVIEW_ONLY", "envelope-coordinate Jacobian diagnostic can be scale-dominated", "157/158 and K7a chain"),
    "152_script_A2_K4_C7_7c_matrix_balance_diagnostic.py": item(
        "RUNNABLE_REVIEW_ONLY", "SVD/condition diagnostics depend on envelope scaling", "157/158 and K7a chain"),
    "153_script_A2_K4_C7_7c_K5_balanced_segment_evolution.py": item(
        "SUPERSEDED", "balanced numerical subtrack timed out and changed error metric", "K7 projected-basis chain"),
    "154_script_A2_K4_C7_7c_K6_vector_atol_segment_evolution.py": item(
        "SUPERSEDED", "vector-atol subtrack demanded precision below float64 arithmetic floor", "K7 projected-basis chain"),
    "159_script_A2_K4_C7_7c_K7a_projected_jacobian_audit.py": item(
        "RUNNABLE_REVIEW_ONLY", "double finite-difference T-prime cancellation", "161/162/164 safe chain"),
    "160_script_A2_K4_C7_7c_K7a_J2_high_precision_Tprime_audit.py": item(
        "RUNNABLE_REVIEW_ONLY", "central-difference cancellation remained at high precision", "161_script_A2_K4_C7_7c_K7a_J3_cancellation_safe_Tprime_audit.py"),
    "163_script_A2_K4_C7_7c_K7a_J4_composite_projected_jacobian_gate.py": item(
        "DO_NOT_RUN_TECHNICAL", "composite parser used the wrong nested JSON path", "164_script_A2_K4_C7_7c_K7a_J4b_composite_parser_corrected_gate.py"),
    "168_script_A2_K4_C7_7c_K7b3a_high_precision_standard_coefficient_export.py": item(
        "DO_NOT_USE_PHYSICS", "soft least-squares moved exact physical anchors", "174/175 hard-constrained chain"),
    "169_script_A2_K4_C7_7c_K7b3a_high_precision_standard_constraint_gate.py": item(
        "DO_NOT_USE_PHYSICS", "gate of dead soft-constraint formulation", "174/175 hard-constrained chain"),
    "170_script_A2_K4_C7_7c_K7b3b_hard_constrained_standard_export.py": item(
        "DO_NOT_RUN_TECHNICAL", "unsupported mpmath matrix[:, list] slice", "174_script_A2_K4_C7_7c_K7b3b1_slice_and_physical_mu_export.py"),
    "171_script_A2_K4_C7_7c_K7b3b_hard_constrained_slice_corrected_export.py": item(
        "SUPERSEDED", "later mu=0 solve overwrote the physical HP registry", "174_script_A2_K4_C7_7c_K7b3b1_slice_and_physical_mu_export.py"),
    "172_script_A2_K4_C7_7c_K7b3b_hard_constrained_constraint_gate.py": item(
        "DO_NOT_USE_PHYSICS", "compared physical-mu float state with mu=0 HP registry and contains fail-open rank check", "new fail-closed successor of 175/176"),
    "173_script_A2_K4_C7_7c_K7b3b1_physical_mu_registry_export.py": item(
        "DO_NOT_RUN_TECHNICAL", "patch searched the capture marker in the wrong transformation layer", "174_script_A2_K4_C7_7c_K7b3b1_slice_and_physical_mu_export.py"),
    "179_script_A2_K4_C7_7c_K7c3_NID_deep_short_projected_ODE.py": item(
        "DO_NOT_RUN_TECHNICAL", "assumed JSON dict order equals registered state order", "180_script_A2_K4_C7_7c_K7c3_NID_deep_JSON_order_corrected_ODE.py"),
    "180_script_A2_K4_C7_7c_K7c3_NID_deep_JSON_order_corrected_ODE.py": item(
        "SUPERSEDED", "adaptive ODE hit the 200000 RHS cap", "184/185 fixed-RK4 review chain"),
    "181_script_A2_K4_C7_7c_K7c3a_exact_linear_operator_profile.py": item(
        "DO_NOT_RUN_TECHNICAL", "unit physical basis triggered normalized safety cap", "182_script_A2_K4_C7_7c_K7c3a1_normalized_basis_operator_profile.py"),
    "182_script_A2_K4_C7_7c_K7c3a1_normalized_basis_operator_profile.py": item(
        "RUNNABLE_REVIEW_ONLY", "zero-integration diagnostic; reconstruction gate remained REVIEW", "clean standalone K7c successor"),
    "183_script_A2_K4_C7_7c_K7c3b_fixed_RK4_step_convergence.py": item(
        "DO_NOT_RUN_TECHNICAL", "NumPy bool JSON failure; also leaves unreachable legacy solver", "184_script_A2_K4_C7_7c_K7c3b_fixed_RK4_JSON_bool_corrected.py"),
    "184_script_A2_K4_C7_7c_K7c3b_fixed_RK4_JSON_bool_corrected.py": item(
        "RUNNABLE_REVIEW_ONLY", "endpoint difference 1.443e-6 exceeded preregistered 1e-6", "clean standalone K7c successor"),
    "185_script_A2_K4_C7_7c_K7c3c_second_fixed_RK4_refinement.py": item(
        "RUNNABLE_REVIEW_ONLY", "non-asymptotic M refinement ratio 0.367", "new M-prime term ledger"),
    "186_script_A2_K4_C7_7c_K7c3d_M_rhs_term_ledger.py": item(
        "DO_NOT_RUN_TECHNICAL", "incomplete file ending at __K7C3D_CONTINUE__", "new numbered M-prime ledger"),
}


QUARANTINE["188_script_python_corpus_status_and_known_error_audit.py"] = item(
    "SUPERSEDED", "immutable 192-target snapshot", "198_script_python_corpus_status_audit_after_K7c_P1_clean_RK4.py"
)
QUARANTINE["189_script_A2_K4_C7_7c_K7b3b2_fail_closed_physical_mu_gate.py"] = item(
    "DO_NOT_RUN_TECHNICAL", "PF-012: parser marker patched one wrapper layer too early", "192_script_A2_K4_C7_7c_K7b3b2a_fail_closed_physical_mu_gate.py"
)
QUARANTINE["190_script_A2_K4_C7_7c_K7b_P0_fail_closed_regression_gate.py"] = item(
    "DO_NOT_RUN_TECHNICAL", "depends on technically dead script 189", "195_script_A2_K4_C7_7c_K7b_P0_segmented_offline_aggregate.py"
)
QUARANTINE["191_script_python_corpus_status_audit_after_K7b_P0.py"] = item(
    "SUPERSEDED", "intermediate 195-target snapshot", "198_script_python_corpus_status_audit_after_K7c_P1_clean_RK4.py"
)
QUARANTINE["193_script_A2_K4_C7_7c_K7b_P0a_PF012_corrected_regression_gate.py"] = item(
    "SUPERSEDED", "monolithic aggregate hit its preregistered internal timeout", "195_script_A2_K4_C7_7c_K7b_P0_segmented_offline_aggregate.py"
)
QUARANTINE["194_script_python_corpus_status_audit_after_PF012.py"] = item(
    "SUPERSEDED", "intermediate 198-target snapshot", "198_script_python_corpus_status_audit_after_K7c_P1_clean_RK4.py"
)
QUARANTINE["196_script_python_corpus_status_audit_after_K7b_P0_segmented.py"] = item(
    "SUPERSEDED", "immutable 200-target snapshot before clean P1 RK4", "198_script_python_corpus_status_audit_after_K7c_P1_clean_RK4.py"
)

QUARANTINE["198_script_python_corpus_status_audit_after_K7c_P1_clean_RK4.py"] = item(
    "SUPERSEDED", "immutable corpus snapshot before scientific P2 script 199", "200_script_python_corpus_status_audit_after_K7c_P2_script199.py"
)
FAIL_OPEN = re.compile(r"\.get\([^\n]+?\)\s*==\s*[A-Za-z_][A-Za-z0-9_]*\.get\(")


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def has_execution_entry(tree: ast.Module) -> bool:
    for node in tree.body:
        if isinstance(node, ast.If):
            rendered = ast.dump(node.test, include_attributes=False)
            if "__name__" in rendered and "__main__" in rendered:
                return True
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            return True
        if isinstance(node, (ast.For, ast.While, ast.With, ast.Try)):
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=15.0)
    parser.add_argument("--target", type=str)
    args = parser.parse_args()
    if not 5.0 <= args.max_runtime_seconds <= 20.0:
        parser.error("max-runtime-seconds must be in [5,20]")
    started = time.monotonic()

    paths = sorted(path for path in HERE.glob("*.py") if path.name != SELF)
    syntax_errors = []
    no_entry_candidates = []
    pattern_findings = []
    records = {}

    for index, path in enumerate(paths):
        if index % 16 == 0 and time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("script corpus audit deadline exceeded")
        text = path.read_text(encoding="utf-8")
        record = {"sha256": sha256(text), "syntax": "PASS"}
        try:
            tree = ast.parse(text, filename=str(path))
            compile(tree, str(path), "exec")
        except SyntaxError as exc:
            record["syntax"] = "FAIL"
            record["syntax_error"] = f"{exc.msg} at line {exc.lineno}:{exc.offset}"
            syntax_errors.append(path.name)
            records[path.name] = record
            continue
        if not has_execution_entry(tree):
            no_entry_candidates.append(path.name)
        findings = []
        if FAIL_OPEN.search(text):
            findings.append("fail_open_get_equality")
        if "matrix_mp[:,fixed_indices]" in text or "matrix_mp[:, fixed_indices]" in text:
            findings.append("unsupported_mpmath_list_slice")
        if "tuple(deep_seed) != NAMES" in text:
            findings.append("json_key_order_assumption")
        if "__K7C3D_CONTINUE__" in text:
            findings.append("incomplete_continuation_marker")
        if "fixed_step + marker" in text and "return 0 if passed else 1" in text:
            findings.append("generated_unreachable_legacy_solver_risk")
        if ("solve_ivp(" in text or "subprocess.run(" in text) and "max-runtime-seconds" not in text:
            findings.append("long_run_without_internal_runtime_argument")
        if findings:
            record["known_pattern_findings"] = findings
            pattern_findings.append({"file": path.name, "findings": findings})
        records[path.name] = record

    quarantine_output = []
    missing_quarantine_files = []
    for filename, metadata in QUARANTINE.items():
        path = HERE / filename
        if not path.exists():
            missing_quarantine_files.append(filename)
            continue
        row = {"file": filename, **metadata, **records[filename]}
        quarantine_output.append(row)

    syntax_prefixes = {name.split("script", 1)[0] for name in syntax_errors}
    expected_syntax = syntax_prefixes == EXPECTED_SYNTAX_FAILURE_PREFIXES
    checks = {
        "corpus_count_excluding_auditor_is_204": len(paths) == EXPECTED_CORPUS_EXCLUDING_SELF,
        "expected_syntax_failures_only": expected_syntax,
        "all_quarantine_files_exist": not missing_quarantine_files,
        "incomplete_186_detected": any(
            row["file"].startswith("186_") and
            "incomplete_continuation_marker" in row.get("known_pattern_findings", [])
            for row in quarantine_output
        ),
        "no_target_script_executed": True,
    }

    target_result = None
    target_blocked = False
    if args.target:
        filename = Path(args.target).name
        metadata = QUARANTINE.get(filename)
        if metadata is None:
            target_result = {"file": filename, "status": "NOT_IN_QUARANTINE", "routine_run": "requires normal preregistration"}
        else:
            target_blocked = True
            target_result = {"file": filename, **metadata, "routine_run": "BLOCKED"}

    passed = all(checks.values())
    output = {
        "test": "bounded corpus status audit after K7c P2 script 199 creation",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "corpus_count_excluding_auditor": len(paths),
        "syntax_errors": syntax_errors,
        "no_execution_entry_candidates": no_entry_candidates,
        "pattern_findings": pattern_findings,
        "quarantine_count": len(quarantine_output),
        "quarantine": quarantine_output,
        "missing_quarantine_files": missing_quarantine_files,
        "checks": checks,
        "target_result": target_result,
        "execution_verdict": "PASS_SCRIPT_CORPUS_INVENTORY" if passed else "REVIEW_SCRIPT_CORPUS_INVENTORY",
        "scope_limit": "source/AST audit only; no target import, execution, or physical verdict",
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if target_blocked:
        return 2
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
