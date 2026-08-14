# A2 — register koľají na backgrounde A1-K1

**Aktualizované:** 2026-08-14  
**Aktívna koľaj:** žiadna — celá stanica `A2` je `FROZEN_PENDING_A0`
**Naposledy aktívna:** `A2-K4 -> P5 -> B6b-2.12/D2SW16`

## Zmrazenie od 2026-08-14

Zavedená upstream stanica `A0` (`tracks/A0/00_STATION.md`). Do jej
rozhodnutia sa v `A2` **neotvára žiadny nový task, prereg, RC, official run
ani podkoľaj**. Hĺbky nižšie sa nemenia a nič sa nemaže; koľaje zostávajú
živé. Zjemnenie špecifikácie `P5.3` blockeru je od tohto dátumu zakázané
(`AGENTS.md` §4.1).

## Šesť koľají, jeden chýbajúci objekt

Stĺpec **spoločný objekt** je nový (audit 2, V.8). Register to už hovoril
doslova v stavových názvoch, ale nebolo to vidieť pohromade: všetkých päť
záložných rodičov čaká na **ten istý lokálny operátor produkcie a transportu**,
teda na presne to, čo blokuje K4. Korelácia ≈ 1.

**Šesť živých koľají je efektívne jedna možnosť.** Pri no-go zomrie všetkých
šesť naraz, nie postupne. Preto sa hľadaný objekt hľadá **raz**, v konečnom
priestore podľa `AGENTS.md` §11, a výsledok platí pre všetkých šesť. Súčasné
rozdelenie na päť trati s vlastnými adresármi násobí režijné náklady bez
pridania šance.

| Koľaj | Mechanizmus | Stav rodiča | Workflow fáza | Hĺbka | Spoločný objekt s K4 | Vlastný adresár |
|---|---|---|---|---:|---|---|
| `A2-K7` | disipatívny/mediátorový rodič | `LIVE_BACKUP / WAITING_FOR_KERNEL` | `FROZEN_PENDING_A0` | `20/100` | **áno** — lokálny produkčno-transportný operátor | `A2K7/` |
| `A2-K8` | kinetická produkcia | `LIVE_BACKUP / WAITING_FOR_COLLISION_OPERATOR` | `FROZEN_PENDING_A0` | `10/100` | **áno** — ten istý | `A2K8/` |
| `A2-K9` | spoločný produkčno-rozptylový operátor | `LIVE_BACKUP / WAITING_FOR_SHARED_OPERATOR` | `FROZEN_PENDING_A0` | `10/100` | **áno** — ten istý | `A2K9/` |
| `A2-K11` | ortogonálny momentum-drag | `WITHDRAW_FALSE_PASS / LIVE_BACKUP / WAITING_FOR_OPERATOR_AND_FULL_DAE` | `FROZEN_PENDING_A0` | `10/100` | **áno** — ten istý | `A2K11/` |
| `A2-K12` | dvojzložkový popol/párový kernel | `LIVE_BACKUP / WAITING_FOR_PAIR_KERNEL` | `FROZEN_PENDING_A0` | `10/100` | **áno** — ten istý | `A2K12/` |

## Úplný register

| Koľaj | Mechanizmus | Stav rodiča | Workflow fáza | Hĺbka | Vlastný adresár |
|---|---|---|---|---:|---|
| A2-K1 | prenos v CDM rámci | `STOP_SCOPE M-009 / SCIENTIFIC` | closed exact scope | `40/100` | `A2K1/` |
| A2-K2 | striktne barotropické palivo | `STOP_SCOPE M-008 / SCIENTIFIC` | closed exact scope | `30/100` | `A2K2/` |
| A2-K3 | prenos v rámci paliva | `STOP_SCOPE M-010 / SCIENTIFIC` | closed exact scope | `40/100` | `A2K3/` |
| **A2-K4** | entalpicky vážený spoločný energy-frame | **`LIVE / FROZEN_PENDING_A0`** | **`CONTRACT_RC_FROZEN / NO_NEW_TASK`** | **`60/100`** | `A2K4/` |
| A2-K5 | kanonické pole s konformnou väzbou | `STOP_SCOPE M-012 / SCIENTIFIC` | closed exact action | `40/100` | `A2K5/` |
| A2-K6 | premenlivé kinetické miešanie | `STOP_SCOPE M-013 / SCIENTIFIC` | closed exact operator class | `30/100` | `A2K6/` |
| A2-K7 | disipatívny/mediátorový rodič | `LIVE_BACKUP / WAITING_FOR_KERNEL` | `FROZEN_PENDING_A0` | `20/100` | `A2K7/` |
| A2-K8 | kinetická produkcia | `LIVE_BACKUP / WAITING_FOR_COLLISION_OPERATOR` | `FROZEN_PENDING_A0` | `10/100` | `A2K8/` |
| A2-K9 | spoločný produkčno-rozptylový operátor | `LIVE_BACKUP / WAITING_FOR_SHARED_OPERATOR` | `FROZEN_PENDING_A0` | `10/100` | `A2K9/` |
| A2-K11 | ortogonálny momentum-drag | `WITHDRAW_FALSE_PASS / LIVE_BACKUP / WAITING_FOR_OPERATOR_AND_FULL_DAE` | `FROZEN_PENDING_A0` | `10/100` | `A2K11/` |
| A2-K12 | dvojzložkový popol/párový kernel | `LIVE_BACKUP / WAITING_FOR_PAIR_KERNEL` | `FROZEN_PENDING_A0` | `10/100` | `A2K12/` |

A2-K10 patrí backgroundovej route A1-K2 a v tomto strome sa neduplikuje.

`LIVE_BACKUP / WAITING` je fyzikálne živý rodič bez otvoreného dostatočného
contractu. Scoped STOP dcéry a technicky terminálne architektúry zostávajú
v histórii, ale ich stav sa neprenáša na rodiča.

**Zrušené 2026-08-14:** pravidlo *„každá novootvorená implementačná línia
začne vlastný error batch `0/10`"*. Bolo to presne to pravidlo, ktoré
umožňovalo obnovovať rozpočet delením problému (audit 2, V.5). Nahradené
rozpočtom na fyzikálnu otázku nižšie.

Behaviorálne mantinely a scoped dcéry K7/K8/K9/K11/K12 sú v
`00_CONSTRAINT_FEASIBILITY_LEDGER.md`. Ich mapovanie samo nemení hĺbku.

## Chybový rozpočet od 2026-08-14

Pravidlo `0/10` na implementačnú líniu je nahradené rozpočtom na **fyzikálnu
otázku** (`AGENTS.md` §4). Všetkých šesť koľají vyššie zdieľa jednu otázku:

```text
QUESTION_ID           Q-A2-LOCAL-PRODUCTION-TRANSPORT-LAW
QUESTION_ERROR_BUDGET 30
QUESTION_ERRORS_USED  0     (nova otazka, historia sa nepresuva)
QUESTION_STATUS       FROZEN_PENDING_A0
```

Otvorenie novej podkoľaje rozpočet nezvyšuje. Pri vyčerpaní sa vydá
`NO_GO_BY_EXHAUSTION` s presným zoznamom skúšaného — to je publikovateľný
vedecký výsledok, nie zlyhanie.
