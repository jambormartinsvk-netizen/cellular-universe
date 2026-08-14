# Audit upratania koľají, skriptov a base modulov

**Dátum:** 2026-07-16  
**ID:** `ORG-V2-P1-AUDIT-01`  
**Rozsah:** iba organizácia, vlastníctvo, odkazy a hashe; žiadny fyzikálny
Python ani nový fyzikálny verdikt.

## Výsledok

`PASS_ORGANIZATION_WITHOUT_PHYSICAL_MOVE`

Historické skripty, výsledky a audity neboli presunuté ani kopírované.
Namiesto toho vznikla route vrstva s jedným vlastníkom a presnou väzbou na
pôvodnú cestu. Tým zostalo zachovaných najmenej 468 známych historických
závislostí a auditných citácií.

## Kontroly

| Kontrola | Výsledok |
|---|---|
| A2 route uzly na A1-K1 | K1–K9, K11, K12 majú `00_TRACK`, ARTIFACTS, BASE a HISTORY |
| oddelená background route | A1-K2/A2-K10 vytvorená bez prenosu výsledkov A1-K1 |
| A2-K4/P5 detail | samostatné BASE, RUNNERS, RESULTS a AUDIT_THREADS registre |
| base moduly | 11 fyzikálnych modulov skontrolovaných proti registrovanému SHA-256 |
| hash nezhody | `0/11` |
| SK/EN AR69 | po jednom identifikátore v tematickom dodatku aj v kumulatívnom 05c |
| root-prefix Markdown odkazy | prvý beh: 151 jedinečných, dve navigačné chyby; obe opravené |
| finálny link check | 157 jedinečných explicitných ciest, po oprave `0` chýbajúcich |
| Python | nespustený; nebol potrebný pre organizačný audit |

## Dve opravené navigačné chyby

1. generický text `A2Kx` vyzeral ako skutočná cesta; nahradený odkazom na
   konkrétny A2 track register;
2. starší K7 stav používal skrátené `08_..._RESULT_SK.md`; nahradený plným
   názvom `08_P3_FULL_BACKGROUND_VS_TRUNCATED_K7_RESULT_SK.md`.

## Base architektúra

Existujúce moduly vznikli bez formálnej verzie `vNNN`. Namiesto tichého
premiestnenia alebo premenovania sú označené `LEGACY_UNVERSIONED` a zmrazené
hashom. Register uvádza jedného vlastníka, importujúce runnery a fyzikálny
scope. Oprava musí vytvoriť novú verziu/hash a rozdielový rerun všetkých
dotknutých manifestov.

## Prečo sa súbory fyzicky nepresunuli

Inventár z 2026-07-15 našiel 468 väzieb, vrátane
`Path(__file__).with_name(...)`, generovaných wrapperov a SHA manifestov.
Navyše aktuálny adresár nie je potvrdený funkčným Git baseline stavom.
Fyzická migrácia by preto zhoršila auditovateľnosť. Je povolená až po Git
baseline, úplnej `OLD_PATH → NEW_PATH` mape, kontrole hashov a komponentovom
presune s regresnými bránami.

## Oporné body

- `tracks/00_READ_FIRST.md`;
- `tracks/00_ROUTE_AND_ARTIFACT_LAYOUT_SK.md`;
- `tracks/A1/A1K1/A2/00_TRACK_REGISTER.md`;
- `scripts/00_ROUTE_SCRIPT_INDEX.md`;
- `scripts/baseScripts/00_MODULE_OWNERSHIP_REGISTER.md`;
- `Audit/00_ROUTE_AUDIT_INDEX.md`;
- `Questions/00_ROUTE_DOCUMENT_INDEX.md`.
