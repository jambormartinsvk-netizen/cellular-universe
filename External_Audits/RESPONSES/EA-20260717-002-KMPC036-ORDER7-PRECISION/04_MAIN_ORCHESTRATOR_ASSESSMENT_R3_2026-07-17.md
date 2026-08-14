# Hlavný posudok opakovaného externého auditu R3

**Dátum:** 2026-07-17  
**Externá odpoveď:** `00_AUDITOR_AUDIT.md`  
**SHA-256 externej odpovede:**
`444EEE5D5EAE555130DA681AB9E948945544A213C0E694A0525420F67F10C542`  
**Autorita:** hlavný orchestrátor

## Autoritatívny rozsudok

`PASS_R3_EXTERNAL_REPRODUCIBILITY_T2_ONLY /`
`REVIEW_M1_ORDER7_POWER7_DRIVER_PRECISION_FLOOR_UNCLOSED`

R3 úspešne odstránila technickú reprodukčnú medzeru R2. Oficiálny smoke aj
`--audit` prešli s exit code 0, runner prijal hash KMPC-035 prerequisite a
generated JSON vznikol. Balík preto dosiahol deklarovanú úroveň
`T2_REPRODUCIBLE_CALCULATION_WITH_ENVIRONMENT_GAP`.

Tento PASS patrí iba reprodukovateľnosti balíka. Nie je to plný PASS
order-7 fyziky ani precision closure. Projektový stav KMPC-036 zostáva:

`PASS_M1_ORDER7_REGRESSION_SHAPE_RANK_ANCHOR_CONDITION_STATE_AND_HOLDOUT_ONLY /
REVIEW_M1_ORDER7_POWER7_DRIVER_PRECISION_FLOOR_UNCLOSED`.

K4 zostáva `LIVE / 60/100`, support step 3 zostáva `BLOCKED` a skóre,
predikcie, release aj Zenodo sa nemenia.

## Čo R3 nezávisle potvrdila

- rank `98/98`, hard anchor `0.0`, condition približne `634.7968`;
- order5→7 regresie a 18/18 holdoutov;
- rovnaký smer rozhodovacích polí ako Windows referencia;
- absolútne power-7 rezíduá zostávajú v pásme približne `10^-17..2×10^-15`;
- na Linux/NumPy 2.4.4 zlyhali iba dva terminálne riadky, kým
  `tight_coupling[7]` prešiel.

Platformovo nestabilná identita formálnych failov pri stabilnom machine-floor
pásme je silný dôkaz pre numerický floor a proti formulačnému rozporu. Nie
je však náhradou za predregistrovaný precision/boundary closure audit.

## Nový technický dlh

Auditor pri deklarovanom dodatočnom opakovaní našiel, že publish kolízia môže
ponechať stale `.tmp-…json`. Guard zostáva fail-closed a kanonický výsledok
neprepíše, takže nejde o fyzikálny problém ani o neúspešný projektový pokus.
Budúci nový runner má:

1. kontrolovať existenciu cieľa pred drahým výpočtom;
2. pri publish kolízii bezpečne odstrániť iba vlastný dočasný súbor;
3. zapísať Python, NumPy a BLAS/LAPACK metadata.

Oprava nesmie retroaktívne meniť runner 280 ani zapečatený KMPC-036 JSON.

## Ďalší fyzikálno-numerický krok

Po skončení pauzy vykonať už predregistrovaný
`M1_ORDER7_NUMERICAL_REFINEMENT_AND_BOUNDARY_CLOSURE_AUDIT` na nezmenenej
sústave a prahoch. Externý generated JSON s hashom
`56363A8B104BD28BE5B274B088EFC71AE652F1C0E5C7FC612947FACA29E733DC`
nie je uložený v projektovom strome; jeho výsledky sú dôkazovo nesené
hashovanou externou Markdown odpoveďou, nie ako nový kanonický raw artefakt.
