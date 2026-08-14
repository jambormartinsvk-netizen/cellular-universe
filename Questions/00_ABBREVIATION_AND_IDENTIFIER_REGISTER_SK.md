# Register skratiek a identifikátorov — SK

Dátum: 2026-07-15  
Stav: autoritatívny navigačný register; fyzikálne definície zostávajú v príslušných odvodeniach

## Ako čítať cestu

| Zápis | Význam |
|---|---|
| `A1`, `A2`, `A3` | kontrolné stanice, nie koľaje |
| `K1`, `K2`, ... | koľaj alebo lokálna podkoľaj; význam je určený úplnou cestou |
| `A2-K4` | štvrtá koľaj testovaná na stanici A2 |
| `A1K1 → A2K4` | route prefix: doteraz zvolená cesta cez stanice |
| `C7.7c` | historické ID konkrétnej aktivity/úplnosti evolučného species/mode ledgeru v A2-K4; nie nová stanica |
| `C7.7c-K1...K7` | alternatívne numerické formulácie tej istej C7.7c brány |
| `K7a` | projektovaná báza `D,M` a Jacobián |
| `K7b` | počiatočné koeficienty a constrainty bez ODE |
| `K7c` | evolúcia a numerická konvergencia projektovanej sústavy |
| `K7d` | plánovaná úplná activity/constraint brána; zatiaľ nedosiahnutá |
| `J1...J4b`, `BR1...`, `RG...` | lokálne diagnostické alebo reformulačné vetvy; plný význam musí byť v `00_CURRENT_STATE.md` daného uzla |

`K4` bez prefixu je zakázané v rozhodovacom dokumente, pretože môže znamenať
`A2-K4` alebo `C7.7c-K4`. Používa sa úplná cesta.

### Stabilita označení staníc a koľají

V ľudskom texte sa `A1/A2/A3` číta ako **kontrolná stanica** a `K` ako
**koľaj**. V angličtine sú odporúčané slová *verification station* a
*track*. Samotné ID sa však nemenia:

- `S1` už označuje auditnú triedu `S1_LOCAL_CORRECTABLE_SAME_TRACK`;
- `T1` už označuje `T1_TECHNICAL_NO_CLAIM_REACH` a písmeno `T` sa používa
  aj pre tenzorové/časové objekty;
- premenovanie A/K by rozbilo historické hashe, route cesty a auditné
  balíky bez pridania fyzikálnej informácie.

## Namespace fáz a balíkov

| Stabilné ID | Krátky historický alias | Význam |
|---|---|---|
| `SCI-A2K4-C7G5-K7C-P0` | P0 | fail-closed provenance/regresná brána K7b |
| `SCI-A2K4-C7G5-K7C-P1-RK4` | P1 | čistá samostatná reprodukcia RK4 na 100/200/400 krokoch |
| `SCI-A2K4-C7G5-K7C-P2-MLEDGER` | P2, K7c.3d | diagnostický ledger deviatich členov `M'`; ďalší vedecký krok |
| `ORG-V2-P1` | organizačná fáza 1 | neinvazívny strom, indexy, manifesty a história bez presunu zdrojov |
| `ORG-V2-P2` | organizačná fáza 2 | neskorší fyzický presun po Git/SHA baseline |
| `BASE-V001-PARITY-197` | base pilot | extrakcia skriptu 197 do kandidáta spoločného jadra a paritný audit |
| `AUD-C7G5-K7C-P1-RK4` | externý RK4 audit | nezávislý audit ne-RK4 pomeru a normy |
| `ZEN-v3.18` | Zenodo v3.18 | publikačný balík; nie výpočtová fáza P2 |

Krátke `P0/P1/P2` sa smie použiť iba v dokumente, ktorého hlavička obsahuje
plnú cestu. V centrálnom pláne, route registri a externom audite sa používa
stabilné ID.

## Jednotné gate ID C7-W1

| Gate | Význam | Váha |
|---|---|---:|
| `C7-G0` | provenance, zmrazená formulácia, vstupy a runner | 5 |
| `C7-G1` | úplná stavová báza a počiatočné dáta | 10 |
| `C7-G2` | algebra, znamienka, nulové limity a počiatočné constrainty | 15 |
| `C7-G3` | ohraničená evolúcia dosiahne cieľ, konečný stav a RHS | 10 |
| `C7-G4` | aktivita a netautologické constrainty pozdĺž trajektórie | 15 |
| `C7-G5` | kroková, tolerančná a metódová konvergencia | 20 |
| `C7-G6` | NID/NIV a deep/shallow pokrytie | 10 |
| `C7-G7` | celý interval a endpoint agreement | 5 |
| `C7-G8` | plná fotónová/neutrínová Boltzmannova hierarchia | 5 |
| `C7-G9` | downstream CMB/S8 likelihood | 5 |

## Fyzikálne a numerické skratky

| Skratka | Význam |
|---|---|
| `D` | projektovaný kompenzovaný hustotný zdroj `Σ_A Ω_A δ_A` |
| `M` | projektovaný kompenzovaný hybnostný zdroj použitý v K7 |
| `M'` | derivácia `M` podľa evolučnej premennej; predmet vedeckého P2 |
| `δ_A` | hustotná porucha zložky A |
| `U_A` | bezrozmerná rýchlostná/hybnostná premenná zložky A |
| `Ω_A` | backgroundová hustotná frakcia zložky A |
| `c`, `f`, `b`, `γ`, `fs` | popol/CDM, palivo, baryóny, fotóny a free-streaming radiácia; malé `c` nie je podkoľaj K7c |
| `NID` | neutrino isocurvature density mód |
| `NIV` | neutrino isocurvature velocity mód |
| `deep/shallow` | hlboká/plytká superhorizontová počiatočná plocha konkrétneho auditu |
| `RHS` | pravá strana evolučnej sústavy |
| `ODE` | obyčajná diferenciálna rovnica/sústava |
| `RK4` | klasická explicitná Rungeho–Kuttova metóda 4. rádu |
| `DOP853` | explicitný adaptívny Rungeho–Kuttov solver vysokého rádu |
| `Radau` | implicitný solver vhodný pre niektoré stuhnuté systémy |
| `FD` | finite difference, numerická konečná diferencia |
| `HP` | high precision, výpočet s vyššou pracovnou presnosťou |
| `dps` | počet desiatkových číslic pracovnej presnosti |
| `rtol/atol` | relatívna/absolútna tolerancia integrátora |
| `nfev` | počet vyhodnotení RHS |
| `CMB` | kozmické mikrovlnné pozadie |
| `S8` | parameter amplitúdy neskorého zhlukovania |
| `H0` | dnešná Hubbleova konštanta |
| `ΛCDM` | štandardný kozmologický model s kozmologickou konštantou a studenou tmavou hmotou |

## Stavové a dôkazové kódy

| Kód | Význam |
|---|---|
| `PASS` | definovaná brána prešla v uvedenom rozsahu |
| `REVIEW` | výsledok je otvorený, technicky neuzavretý alebo nedostatočný na verdikt |
| `STOP/DEAD` | konkrétna koľaj/podkoľaj sa nesmie opakovať bez novej príčiny alebo mechanizmu; dôvod a dôkazy sa zachovajú |
| `NOT_REACHED` | brána sa pre skorší blocker nevykonala |
| `INHERITED` | tvrdenie je iba prevzaté; bez samostatného auditu nezískava body |
| `TIMEOUT_UNCLOSED` | časový limit; technický výsledok, nie automaticky fyzikálny FAIL |
| `DO_NOT_RUN_TECHNICAL` | známy chybný alebo neúplný skript, uchovaný iba pre audit |
| `PROVENANCE_FAIL` | chýbajúci/nesprávny zdroj, hash alebo manifest |
| `LIMITED` | neskorší audit obmedzil rozsah staršieho tvrdenia |
| `SUPERSEDED` | existuje novší autoritatívny nástupca; starý dôkaz sa nemaže |
| `CORRECTS` | nová historická udalosť opravuje staršiu bez jej prepísania |

## Skóre a dokumentácia

| Pojem | Význam |
|---|---|
| fyzikálna hĺbka | súčet váh prejdených fyzikálnych staniciových brán; aktuálne A2-K4 `60/100`; nie je to pravdepodobnosť pravdivosti |
| historická technická hĺbka | starší diagnostický údaj, napr. K7 `66.5/100`; neprenáša sa do fyzikálnej hĺbky koľaje |
| gate váha | vopred zmrazená rozhodovacia dôležitosť výsledku |
| podpora | súčet váh autoritatívnych PASS v danom scorecarde |
| blocker | váha autoritatívneho FAIL aktuálnej formulácie |
| otvorená váha | REVIEW, technicky neuzavreté alebo nedosiahnuté brány |
| pokrytie | súčet váh brán s autoritatívnym PASS alebo FAIL; nie pravdepodobnosť pravdy |
| `PRERUN` | očakávania a rozhodovanie zapísané pred výpočtom |
| checkpoint | nemenný medzivýsledok uložený pred ďalším prípadom |
| manifest | zoznam vstupov, verzií, hashov, parametrov a výstupov |
| lineage | doložený pôvod artefaktu a jeho transformácií |
| audit thread | nemenná viac-kolová diskusia audit → response → evidence → reaudit |
| `HISTORY` | append-only event ledger zmien stavu, skóre, obmedzení a supersession |
| `baseScripts` | verziované spoločné jadro; nikdy mutable alias pre historický výsledok |


## K7c diagnostické identifikátory po P2

| ID | Význam a stav |
|---|---|
| `SCI-A2K4-C7G5-K7C-P2-MLEDGER` | ukončený deväťčlenný ledger `M'`; jednoduché `math.fsum` vysvetlenie STOP |
| `K7c.3e fsum-only` | mŕtva podkoľaj: presnejšie finálne sčítanie dalo iba `1×` zlepšenie na 3/3 checkpointoch |
| `SCI-A2K4-C7G5-K7C-P3A-ZERO-IDENTITY` | živý audit dvoch algebraicky nulových koeficientov; P3a-A bez ODE, P3a-B až po PASS |
| `P3a-A` | symbolická, 80-dps a provenance kontrola identity; bez skóre |
| `P3a-B` | historické preregistračné meno evolučného handoffu; realizované ako route uzol `P3b`, PASS iba pre izolovanú krokovú bránu |
| `SCI-A2K4-C7G5-K7C-P3B-ZERO-IDENTITY-RK4` | autoritatívny P3b beh; `diff200/400=3.0308e-14`, pomer `16.004121`, celý G5 ešte REVIEW |
| `P4a` | preregistrovaný, ešte nespustený uzol: metódová a tolerančná šírka C7-G5 pred G4/G6 |
| `SCI-A2K4-C7G5-K7C-P4A-METHOD-TOLERANCE` | stabilné ID P4a; DOP853-medium/tight a Radau-tight, offline agregát |
