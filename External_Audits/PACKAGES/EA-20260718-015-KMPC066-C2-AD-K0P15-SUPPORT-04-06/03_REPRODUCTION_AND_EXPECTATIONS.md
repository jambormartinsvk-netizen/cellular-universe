# Reprodukcia — EA-015

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_ad_k0p15_support_04_06.py scripts/310_script_KMPC_066_P5_3g7_C2_AD_k0p15_support_04_06.py
python scripts/310_script_KMPC_066_P5_3g7_C2_AD_k0p15_support_04_06.py --max-runtime-seconds 4.8 --smoke
python scripts/310_script_KMPC_066_P5_3g7_C2_AD_k0p15_support_04_06.py --max-runtime-seconds 4.8 --atom --mode AD --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_066_P5_3G7_C2_AD_K0p15_SUPPORT_04_06.json
```

Očakávanie: `PASS_C2_AD_K0p15_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY`, všetky
brány PASS; F0/M3 tail `.01` `9.14145e-9/1.51953e-8`. Reference SHA
`81370874BCF25123565FBB117EDFEB4D51F12560CCC04BDC8CCDFC0DF8FDE816`.
Negatívne: missing KMPC-065 a mutated base musia skončiť exit 2.
