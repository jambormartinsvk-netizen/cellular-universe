# A2 — inventúra vetiev obnovených po zmene technického capu 2 → 10

**Dátum:** 2026-07-16  
**Rozsah:** aktívne vetvy, ktoré historicky zastavila formulácia
„prvá implementácia + dve technické opravy“  
**Autoritatívny rozsudok:** hlavný orchestrátor  
**Fyzikálny účinok:** bez bodov, bez zmeny hĺbky a bez release triggera

## 1. Ľudský záver

Starý limit dvoch technických opráv nesmie pochovať fyzikálnu koľaj iba
preto, že skript, register alebo adapter bol chybný. Inventúra našla dve
živé vetvy, ktorým tento limit reálne zastavil ďalšiu implementáciu:

1. `A2-K4 -> P5 -> P5.3g7-M3`;
2. `A2-K11 -> K11-R -> K11-CS2`.

Obe sa obnovujú technicky, nie fyzikálne. Ich rovnice, mechanizmy, prahy a
hĺbka sa nemenia.

## 2. Autoritatívna tabuľka

| Vetva | Historické incidenty | Skutočný stav | Nová technická vetva |
|---|---|---|---|
| `A2-K4/P5/P5.3g7-M3` | KMPC-022: PF-055 JSON; KMPC-023: PF-056 M1 mimo solve; KMPC-024 potom odhalil PF-058 chýbajúce `delta_f,U_f` a rows | K4 je živá `60/100`; legacy runner má `STOP_M3_RUNNER_CONTRACT`, nie fyzikálny STOP | `M3-FULL/R-A/ARCH-A`; counter `5/10`, B1 contract preflight PASS, ďalší seedový balík 6/10 |
| `A2-K11/K11-CS2` | PF-061 external-exit timeout; PF-062 chybný E-mode state register; pokusy 1–4 full-v002 technicky zdokumentované | K11 je REVIEW `10/100`; scoped podtriedy sú mŕtve, full K11 nie | full v002/ARCH-A, `5/10`; source-AST contract PASS, full DAE NOT_RUN |

## 3. K4 — prečo nejde o slepý RERUN3

Legacy KMPC-022/023/024 testoval neúplný 11-zložkový frakčný ansatz.
PF-058 dokázal, že nadradený kontrakt vyžadoval dynamické
`delta_f,U_f` a fuel continuity/Euler rows. Preto sa starý runner
nepatchuje lokálne a jeho 21 frakčných FAIL sa nesmie fyzikálne súdiť.

Nová R-A architektúra najprv uzavrie:

- `Phi^0/Phi^1 × z^j` coefficient manifest;
- úplné synchronné fuel/ash rows z rovnakého `Q_A^mu`;
- total-energy a total-momentum left-null/Bianchi identitu;
- presný K4-viazaný `h,eta` seed;
- deklarovanú steam vetvu a povinné nulové limity.

Až potom sa smie vytvoriť nový versioned base/runner. Ide o technickú
implementáciu rovnakého K4 mechanizmu, nie K4-K8 ani nový fyzikálny suffix.
Counter sa konzervatívne neresetuje: KMPC-022/023/024 ostávajú pokusy 1–3
a úplný R-A preflight bude pokus 4/10. Tým sa cap nedá obísť premenovaním
base modulu.

## 4. K11 — prečo full v002 začína 0/10

PF-061/PF-062 patria S0-v001, ktorý ostáva zmrazený ako formula-regression
a STOP-state dôkaz. Full v002 je nová úplná technická architektúra s exact
state/RHS paritou, multispecies DAE, regular basis, thermal/TCA mapou a
nezávislými holdoutmi. Preto jej ledger začína `0/10`; staré incidenty sa
nezapočítavajú druhý raz.

## 5. Nálezy, ktoré sa neobnovujú

| Nález | Rozhodnutie |
|---|---|
| K7d V1/V2 | V2 prešla a historický scoped K7d PASS existuje; stará RHS však nemala dynamické `U_c`, preto jej aktívny nástupca je P5, nie V3 |
| G8 SCREEN S0–S3 | technicky prešli; FULL blokuje neplatný starý K4 background/state, nie cap opráv |
| K7c/P4A | nevyčerpal opravný rozpočet a bol uzavretý |
| K1/K2/K3/K5/K6 | ich scope-limited fyzikálne STOP-y boli znovu auditované; technický cap ich neoživuje |
| K11-COMP a ďalšie certified-empty podtriedy | zostávajú mŕtve; obnovený je iba full coupled DAE rodič |

## 6. Technický STOP po novom

Každá nová architektúra má vlastný ledger najviac 10 technických pokusov.
Po desiatom neúspechu zomrie iba tá technická cesta a musí uviesť presný
dôvod `SCRIPT_IMPLEMENTATION_FAILURE`, `PYTHON_OR_DEPENDENCY_FAILURE`,
`SANDBOX_OR_ENVIRONMENT_FAILURE` alebo `BUILD_OR_ADAPTER_FAILURE`.
Fyzikálny rodič zostáva `REVIEW_TECHNICAL_UNRESOLVED`.

## 7. Poradie pokračovania

1. K4 R-A B1 coefficient/species/Bianchi ledger — najvyššia informačná
   hodnota, pretože K4 je jediná živá koľaj na `60/100`;
2. po uzavretí B1 jeden úplný K4 M3-FULL technický preflight/run;
3. paralelne dokumentačne pripraviť K11 v002 package/adapter kontrakt;
4. G8 až po úplnom P5.3/P5.4; starý K7 adapter sa neobnovuje.

## 8. Stav po pokračovaní

- K4 spoločný counter je `5/10`. Pokus 4 zachoval presné algebraické nuly,
  ale PF-064 odhalila self-auditing state guard. Pokus 5 zaviedol samostatný
  contract a prešiel `9/9` plus deväť negatívnych fixtures. B1 je
  `PASS_CONTRACT_PREFLIGHT_ONLY`; seedový pokus 6 ešte nebežal.
- PF-058 bola spresnená: na prvom metrickom ráde netreba mechanicky pridať
  `delta_f[1],U_f[1]` do gravitačného bloku, ale treba úplnú `Phi^0` fuel
  vežu a obe rows. PF-063 navyše našla 3× chybný legacy pressure source.
- K11 použila `5/10` poradových miest. Audit K11-TC-A dokázal, že univerzálna presná
  finite-`L` CAMB-E uzávera neexistuje. Nezabil K11; otvoril cestu
  K11-TC-A3 s explicitne numerickým top rezom a povinnou `lmax`/closure
  konvergenciou. Alternatíva K11-TC-B zostáva natívny CLASS backend s
  presnou mapou. Pokusy 1–4 zachovali presné technické dôvody; pokus 5
  prešiel source-AST contractom `55/55`. Full DAE ešte nebežal.

Tieto zmeny nemenia fyzikálnu hĺbku ani release trigger.
