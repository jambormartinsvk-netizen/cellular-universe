# Reprodukcia — EA-019

Z koreňa čerstvej kópie `REPRO`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_holdout_assembly.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_holdout_assembly_v2_hash_owner.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_holdout_assembly_v3_fixture.py scripts/330_script_KMPC_086_P5_3g7_C2_BI_k0p15_assembly_fixture_successor.py
python scripts/330_script_KMPC_086_P5_3g7_C2_BI_k0p15_assembly_fixture_successor.py --max-runtime-seconds 4.8 --smoke
python scripts/330_script_KMPC_086_P5_3g7_C2_BI_k0p15_assembly_fixture_successor.py --max-runtime-seconds 45 --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_086_P5_3G7_C2_BI_K0p15_HP_HOLDOUT_ASSEMBLY_FIXTURE_SUCCESSOR.json
```

Pred official behom musí byť cieľový KMPC-086 JSON neprítomný. Dodané
immutable KMPC-083 a ostatné prerequisite JSON zostávajú na mieste.

Očakávanie: exit code 0; candidate
`REVIEW_C2_BI_K0p15_EXACT_DRIVER_ASSEMBLY_REQUIRED`; jeden 80-dps solve;
driver SHA `FE5E5A7C...127240F`; holdout SHA `2DE8C982...06E2DE`;
`Einstein_0i[7] = 3.0197567116259885e-9`; holdout non-fit; ostatné brány s
HP replacementom PASS. Byteový SHA generated JSON sa môže líšiť iba
runtime/path poliami; numerické a fyzikálne polia musia mať field-level
paritu s Evidence 011.
