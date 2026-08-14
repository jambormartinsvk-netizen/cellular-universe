# READ FIRST — A2 po audite skriptov 173–185

Dátum: 2026-07-15

Aktuálny stav: **A2-K4 ŽIVÁ, 66.5/100; K7b numerický PASS; K7c REVIEW.**

## Čo je už uzavreté

- Nezhoda `U_fs/U_gamma` v 172 a extrémna D-aktivita mali spoločnú príčinu: neskorší `mu=0` solve prepísal HP register fyzikálneho solve.
- 174/175 túto chybu opravili a 176 prešiel štyrmi povrchmi.
- K7c preto nededí posunuté rýchlosti z `mu=0` registra.

## Čo ešte nie je uzavreté

- Individuálny rank check v 172/175 je fail-open pri súčasnom chýbaní oboch kľúčov. Skutočný PASS payload ich mal (`58=58`), takže výsledok sa neruší, ale pred publikáciou treba fail-closed náhradu.
- Checky `rhs[0]-(3D+2s²eta)`, `rhs[1]-M`, spätné skladanie species z `D/M` a self-checky v 178 nie sú nezávislý fyzikálny dôkaz.
- K7c.3c zlyhala na neasymptotickej konvergencii `M`: pomer zjemnení je `0.367`, nie približne 16.
- Skript 186 je iba nedokončená zachovaná stopa. Nespúšťať ho a nedopisovať pod rovnakým číslom.

## Povinný nasledujúci smer

Najprv fail-closed spevniť provenienciu K7b/K7c seed reťazca. Potom vytvoriť čistý samostatný RK4 konvergenčný gate s explicitným pomerom a bez nedosiahnuteľného `solve_ivp` bloku. Až následne vytvoriť novú náhradu za 186 pre term ledger `M'`.

Úplný rozsudok: `Audit/A2_K4_C7_7C_SCRIPTS_173_185_CLAIM_AUDIT_2026-07-15.md`.
