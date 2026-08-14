# Reprodukcia — EA-007

Z koreňa čerstvej kópie `REPRO/`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/nid_support_step2.py
python -m py_compile scripts/292_script_KMPC_048_P5_3g7_NID_support_step2_05_07.py
python scripts/292_script_KMPC_048_P5_3g7_NID_support_step2_05_07.py --help
python scripts/292_script_KMPC_048_P5_3g7_NID_support_step2_05_07.py --max-runtime-seconds 4.8 --smoke
python scripts/292_script_KMPC_048_P5_3g7_NID_support_step2_05_07.py --max-runtime-seconds 4.8 --audit --output scripts/results/k_mpc_005/RUN_KMPC_048_P5_3G7_NID_SUPPORT_STEP_2_05_07.json
```

Pred auditom musia byť success/failure/temp outputy neprítomné. Očakávanie:

```text
candidate       = REVIEW_NID_SUPPORT_STEP_2_CORE_GATE_UNCLOSED
regression_pass = true
core_pass       = false
common_pass     = true
tail_pass       = true
```

Reference SHA je
`B4F320F5D850DCF78FD9EC2A5BDDEBDA87D590DA2988CF505FA7D5B25B49BF32`.
Generated JSON dostane vlastný hash. V zahoditeľnej druhej kópii odstráňte
KMPC-047 prerequisite a overte fail-closed smoke bez fyzikálneho verdictu.

