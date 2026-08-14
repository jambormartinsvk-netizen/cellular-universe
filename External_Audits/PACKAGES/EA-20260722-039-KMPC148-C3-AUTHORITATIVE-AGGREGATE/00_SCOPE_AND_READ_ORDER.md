# EA-039 — KMPC-148 C3 autoritatívny agregát 45/45

**Stav:** `SEALED_READY_FOR_EXTERNAL_T2_AUDIT`  
**Target tier:** `T2_REPRODUCIBLE_CALCULATION`  
**Autorita:** interný audit 243; externý auditor iba odporúča  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov/interný orchestrátor:** Codex (OpenAI)  
**LIVE_FILES_CHANGED:** `6` — base, runner, preregistrácia, raw, interný
audit a jedna batch aktualizácia centrálneho plánu; DNR je jediný register  
**AUDIT_PACKAGE_COPIES:** `25` manifestových kópií + `7` controls = `32`;
response `1`; spolu `33 < 40`

## Presná otázka

1. Je package úplná T2 runtime closure pre read-only KMPC-148, vrátane
   runnera, base, všetkých 15 pair rawov a 5 mode-closure autorít?
2. Overí fresh official bez odchýlky exact SHA a kontrakt `20/20`
   vstupov a vytvorí exact kartézsky register `5 × 3 × 3 = 45` bez
   duplicity, s mode counts `9/9/9/9/9`?
3. Má generated JSON po jedinej povolenej normalizácii
   `runtime_seconds` nulový field diff voči reference rawu?
4. Zlyhajú missing-pair a missing-mode-authority guardy fail-closed bez
   success rawu a fyzikálneho verdiktu?
5. Je interný záver správne ohraničený: C3 aggregate PASS, ale žiadny nový
   fyzikálny bod, K4 stále `60/100`, P5 `3.5/6` a P5.4 `NOT RUN`?

## Poradie čítania

1. `EVIDENCE/001` — predregistrácia, 15+5 hashový register a STOP vetvy;
2. `REPRO/scripts/baseScripts/.../c3_authoritative_logical_aggregate.py` —
   jediná testovaná transformačná logika;
3. `REPRO/scripts/392_...py` — immutable CLI, source guard a output guard;
4. manifest, runtime mapa a dokument 03;
5. fresh T2 reprodukcia a dva negatívne guardy;
6. `EVIDENCE/003` iba na field parity;
7. `EVIDENCE/002` až nakoniec na posúdenie interného verdiktu.

## Predregistrované auditné rozhodnutie

- manifest/preflight, compile, help, smoke, official, independent register,
  field parity a oba negatívne guardy PASS bez odchýlky → `AGREE_IN_SCOPE`;
- úplný official vytvorí iný register/candidate alebo nenulový chránený
  field diff → `DISAGREE` a STOP pred successorom;
- chýbajúca dependency closure, nevykonateľný official alebo nutnosť
  obísť guard → `CANNOT_AUDIT` alebo `AGREE_WITH_LIMITATION`, najviac T1;
- platformová či iná odchýlka musí byť `DECLARED_DEVIATION` a nesmie sa
  započítať do T2 official vetvy.

## Tier hranica

T2 je dosiahnuté iba fresh oficiálnou vetvou z novej dočasnej kópie
`REPRO/` bez zmeny source, vstupov, mien, hashov alebo guardov. Balík
neobsahuje druhú nezávislú implementáciu, preto netvrdí T3.

## Nonclaims a STOP

- Audit nereviduje pôvodné fyzikálne solvery, ktoré vytvorili 15 pair
  rawov; kontroluje read-only hashové a logické agregovanie prijatých
  autorít.
- PASS KMPC-148 nie je nová experimentálna evidencia ani nový seed solve.
- K4 sa nemení z `60/100`; S-M/palivový kontrakt ostáva otvorený.
- Pred prijatím externého posudku sa nesmie spustiť S-M successor, P5.4,
  G8, G9, release, Zenodo ani prediction-table zmena.
- Externý auditor odporúča; projektový verdikt mení iba hlavný
  orchestrátor v novom response súbore.
