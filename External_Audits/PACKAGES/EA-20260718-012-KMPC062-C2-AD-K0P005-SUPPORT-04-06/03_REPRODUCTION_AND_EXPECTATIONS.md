# Reprodukcia — EA-012

Z koreňa čerstvej `REPRO/`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_atomic_runner_harness.py scripts/baseScripts/p5_general_synchronous/c2_ad_k0p005_support_04_06.py scripts/306_script_KMPC_062_P5_3g7_C2_AD_k0p005_support_04_06.py
python scripts/306_script_KMPC_062_P5_3g7_C2_AD_k0p005_support_04_06.py --help
python scripts/306_script_KMPC_062_P5_3g7_C2_AD_k0p005_support_04_06.py --max-runtime-seconds 4.8 --smoke
python scripts/306_script_KMPC_062_P5_3g7_C2_AD_k0p005_support_04_06.py --max-runtime-seconds 4.8 --atom --mode AD --k-mpc 0.005 --output scripts/results/k_mpc_005/RUN_KMPC_062_P5_3G7_C2_AD_K0p005_SUPPORT_04_06.json
```

Očakávanie: candidate
`REVIEW_C2_AD_K0p005_FURTHER_SUPPORT_EXTENSION_REQUIRED`; M1/core/common/
background/owner restore PASS; tail overall FAIL, pričom oba `z=1e-4`
riady PASS a oba `.01` riady FAIL. Reference SHA
`640057CB6AC3F059988D6BD6C0CBE65ABAC1712F18961A2FEAFA5E1341EA6760`.
Generated hash sa môže líšiť iba runtime poľom.

Negatívne: v zahoditeľnej kópii odstráň KMPC-061 prerequisite a osobitne
mutuj base; oba smoke behy musia fail-closed exit `2` bez fyzikálneho verdiktu.
