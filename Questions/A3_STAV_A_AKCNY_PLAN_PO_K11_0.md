# A3/Q20 — celkový stav po audite A2-K11.0

**Dátum:** 2026-07-13  
**Nahrádza pre budúce riadenie:**
`Questions/A3_STAV_A_AKCNY_PLAN_PO_K7_0.md`  
**Starší súbor sa nemaže a zostáva historickým stavom pred auditom K11.**

| Koľaj | Kanonický stav | Max. hĺbka |
|---|---|---:|
| A2-K1 | `MŔTVA M-009` | `45/100` |
| A2-K2 | `MŔTVA M-008` | `25/100` |
| A2-K3 | `MŔTVA M-010` | `45/100` |
| A2-K4 | `MŔTVA M-011` | `50/100` |
| A2-K5 | `MŔTVA M-012` | `75/100` |
| A2-K6 | `MŔTVA M-013` | `60/100` |
| A2-K7 | `PREŽÍVA K7.0` | `30/100` |
| A2-K8 | `ČAKÁ` | `5/100` |
| A2-K9 | `ČAKÁ` | `5/100` |
| A1-K2/A2-K10 | `ČAKÁ`; backgroundová vetva | `5/100` |
| **A2-K11** | **`PREŽÍVA IBA FORMULAČNÚ BRÁNU`** | **`15/100`** |

Všetky dôvody smrti aj steny živých koľají sú priamo v
`Audit/A2_KATALOG_STAV_SKORE_A_DOVOD_SMRTI_K1_AZ_K11.md`.

## Rozhodnutie o skripte 45

`PASS_S8_K1b_SUPERHORIZON_GATE` je zamietnutý. Dôvody:

- nesprávne znamienko sily pri deklarovanej konvencii;
- neúplné/nesprávne interakčné rovnice;
- relatívne `00` rezíduum `1.0`;
- výsledok pod `atol`;
- zlyhanie amplitúdového a krokového testu;
- žiadny výpočet `S8`.

Toto je neplatný dôkaz v rámci K11, nie dôvod vymazať mechanizmus alebo
staré výpočty.

## Aktívny ďalší krok

Aktívna je **K11.1**: odvodiť plusovo orientovaný momentum-transfer z
lokálneho a v hustotných limitoch pravidelného operátora. Až potom sa smie
znovu zostaviť úplná perturbačná sústava.

K7.1 zostáva druhou prioritou a jej stav `30/100` sa nemení.

