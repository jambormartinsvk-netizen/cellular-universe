# A2-K4 — vzdialenosť od dokončenia, odhad práce a ochrana pred nekonečným vetvením

**Dátum:** 2026-07-15  
**Typ:** projektový a auditný odhad; bez nového fyzikálneho výpočtu  
**Verdikt:** `BOUNDED_PATH_EXISTS`, ale A2-K4 ešte nie je blízko finálneho fyzikálneho verdiktu

## Krátka odpoveď

A2-K4 nesmeruje náhodne bez akejkoľvek mapy: aktuálna definícia C7-W1 má
presne desať brán G0–G9. Štyri sú úplne prejdené, kroková časť G5 je prejdená
a zostáva šesť ohraničených vedeckých balíkov. Doterajšia dokumentácia však
miešala tri odlišné čísla, preto pokrok nebolo vidieť.

Aktuálny stav sa odteraz uvádza takto:

| Ukazovateľ | Stav | Čo znamená |
|---|---:|---|
| historická jemná hĺbka A2-K4 | `66.5/100` | najhlbší dosiahnutý sekvenčný auditný bod; nie percento hotovej práce |
| striktne validovaná podpora C7-W1 | `40/100` | celé PASS G0+G1+G2+G3 |
| pracovný postup WBS-1 | **`48/100`** | podpora 40 plus dokončená kroková časť G5 s pracovnou váhou 8 |
| autoritatívny blocker opravenej formulácie | `0/100` | starý P1 blocker bol obmedzený P3a/P3b |
| otvorená práca podľa WBS-1 | `52/100` | zvyšok G5, G4 a G6–G9 |

`48/100` nie je pravdepodobnosť pravdy ani nový fyzikálny score. Je to
výlučne ukazovateľ dokončenia pracovného plánu, aby bol viditeľný aj pokrok
vo vnútri ešte neuzavretej brány.

## Prečo sa 66.5 nemenilo

Hĺbka `66.5` bola navrhnutá ako sekvenčný rekord celej koľaje. Diagnostické
opravy vo vnútri jednej otvorenej brány ju nesmeli zvyšovať. To chránilo
pred falošným prideľovaním fyzikálnych bodov, ale zakrylo reálnu prácu.
Riešením nie je spätne nafúknuť hĺbku, ale vedľa nej viesť WBS-1.

## Zmrazené pracovné rozdelenie WBS-1

Váhy celých G0–G9 zostávajú C7-W1. Iba pre zobrazenie práce sa G5 rozdelí:

| Časť | Pracovná váha | Stav |
|---|---:|---|
| G5-S: kroková konvergencia | 8 | PASS P3b |
| G5-T: tolerančná konvergencia | 6 | P4a NOT RUN |
| G5-M: metódová konvergencia | 6 | P4a NOT RUN |

Súčet G5 zostáva 20. Čiastkové pracovné body sa nesmú uviesť ako vedecká
podpora. Až úplný PASS G5 presunie celých 20 bodov do C7-W1 podpory.

## Konečná hranica A2-K4

A2-K4 je dokončená jedným z dvoch spôsobov:

1. **PASS cesta:** G0–G9 prejdú a vznikne finálny A2-K4 rozsudok s plnou
   hierarchiou a downstream likelihoodom;
2. **STOP cesta:** niektorá brána dá reprodukovateľný fyzikálny no-go pri
   platnej numerike a koľaj sa uzavrie s dôvodom, skriptmi a výpočtami.

Timeout, chyba parsera alebo chýbajúci backend nie sú dokončením; po
obmedzenom počte opráv však musia dostať stav `REVIEW_BLOCKED`, nie ďalšie
nekonečné písmeno podkoľaje.

## Zostávajúcich šesť vedeckých balíkov

| Balík | Obsah | Stav | Odhad pri hladkom priebehu | Odhad pri probléme |
|---|---|---|---:|---:|
| 1. P4a / G5 | DOP853 medium/tight, Radau, offline agregát | preregistrované | 0.5–2 dni | 3–5 dní |
| 2. P4b / G4 | netautologické constrainty a aktivita pozdĺž trajektórie | nezačaté | 1–3 dni | 4–7 dní |
| 3. P4c / G6 | NID/NIV × deep/shallow | nezačaté | 1–3 dni | 4–7 dní |
| 4. G7 | celý požadovaný interval a endpoint agreement | nezačaté | 2–5 dní | 1–2 týždne |
| 5. G8 | plná fotónová/neutrínová Boltzmannova hierarchia | nezačaté | 1–3 týždne | 3–6 týždňov |
| 6. G9 | CMB/S8 likelihood bez zmeny fyziky | nezačaté | 1–2 týždne | 2–4 týždne |
| záver | finálny audit, Git/GitHub baseline a release kandidát | nezačaté | 2–5 dní | 1–2 týždne |

Kalendárny odhad nie je súčet fyzikálnych váh. G8 a G9 majú iba po päť
bodov, ale môžu spotrebovať väčšinu zostávajúceho času.

### Celkový odhad

- optimisticky: **15–20 sústredených pracovných dní**, približne 3–4 týždne;
- realisticky: **25–40 pracovných dní**, približne 5–8 týždňov;
- rizikovo: **2–3 mesiace**, ak G8/G9 vyžadujú novú backend integráciu;
- platný fyzikálny STOP môže A2-K4 uzavrieť podstatne skôr.

## Skutočný stav skriptov a Q

Read-only inventúra dala:

- `213` číslovaných Python súborov v `scripts/`;
- najvyššie existujúce číslo je **208**;
- skripty 209–212 sú zatiaľ iba rezervované v P4a pláne, neexistujú;
- posledný corpus checker eviduje `75` karanténnych alebo historicky
  obmedzených súborov;
- posledná metodická otázka je **Q93**.

Počet súborov preto nie je počet aktívnych vedeckých krokov. Veľkú časť
tvoria zachované technické chyby, superseded checkery a negatívne dôkazy.

## Pevné obmedzenia proti P200b a skriptu 1000000

1. Aktuálna A2-K4 vetva má iba šesť zostávajúcich balíkov uvedených vyššie.
2. Na jeden balík je povolená prvá implementácia a najviac **dve technické
   opravy**. Potom sa vydá PASS, fyzikálny STOP alebo `REVIEW_BLOCKED` s
   architektonickým rozhodnutím. Nevzniká tretia technická podpodkoľaj.
3. Technická chyba nevytvára nové centrálne Q. Patrí do error ledgeru a
   HISTORY existujúceho balíka.
4. Q94 odpovedá na túto vzdialenosť. Q95–Q99 sú rezervované pre finálne
   výsledky zostávajúcich brán; v A2-K4 sa bez novej fyzikálnej vetvy nejde
   nad Q99.
5. Skripty 209–212 patria P4a. Po nich sa musí použiť verziované spoločné
   jadro a route-local konfigurácie; parameter sweep nesmie vytvárať nový
   Python súbor pre každý prípad.
6. Očakávaný posledný flat script ID je približne `225–232`. **Hard stop je
   240**: pred vytvorením 241 musí vzniknúť samostatný audit, prečo zlyhala
   architektúra zdieľaného jadra a prečo je rozšírenie nevyhnutné.
7. Mená P4a/P4b/P4c uzatvárajú lokálnu diagnostickú sériu. Ďalšie práce sa
   pomenúvajú priamo G7, G8 a G9, nie K7y alebo P200b.

## Smerovanie, nie náhodné hľadanie

Doterajšia fáza K1–K7 bola prevažne diagnostická: hľadala reprezentáciu,
ktorá vôbec umožní stabilne integrovať rovnice. P3b prvýkrát odstránila
konkrétnu identifikovanú numerickú príčinu a vrátila štvrtý rád. Od P4a sa
už nesmie voľne hľadať ďalšia reprezentácia; postupuje sa cez zmrazené
brány. Každý ďalší balík má vopred definovaný výstup a terminálny verdikt.

## Odporúčanie

Pokračovať P4a, pretože je krátka a môže zvýšiť strict support z 40 na 60.
Ak P4a prejde, vykonať P4b a P4c. Pred G7 zaviesť verziované spoločné jadro.
Pred začiatkom G8 urobiť nový časový audit, pretože práve G8/G9 rozhodnú,
či realistický odhad ostáva 5–8 týždňov alebo sa predĺži.

