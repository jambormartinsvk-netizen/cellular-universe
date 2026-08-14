# FULL RUN-000 — technické zlyhanie MSYS temporary directory

**Stav:** `TECHNICAL / DO_NOT_INTERPRET`  
**Fyzika vykonaná:** nie  
**Čas:** približne 2 s, pod oboma limitmi.

Nezmenený CLASS build spustil prvé dva `gcc` príkazy, ale oba skončili pred
kompiláciou s:

```text
Cannot create temporary file in C:\msys64\tmp\: Permission denied
```

Koreň je ACL dočasného adresára izolovaného MSYS2 pod sandboxom. Zdroj CLASS
ani jeho Makefile neboli upravené. Povolená jediná technická oprava je
nastaviť `TMPDIR=/d/Teoria/.tmp_msys` a znovu spustiť ten istý nezmenený
build s rovnakými limitmi. Nesmie sa meniť optimalizácia, fyzika ani zdroj.
