# Reprodukcia — EA-023

Každú vetvu spusti v samostatnej čerstvej kópii adresára `REPRO`.

## Vetva A — PF-104 output-path guard

Odstráň iba:

`scripts/results/k_mpc_005/RUN_KMPC_101_P5_3G7_C2_BI_K0p15_NATIVE_HP_M1_CPQR_TECHNICAL_FAILURE.json`

Potom z rootu čerstvej kópie spusti presne pôvodný chybný official príkaz:

```powershell
python scripts/345_script_KMPC_101_P5_3g7_C2_BI_k0p15_native_HP_M1_CPQR.py --atom --mode BI --k-mpc 0.15 --output RUN_KMPC_101_P5_3G7_C2_BI_K0p15_NATIVE_HP_M1_CPQR.json --max-runtime-seconds 45.0
```

Očakáva sa exit `2`, phase `guarded_import`, message
`output path differs from canonical KMPC-101 target` a immutable failure SHA
`378A4FC7180E01FD89AF58CA803D3FBDD058DED6AA57AF38E1D1EB0B53A119CA`.
Táto vetva nesmie vykonať M1 assembly ani production CPQR.

## Vetva B — KMPC-102 vecný CPQR

Odstráň iba:

`scripts/results/k_mpc_005/RUN_KMPC_102_P5_3G7_C2_BI_K0p15_NATIVE_HP_M1_CPQR_ROUTING_SUCCESSOR.json`

Potom spusti:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v9_native_cpqr.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v10_cpqr_routing_successor.py scripts/346_script_KMPC_102_P5_3g7_C2_BI_k0p15_native_HP_M1_CPQR_routing_successor.py
python scripts/346_script_KMPC_102_P5_3g7_C2_BI_k0p15_native_HP_M1_CPQR_routing_successor.py --help
python scripts/346_script_KMPC_102_P5_3g7_C2_BI_k0p15_native_HP_M1_CPQR_routing_successor.py --smoke --max-runtime-seconds 4.8
python scripts/346_script_KMPC_102_P5_3g7_C2_BI_k0p15_native_HP_M1_CPQR_routing_successor.py --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_102_P5_3G7_C2_BI_K0p15_NATIVE_HP_M1_CPQR_ROUTING_SUCCESSOR.json --max-runtime-seconds 45.0
```

Všetky štyri príkazy majú exit `0`. Generated JSON musí mať field-level
paritu s Evidence 044 po odrátaní iba `runtime_seconds`. Referenčný raw SHA je
`49187BB85B8C59559A23EF6741DFB64F0015C2F0CC458D5C9D284FF2CECDE0CB`.

## Očakávané jadro výsledku

- candidate `REVIEW_C2_BI_K0p15_NATIVE_HP_M1_CPQR_COMPLETE`;
- diagnostic contract true;
- rank `98/98`;
- jeden native/authoritative HP-M1 solve;
- všetky tri numerické checks true;
- raw M1 driver-and-holdout boundary true;
- physics role `DIAGNOSTIC_ONLY`, C2 candidate false;
- score/release/prediction/Zenodo effect none.
