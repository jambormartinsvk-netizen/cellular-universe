# P5.3g7-M3-FULL/R-A — pokus 4/10, výsledok a PF-064 audit

**Dátum:** 2026-07-16  
**Runner:** `264_script_KMPC_025_P5_3g7_m3_full_ra_b1_preflight.py`  
**Raw výsledok:** `RUN_KMPC_025_P5_3G7_M3_FULL_RA_B1_PREFLIGHT.json`  
**SHA-256 výsledku:** `B61DB70A65DE2A80A128DE4FEAF9AB48D84E0F945FCC22661926F1472D0C61D7`  
**Counter po behu:** `4/10`  
**Autoritatívny rozsudok:** `PASS_ALGEBRA_SCOPE / STOP_CONTRACT_GUARD_PF064`  
**Fyzikálny dopad:** žiadny; K4 zostáva živá na `60/100`

## Čo prebehlo

Všetky procesy použili priamy Python, vonkajší limit 10 s a vnútorný limit
najviac 5 s:

| Fáza | Výsledok |
|---|---|
| base `py_compile` | PASS |
| runner `py_compile` | PASS |
| `--help` | PASS; všetky preregistrované voľby |
| smoke | `15/15`, `PASS_R_A_B1_PREFLIGHT_ONLY`, približne `0.141 s` |
| full preflight | `15/15`, raw verdict PASS, približne `0.125 s`; JSON zapísaný |

## Platný čiastkový výsledok

Raw JSON obsahuje presné nuly pre:

- správny pressure coefficient;
- total-energy a total-momentum product rules;
- obe Bianchi propagation identity;
- background `k` cancellation;
- conditional S-C vážený split.

Zdrojové hashe sa presne zhodovali. Nebežal solve ani ODE. Tento algebraický
scope zostáva použiteľný ako regresná kotva.

## PF-064 — prečo sa raw `15/15` neuznáva ako celý B1 PASS

Kontrola `state_ordered_exact_13` overila iba `len==13` a jedinečnosť. Neoverila
presný ordered tuple proti nezávislému nadradenému kontraktu. Negatívne
fixtures boli zostavené z lokálneho `STATE` a následne testovali iba
`candidate != STATE`; neprešli tou istou validačnou funkciou, ktorú by
neskôr použil seedový modul.

Chybný lokálny `STATE` s rovnakým počtom by preto mohol dostať zelenú. Je to
rovnaká trieda chyby ako PF-062: lokálny register auditoval sám seba.

## Rozsudok

```text
PASS_ALGEBRA_SCOPE
STOP_CONTRACT_GUARD_PF064
```

Raw JSON, runner a base sa zachovávajú a nesmú sa vydávať za úplný B1
contract PASS. Pokus 4 je technický neúspech kategórie
`SCRIPT_IMPLEMENTATION_FAILURE`, nie fyzikálny pokus ani smrť K4.

## Povolená oprava — pokus 5/10

Pokus 5 musí:

1. zaviesť samostatný autoritatívny contract modul;
2. mať jedinú `validate_contract(state,driver,holdout)` funkciu;
3. testovať presný ordered tuple, nie count;
4. poslať všetky negatívne fixtures cez tú istú validačnú funkciu;
5. nechať budúci seedový modul importovať ten istý contract;
6. zachovať všetky algebraické identity, hashe a nulové výsledky pokusu 4;
7. znovu nevykonať solve ani ODE.

Ak pokus 5 neprejde, zapíše sa ďalší technický dôvod. Fyzikálny suffix ani
prahy sa nemenia.
