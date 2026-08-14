# Register mantinelov brán G1–G9 a staníc A3/A4

**Stav:** `AKTÍVNY RIADIACI REGISTER`  
**Pravidlo:** AR68; dopĺňa AR30 (sekvenčná hĺbka), nemení žiadny existujúci
PASS, STOP, skóre ani fyzikálny rozsudok spätne.

**Pracovný vykonávací protokol neprázdnosti:**
`tracks/METHODOLOGY/00_CONSTRAINT_FEASIBILITY_GATE_SK.md`. Tento súbor
naďalej vlastní obsah brán G1–G10; protokol v `tracks` určuje, ako sa pred
konkrétnou funkciou testuje ich spoločný behaviorálny a funkčný prienik.

## Účel

Brána nie je iba zoznam výpočtov. Je to prienik podmienok, ktoré musia platiť
súčasne. Bez takého prieniku môže test nájsť správne číslo, ale stále porušiť
energetický ledger, nulový limit alebo zákaz nového fitu.

Pre každú budúcu bránu sa preto pred začatím výpočtu založí jej **mantinelový
pas** s týmito pevnými položkami:

1. identita a route prefix; 2. presný predmet a rozsah; 3. fyzikálny zákon
   alebo pozorovací limit; 4. matematická veličina a jednotky; 5. PASS,
   fyzikálny STOP a `REVIEW_BLOCKED`; 6. nulový limit; 7. zakázané nové
   parametre; 8. dôkazové artefakty a ich proveniencia; 9. trieda dôkazu
   `E0_EXACT/E1_DIRECT_MEASUREMENT/E2_REFERENCE_MODEL/E3_PROVISIONAL` a štítok `PRECHECK_EXCLUDED_SCOPE`,
   `COMPUTED_STOP_SCOPE`, `OBSERVATIONAL_STOP_SCOPE`,
   `REFERENCE_MISMATCH_ONLY` alebo `TECHNICAL_STOP`.

`PASS` brány znamená splnenie **všetkých** jej mantinelov. Nevykonaný,
nejasný alebo technicky zablokovaný mantinel znamená `REVIEW_BLOCKED`, nie
implicitný PASS ani smrť koľaje.

`E2_REFERENCE_MODEL` (vrátane ΛCDM/GR/SM) je comparator, nie automatický
kill limit. `E1_DIRECT_MEASUREMENT` musí uviesť confidence level, chyby,
systematiky a mapovanie modelu na observablu. Predbežný no-go s úplným
certifikátom sa vedie oddelene od vykonaného fyzikálneho STOP a nepridáva
kanonickú hĺbku.

Mantinely sa majú riešiť ako spoločný systém: rovnice a conservation určia
dynamické jadro, nerovnosti a nulové limity vytvoria obal a pozorovania až
potom vyberajú medzi zostávajúcimi riešeniami. Presný postup a povinné
počítanie zvyšných voľných funkcií je
`Questions/Q22A_CONSTRAINT_TO_FUNCTION_DERIVATION_PROTOCOL_SK.md`.

## Kanonické brány

| Brána | Mantinely, ktoré musí jej pas obsahovať | Čo brána nesmie nahradiť |
|---|---|---|
| G1 | odlišná hypotéza, jej mechanizmus, route prefix, dimenzie, zdroj každého nového parametra, odlíšenie od staršej koľaje | slovný opis alebo premenovanie existujúcej koľaje |
| G2 | úplný background ledger, `sum Q_A^mu=0`, kladnosť hustôt/H², nulový limit, žiadne `k` v backgrounde, pôvod normalizácií | fit na `H0`/`S8` alebo nezdokumentovaný rezervoár |
| G3 | lokálnosť, kovariancia/akcia alebo ekvivalentný úplný uzáver, frame prenosu, energia aj hybnosť, causalita a bez skrytého času | iba homogénnu ODE alebo globálne `H0` ako mikrofyzický clock |
| G4 | úplné lineárne rovnice všetkých zložiek, Einsteinove constrainty, gauge mapa, znamienka, `delta Q_A`, nulový limit a Bianchi identity | neúplný sektor či test-field za plnú sústavu |
| G5 | úplná regulárna superhorizontová báza, počet módov, adiabatic/isocurvature klasifikácia, constrainty, linearita amplitúdy | jeden vybraný seed alebo kompenzáciu definovanú len numericky |
| G6 | úplná báza v subhorizontovom/high-k limite, ghost/gradient/causalita, stiffness/konvergencia, fyzikálne menovatele | stabilitu jedného módu alebo jednej tolerancie |
| G7 | úplný Einstein–Boltzmann systém, hierarchie/uzáver, rekombinácia a TCA, conservation/constraint/null testy, nezávislá implementácia alebo gauge cross-check, fyzické transfery | binárny wrapper, dekoratívne identity alebo post-data opacity/drag |
| G8 | CMB-normalizácia a transfery, `A_s,n_s` proveniencia, linearita, predregistrované rozsahy `k,z`, `sigma8/S8`, nulový model a konvergencia | prispôsobenie amplitúdy iba na trafenie `S8` |
| G9 | pevný zoznam dát/likelihoodov/covariancií, priory a nuisance parametre, počet voľností, systémové chyby, holdout/validácia a kill prahy | výber iba priaznivého datasetu alebo skrytý look-elsewhere efekt |

G10 ostáva verzia/reprodukcia; jeho mantinely sú manifest, hash, changelog,
nezávislé zopakovanie a úplné priznanie otvorených brán.

## Stanica A3 — implementácia a spektrá

A3 nie je druhá G7. Je pracovná stanica, ktorá môže postúpiť iba cez
kanonické G7 a G8. Jej pas musí súčasne držať:

| A3 mantinel | Minimálny obsah |
|---|---|
| A3-M1 Proveniencia | zmrazená verzia/commit CLASS alebo CAMB, patch, konfigurácia, jednotky a vstupy z A2 |
| A3-M2 Referencia | pri nulovom bunkovom transfere reprodukovať štandardný background, `C_ell` a `P(k)` v predregistrovanej tolerancii |
| A3-M3 Prenos fyziky | implementovať celý A2 operátor, nie iba background alebo rastovú rovnicu; zachovať ledger a frame |
| A3-M4 Numerika | nezávislá tolerancia/metóda, mriežková a multipólová konvergencia, checkpointy a obmedzený runtime |
| A3-M5 Interpretácia | každý posun spektra má mechanizmus; žiadny nový post-data drag, opacity, `A_s` či počiatočný mód |
| A3-M6 Výstup | fyzické transfery a CMB-normalizované `sigma8/S8` s oddelením G7 od G8 |

## Stanica A4 — para, exit a reliktný sektor

A4 je samostatná mikrofyzická stanica. Nemôže byť uzavretá vložením
`Delta N_eff` ako hotového čísla.

| A4 mantinel | Minimálny obsah |
|---|---|
| A4-M1 Lokálny zdroj | `C_s(chi,I_i)` s lokálnym clock/stavom, nie voľný `ln a`; M0 z Q22a/Q18 |
| A4-M2 Rezervoár a ledger | `T_e^(mu nu)`, párové `+S_s^mu/-S_s^mu`, energia i hybnosť, pozitívne hustoty |
| A4-M3 Časovanie | vznik, rovnováha, decoupling, exit/reheating a nulový neskorý chvost; priamy neskorý voľno-relativistický kanál rešpektuje M-015 |
| A4-M4 Termodynamika | entropia, teplota, stupne voľnosti a BBN limity bez dvojitého započítania |
| A4-M5 Poruchy | z rovnakého operátora `delta S_s`, noise/frame, izokurvatúra a voľná dráha/uzáver pary |
| A4-M6 Predikčnosť | `Delta N_eff` a vlastnosti pary sú odvodené; pozorovania testujú, nie určujú jej tvar |

Súčasný stav A4-M1 je `REVIEW/STOP`: [M0 provenance audit](Q22A_M0_CLOCK_AND_RESERVOIR_PROVENANCE_AUDIT_2026-07-16.md)
nenašiel v súčasnej teórii definovaný `chi` ani rezervoár. To nezabíja
efektívnu FLRW triedu, ale blokuje fundamentálny PASS A4.

## Použitie pri ďalšom kroku

Predregistrácia novej úlohy musí odkázať na presný riadok Gx alebo Ax a
uviesť, ktoré mantinely sa testom uzatvárajú a ktoré zostávajú otvorené.
Výsledný audit musí mať rovnakú tabuľku so stavom `PASS`, `STOP` alebo
`REVIEW_BLOCKED`. Až potom sa smie zmeniť hĺbka alebo prejsť na ďalšiu bránu.
