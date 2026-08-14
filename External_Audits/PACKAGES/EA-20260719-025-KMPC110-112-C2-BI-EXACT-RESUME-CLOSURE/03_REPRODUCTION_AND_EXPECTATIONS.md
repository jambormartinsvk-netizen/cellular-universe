# Reprodukcia — EA-025

Pracuj v samostatnej čerstvej kópii adresára `REPRO`. Vnútorný vedecký
deadline je `45 s`; vonkajší procesný limit musí byť aspoň `120 s`.

## Negatívny dependency guard

V pomocnej kópii dočasne odober:

`scripts/results/k_mpc_005/RUN_KMPC_111_P5_3G7_C2_BI_K0p15_HP_M1_CHECKPOINT_EXACT_RESUME_ORDER_SUCCESSOR_TECHNICAL_FAILURE.json`

Spusť smoke KMPC-112. Očakáva sa nonzero exit v `static_hash_guard`, bez
fyzikálneho volania a bez success raw. Pomocnú kópiu potom zahoď; súbor
neobnovuj ručne v tej istej vetve.

## Oficiálna vetva KMPC-112

V novej čerstvej kópii `REPRO` spusti z jej rootu:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v17_exact_resume.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v18_exact_resume_order_successor.py scripts/baseScripts/p5_general_synchronous/c2_bi_k0p15_high_precision_m1_reassembly_v19_exact_resume_json_parity_successor.py scripts/356_script_KMPC_112_P5_3g7_C2_BI_k0p15_HP_M1_checkpoint_exact_resume_JSON_parity_successor.py
python scripts/356_script_KMPC_112_P5_3g7_C2_BI_k0p15_HP_M1_checkpoint_exact_resume_JSON_parity_successor.py --help
python scripts/356_script_KMPC_112_P5_3g7_C2_BI_k0p15_HP_M1_checkpoint_exact_resume_JSON_parity_successor.py --smoke --max-runtime-seconds 4.8
python scripts/356_script_KMPC_112_P5_3g7_C2_BI_k0p15_HP_M1_checkpoint_exact_resume_JSON_parity_successor.py --atom --mode BI --k-mpc 0.15 --output scripts/results/k_mpc_005/RUN_KMPC_112_P5_3G7_C2_BI_K0p15_HP_M1_CHECKPOINT_EXACT_RESUME_JSON_PARITY_SUCCESSOR.json --max-runtime-seconds 45.0
```

Všetky štyri príkazy majú exit `0`. Generated raw sa porovná s Evidence
018 po rekurzívnom odrátaní iba polí nazvaných `runtime_seconds`.

Očakávané jadro:

- candidate
  `PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY`;
- technical a physics false množiny prázdne;
- pôvodná audit false množina presne `M3_driver`;
- source count `48`, checkpoint/audit parity a 13-state merge PASS;
- exact driver/holdout PASS, jeden solve, holdout rows fit `0`;
- `pass_c2_atom_candidate=true`, C2 dopad iba po internom audite 179.

Ak sa oficiálny runner obíde priamym volaním modulu alebo zmenou prahu,
výsledok označ `DECLARED_DEVIATION` a neudeľ T2 deklarovanej vetve.
