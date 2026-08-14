# Reprodukcia — EA-017

Každý runner spusti v **samostatnej čerstvej kópii** `REPRO`. Balík obsahuje
immutable raw 075–080; pred konkrétnym official behom odstráň iba jeho vlastný
cieľový JSON, ostatné nechaj ako hashované prerequisites. Runnery sa nesmú
reťaziť cez novovygenerované JSON, pretože `runtime_seconds` mení byteový SHA.

Príkazy pre jednotlivé izolované kópie:

```powershell
python -m py_compile scripts/320_script_KMPC_076_P5_3g7_C2_BI_k0p005_nominal.py scripts/321_script_KMPC_077_P5_3g7_C2_BI_k0p005_support_07_checkpoint.py scripts/322_script_KMPC_078_P5_3g7_C2_BI_k0p005_support_07_09_checkpoint_resume.py scripts/323_script_KMPC_079_P5_3g7_C2_BI_k0p15_nominal.py scripts/324_script_KMPC_080_P5_3g7_C2_BI_k0p15_same_matrix_refinement.py
python scripts/320_script_KMPC_076_P5_3g7_C2_BI_k0p005_nominal.py --max-runtime-seconds 4.8 --atom --mode BI --k-mpc 0.005 --output scripts/results/k_mpc_005/RUN_KMPC_076_P5_3G7_C2_BI_K0p005_NOMINAL.json
python scripts/321_script_KMPC_077_P5_3g7_C2_BI_k0p005_support_07_checkpoint.py --max-runtime-seconds 4.8 --atom --mode BI --k-mpc 0.005 --output scripts/results/k_mpc_005/RUN_KMPC_077_P5_3G7_C2_BI_K0p005_SUPPORT_07_ACCEPTED_CHECKPOINT.json
python scripts/322_script_KMPC_078_P5_3g7_C2_BI_k0p005_support_07_09_checkpoint_resume.py --max-runtime-seconds 4.8 --atom --mode BI --k-mpc 0.005 --output scripts/results/k_mpc_005/RUN_KMPC_078_P5_3G7_C2_BI_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json
python scripts/323_script_KMPC_079_P5_3g7_C2_BI_k0p15_nominal.py --max-runtime-seconds 4.8 --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_079_P5_3G7_C2_BI_K0p15_NOMINAL.json
python scripts/324_script_KMPC_080_P5_3g7_C2_BI_k0p15_same_matrix_refinement.py --max-runtime-seconds 4.8 --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_080_P5_3G7_C2_BI_K0p15_SAME_MATRIX_REFINEMENT.json
```

Očakávanie: KMPC-076 tail REVIEW; KMPC-077 iba complete checkpoint; KMPC-078
PASS BI/.005; KMPC-079 core REVIEW; KMPC-080 main driver PASS po troch
same-matrix corrections, ale `Einstein_0i[7]` holdout približne `3.02e-9`
ostáva REVIEW. Runtime/path polia smú meniť byteový SHA; všetky ostatné
fyzikálne a numerické polia musia mať field-level paritu.
