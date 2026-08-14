# Audit parity kontraktu P5.3g7 po RERUN2

**Otázka:** testoval KMPC-024 skutočne úplný M3 stav, ktorý vyžadovali
predregistrácie 25–29?  
**Odpoveď:** nie. M1 oprava je správna, frakčný stav je neúplný.

## Nemenná evidencia

| Artefakt | SHA-256 | Klasifikácia |
|---|---|---|
| RERUN2 runner | `12ba3b200659703a8edfe601459def9d848a319f0990cf1d86966f0b52eabf95` | `RUNNABLE_REVIEW_ONLY / DO_NOT_USE_PHYSICS` |
| V2 M1 overlay | `5de2c280b0e9daf528a9e3011368361b37ae53de38827fb6f6ce4ab2019a4455` | `PASS_M1_ANCHOR / REVIEW_ONLY_M3` |
| RERUN2 JSON | `0613ad04cfafcb4414247cdc9fecbcbafa1288520eba51fc5bbde7a37b1c3ee8` | immutable incomplete-ansatz diagnostic |
| V1 base | `5a89cf82006cb5ecc1d8b4be1fd56a463453ee3d6261968cb64de8ccf2c8b7ae` | `V1_UNANCHORED_M1 / INCOMPLETE_FUEL_STATE` |

## Rovnosť zadania, vzorca a vykonaného stavu

### Zadanie

- `P5/00_WORK_PLAN.md` uvádza povinné palivové premenné `delta_f,U_f`;
- dokument 25 požaduje plný seed fotónov, neutrín/pary, baryónov, popola a
  paliva;
- dokument 26 definuje ako neznáme všetky koeficienty `delta_A,U_A` na
  prvom K4 rade;
- dokument 27 zakazuje odstrániť povinný stav a požaduje species RHS.

### Vykonaná implementácia

- `VARS` v base V1 má 11 názvov a neobsahuje `delta_f,U_f`;
- `DRIVER_ROWS` nemá `fuel_continuity` ani `fuel_Euler`;
- `fuel_uf` a `fuel_df` vzniknú pred zostavením indexu neznámych;
- reportované hodnosti sú presne `11 × počet vrstiev`;
- V2 mení iba štandardný M1 solver a túto frakčnú architektúru zámerne
  nemení.

### Rozhodnutie

Nenulové `00/0i` rezíduá sú skutočný výsledok testovaného 11-zložkového
ansatzu, nie numerický šum. Nie sú však invariantným dôkazom, že úplná
energy-frame K4 nemá regulárny seed. Chýba explicitná kontrola palivovej
kontinuity/Euler a ich total-energy/momentum Bianchi kombinácie. To ruší
oprávnenie na fyzikálny rozsudok, ale ešte nedokazuje jedinú kauzálnu príčinu
nenulových holdoutov.

## Obmedzenie starších formulácií

P5.3d PASS zostáva platný ako vedúci regularitný seed. Neskorší RERUN2 audit
obmedzuje iba širšie použitie: vedúcu dvojicu `delta_f,U_f` nemožno bez
dôkazu zmraziť na všetkých M3 vrstvách. Podobne `fractional_full_rank` v
KMPC-023/024 znamená plnú hodnosť 11-zložkovej truncation, nie úplného P5
stavu.

## Architektonická hranica

Toto je povinný audit vyžiadaný numbering capom po druhej oprave 261.
Neautorizuje okamžitý ďalší Python runner. Autorizuje iba textové odvodenie
dvojparametrového palivového coefficient systému, jeho Bianchi/left-null
mapy a nový vopred ohraničený implementačný návrh. Až tento ledger rozhodne,
či treba plných 13 frakčných stavov alebo dlhšiu pomocnú `Phi^0` palivovú
vežu. Číslo a jediný budúci beh sa
pridelia až po uzavretí tejto mapy; 262 sa nesmie spotrebovať pred P5.4.

## Obmedzenie dvojštartového názvu

KMPC-024 nespustil dva nezávislé solvery. Rovnaký konečný Puiseuxov rad iba
vyhodnotil pri dvoch `a` a normu porovnal s jednou mocninou. NID/NIV FAIL je
preto `leading-power/truncation diagnostic`, nie nezávislá stabilitná ani
štartovacia brána. Pri `k=0.05,0.15 Mpc^-1` navyše plytká plocha dáva
`z` približne `2.31` a `6.93`, mimo bezpečného `z<<1` režimu.
