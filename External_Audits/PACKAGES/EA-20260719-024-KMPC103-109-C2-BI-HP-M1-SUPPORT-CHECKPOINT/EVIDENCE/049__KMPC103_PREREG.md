# KMPC-103 — HP-M1 downstream F0/M3/holdout insertion: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `0/10`

## Dôvod a jediná otázka

KMPC-102 uzavrel natívny 80-dps M1 numerical boundary: CPQR rank `98/98`,
všetky numerické invarianty aj M1-local driver/holdout prešli. Otvorená je
už iba propagácia tohto riešenia do úplného 13-stavového F0/M3 systému.

KMPC-103 smie zodpovedať iba:

> Uzavrie nezmenené natívne HP-M1 riešenie po vložení do frozen F0/M3
> pipeline finálny exact driver a nezávislý `Einstein_00/0i` holdout pre
> BI/k=.15, pričom accepted `[0,5]` ostáva adekvátny voči audit `[0,7]`?

## Zmrazený výpočtový sled

1. Reprodukovať jeden V9 MGS-CPQR solve pri 80 dps bez zmeny V9 alebo prahov.
2. Frozen F0 vyrátať osobitne pre accepted `[0,5]` a audit `[0,7]` z HP-M1
   state.
3. Zlúčiť presne 11 M1 a 2 fuel stavy v autoritatívnom 13-state poradí;
   SHA pred/po merge musí dokázať, že merge nemení `delta_f,U_f`.
4. Frozen M3 vyrátať pre accepted aj audit, potom použiť pôvodné common/tail,
   S-C0, R_fs a background brány bez zmeny tolerancií.
5. Auditný float64 `104×104` driver capture vykonať presne raz a na tom istom
   combined state zostaviť 80-dps exact `104×104` driver plus nezávislý
   `16×104` holdout; holdout riadky sa nesmú pridať do solve.
6. Reportovať finálny `Einstein_0i[7]` residual, normu a metriku.

Historický KMPC-087 attribution-reconstruction ledger nie je success gate:
jeho uložený residual a fingerprint patria starému M1 state a po legitímnej,
predregistrovanej náhrade M1 nie sú invariantom. Žiadna atribučná tolerancia
sa neuvoľňuje; nová atribúcia je mimo scope.

## Nezmenené brány

- driver `1e-10`;
- independent holdout `1e-9`;
- common `1e-8`;
- tail `1e-6`;
- absolute fallback a background prahy presne z frozen C2 kontraktu;
- V9 CPQR rank/orthogonality/factorization/normal thresholds
  `1e-60/1e-60/1e-60/1e-55`.

`PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY` vyžaduje
súčasne M1, static/core, accepted, audit, common, tail, S-C0, R_fs,
background, exact driver a independent holdout PASS, fuel SHA paritu,
presne jeden audit driver capture a `Einstein_0i[7] <= 1e-9`.

Ak zlyhá exact driver, výsledok je
`REVIEW_C2_BI_K0p15_HP_M1_EXACT_DRIVER_UNCLOSED`. Ak zlyhá independent
holdout, výsledok je
`REVIEW_C2_BI_K0p15_HP_M1_NONFIT_HOLDOUT_UNCLOSED`. Iný otvorený downstream
gate je `REVIEW_C2_BI_K0p15_HP_M1_DOWNSTREAM_GATE_UNCLOSED`.

Skript vydáva iba kandidáta. C2 bod môže pridať až interný audit raw.

## Scope

Vylúčené sú nová coefficient attribution, `[0,9]`, ostatné C2 atómy,
S-M, ODE, P5.4, G8/G9, likelihood, prediction table a release trigger.

## Procesné zlepšenie runnera

Runner 347 nereplikuje ručne 39 starších source hashov a 15 prerequisite
hashov. Read-only načíta tieto dve frozen mapy z runnera 346 až po overení
jeho presného SHA, potom pridá iba V11 a raw KMPC-102. Tým sa znižuje riziko
prepisovej chyby bez dynamického uvoľnenia hash guardov.

## Zmrazená implementácia pred prvým Python behom

- V9 calculation modul:
  `8EBDA7232BEADF0640A2C8361B444A9A896EB215E159E552AC494EAE2C0CCD0A`;
- V11 downstream modul:
  `28B5FD79225BD06D8CB762BA9960EFFB1AE82E9E84F05E0FCCBFC77429B4B573`;
- frozen runner 346 contract:
  `5DF6010385C76F743B4F59DA5F5F39C88CC4F205645CE2167864CAC40A548BCB`;
- runner 347:
  `584FE4FD2F0EFF3539419356D9E3409E355AD1C426481B500C1589FA33FF52CB`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `40/40` source, `16/16` prerequisite a prior-runner SHA
  sedí.

Pred vytvorením tejto predregistrácie nebol V11 ani runner 347 spustený cez
Python. Od tohto bodu sú V11, runner 347, sled, prahy a rozhodovací strom
immutable.
