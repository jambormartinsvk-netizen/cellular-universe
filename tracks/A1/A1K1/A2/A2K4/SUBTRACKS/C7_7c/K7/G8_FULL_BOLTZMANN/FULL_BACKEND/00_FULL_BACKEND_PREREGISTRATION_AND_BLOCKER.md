# G8 FULL — predregistrácia backendu a architektonický blok

**Pôvodný stav:** `REVIEW_BLOCKED — chýba zdrojovo upraviteľný backend`  
**Fyzikálny verdikt:** žiadny  
**Skóre:** bez zmeny, `90/100`

## Čo FULL musí reálne obsahovať

FULL nie je ďalší testovací script. Musí v jednom reprodukovateľnom backend-e
spojiť:

1. presný K4 background v `H(a)` a konformnom čase;
2. štandardnú atómovú kinetiku, z ktorej vzniknú `x_e`, opacity a visibility;
3. úplný 32/44/56‑stavový lineárny Einstein–Boltzmann systém s oddeleným
   `U_b`, fotónovou teplotou/polarizáciou, free-streaming hierarchiou a
   ne-nulovým autoritatívnym closure;
4. zdokumentovaný TCA switch, konvergenciu `lmax` a úplné constraint ledgery;
5. nulový referenčný beh proti zamrznutému CAMB rozhraniu pred interpretáciou
   K4 výsledku.

SCREEN-S0 až S3 tieto body neprinášajú a nesmú byť povýšené na FULL.

## Overený lokálny stav

Read-only inventár 2026-07-15 našiel lokálny Python balík CAMB 1.6.6 s
`cambdll.dll`, `camb.exe` a Python wrappermi, ale nenašiel zdrojový strom
CAMB/CLASS ani `recfast`, `hyrec`, Fortran zdroje alebo build súbory
príslušného backendu. Skompilovanú DLL nemožno auditovateľne upraviť tak,
aby používala K4 `H(a)`.

Projektový `scripts/00_DO_NOT_RUN_SCRIPT_REGISTRY.md` už tiež eviduje,
že skorší symbolic CAMB source path bol environment-blocked pre chýbajúci
Fortran compiler. To nezabíja A2-K4; znamená to iba, že teraz nemáme
potrebný produkčný nástroj.

## Prečo sa nesmie použiť obchádzka

- CAMB s `w0/wa` surrogate nie je presný K4 background;
- `chi=100` z SCREEN-S2/S3 nie je atómová opacity;
- vlastná rýchla aproximácia rekombinácie bez nezávislej validácie by
  nedokázala splniť FULL kritériá visibility ani nulový referenčný beh.

Každá z týchto ciest je užitočná ako SCREEN, ale ako FULL by bola zavádzajúca.

## Potrebný ďalší vstup

Je potrebný jeden z nasledujúcich reprodukovateľných vstupov:

1. zdroj CAMB s build nástrojom (typicky podporovaný Fortran toolchain), alebo
2. zdroj CLASS s jeho build závislosťami, alebo
3. iný otvorený, zdrojovo auditovateľný Boltzmann + recombination backend,
   pri ktorom možno explicitne nahradiť background za K4.

Po dodaní sa najprv vykoná **bez zmeny zdroja** bounded build/reference test
na štandardnom backgrounde; až potom oddelený K4 adapter, test nulového
limitu a jedna krátka FULL case. Žiadny externý zdroj sa nesťahuje ani
neinštaluje bez výslovného súhlasu používateľa.

## Rozhodnutie

G8 je `SCREEN COMPLETE / FULL BACKEND BLOCKED`. Toto je technický a
architektonický stav, nie STOP teórie a nie dôkaz či vyvrátenie A1-K1.

## Aktualizácia 2026-07-15 — blok odstránený

Zdrojový CLASS/HyRec backend bol získaný, skompilovaný a jeho štandardný
nulový reference beh prešiel. Autoritatívny audit je
`ARTIFACTS/RUN_FULL_000_001_CLASS_REFERENCE_BACKEND_AUDIT.md`.

Aktuálny stav je preto `FULL BACKEND READY / K4 ADAPTER NOT RUN`. Pôvodný
blok sa nemaže: vysvetľuje, prečo predchádzajúce SCREEN-y nemohli byť FULL.
