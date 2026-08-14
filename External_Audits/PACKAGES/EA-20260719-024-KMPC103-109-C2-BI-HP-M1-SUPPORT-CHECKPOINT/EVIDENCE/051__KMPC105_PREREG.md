# KMPC-105 — HP-M1 downstream identity successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `2/10`

## Dôvod

KMPC-104 AST loader, compile/help a všetkých 17 smoke checks prešli. Smoke
však odhalil, že V11 payload stále niesol pôvodné `run_id=KMPC-103`.
Stabilný harness payload identity nekontroluje, preto official nebol
spustený a raw nevznikol (`PF-106`).

## Jediná dovolená zmena

KMPC-105 pridáva V12 identity-only wrapper:

- deleguje celý smoke/official výpočet byteovo nezmenenému V11;
- po návrate mení iba `run_id`, `test`, source-hash ledger a contract metadata;
- pridáva fail-closed check `payload.run_id == KMPC-105`;
- V9 CPQR, V11 downstream sled, prahy, rovnice, support, merge a rozhodovací
  strom dokumentu 168 ostávajú byteovo nezmenené;
- SHA-guarded AST načítanie prior hash máp ostáva podľa KMPC-104.

Official sa smie spustiť iba ak smoke vráti `run_id=KMPC-105` a všetky
checks true.

## Zmrazená implementácia pred prvým Python behom

- V11 calculation:
  `28B5FD79225BD06D8CB762BA9960EFFB1AE82E9E84F05E0FCCBFC77429B4B573`;
- V12 identity wrapper:
  `479EEFD9BFDBF6E663BF6C6941444AB347C1CF9B54EBC522A3E82601D9C615F3`;
- runner 349:
  `1AA37C77A9992424EB7878C9056DD6AF4A48609149148F4F9663CEAE9C8D146E`;
- frozen runner 346 contract:
  `5DF6010385C76F743B4F59DA5F5F39C88CC4F205645CE2167864CAC40A548BCB`;
- raw KMPC-102:
  `49187BB85B8C59559A23EF6741DFB64F0015C2F0CC458D5C9D284FF2CECDE0CB`;
- výsledný literal contract: `41` source a `16` prerequisite položiek;
- harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`.

Pred vytvorením tejto predregistrácie nebol V12 ani runner 349 spustený cez
Python. Od tohto bodu sú V12 a runner 349 immutable.
