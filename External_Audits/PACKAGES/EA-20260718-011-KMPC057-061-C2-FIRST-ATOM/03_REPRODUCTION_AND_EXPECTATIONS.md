# Reprodukcia — EA-011

Z koreňa čerstvej kópie `REPRO/`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_atomic_runner_harness.py scripts/baseScripts/p5_general_synchronous/c2_fourier_coverage_v4_guard_semantics.py scripts/305_script_KMPC_061_P5_3g7_C2_Fourier_guard_semantics_successor.py
python scripts/305_script_KMPC_061_P5_3g7_C2_Fourier_guard_semantics_successor.py --help
python scripts/305_script_KMPC_061_P5_3g7_C2_Fourier_guard_semantics_successor.py --max-runtime-seconds 4.8 --smoke
python scripts/305_script_KMPC_061_P5_3g7_C2_Fourier_guard_semantics_successor.py --max-runtime-seconds 4.8 --atom --mode AD --k-mpc 0.005 --output scripts/results/k_mpc_005/RUN_KMPC_061_P5_3G7_C2_AD_K0p005_NOMINAL.json
python -c "import numpy,platform,sys; numpy.show_config(); print(sys.version); print(platform.platform()); print(platform.machine())"
```

Pred official auditom musia byť KMPC-061 success/failure/temp výstupy
neprítomné. Očakávanie:

```text
smoke passed       = true
V1 false checks    = BI, CDI
historical diff    = AD, CDI, BI
candidate          = REVIEW_C2_SUPPORT_EXTENSION_REQUIRED
M1/core/common     = true
S-C0/background    = true
tail               = false
overlay restored   = true
```

Referenčný SHA je
`0952AF08B1DE291D015F71396954F70EAE2F78A962E1EE1D3A08ECA48A1F5DCD`;
generated JSON dostane vlastný hash, pretože obsahuje runtime. V zahoditeľnej
kópii odstráň jeden C1 prerequisite; smoke musí skončiť fail-closed. V druhej
zahoditeľnej kópii zmeň jeden import; static hash guard musí skončiť
fail-closed. Ani negatívny test nesmie vytvoriť fyzikálny verdict.
