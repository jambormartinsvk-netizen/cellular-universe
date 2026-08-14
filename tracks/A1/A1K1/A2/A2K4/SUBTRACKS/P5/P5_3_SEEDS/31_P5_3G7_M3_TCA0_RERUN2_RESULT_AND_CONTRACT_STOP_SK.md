# P5.3g7-M3/TCA0 RERUN2 — výsledok a STOP neúplnej implementácie

**Dátum:** 2026-07-16  
**Runner:** `261_script_KMPC_024_P5_3g7_mode_resolved_full_seed_audit_rerun2.py`  
**Výstup:** `RUN_KMPC_024_P5_3G7_M3_TCA0_RERUN2.json`  
**Machine verdict:** `REVIEW_M3_TCA0_UNCLOSED`  
**Auditný verdict:** `STOP_M3_RUNNER_CONTRACT / REVIEW_BLOCKED_ARCHITECTURE`  
**A2-K4:** zostáva živá na `60/100`; bez nového PASS a bez rozsudku smrti

## Čo oprava M1 preukázala

Tvrdá eliminácia M1 koeficientu podľa AR50 fungovala:

- všetkých 15 štandardných prípadov má redukovanú hodnosť `76/76`;
- M1 absolútny rozdiel je presne `0`;
- štandardné driver rezíduá sú `4.4e-16` až `1.14e-14`;
- štandardné nezávislé holdouty sú `5.9e-17` až `1.29e-14`;
- presné k-cancel identity a background invariancia ostali bez regresie.

Tým sa potvrdilo, že spoločný FAIL RERUN1 pochádzal z neukotvenej amplitúdy.
V2 overlay je platný nástroj na tvrdé M1 ukotvenie.

## Čo po ukotvení zlyhalo

Frakčné `00/0i` holdouty neprešli v žiadnom z `3 k × 5 módov`.
Škálované maximá ležia približne od `2.39e-6` do `2.11e-3`, teda o viac než
tri až šesť rádov nad prahom `1e-9`. AD/BI/CDI hodnoty sa pri zmene `k`
opakujú s rovnakým škálovaným podpisom, takže nejde o náhodný round-off.
NID/NIV navyše neprešli preregistrovanú kontrolu leading-power pomeru.
Neskorší audit ju obmedzil: nešlo o dva nezávislé solvery ani ODE štarty,
ale o vyhodnotenie normy toho istého konečného radu na dvoch plochách.
Je to diagnostika truncation/asymptotiky, nie druhý fyzikálny dôvod smrti.

Tieto čísla by pri úplnom P5 stave boli vážnym Bianchi/constraint STOP.
Post-run contract audit však odhalil, že testovaný stav úplný nebol.

## Rozhodujúca contract-parity chyba

Nadradený P5 kontrakt vyžaduje dynamické `delta_f,U_f`. V1 base má iba 11
frakčných neznámych:

```text
h, eta, dg, dfs, db, dc, Ug, Ufs, sigfs, Ub, Uc.
```

`delta_f` a `U_f` vypočíta pred maticou z vedúcej formule P5.3d a vloží ich
ako pevné slovníky. `DRIVER_ROWS` neobsahuje palivovú kontinuitu ani palivový
Euler. Preto počty `33/33`, `22/22`, `44/44` dokazujú iba plnú hodnosť
11-zložkovej truncation, nie úplnosť palivového kontraktu. Mechanické počty
`39`, `26`, `52` (`13 × počet vrstiev`) sú iba jedna možná implementácia,
nie už odvodená povinnosť: najprv treba oddeliť celočíselnú `Phi^0`
palivovú vežu od prípadných frakčných `Phi^1` korekcií.

Leading formula P5.3d bola platná vo svojom pôvodnom rozsahu. Runner však
neoveril palivovú kontinuitu/Euler na všetkých použitých rádoch ani nevydal
dvojparametrový coefficient manifest. RERUN2 preto testoval užší ansatz než
deklaroval. Tento nedostatok ruší oprávnenie interpretovať 15 holdoutov ako
smrť K4; zatiaľ nedokazuje, že chýbajúce palivové koeficienty sú ich jedinou
kauzálnou príčinou.

## Správny rozsudok

- RERUN2 nie je technicky pokazený: reprodukovateľne vyrátal deklarovaný
  11-zložkový ansatz;
- tento ansatz je `STOP_INCOMPLETE_STATE` pre P5.3g7 a nesmie byť použitý
  ako fyzikálny dôkaz smrti K4;
- RERUN2 runner je `RUNNABLE_REVIEW_ONLY / DO_NOT_USE_PHYSICS`;
- V1 base je `REVIEW_ONLY`; V2 overlay je použiteľný iba na M1 anchor, nie
  ako samostatný dôkaz úplnosti M3;
- JSON ostáva immutable diagnostický artefakt;
- fyzikálna hĺbka K4 zostáva `60/100`.

## Ďalší povolený postup bez násobenia skriptov

Automatický RERUN3 je zakázaný. Najprv sa musí v Markdowne uzavrieť nový
architektonický ledger:

1. odvodiť synchronnú palivovú kontinuitu a Eulerovu rovnicu z presného
   energy-frame `Q^mu`, nie iba preniesť leading seed;
2. vytvoriť dvojitý ledger rádov `Phi^0/Phi^1` a `z^j`; určiť, ktoré
   `delta_f,U_f` koeficienty naozaj vstupujú do prvého K4 Einsteinovho rádu;
3. presne ukázať, ktoré palivové koeficienty sú tvrdé regularitné kotvy a
   ktoré sa riešia dynamicky;
4. pred kódom skontrolovať total-energy/momentum left-null/Bianchi identity;
5. asymptotický test robiť pri módovo zvolených `z<<1`; fixed-`a` plochy
   ponechať samostatne pre k-nezávislosť backgroundu;
6. až nový architektonický audit môže povoliť jeden nový finálny runner a
   prideliť mu číslo. Skript 262 ostáva rezervovaný P5.4.

## Neskoršie metodické rozhodnutie

Architektonický audit a pravidlo cap `10` povolili pokračovať, ale nie
legacy RERUN3. KMPC-022/023/024 sa konzervatívne počítajú ako technické
pokusy `1–3/10`. Nový úplný R-A kontrakt smie po B1 začať preflightom bez
solve ako pokus `4/10`. Tento dodatok nemení uvedený contract STOP ani
fyzikálnu hĺbku K4.

## Neskoršie fyzikálno-formálne obmedzenie PF-063

B1 audit ukázal, že prvý metrický rád potrebuje úplnú `Phi^0` palivovú vežu,
nie mechanicky 13 gravitačných neznámych. Zároveň legacy M3 V1/V2 použila v
`fuel_pf` trojnásobok správnej neadiabatickej tlakovej časti. Preto 21
frakčných FAIL nemožno použiť ani ako test správneho pressure/trace systému.
Oprava tejto chyby však sama nie je dôkazom, že úplný R-A systém prejde.
