# Reprodukcia — EA-018

Z koreňa čerstvej kópie `REPRO`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_holdout.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_holdout_v2_deadline.py scripts/baseScripts/p5_general_synchronous/c2_high_precision_runner_harness.py scripts/327_script_KMPC_083_P5_3g7_C2_BI_k0p15_internal_deadline_successor.py
python scripts/327_script_KMPC_083_P5_3g7_C2_BI_k0p15_internal_deadline_successor.py --max-runtime-seconds 4.8 --smoke
python scripts/327_script_KMPC_083_P5_3g7_C2_BI_k0p15_internal_deadline_successor.py --max-runtime-seconds 45 --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_083_P5_3G7_C2_BI_K0p15_HIGH_PRECISION_HOLDOUT_BOUNDARY.json
```

Očakávanie: exit 0; candidate
`REVIEW_C2_BI_K0p15_EXACT_ASSEMBLY_REQUIRED`; jeden 80-dps solve; driver
`9.8186e-82`, holdout `3.019756782e-9`, holdout non-fit. Byteový SHA sa môže
líšiť iba runtime/path poliami; ostatné polia vyžadujú field-level paritu.
