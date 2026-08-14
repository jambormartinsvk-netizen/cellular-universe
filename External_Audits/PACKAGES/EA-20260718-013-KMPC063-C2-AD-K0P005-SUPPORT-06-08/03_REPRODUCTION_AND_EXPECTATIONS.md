# Reprodukcia — EA-013

Z koreňa čerstvej `REPRO/`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_atomic_runner_harness.py scripts/baseScripts/p5_general_synchronous/c2_ad_k0p005_support_04_06.py scripts/baseScripts/p5_general_synchronous/c2_ad_k0p005_support_06_08.py scripts/307_script_KMPC_063_P5_3g7_C2_AD_k0p005_support_06_08.py
python scripts/307_script_KMPC_063_P5_3g7_C2_AD_k0p005_support_06_08.py --help
python scripts/307_script_KMPC_063_P5_3g7_C2_AD_k0p005_support_06_08.py --max-runtime-seconds 4.8 --smoke
python scripts/307_script_KMPC_063_P5_3g7_C2_AD_k0p005_support_06_08.py --max-runtime-seconds 4.8 --atom --mode AD --k-mpc 0.005 --output scripts/results/k_mpc_005/RUN_KMPC_063_P5_3G7_C2_AD_K0p005_SUPPORT_06_08.json
```

Očakávanie: candidate
`PASS_C2_AD_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY`; M1/core/common/
background/owner restore aj tail overall PASS. Oba tail rady musia prejsť
na oboch `z`; referenčné maximum na `.01` je F0 `1.8269976120859345e-9`
a M3 `5.074642949718514e-9`. Reference SHA
`CB0CEA5DD92BF85F0F0066FAD8DE77D5F8247B02B864FACF92FA374E0FBC85BD`.
Generated hash sa môže líšiť iba runtime poľom.

Negatívne: v zahoditeľnej kópii odstráň KMPC-062 prerequisite a osobitne
mutuj base KMPC-063; oba smoke behy musia fail-closed exit `2` bez
fyzikálneho verdiktu.
