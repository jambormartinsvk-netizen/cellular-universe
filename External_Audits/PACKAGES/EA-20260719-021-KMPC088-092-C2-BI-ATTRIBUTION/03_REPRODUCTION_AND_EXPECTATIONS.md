# Reprodukcia — EA-021

Z koreňa čerstvej kópie `REPRO`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_coefficient_attribution.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_coefficient_attribution_v2_serialization_bound.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_coefficient_attribution_v3_fixture.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_coefficient_attribution_v4_float_product.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_coefficient_attribution_v5_nested_owner.py scripts/336_script_KMPC_092_P5_3g7_C2_BI_k0p15_attribution_nested_owner_successor.py
python scripts/336_script_KMPC_092_P5_3g7_C2_BI_k0p15_attribution_nested_owner_successor.py --max-runtime-seconds 4.8 --smoke
python scripts/336_script_KMPC_092_P5_3g7_C2_BI_k0p15_attribution_nested_owner_successor.py --max-runtime-seconds 45 --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_092_P5_3G7_C2_BI_K0p15_COEFFICIENT_ATTRIBUTION_NESTED_OWNER_SUCCESSOR.json
```

Pred official behom musí byť cieľový KMPC-092 JSON neprítomný. Dodané
immutable KMPC-087, failure KMPC-088/090 a ostatné prerequisite JSON ostávajú
na mieste.

Očakávanie: exit code 0; candidate
`REVIEW_C2_BI_K0p15_UPSTREAM_ATTRIBUTION_COMPLETE`; attribution boundary
PASS; 73 členov; cancellation factor `8.907636904e8`; všetky owner a
serialization checks true. Byteový SHA generated JSON sa môže líšiť iba
runtime/path poliami; numerické a kontraktové polia musia mať field-level
paritu s Evidence 017.
