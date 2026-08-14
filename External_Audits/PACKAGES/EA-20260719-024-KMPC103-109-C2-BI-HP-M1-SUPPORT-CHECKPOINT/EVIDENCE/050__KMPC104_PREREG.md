# KMPC-104 — HP-M1 downstream AST-contract successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `1/10`

## Dôvod

KMPC-103 V11 a runner compile prešli, ale help/smoke sa zastavili pred CLI
parserom. Runner 347 načítal frozen mapy cez vykonanie runnera 346; jeho
top-level `configure(KMPC-102)` bol side effect a druhá konfigurácia bola
správne fail-closed odmietnutá. V11, M1, CPQR, F0 a M3 sa nespustili a raw
nevznikol (`PF-105`).

## Jediná dovolená zmena

KMPC-104 mení iba loader prior-runner kontraktu:

- runner 346 sa najprv overí presným SHA;
- jeho text sa načíta cez `ast.parse`;
- iba assignment literalov `EXPECTED_SOURCE_HASHES` a
  `EXPECTED_PREREQUISITES` sa vyhodnotí cez `ast.literal_eval`;
- žiadny top-level kód runnera 346 sa nevykoná;
- adapter sa konfiguruje presne raz až pre KMPC-104;
- V11, V9 CPQR, výpočtový sled, scope, prahy a rozhodovací strom dokumentu
  168 ostávajú byteovo nezmenené.

Smoke musí navyše nepriamo potvrdiť, že SHA-guarded AST loader dovolil jednu
konfiguráciu, V11 fixture a všetky inherited CPQR fixture checks.

## Zmrazená implementácia pred prvým Python behom

- V11 downstream modul:
  `28B5FD79225BD06D8CB762BA9960EFFB1AE82E9E84F05E0FCCBFC77429B4B573`;
- frozen runner 346 contract:
  `5DF6010385C76F743B4F59DA5F5F39C88CC4F205645CE2167864CAC40A548BCB`;
- runner 348:
  `2468F528601B336BF2249563C259D696F04DDD29D1D2BA6E7EE692C1F3D1A25A`;
- raw KMPC-102 prerequisite:
  `49187BB85B8C59559A23EF6741DFB64F0015C2F0CC458D5C9D284FF2CECDE0CB`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- výsledný literal contract má po pridaní V11/raw102 presne `40` source a
  `16` prerequisite položiek.

Pred vytvorením tejto predregistrácie nebol runner 348 spustený cez Python.
Od tohto bodu je runner 348 immutable.
