# Dodatok k 05 — register formálnych chýb Python skriptov (SK)

Dátum: 2026-07-15  
Stav: záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR29 už prikazuje externý časový limit každému spusteniu a určuje, že timeout nie je fyzikálny FAIL. AR39 zachováva neúspešnú stopu pri opravách katastrofického odčítania. AR50–AR52 riešia tvrdé kotvy, importované polia a dosiahnuteľnosť generovaného kódu. Chýbalo všeobecné pravidlo, ktoré pri každej formálnej Python chybe vyžaduje jednotný ledger, predbehovú syntaxovú/serializačnú kontrolu a zápis preventívneho poučenia. AR53 vypĺňa iba túto medzeru a timeoutové prahy AR29 nemení.

## AR53 — Každá formálna Python chyba musí zostať v registri aj s prevenciou

Pred prvým numerickým behom nového alebo generovaného Python skriptu sa musí s externým limitom vykonať najmenej `py_compile`, parser/CLI smoke-test a podľa typu výstupu JSON serializačný smoke-test. Pri generovanom zdroji sa musí skompilovať výsledný text, nie iba wrapper.

Ak nastane syntaxová, parserová, importná, markerová, serializačná, CLI, dátovo-cestová alebo runtime-API chyba:

- pôvodný skript a výstup sa zachovajú;
- zapíše sa presná exception, koreňová príčina a či sa fyzika vôbec vykonala;
- výsledok dostane `TECHNICAL_ERROR/REVIEW`, nie fyzikálny PASS alebo smrť;
- oprava vznikne ako nový číslovaný skript alebo explicitne auditovaný nemenný wrapper;
- do `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md` sa pridá preventívna kontrola, ktorá má zabrániť opakovaniu rovnakej triedy chyby.

Úspešný `py_compile` nie je dostačujúci dôkaz: musí ho doplniť minimálny behaviorálny smoke-test schopný zachytiť poradie kľúčov, markerovú cestu, serializáciu, fail-open logiku a identitu vykonanej vetvy.

AR29 zostáva samostatne povinné pri každom spustení: externý timeout sa nesmie vynechať ani vtedy, keď skript obsahuje interný deadline.

## Q78 — Kde je trvalo zapísaná povinnosť evidovať chyby a timeouty?

Globálna pamäť asistenta medzi nezávislými úlohami nie je garantovaná. Autoritatívnou projektovou pamäťou sú:

- AR29 a `scripts/00_EXECUTION_TIME_LIMITS.md` pre každý externý/interný časový limit;
- AR53 a `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md` pre formálne a implementačné chyby;
- auditné MD a zachované staré skripty pre konkrétny dôvod a spätnú reprodukciu.

Ak budúca práca tieto súbory najprv načíta, pravidlá prežijú aj nový chat alebo zmenu asistenta.
