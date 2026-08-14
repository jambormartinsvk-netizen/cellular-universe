# Q22a-K1 — výsledok auditu efektívneho A1 ledgeru

**Verdikt:** `BASELINE_EFFECTIVE_LEDGER_PASS_NOT_MICRO_SEQUENCE_DECISION`  
**Skóre:** `bez fyzikálneho skóre`  
**Skript a príloha:** `scripts/255_script_Q22A_K1_effective_ledger_audit.py`,
`scripts/results/q22a/RUN_Q22A_001_K1_EFFECTIVE_LEDGER_AUDIT.json`.

## Výsledok

Audit prešiel všetky štyri predregistrované kontroly. Pre
`Gamma=lambda/E` platí presne

```text
Q_F = -Gamma rho_F
Q_C = +Gamma rho_F
Q_R = 0
Q_F + Q_C + Q_R = 0.
```

To isté znamienkové rozdelenie sa našlo v nezávisle udržiavaných A1
implementáciách `11_script_A1_K1_cdm_background_audit.py` aj
`baseScripts/k_mpc_005/af_from_a1_background.py`. Pri `lambda=0` zmiznú
všetky zdroje.

## Čo výsledok znamená a čo nie

Výsledok robí z K1 dôveryhodný **efektívny backgroundový referenčný ledger**.
Nedokazuje, že mikroudalosť delenia produkuje iba popol, ani že popol musí
vzniknúť pred parou. Existujúce A1 rovnice nijako nerozlišujú paralelný a
sekvenčný mikroproces, ak po coarse-grainingu dávajú rovnaké `Q_A`.

Preto K1 neuzatvára Q22a a nemení hĺbku A1-K1/A2-K4. Slúži ako nulový-nový-
predpokladový bod pre K2 až K7.

## Ďalší krok

Q22a-K3 dostane minimálny paralelný ledger. Audit preverí, že zachovanie
energie samo určí iba súčet produktov, nie rozdelenie medzi popol a paru.
Ak sa objaví neodvodený podiel, nebude zavedený do fyzikálneho modelu ani
označený ako riešenie.
