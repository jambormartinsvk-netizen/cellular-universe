# G8 RUN-000 — očakávanie pred exact CAMB coefficient sanity checkom

**Dátum:** 2026-07-15  
**Spúšťaný skript:** `scripts/76_script_A2_K4_3b_exact_CAMB_hierarchy_coefficients_alias_fixed.py`  
**Rozsah:** iba `SCREEN-S0`, žiadna evolúcia a žiadny G8 bod

## Ľudskou rečou

Kontrola sa pýta, či máme stále dostupnú tú istú lokálnu verziu CAMB a či
naše zapísané fotónové, neutrínové a polarizačné koeficienty presne
zodpovedajú jeho symbolickým rovniciam. Nepočíta vývoj vesmíru ani hodnoty
S8/H0. Je to kontrola pravopisu rovníc pred stavbou väčšieho operátora.

## Očakávaný výsledok

- CAMB verzia `1.6.6`;
- `J_l`, `G_l`, `E_l` pre `l=2..8`: 21 presných nulových rezíduí;
- polarizačný zdroj `polter`: 1 presné nulové rezíduum;
- spolu 22/22 PASS;
- verdict `PASS_EXACT_CAMB_HIERARCHY_COEFFICIENTS_ALIAS_FIXED`;
- runtime pod 10 s.

## Rozhodnutie

- pri úplnom PASS: pokračovať skriptom 221; support ostáva `90/100`;
- pri nenulovom rezíduu: zastaviť G8 mapovanie a auditovať konvencie/aliasy;
- pri importe alebo timeoute: technické REVIEW, nie fyzikálna smrť K7;
- očakávanie sa po výsledku nesmie meniť bez písomného dôvodu.

## Limity

- interný deadline skriptu: 10 s;
- externý procesný timeout: 15 s;
- žiadny retry v tom istom procese.

