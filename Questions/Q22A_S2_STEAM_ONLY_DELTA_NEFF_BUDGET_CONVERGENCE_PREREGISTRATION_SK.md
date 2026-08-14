# Q22a-S2 — preregistrácia konvergencie parného rozpočtu

**Vstupný výsledok:** `RUN_Q22A_006_S2_STEAM_ONLY_DELTA_NEFF_BUDGET_SCREEN.json`.

## Postup

Rovnaké S2 sa zopakuje s polovičným krokom `5e-5`. Bisection sa zníži z 22 na
20 iterácií iba kvôli pevnému runtime limitu; výsledok sa preto bude čítať ako
interval `[f_pass,f_fail]`, nie ako bod s falošnou presnosťou.

## Očakávanie a kritérium

K1 musí zostať pozitívna a K2 musí skončiť zápornou parou. Stred polkrokového
intervalu sa má od strednej hodnoty pôvodného intervalu odlišovať najviac o
5 %. Šírka nového intervalu je sama súčasťou výsledku.

## STOP

Zmena kvalitatívneho verdiktu alebo neprekrývanie intervalov znamená
`STOP_NUMERICAL_CONVERGENCE`; fyzikálne obmedzenie sa potom nesmie citovať.

## Limity

Interný limit 4.5 s, vonkajší 10 s, najviac 200 000 krokov na trajektóriu.
