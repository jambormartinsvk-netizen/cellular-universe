# FULL backend — CLASS/HyRec source build a nulový referenčný beh

**Backend verdict:** `PASS_STANDARD_REFERENCE_BACKEND`  
**K4 FULL verdict:** `NOT RUN`  
**Fyzikálne skóre G8:** bez zmeny, `90/100`

## Zamrazená provenance

- upstream: `https://github.com/lesgourg/class_public`;
- shallow source commit: `e85808324f51fc694d12e3ed7439552a3c3f9540`;
- compiler: izolovaný MSYS2 UCRT `gcc 16.1.0`, `make 4.4.1`;
- build: nezmenený CLASS source, `HyRec2020` a `RecfastCLASS` sú zahrnuté;
- jediný UCRT portability flag: `_GNU_SOURCE` v C++ compiler command line;
- binárka `class.exe` SHA-256:
  `BE62910540B57FE47C5964C6DF3EC73B79CE3164AAE354608DDD0BF095ECD7A3`.

Technické pokusy s MSYS temporary directory a POSIX cestou v natívnej
Windows binárke ostávajú v `HISTORY/`. Neskorší audit obmedzil pôvodnú
interpretáciu ACL: konečný koreň bol formát `root=/d/...`, nie teória ani
rekombinácia.

## Nulový referenčný beh

`CLASS_REFERENCE_SMOKE_V3.ini` je štandardná plochá ΛCDM konfigurácia s
HyRec, `l_max_scalars=100`, bez K4 modifikácie. Skončila návratovým kódom 0
v približne 1.5 s (limit 45/55 s) a vytvorila:

| Artefakt | SHA-256 |
|---|---|
| `class__background.dat` | `BE351C29C4932526649D604FD723DD7F0F857917649BCD21B3FFA44BD1C71C7A` |
| `class__thermodynamics.dat` | `6AA565EC9EE6C44E04599A41588EDCB55B3C9F7B76CF8A539D16E3557A36B6EE` |
| `class__cl.dat` | `D9A10CD76A1830276FD1C575C181C8BAA6BFB42545BA9AF182149C207D55D970` |

Background export je konečný od `z=10^14` po `z=0`; thermodynamics export
je konečný od dneška po `z=5×10^6`, obsahuje štandardný `x_e`, Thomsonovu
opacity a teplotné položky. To je dostatočné na potvrdenie, že build,
štandardná rekombinácia a lineárna pipeline fungujú.

## Čo ešte chýba k G8 FULL

1. PASS `03_K4_BACKGROUND_UNIVERSALITY_GATE.md`: odvodiť jedno univerzálne
   k‑nezávislé `H_K4(a)`;
2. oddelený K4 adapter v CLASS background module, uložený ako malý patch;
3. test nulového limitu, kde adapter vráti štandardný CLASS background;
4. porovnanie K4/štandardnej ionizácie, opacity a visibility;
5. plná 32/44/56 stavová G8 konfigurácia, TCA switch, constraints a
   `lmax` convergence na K4; až potom G8 +5 a G9.

Tento audit nezverejňuje ani neodvodzuje novú predpoveď. Potvrdzuje len, že
už máme zdrojovo auditovateľný nástroj, na ktorom sa K4 adapter môže poctivo
stavať.
