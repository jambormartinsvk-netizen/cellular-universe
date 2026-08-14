# R3 refreeze po externom technickom STOP-e

**Dátum:** 2026-07-17  
**Stav:** `R3_READY_FOR_REPEAT_EXTERNAL_AUDIT`  
**Pôvodný problém:** `R2_TECHNICAL_STOP_MISSING_PREREQUISITE`

## Čo externý audit zistil

Smoke vetva R2 prešla, ale oficiálna `--audit` vetva skončila fail-closed
na `FileNotFoundError`. Runner 280 vyžaduje raw výsledok KMPC-035 a overuje
jeho hash, no R2 ho nepribalila. Fyzika preto cez predpísanú cestu nebola
spustená.

## Jediná obsahová oprava balenia

Do R3 boli pridané dve byte-identické kópie toho istého zmrazeného zdroja:

1. `EVIDENCE/015__KMPC035_PREREQUISITE_RAW_RESULT.json`;
2. `REPRO/scripts/results/k_mpc_005/RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json`.

Zdroj:
`scripts/results/k_mpc_005/RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json`

SHA-256 všetkých troch kópií:
`A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01`.

## Čo sa nezmenilo

- runner 280 a všetky tri base moduly;
- preregistrácia a zmrazené prahy;
- KMPC-036 autoritatívny raw JSON;
- rovnice, parametre a interpretácia výsledku;
- route, hĺbka, skóre a projektový `REVIEW`.

Do reprodukčného opisu pribudla iba vetva pre platformovo odlišnú
podmnožinu floor-level failov a povinnosť zaznamenať numerické prostredie.
Nie je to spätná zmena prahu ani povýšenie výsledku.

## Kritérium úspechu opakovaného auditu

R3 opravila technickú medzeru iba vtedy, ak oficiálna `--audit` cesta:

1. nájde a hashovo prijme KMPC-035 prerequisite;
2. neskončí pôvodným `FileNotFoundError`;
3. vytvorí KMPC-036 auditný výsledok alebo iný presne zdokumentovaný
   technický výsledok.

Aj úspešná reprodukcia nemení automaticky `REVIEW` na `PASS`.
