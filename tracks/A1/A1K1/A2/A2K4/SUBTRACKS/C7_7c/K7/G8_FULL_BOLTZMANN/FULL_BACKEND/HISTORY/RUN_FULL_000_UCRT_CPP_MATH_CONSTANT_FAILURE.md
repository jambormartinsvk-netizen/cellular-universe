# FULL RUN-000 — technické zlyhanie UCRT C++ math constants

**Stav:** `TECHNICAL / DO_NOT_INTERPRET`  
**Fyzika vykonaná:** nie  
**Predchádzajúca oprava:** workspace `TMPDIR` prešla; compiler už vytvoril
viacero objektov.

Build nezmeneného CLASS sa zastavil v `tools/hyperspherical.c` kompilovanom
cez `g++` s chybou:

```text
'M_PI_2' was not declared in this scope
```

Ide o známu rozdielnosť math macro viditeľnosti pri UCRT/C++ strict standard
mode, nie o zmenu zdroja ani o fyzikálny výpočet. Povolený je už len jeden
build pokus s compiler definíciou `_GNU_SOURCE` dodanou na command line
(`CPP=... -D_GNU_SOURCE ...`). Ak zlyhá, FULL backend ostáva technicky
blokovaný až do samostatného auditovaného výberu toolchainu.
