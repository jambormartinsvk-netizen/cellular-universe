# A2 katalóg — dodatok jemnej desatinnej hĺbky

**Dátum:** 2026-07-14  
**Nahrádza:** iba spôsob zobrazenia hĺbky v aktuálnych stavových tabuľkách  
**Nemení:** stav koľají, dôvody smrti, skripty ani najhlbší vykonaný test

## Aktuálna porovnávacia tabuľka

| Koľaj | Stav | Jemná hĺbka | Posledná úplná brána | Najhlbší vykonaný / otvorený test |
|---|---|---:|---|---|
| A2-K1 | `MŔTVA M-009` | `40.0/100` | G4 | G5 no-go |
| A2-K2 | `MŔTVA M-008` | `30.0/100` | G3 | G6 FAIL; G4–G5 neprešli sekvenčne |
| A2-K3 | `MŔTVA M-010` | `40.0/100` | G4 | G5 no-go |
| **A2-K4** | **ŽIVÁ** | **`66.0/100`** | **G6 PASS** | **G7/C7.7 otvorená** |
| A2-K5 | `MŔTVA M-012` | `40.0/100` | G4 | G6 vykonaná; G8 hybridný screen FAIL |
| A2-K6 | `MŔTVA M-013` | `30.0/100` | G3 | G6 presný no-go |
| A2-K7 | `PREŽÍVA CEZ PODKOĽAJE` | `20.0/100` | G2 | G3 otvorená |
| A2-K8 | `ČAKÁ` | `10.0/100` | G1 | G2 otvorená |
| A2-K9 | `ČAKÁ` | `10.0/100` | G1 | G2 otvorená |
| A1-K2/A2-K10 | `ČAKÁ; INÁ A1 VETVA` | `10.0/100` | G1 | nová A1/G2 otvorená |
| A2-K11 | `PREŽÍVA IBA HYPOTÉZU` | `10.0/100` | G1 | G2/G3 otvorená |
| A2-K12 | `PREŽÍVA CEZ K12-K2/K3` | `10.0/100` | G1 | G2 otvorená |

Desatinná nula pri starších koľajach neznamená, že v ďalšej bráne nebola
vykonaná práca. Znamená, že nemajú zmrazený sekvenčný jemný ledger, z ktorého
by sa dali prideliť porovnateľné body bez spätnej svojvôle. Preto sa naďalej
musí čítať aj stĺpec najhlbšieho vykonaného testu.

## K4

K4 je prvá koľaj prepočítaná novou metódou:

```text
staré zobrazenie: 60/100, G7 otvorená
nové zobrazenie: 66.0/100, G6 PASS, G7 otvorená
```

Nejde o zmenu fyzikálneho verdiktu. Rozpis šiestich získaných bodov a
budúcich desatinných checkpointov je v
`Audit/A2_DECIMAL_GATE_DEPTH_SCORING_AND_K4_RECALCULATION.md`.

## Povinné zachovanie mŕtvych koľají

Tento dodatok nič nemaže. Pri každej mŕtvej koľaji zostávajú povinné:

1. posledná úplná brána a maximálna jemná hĺbka;
2. najhlbší vykonaný test aj vtedy, keď preskočil medzibránu;
3. fyzikálny dôvod smrti a obmedzenie jeho platnosti;
4. skripty, výstupy, erratá a kontrolné súčty.

