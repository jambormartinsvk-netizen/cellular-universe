# Reprodukcia primárneho K_MPC background auditu

**Interné limity:** runner 224 najviac `10 s`; runnery 234/235 po `5 s` na
integračný úsek  
**Externý limit:** `10 s` na každý proces  
**Prostredie pôvodných behov:** Python 3.11; runner 224 vyžaduje SymPy.
Presné pôvodné verzie neboli uložené — auditor zaznamená svoje.

Spúšťať z koreňa čerstvej kópie balíka. Adresár výsledkov musí byť bez
generated JSON; reference výsledky sú iba v `EVIDENCE/`.

## R1 — symbolická univerzálnosť

```bash
timeout 10s python REPRO/scripts/224_script_A2_K4_G8_FULL_background_universality_audit.py --smoke --max-runtime-seconds 10
timeout 10s python REPRO/scripts/224_script_A2_K4_G8_FULL_background_universality_audit.py --max-runtime-seconds 10 --output REPRO/scripts/results/k_mpc_005/RUN_FULL_002_REPRO.json
```

Očakáva sa:

- raw verdict `STOP_BACKGROUND_K_DEPENDENCE_UNRESOLVED`;
- `mu*z` a `g2*z^2` sú `k`-independent;
- fuel je homogénny stupňa `p` v `k` a `dfuel/dk != 0` pre `p=3.93109`;
- druhý proces končí **exit 1 zámerne**, pretože runner mapuje nájdený STOP
  na procesový exit 1. Výstupný JSON musí existovať. Exit 1 bez správneho
  JSON je technicky neuzavreté.

## R2 — odvodenie `A_f` zo zmrazeného A1

```bash
timeout 10s python REPRO/scripts/234_script_KMPC_001_A1_frozen_background_Af_audit.py --x-min -18 --deadline-seconds 5 --output REPRO/scripts/results/k_mpc_005/RUN_KMPC_001_AF_REPRO.json
```

Očakáva sa exit 0, `lambda=0.15`, `delta=0.02297`,
`A_f=7809.270101963506` na najjemnejšom kroku a medium/fine rozdiel
približne `5.34e-13`. Tento výsledok znamená iba „bez nového nezávislého
fitu pri zmrazenom A1 closure“.

## R3 — exact-A1 verzus skrátený K7

```bash
timeout 10s python REPRO/scripts/235_script_KMPC_002_full_A1_vs_truncated_K7_background.py --af-json REPRO/scripts/results/k_mpc_005/RUN_KMPC_001_AF_REPRO.json --x-min -18 --deadline-seconds 5 --output REPRO/scripts/results/k_mpc_005/RUN_KMPC_002_P3_REPRO.json
```

Očakáva sa exit 0 a raw verdict
`STOP_K7_TRUNCATED_SERIES_IS_NOT_FULL_BACKGROUND`, prvý nulový prechod
`a≈0.70895788`, pri `a=1` približne `D_A1=10470.7875` a
`D_K7,trunc=-24131.5578`.

## Vyhodnotenie odchýlok

- R1–R3 reprodukované v rozsahu tolerancií: pôvodný audit sa posilní na T2.
- Numerická malá odchýlka bez zmeny brán: uviesť platformu a rozsah, verdict
  automaticky nemení.
- Zmena znamienka, ranku, algebraických núl alebo vetvenia: formula/platform
  mismatch vyžadujúci lokalizáciu.
- Timeout/exception/chýbajúci import: `TECHNICAL_STOP`, fyzika `NOT_RUN`.
