# Reprodukcia EA-037 a corrected field parity

Pracujte v novej dočasnej kópii `REPRO/`. Z jej koreňa spustite oddelene:

```powershell
python -c "from pathlib import Path; p=Path(r'scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py'); compile(p.read_text(encoding='utf-8'), str(p), 'exec'); print('COMPILE_PASS')"

python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --help

python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --smoke --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8

python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --audit --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8
```

Očakávané exit codes sú `0/0/0/0`. Smoke má `4/4`, bez fyziky a rawu.
Official musí pri vonkajšom limite `20 s` vytvoriť:

`scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR.json`

Očakávaný candidate je `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED`,
`pair_pass=false`; REVIEW je úspešná reprodukcia frozen výsledku, nie
technický failure.

## Corrected field parity

Vo generated a reference JSON sa pred exact rekurzívnym diffom smú odobrať
iba tieto šesť wall-time hodnoty:

1. `runtime_seconds`;
2. `variants.gamma0.support_worker_runtime_seconds.accepted`;
3. `variants.gamma0.support_worker_runtime_seconds.audit`;
4. `variants.af0.support_worker_runtime_seconds.accepted`;
5. `variants.af0.support_worker_runtime_seconds.audit`;
6. `frozen_B1_left_null_Bianchi.runtime_seconds`.

Pole `frozen_B1_left_null_Bianchi.frozen_algebra_source` sa neodstraňuje.
Normalizuje sa iba jeho absolútny koreň. V oboch rawoch musí cesta končiť
presne na
`scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight.py` a
`frozen_algebra_sha256` musí byť exact
`62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D`.
Po tejto jednej path-root normalizácii a odobratí šiestich runtime hodnôt
musia zostať `0` rozdielov. Nijaké fyzikálne číslo, identity, brána, prah
ani hash sa normalizovať nesmie.

## Negatívne guardy

V samostatných fresh kópiách odstráňte vždy iba jeden súbor:

- `scripts/88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py`;
- `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/26_P5_3G7_M1_STANDARD_METRIC_SOURCE_MAP_SK.md`.

V každej kópii spustite official s vonkajším limitom `20 s`. Očakávanie:
nonzero exit, technical failure pred fyzikou, missing/hash príčina, žiadny
success raw. Pôvodný package sa nesmie meniť.
