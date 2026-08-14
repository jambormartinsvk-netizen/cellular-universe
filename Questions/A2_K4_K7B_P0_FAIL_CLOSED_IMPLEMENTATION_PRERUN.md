# A2-K4 / K7b P0 — predregistrácia fail-closed implementácie 189/190

Dátum: 2026-07-15  
Typ očakávania: `REGRESSION`  
Skóre: `NONE`; A2-K4 ostáva `66.5/100`

## Zmrazený rozsah

Nový skript 189 smie oproti 175 zmeniť iba validáciu existencie a presného typu `reduced_rank/free_count`, logicky strážené porovnanie ich rovnosti, identitu verdictu a explicitnú syntetickú fault injection. Rovnice, parametre, fyzikálny `mu`, koeficienty, tolerancie, 13 RHS a baseline payload sa nemenia.

Skript 190 vykoná dve pozitívne NID regresie 175 versus 189, dve nezmenené pozitívne NIV brány cez 166 a tri negatívne behy 189: odstránený `reduced_rank`, odstránený `free_count` a odstránené oba.

## Pozitívne očakávania

| Mód/povrch | D activity rel. | Stav/allowance | RHS/allowance |
|---|---:|---:|---:|
| NID/deep | `5.9511e-3` | `9.4022e-6` | `8.5918e-13` |
| NID/shallow | `1.0921e-4` | `8.0083e-6` | `6.3485e-12` |
| NIV/deep | nevyžadované | `3.2127e-5` | `3.5503e-11` |
| NIV/shallow | nevyžadované | `3.8442e-5` | `2.6233e-10` |

Tabuľkové hodnoty sú zaokrúhlené a kontrolujú sa relatívnou odchýlkou najviac `1e-4`. NID baseline 175 a kandidát 189 však musia mať bitovo rovnaký SHA-256 fingerprint kanonického fyzikálneho payloadu: background, projected seeds, state comparison, 13 RHS audit, najhoršie pomery, D activity a solver audit. Runtime, názov testu, verdict, nové rank checky a fault metadata sú z fingerprintu vylúčené.

Povinné presné hodnoty solvera: `fixed_count=30`, `free_count=58`, `reduced_rank=58`, `hard_conflict_count=0`, `fixed_max_absolute_error < 1e-60`. Pozitívny 189 musí mať rank kľúče prítomné, oba typu presne `int` (nie `bool`) a guarded full-rank check `True`.

## Negatívne očakávania

Každý z troch fault-injection behov musí:

- skončiť exit kódom `1`, nie `0`;
- vrátiť REVIEW verdict 189;
- mať `rank_keys_present=False`, `rank_values_plain_int=False` a guarded full-rank check `False`;
- nikdy nevyhodnotiť chýbajúce oba kľúče cez `None == None` ako PASS;
- zachovať ostatný fyzikálny payload; nejde o fyzikálny beh ani rozsudok K4.

## Formálne a časové brány

- pred behom: aktuálny korpusový checker target, AST/`py_compile`, CLI help a krátky JSON smoke-test;
- child interný limit najviac 8 s;
- agregátor interný limit 15 s a externý limit 20 s;
- kontrola procesu najneskôr po 10 s;
- timeout, invalid JSON, marker count iný než 1 alebo zmena fyzikálneho fingerprintu znamená `REVIEW`, nie fyzikálnu smrť K4;
- ak sa po výsledku zmení tolerancia alebo očakávanie, pôvodný text ostáva a zmena patrí do novej podkoľaje.
## Operatívny nástupca checkeru 191

Pridanie 189/190 zámerne poruší zmrazený počet 192 v historickom checkeri 188. Skript 188 sa nemení. Nový 191 smie oproti nemu zmeniť iba očakávaný počet korpusu, názov count checku/testu a pridať 188 do karantény ako `SUPERSEDED`.

Po vytvorení 189–191 sa očakáva: **195** ostatných Python súborov z pohľadu 191, **63** karanténnych položiek, syntaxové chyby iba 118/119, neúplný vstup iba 186 a nula spustených cieľov. Target 189 aj 190 musí byť `NOT_IN_QUARANTINE`; tento stav stále nie je fyzikálny PASS.