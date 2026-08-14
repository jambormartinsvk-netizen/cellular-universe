# P5.3f — výsledok: gauge-invariantná rýchlosť a medzera hierarchy

**Dátum:** 2026-07-15  
**Skript:** `scripts/247_script_KMPC_010_P5_3f_gauge_hierarchy_seed_audit.py`  
**Strojový záznam:** `scripts/results/k_mpc_005/RUN_KMPC_010_P5_3F_GAUGE_HIERARCHY_AUDIT.json`  
**Čas:** 0.032 s; limit 5 s interný / 10 s vonkajší  
**Verdikt:** `PASS_P5_3F_GAUGE_HIERARCHY_GAP_MAPPED`; `P5.4_BLOCKED_STANDARD_L2_PLUS_HIERARCHY_SEED_MISSING`.

## Čo bolo overené

1. Pri spoločnom synchronnom velocity-shifte `G` platí presná identita
   `(U_f+G)-(U_c+G)-(U_f-U_c)=0`. Relatívna rýchlosť `U_f-U_c` je teda
   gauge-invariantná; nulovanie `U_c` by odstránilo fyzikálny relatívny mód,
   nie iba voľbu súradníc.
2. Historický skript 80 obsahuje presný operátor collisionless hierarchy a
   regulárne rády `l=2` a vyššie, avšak pre interný nu–steam mód.
3. Zdroj 84 a štandardné inicializácie BR2 89/90 sú zdokumentovane iba v
   sektore `l=0,1`. Nie je v nich regulárne štandardné fotónové/neutrínové
   semeno pre `l>=2`.

## Čo tento výsledok neznamená

Nie je to ODE test, dynamické zachovanie constraintov, dôkaz plnej hierarchie
ani otvorenie G8. Je to `PASS_MAPY`: presne lokalizuje chýbajúci diel a
zabraňuje tomu, aby P5.4 omylom integroval neúplný počiatočný stav.

## Rozhodnutie a ďalší krok

K4 zostáva **živá**; P5.4 a G8 zostávajú **blokované**, nie mŕtve. Nasleduje
P5.3g: odvodiť alebo prevziať s úplnou formula-provenance stopou regulárne
standard-mode seedy pre fotónové a neutrínové multipóly `l>=2`, skontrolovať
ich voči K7 konvencii a až potom ich overiť na dvoch štartových plochách.

Žiadne skóre ani hĺbka sa týmto mapovacím krokom nemenia.
