# Retrospektívny master plán auditu dôveryhodnosti

**Dátum:** 2026-07-15  
**Účel:** určiť, ktoré už existujúce výpočty a rozsudky musia dostať
formula-provenance, numerický alebo fyzikálny re-audit, aby sa ich výsledkom
dalo dôverovať. Neznamená to opakovane spustiť každý starý skript.

## Základné pravidlo

Audit postupuje po **závislostiach**, nie po čísle skriptu. Ak rodičovský
vzorec alebo stavový priestor neprejde, jeho potomkovia sa neprepočítavajú;
dostanú `REVIEW_BLOCKED` a zachovajú sa ako historické artefakty. Každý
balík musí spĺňať AR66.2: rodičovská rovnica, term map, nezávislé rezíduum,
limity a rozmery.

## Prehľad balíkov

| ID | Auditný balík | Prečo je dôležitý | Aktuálny stav | Potrebný výsledok | Priorita |
|---|---|---|---|---|---|
| R0 | Provenance a nemennosť artefaktov | bez hashov a väzieb sa nedá povedať, čo bolo testované | čiastočne: manifesty, karanténa, P5 index | cesta → hash → dokument → JSON → verdict pre aktívne a citované artefakty | P0 |
| R1 | A1-K1 kanonický background | všetky A2 výsledky používajú `X_i(a), E(a), gamma=lambda/E` | P2a/P3/P5.1 čiastočne PASS | nezávislá term map continuity → H/E/D, limity a jednotky | P0 |
| R2 | `K_MPC=0.05` a background/perturbation rozdelenie | pevný perturbatívny mód nesmie preniknúť do backgroundu | P2/P3/P4 auditované; starý K7 STOP | prejsť všetkých potomkov starého denominatoru a označiť scope | P0 |
| R3 | A2-K4 covariant → species rovnice | rozhoduje, či mechanizmus vôbec implementuje deklarované `Q^mu` | L2-B2.1 a P5.1/P5.2 čiastočne PASS | úplný formula ledger C1–C6, vrátane palivovej kontinuity a gauge konvencií | P0 |
| R4 | P5 seed → evolúcia | zlé seedy môžu simulovať stabilitu alebo nestabilitu | P5.3b–e leading PASS, stále neúplné | full hierarchy seed, gauge-invariant relatívny mód, dva štarty | P0 |
| R5 | K7 projected lineage | historické vysoké skóre nesmie byť použité mimo rozsahu | L2-B1 PASS; implementačný STOP | overiť, že všetky citujúce dokumenty nesú obmedzenie; žiadny fyzikálny rerun | P0 |
| R6 | BR2/K4.3b staré backreaction behy | majú správne jadro, ale seed bol `Gamma=0` extension | L2-B2/B2.1 PASS_MAP/formula core | označiť výsledky ako seed-limited; po P5 seedoch zopakovať iba relevantnú krátku bránu | P1 |
| R7 | A2-K1 až A2-K6 rozsudky smrti | potrebujeme dôverovať, že mŕtve koľaje nezomreli na chybu implementácie | **CLOSED `CONFIRMED_SCOPE` 2026-07-16 pre K1,K2,K3,K5,K6; K4 je živá a patrí R1–R4** | seal: `Audit/A2_R7_POST_ERROR_SCOPE_SEALS_K1_K2_K3_K5_K6_2026-07-16.md` | P1 CLOSED |
| R8 | A2-K7/K8/K9/K11/K12 živé zálohy | ak K4 zastane, nesmú sa začínať z neoverenej starej formulácie | **parent blockers mapped 2026-07-16; konkrétne dcéry ešte nemajú operátor** | každá nová dcéra musí dostať formula-provenance pred prvým solverom; staré K11 PASS ostávajú zrušené | P1 |
| R9 | G8 screen a CAMB/CLASS väzba | G8 nesmie skryť zjednodušený K7 stav ako plný model | screeny scope-limited; FULL blokovaný | shared operator, hierarchy seed, `lmax` convergence, independent Einstein–Boltzmann residuals | P0 pred G8 |
| R10 | Numerická dôveryhodnosť | malé rezíduum môže byť škálovací artefakt alebo tautológia | error ledger a karanténa existujú | replay iba autoritatívnych runnerov s timeoutom, dva kroky/metódy, nezávislé residualy | P1 |
| R11 | Pozorovacie fitovanie a tabuľka predpovedí | čísla S8/H0 nesmú byť výsledkom neplatnej formulácie | zatiaľ pred G8/G9 | zmrazená fyzika, likelihood provenance, reprodukovateľné datasety, nové/opravené predpovede | P2 |
| R12 | Release/Zenodo/GitHub | citovateľná verzia nesmie meniť minulosť | changelog pravidlo existuje | release snapshot, hashes, changelog, status koľají, prediction-table diff | P2 |

## Čo sa už nemá robiť

- znovu spúšťať K7/213 ako fyzikálny dôkaz A2-K4;
- prepočítavať skript len preto, že je starý alebo má nízke číslo;
- akceptovať `PASS` z testu, ktorý meria definíciu rovnakou definíciou;
- meniť mŕtvy alebo immutable artefakt namiesto vytvorenia nástupcu;
- spúšťať G8, G9 alebo meniť predpovede pred R1–R4 a R9.

## Povinné kontroly v každom spätnom balíku

1. **Identita:** SHA-256, zdrojová cesta, verzia závislostí, vstupný JSON.
2. **Formula provenance:** rodič, konvencie, term map, aproximácie.
3. **Fyzika:** zachovanie energie-hybnosti, gauge, rozmery, nulové limity,
   stabilita alebo jasný invariantný no-go dôvod.
4. **Numerika:** interný aj vonkajší limit, nezávislé residualy, krok/metóda
   tam, kde sa integruje; žiadne fail-open čítanie JSON.
5. **Rozsah:** jasne pomenovať, čo výsledok nedokazuje.
6. **Rozsudok:** `PASS_MAPY`, `PASS_SCOPE`, `STRUCTURAL PASS`, `FORMULA PASS`,
   `REVIEW_BLOCKED` alebo `STOP`; nie neurčité „PASS“.

## Odporúčané poradie

1. dokončiť **R4/P5.3f** a potom P5.4;
2. uzavrieť **R1–R3** jedným formula ledgerom A1 → K4 → P5;
3. pridať obmedzenia **R5–R6** ku všetkým citujúcim status/release dokumentom;
4. **R7 je uzavretá** pre scope-limited STOP K1, K2, K3, K5 a K6; pri
   návrate k živej zálohe vykonať jej konkrétny R8 formula seal;
5. pred prvým G8 spraviť **R9**, až potom numerické replaye R10;
6. G9, tabuľka predpovedí a release až po tom.

## Kritérium dostatočnej dôvery pred G8

G8 je povolená iba ak R1, R2, R3, R4 a R9 majú príslušný formula/seed
verdict, P5.4 má nezávislé dynamické residualy a R5/K7 je všade označená ako
historická redukovaná vetva. Ostatné retrospektívne balíky môžu pokračovať
paralelne, ale ich neuzavretie nesmie meniť status G8.

## Údržba

Tento plán sa aktualizuje iba pri uzavretí balíka R0–R12, pri novom náleze
formulového problému alebo pred release. Súvisiace pravidlá: AR66.1,
AR66.2, AR8 a `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md`.
