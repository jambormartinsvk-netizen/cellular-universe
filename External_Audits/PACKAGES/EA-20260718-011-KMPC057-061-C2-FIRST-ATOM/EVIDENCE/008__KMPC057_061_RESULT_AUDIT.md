# KMPC-057 až 061 — C2 prvý atóm: výsledok a orchestrátorský audit

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C2 → AD/k=.005/nominal`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Autoritatívny stav:** `REVIEW_C2_AD_K0p005_SUPPORT_EXTENSION_REQUIRED`  
**Skóre:** K4 `60/100`, P5 `3.5/6`; bez zmeny

## 1. Technická línia

- KMPC-057/PF-077 zastal v smoke na zámene historickej S1 extended mapy za
  dnešný closed C1 support;
- KMPC-058/PF-078 príliš široko očakával stale rozdiel pri štyroch módoch;
- KMPC-059/PF-079 už mal správny V1 false diff, ale jeho failure reporting
  nevypísal vnútorný false check;
- read-only KMPC-060 dokázal, že V1 false checks sú `(BI,CDI)`, zatiaľ čo
  historical-S1-vs-closed diff je `(AD,CDI,BI)`;
- KMPC-061 obe otázky oddelil, celý preflight prešiel a úspešný vecný proces
  vynuloval aktívny technický counter na `0/10`.

Žiadny z PF-077 až PF-079 nevykonal fyzikálny atóm ani nevytvoril JSON.

## 2. Immutable výsledok

`scripts/results/k_mpc_005/RUN_KMPC_061_P5_3G7_C2_AD_K0p005_NOMINAL.json`  
SHA-256 `0952AF08B1DE291D015F71396954F70EAE2F78A962E1EE1D3A08ECA48A1F5DCD`

| Brána | Výsledok |
|---|---:|
| M1 rank | `76/76`, PASS |
| M1 driver / holdout state-scaled | `2.62013e-14 / 5.24025e-14`, PASS |
| accepted `[0,2]` a audit `[0,4]` core | PASS |
| S-C0 actual lower moments | PASS |
| common F0 / M3 | `1.24949e-15 / 7.67380e-13`, PASS pod `1e-8` |
| background worst relative | `1.15195e-16`, PASS pod `1e-12` |
| F0 tail `3,4`, `z=1e-4 / 1e-2` | `2.81017e-4 / 2.85958e-2`, FAIL |
| M3 tail `3,4`, `z=1e-4 / 1e-2` | `3.27772e-4 / 3.35204e-2`, FAIL |

Najhorší F0 stav je `delta_f`, najhorší M3 stav `eta`. Všetky štyri tail
hodnoty prekračujú frozen limit `1e-6` o viac rádov; nejde o vstupný roundoff
ani o hraničnú toleranciu.

## 3. Autoritatívna interpretácia

AD support `[0,2]`, ktorý bol dostatočný pri `k=.05`, nie je dostatočný pri
`k=.005`. Toto nie je STOP A2-K4 ani zlyhanie background mapy: background,
rovnice, rank, driver, holdout, S-C0 a common koeficienty prešli. Je to
lokálny C2 support REVIEW a dôkaz, že support nemožno preniesť medzi `k`
iba podľa výsledku sentinelu.

Automatické C2 poradie sa správne zastavilo po prvom z desiatich atómov;
ostatných deväť sa nespustilo.

## 4. Ďalší predregistrovaný krok

Nový samostatný AD/`.005` support ladder smie testovať candidate `[0,4]`
voči audit `[0,6]` pri M1 depth 6, rovnakých povinných bránach a nezmenených
prahoch. Až jeho PASS dovolí pokračovať do AD/`.15`; jeho tail FAIL otvorí
ďalší, vopred zapísaný krok, nie automatický skok.

Bez score/release/Zenodo/prediction triggera. Bez zmeny fyzikálneho verdiktu
A2-K4 a bez extrapolácie na CDI/BI/NID/NIV.
