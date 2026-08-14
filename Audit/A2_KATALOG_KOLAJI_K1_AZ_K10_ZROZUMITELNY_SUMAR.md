# A2 — katalóg koľají K1 až K10 bez potreby čítať hlboké odvodenia

**Dátum:** 2026-07-13  
**Účel:** pri každej koľaji zachovať fyzikálny základ, rozdiel od ostatných,
stav a dôvod smrti alebo ďalšiu bránu  
**Kanonické číslovanie:** A2-K1 až A2-K9 a backgroundová A1-K2/A2-K10

## Ako katalóg používať

Pred založením novej koľaje treba skontrolovať sekciu **„Čo táto koľaj nie
je“**. Ak nový návrh používa ten istý fyzikálny obraz a iba mení gauge,
počiatočnú amplitúdu, integračný krok alebo názov veličiny, nie je nový a
nesmie obísť starý rozsudok.

## Rýchla mapa

| Koľaj | Jednovetový základ | Hlavný rozdiel | Stav |
|---|---|---|---|
| A2-K1 | prenos energie v pokojovom rámci CDM | CDM nedostane hybnostný kopanec; recoil nesie palivo | `MŔTVA M-009 — G4=40` |
| A2-K2 | striktne barotropické palivo | `c_s^2` je nútene rovné zápornému `w` | `MŔTVA M-008 — G3=30` |
| A2-K3 | prenos energie v pokojovom rámci paliva | palivo nedostane kopanec; CDM áno | `MŔTVA M-010 — G4=40` |
| A2-K4 | prenos v entalpickom energy-frame celého tmavého sektora | pokus o fyzikálny stred medzi K1 a K3 | `PREŽÍVA K4.2 — G6=60; M-011 obmedzený` |
| A2-K5 | kanonické skalárne palivo a meniaca sa hmotnosť CDM | tok vzniká z akcie, nie postulovaného `Q^mu` | `MŔTVA M-012 — G4=40; G8 screen FAIL` |
| A2-K6 | energy+momentum akcia s derivatívnym `eta Z^2` | pridáva akciou odvodený momentum transfer ku K5 typu toku | `MŔTVA M-013 — G3=30; G6 no-go` |
| A2-K7 | konečno-entalpický mediátor | energiu/hybnosť dočasne nesie tretí dynamický komponent | `PREŽÍVA CEZ PODKOĽAJE — G2=20` |
| A2-K8 | produkcia počtu konštantne hmotných častíc | tvorí nové častice namiesto zmeny ich hmotnosti | `ČAKÁ — G1=10` |
| A2-K9 | jeden operátor pre produkciu aj elastický rozptyl | zdroj a brzdenie nie sú dva nezávislé fit parametre | `ČAKÁ — G1=10` |
| A1-K2/A2-K10 | prahový alebo fázový tok | mení časový profil už na backgrounde | `ČAKÁ — G1=10; iná A1 vetva` |

---

## A2-K1 — tok rovnobežný s rýchlosťou CDM

**Na čom bola založená:** palivo a popol/CDM boli dve efektívne tekutiny.
Backgroundový tok `Q=Gamma rho_f` sa kovariantne zvolil v smere
štvorrýchlosti CDM:

```text
Q_c^mu=+Gamma rho_f u_c^mu,
Q_f^mu=-Gamma rho_f u_c^mu.
```

Palivo nebolo barotropické: background mal `w_f=-0.97703`, ale fyzikálna
pokojová zvuková rýchlosť bola zvolená zdravá `c_s,f^2=1`.

**Fyzikálny obraz:** popol vo vlastnom pokojovom rámci prijíma energiu bez
priestorového kopnutia a zostáva geodetický. Hybnostnú reakciu transferu musí
niesť palivo.

**V čom bola iná:** oproti K3 je bezmomentový rámec CDM, nie palivo. Oproti
K2 nemá zápornú barotropickú zvukovú rýchlosť.

**Čo táto koľaj nie je:** nie je to „ľubovoľný prenos do CDM“ ani všeobecný
interagujúci model. Je to presná voľba smeru `u_c^mu` pri konštantnom
`Gamma=lambda H0`.

**Prečo zomrela:** recoil v Eulerovej rovnici paliva sa delil malou entalpiou
`rho_f+p_f=delta rho_f`. Gauge-invariantná relatívna rýchlosť sa od
rekombinácie zosilnila približne `2.014e5`. Zmena gauge alebo ručné nulovanie
módu túto fyziku neodstráni.

**Dôkaz:** `Audit/A2_K1_MRTVA_superhorizontova_rychlostna_nestabilita.md`.

## A2-K2 — striktne barotropické palivo

**Na čom bola založená:** rovnaký background a smer transferu ako K1, ale
palivo sa interpretovalo ako ideálna barotropická tekutina:

```text
p_f=w_f rho_f,
c_s,f^2=dp_f/d rho_f=w_f=-0.97703.
```

**Fyzikálny obraz:** tlak paliva je v každej lokálnej poruche jednoznačnou
funkciou hustoty; neexistuje samostatná entropická alebo poľová zložka tlaku.

**V čom bola iná:** nemenila rámec prenosu. Menila iba mikrofyzický uzáver
tlakovej poruchy oproti K1.

**Čo táto koľaj nie je:** nie je to kanonický skalár ani k-essence, kde môže
byť `w<0` a súčasne `c_s^2>=0`. Taký model je nová akcia, nie oživená K2.

**Prečo zomrela:** záporné `c_s^2` zmenilo zvukové oscilácie na exponenciálny
rast úmerný `k`. Ide o analytickú gradientovú nestabilitu, nie chybu
integrátora.

**Dôkaz:** `Audit/A2_K2_MRTVA_barotropicke_palivo_gradientova_nestabilita.md`.

## A2-K3 — tok rovnobežný s rýchlosťou paliva

**Na čom bola založená:** dve efektívne tekutiny, zdravé
`c_s,f^2=1`, ale štvorvektor prenosu bol rovnobežný s palivom:

```text
Q_c^mu=+Gamma rho_f u_f^mu,
Q_f^mu=-Gamma rho_f u_f^mu.
```

**Fyzikálny obraz:** palivo vo vlastnom rámci odovzdáva energiu bez
hybnostného kopnutia. Vznikajúci popol/CDM preberá rozdiel rýchlostí.

**V čom bola iná:** je zrkadlovou voľbou rámca ku K1. Znížila koeficient
nestability, ale nemenila near-vacuum entalpiu ani konštantný tok.

**Čo táto koľaj nie je:** nie je to nový nosič ani priemer rámcov. Samotná
zmena `u_c` na `u_f` nepridáva mikrofyziku.

**Prečo zomrela:** relatívny mód obsahoval exponent `Gamma/delta`; zosilnenie
bolo `448.789`. Je menšie než K1, ale stále fyzicky neprípustné.

**Dôkaz:** `Audit/A2_K3_MRTVA_superhorizontova_rychlostna_nestabilita.md`.

## A2-K4 — energy-frame celého tmavého sektora

**Na čom bola založená:** tok bol rovnobežný s jednoznačne definovanou
entalpicky váženou rýchlosťou paliva a CDM:

```text
(rho_c+delta rho_f) theta_d=rho_c theta_c+delta rho_f theta_f,
Q_c^mu=+Gamma rho_f u_d^mu.
```

**Fyzikálny obraz:** energia a hybnosť sa odovzdávajú v lokálnom
energy-frame spoločného tmavého sektora — fyzikálnom „strede“ medzi K1 a K3.

**V čom bola iná:** neuprednostnila ani pokojový rámec CDM, ani paliva.
Použila entalpiu, nie svojvoľný aritmetický alebo iba hustotný priemer.

**Čo táto koľaj nie je:** nie je tretí mediátor. `u_d` je iba algebraická
kombinácia dvoch existujúcich rýchlostí a nenesie vlastnú energiu ani
relaxačný čas.

**Historický dôvod M-011 (zachovaný):** algebraická dvojzložková výmena mala
v starom rekombinačnom fuel-only velocity teste kladný relatívny eigenmód a
deklarovaný referenčný zisk `1.08028e5`.

**Prečo už M-011 nie je všeobecným rozsudkom:** K4.1 ukázala, že starý seed
neleží v úplnom regulárnom primordiálnom priestore a že zisk bol pomerom k
silno zanikajúcej referencii, nie absolútnou divergenciou. K4.2 otestovala
všetky tri regulárne módy na `q=30,300,1000`; propagujúci high-k symbol bol
zdravý a `T_max` K4 bol na každom q menší než pri `lambda=0`.

**Súčasný stav:** `PREŽÍVA K4.2 — G6=60`. Ďalšia brána K4.3/G7 musí
doplniť vlastný plný Einstein–Boltzmann a fyzické transfery. CMB
normalizácia a `S8` patria až do A3/G8.

**Historický dôkaz:** `Audit/A2_K4_MRTVA_total_dark_sector_velocity_instability.md`.
**Obmedzujúce audity:**
`Audit/A2_K4_1_UPLNA_REGULARNA_CONSTRAINT_BAZA_A_ROZSUDOK.md` a
`Audit/A2_K4_2_HIGH_K_SUBHORIZONTOVY_AUDIT_A_ROZSUDOK.md`.

## A2-K5 — kanonický skalár a konformne viazané CDM

**Historický názov:** `A2-K5/K1`.

**Na čom bola založená:** near-vacuum palivo sa nahradilo kanonickým
skalárnym poľom. Počet častíc CDM bol zachovaný, ale ich Einstein-frame
hmotnosť závisela od poľa cez `A(phi)`.

**Fyzikálny obraz:** energia paliva sa mení na pokojovú hmotnosť už
existujúcich častíc popola. Tok, trenie aj skalárna sila vyplývajú z jednej
lokálnej akcie.

**V čom bola iná:** ako prvá nepoužila postulovaný fluidný smer `Q^mu`.
Odstránila pól `1/(1+w_f)` a prešla superhorizontovými testami K5.1.

**Čo táto koľaj nie je:** nie je produkcia nových častíc. Nie je dovolené
ponechať iba priaznivé trenie a vymazať akciou vynútenú príťažlivú silu.

**Prečo zomrela:** rovnaká väzba, ktorá vytvorila tok, dala príliš silnú
príťažlivú silu a neskorý rast. Konzervatívna CMB-normalizovaná brána dala
`S8=0.9836–1.0063`; rozsudok je M-012.

**Dôkaz:** `Audit/A3_K5_K1_MRTVA_CMB_normalizovana_rastova_brana_M012.md`.

## A2-K6 — derivatívna energy+momentum akcia

**Historický alias:** `K5/K3a`.

**Na čom je založená:** jedna kovariantná akcia

```text
f=-f1(phi)rho_c+eta Z^2,
Z=u_c^mu partial_mu phi.
```

`f1` realizuje A1 tok energie; `eta Z^2` pridáva momentum transfer.

**Fyzikálny obraz:** tok môže stále vynucovať skalárnu silu, ale pohyb popola
zároveň reaguje na derivatívnu väzbu k jeho rýchlosti. Cieľom je zistiť, či
jedna zdravá akcia môže dať slabšie efektívne zhlukovanie.

**V čom je iná:** oproti K5 má nový fyzikálny operátor ovplyvňujúci Eulerovu
rovnicu a kinetickú maticu. Oproti K7 nemá tretí mediátor. Oproti K8
zachováva počet častíc a používa meniacu sa efektívnu hmotnosť.

**Čo táto koľaj nie je:** nie je K5 s ručne pridaným fenomenologickým trením.
Hodnota `eta=0` je iba nulový kontrolný limit, nie tvrdenie, že K6 je dieťa
K5.

**Súčasný stav:** `MŔTVA M-013 — G3=30`. K6 vykonala neskorý G6
presný `G_ij`/QS no-go, ale neprešla úplné G4–G5; kill test preto
nezvyšuje sekvenčné skóre. V celom zdravom intervale zostalo `mu_cc>1`.

## A2-K7 — konečno-entalpický mediátor

**Historický alias:** `K5/K4a`.

**Na čom je založená:** nový dynamický komponent `M` s vlastným
tenzorom energie a hybnosti, kladnou entalpiou a zdravou zvukovou rýchlosťou.
Prenos je dvojstupňový `palivo -> M -> popol`.

**Fyzikálny obraz:** hybnosť nemusí okamžite skočiť medzi near-vacuum
palivom a prachom. Mediátor ju môže niesť a relaxovať počas konečného času.

**V čom je iná:** ako jediná pridáva explicitný tretí nosič. K4 používala iba
algebraický priemer dvoch rýchlostí; K7 má nový fyzický stupeň voľnosti.

**Čo táto koľaj nie je:** nie je K4 s novým názvom. Mediátor sa nesmie
algebraicky zahodiť, ak nesie nezanedbateľnú energiu alebo hybnosť.

**Stav a stena:** `PREŽÍVA CEZ PODKOĽAJE — G2=20`. Formálny background
a ledger prešli; G3 zostáva otvorená, kým konkrétna dcéra neodvodí lokálny
kernel, `delta Q`, noise/memory a pozitivitu. Staré 32–42 sú iba intra-G3
checkpointy.

## A2-K8 — produkcia počtu konštantne hmotného popola

**Historický alias:** `K5/K2a`.

**Na čom je založená:** popol má konštantnú hmotnosť a tok vzniká lokálnou
produkciou počtu častíc:

```text
nabla_mu(n_c u_c^mu)=S_n,
m_c=constant.
```

**Fyzikálny obraz:** palivo vytvára nové častice popola; nemení hmotnosť už
existujúcich častíc. Po vzniku preto popol nemusí niesť trvalý skalárny náboj.

**V čom je iná:** priamo mení ledger K5/K6 z „meniaca sa hmotnosť pri
zachovanom počte“ na „meniaci sa počet pri konštantnej hmotnosti“. Oproti K7
nemusí mať dlhšie žijúci mediátor.

**Čo táto koľaj nie je:** nie je iba zdroj pridaný do kontinuity. Musí
odvodiť creation pressure, entropiu, spätnú reakciu a prípadný šum.

**Stav a stena:** čaká. Zomrie, ak `S_n` zostane fenomenologický bez
kovariantnej bilancie alebo ak produkcia znovu vytvorí near-vacuum
`1/delta` nestabilitu.

## A2-K9 — jednotný produkčno-rozptylový operátor

**Historický alias:** `K5/K6`.

**Na čom je založená:** jeden mikrofyzický proces súčasne určuje produkciu
konštantne hmotného popola a elastický prenos hybnosti medzi vzniknutým
popolom a sieťou/palivom.

**Fyzikálny obraz:** tá istá zrážková alebo deliaca udalosť vytvorí časticu a
určí, ako rýchlo sa jej rýchlosť relaxuje. Zdroj a disipácia majú spoločný
pôvod.

**V čom je iná:** oproti K8 obsahuje aj odvodený momentum transfer. Oproti
K6 nevytvára tok zmenou hmotnosti. Oproti K7 nemusí zavádzať propagujúci
mediátor.

**Čo táto koľaj nie je:** nie sú to dva nezávislé parametre `produkcia +
drag` vybrané po výsledku `S8`. Obe sadzby musí spájať jeden operátor a pri
otvorenom systéme aj vzťah šumu a disipácie.

**Stav a stena:** čaká. Bez spoločného operátora alebo pri nezdravom šume je
koľaj mŕtva ešte pred kozmologickým fitom.

## A1-K2/A2-K10 — prahový, fázový alebo nukleačný tok

**Historický alias:** `A1-K2/A2-K6a`.

**Na čom je založená:** `Gamma_eff` nie je konštantné až do dneška. Vzniká z
lokálneho prahu, fázového prechodu alebo nukleácie a po určitej epoche sa
výrazne zmenší alebo vypne.

**Fyzikálny obraz:** metabolizmus siete je aktívny iba v stave, kde sú
splnené lokálne podmienky. Neskorý vesmír už nemusí mať veľký tok ani veľkú
väzbu.

**V čom je iná:** ako jediná primárne mení príčinu C3 — časový profil
backgroundového toku. K6–K9 sa najprv snažia reprodukovať A1-K1.

**Čo táto koľaj nie je:** nie je čistá perturbačná oprava A2. Musí začať ako
nová A1 backgroundová koľaj a pri zmene fundamentu patrí do verzie 4.

**Stav a stena:** čaká. Najprv musí odvodiť prah z bunkovej mikrofyziky,
prejsť backgroundom, BBN/CMB históriou a až potom vlastnými A2 perturbáciami.

## Záverečný zákaz duplicity

- `Q parallel u_c` s iným názvom je stále mŕtva K1.
- `c_s^2=w<0` s numerickým tlmením je stále mŕtva K2.
- `Q parallel u_f` je stále mŕtva K3.
- algebraický priemer bez nového stupňa voľnosti je stále mŕtva K4.
- meniaca sa hmotnosť s ponechanou príťažlivou silou je stále mŕtva K5.
- nový názov je oprávnený až novou akciou, nosičom, ledgerom alebo
  backgroundovým zákonom podľa AR10.


