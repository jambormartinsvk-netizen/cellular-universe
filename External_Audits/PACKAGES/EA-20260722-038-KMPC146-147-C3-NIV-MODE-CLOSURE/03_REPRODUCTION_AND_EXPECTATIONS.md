# Reprodukcia EA-038 a corrected field parity

Pracujte v novej dočasnej kópii `REPRO/`. Z jej koreňa spustite oddelene:

```powershell
python -c "from pathlib import Path; p=Path(r'scripts\391_script_KMPC_147_P5_3g7_C3_NIV_k0p15_read_only_f0_parity_correction.py'); compile(p.read_text(encoding='utf-8'), str(p), 'exec'); print('COMPILE_PASS')"

python scripts\391_script_KMPC_147_P5_3g7_C3_NIV_k0p15_read_only_f0_parity_correction.py --help

python scripts\391_script_KMPC_147_P5_3g7_C3_NIV_k0p15_read_only_f0_parity_correction.py --smoke --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8

python scripts\391_script_KMPC_147_P5_3g7_C3_NIV_k0p15_read_only_f0_parity_correction.py --audit --mode NIV --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8
```

Očakávané exit codes sú `0/0/0/0`. Smoke má `physics_executed=false`,
všetkých `13/13` checks true a `workers=solvers=physics=0`. Official musí
vytvoriť generated JSON:

`scripts/results/k_mpc_005/RUN_KMPC_147_P5_3G7_C3_NIV_K0p15_READ_ONLY_F0_PARITY_CORRECTION.json`

Očakávaný candidate je
`PASS_C3_NIV_K0P15_MULTI_RANK_PARITY_CORRECTION_CANDIDATE_ONLY` a
`pair_pass=true`.

## Corrected field parity

Pred exact rekurzívnym diffom generated verzus `EVIDENCE/007` sa smie
odobrať iba:

`read_only_f0_parity_correction.runtime_seconds`.

Po odobratí musí zostať `0` rozdielov. Nijaký iný runtime, fyzikálne číslo,
identity, brána, prah, provenance alebo hash sa normalizovať nesmie.

Generated raw musí mať:

- `read_only_f0_parity_correction.pass=true`;
- identické protected SHA pred/po
  `9F76DD48A83DEC2AB825A0E1B2B0D22B443F5965868BCAAFD46812033E360A0A`;
- štyri corrected F0 parity checks true;
- všetky štyri refinement row pass true;
- operation counts `0/0/0`;
- zachovaný source runtime `2.905999999959022`.

## Nezávislá protected projekcia

Z KMPC-146 source a generated KMPC-147 odstráňte na oboch stranách iba
`run_id`, `test`, candidate, `pair_pass`, `same_matrix_multi_rank_pass`;
z každého zo štyroch refinement rows odstráňte iba
`f0_exact_predecessor_parity` a row `pass`; z outputu navyše celý nový
`read_only_f0_parity_correction` blok a rovnomenný process-architecture
blok. Zvyšok musí byť exact zhodný. Každé ďalšie vylúčenie je odchýlka.

## Negatívne guardy

V dvoch samostatných fresh kópiách odstráňte vždy iba jeden súbor:

- `scripts/results/k_mpc_005/RUN_KMPC_146_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR_MULTI_RANK_REFINEMENT.json`;
- `scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR.json`.

V každej kópii spustite official s limitom `10 s`. Očakávanie: nonzero
exit, presná missing/hash príčina, žiadny success raw a žiadny fyzikálny
verdikt. Pôvodný package sa nesmie meniť.

## KMPC-146 T1 hranica

T1 source/raw audit musí overiť tvrdenia auditu 239, ale z EA-038 samotného
nesmie hlásiť fresh KMPC-146 T2. Ak auditor dobrovoľne skladá runtime z
iného balíka, musí to označiť ako `DECLARED_DEVIATION` a oddeliť od
oficiálneho EA-038 výsledku.
