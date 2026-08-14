# FULL RUN-001 — technické zlyhanie výstupného ACL

**Stav:** `TECHNICAL / DO_NOT_INTERPRET`  
**Fyzika vykonaná:** nie.

CLASS načítal vstup, ale skončil pred výpočtom pri pokuse vytvoriť
`class__parameters.ini` v auditnom `D:` adresári:

```text
could not open param_output ... mode "w"
```

MSYS sandbox nemá do tohto adresára zápis. Nezmenil sa CLASS zdroj, K4 ani
štandardné parametre. Povolená oprava zmení iba `root` výstupu na
`external/CLASS/build/full_reference/`, t. j. generovaný build adresár;
vstup a auditný rozsudok ostávajú oddelené od zdroja.
