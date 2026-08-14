# Register skriptov — predregistrované očakávania korpusového auditu

Dátum: 2026-07-15  
Stav: zapísané pred vytvorením a prvým behom auditného checkera

## Rozsah

Audit iba číta všetky `scripts/*.py`; žiadny cieľový skript neimportuje ani nespúšťa. Vykoná parser/`compile()` kontrolu zdrojového textu, AST kontrolu vstupného bodu, scan známych chybových vzorov a porovnanie s ručne auditovanou karanténou.

Zmrazený počet pri predregistrácii: **192 Python súborov**. Stav sa eviduje podľa celého názvu, nie iba čísla, pretože čísla 45, 46, 47 a 61 majú viac súborov.

## Očakávania

Typ: `REGRESSION + DISCOVERY`.

- Očakávané syntaxové zlyhania: skripty 118 a 119, už zachované ako `SYNTAX_ERROR_UNCLOSED`.
- Očakávaný syntakticky platný, ale nedokončený/neaktívny súbor: 186, končiaci markerom `__K7C3D_CONTINUE__` bez autoritatívneho výstupu.
- Očakávané známe triedy: JSON NumPy/SymPy skaláre, nesprávna markerová cesta, fail-open `.get()==.get()`, nedosiahnuteľný legacy solver, chýbajúci compiler/backend, timeoutová slepá podkoľaj, fyzikálne neautoritatívny alebo nahradený skript.
- Aktuálne revízie 66 a 67 sa očakávajú syntakticky funkčné: ich staré serializačné hash revízie sú v erratách, ale dnešný zdroj už obsahuje `int(...)`/`bool(...)` opravy.
- Audit nesmie označiť `REVIEW` alebo fyzikálne mŕtvy, ale reprodukovateľný skript za technicky nekompilovateľný. Tieto kategórie sa musia oddeliť.

## Povinné kategórie registra

- `ACTIVE_AUTHORITATIVE` — smie sa používať podľa svojho rozsahu;
- `RUNNABLE_REVIEW_ONLY` — iba historická/regresná diagnostika, nie nový PASS;
- `DO_NOT_USE_PHYSICS` — môže bežať, ale jeho fyzikálny verdict je zamietnutý alebo nahradený;
- `DO_NOT_RUN_TECHNICAL` — známa formálna/runtime chyba alebo nedokončený súbor; spustiť iba pri explicitnom audite reprodukcie chyby;
- `ENVIRONMENT_BLOCKED` — v aktuálnom prostredí chýba backend/compiler;
- `SUPERSEDED` — existuje autoritatívny nástupca; starý súbor sa bežne nespúšťa;
- `UNCLASSIFIED_REVIEW` — checker našiel podozrenie, ktoré vyžaduje ručný audit.

## Rozhodovacie kritériá

- `PASS_INVENTORY`: všetkých 192 súborov je prečítaných; známe syntaxové chyby sú presne lokalizované; každý známy DO_NOT_RUN súbor má dôvod a nástupcu alebo explicitné `none`; checker nevykoná cieľovú fyziku.
- Nová syntaxová chyba mimo 118/119: `REVIEW_NEW_FORMAL_ERROR` a okamžitý zápis do error ledgeru.
- Nefunkčný súbor bez auditného dôvodu: `REVIEW_UNDOCUMENTED_FAILURE`.
- Nezhoda medzi centrálnym registrom a zdrojovým scanom: `REVIEW_STATUS_DRIFT`.

## Limity

- interný limit checkera: 15 s;
- externý limit: 20 s;
- žiadny target subprocess;
- kontrola procesu najneskôr po 10 s;
- timeout znamená `REVIEW_UNCLOSED`.

## Očakávaný výstup

JSON súhrn s počtom súborov, syntaxovými chybami, súbormi bez vykonateľného vstupu, nálezmi známych vzorov, karanténnymi kategóriami a kontrolou, že všetky menované súbory na disku existujú. Po behu sa výsledok prepíše do centrálneho MD registra; pôvodné skripty sa nemenia.
