# Reprodukcia — EA-022

## Vetva A — standalone KMPC-099

V prvej čerstvej kópii `REPRO` odstráň iba cieľ
`scripts/results/k_mpc_005/RUN_KMPC_099_P5_3G7_C2_BI_K0p15_HP_M1_STANDALONE_MATRIX_PROVENANCE.json`.

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v2_attribution_owner.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v3_column_equilibrated.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v4_scale_fixture.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v5_matrix_provenance.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v6_combined_register.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v7_standalone_provenance.py scripts/343_script_KMPC_099_P5_3g7_C2_BI_k0p15_HP_M1_standalone_matrix_provenance.py
python scripts/343_script_KMPC_099_P5_3g7_C2_BI_k0p15_HP_M1_standalone_matrix_provenance.py --max-runtime-seconds 4.8 --smoke
python scripts/343_script_KMPC_099_P5_3g7_C2_BI_k0p15_HP_M1_standalone_matrix_provenance.py --max-runtime-seconds 45 --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_099_P5_3G7_C2_BI_K0p15_HP_M1_STANDALONE_MATRIX_PROVENANCE.json
```

Compile a smoke majú exit 0. Official má deklarovaný exit 2 až po exclusive
publish pre legacy terminal-summary `KeyError: atom_id`. Generated JSON musí
existovať, mať completed diagnostic contract a field-level paritu s Evidence
022 okrem `runtime_seconds`.

## Vetva B — read-only KMPC-100 receipt

V druhej čerstvej kópii ponechaj dodaný immutable KMPC-099 a odstráň iba
cieľ KMPC-100.

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v8_publication_receipt.py scripts/344_script_KMPC_100_P5_3g7_C2_BI_k0p15_HP_M1_publication_receipt.py
python scripts/344_script_KMPC_100_P5_3g7_C2_BI_k0p15_HP_M1_publication_receipt.py --max-runtime-seconds 4.8 --smoke
python scripts/344_script_KMPC_100_P5_3g7_C2_BI_k0p15_HP_M1_publication_receipt.py --max-runtime-seconds 45 --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_100_P5_3G7_C2_BI_K0p15_HP_M1_PUBLICATION_RECEIPT.json
```

Všetky tri príkazy majú exit 0. Generated receipt má byť byteovo zhodný s
Evidence 023 a mať SHA
`2581BC157F0CBA08D91654A9BCE9976D93429D9DB6AA0FA2AE4765F05AD9CC1A`.
