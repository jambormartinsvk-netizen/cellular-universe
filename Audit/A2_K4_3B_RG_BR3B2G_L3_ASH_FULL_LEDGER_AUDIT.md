# A2-K4.3b-RG BR3B-2g — audit `l=3` hierarchie a prvého gravitačného popola

Dátum: 2026-07-14  
Rozsudok BR3B-2g: **PASS**  
Rozsudok A2-K4: **ŽIVÁ**  
Kanonická hĺbka: **60/100 = G6**  
G7: **NEUZAVRETÁ**

## Rozsah

BR3B-2g nadviazala na úplný mixed matter/fuel reťazec skriptu 124 a pridala
v jednom koeficientovom systéme:

- prvý species-local feedback tretieho multipólu voľne prúdiacej zložky;
- kontrolný štvrtý multipól, ktorého fyzikálny vstup musí byť až za touto
  bránou;
- prvú transferovú korekciu fuel backgroundu a fuel perturbácií;
- prvú vytvorenú ash zložku backgroundu;
- transferovú korekciu `delta_c` a jej prvý vstup do Einsteinových rovníc.

Výpočet je prvého rádu v skorom fuel koeficiente `Phi`. Nepribudol nový fit.

## Hierarchia a konvencie

Použité regulárne premenné sú

`L3 = (k/Hconf) F3`,  
`L4 = (k/Hconf)^2 F4`.

Z plochej massless Boltzmannovej hierarchie vyplývajú rovnice

`L3_x + q L3 - (6/7)s^2 sigma + (4/7)L4 = 0`,

`L4_x + 2q L4 - (4/9)s^2 L3 + (5/9)L5 = 0`.

Shear rovnica obsahuje `+(3/5)L3`. Jej rýchlostný zdroj používa rýchlosť
tej istej free-streaming zložky. Konvencia bola overená proti oficiálnemu
[CLASS `perturbations.c`](https://raw.githubusercontent.com/lesgourg/class_public/master/source/perturbations.c).

## Presné poradie sektorov

Nech `p=4-3 delta=3.93109`.

| Mód | Common fuel | Prvý `L3` feedback | Ash `delta_c` | Prvý ash/CDM gravity | Prvý `L4` feedback |
|---|---:|---:|---:|---:|---:|
| NID | `p+3=6.93109` | `p+4=7.93109` | `p+4=7.93109` | `p+5=8.93109` | `p+6=9.93109` |
| NIV | `p+2=5.93109` | `p+3=6.93109` | `p+3=6.93109` | `p+4=7.93109` | `p+5=8.93109` |

Skript 128 overil toto poradie aj transformáciu hierarchie v **16/16**
exaktných kontrolách.

## Transferový background

V radiation limite je `g=Gamma/H=G z^2`. Na jednotku `Phi` sú prvé
backgroundové korekcie jednoznačné:

- fuel depletion pri `p+2`: `-G/2`;
- vytvorený popol pri `p+2`: `G/(p+1)`;
- `g rho_f/rho_c` má mocninu `p+1`.

CDM rýchlosť `U_c` sa v tomto prvom ráde neobjaví. Jej interakčný zdroj
obsahuje `(g rho_f/rho_c) beta`; oba faktory sú rádu `Phi`, takže zdroj je
`O(Phi^2)` a leží mimo tejto brány.

## Výsledok skriptu 127

| Kontrola | NID | NIV | Brána |
|---|---:|---:|---|
| Fyzikálna matica | `88 x 66` | `88 x 66` | informačné |
| Hodnosť | `66/66` | `66/66` | PASS |
| Číslo podmienenosti | `255.13` | `324.22` | konečné |
| Škálované rezíduum | `2.33e-15` | `2.87e-15` | `<1e-11` |
| Maximum fyzikálneho riadku | `1.14e-15` | `4.40e-15` | `<1e-10` |
| Štandardný systém | `88/88` | `88/88` | PASS |
| Všetky brány | `40/40` spolu | `40/40` spolu | PASS |

Lambda-zero common-fuel koeficienty reprodukujú skript 124 s maximálnou
chybou `6.09e-16` pre NID a `4.70e-16` pre NIV.

## Nové fyzikálne koeficienty

Hodnoty sú na jednotku `Phi` pri auditovanom `k=0.05 Mpc^-1`.

| Mód | Prvý shear príspevok `(3/5)L3` | Ash korekcia `delta_c` | Ash/CDM density-stress príspevok |
|---|---:|---:|---:|
| NID | `-4.122862e-3` | `+5.363866e-12` | `-4.491322e-13` |
| NIV | `-2.699254e-2` | `+6.919397e-11` | `-3.847021e-12` |

Popol je teda v tomto skorom sektore fyzikálne konzistentný, ale numericky
veľmi slabý. Dominantnú neskorú odozvu tvorí `l=3`/fuel reťazec, nie ash
gravity. To nie je dôvod smrti; je to obmedzenie možného účinku popola.

## Stabilita odrezania

Skript 127 prešiel `40/40` kontrol pri `standard-order=5` aj `6`.

| Veličina | Order 5 | Order 6 | Absolútna zmena |
|---|---:|---:|---:|
| NID `(3/5)L3` | `-0.004122862130030472` | `-0.004122862130030628` | `1.56e-16` |
| NIV `(3/5)L3` | `-0.026992535943698475` | `-0.026992535943698583` | `1.08e-16` |
| NID ash `delta_c` | `5.363903e-12` | `5.363866e-12` | `3.73e-17` |
| NIV ash `delta_c` | `6.919409e-11` | `6.919397e-11` | `1.21e-16` |

## Prečo skript 126 ostáva REVIEW

Skript 126 pridal správne rovnice, ale neuzamkol fyzikálnu regularitu vyšších
multipólov. Matematická sústava preto pripustila dva homogénne módy `L3/L4`,
ktoré po spätnej transformácii znamenajú nenulový skorý `F3/F4` bez
gradientového generovania.

Dôsledky:

- štandardná hodnosť bola iba `86/88`;
- nulový smer zasahoval skoré koeficienty (`lower_null` až `0.85`);
- common-fuel regresia sa posunula až o `3.24e-4`;
- skript skončil `30/40`, teda `REVIEW_UNCLOSED`, nie fyzikálnou smrťou.

Skript 127 pridal nulové podmienky pred prvým gradientovo dovoleným rádom.
Potom sa hodnosť obnovila na `88/88` a všetky regresie prešli. Skript 126 sa
nemaže; dokumentuje presne, prečo je regularitná brána povinná.

## Rozsudok a ďalší krok

BR3B-2g je v auditovanom prvom ráde **uzavretá PASS**. K4 ostáva živá, ale
kanonické skóre sa nemení: interná podbrána nepridáva čiastočné body G7.

Nasleduje **BR3C**:

- inicializácia úplnej evolúcie z dvoch skorých hĺbok;
- všetky štyri Einsteinove rezíduá, absolútne aj škálované;
- zmena kroku, tolerancie a hĺbky Boltzmannovej hierarchie;
- zhoda neskorého riešenia bez opätovného fitovania.

