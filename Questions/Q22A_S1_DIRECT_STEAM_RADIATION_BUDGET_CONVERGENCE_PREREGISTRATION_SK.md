# Q22a-S1 — preregistrácia konvergencie hranice priamej pary

**Vstupný výsledok:** `RUN_Q22A_004_S1_DIRECT_STEAM_RADIATION_BUDGET_SCREEN.json`  
**Úloha:** overiť, že hranica `f_R,max` nie je artefakt kroku RK4.

## Čo sa zopakuje

Ten istý registrovaný model a tá istá bisection sa spustia s polovičným
krokom `0.0005` namiesto `0.001`. Žiadny parameter fyziky sa nemení.

## Očakávanie

K1 (`f_R=0`) má ostať pozitívna, K2 (`f_R=1`) má stále zlyhať na radiácii a
nová hranica sa má od pôvodnej líšiť menej než `1e-4` relatívne. Táto tolerancia
je úmyselne voľnejšia než očakávaný štvrtý rád RK4, pretože hranicu navyše
diskretizuje bisection a detekcia prechodu cez nulu.

## PASS / STOP

* **PASS:** oba kvalitatívne verdikty sú rovnaké a relatívny rozdiel hraníc
  je pod `1e-4`.
* **STOP numeriky:** ak sa zmení kvalitatívny výsledok alebo sa hranica
  nezhodne. Fyzikálny rozsudok sa potom nesmie použiť, kým sa neurčí príčina.

## Limity

Vnútorný limit 4.5 s, vonkajší limit 10 s. Tento beh nemení fyzikálne skóre.
