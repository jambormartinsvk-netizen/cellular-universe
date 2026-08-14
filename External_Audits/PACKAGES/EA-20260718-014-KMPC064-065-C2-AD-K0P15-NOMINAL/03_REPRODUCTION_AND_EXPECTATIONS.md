# Reprodukcia — EA-014

Z koreňa čerstvej `REPRO/`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_ad_k0p15_nominal.py scripts/baseScripts/p5_general_synchronous/c2_ad_k0p15_nominal_v2_smoke_scope.py scripts/309_script_KMPC_065_P5_3g7_C2_AD_k0p15_smoke_scope_successor.py
python scripts/309_script_KMPC_065_P5_3g7_C2_AD_k0p15_smoke_scope_successor.py --help
python scripts/309_script_KMPC_065_P5_3g7_C2_AD_k0p15_smoke_scope_successor.py --max-runtime-seconds 4.8 --smoke
python scripts/309_script_KMPC_065_P5_3g7_C2_AD_k0p15_smoke_scope_successor.py --max-runtime-seconds 4.8 --atom --mode AD --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_065_P5_3G7_C2_AD_K0p15_NOMINAL.json
```

Očakávanie: candidate `REVIEW_C2_AD_K0p15_SUPPORT_04_06_REQUIRED`;
M1/core/common/background/owner restore PASS; tail overall FAIL na oboch
`z`. Referenčné hodnoty: F0 `9.36649e-6`, `9.45894e-4`; M3
`1.09234e-5`, `1.09425e-3`. Reference SHA
`987E467EA2F36EA8F061F665A33AE1F6DC9AB6E2EFE9FB710E23CE0C50171636`.
Generated hash sa môže líšiť iba runtime poľom.

Negatívne: v zahoditeľnej kópii odstráň KMPC-063 prerequisite a osobitne
mutuj V2 base; oba smoke behy musia fail-closed exit `2` bez fyzikálneho
verdiktu.
