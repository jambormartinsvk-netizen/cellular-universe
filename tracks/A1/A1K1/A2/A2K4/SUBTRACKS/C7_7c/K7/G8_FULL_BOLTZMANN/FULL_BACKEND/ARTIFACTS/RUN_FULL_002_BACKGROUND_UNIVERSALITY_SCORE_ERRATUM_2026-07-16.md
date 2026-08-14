# FULL RUN-002 — skórovacie a rozsahové erratum

**Dátum:** 2026-07-16  
**Pôvodný audit:** `RUN_FULL_002_BACKGROUND_UNIVERSALITY_AUDIT.md`  
**Pôvodný verdikt:** `STOP_BACKGROUND_K_DEPENDENCE_UNRESOLVED`  
**Autoritatívna oprava interpretácie skóre:** pôvodný samostatný zápis
`Skóre: bez zmeny, 90/100` sa nesmie čítať ako fyzikálna hĺbka A2-K4.

## Rozsudok

| Metrika | Správna hodnota | Rozsah |
|---|---:|---|
| body získané RUN-002 | `0` | test nepridal fyzikálnu podporu |
| historické K7 interné G0-G7 pokrytie | `90/100` | iba redukovaná K7 RHS; neprenositeľné |
| historická K7 technická hĺbka | `66.5/100` | neprenositeľná na aktívnu formuláciu |
| autoritatívna fyzikálna hĺbka A2-K4 | `60/100` | aktívna species-first P5 |

Číslo `90/100` bolo lokálnou WBS/support metrikou historickej vetvy K7.
Nebolo jednotnou sekvenčnou hĺbkou celej koľaje. Bez tohto označenia bol
riadok v pôvodnom audite zavádzajúci.

## Rozsah fyzikálneho STOP

RUN-002 presne dokázal iba toto:

```text
D_raw_K7(a,k) = 1 + Omega_m*a/Omega_r + k^p*A(a)
```

pri surovom historickom K7 zápise s implicitným `Phi=1`. Taký background
závisí od perturbatívneho Fourierovho módu a nesmie sa použiť ako jedno
globálne `H_K4(a)` v CLASS adaptéri.

Preto zostáva platné:

- **STOP** historického surového K7 CLASS adaptéra;
- **žiadny STOP** A1-K1;
- **žiadna smrť** A2-K4;
- v čase errata bola P5 `REVIEW_BLOCKED_ARCHITECTURE`; neskôr B1 contract
  preflight prešiel a aktuálny stav je `LIVE / B1_CONTRACT_PREFLIGHT_PASS /
  SEED_NOT_RUN` na `60/100`.

## Neskoršie obmedzenie staršej formulácie

Neskorší audit proveniencie odlíšil backgroundový pomer hustôt od
perturbačnej premennej

```text
z = k*a/(H0*sqrt(Omega_r0)).
```

Ak je globálna amplitúda zapísaná

```text
Phi(k) = A_f*(H0*sqrt(Omega_r0)/k)^p,
```

potom

```text
Phi(k)*z^p = A_f*a^p
```

a explicitné `k^p` sa vykráti. To nemení historický výsledok RUN-002:
dokazuje, že stará implicitná voľba `Phi=1` bola pre globálny background
neprípustná. Zároveň však znamená, že RUN-002 nemôže zabiť opravenú
kandidátnu normalizáciu.

Opravená formulácia ešte nemá PASS, kým sa:

1. `A_f` neodvodí z existujúcej hustoty alebo počiatočnej podmienky bez
   nového tichého fitu;
2. nepreukáže rovnaké `rho_f(a)`, `rho_ash(a)`, `D(a)` a `H_K4(a)` pre viac
   skúšobných Fourierových módov;
3. neuzavrie aktuálny P5 coefficient/species/Bianchi kontrakt.

## Povinné citovanie výsledku

Budúce dokumenty nesmú uvádzať iba `RUN-002: 90/100`. Správny skrátený
zápis je:

```text
RUN-002: 0 nových bodov; STOP surového K7 k-závislého backgroundu.
Historické K7 interné pokrytie ostalo 90/100, ale je neprenositeľné.
Aktuálna fyzikálna hĺbka A2-K4/P5 ostáva 60/100.
```

Pôvodný audit sa nemaže, aby zostala zachovaná auditná história. Toto
erratum je jeho záväzným rozsahovým a skórovacím dodatkom.
