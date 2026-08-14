# Reprodukcia — EA-020

Z koreňa čerstvej kópie `REPRO`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_driver_assembly.py scripts/331_script_KMPC_087_P5_3g7_C2_BI_k0p15_high_precision_driver_assembly.py
python scripts/331_script_KMPC_087_P5_3g7_C2_BI_k0p15_high_precision_driver_assembly.py --max-runtime-seconds 4.8 --smoke
python scripts/331_script_KMPC_087_P5_3g7_C2_BI_k0p15_high_precision_driver_assembly.py --max-runtime-seconds 45 --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_087_P5_3G7_C2_BI_K0p15_HIGH_PRECISION_DRIVER_ASSEMBLY.json
```

Pred official behom musí byť cieľový KMPC-087 JSON neprítomný. Dodané
immutable KMPC-083, KMPC-086 a ostatné prerequisite JSON zostávajú na mieste.

Očakávanie: exit code 0; candidate
`REVIEW_C2_BI_K0p15_UPSTREAM_COEFFICIENT_PRECISION_REQUIRED`; baseline SHA
`FE5E5A7C...127240F`; exact-driver SHA `CEBB46C4...43EF2`; driver
`8.720279045e-82`; holdout SHA `2DE8C982...06E2DE`; `Einstein_0i[7] =
3.019756577618421e-9`; presne dva HP solve a holdout non-fit. Byteový SHA
generated JSON sa môže líšiť iba runtime/path poliami; numerické a fyzikálne
polia musia mať field-level paritu s Evidence 021.
