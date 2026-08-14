# FULL RUN-000 — nezmenený CLASS reference build: očakávanie

Pred K4 adapterom sa najprv skompiluje **nezmenený** CLASS commit
`e85808324f51fc694d12e3ed7439552a3c3f9540`. Tento krok netestuje teóriu;
iba overuje reprodukovateľnosť nástroja a štandardnej recombination cesty.

Build používa izolovaný MSYS2 `gcc/make`, `HOME=/tmp`, bez zmeny systémového
PATH. Má interný shell deadline 45 s a vonkajší limit 55 s. Po PASS nasleduje
jediný štandardný `default.ini` smoke-run s vlastným limitom a immutable
logom. Po timeout/compile chybe je stav `TECHNICAL REVIEW`; nevyvodzuje sa
nič o K4 ani A1-K1.

## Dodatok po prvom technickom pokuse

Pôvodný build skončil pred kompiláciou na neprístupnom `C:\msys64\tmp`.
Rovnaký build sa smie raz zopakovať bez zmeny zdroja s explicitným
`TMPDIR=/d/Teoria/.tmp_msys`; tento adresár je v projekte a slúži iba na
prechodné súbory compileru. Dôvod a zachovaný prvý pokus sú v `HISTORY/`.

## Dodatok po druhom technickom pokuse

Workspace `TMPDIR` opravil ACL problém. Build sa následne zastavil na
viditeľnosti štandardnej math macro `M_PI_2` v UCRT `g++` režime. Posledný
dovolený nezmenený source build pridá len `_GNU_SOURCE` do preprocesora C++.
Neopravuje ani neupravuje žiadny CLASS súbor. Ďalšie pokusy po jeho zlyhaní
nie sú povolené bez nového auditovaného rozhodnutia.
