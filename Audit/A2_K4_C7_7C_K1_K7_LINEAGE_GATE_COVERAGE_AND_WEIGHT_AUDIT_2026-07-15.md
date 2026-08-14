# A2-K4 / C7.7c — pôvod K1 až K7, jednotné brány a váhy výsledkov

Dátum: 2026-07-15  
Rozsah: organizačný a dôkazový audit; bez nového fyzikálneho výpočtu  
Aktuálny stav A2-K4: **ŽIVÁ, 66.5/100 podľa doterajšej staniciovej hĺbky**  
Aktuálny stav C7.7c/K7c: **REVIEW — evolúcia dobehla, klasická RK4 konvergencia neprešla**

## Krátka odpoveď: prečo K7c a prečo neexistuje K1c

`K1` až `K6` neboli prvý až šiesty rovnaký test. Boli to po sebe zavedené
**alternatívne numerické formulácie tej istej brány C7.7c**. Každá sa pokúsila
odstrániť konkrétnu numerickú príčinu zlyhania predchodcu. Písmená `a`, `b`,
`c` sa začali používať až vo vnútri siedmej formulácie:

- `K7a` — projektovaná reprezentácia a Jacobián;
- `K7b` — počiatočné koeficienty a constrainty bez ODE;
- `K7c` — nenulová evolúcia a jej numerická konvergencia;
- `K7d` — plánovaná úplná activity/constraint brána, zatiaľ nedosiahnutá.

Historické meno `K7c` teda znamená „tretia etapa siedmej formulácie“, nie
„brána c, ktorú musela dostať každá K1 až K7“. `K1c` nevznikla, pretože K1
sa zastavila na nerozlíšenej komponentovej aktivite ešte pred zavedením
tohto jednotného členenia. Chýbajúci súbor `K1c` nie je chýbajúci výsledok;
je to chýbajúca historická symetria názvov. Nová matica nižšie túto
nejednoznačnosť odstraňuje bez premenovávania starých dôkazov.

## Čo jednotlivé formulácie menili

| Formulácia | Ľudský opis zmeny | Autoritatívny výsledok | Prečo sa zastavila |
|---|---|---|---|
| K1 | Jeden uniformný absolútny `atol` pre všetkých 13 zložiek | 88/116 PASS, 28 activity FAIL | amplitúdy od približne `10^6` po `10^-24` nemožno auditovať jednou absolútnou podlahou; numerický dôkaz mŕtvy, nie fyzika |
| K2 | Každá zložka vydelená svojou počiatočnou amplitúdou; DOP853 | timeout bez výsledného JSON | explicitná evolúcia bola v danom kontrakte príliš drahá; fyzika nerozhodnutá |
| K3 | Rovnaké škálovanie ako K2, iba implicitný Radau | timeout a overflow numerického Jacobiánu | počiatočné mierky mali rozsah až približne `10^48`; technická slepá vetva |
| K4 | Mierka anticipuje analytickú obálku v `x_ref=-18` | referenčný stav 94/94 PASS, evolúcia timeout | opravená škála, ale nie cena/stuhnutosť evolúcie |
| K5 | Lokálne maticové vyváženie zmenšilo Jacobián | lokálne redukcie PASS, prvý segment 0/1 | nedokončený segment a zmenený komponentový chybový rozpočet |
| K6 | Fyzikálny stav, analytická obálka iba ako vektor `atol_i` | prvý segment 0/1 | niektoré požadované tolerancie až `10^-36`, pod aritmetickou podlahou float64 RHS |
| K7 | Dve degenerované druhové premenné nahradené projektovanými zdrojmi `D,M` | K7a PASS, K7b PASS, K7c reprodukcia PASS / konvergencia FAIL | prvý čistý RK4 beh je konečný, ale rozdiel sa pri zjemnení zväčšil a dominuje `M` |

## Jednotné brány odteraz

Staré mená zostávajú nemenné. Nad nimi sa zavedú stabilné gate ID, aby bolo
pri každej formulácii viditeľné aj to, čo sa **nevykonalo**.

| Gate ID | Obsah | Váha |
|---|---|---:|
| `C7-G0` | zmrazená formulácia, provenance, vstupy a reprodukovateľný runner | 5 |
| `C7-G1` | úplná stavová báza a auditované počiatočné dáta | 10 |
| `C7-G2` | algebra, znamienka, nulové limity a počiatočné constrainty | 15 |
| `C7-G3` | ohraničená evolúcia dosiahne cieľ s konečným stavom a RHS | 10 |
| `C7-G4` | aktivita komponentov a netautologické constrainty pozdĺž trajektórie | 15 |
| `C7-G5` | kroková, tolerančná a metódová konvergencia | 20 |
| `C7-G6` | NID aj NIV, deep aj shallow, bez tichého vynechania plochy | 10 |
| `C7-G7` | požadovaný plný interval a deep/shallow endpoint agreement | 5 |
| `C7-G8` | plná fotónová/neutrínová Boltzmannova hierarchia | 5 |
| `C7-G9` | downstream CMB/S8 likelihood bez zmeny už auditovanej fyziky | 5 |
| **Spolu** |  | **100** |

Váhy sú verzia `C7-W1`. Nemožno ich meniť po výsledku bez novej verzie,
odôvodnenia v `HISTORY/SCORE_CHANGES` a prepočtu všetkých súrodencov.
Viaceré riadky, ktoré dokazujú rovnaký claim, sa nesmú započítať viackrát.

## Význam troch skóre

Každý výsledok má jednu vopred zmrazenú gate váhu, ale podľa verdiktu sa
započíta do iného vedra:

- **validovaná podpora** — iba autoritatívny PASS; ukazuje, čo koľaj naozaj unesie;
- **blokujúca evidencia** — autoritatívny fyzikálny alebo numerický FAIL danej formulácie; výsledok má vysokú informačnú hodnotu, ale nie je podporou;
- **otvorená/technická váha** — REVIEW, timeout, technická chyba alebo ešte nevykonaná brána.

Samostatne sa uvádza **pokrytie auditu**: súčet váh brán s autoritatívnym
výsledkom PASS alebo FAIL. Timeout môže byť cenný diagnostický výsledok, ale
neuzatvára fyzikálnu bránu. `66.5/100` je doterajšia hĺbka celej A2-K4;
nové C7 skóre ju zatiaľ nenahrádza a nesmie sa s ňou sčítať.

## Konzervatívna matica historického pokrytia

`P` = PASS, `F` = FAIL danej formulácie, `R` = REVIEW/technicky neuzavreté,
`N` = nedosiahnuté, `I` = iba zdedené alebo nie samostatne auditované.

| Formulácia | G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | Terminálny dôvod |
|---|---|---|---|---|---|---|---|---|---|---|---|
| K1 | P | I | I | P | F | N | N | N | N | N | uniformný `atol` nerozlíšil 28 activity kontrol |
| K2 | P | I | I | R | N | N | N | N | N | N | timeout DOP853 |
| K3 | P | I | I | R | N | N | N | N | N | N | timeout/zle podmienený numerický Jacobián |
| K4 | P | P | I | R | N | N | N | N | N | N | obálka PASS, evolúcia timeout |
| K5 | P | I | I | F | N | N | N | N | N | N | 0/1 segment a zmenený error budget |
| K6 | P | I | I | F | N | N | N | N | N | N | 0/1 segment, `atol_i` pod float64 podlahou |
| K7 | P | P | P | P | R | F | N | N | N | N | K7c konvergencia FAIL; G4 nie je uzavretá tautologickými monitormi |

`I` nezískava body. Pri spätnej migrácii možno `I` zmeniť na `P` iba odkazom
na konkrétny dôkaz, ktorý skutočne testoval tú istú formuláciu a background.

## Váhový obraz aktuálnej K7

Konzervatívne započítanie K7 podľa `C7-W1`:

| Vedro | Body | Význam |
|---|---:|---|
| validovaná podpora | `40/100` | G0+G1+G2+G3 |
| blokujúca evidencia aktuálnej formulácie | `20/100` | G5: klasická RK4 konvergencia neprešla |
| otvorené alebo nedosiahnuté | `40/100` | G4 a G6 až G9 |
| auditované pokrytie PASS+FAIL | `60/100` | nie pravdepodobnosť pravdivosti |

Toto vysvetľuje, prečo ľudské `8/10 kontrol PASS` neznamená 80 % úspech.
Štyri reprodukčné riadky P1 overovali ten istý historický výsledok, dva
cancellation riadky boli monitory, runtime a safety neoverovali fyzikálnu
konvergenciu. Dve neprejdené kontroly patrili do jednej, ale najťažšej
aktuálnej brány G5 s váhou 20.

## Priorita ďalšej práce

1. Najvyššiu prioritu má G5: nezávisle vysvetliť ne-RK4 pomer a dominantný `M`.
2. Paralelne sa musí presne definovať G4 tak, aby constrainty neboli tautologické.
3. G6 až G9 sa nespúšťajú, kým G5 neprejde; ich veľký počet nesmie zakryť blocker.
4. Externý audit má dostať script 197, tri checkpointy, zmrazené očakávania,
   presnú definíciu normy a otázku, či je výpočet vôbec v asymptotickom RK4 režime.

## Dôkazové zdroje

- `Audit/A2_K4_C7_7C_K1_UNIFORM_ATOL_ACTIVITY_REVIEW.md`
- `Audit/A2_K4_C7_7C_K2_NORMALIZED_DOP853_TIMEOUT.md`
- `Audit/A2_K4_C7_7C_K3_NORMALIZED_RADAU_TIMEOUT.md`
- `Audit/A2_K4_C7_7C_K4_ANALYTIC_ENVELOPE_TIMEOUT.md`
- `Audit/A2_K4_C7_7C_K5_EVOLUTION_ADDENDUM_2026-07-14.md`
- `Audit/A2_K4_C7_7C_K5_K6_CORRECTION_AND_DEATH_AUDIT_2026-07-14.md`
- `Audit/A2_K4_C7_7C_K7A_FINAL_PROJECTED_JACOBIAN_VERDICT_2026-07-14.md`
- `Audit/A2_K4_C7_7C_K7B_FINAL_FOUR_SURFACE_VERDICT_2026-07-15.md`
- `Audit/A2_K4_K7C_P1_CLEAN_STANDALONE_RK4_FINAL_AUDIT_2026-07-15.md`

## Neskoršie obmedzenie po P3b

Tento audit zachytáva stav pred P3a/P3b. Historický G5 blocker 20 bol
neskôr obmedzený na legacy float64 zápis dvoch presných nulových
koeficientov. Aktuálna opravená formulácia má support 40, blocker 0,
otvorené 60 a G5 `PARTIAL PASS / REVIEW`. Povinne čítať spolu s
`Audit/A2_K4_C7_W1_P3B_SCORECARD_LIMITATION_ADDENDUM_2026-07-15.md`.
