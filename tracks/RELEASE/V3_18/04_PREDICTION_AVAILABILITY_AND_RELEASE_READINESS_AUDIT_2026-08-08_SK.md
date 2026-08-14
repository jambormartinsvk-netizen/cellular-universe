# Audit dostupnosti predikcií a pripravenosti vydania v3.18

**Dátum auditu:** 2026-08-08  
**Auditovaný release candidate:** `D:\Teoria-v3.18-release`  
**Rozsah:** P01–P11, hlavný SK dokument, SK register predikcií a draft Zenodo description  
**Typ zápisu:** pracovný release audit; nemení stav ani skóre vedeckých koľají  
**Autoritatívny rozsudok hlavného orchestrátora:** `REVIEW_DOCUMENTATION_CLARITY / SCIENTIFIC_STATUS_UNCHANGED`

## 1. Priama odpoveď

Nie, v3.18 nemá „tri predikcie“. Tri zobrazené riadky sú tri **zvolené
vstupné hodnoty** `Delta N_eff` jedného podmieneného citlivostného výpočtu.
Každý vstup dá dva výstupy, podmienené `H0` a podmienené `S8`.

Nie sú to tri nezávislé fyzikálne predikcie a ani intervaly teórie.

Aktuálny stav možno najpresnejšie zhrnúť takto:

| Trieda dostupnosti | Počet / obsah |
|---|---|
| úplná aktuálna tvrdá číselná predikcia KBTP | **0** |
| externe reprodukovaná podmienená diagnostická rodina | **1** — P04/P05 pri troch vložených hodnotách `Delta N_eff` |
| úzko platný štrukturálny výsledok | **1** — P10: nulový lineárny člen iba pre auditovaný párny skalárny cosine-Laplacian operátor |
| podmienený štandardný comparator vzorec bez odvodených vstupov | P01; súvisiaca termálna aritmetika P11 |
| odvolané presné tvrdenie | **1** — P08 |
| otvorené alebo zúžené ciele bez current číselného intervalu | zostávajúce riadky P01–P07, P09 a P11 podľa ich presného scope |

V3.18 je preto možné vydať ako **samostatný auditovateľný stavový snapshot
teórie**, nie ako vydanie novej sady tvrdých kozmologických predikcií.

## 2. Čo presne znamenajú tri publikované body

| vložené `Delta N_eff` | podmienené `H0` [km/s/Mpc] | podmienené `S8` |
|---:|---:|---:|
| `0` | `65.79213819466531` | `0.8856095825403126` |
| `0.02675` | `66.08320294879377` | `0.8800254370658636` |
| `0.0535` | `66.37433224357665` | `0.874499891729803` |

Tieto body dokazujú iba numerickú citlivosť zmrazeného legacy-anchor modelu
na jeden vložený príspevok. Ich **vzorkovaný číselný rozpon** je:

- `H0`: od `65.79213819466531` do `66.37433224357665 km/s/Mpc`;
- `S8`: od `0.874499891729803` do `0.8856095825403126`.

Tento rozpon sa nesmie nazvať predikčným, confidence ani credible intervalom,
spojitou obálkou alebo posteriorom. Tri hodnoty `Delta N_eff` takisto nie sú
odvodený povolený interval P01. Výpočet používa syntetickú kotvu
`h_ref=0.673`; `S8` používa zjednodušený rast a `sigma8_LCDM=0.811`.
`Delta N_eff=0` vypína iba legacy príspevok pary a nie je nulovým limitom
celej teórie ani automaticky modelom LambdaCDM.

## 3. Audit P01–P11

| ID | Aktuálne dostupný obsah | Má v3.18 current rozsah? | Čo chýba k rozsahu alebo tvrdej hodnote |
|---|---|---|---|
| P01 `N_eff / Delta N_eff` | Rovnica termálneho reliktu (24) je platný **podmienený comparator**. Historický bod `Delta N_eff=0.0535`, `N_eff≈3.10` používa neodvodené predpoklady `g_x=2`, `g_*s,dec=106.75`. | **Nie.** Ani vstupný grid `0–0.0535` nie je interval teórie. | Odvodiť kovariantný zdroj `C_s`, čas produkcie a odpojenia, počet stupňov voľnosti, reheating, entropický ledger a branching hmota/para/popol; až potom preniesť meracie neistoty. |
| P02 `n_s` | Historické mechanistické čítanie `n_s-1=-3 delta/2`; pri zmrazenom `delta` by dalo iba historický bod, nie current predikciu. | **Nie.** | Uzavrieť gauge-invariantné `zeta`, amplitúdu a tvar `P_zeta(k)`, seed, gaussovskosť/izokurvatúry a plný A2 systém. |
| P03 `r` | Historická hranica `r<1e-10` je zachovaná iba pre históriu. | **Nie.** | Odvodiť tenzorový operátor, zdroj, počiatočný stav, skalárnu aj tenzorovú normalizáciu a mapu na CMB observable. |
| P04 `H0` | Tri reprodukované podmienené body uvedené v §2. | Iba **vzorkovaný diagnostický rozpon**, nie predikčný interval. | Jeden módovo nezávislý background, fyzické hustoty, rekombinácia a zvukový horizont, nezávislá dátová kotva, A3 CLASS/CAMB a likelihood s covariance. |
| P05 `S8` | Tri reprodukované podmienené body uvedené v §2. | Iba **vzorkovaný diagnostický rozpon**, nie predikčný interval. | Dokončený A2, úplná Boltzmannova hierarchia, fyzikálna normalizácia `A_s/sigma8`, lensing/LSS observable mapa a likelihood s covariance. |
| P06 `w0, wa` | Efektívna účtovná rekonštrukcia (23). Historické `w0=-0.919`, `wa=-0.612` nie sú current výsledok. | **Nie.** | Prijať jeden konzistentný `H(a)`, presne definovať projekciu na CPL a vykonať dátovú pipeline; oddeliť fundamentálne `w_f` od efektívneho `w_eff`. |
| P07 priama detekcia DM/popola | Iba podmienená falzifikačná otázka; absolútny zákaz negravitačných signálov bol správne zúžený. | **Nie je ešte definovaná veličina, ktorej rozsah možno počítať.** | Particle model popola: hmotnosť/spektrum, kvantové čísla, interakcie, abundancia, fázový priestor a detector response. |
| P08 presný `n_s-w` vzťah | Presná stará formula je `WITHDRAWN`. | **Nie; rozsah sa nemá zachraňovať bez nového odvodenia.** | Ak sa hypotéza obnoví, potrebuje novú explicitnú koľaj a nový dôkaz spoločného mikrofyzikálneho pôvodu; nesmie sa potichu obnoviť staré tvrdenie. |
| P09 časový drift `delta` | Konštantný benchmark existuje, ale funkcia `delta(a)` alebo `delta(x)` nie. | **Nie.** | Odvodiť dynamickú rovnicu pre `delta`, počiatočné/okrajové podmienky, stabilitu a mapu driftu na pozorovateľné veličiny. |
| P10 Lorentz/disperzia | V auditovanom skalárnom cosine-Laplacian scope je disperzia exaktne párna: lineárny nepárny člen je presne nula; prvá relatívna korekcia je `O((k l_cell)^2)`. | **Je dostupný exact štrukturálny výsledok, nie univerzálny experimentálny interval.** | Odvodiť fotónový operátor, boost sektor, koeficient kvadratickej korekcie, birefringenciu, multi-field spoločný kužeľ a ekvivalenčný princíp. |
| P11 termálne gravitónové/relativistické pozadie | Historické `0.90 K / 53 GHz` pochádza z podmieneného instant-decoupling čítania. | **Nie.** | Rovnaký zdrojovo-entropický uzáver ako P01 plus spektrum, polarizácie, dnešný transfer a detekčná observable mapa. |

## 4. Prečo dnes nemožno poctivo doplniť „aspoň rozsah“ ku každému riadku

Rozsah je vedecký výsledok iba vtedy, keď sú odvodené alebo predregistrovane
obmedzené domény jeho vstupov. Ak zatiaľ nepoznáme zdroj `C_s`, tensorový
operátor, `delta(a)` alebo particle model popola, vloženie ľubovoľne širokých
odhadov by vytvorilo ad-hoc interval bez fyzikálnej váhy.

Povolené je viesť **prípustnú množinu funkcií a mantinelov**. To je správna
metóda pre ďalší výskum, ale `RANGE_CONDITIONAL_OPEN` nie je vypočítaný
predikčný interval. Rozsah možno povýšiť na current výsledok až po dôkaze, že:

1. jeho vstupná doména pochádza z rovníc alebo explicitných pozorovacích
   hraníc;
2. všetky body rešpektujú conservation, covariance, gauge, kauzalitu,
   stabilitu a správne nulové limity;
3. model-to-observable mapa je úplná;
4. boli zahrnuté neistoty a covariance;
5. výsledok prešiel nezávislým auditom exact contractu a výpočtu.

## 5. Čo treba urobiť, aby bolo možné vydať v3.18

### 5.1 Odporúčaná cesta: stavové vydanie v3.18

Túto verziu možno dokončiť bez predstierania, že P01–P11 už majú číselné
intervaly. Pred publikovaním odporúčam povinne odstrániť možné čitateľské
nedorozumenie v Zenodo popise:

1. V SK §8 a v SK CSV pridať explicitnú **triedu kvantitatívnej dostupnosti**
   a stĺpec „čo chýba k rozsahu“ podľa §3 tohto auditu.
2. Rovnakú významovú zmenu preniesť do EN §8 a EN CSV; SK zostáva významovou
   autoritou.
3. V `zenodo_description_v3.18.html` pred troma bodmi výslovne uviesť:
   „11 registrovaných predikčných cieľov; 0 úplných current tvrdých
   číselných predikcií; 1 podmienená diagnostická rodina P04/P05; 1 úzko
   štrukturálny výsledok P10; P08 withdrawn.“
4. Nad tabuľku troch bodov doplniť, že nejde o zoznam troch predikcií, ale o
   tri vstupy jedného citlivostného testu. Možno uviesť vzorkovaný rozpon,
   vždy s explicitným zákazom interpretovať ho ako interval teórie.
5. Zapísať túto post-preseal dokumentačnú opravu do `CHANGELOG_v3.18.md`.
6. Pregenerovať `RELEASE_STAGING_MANIFEST_v3.18.tsv` a
   `MANIFEST_v3.18.sha256`; staré preseal hashe po zmene payloadu prestanú
   platiť.
7. Znovu vykonať SK významový audit, EN parity audit, kontrolu odkazov,
   manifestov a finálny preseal audit. Toto je dokumentačný/release audit,
   nie opakovanie vedeckých official runov.
8. Martin Jambor prečíta a výslovne schváli finálnych 13 payload súborov.
9. Až potom: `git add` -> kontrola staged diff/hashov -> commit na release
   vetve -> push -> pull request -> schválenie/merge -> nemenný tag `v3.18`.
10. Zenodo payload nahrať ručne až z exact tagu, overiť 13 súborov a SHA-256,
    priradiť DOI a zverejniť bez tichého prepisu; následne doplniť DOI do
    GitHub release metadát podľa release pravidiel.

### 5.2 Iná, výrazne dlhšia cesta: vydanie s novými tvrdými intervalmi

Ak má byť podmienkou vydania aspoň jedna nová úplná kozmologická predikcia,
v3.18 dnes pripravená nie je. Najkratšia fyzikálna cesta vedie cez:

1. lokálny kovariantný a konzervačný mechanizmus produkcie/branchingu
   hmota–para–popol;
2. jeden univerzálny módovo nezávislý `H(a)`;
3. dokončenie jednej A2 koľaje vrátane všetkých Einsteinových constraintov,
   gauge-invariantných módov a super/subhorizontálnej stability;
4. úplnú fotónovú a neutrínovú Boltzmannovu hierarchiu;
5. A3 implementáciu v CLASS/CAMB s nulovým limitom a numerickou
   konvergenciou;
6. fyzikálnu normalizáciu skalárneho a tenzorového spektra;
7. spoločnú CMB/BAO/BBN/lensing/LSS likelihood s neistotami a covariance;
8. až potom výpočet predregistrovaných intervalov P01–P06 a P11.

P07, P09 a úplné P10 navyše vyžadujú svoje mikrofyzické operátory; nemožno
ich automaticky získať iba z kozmologickej likelihood.

## 6. Rozsudok pripravenosti

| Otázka | Rozsudok |
|---|---|
| Má v3.18 tri nezávislé predikcie? | **Nie.** Má tri body jedného podmieneného diagnostického testu. |
| Má v3.18 aspoň jednu úplnú aktuálnu tvrdú číselnú predikciu? | **Nie.** |
| Obsahuje vedecky hodnotné current výsledky? | **Áno.** Opravy chybných historických tvrdení, auditované backgroundové/štrukturálne mosty, P10 exact scoped result a reprodukovanú P04/P05 citlivosť. |
| Dá sa v3.18 poctivo vydať? | **Áno, ako self-contained status/methodology release**, po oprave prezentácie dostupnosti predikcií a obnovení preseal auditov. |
| Je v3.18 pripravená ako „prediction release“? | **Nie.** Vyžadovala by uzavretie A2 a A3 pipeline. |

Odporúčanie je vydať v3.18 ako poctivý, úplný a auditovateľný stav teórie.
Jej vedeckou hodnotou nie je množstvo nových tvrdých čísel, ale presné
oddelenie toho, čo prežilo audit, čo je iba conditional, čo bolo zúžené a čo
bolo odvolané. Číselné intervaly sa nesmú doplniť iba preto, aby release
pôsobil predikčne bohatšie.

## 7. Súborový rozpočet tohto auditu

- `LIVE_SCIENTIFIC_ARTIFACTS = 1` — tento release audit;
- `LIVE_CENTRAL_REGISTERS_UPDATED = 0`;
- `RELEASE_PAYLOAD_FILES_UPDATED = 0`;
- `AUDIT_PACKAGE_COPIES = 0`;
- autoritatívny vedecký stav, skóre a hĺbka koľají: **bez zmeny**.

