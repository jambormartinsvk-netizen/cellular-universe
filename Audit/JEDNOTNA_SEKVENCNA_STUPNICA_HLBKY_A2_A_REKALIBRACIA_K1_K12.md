# Jednotná sekvenčná stupnica hĺbky A2 a rekalibrácia K1–K12

**Dátum:** 2026-07-14  
**Dôvod:** staré percentá miešali úspešne prejdenú hĺbku s najhlbšie
vykonaným testom; medzi koľajami preto neboli plne porovnateľné  
**Autoritatívny výsledok:** skóre je odteraz iba najvyššia **sekvenčne
prejdená** kanonická brána

## 1. Nájdený problém

Staré skóre používalo formuláciu „najhlbší vykonaný test“. To umožnilo, aby
koľaj dostala vysoké číslo aj vtedy, keď:

- preskočila povinnú medzibránu;
- neskorší konzervatívny no-go test ju zabil;
- test nebol plnou vlastnou implementáciou danej koľaje;
- skóre označovalo checkpoint vnútri jednej brány, nie rovnakú fyzikálnu
  úroveň ako pri inej koľaji.

Príklad: K5 dostala `75/100` za CMB-kotvený hybridný screen, hoci nemala
vlastnú úplnú fotónovo-neutrínovú Boltzmannovu implementáciu a nemala
auditovanú úplnú bázu všetkých regulárnych módov. Screen môže oprávnene zabiť
konkrétnu akciu M-012, ale nesmie predstierať, že K5 sekvenčne prešla všetky
brány do 75.

## 2. Dve povinné a oddelené veličiny

### 2.1 Kanonická max. prejdená hĺbka

Najvyššia brána `Gn`, ktorá prešla a prešli aj všetky `G0...G(n-1)`.
Jediná táto hodnota sa zapisuje ako `N/100` a je porovnateľná medzi koľajami.

### 2.2 Najhlbšie vykonaný test / brána smrti

Neskorší test sa eviduje osobitne. Môže koľaj zabiť aj bez vykonania každej
medzibrány, ak je to nutná podmienka alebo konzervatívny no-go. Nezvyšuje
však kanonické skóre.

Mŕtva koľaj si zachová:

- kanonickú max. prejdenú hĺbku;
- identifikátor a dôvod smrti;
- najhlbšie vykonaný test;
- skripty a výstupy.

## 3. Jednotná stupnica G0–G10

| Brána | Skóre | Rovnaká požiadavka pre každú A2 koľaj |
|---|---:|---|
| G0 | `0/100` | iba neregistrovaný nápad; ešte nie koľaj |
| G1 | `10/100` | fyzikálne odlišná hypotéza, stupne voľnosti, parametre a rozdiel od existujúcich koľají sú zapísané |
| G2 | `20/100` | uzavretý background a úplný ledger energie/hybnosti reprodukujú registrovaný A1 bez placeholdera |
| G3 | `30/100` | lokálna akcia alebo úplný kovariantný konštitutívny uzáver; žiadny chýbajúci operátor, frame ani zdroj |
| G4 | `40/100` | úplné lineárne kontinuity, Eulery a Einsteinove constrainty; znamienka, gauge mapovanie a nulový limit |
| G5 | `50/100` | úplná constraintovo prípustná regulárna superhorizontová báza všetkých fyzických módov |
| G6 | `60/100` | ghost/gradient/high-k a subhorizontová stabilita celej regulárnej bázy; konvergencia na relevantnej `k` mriežke |
| G7 | `70/100` | vlastná úplná Einstein–Boltzmannova implementácia: fotóny, neutrína, anizotropný stres, tight coupling, rekombinácia, fyzické transfery, null/gauge/convergence |
| G8 | `80/100` | CMB-normalizované spektrá a rastová brána `sigma8/S8`; nie iba ľubovoľne normalizovaný efektívny mód |
| G9 | `90/100` | vlastná spoločná CMB+BAO+lensing likelihood, nuisance/systematiky a robustnosť parametrov |
| G10 | `100/100` | všetky predregistrované brány verzie, nezávislá reprodukcia a požadované nelineárne/ďalšie predikcie |

Skóre sa udeľuje iba po celej bráne. Čísla `25`, `42`, `55`, `59`, `75`
sa odteraz nepoužívajú ako kanonická hĺbka. Môžu zostať iba v historickom
changelogu alebo ako označenie starého interného checkpointu.

## 4. Rekalibrácia hlavných koľají

| Koľaj | Stav | Staré skóre | Nová kanonická max. hĺbka | Najhlbšie vykonaný test / otvorená brána | Dôvod zmeny |
|---|---|---:|---:|---|---|
| A2-K1 | `MŔTVA M-009` | 45 | **40** | G5 superhorizontový no-go | G4 rovnice/sign/null prešli; úplná regulárna báza nebola dokončená |
| A2-K2 | `MŔTVA M-008` | 25 | **30** | G6 analytická high-k gradientová smrť | uzavretý barotropický model prešiel G3; úplný G4 systém sa nerobil |
| A2-K3 | `MŔTVA M-010` | 45 | **40** | G5 superhorizontový no-go | rovnaká sekvenčná úroveň ako K1 |
| **A2-K4** | **`PREŽÍVA K4.2`** | 59 | **60** | **G7 otvorená** | jediná koľaj s úplnou regulárnou bázou aj high-k/subhorizontovou bránou |
| A2-K5 | `MŔTVA M-012` | 75 | **40** | G6 efektívny rast vykonaný; G8 hybridný CMB screen zabil koľaj | K5 nemala úplnú G5 bázu ani vlastnú G7 Boltzmannovu implementáciu; neskorý no-go ostáva platný, ale nezvyšuje skóre |
| A2-K6 | `MŔTVA M-013` | 60 | **30** | G6 presný `G_ij`/QS no-go | akcia/background/stabilitný uzáver prešli G3; úplné G4–G5 sa po nutnom no-go nerobili |
| A2-K7 | `PREŽÍVA CEZ PODKOĽAJE` | 30 | **20** | G3 otvorená | ledger a background sú zapísané, ale chýba odvodený lokálny kernel, `delta Q`, noise/memory |
| A2-K8 | `ČAKÁ` | 5 | **10** | G2 otvorená | fyzikálne odlišná produkcia počtu je registrovaná; chýba ledger/creation operator |
| A2-K9 | `ČAKÁ` | 5 | **10** | G2 otvorená | spoločný produkčno-rozptylový operátor je iba registrovaná hypotéza |
| A1-K2/A2-K10 | `ČAKÁ; INÁ A1 VETVA` | 5 | **10** | nová A1/G2 otvorená | pomenovaná odlišná backgroundová koľaj; neporovnáva sa ako záchrana A1-K1 |
| A2-K11 | `PREŽÍVA IBA HYPOTÉZU` | 15 | **10** | G2/G3 otvorená | ortogonálny drag je pomenovaný, ale chýba prijatý lokálny operátor a úplný ledger |
| A2-K12 | `PREŽÍVA CEZ K12-K2/K3` | 25 | **10** | G2 otvorená | opačné náboje sú registrované; bez samostatného production operatora nereprodukujú A1 tok |

## 5. K12 podkoľaje

| Podkoľaj | Nové skóre | Testovaná brána | Stav |
|---|---:|---|---|
| K12-K1 | `10/100` | G2 FAIL: presná symetria dá nulový čistý tok | `MŔTVA M-016` |
| K12-K2 | `10/100` | G2 otvorená: úplný asymetrický background/ledger | `OTVORENÁ — ČERVENÁ` |
| K12-K3 | `10/100` | G2 otvorená: lokálny `fuel -> c+ + c-` operátor | `AKTÍVNA HYPOTÉZA` |

## 6. K7 podkoľaje

Staré `32–42/100` boli checkpointy **vnútri jednej mikrofyzickej G3
brány**, nie úrovne medzi G3 a G4 porovnateľné s inými koľajami. Preto:

- kanonická rodina K7 a jej odvodené vetvy majú najviac `20/100`, kým
  niektorá konkrétna vetva neuzavrie celý lokálny kernel, noise/memory a
  pozitivitu G3;
- staré čísla 32–42 sa nemažú; presúvajú sa do stĺpca
  `historický intra-G3 checkpoint`;
- mŕtve listy zostávajú mŕtve s pôvodnými dôvodmi M-014...;
- nová alebo zmenená mikrofyzická dcéra nezdedí G3 iba názvom; zdedí iba
  G1–G2, ktoré fyzikálne nemení.

## 7. Čo presne ešte chýba K4 pred A3

K4 nie je na 60 preto, že by jej chýbal jeden malý výpočet. Otvorená G7 je
samostatná veľká brána:

1. samostatná fotónová a neutrínová hierarchia;
2. neutrínový anizotropný stres a `Phi != Psi`;
3. baryón-fotónový tight coupling a rekombinácia;
4. úplné regulárne počiatočné podmienky v rozšírenom systéme;
5. implementácia rovnakého K4 operátora bez nového drag fitu;
6. bodové constrainty, nulový limit, gauge alebo nezávislý code cross-check;
7. konvergované fyzické transfery `delta_m(k,z)`.

Až prejdenie celej G7 dá K4 `70/100` a právo prejsť do A3/G8. CMB
normalizácia, `sigma8`, `S8` a dátový screen sú G8, nie súčasť skóre 60.

## 8. Obmedzenie starších formulácií

Tento audit nemení nijaký fyzikálny rozsudok. Mení iba význam a hodnotu
skóre:

- AR14 sa obmedzuje: „najvzdialenejšia zdokumentovaná brána“ odteraz
  znamená najvzdialenejšiu **sekvenčne úspešne prejdenú** bránu;
- staré „max. hĺbka = najhlbší vykonaný test“ sa nahrádza dvoma stĺpcami;
- staré percentá zostávajú v historických auditoch a manifestoch, ale
  aktuálne stavové tabuľky ich nesmú používať ako kanonické skóre.

