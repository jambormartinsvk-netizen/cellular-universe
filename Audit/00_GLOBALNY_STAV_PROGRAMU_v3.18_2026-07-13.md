# Globálny stav programu Bunkového priestoru pre v3.18

**Dátum stavu:** 2026-07-13  
**Typ dokumentu:** autoritatívny stavový register  
**Rozsah:** A0–A8, otvorené fundamentálne otázky, vetva `S8/H0` a pripravenosť vydania

## 1. Autorita dokumentu

Tento dokument zjednocuje stav, ktorý bol postupne rozptýlený medzi staršími auditmi, registrami otázok, návrhmi v `Nespracovane` a novými auditmi vetvy `S8/H0`.

Pri rozpore o **aktuálnom stave alebo poradí práce** má tento dokument prednosť pred staršími stavovými súhrnmi. Pôvodné dokumenty zostávajú zachované ako auditná stopa; nejde o ich tiché prepísanie.

Podrobný vykonávací plán je v:

- `Questions/00_AKCNY_PLAN_v3.18_AKTUALNY_2026-07-13.md`

Aktuálna triáž materiálov na zapracovanie je v:

- `Nespracovane/00_AKTUALNY_TRIAGE_A_ZAPRACOVANIE_v3.18_2026-07-13.md`

## 2. Význam stavov

- **VYBAVENÉ:** krok splnil svoj deklarovaný rozsah.
- **PREŠLO BRÁNOU:** výsledok je použiteľný iba v uvedenom rozsahu; nie je to potvrdenie celej teórie.
- **AKTÍVNY ĎALŠÍ KROK:** najbližšia práca s najvyššou informačnou hodnotou.
- **ČAKÁ / BLOKOVANÉ ZÁVISLOSŤOU:** krok nesmie byť vyhlásený za hotový pred splnením uvedenej závislosti.
- **PREŽÍVA N/100:** hypotéza zatiaľ nenarazila na potvrdený fyzikálny rozpor, ale jej zrelosť je obmedzená.
- **MŔTVA:** konkrétna formulácia alebo tvrdenie neprešlo fyzikálnou, matematickou alebo štatistickou bránou. Neznamená to automaticky smrť každej príbuznej formulácie.

## 3. Hlavný záver auditu stavu

Teória **ešte nie je pripravená vydávať nové presné predikcie pre rast štruktúr, `S8` ani úplný fit `H0`**. Má však konzistentného pracovného kandidáta pre kozmologické pozadie: prenos energie z palivovej zložky vytvára CDM/popol, baryóny sa zachovávajú samostatne.

Tento kandidát prešiel kontrolami pozadia, ale neprešiel perturbáciami, stabilitou ani plným likelihoodom. Preto je bezprostredným ďalším krokom **A2/Q20: kovariantná a gauge-konzistentná teória perturbácií**.

## 4. Stav krokov A0–A8

| Krok | Aktuálny stav | Čo je skutočne hotové | Čo ešte nesmie byť tvrdené | Nasledujúca brána |
|---|---|---|---|---|
| **A0 — verzovanie a nemennosť** | **VYBAVENÉ** | Zenodo v2/v3.17 sa nemení; každé ďalšie publikované vydanie dostane changelog a kontrolné súčty. | Staré publikované čísla sa nesmú spätne nahradiť novými. | Pri vydaní vytvoriť manifest súborov, hashov a changelog. |
| **A1 — prijímateľ zdroja `Q`** | **PREŠLO BRÁNOU POZADIA** | Koľaj A1-K1: `Q` vytvára CDM/popol, baryóny sú konzervované. Prešli rozmerové, bilančné, limitné, pozitivitné a numerické kontroly pozadia. | A1-K1 ešte nie je vybraná fyzikálna teória perturbácií ani potvrdený mikroskopický mechanizmus. | A2: perturbácie, stabilita a kovariantná bilancia. |
| **A2 — perturbácie interagujúcich zložiek** | **AKTÍVNY ĎALŠÍ KROK** | Existujú požiadavky a auditné brány. | Neexistuje uzavretý overený súbor perturbovaných rovníc pre všetky zložky. | Odvodiť `Q_A^mu`, energetickú a hybnostnú časť, limity a stabilitu. |
| **A3 — implementácia v Boltzmannovom riešiči** | **BLOKOVANÉ A2** | Máme pomocné a citlivostné skripty, nie plnohodnotný Boltzmannov riešič modelu. | Skript 09 ani lokálne gridy nie sú náhradou CLASS/CAMB a plného spektra. | Najprv reprodukovať ΛCDM v rovnakej pipeline, potom zapnúť bunkový model. |
| **A4 — para, časovanie a exit/reheating** | **OTVORENÉ** | Sú formulované otázky Q18 a Q23. | `Delta N_eff` ani história pary nie sú odvodené ako úplná termodynamická história. | Definovať vznik, tepelnú väzbu, decoupling, entropický ledger a exit. |
| **A5 — primordiálne perturbácie** | **BLOKOVANÉ A4/Q21/Q22** | Sú evidované hypotézy pre `n_s`, amplitúdu a fluktuácie. | `m=1/2`, `C=28`, gaussovskosť a prevod `delta E -> zeta` nie sú vetami teórie. | Jednotný generátor fluktuácií, gauge-invariantný prevod na `zeta`, distribúcia a spektrum. |
| **A6 — 3D sieť verzus 4D kauzalita** | **KRITICKY OTVORENÉ** | Problém je explicitne priznaný. | Nemožno tvrdiť plnú relativistickú konzistenciu iba z 3D rastového grafu s globálnym časom. | Odvodiť 4D kauzálnu štruktúru alebo presne priznať preferovaný rámec a otestovať jeho limity. |
| **A7 — reprodukovateľnosť skriptov** | **ČIASTOČNE VYBAVENÉ** | Auditné skripty 11–20 majú stavové dokumenty; 17–20 reprodukovali deklarované toy-gridy a odhalili ich interpretačné limity. | Pomocné skripty 06–10 nemožno automaticky povýšiť na dôkaz fyziky modelu. | Opraviť popisy, zmraziť vstupy/výstupy a oddeliť smoke test, aproximáciu a fyzikálnu predikciu. |
| **A8 — plný dátový fit** | **BLOKOVANÉ A2+A3** | Existujú referenčné dátové body a predbežné citlivostné porovnania. | `chi2_3front`, post-data optimum ani dvojparametrové gridy nie sú globálny likelihood alebo dôkaz zlepšenia oproti ΛCDM. | Definovať dataset, covariance, nuisance parametre, priory, počet parametrov a slepú validačnú množinu. |

## 5. Stav A1 bez nadinterpretácie

Pracovná koľaj **A1-K1** znamená iba:

1. na homogénnom pozadí ide energia zo zdrojovej/palivovej zložky do CDM/popola;
2. baryónová zložka nemá tento zdroj;
3. súčet zdrojov zachováva celkovú energiu;
4. hustoty zostali v testovanom rozsahu kladné;
5. limit bez interakcie sa správa správnym smerom.

Numerický referenčný výsledok pozadia zostáva:

- približne `8.999 %` dnešnej komovanej CDM bolo v tejto implementácii vytvorenej od rekombinácie;
- výsledok nie je meranie ani odvodenie mikrofyziky;
- test T7 (perturbácie) patrí A2 a T8 (plný likelihood) patrí A8.

Preto je presný stav: **A1-K1 PREŽÍVA ako kandidát pozadia; nie je definitívne VYBRANÁ.**

## 6. Dôležité rozlíšenie rovnako pomenovaných koľají

V dokumentoch vznikla kolízia označenia `K1`:

- **A1-K1:** prijímateľ energie `Q` je CDM/popol; táto koľaj prešla bránou pozadia.
- **S8-K1a:** konštantné fenomenologické trenie pridané celej látke; táto formulácia je **MŔTVA**.
- **S8-K1b:** kovariantná výmena hybnosti iba v tmavom sektore, s určeným nositeľom protihybnosti; **PREŽÍVA 35/100**, ale zatiaľ bez rovníc a testov A2.

Tieto tri položky sa nesmú v ďalších dokumentoch zamieňať.

## 7. Stav vetvy `S8/H0`

| Koľaj/tvrdenie | Stav | Dôvod |
|---|---:|---|
| Konštantné trenie celej látky `gamma_drag` | **MŔTVA** | Nie je kovariantne uzavreté, nerozlišuje baryóny/CDM a nemá nositeľa protihybnosti. |
| Kovariantná výmena hybnosti iba popol–tmavý sektor | **PREŽÍVA 35/100** | Fyzikálne možná trieda, ale potrebuje `Q_A^mu`, stabilitu, CMB/LSS a plný likelihood. |
| FLRW s voľným `Omega_K` ako fenomenologický test | **PREŽÍVA 63/100** | Je to štandardne konzistentná geometrická rozšírená kozmológia, nie odvodenie z bunkovej siete. |
| Odvodenie nenulovej krivosti z bunkovej siete | **PREŽÍVA 20/100** | Zatiaľ chýba škálovací limit, Reggeho/ekvivalentná geometrická mapa a nezávislá predikcia znamienka i veľkosti. |
| Tvrdenie, že `Omega_K = 0.005` vyriešilo obe napätia | **MŔTVA ako dôkaz** | Bod bol zvolený po dátach, zvyšuje `Omega_m`, nemá plný likelihood a voči SH0ES zostáva výrazné rezíduum. |
| Kombinácia `Omega_K=0.002`, `gamma=0.015` trafí cieľ | **MŔTVA** | Reprodukcia dala približne `H0=67.267` a `S8=0.8251`, nie deklarovaný cieľ. |
| Kombinovaná fyzikálna trieda krivosť + výmena hybnosti | **PREŽÍVA 35/100** | Nie je v rozpore sama osebe, ale má nulovú predikčnú váhu, kým sa parametre neodvodia pred dátami. |

Z toho plynie zákaz používať gridy 17–20 ako „presnú kalibráciu“ alebo dôkaz zlepšenia o určitý počet bodov `chi2`. Sú reprodukovateľnými **citlivostnými toy-výpočtami**.

## 8. Ďalšie fundamentálne otvorené vetvy

- **Q4 — vznik jazvy a pôvod `epsilon`:** otvorené. Hodnota `epsilon` nie je odvodená z prvých princípov siete.
- **Q8 — tri roly domény I:** otvorené. Nie je dokázané, že ireverzibilná jazva, kolaps a šíp času sú jedným mikroskopickým operátorom.
- **Q11d — gaussovskosť:** otvorené. Treba testovať celý generatívny mechanizmus, nie iba prispôsobiť histogram.
- **Q6 — anizotropia siete:** čiastočne spracované. Pozorovaný pokles v konečných simuláciách nie je analytický dôkaz nulovej makroskopickej anizotropie.
- **`lambda`, `m=1/2`, `C=28`:** zostávajú fitom alebo mechanistickým čítaním, nie odvodenými vetami.

Tieto vetvy sú dôležité, ale pre kozmologické tvrdenia má teraz najvyššiu prioritu A2, lebo môže rýchlo zabiť alebo zachrániť celý kandidátsky model pozadia.

## 9. Pripravenosť verzie 3.18

### 9.1 Úzka dokumentačná v3.18

Môže zostať verziou **3.18**, ak jej cieľ bude:

- changelog a auditná stopa;
- oprava rozdelenia baryónov a CDM na pozadí;
- A1-K1 jasne označená ako pracovný kandidát pozadia;
- erratá k starým interpretáciám skriptov a `S8/H0`;
- otvorené otázky a falzifikačné brány bez nových tvrdení o plnom raste štruktúr.

Taká verzia ešte potrebuje redakčnú konsolidáciu, manifest a kontrolné súčty, ale nemusí predstierať dokončené A2/A3/A8.

### 9.2 Kozmologicky prediktívna v3.18

Ak má v3.18 publikovať nové hodnoty `S8`, CMB, matter power spectrum alebo globálny fit `H0`, **nie je pripravená**. Pred vydaním musí prejsť A2, A3 a A8.

### 9.3 Kedy už verzia 4

Označenie **v4** je potrebné, ak úspešná koľaj zmení fundament teórie, napríklad:

- zavedie nový základný mediátor alebo pole;
- zmení základnú topológiu či kauzálnu štruktúru;
- zmení význam bunky, domény I alebo základného zákona delenia;
- nahradí doterajší fundament iným dynamickým princípom.

Kovariantné doplnenie perturbácií existujúcich zložiek bez zmeny fundamentu zostáva v rade v3.

## 10. Autoritatívny ďalší krok

**Začať A2.0 a A2.1:** vytvoriť jednoznačný kovariantný ledger zložiek a odvodiť perturbácie základnej A1-K1 bez dodatočného trenia.

Vetva S8-K1b sa smie otvoriť až po tom, čo základný energetický prenos prejde limitmi, gauge kontrolou a stabilitou. Krivostná K4b môže bežať ako nezávislá vedľajšia vetva, ale nesmie zdržať A2 ani sa kalibrovať na požadované `H0`.

