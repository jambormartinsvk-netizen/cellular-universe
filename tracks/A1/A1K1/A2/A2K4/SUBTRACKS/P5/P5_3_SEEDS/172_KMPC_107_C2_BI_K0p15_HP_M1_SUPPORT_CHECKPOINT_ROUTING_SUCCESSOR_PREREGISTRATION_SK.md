# KMPC-107 — HP-M1 checkpoint routing successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `4/10`

## Dôvod

Runner 350/KMPC-106 prešiel compile, ale help/smoke sa zastavili pred CLI na
`ast.literal_eval(dict(_prior_sources))` (`PF-108`). Auditný modul V13,
checkpointová fyzika ani CPQR/F0/M3 nebežali. V13 preto ostáva byteovo
nezmenený.

## Jediná dovolená zmena

KMPC-107 mení iba routing a identitu:

- fail-closed overí SHA neúspešného runnera 350;
- source/prerequisite mapy načíta zo SHA-pinned runnera 346, posledného
  priameho literal ancestor;
- explicitnými hashmi doplní V11, V12, V13, nový identity-only V14, raw
  KMPC-102 a failure raw KMPC-105;
- pred `ast.literal_eval` vyžaduje uzol typu `ast.Dict`;
- V14 po delegovaní V13 mení iba `run_id`, test a source/contract metadata;
- V13 CPQR, support solve, serialization, prahy, rovnice a limit `45 s`
  ostávajú byteovo nezmenené.

Všetky rozhodovacie a checkpointové pravidlá dokumentu 171 platia bez
zmeny. Official je dovolený iba po compile/help/smoke PASS a smoke musí
vrátiť presne `run_id=KMPC-107`.

## Zmrazené hashe pred prvým Python behom

- V13 checkpoint:
  `301E3121DA9E260308FB46E6011A9694BA79676EE57F653DCCD3D472C4C44A78`;
- V14 identity successor:
  `0ED499BFBBD6E6D7FC2640FE13BDAF67CE0C31C1B9AE593648BC2FEB3934733A`;
- runner 351:
  `00463EA658FB5194F6663FA1741D55EF66911010F2CCDA5EE735F964F3F89F69`;
- failed runner 350:
  `978D5D4CBDC814B393AD5D1098BEF54123C9AAB80741BBEB145EEBCB29442E1F`;
- literal ancestor runner 346:
  `5DF6010385C76F743B4F59DA5F5F39C88CC4F205645CE2167864CAC40A548BCB`;
- výsledný contract: `43` source a `17` prerequisite položiek;
- harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`.

Pred vytvorením tejto predregistrácie nebol V14 ani runner 351 spustený cez
Python. Od tohto bodu sú V14 a runner 351 immutable.
