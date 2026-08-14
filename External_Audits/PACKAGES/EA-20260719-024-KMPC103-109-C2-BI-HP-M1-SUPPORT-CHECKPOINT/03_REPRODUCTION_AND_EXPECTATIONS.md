# Reprodukcia — EA-024

Každú vetvu spusti v samostatnej čerstvej kópii adresára `REPRO`. Vnútorný
vedecký deadline KMPC-108 je `45 s`; vonkajší procesný limit musí mať aspoň
ďalších 45 s na import, publish a čisté ukončenie procesu.

## Vetva A — KMPC-108 checkpoint

Odstráň iba:

`scripts/results/k_mpc_005/RUN_KMPC_108_P5_3G7_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_JSON_SUCCESSOR.json`

Potom spusti z rootu čerstvej kópie:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v13_support_checkpoint.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v14_checkpoint_identity_successor.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v15_checkpoint_json_successor.py scripts/352_script_KMPC_108_P5_3g7_C2_BI_k0p15_HP_M1_support_checkpoint_JSON_successor.py
python scripts/352_script_KMPC_108_P5_3g7_C2_BI_k0p15_HP_M1_support_checkpoint_JSON_successor.py --help
python scripts/352_script_KMPC_108_P5_3g7_C2_BI_k0p15_HP_M1_support_checkpoint_JSON_successor.py --smoke --max-runtime-seconds 4.8
python scripts/352_script_KMPC_108_P5_3g7_C2_BI_k0p15_HP_M1_support_checkpoint_JSON_successor.py --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_108_P5_3G7_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_JSON_SUCCESSOR.json --max-runtime-seconds 45.0
```

Všetky príkazy majú exit `0`. Generated raw musí mať field-level paritu s
Evidence 059 po odrátaní všetkých meraných polí `runtime_seconds` a po
normalizácii jediného environmentálneho prefixu v `frozen_algebra_source`;
suffix musí zostať presne
`scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight.py`.

Očakávané jadro:

- candidate `REVIEW_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_UNCLOSED`;
- raw false checks presne `audit_support_complete,pre_exact_core_complete`;
- audit false checks presne `M3_driver`;
- M1/accepted/common/tail/S-C0/background a audit holdout PASS;
- serialized-state SHA `402B42E1...5EBF40`;
- šesť `mpf` ciest, C2 candidate false.

## Vetva B — KMPC-109 read-only receipt

V druhej čerstvej kópii ponechaj referenčný KMPC-108 raw a odstráň iba:

`scripts/results/k_mpc_005/RUN_KMPC_109_P5_3G7_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_READ_ONLY_RECEIPT.json`

Potom spusti:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v16_checkpoint_receipt.py scripts/353_script_KMPC_109_P5_3g7_C2_BI_k0p15_HP_M1_support_checkpoint_read_only_receipt.py
python scripts/353_script_KMPC_109_P5_3g7_C2_BI_k0p15_HP_M1_support_checkpoint_read_only_receipt.py --help
python scripts/353_script_KMPC_109_P5_3g7_C2_BI_k0p15_HP_M1_support_checkpoint_read_only_receipt.py --smoke --max-runtime-seconds 4.8
python scripts/353_script_KMPC_109_P5_3g7_C2_BI_k0p15_HP_M1_support_checkpoint_read_only_receipt.py --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_109_P5_3G7_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_READ_ONLY_RECEIPT.json --max-runtime-seconds 4.8
```

Všetky príkazy majú exit `0`. Generated receipt musí mať field-level paritu
s Evidence 060 po odrátaní iba `runtime_seconds`, candidate
`REVIEW_C2_BI_K0p15_HP_M1_CHECKPOINT_RECEIPT_EXACT_RESUME_ALLOWED` a
`pass_c2_atom_candidate=false`.
