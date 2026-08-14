# A3/Q20 — celkový stav a akčný plán po retrospektíve K1–K5

**Dátum:** 2026-07-13  
**Bezprostredný auditný krok:** A2-K4.1  
**Nezmenená vývojová koľaj:** A2-K7, koherentná K1a2b-K1

| Hlavná koľaj | Stav | Kanonické skóre | Max. hĺbka potomka/poznámka |
|---|---|---:|---:|
| A2-K1 | `MŔTVA M-009` | `45/100` | — |
| A2-K2 | `MŔTVA M-008` | `25/100` | — |
| A2-K3 | `MŔTVA M-010` | `45/100` | — |
| **A2-K4** | **`ZNOVU OTVORENÁ; M-011 POZASTAVENÁ`** | **`50/100`** | čaká úplnú K4.1 bázu módov |
| A2-K5 | `MŔTVA M-012` | `75/100` | — |
| A2-K6 | `MŔTVA M-013` | `60/100` | — |
| **A2-K7** | **`PREŽÍVA K7.0`** | **`30/100`** | **`42/100` (mŕtva K1a2a)** |
| A2-K8 | `ČAKÁ` | `5/100` | — |
| A2-K9 | `ČAKÁ` | `5/100` | — |
| A1-K2/A2-K10 | `ČAKÁ` | `5/100` | — |
| A2-K11 | `PREŽÍVA IBA FORMULAČNÚ BRÁNU` | `15/100` | — |

## Poradie práce

1. vykonať K4.1 úplnú superhorizontovú bázu a rozhodnúť, či sa M-011 znovu
   potvrdí alebo K4 postúpi;
2. aktualizovať tento stavový dokument novým nemazacím dodatkom;
3. potom pokračovať už založenou K7 koherentnou podkoľajou
   K7.1a-K3.1-K2.2-K1a2b-K1;
4. K8–K11 nemenia poradie bez samostatného rozhodnutia.

## Dôvod priority K4.1

Retrospektíva nezmenila rovnice ani výsledok skriptu 30. Zistila však, že
historická brána porovnala `T_K4/T_null` s `e`, hoci `T_null` silno zaniká.
Absolútny transfer bol iba `1.587<e` a doplnený adiabatický mód
neexplodoval. K4 preto nemožno ponechať ako konečne mŕtvu ani označiť za
preživšiu bez úplného spektra módov.

