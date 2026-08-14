# Reprodukcia a očakávania — EA-016

Príkazy sa spúšťajú z koreňa `REPRO` v čerstvej pracovnej kópii:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_checkpointed_single_atom.py scripts/baseScripts/p5_general_synchronous/c2_checkpointed_single_atom_v3_phase_order.py scripts/baseScripts/p5_general_synchronous/c2_cdi_k0p15_same_matrix_refinement.py scripts/317_script_KMPC_073_P5_3g7_C2_CDI_k0p005_phase_aware_state_order_successor.py scripts/319_script_KMPC_075_P5_3g7_C2_CDI_k0p15_same_matrix_refinement.py
python scripts/317_script_KMPC_073_P5_3g7_C2_CDI_k0p005_phase_aware_state_order_successor.py --max-runtime-seconds 4.8 --smoke
python scripts/317_script_KMPC_073_P5_3g7_C2_CDI_k0p005_phase_aware_state_order_successor.py --max-runtime-seconds 4.8 --atom --mode CDI --k-mpc 0.005 --output scripts/results/k_mpc_005/RUN_KMPC_073_P5_3G7_C2_CDI_K0p005_SUPPORT_07_09_PHASE_ORDER_SUCCESSOR.json
python scripts/319_script_KMPC_075_P5_3g7_C2_CDI_k0p15_same_matrix_refinement.py --max-runtime-seconds 4.8 --smoke
python scripts/319_script_KMPC_075_P5_3g7_C2_CDI_k0p15_same_matrix_refinement.py --max-runtime-seconds 4.8 --atom --mode CDI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_075_P5_3G7_C2_CDI_K0p15_SAME_MATRIX_REFINEMENT.json
```

Očakávania:

- KMPC-073 candidate
  `PASS_C2_CDI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY`, reference SHA
  `B7B2B7231E20D90D7EA71F1934B795296B7B0C2772148988C0FCFB2CF96E8498`;
- KMPC-075 candidate
  `PASS_C2_CDI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`, reference SHA
  `19F5F0B38CFE62C6E2ECA277EE5F959D866967027C5AF721CF4B2E1A30B999B9`;
- všetky M1/core/common/tail/background brány PASS;
- refinement baseline maximum `3.8441418852221534e-10`, final
  `1.1149921347627513e-16`, `selection_rule_pass=true`.

Referenčné SHA identifikujú zapečatené projektové raw, nie povinnú byteovú
rovnosť nového behu. JSON obsahuje meraný `runtime_seconds` a KMPC-075 aj
lokálnu absolútnu `frozen_algebra_source`; tieto polia sa pri čerstvej kópii
legitímne menia. T2 PASS preto vyžaduje rovnosť všetkých fyzikálnych,
numerických, prahových, kandidátskych a provenance polí po deklarovanom
vylúčení iba runtime/path polí. Každý ďalší rozdiel je `REVIEW`.

Negatívna kontrola: chýbajúci checkpoint KMPC-070 alebo zmenený refinement
base musí skončiť exit code `2` bez generated fyzikálneho raw. Cross-platform
odlišný exact JSON hash sa nesmie potichu povýšiť; auditor uvedie field-level
paritu a označí odchýlku.
