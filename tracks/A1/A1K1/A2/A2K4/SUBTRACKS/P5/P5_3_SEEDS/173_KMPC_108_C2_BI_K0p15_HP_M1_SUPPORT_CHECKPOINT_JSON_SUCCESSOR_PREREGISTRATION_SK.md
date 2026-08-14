# KMPC-108 — HP-M1 checkpoint JSON successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `5/10`

## Dôvod

KMPC-107 prešiel compile/help/smoke a vypočítal celý V13 checkpoint prefix,
ale stabilný publish odmietol najmenej jeden `mpmath.mpf` v širšom
diagnostickom payload-e (`PF-109`). Immutable success raw preto nevznikol a
in-memory výpočet sa neinterpretuje. Osobitný resume register V13 už pritom
mal správny decimal90/float-hex kontrakt.

## Jediná dovolená zmena

KMPC-108 pridáva V15 publish-representation adapter nad byteovo nezmeneným
V13 výpočtom:

- rekurzívne nájde každý zostávajúci `mpmath.mpf` v celom payload-e;
- prevedie ho na 90-digit desatinný reťazec a pri 80 dps vyžaduje presný
  round-trip;
- zapíše počet a presnú JSON-like cestu každej konverzie;
- nesmie meniť už serializovaný `resume_checkpoint`, jeho schema, poradie,
  hodnoty ani `serialized_state_sha256`;
- nesmie meniť CPQR, F0/M3, support, rovnice, prahy alebo limit `45 s`;
- zachová `pass_c2_atom_candidate=false` a checkpoint-only rolu.

Smoke musí navyše overiť nested payload fixture, presné cesty konverzií,
nezmenené obyčajné skaláre a neprítomnosť `mpf` po adaptéri. Official je
dovolený iba po compile/help/smoke PASS.

## Zmrazené hashe pred prvým Python behom

- V13 calculation:
  `301E3121DA9E260308FB46E6011A9694BA79676EE57F653DCCD3D472C4C44A78`;
- V14 identity:
  `0ED499BFBBD6E6D7FC2640FE13BDAF67CE0C31C1B9AE593648BC2FEB3934733A`;
- V15 JSON successor:
  `0818D47F50A99C4EDE4FD5320F9A39E4FA0B6134A95FC1027D6FF7AB57A5362B`;
- runner 352:
  `1308134805BC339551177C7FA78C3379F4A2AB0D2BE90E68B26732ECBA7E4A48`;
- failed runner 351:
  `00463EA658FB5194F6663FA1741D55EF66911010F2CCDA5EE735F964F3F89F69`;
- PF-109 failure raw:
  `ADB8D2A1669E4C6E0C07C4A3E2C0E3B8809A4514C4F32E26CF76684FAA92F89C`;
- výsledný contract: `44` source a `18` prerequisite položiek;
- harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`.

Pred vytvorením tejto predregistrácie nebol V15 ani runner 352 spustený cez
Python. Od tohto bodu sú V15 a runner 352 immutable.
