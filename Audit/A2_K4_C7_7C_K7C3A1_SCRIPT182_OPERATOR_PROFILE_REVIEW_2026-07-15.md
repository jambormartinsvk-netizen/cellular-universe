# A2-K4 / C7.7c / K7c.3a.1 — REVIEW operátorového profilu 182

Dátum: 2026-07-15  
Stav skriptu 182: **REVIEW — jedna preregistrovaná brána neprešla**  
Stav K4: **ŽIVÁ, 66.5/100**

## Výsledky bez ODE

- rozpätie envelope škál: `4.17e36`;
- maximum počiatočného normalizovaného RHS: `0.03747`;
- maximum fyzikálneho operátora: `43.54`;
- maximum škálovaného operátora: `17.83`;
- fyzikálny spektrálny polomer: `3.4441515426250273`;
- škálovaný spektrálny polomer: `3.4441515426250175`;
- relatívny rozdiel spektier: `2.84e-15` — PASS;
- relatívna rekonštrukcia fyzikálneho `A*y`: `1.785e-8` oproti prahu `1e-12` — FAIL.

Najväčší škálovaný coupling bol `D -> delta_f` s absolútnou hodnotou `17.83`. Žiadny coupling ani počiatočný normalizovaný RHS nevysvetľuje 200 000 adaptívnych RHS volaní fyzikálnou explóziou.

## Interpretácia

Formálne sa nesmie vyhlásiť PASS, pretože preregistrovaný relatívny `A*y` prah neprešiel. Súčasne tento jediný neúspech nie je dôkazom fyzikálnej nestability: operátor bol vytvorený z veľmi rozdielnych probe amplitúd a relatívna metrika delí absolútny float64 floor malým fyzikálnym RHS. Prah sa spätne neuvoľňuje.

Skript 182 zostáva REVIEW. Nasledujúca samostatná podkoľaj nebude meniť RHS ani seed; odstráni adaptívny error controller a použije dve predregistrované pevné RK4 mriežky. Jej dôkazom bude kroková konvergencia koncového projektovaného stavu, nie post hoc premenovaná brána 182.

