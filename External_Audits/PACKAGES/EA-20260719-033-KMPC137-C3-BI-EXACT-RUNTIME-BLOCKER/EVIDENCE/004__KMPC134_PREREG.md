# KMPC-134 — C3 BI/.15 HP-M1 checkpoint exact resume

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Východisko:** KMPC-131 BI/.15 je technicky úplný core REVIEW; K4 ostáva
`60/100`.

## 1. Presný blocker

Accepted solve, common, tail, background a nulové limity prešli. Audit
rank-104 M3 mal pri oboch nulových variantoch iba driver a nezávislý
`Einstein_0i[7]` holdout nad prahom:

| variant | driver | limit | holdout | limit |
|---|---:|---:|---:|---:|
| gamma0 | `1.849590623e-10` | `1e-10` | `3.070015092e-9` | `1e-9` |
| af0 | `1.555001895e-10` | `1e-10` | `3.227055158e-9` | `1e-9` |

Pri af0 zlyhal navyše audit M3 nominal bridge `2.585271113e-8 > 1e-8`.
Immutable REVIEW raw má SHA-256
`F04725F06B29AB596518CA9A9A2C34C6349D82AC17B743E007FB5D81B67E3A10`.

Toto je známy BI upstream precision mechanizmus: nominal BI/.15 prešiel až
cez lossless HP-M1 checkpoint KMPC-108 a exact resume KMPC-112. Jednoduchá
same-matrix korekcia by neuzavrela nezávislý holdout.

## 2. Jediná otázka

Prejdú `gamma0` aj `af0`, ak sa bez opakovania CPQR obnoví presný HP-M1
checkpoint, nanovo sa vypočíta variantový F0 a audit driver plus non-fit
holdout sa zostavia a vyriešia pri 80 dps?

## 3. Zmrazený resume kontrakt

- identita iba `BI/k=.15/gamma0+af0`;
- support accepted `[0,5]`, audit `[0,7]`, M1 depth 7 bez zmeny;
- štyri shardy `gamma0/af0 × accepted/audit`;
- KMPC-108 checkpoint SHA
  `683D867D19324B7B45F3724545FFB1D975DFBED883936298D790C12836E9D995`;
- serialized-state fingerprint
  `402B42E11C3582B4E3E46D047EA917A4C256E552F65C9DB070589150675EBF40`;
- KMPC-109 receipt SHA
  `21EF9A9BF8D6E437CC848BD76EC026C5621534F35C0D88F99D2BFAFAD28118F9`;
- checkpoint HP-M1 sa obnoví v explicitnom poradí a roundtrip musí byť exact;
- F0 sa pre každý variant/support rieši nanovo; checkpointový nominal F0 sa
  nepoužije ako variantový výsledok;
- audit float64 matrix sa zachytí iba na fingerprint/provenance;
- exact audit driver: jedna 80-dps solve, rows/unknowns `104/104`;
- exact holdout: `16×104`, `rows_added_to_driver_solve=0`;
- accepted rank-78 solve sa exact-resume náhradou neprepisuje;
- exact výsledok smie supersedovať iba `M3_driver` a
  `M3_independent_00_0i_holdout`; common, tail, S-C0, background, null a
  `af0` coefficient bridge sa znovu počítajú z variantových coefficient
  stavov a musia samostatne prejsť;
- precision `80 dps`; všetky fyzikálne prahy, rovnice, matrix rows, RHS,
  support a `rcond` bez zmeny;
- každý worker `≤4.8 s`, parent solver calls `0`, jeden immutable pair raw;
- compile/help/smoke/official oddelene s vonkajším limitom `≤10 s`.

## 4. Predregistrované hodnotenie

- checkpoint/receipt/fingerprint, variantové coefficient brány, exact driver
  a non-fit holdout všetko PASS:
  `PASS_C3_BI_K0P15_ZERO_PAIR_HP_M1_EXACT_RESUME_CANDIDATE_ONLY`;
- exact driver alebo holdout ostane otvorený:
  `REVIEW_C3_BI_K0P15_HP_M1_EXACT_BOUNDARY_UNCLOSED`;
- `af0` bridge, common, tail, null alebo background fail zostáva vlastným C3
  REVIEW/STOP kandidátom a nesmie sa supersedovať exact driverom;
- checkpoint/hash/order/parity/timeout/schema chyba je technická bez fyziky;
- BI mód sa neuzavrie pred interným auditom.

## 5. Source freeze pred prvým Python procesom

| artefakt | SHA-256 |
|---|---|
| KMPC-131 four-shard base | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| KMPC-112 JSON-parity exact-resume module | `067CFDBBA95712B04FCD8D571537D751A441B41F4B479FCFB54D7F7AAB281DA5` |
| nový KMPC-134 base | `41332BA6814B7931F518467A95201B2581A564A7AB0AB5970F779FECEF49AB3D` |
| runner 378 | `6B12DEC80AD09D107F551FD1B1FC19D61A993FB1A91FB2A8872DA6EEEAC910D5` |

Hash KMPC-112 modulu bol pred prvým Python procesom overený priamo zo zdroja;
žiadny výpočet pri tejto kontrole nebežal.

## 6. R5 rozpočet

Najviac päť nových live artefaktov: táto predregistrácia, jeden adapter base,
jeden runner, jeden raw a spoločný BI mode audit. Historické HP moduly a rawy
sa nemenia. Externý balík sa vytvorí pri mode closure alebo novom významnom
blockeri; jeho prípadný runtime budget exception musí byť vysvetlený vopred.
