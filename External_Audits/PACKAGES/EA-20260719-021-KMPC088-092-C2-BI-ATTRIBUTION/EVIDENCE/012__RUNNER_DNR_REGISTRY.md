# Centrálny register Python skriptov, ktoré sa rutinne nespúšťajú

Dátum: 2026-07-15  
Stav: autoritatívny ľudský mirror auditu skriptu 198; staršie checkery ostávajú historické snapshoty

## Povinné použitie

Pred spustením historického Python skriptu sa najprv skontroluje tento register alebo sa vykoná:

```text
C:\Python311\python.exe scripts\198_script_python_corpus_status_audit_after_K7c_P1_clean_RK4.py --max-runtime-seconds 15 --target scripts\NAZOV.py
```

Exit code `2` znamená, že skript je v karanténe. Priamy beh je potom povolený iba ako výslovne predregistrovaná reprodukcia starej chyby. Skripty sa nepremenúvajú ani neupravujú komentárom, aby zostali platné historické odkazy a checksumy.

Výsledok `NOT_IN_QUARANTINE` znamená iba to, že skript nie je v tomto registri. Nie je to certifikácia technickej správnosti, numerickej konvergencie ani fyzikálnej platnosti; tieto brány sa musia auditovať samostatne.

## Výsledok korpusového auditu

- auditovaných cieľových súborov: **202**;
- karanténa: **69**;
- syntaxové chyby: **2** — 118 a 119;
- bez vykonateľného vstupu: **1** — skript 186;
- cieľové skripty spustené auditom: **0**;
- verdict: **PASS_SCRIPT_CORPUS_INVENTORY**.

Tieto počty patria nemennému korpusovému behu checkeru 198. Neskoršie AR8
fyzikálne prekrytia sa uvádzajú v samostatných sekciách nižšie a počty
checkeru 198 spätne nemenia.

### Počty podľa kategórie

| Kategória | Počet | Rutinné spustenie |
|---|---:|---|
| `DO_NOT_RUN_TECHNICAL` | 20 | NIE |
| `DO_NOT_USE_PHYSICS` | 7 | NIE |
| `ENVIRONMENT_BLOCKED` | 2 | NIE |
| `RUNNABLE_REVIEW_ONLY` | 21 | NIE; iba explicitná historická/regresná diagnostika |
| `SUPERSEDED` | 19 | NIE |

## Karanténny register

| Súbor | Stav | Dôvod | Autoritatívny nástupca | SHA-256 |
|---|---|---|---|---|
| `101_script_A2_K4_3b_RG_BR3B2d_NID_NIV_power_ordering.py` | `DO_NOT_RUN_TECHNICAL` | SymPy BooleanTrue JSON serialization failure | `102_script_A2_K4_3b_RG_BR3B2d_NID_NIV_power_ordering_fixed.py` | `95e3e51ff928fceda566948840f8c92e2a6611a141bb9c5e276c1b88ecb93e27` |
| `114_script_A2_K4_3b_RG_BR3B2f3_Frobenius_null_direction_audit.py` | `DO_NOT_RUN_TECHNICAL` | unexecuted duplicate after patch-helper failure | `115_script_A2_K4_3b_RG_BR3B2f3_Frobenius_null_direction_audit_fixed.py` | `c94a01fe69048c91e80d10cec9364524ebf7e89007f6b9f19fdb2fe7bb8dffcd` |
| `118_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py` | `DO_NOT_RUN_TECHNICAL` | preserved SyntaxError: missing parenthesis in solve_fuel | `124_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain_audited.py` | `e5ea459aef997b593fc1fc192d5d3c300bd97cee5efa198c60432122f097950f` |
| `119_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py` | `DO_NOT_RUN_TECHNICAL` | preserved SyntaxError: outer list still unclosed | `124_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain_audited.py` | `f4e82c3d717600f02748646ac89f85d3838f26872efdeb4377323d8fa195dc8c` |
| `120_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py` | `DO_NOT_RUN_TECHNICAL` | numpy.bool_ JSON serialization failure after equations | `121/124 corrected chain` | `f466f39dfb435cc20c7ce3f04eb2c622889d979385db12376737d6fd109efe70` |
| `133_script_A2_K4_3b_RG_BR3C_a_projected_order_audit.py` | `DO_NOT_RUN_TECHNICAL` | source-verdict marker had two matches | `134_script_A2_K4_3b_RG_BR3C_a_projected_order_audit_fixed.py` | `55058ff1c292e9b00f18356fdbbdae9964074d9cd52d3fdc732a2e00f120af72` |
| `163_script_A2_K4_C7_7c_K7a_J4_composite_projected_jacobian_gate.py` | `DO_NOT_RUN_TECHNICAL` | composite parser used the wrong nested JSON path | `164_script_A2_K4_C7_7c_K7a_J4b_composite_parser_corrected_gate.py` | `1b4fb79ca2d5bb77d1aeadf986cd9c12178317d886778b36716a48dcbcd9b329` |
| `170_script_A2_K4_C7_7c_K7b3b_hard_constrained_standard_export.py` | `DO_NOT_RUN_TECHNICAL` | unsupported mpmath matrix[:, list] slice | `174_script_A2_K4_C7_7c_K7b3b1_slice_and_physical_mu_export.py` | `1a7666a0cddd46dece2b3faa901295af2a0be42a87cff2d3c7c122402b60c3c7` |
| `173_script_A2_K4_C7_7c_K7b3b1_physical_mu_registry_export.py` | `DO_NOT_RUN_TECHNICAL` | patch searched the capture marker in the wrong transformation layer | `174_script_A2_K4_C7_7c_K7b3b1_slice_and_physical_mu_export.py` | `2e55ea23f2e8766a8bdfb18848e5155a1bbe10b32efaea33dee7abf72e63dc69` |
| `179_script_A2_K4_C7_7c_K7c3_NID_deep_short_projected_ODE.py` | `DO_NOT_RUN_TECHNICAL` | assumed JSON dict order equals registered state order | `180_script_A2_K4_C7_7c_K7c3_NID_deep_JSON_order_corrected_ODE.py` | `8f45dc698817992e4fb2b859a7cafa49d225b4f7f5fd54b07f88ca99059bd441` |
| `181_script_A2_K4_C7_7c_K7c3a_exact_linear_operator_profile.py` | `DO_NOT_RUN_TECHNICAL` | unit physical basis triggered normalized safety cap | `182_script_A2_K4_C7_7c_K7c3a1_normalized_basis_operator_profile.py` | `359aae29416998383f25e0e190ce34014b53a7275782e8150b803dc9f9723832` |
| `183_script_A2_K4_C7_7c_K7c3b_fixed_RK4_step_convergence.py` | `DO_NOT_RUN_TECHNICAL` | NumPy bool JSON failure; also leaves unreachable legacy solver | `184_script_A2_K4_C7_7c_K7c3b_fixed_RK4_JSON_bool_corrected.py` | `90f177dcd8ac612524ab9dd3dba4516ec7a3805f4de46682bebe5f9d566ea7c8` |
| `186_script_A2_K4_C7_7c_K7c3d_M_rhs_term_ledger.py` | `DO_NOT_RUN_TECHNICAL` | incomplete file ending at __K7C3D_CONTINUE__ | `new numbered M-prime ledger` | `9923ed61c47b696088d517dcd5697b260cbf89568b6c284facd2044ce68a36ff` |
| `188_script_python_corpus_status_and_known_error_audit.py` | `SUPERSEDED` | immutable 192-target corpus snapshot | `196_script_python_corpus_status_audit_after_K7b_P0_segmented.py` | `5acce3680b082a4fb07ca47ddb9f950668ae5f1758d53128c4d16c9280e889d6` |
| `189_script_A2_K4_C7_7c_K7b3b2_fail_closed_physical_mu_gate.py` | `DO_NOT_RUN_TECHNICAL` | PF-012: parser marker patched one generated wrapper layer too early | `192_script_A2_K4_C7_7c_K7b3b2a_fail_closed_physical_mu_gate.py` | `01ff76baac0dba1552ff1e8f2d7731751f938ad69bc72bcbf92e6242ff49b2ba` |
| `190_script_A2_K4_C7_7c_K7b_P0_fail_closed_regression_gate.py` | `DO_NOT_RUN_TECHNICAL` | depends on technically dead script 189; no scientific aggregate was run | `195_script_A2_K4_C7_7c_K7b_P0_segmented_offline_aggregate.py` | `0549fb845f1a5b81b88fad18c6b362f4442aad1d59d07f1ff067b0b911d699fc` |
| `191_script_python_corpus_status_audit_after_K7b_P0.py` | `SUPERSEDED` | intermediate 195-target corpus snapshot | `196_script_python_corpus_status_audit_after_K7b_P0_segmented.py` | `8d12ad8ae3031406e640139c65a8d6382d0be1906ff72c145d9852480578c712` |
| `193_script_A2_K4_C7_7c_K7b_P0a_PF012_corrected_regression_gate.py` | `SUPERSEDED` | monolithic aggregate hit its preregistered internal timeout | `195_script_A2_K4_C7_7c_K7b_P0_segmented_offline_aggregate.py` | `df0815eb6292f39300c97767252808672462e34fb2121cfa046f4ec56073a465` |
| `194_script_python_corpus_status_audit_after_PF012.py` | `SUPERSEDED` | intermediate 198-target corpus snapshot | `196_script_python_corpus_status_audit_after_K7b_P0_segmented.py` | `5881f1734dce594bbd6033c89c94957857d558e07f8f40d59a46109e75990c1a` |
| `196_script_python_corpus_status_audit_after_K7b_P0_segmented.py` | `SUPERSEDED` | immutable 200-target snapshot pred čistým P1 RK4 | `198_script_python_corpus_status_audit_after_K7c_P1_clean_RK4.py` | `013507cd100e7818149077c0b9a785bd901ea8196eaeb47ca6b81c0535efc014` |
| `28_script_A2_K4_full_superhorizon_relative_mode.py` | `DO_NOT_RUN_TECHNICAL` | numpy.bool_ JSON failure after integration | `29_script_A2_K4_full_superhorizon_relative_mode_serialized.py` | `e27587aed5dced17eae8603e55ee835c27e64b76ec871cb246e1e7f313891227` |
| `43_script_A2_K5_1_delta_zero_singular_limit.py` | `DO_NOT_RUN_TECHNICAL` | AttributeError from a non-exported helper | `44_script_A2_K5_1_delta_zero_singular_limit_fixed.py` | `8af163fbd4c005fc1acd0c66e2e17e41ba41f962dffcfa1f99d735b68d5f5b83` |
| `51_script_A2_K11_script45_equation_and_sign_audit.py` | `DO_NOT_RUN_TECHNICAL` | historical long/overflowing anti-damping branch; partial results preserved | `52_script_A2_K11_script45_recoverable_runs.py` | `8aaa966aaafc273cea2cedd816cfd12444314cdac47a48d2800faf9abe3acb5a` |
| `91_script_A2_K4_3b_RG_BR2_Omega_conditioned_DAE.py` | `DO_NOT_RUN_TECHNICAL` | numpy.bool_ JSON serialization failure | `92_script_A2_K4_3b_RG_BR2_Omega_conditioned_DAE_json_fixed_alias.py` | `a1384faeecb83bfb13ce52a26bd66b80331214ddce2b13fccb206435506c989f` |
| `93_script_A2_K4_3b_RG_BR2_velocity_roundoff_condition_gate.py` | `DO_NOT_RUN_TECHNICAL` | numpy.bool_ JSON serialization failure | `94_script_A2_K4_3b_RG_BR2_velocity_roundoff_condition_gate_json_alias.py` | `ce7aa1c82bcdf42b5af89cba9149372f8e66d3cf41a6da3a98a7155b7d591f6e` |
| `168_script_A2_K4_C7_7c_K7b3a_high_precision_standard_coefficient_export.py` | `DO_NOT_USE_PHYSICS` | soft least-squares moved exact physical anchors | `174/175 hard-constrained chain` | `9049e4714c4f85487503c4e45fe2af01c967b45ea7378bf15f99810d71e62035` |
| `169_script_A2_K4_C7_7c_K7b3a_high_precision_standard_constraint_gate.py` | `DO_NOT_USE_PHYSICS` | gate of dead soft-constraint formulation | `174/175 hard-constrained chain` | `fc7ba6362f9b9cddd4edc094ebf49ff417e2b2b47061b4c30192d0e93c39fa96` |
| `172_script_A2_K4_C7_7c_K7b3b_hard_constrained_constraint_gate.py` | `DO_NOT_USE_PHYSICS` | compared physical-mu float state with mu=0 HP registry and contains fail-open rank check | `new fail-closed successor of 175/176` | `3ba3118dbd96fa45f50bc0f367434140a0552d20173493247e545e96dc2ddeb7` |
| `45_script_A2_K11_S8_K1b_superhorizon_instability_test.py` | `DO_NOT_USE_PHYSICS` | printed PASS rejected: wrong/incomplete equations and failed Einstein constraint | `new covariant K11 operator required` | `973905d79cbecbfd2de55f13d3d3713d66c18b068ba74c7cab566001a7312aeb` |
| `46_script_A2_K11_S8_K1b_rigorous_amplitude_scaling_test.py` | `DO_NOT_USE_PHYSICS` | inherits the non-authoritative K11 equation system | `new covariant K11 operator required` | `e24c8d18a177bc112ecf7fe289cbe3b45d66adfcabe313889c8ee2c5a28f559b` |
| `47_script_A2_K11_S8_K1b_fully_consistent_einstein_test.py` | `DO_NOT_USE_PHYSICS` | later audit rejects its physical/constraint interpretation | `68_script_A2_K11_script47_physics_and_constraint_audit.py` | `3cffd6e9977bd8a4619362bbd0bddcc2436bbef468ec47b00dadd8f6f0e056bc` |
| `61_script_A2_K7_K3_1_K2_2_K1b_spin2_coupling_scale_gate_PRE_ERRATUM_OVERBROAD.py` | `DO_NOT_USE_PHYSICS` | pre-erratum overbroad spin-2 conclusion | `61_script_A2_K7_K3_1_K2_2_K1b_spin2_coupling_scale_gate.py` | `444b658d895374410e1f4ecd10f547130c5fb944388e91a2ce4fda9046bbdcac` |
| `105_script_A2_K4_3b_RG_BR3B2e2_NIV_shear_CAMB_constraint_crosscheck.py` | `ENVIRONMENT_BLOCKED` | symbolic CAMB output requires unavailable Fortran compiler | `106_script_A2_K4_3b_RG_BR3B2e2_NIV_shear_CAMB_precompiled_crosscheck.py` | `350d0c1ed7da26a7048c9086852e583c94025154941db20454dc87d3634ebb73` |
| `78_script_A2_K4_3b_RG_collective_CAMB_regular_seed_active_start_fixed.py` | `ENVIRONMENT_BLOCKED` | symbolic pi_r path requires unavailable Fortran compiler | `79_script_A2_K4_3b_RG_collective_CAMB_regular_seed_precompiled_only.py` | `8c6151c186faaa606ffeaf2991b010bfe368a54e9d904cc1e6256c13a40f493d` |
| `110_script_A2_K4_3b_RG_BR3B2f_CAMB_mode_coefficients_in_a.py` | `RUNNABLE_REVIEW_ONLY` | NID/NIV regression unstable for high coefficients | `115/116/124 chain` | `97e4f522077f418cac3053269cb5c24a1058eef80b171d88f73fc78bce259ff3` |
| `111_script_A2_K4_3b_RG_BR3B2f2_NID_NIV_baryon_fraction_difference.py` | `RUNNABLE_REVIEW_ONLY` | time-window dependence remained | `115/116/124 chain` | `c8a91e41fdf5c05c44fc69a459c1755c1e311580bafb4fccf736d1dbcfcaf19d` |
| `113_script_A2_K4_3b_RG_BR3B2f3_Frobenius_bounded_coefficients.py` | `RUNNABLE_REVIEW_ONLY` | leading coefficients passed but full-rank/k-independence gates were not valid | `115/116 chain` | `53541b338834bf58b8ad9090f51f9e24bd45363c92d04a1f27c27a2ba415b5f9` |
| `121_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py` | `RUNNABLE_REVIEW_ONLY` | legacy shear oracle was wrong; result localized but not authoritative | `124_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain_audited.py` | `b088d27114e2628afd7a322c20947e81226d23c1cccf119b5dc21cc289c75f84` |
| `126_script_A2_K4_3b_RG_BR3B2g_l3_ash_full_ledger.py` | `RUNNABLE_REVIEW_ONLY` | homogeneous L3/L4 modes contaminated early coefficients | `127_script_A2_K4_3b_RG_BR3B2g_l3_ash_regular_hierarchy.py` | `5ce670e19f068567ed5066b9d851943a9ee8cffbeb98dabd608d4f5993682a72` |
| `131_script_A2_K4_3b_RG_BR3C_a_order5_order6_state_audit.py` | `RUNNABLE_REVIEW_ONLY` | division of round-off zero slots made F3/F4 unstable | `132/134 chain` | `702afdd878902f8c63d53de13be91a59b015c692656b55c7ebfbd7c47583b03c` |
| `150_script_A2_K4_C7_7c_segment_profiler.py` | `RUNNABLE_REVIEW_ONLY` | historical profiler only; no physical or score verdict | `later K7 diagnostics` | `bb8d68a970a67c802abcc776e8538fa3817088deb48593e9ee3d2d839bab12e6` |
| `151_script_A2_K4_C7_7c_initial_scaled_jacobian_profile.py` | `RUNNABLE_REVIEW_ONLY` | envelope-coordinate Jacobian diagnostic can be scale-dominated | `157/158 and K7a chain` | `22ee98940e86603fccee5ebf62ddefabf7cc233124d4854e9bb985d0670b4bb9` |
| `152_script_A2_K4_C7_7c_matrix_balance_diagnostic.py` | `RUNNABLE_REVIEW_ONLY` | SVD/condition diagnostics depend on envelope scaling | `157/158 and K7a chain` | `460785d2ba37c56c84bee9bf0ea981ee0c4aa111f3a71e37505524965542ab1d` |
| `159_script_A2_K4_C7_7c_K7a_projected_jacobian_audit.py` | `RUNNABLE_REVIEW_ONLY` | double finite-difference T-prime cancellation | `161/162/164 safe chain` | `4051da86fb855e071d94f6e1a274828123dcf2d3dce66d974aaeb2ddfbd7146e` |
| `160_script_A2_K4_C7_7c_K7a_J2_high_precision_Tprime_audit.py` | `RUNNABLE_REVIEW_ONLY` | central-difference cancellation remained at high precision | `161_script_A2_K4_C7_7c_K7a_J3_cancellation_safe_Tprime_audit.py` | `a8f6c0b7686fd9c4681fc4a2dcc55426174032c4beef32d3c082d1e711e90a08` |
| `182_script_A2_K4_C7_7c_K7c3a1_normalized_basis_operator_profile.py` | `RUNNABLE_REVIEW_ONLY` | zero-integration diagnostic; reconstruction gate remained REVIEW | `clean standalone K7c successor` | `c534f8a687f7dadd062a3dabc5e407ef8d6b3f14107033f029ebc929ced550ef` |
| `184_script_A2_K4_C7_7c_K7c3b_fixed_RK4_JSON_bool_corrected.py` | `RUNNABLE_REVIEW_ONLY` | endpoint difference 1.443e-6 exceeded preregistered 1e-6 | `clean standalone K7c successor` | `9eece141c889dfbfa42d7bf9cc5de331964460c525211bc88b0b779adb1add22` |
| `185_script_A2_K4_C7_7c_K7c3c_second_fixed_RK4_refinement.py` | `RUNNABLE_REVIEW_ONLY` | non-asymptotic M refinement ratio 0.367 | `new M-prime term ledger` | `ce75b6db373f70701c7b35650ceb663c430197f2ed237a7346e7ebb666982686` |
| `29_script_A2_K4_full_superhorizon_relative_mode_serialized.py` | `RUNNABLE_REVIEW_ONLY` | serialization fixed, but convergence and pointwise constraint gates failed | `later K4.1/K4.2 chain` | `c5aae2d8628e77e8c6c44932a0e8cd2690f6ace6b22691bd36f4e3e907f1ebba` |
| `52_script_A2_K11_script45_recoverable_runs.py` | `RUNNABLE_REVIEW_ONLY` | recoverable branches only; no converged or constraint-valid physical PASS | `54_script_A2_K11_script45_constraint_and_scaling_audit.py` | `b312c1a379f71dabbee42ac34c2f7adf10f6fd65088fcb357774205d0aa92be3` |
| `53_script_A2_K11_solver_floor_and_amplitude_scaling.py` | `RUNNABLE_REVIEW_ONLY` | documented numerical-resolution failure | `54_script_A2_K11_script45_constraint_and_scaling_audit.py` | `55951c028a1b54c2c68f1b9a20b53fe3d60d0806c5d8ce1517e1b9dc9802c8b2` |
| `54_script_A2_K11_script45_constraint_and_scaling_audit.py` | `RUNNABLE_REVIEW_ONLY` | audit diagnostic; current K11 requires a new operator before evolution | `none` | `c953bb7bc38c6f3ffc1f4d70c747aa8e7fc18b2b5f2fcf0331a8c454139330cf` |
| `89_script_A2_K4_3b_RG_BR2_backreacted_superhorizon_evolution.py` | `RUNNABLE_REVIEW_ONLY` | raw eta second derivative is ill-conditioned in deep radiation era | `90/92/94 conditioned chain` | `bcc9da578ceff40476c71c95e8a3028187b6fb4c873ecf9910d07a34c44ed046` |
| `90_script_A2_K4_3b_RG_BR2_conditioned_DAE_constraint_audit.py` | `RUNNABLE_REVIEW_ONLY` | species variables remained cancellation-prone | `92/94 conditioned chain` | `dca036ca320e2f6905516394be1d1bc0173ac9f365b28b0626ebcf75c3266221` |
| `92_script_A2_K4_3b_RG_BR2_Omega_conditioned_DAE_json_fixed_alias.py` | `RUNNABLE_REVIEW_ONLY` | density passed but two velocity modes remained above fixed tolerance | `94_script_A2_K4_3b_RG_BR2_velocity_roundoff_condition_gate_json_alias.py` | `c65d4dfdeae6658bf9292e400670907de9914c055a4b650f5d0209e5a98b802b` |
| `107_script_A2_K4_3b_RG_BR3B2e2_NID_NIV_shear_sector_solution.py` | `SUPERSEDED` | exact linsolve repeatedly exceeded the bounded runtime | `108_script_A2_K4_3b_RG_BR3B2e2_NID_NIV_shear_sector_solution_bounded.py` | `e56697d4e3f4d4caae7d9b3450ed03cafb759be709cdc43349a936f914991219` |
| `112_script_A2_K4_3b_RG_BR3B2f3_exact_Frobenius_standard_NID_NIV.py` | `SUPERSEDED` | symbolic series exceeded external timeout | `115_script_A2_K4_3b_RG_BR3B2f3_Frobenius_null_direction_audit_fixed.py` | `8b32ae418e8baa7fe6f232097d1b00c58fad7a0e0385088d900c39ddf33cf46f` |
| `140_script_A2_K4_3b_RG_BR3C_c_species_mode_activity_audit.py` | `SUPERSEDED` | key handling corrected by explicit fixed-keys successor | `141_script_A2_K4_3b_RG_BR3C_c_species_mode_activity_audit_fixed_keys.py` | `7248217b056d1a764fba4753a1b8f5d2b565904713ec3d45a8b0065239e06c52` |
| `142_script_A2_K4_3b_RG_C7_7c_K2_normalized_component_evolution.py` | `SUPERSEDED` | normalized DOP853 numerical subtrack timed out | `K7 projected-basis chain` | `0ddf286acf4d45a5ac5c85d367db6f0c7f8a7b843a3564a68eff11b7dcbe181b` |
| `143_script_A2_K4_3b_RG_C7_7c_K2_normalized_activity_audit.py` | `SUPERSEDED` | audit wrapper of timed-out K2 subtrack | `K7 projected-basis chain` | `b7f1badef501a299ea87a3f448e14136209939339befe3695b33a39820cb0e92` |
| `144_script_A2_K4_3b_RG_C7_7c_K3_normalized_Radau_evolution.py` | `SUPERSEDED` | Radau subtrack timed out/failed on scaling | `K7 projected-basis chain` | `9e4299437e448cebf9c502f744da4400321a014fdb5ea78aa5529e7ef77dea64` |
| `145_script_A2_K4_3b_RG_C7_7c_K3_normalized_Radau_activity_audit.py` | `SUPERSEDED` | audit wrapper of dead K3 numerical subtrack | `K7 projected-basis chain` | `2ff3e7ace29e02856cc11220eb9f01f313bb003984d4b3cdbd73229f9f035252` |
| `147_script_A2_K4_3b_RG_C7_7c_K4_analytic_envelope_evolution.py` | `SUPERSEDED` | analytic-envelope evolution hit internal deadline | `K7 projected-basis chain` | `e02325fcdfc8645fdc13a5d0a5cc7e213a1158bd42ac5936f3680f8bb8b778dd` |
| `148_script_A2_K4_3b_RG_C7_7c_K4_analytic_envelope_activity_audit.py` | `SUPERSEDED` | activity gate unclosed because child timed out | `K7 projected-basis chain` | `bafad4e610715a46976ac912dceb64b45128ef069a2f7f383c27de571d47bf80` |
| `153_script_A2_K4_C7_7c_K5_balanced_segment_evolution.py` | `SUPERSEDED` | balanced numerical subtrack timed out and changed error metric | `K7 projected-basis chain` | `5003389d4c5fc318f39fe6cd00cb1b98d7a4e849b148158ed562d753a429abd8` |
| `154_script_A2_K4_C7_7c_K6_vector_atol_segment_evolution.py` | `SUPERSEDED` | vector-atol subtrack demanded precision below float64 arithmetic floor | `K7 projected-basis chain` | `3d61335a8accc11d7571254cb5379192eef7b9e82ac08d7b467d8c9eef15b323` |
| `171_script_A2_K4_C7_7c_K7b3b_hard_constrained_slice_corrected_export.py` | `SUPERSEDED` | later mu=0 solve overwrote the physical HP registry | `174_script_A2_K4_C7_7c_K7b3b1_slice_and_physical_mu_export.py` | `06e284b618a4c63c27ac8804de6705799f221c0a860f0db93636ca58f1551ced` |
| `180_script_A2_K4_C7_7c_K7c3_NID_deep_JSON_order_corrected_ODE.py` | `SUPERSEDED` | adaptive ODE hit the 200000 RHS cap | `184/185 fixed-RK4 review chain` | `c9e77983049388370464e9e08f2605c39a48e4e24042e5a0bb05eecae049208c` |
| `75_script_A2_K4_3b_exact_CAMB_hierarchy_coefficient_crosscheck.py` | `SUPERSEDED` | J2/G2 alias mapping was not converted | `76_script_A2_K4_3b_exact_CAMB_hierarchy_coefficients_alias_fixed.py` | `1ad8b2b59efd649d089e6adbd38f850eae09b77cd8c70a5e996ab8509a56c228` |

## Syntaxové a vstupné zlyhania

- `118_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py` — `closing parenthesis ')' does not match opening parenthesis '[' on line 232 at line 233:85`; `DO_NOT_RUN_TECHNICAL`.
- `119_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py` — `closing parenthesis ')' does not match opening parenthesis '[' on line 236 at line 237:85`; `DO_NOT_RUN_TECHNICAL`.
- `186_script_A2_K4_C7_7c_K7c3d_M_rhs_term_ledger.py` — nemá vykonateľný top-level vstup; súbor je nedokončený a neprodukuje verdict.

## Surové nálezy známych vzorov

Tieto nálezy sú **lint kandidáti, nie automatický rozsudok**. V source-generujúcich wrapperoch môže text patriť starému markeru, ktorý sa nahrádza ešte pred vykonaním. Rozhoduje karanténny stav a ručný audit vykonanej cesty.

| Súbor | Nájdené vzory |
|---|---|
| `142_script_A2_K4_3b_RG_C7_7c_K2_normalized_component_evolution.py` | `long_run_without_internal_runtime_argument` |
| `150_script_A2_K4_C7_7c_segment_profiler.py` | `long_run_without_internal_runtime_argument` |
| `154_script_A2_K4_C7_7c_K6_vector_atol_segment_evolution.py` | `long_run_without_internal_runtime_argument` |
| `170_script_A2_K4_C7_7c_K7b3b_hard_constrained_standard_export.py` | `unsupported_mpmath_list_slice` |
| `171_script_A2_K4_C7_7c_K7b3b_hard_constrained_slice_corrected_export.py` | `unsupported_mpmath_list_slice` |
| `172_script_A2_K4_C7_7c_K7b3b_hard_constrained_constraint_gate.py` | `fail_open_get_equality` |
| `174_script_A2_K4_C7_7c_K7b3b1_slice_and_physical_mu_export.py` | `unsupported_mpmath_list_slice` |
| `179_script_A2_K4_C7_7c_K7c3_NID_deep_short_projected_ODE.py` | `json_key_order_assumption` |
| `180_script_A2_K4_C7_7c_K7c3_NID_deep_JSON_order_corrected_ODE.py` | `json_key_order_assumption` |
| `181_script_A2_K4_C7_7c_K7c3a_exact_linear_operator_profile.py` | `json_key_order_assumption, long_run_without_internal_runtime_argument` |
| `183_script_A2_K4_C7_7c_K7c3b_fixed_RK4_step_convergence.py` | `json_key_order_assumption, generated_unreachable_legacy_solver_risk, long_run_without_internal_runtime_argument` |
| `186_script_A2_K4_C7_7c_K7c3d_M_rhs_term_ledger.py` | `incomplete_continuation_marker` |
| `187_script_A2_K4_K7b_K7c_claim_audit.py` | `fail_open_get_equality, json_key_order_assumption, generated_unreachable_legacy_solver_risk` |
| `45_script_A2_K11_S8_K1b_superhorizon_instability_test.py` | `long_run_without_internal_runtime_argument` |
| `46_script_A2_K11_S8_K1b_rigorous_amplitude_scaling_test.py` | `long_run_without_internal_runtime_argument` |
| `47_script_A2_K11_S8_K1b_fully_consistent_einstein_test.py` | `long_run_without_internal_runtime_argument` |
| `51_script_A2_K11_script45_equation_and_sign_audit.py` | `long_run_without_internal_runtime_argument` |
| `53_script_A2_K11_solver_floor_and_amplitude_scaling.py` | `long_run_without_internal_runtime_argument` |
| `54_script_A2_K11_script45_constraint_and_scaling_audit.py` | `long_run_without_internal_runtime_argument` |
| `66_script_A2_K4_1_complete_regular_mode_basis.py` | `long_run_without_internal_runtime_argument` |

## AR8 — fyzikálna karanténa projektovaného K7 lineage (2026-07-15)

Táto vrstva karantény je **dodatočná k technickému stavu** v hlavnej tabuľke.
Nemaže ani neprepisuje historické behy. Audit `L2-B1` presne oddelil skripty,
ktoré definujú redukovanú 13-zložkovú RHS bez dynamického `U_c`, od skriptov,
ktoré iba kontrolujú jej dôsledky. Deklarovaný K4 energy-frame prenos však
`U_c` vyžaduje. Preto sa nijaký z týchto artefaktov nesmie spustiť alebo
citovať ako fyzikálny dôkaz A2-K4; povolené sú iba výslovne predregistrované
historické reprodukcie. Nejde o rozsudok smrti mechanizmu A2-K4, ale o STOP
tejto implementačnej línie. Autoritatívny nástupca: P5 s úplným stavom.

| Súbor | AR8 stav | Presný dôvod | SHA-256 |
|---|---|---|---|
| `179_script_A2_K4_C7_7c_K7c3_NID_deep_short_projected_ODE.py` | `DO_NOT_USE_PHYSICS` | priamo definuje redukovanú RHS bez `U_c`; navyše historická technická karanténa | `8f45dc698817992e4fb2b859a7cafa49d225b4f7f5fd54b07f88ca99059bd441` |
| `197_script_A2_K4_C7_7c_K7c_P1_clean_standalone_RK4.py` | `DO_NOT_USE_PHYSICS` | definuje redukovanú RHS bez `U_c` a používa starý pevný `K_MPC` background | `088b4cd58f57a30bd061d30042ba3e2cb5021df9bf320003ed8291d86fb6c022` |
| `203_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4.py` | `DO_NOT_USE_PHYSICS` | definuje redukovanú RHS bez `U_c` a starý pevný `K_MPC` background | `886aaf8a48086ec464e5495dfe1cbab3b065b476b6fcf89976472addec9b2243` |
| `204_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4_complete.py` | `DO_NOT_USE_PHYSICS` | definuje redukovanú RHS bez `U_c` a starý pevný `K_MPC` background | `abf3733d92d493011d2a5e36281245d007b6d9bd7183b28b827f5e372e0a4593` |
| `205_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4_audited.py` | `DO_NOT_USE_PHYSICS` | definuje redukovanú RHS bez `U_c` a starý pevný `K_MPC` background | `b7ec8bad3bfb0d48ec91d6f1bb0a602fa1834a021bb94c92d6d1b398d5f3cdc2` |
| `209_script_A2_K4_C7_7c_K7c_P4a_single_case_solver.py` | `DO_NOT_USE_PHYSICS` | definuje redukovanú RHS bez `U_c` a starý pevný `K_MPC` background | `67e5b3c1b7c942242e4feb4458a4cc81a52f6417e25d50a6e2009023f321a612` |
| `213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py` | `DO_NOT_USE_PHYSICS` | definuje redukovanú RHS bez `U_c` a starý pevný `K_MPC` background | `8726bae5e3f8c06c74d2053bf9b7430f22b73fa867534c9b421a228aec8fdc39` |
| `181_script_A2_K4_C7_7c_K7c3a_exact_linear_operator_profile.py` | `RUNNABLE_REVIEW_ONLY` | checker redukovanej RHS; jeho výsledok nedokazuje K4 | `359aae29416998383f25e0e190ce34014b53a7275782e8150b803dc9f9723832` |
| `182_script_A2_K4_C7_7c_K7c3a1_normalized_basis_operator_profile.py` | `RUNNABLE_REVIEW_ONLY` | checker redukovanej RHS; jeho výsledok nedokazuje K4 | `c534f8a687f7dadd062a3dabc5e407ef8d6b3f14107033f029ebc929ced550ef` |
| `183_script_A2_K4_C7_7c_K7c3b_fixed_RK4_step_convergence.py` | `RUNNABLE_REVIEW_ONLY` | checker redukovanej RHS; jeho výsledok nedokazuje K4 | `90f177dcd8ac612524ab9dd3dba4516ec7a3805f4de46682bebe5f9d566ea7c8` |
| `206_script_A2_K4_C7_7c_K7c_P3b_source_delta_audit.py` | `RUNNABLE_REVIEW_ONLY` | checker redukovanej RHS; jeho výsledok nedokazuje K4 | `511a6ac302960b032b3947e3b136b21940a851c64c405e44a0edd2b1442d3f41` |
| `207_script_A2_K4_C7_7c_K7c_P3b_source_delta_audit_tuple_fixed.py` | `RUNNABLE_REVIEW_ONLY` | checker redukovanej RHS; jeho výsledok nedokazuje K4 | `00b2b1ddc87fa9e544a3a2a9c196d94e621b4e440d99b0c1c4aef551ee047070` |
| `210_script_A2_K4_C7_7c_K7c_P4a_source_delta_audit.py` | `RUNNABLE_REVIEW_ONLY` | checker redukovanej RHS; jeho výsledok nedokazuje K4 | `d86022c8d8d5c32223ecd9f62097aee09a6685c8358f8a1d1b0d691c897f662d` |
| `214_script_A2_K4_C7_7c_K7d_integrated_preflight_and_source_audit.py` | `RUNNABLE_REVIEW_ONLY` | checker redukovanej RHS; jeho výsledok nedokazuje K4 | `133a57d20f60845b6d62fae6ea2a2276e71c143a5da525d9c27e88c233b2e865` |
| `215_script_A2_K4_C7_7c_K7d_V1_offline_diagnostic_correction.py` | `RUNNABLE_REVIEW_ONLY` | checker redukovanej RHS; jeho výsledok nedokazuje K4 | `5b9e123decfc57b4903eeb9f9f8e9eb286f4070aafc89c8ea4ec88d5144f9129` |
| `216_script_A2_K4_C7_7c_K7d_V2_HP_parity_shear_correction.py` | `RUNNABLE_REVIEW_ONLY` | checker redukovanej RHS; jeho výsledok nedokazuje K4 | `0218c82c08c413058002676f14c5867cf14c8575589b44e916427b52e9b85cbe` |

L2-B1 je uložený v `Independent_Audits/Implementation_Lineage/05_L2_B1_PROJECTED_K7_RESULT_SK.md`.

## Aktuálne opravené revízie, ktoré sa nemajú omylom karantenizovať

- skript 66 aktuálne obsahuje `regular_count=int(...)`; stará zlyhaná hash revízia ostáva iba v errate;
- skript 67 aktuálne konvertuje kontroly cez `bool(...)`; stará serializačná revízia ostáva iba v errate;
- skript 174 obsahuje starý nepodporovaný slice iba ako marker určený na nahradenie; vykonaná cesta používa explicitnú maticu;
- skripty 180/181/183 môžu obsahovať starý `tuple(deep_seed)` ako replacement marker; to neodstraňuje ich samostatné zdokumentované dôvody REVIEW/smrti.

## Aktualizácia registra

Pri novej formálnej chybe sa pred ďalšou fyzikou vykonajú tri kroky: doplniť `00_PYTHON_FORMAL_ERROR_LEDGER.md`, vytvoriť alebo doplniť nový číslovaný korpusový checker a vydať nový datovaný dodatok k tomuto MD alebo nový regenerovaný register. Aktuálny checker je 198; staré snapshoty sa neprepisujú a ostávajú `SUPERSEDED`. Checker 198 auditoval 202 ostatných `.py` a eviduje 69 karanténnych položiek. Starý skript sa nemaže. Ak je opravený v tej istej ceste, status musí byť viazaný na SHA-256 revíziu; preferovaný postup je nový číslovaný nástupca.

## Dodatok 2026-07-16 — KMPC-027 / PF-068

| Súbor | Stav | Dôvod | Autoritatívny nástupca | SHA-256 |
|---|---|---|---|---|
| `271_script_KMPC_027_P5_3g7_m3_full_ra_seed_attempt6.py` | `DO_NOT_RUN_FULL_MODE / SMOKE_REGRESSION_ONLY` | frozen compile/help a úzky smoke prešli, ale `--mode AD` zoskupil 18 F0/M3 solve blokov a prekročil interný 4.8 s limit pred verdictom; opakovanie rovnakého príkazu je zbytočné | pokus 7 s jedným `mode×k×variant` na proces podľa dokumentu 39 | `E72DD58E8D2719DE1DF9286D9E7D8D8FE5938670DCF74C2EC5E64171BE01554A` |

## Dodatok 2026-07-16 — KMPC-028 až KMPC-030

| Skript | Stav | Dôvod | Nástupca | SHA-256 |
|---|---|---|---|---|
| `272_script_KMPC_028_P5_3g7_m3_full_ra_atomic_attempt7.py` | `RUNNABLE_REGRESSION_ONLY / IMMUTABLE_RESULT_EXISTS` | autoritatívny J4 výsledok už existuje; rovnaký output sa nesmie prepisovať | KMPC-029/030 lineage | `65AD56720AD06B32BE0EC54C2924491F1D8D9DB1C84E04015E56521B8FF8813D` |
| `273_script_KMPC_029_P5_3g7_m3_full_ra_support_ladder_attempt8.py` | `RUNNABLE_REGRESSION_ONLY / IMMUTABLE_RESULTS_EXIST` | J6/J8 výsledky existujú; opakovanie nepridá informáciu | KMPC-030 a pokus 10 tail provenance | `4B44F183325E5BC4437EA5703E2A3DE242A2F11E86D0DB46B1878EAFB12D1F33` |
| `274_script_KMPC_030_P5_3g7_m3_full_ra_j8_refinement_attempt9.py` | `RUNNABLE_REVIEW_ONLY / IMMUTABLE_RESULT_EXISTS` | jedna korekcia technicky prešla; raw tail semantics ostáva REVIEW, rovnaký output je immutable | pokus 10 no-solve decomposition | `81D777534C552DC14E12807814FA63446807C1243B228EAFEE997F9D76B816FD` |
| `275_script_KMPC_031_P5_3g7_m3_full_ra_deep_tail_branch_provenance_attempt10.py` | `RUNNABLE_REGRESSION_ONLY / IMMUTABLE_RESULT_EXISTS` | ARCH-A cieľ úspešne uzavretý na 10/10; opakovanie rovnakého outputu je zakázané | S1/mode coverage je nová fyzikálna brána, nie attempt 11 | `A222F96EEAF32042CCAE634FB71EE1794119704D83B26BC30D83B358568C15B2` |

Shared modul `full_ra_m3_seed.py` sa nekarantenizuje: smoke potvrdil jeho
úzky kontrakt a timeout vznikol granularitou runnera. Jeho fyzikálny scope
ostáva bez plného verdiktu.

## Dodatok 2026-07-16 — KMPC-032 / PF-069

| Skript | Stav | Dôvod | Nástupca | SHA-256 |
|---|---|---|---|---|
| `276_script_KMPC_032_P5_3g7_s_c0_coefficient_passport.py` | `DO_NOT_RUN_AUDIT_TECHNICAL / HELP_SMOKE_HISTORY_ONLY` | prvý skutočný `np.float64` koeficient neprešiel textovou konverziou do SymPy; fyzika nebola vyhodnotená | úzky KMPC-033 RERUN1 scalar-conversion overlay | `B6D108C2B2292E7D83B1C9251665C3C7B4C55D3C16C341D1545F946DC2FBC76E` |
| `277_script_KMPC_033_P5_3g7_s_c0_coefficient_passport_rerun1.py` | `RUNNABLE_REGRESSION_ONLY / IMMUTABLE_RESULT_EXISTS` | PF-069-only RERUN1 dokončil scoped S-C0 passport; opakovanie nesmie prepísať výsledok SHA `4CED9D...CFE8C` | CDI C1 runner 278 po samostatnej predregistrácii | `9FC086E85AE23A6B96F4A859B9C8CB06B8E3F293959756CB354C82DEF06C8B0F` |
| `278_script_KMPC_034_P5_3g7_CDI_C1_primary_extended_coverage.py` | `RUNNABLE_REGRESSION_ONLY / IMMUTABLE_RESULT_EXISTS` | fixed CDI/k=.05/nominal atom dokončený; result SHA `37FB4453...DCE20`; rovnaký output sa nesmie prepísať; jeho `[0,3]` open stav obmedzil KMPC-035 | successor 279 dokončený; ďalší support až po M1 order-7 bráne | `E8C2677E590D8129C6425AABAD5D80C1746BC5EF0B1E90E055A23641040695A4` |
| `279_script_KMPC_035_P5_3g7_CDI_C2_support_03_05_ladder.py` | `RUNNABLE_REGRESSION_ONLY / IMMUTABLE_RESULT_EXISTS` | `GLOBAL_C1/CDI_SUPPORT_STEP_2` dokončený; result SHA `A9BD519F...E42A01`; scoped core/common PASS, `[0,3]` remainder REVIEW; rovnaký output neprepisovať | successor 280 dokončený; current precision/boundary audit, nie automatický `[0,7]` | `09F86A2A6E8BA81F4F41C73722BC40264888D1EF45BB4016F223A5E2C76649E3` |
| `280_script_KMPC_036_P5_3g7_M1_order7_provenance_gate.py` | `RUNNABLE_REGRESSION_ONLY / IMMUTABLE_RESULT_EXISTS` | result SHA `39BB3886...B7B497`; scoped PASS + tri terminal power7 driver precision REVIEW; output neprepisovať | nový precision/boundary audit; support step 3 stále zakázaný | `EBA6F6D0392F94A511D3D0B9FEFDA07558CB6DE5ED968F0CC02AF6754C2A204B` |

V1 base `s_c0_coefficient_passport.py` s hashom
`C370B610...A2A6B95` sa nemení a zachováva príčinu PF-069. Nesmie sa použiť
na nový auditný verdict; nástupca musí zmraziť V1 hash a meniť iba `_q`.

## Dodatok 2026-07-16 — P5/M3 obmedzenie skriptu 124

Tento dodatok nemení nemenné počty checkeru 198. Pridáva neskoršie AR8
fyzikálne obmedzenie, ktoré vzniklo po oprave `K_MPC` backgroundu a po
zavedení nezávislých M3 holdoutov.

| Súbor | Stav | Dôvod | Autoritatívny nástupca | SHA-256 |
|---|---|---|---|---|
| `124_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain_audited.py` | `RUNNABLE_REVIEW_ONLY / REGRESSION_ONLY` | vykonateľný a platný iba pre vlastnú skrátenú NID/NIV maticu; použil všetky Einsteinove rovnice naraz, nemá nezávislý `00/0i` holdout, neobsahuje celý exact-A1 frakčný background a nie je päťmódový P5 seed | `261` M3/P5.3g7 podľa predregistrácie 27 | `681f2e6b1398d593f235adb34dd9fbe94e69e788838575bf5f5918ce74e97ab4` |

Rutinný fyzikálny beh 124 je od tohto dodatku zakázaný. Výslovne
predregistrovaná regresná reprodukcia je povolená s timeoutom, ale jej PASS
nesmie meniť stav P5 ani hĺbku A2-K4. Dôkaz:
`Audit/A2_K4_P5_3G7_M3_LEGACY_BR3_LINEAGE_AUDIT_2026-07-16.md`.

## Dodatok 2026-07-16 — PF-055, prvý runner 261

| Súbor | Stav | Dôvod | Autoritatívny nástupca | SHA-256 |
|---|---|---|---|---|
| `261_script_KMPC_022_P5_3g7_mode_resolved_full_seed_audit.py` | `DO_NOT_RUN_TECHNICAL` | prvý plný payload obsahoval `numpy.bool_`; JSON export skončil `TypeError` a nevznikol výsledkový súbor | `261_script_KMPC_023_P5_3g7_mode_resolved_full_seed_audit_rerun1.py` | `6f749909b52ea6b0b4e99df1a70025aff01519dd0e68d57c884847b9dbe6846b` |

Pôvodný runner sa zachováva bez úpravy. To, že pred výnimkou mohol vyriešiť
matice, nie je vedecký výsledok. RERUN1 smie zmeniť iba serializáciu; base
fyzika ostáva viazaná na hash
`5a89cf82006cb5ecc1d8b4be1fd56a463453ee3d6261968cb64de8ccf2c8b7ae`.

## Dodatok 2026-07-16 — KMPC-023 RERUN1 a base V1

| Súbor | Stav | Dôvod | Autoritatívny nástupca | SHA-256 |
|---|---|---|---|---|
| `261_script_KMPC_023_P5_3g7_mode_resolved_full_seed_audit_rerun1.py` | `RUNNABLE_REVIEW_ONLY` | technicky dobehol, ale štandardný seed mal hodnosť `76/77`; prijatá M1 amplitúda bola iba post-check, nie tvrdá vstupná podmienka, preto výstup nie je P5 seed ani fyzikálny STOP | predregistrovaný `261 ... RERUN2` s M1 elimináciou | `56cae70e6391a5e09dabac233615be2c7f26accd8a37b6c646d1afa8cfe55537` |
| `baseScripts/p5_general_synchronous/mode_resolved_puiseux.py` | `REVIEW_ONLY / V1_UNANCHORED_M1` | znovupoužiteľná matematika k-cancel ostáva platná, ale `solve_standard_seed` rieši neukotvenú rodinu; nesmie produkovať autoritatívny M3/P5 seed | versioned M1-anchored overlay, V1 sa neprepisuje | `5a89cf82006cb5ecc1d8b4be1fd56a463453ee3d6261968cb64de8ccf2c8b7ae` |

RERUN1 JSON s hashom
`4c925d10627a69430f2d3ac59f2609423a8743165d518644ffb1ec9bba869469`
ostáva immutable REVIEW dôkaz príčiny. Presné background identity z neho sa
nestrácajú, ale runner ani V1 solver sa rutinne nespúšťajú na nový verdict.
Podrobný rozsudok:
`Audit/A2_K4_P5_3G7_M3_TCA0_RERUN1_REVIEW_2026-07-16.md`.

## Dodatok 2026-07-16 — KMPC-024 RERUN2 a PF-058

| Súbor | Stav | Dôvod | Autoritatívny nástupca | SHA-256 |
|---|---|---|---|---|
| `261_script_KMPC_024_P5_3g7_mode_resolved_full_seed_audit_rerun2.py` | `RUNNABLE_REVIEW_ONLY / DO_NOT_USE_PHYSICS` | M1 anchor a štandardné constrainty prešli, ale frakčný solver nepreukázal úplný palivový coefficient/row kontrakt; `two_start_power` je iba normová diagnostika jedného radu | žiadny runner, kým nebude uzavretý dvojparametrový palivový/Bianchi ledger | `12ba3b200659703a8edfe601459def9d848a319f0990cf1d86966f0b52eabf95` |
| `baseScripts/p5_general_synchronous/mode_resolved_puiseux_v2_m1_anchored.py` | `PASS_M1_ANCHOR / REVIEW_ONLY_M3` | správne odstraňuje AR50 M1 null smer, ale volá neúplnú V1 frakčnú architektúru a jeho pre-monkeypatch identity guard je tautologický (PF-059) | budúci plný base smie znovupoužiť iba hard-anchor helper po novom audite | `5de2c280b0e9daf528a9e3011368361b37ae53de38827fb6f6ce4ab2019a4455` |

Immutable KMPC-024 JSON hash
`0613ad04cfafcb4414247cdc9fecbcbafa1288520eba51fc5bbde7a37b1c3ee8`
je diagnostika neúplného ansatzu. Rutinné opakovanie je zbytočné. Nejde o
fyzikálny rozsudok smrti K4. Audit:
`Audit/A2_K4_P5_3G7_RERUN2_CONTRACT_PARITY_AUDIT_2026-07-16.md`.

## Dodatok 2026-07-16 — K11-CS2 S0 RUN-001 / PF-061

| Súbor | Stav | Dôvod | Autoritatívny nástupca | SHA-256 |
|---|---|---|---|---|
| `262_script_A2_K11_CS2_full_multispecies_constrained_DAE_runner.py` | `DO_NOT_RUN_TECHNICAL` | structural payload a immutable JSON sa dokončili, ale povinný vonkajší proces skončil timeoutom 124 po duplikovaní plného JSON na stdout; výsledok preto nie je autoritatívny PASS | `263_script_A2_K11_CS2_S0_structural_quiet_output_rerun1.py` | `CCF17673A30E1F550B9761D688254D22407491FD8B10B275C03EB6A40F57A502` |

RUN-001 JSON sa nemaže; hash a rozsah sú v route-local timeout audite.
Runner 263 smie zmeniť iba output/lifecycle obal, nie base fyziku.

## Dodatok 2026-07-16 — K11-CS2 S0 PF-062

| Súbor | Stav | Dôvod | Autoritatívny nástupca | SHA-256 |
|---|---|---|---|---|
| `263_script_A2_K11_CS2_S0_structural_quiet_output_rerun1.py` | `RUNNABLE_REGRESSION_ONLY / DO_NOT_USE_STATE_CONTRACT` | formula identity payload je reprodukovateľný, ale v001 state register obsahuje nadbytočné CAMB E-mode `E_0,E_1`; RUN-002 count PASS je tautologický | posledný K11-CS2 full v002 runner podľa PF-062 | `F008465A16681DCECBDDD0A8E1A00B8B4FBC7D0BB3017C75D158D5894291DF45` |
| `baseScripts/a2_k11_cs2/full_multispecies_constrained_dae.py` | `PASS_FORMULA_IDENTITIES_ONLY / STOP_STATE_REGISTER_V001` | správne K11/A1/CAMB identity, ale chybná state množina a count `4l+11` namiesto `4l+9`; full propagátor aj tak fail-closed | nový versioned full v002 base; v001 sa neprepisuje | `19263A674E1F342E06E6D0D3999E65E58687CCFF20E5EE083A05D06D7BB107FF` |
# 281 / KMPC-037

- `281_script_KMPC_037_P5_3g7_M1_order7_numerical_refinement_boundary_closure.py`
  — `DO_NOT_RUN_TECHNICAL`; immutable PF-072 failure pri V3
  `mpmath.qr_solve: matrix is numerically singular`; KMPC-036 verdict sa
  nemení a runner sa nesmie opakovať.

# 282 / KMPC-038

- `282_script_KMPC_038_P5_3g7_M1_order7_householder_zero_tie_successor.py`
  — `DO_NOT_RUN_TECHNICAL`; PF-073 smoke zasiahol nesprávny `mpmath` owner
  pred plným auditom. Immutable failure sa zachováva a runner sa neopakuje.

# 299 / KMPC-055

- `299_script_KMPC_055_P5_3g7_NIV_support_step2_minus1_4_minus1_6.py`
  — `DO_NOT_RUN_AUDIT_TECHNICAL`; PF-076, neoverený helper owner
  `niv_c1_coverage._all_finite`; canonical výsledok nevznikol, immutable
  failure SHA je `93906783C433800CB9609A7D3F735F01C504840B323EA981E95BDE79CF7576EC`.
  Povolený je iba versioned KMPC-056 owner-overlay nástupca.

# 301 / KMPC-057

- `301_script_KMPC_057_P5_3g7_C2_Fourier_coverage.py`
  — `DO_NOT_RUN_AUDIT_TECHNICAL`; PF-077, smoke porovnával aktuálny C1
  support so zastaranou počiatočnou `S1 MODE_SPEC.extended` mapou. Žiadny
  fyzikálny atóm ani JSON nevznikol. Povolený je iba versioned KMPC-058
  support-contract-guard nástupca pri nezmenenej C2 matici a prahoch.

# 302 / KMPC-058

- `302_script_KMPC_058_P5_3g7_C2_Fourier_coverage_guard_successor.py`
  — `DO_NOT_RUN_AUDIT_TECHNICAL`; PF-078, successor smoke správne ukázal
  obsolete diff iba `(CDI,BI)`, kým fixture chybne očakával aj NID/NIV.
  Žiadny atóm ani JSON nevznikol. Povolený je iba KMPC-059 exact-diff
  nástupca; fyzika, support mapa, prahy a poradie ostávajú nezmenené.

# 303 / KMPC-059

- `303_script_KMPC_059_P5_3g7_C2_Fourier_exact_diff_successor.py`
  — `DO_NOT_RUN_AUDIT_TECHNICAL`; PF-079, exact stale diff už prešiel, ale
  agregovaný corrected guard ostal false bez exportu vnútorného false názvu.
  Žiadny atóm ani JSON nevznikol. Pred ďalším successorom je povinný
  read-only KMPC-060 false-check diagnostic.

# 308 / KMPC-064

- `308_script_KMPC_064_P5_3g7_C2_AD_k0p15_nominal.py`
  — `DO_NOT_RUN_AUDIT_TECHNICAL`; PF-080, atom-local output guard bol
  aktívny počas zdedeného 10-name matrix smoke. Žiadny fyzikálny atóm ani
  JSON nevznikol. Povolený je iba KMPC-065 successor, ktorý oddelí parent
  matrix smoke od restricted atom overlaya; fyzika a prahy sa nemenia.

# 312 / KMPC-068

- `312_script_KMPC_068_P5_3g7_C2_CDI_k0p005_support_07_09.py`
  — `DO_NOT_RUN_AUDIT_TECHNICAL`; PF-081, depth-9 atóm prekročil interný
  limit `4.8 s`. Canonical fyzikálny raw nevznikol; immutable failure SHA je
  `5F7A23E612048073A5F7CDC166F945F0CFDC11BBCBF47984B839DDFA7FC57823`.
  Povolený je iba KMPC-069 successor s predimportovým single-thread
  BLAS/OpenMP pri nezmenenej fyzike a rovnakom limite; opakovanie runnera 312
  alebo samotné predĺženie času je zakázané.

# 313 / KMPC-069

- `313_script_KMPC_069_P5_3g7_C2_CDI_k0p005_support_07_09_single_thread.py`
  — `DO_NOT_RUN_AUDIT_TECHNICAL`; PF-082, aj predimportový single-thread
  backend prekročil interných `4.8 s`. Canonical raw nevznikol; failure SHA
  `480CA008458CFE1248BE49213F8506B5F47ACB8FAAA3BE1F14420CF316FA1E7D`.
  Povolený je iba hashovo viazaný dvojstupňový KMPC-070/071 checkpoint-resume
  nástupca; dlhší limit ani opakovanie runnera 313 nie sú povolené.

# 315 / KMPC-071

- `315_script_KMPC_071_P5_3g7_C2_CDI_k0p005_support_07_09_checkpoint_resume.py`
  — `DO_NOT_USE_PHYSICS`; PF-083, JSON `sort_keys=True` zmenil po resume
  insertion order `standard_state`, preto production contract odmietol inak
  numericky PASS audit. Immutable raw SHA je
  `B2A1F7D36FC440775E72E161E723F0687A57BC65ABC24A816401FB6955850DC5`.
  Povolený je iba KMPC-072 state-order successor s tým istým checkpointom;
  runner 315 sa neopakuje.

# 316 / KMPC-072

- `316_script_KMPC_072_P5_3g7_C2_CDI_k0p005_checkpoint_state_order_successor.py`
  — `DO_NOT_RUN_AUDIT_TECHNICAL`; PF-084, smoke mylne vyžadoval plný
  13-stavový kontrakt v 11-stavovom checkpoint `standard_state`. Audit sa
  nespustil a nevznikol raw. Povolený je iba KMPC-073 successor s
  phase-aware 11-state subset a 13-state combined fixture.

# 325 / KMPC-081

- `325_script_KMPC_081_P5_3g7_C2_BI_k0p15_high_precision_holdout_boundary.py`
  — `DO_NOT_RUN_AUDIT_TECHNICAL`; PF-086, stabilný C2 harness odmietol
  predregistrovaných 45 s ešte pred importom a solve. Povolený je iba runner
  326 / KMPC-082 s hashovaným high-precision harnessom; auditný modul ostáva
  nezmenený. Runner SHA `3C34EDD4...698CB7B`.

# 326 / KMPC-082

- `326_script_KMPC_082_P5_3g7_C2_BI_k0p15_high_precision_harness_successor.py`
  — `DO_NOT_RUN_AUDIT_TECHNICAL`; PF-087, CLI 45 s prešiel, ale vnútorný
  KMPC-057 deadline odmietol limit pred solve. Failure SHA `8B557EC2...3041DD`.
  Povolený je iba KMPC-083 s verzovaným internal-deadline overlayom.
