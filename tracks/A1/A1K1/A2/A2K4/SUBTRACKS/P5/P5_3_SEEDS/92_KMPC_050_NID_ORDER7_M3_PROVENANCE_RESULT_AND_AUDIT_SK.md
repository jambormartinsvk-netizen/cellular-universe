# KMPC-050 — výsledok NID order-7 M3 provenance

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NID`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Autoritatívny lokálny stav:** `REVIEW_NID_ORDER7_CONSTRAINT_COMPATIBILITY_UNCLOSED`  
**K4/P5:** `LIVE 60/100 / 3.5/6`; score/release/Zenodo/prediction trigger `NONE`

## Výsledok

Technická chyba PF-075 bola odstránená bez zmeny rovníc, supportu alebo
prahov. Shared solver vykonal presne jeden F0 passthrough a jeden zachytený
104×104 M3 solve; owneri sa obnovili. Matica je plnej hodnosti `104/104`
raw aj po equilibrácii. Immutable KMPC-048 regresia, M1 metadata,
combined-`R_fs` a finite guard prešli.

Raw výsledok:
`RUN_KMPC_050_P5_3G7_NID_ORDER7_M3_PROVENANCE_RANK_FILTER.json`, SHA
`8D527E822959D861EB33994233D22BDF752C368025AC66F28C6F820DEF479F65`.

## Čo bolo vylúčené

- Nie je to rank loss: raw aj equilibrated rank sú `104/104` a
  equilibrated singular ratio je `2.7591e-1`.
- Nie je to veľká chyba lineárneho solve: normovaný backward error je
  `9.2733e-17`.
- Nie je to prepis alebo nízka desatinná presnosť vstupu: same-matrix
  korekcia mala iba `2.2867e-16` absolútne aj relatívne.
- Korekcia znížila driver maximum z `1.2631e-10` na `1.5755e-16`, teda
  všetky určujúce riadky po korekcii prešli.

## Čo zostalo otvorené

Nezávislé Einsteinove constraint holdouty sa korekciou prakticky
nezmenili:

| Riadok | Raw rezíduum | Scale | Relatívna metrika |
|---|---:|---:|---:|
| `Einstein_00[7]` | `2.4826e-5` | `1.0795e-4` | `2.2999e-1` |
| `Einstein_0i[7]` | `-1.3002e-6` | `1.5417e-5` | `8.4334e-2` |

To je rádovo väčšie než roundoff a nie je dovolené premenovať ho na
numerický PASS. Výsledok lokalizuje blocker na kompatibilitu určujúcich
rovníc s nezávislými Einsteinovými constraintmi na hornom orderi 7.

## Nové zistenie a ďalší krok

Implementácia M3 auditu používa pre každý fractional support štandardný M1
stav natvrdo iba do orderu `5`, zatiaľ čo KMPC-048/050 vyžaduje M3 order
`7`. Je preto vecne možná **depth-mismatch hypotéza**: fractional
constraint na orderi 7 môže potrebovať M1 koeficienty nad orderom 5.
Zatiaľ je to hypotéza zo source provenance, nie potvrdená príčina.

Predregistrovaný nástupca musí porovnať tú istú NID/.05/nominal M3 maticu
`[0,7]` pri M1 depth `5` a `7`, zachovať rovnice, support, prahy a hard M1
anchor, exportovať rozdiel matíc/konštánt aj koeficientov a overiť regresiu
orderov `0…5`. Ak depth 7 uzavrie oba holdouty bez poškodenia regresie,
príčina sa môže označiť `M1_DEPTH_MISMATCH_CANDIDATE_ONLY`. Ak nie, nasleduje
rovnicový Bianchi/constraint-dependence audit. `[0,9]` a NIV zostávajú
zakázané, kým sa táto príčina nerozlíši.

## Autoritatívny dosah

KMPC-050 nepridáva bod, nemení A2-K4 ani P5 verdict a nie je fyzikálny STOP.
Je to relevantný diagnostický progres: pôvodný order-7 problém už nie je
neurčitá „presnosť“, ale konkrétna constraint-compatibility vetva s jednou
testovateľnou depth-mismatch hypotézou.
