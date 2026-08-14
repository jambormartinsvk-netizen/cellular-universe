# A2-K4/P5.3g7 — pevné vstupné vetvy pre úplný seed

**Dátum:** 2026-07-16  
**Stav:** `REVIEW_BLOCKED`; toto je mapa vstupov, nie nový fyzikálny výsledok ani nový skript.  
**Účel:** pred jedným budúcim testom 261 presne oddeliť, čo možno prevziať ako overiteľný nulový limit, od toho, čo musí odvodiť bunková mikrofyzika.

## Prečo nestačí doplniť dve čísla

Plný seed má obsahovať metrické premenné `h, eta`, fotóny, štandardné neutrína, baryóny, popol `c`, palivo `f` a vo vetve S1 aj samostatnú paru `s`. Ak by sa `h` vybral z Einsteinovho constraintu, ktorý má 261 následne merať, výsledok by bol kruhový. Ak by sa para iba skopírovala zo štandardného neutrína, zmenila by sa kompenzácia neutrínových izokurvatúrnych módov bez odvodenia jej korelácie.

Použitá štandardná referencia je päť regulárnych módov AD/CDI/BI/NID/NIV v synchronnej gauge; ich úplnú klasifikáciu uvádza Bucher--Moodley--Turok a rovnice/adiabatický superhorizontový limit Ma--Bertschinger ([BMT](https://arxiv.org/abs/astro-ph/9904231), [MB](https://arxiv.org/abs/astro-ph/9506072)). Implementačný kontrolný bod je [CLASS](https://github.com/lesgourg/class_public), ktorý tieto módy označuje normalizáciou počiatočnej krivosti (AD), resp. entropy alebo relatívnej rýchlosti (CDI/BI/NID/NIV). Tieto zdroje **nie sú** odvodením K4 interakcie.

## Vetva M — metrický seed a nulový limit

| Povinnosť | Čo už vieme | Čo ešte musí prebehnúť | STOP proti skratke |
|---|---|---|---|
| M1: štandardný referenčný seed | script 84 má `eta`, hustoty a rýchlosti pre všetkých päť módov | z rovnakého fixovaného zdroja doplniť vedúce `h` a `h'` a konvenciu amplitúdy | nepoužiť `00`/`0i` constraint na definovanie `h` |
| M2: gauge deklarácia | starší test-field 86 už používal `U_c=0` len na štarte a po zapnutí K4 integroval `U_c` dynamicky | zapísať reziduálnu gauge konštantu a presne spojiť túto voľbu s M1 amplitúdou | `U_c=0` môže byť iba počiatočná koordinátová voľba, nie odstránenie dynamického `U_c` z P5 RHS |
| M3: K4 oprava | P5.3d určuje vedúce `c,f` členy pri všeobecnom `h_x=H a^n` | vložiť M1 normalizáciu, dopočítať K4 korekcie a porovnať ich s nezávislými constraintmi | štandardný seed sa nesmie označiť za plný K4 seed |
| M4: nulový limit | pri nulovej K4 výmene a nulovej pare sa má vrátiť štandardná báza | 261 musí tento limit explicitne otestovať pre AD, CDI, BI, NID, NIV | test jedného AD módu nestačí |

M1--M4 sú jedna konečná vetva, nie séria voľne vytváraných suffixov. Jej výsledok môže byť len `PASS_MAPY`, `REVIEW_BLOCKED` alebo `STOP` s invariantným dôvodom.

Historický test-field je užitočný, ale obmedzený: držal `h_x` na štandardnej
analytickej hodnote. Nezahŕňal spätný zdroj paliva prvého rádu
`a^(4-3 delta)` ani popolovú K4 korekciu a netestoval `00`, `0i`, trace ani
traceless Einsteinovo rezíduum. Je preto dôkazom M2, nie M1/M3/M4. Pozri
`Audit/A2_K4_3B_RG_REGULAR_SEEDS_PUISEUX_AND_SYNCHRONOUS_TEST_FIELD_AUDIT.md`,
sekcie 6--7.

## Vetva S — samostatná para S1

| Možnosť | Čo znamená | Súčasný status | Čo by dovolila |
|---|---|---|---|
| S-C: podmienený test | explicitne predpokladať, že S1 má v každom štandardnom móde vopred určený adiabatic/kompenzačný korelačný seed | `NIE_ODVODENÉ`; nesmie sa volať predikcia teórie | matematický conditional residual v 261, oddelený od fyzikálneho verdiktu |
| S-M: mikrofyzikálny seed | odvodiť vznik, decoupling a koreláciu pary z lokálneho zdroja Q18/Q22 | `OPEN / A4 BLOCKER` | fyzikálne interpretovateľný plný P5 seed |

Pre AD je jednoduché slovné „para je adiabaticá“ stále nedostatočné: treba
zapísať jej normalizáciu a all-species constraint. Pri NID a NIV je priame
`delta_s=delta_nu` chybné, ak sa para iba **pridá** k pôvodnému neutrínovému
seedu. Podmienená vetva S-C je prípustná iba ako rozdelenie už existujúceho
spoločného collisionless sektora: neutrínový aj parný vektor môžu byť
rovnaké, ale ich vážený súčet musí presne reprodukovať pôvodný spoločný
vektor a kompenzácia sa musí počítať s `R_fs=R_nu+R_s`. Pre každý z piatich
módov musí S-C uviesť celý vektor a následne prejsť nezávislými residualmi;
S-M musí navyše uviesť jeho mikrofyzikálny pôvod. Presný kontrakt a hranice
sú v `51_P5_3G7_S1_BRANCH_AND_SUPPORT_TRANSFER_CONTRACT_SK.md`.

## Presná postupnosť do 261

1. M1: citovaný, amplitúdovo a gauge jednoznačný štandardný `h,eta` rad.
2. M2--M3: mapovanie do P5 a K4 korekcia bez použitia testovaného constraintu.
3. Vybrať **jednu** z dvoch explicitných S vetiev: S-C (len conditional) alebo S-M (odvodený zdroj Q18/Q22).
4. Až potom napísať 261: dva štarty, päť módov, plný vektor a oddelené `00`, `0i`, trace a traceless rezíduá. S-C výsledok nikdy nezvyšuje fyzikálne skóre K4; môže len potvrdiť alebo vyvrátiť matematickú konzistenciu.

**Aktuálny rozsudok:** P5 zostáva živá a blokovaná vstupmi. Neexistuje dôvod označiť A2-K4 za mŕtvu, ale neexistuje ani oprávnenie spustiť 261 alebo G8.

## Nadväzujúca M3 predregistrácia

M3 má od 2026-07-16 zmrazený módovo rozlíšený kontrakt vrátane exact-A1
backgroundového radu, troch skúšobných Fourierových módov, driver/holdout
rozdelenia a podmienenej S-C pary:
`27_P5_3G7_M3_MODE_RESOLVED_PUISEUX_PREREGISTRATION_SK.md`.
Tento odkaz nemení stav: runner 261 ešte nebežal.
