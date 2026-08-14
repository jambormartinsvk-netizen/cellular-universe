# A2-K4.3b-RG BR3B-2f — štandardné vstupy a audit zmiešaných mocnín

Dátum: 2026-07-14  
Rozsudok K4: **ŽIVÁ**  
Kanonická hĺbka: **60/100 = G6**  
G7: **NEUZAVRETÁ**

## Výsledok

Štandardné NID/NIV koeficienty potrebné pri spoločnom fuel sektore boli
získané stabilnou Frobeniovou rekurenciou a v požadovanej hĺbke sú jedinečné.
Pri následnej kontrole poradia sa však preukázalo, že doterajší zoznam
frakčných sektorov nezahŕňal všetky zmiešané mocniny vznikajúce súčasným
pôsobením palivového backgroundu a nenulovej ranej hmoty.

K4 preto **nie je mŕtva**, ale BR3B-2f sa ešte nesmie uzavrieť.

## Prečo nebolo možné použiť priamu CAMB regresiu

Skript 110 reprodukoval analytické AD/CDI/BI pomery, ale NID/NIV koeficienty
ležia až po odčítaní niekoľkých nižších mocnín. Dve skoré časové okná potom
dali nestabilné pomery a pre NID/NIV aj opačné znamienka. Výsledok je
`REVIEW_UNCLOSED`, nie fyzikálny fail.

Skript 111 izoloval baryónovú časť centrálnou diferenciou pri nezmenenom
`Omega_m`. Dva diferenciálne kroky sa zhodli, ale dve časové okná nie. Tým sa
potvrdilo, že problémom je extrakcia vysokého rádu z `float64`, nie porušenie
Einsteinových rovníc.

## Frobeniova náhrada

Skript 112 použil symbolické rady, ale jeho jedna blokujúca operácia
prekročila vonkajší limit 35 s. Stav je
`EXTERNAL_TIMEOUT_UNCLOSED`; skript bol zachovaný.

Skript 113 nahradil symbolické rady konečnou koeficientovou algebrou. Presne
reprodukoval kontrolné koeficienty CLASS/CAMB:

- NID `delta_gamma`, `delta_nu`, `U_gamma`, `U_nu`, `sigma_nu`, `eta` a
  `delta_c` s relatívnymi chybami približne `10^-13` až `10^-15`;
- NIV samo-konzistentné `sigma_nu=1/(4Rnu+5)` a
  `eta=-Rnu/(4Rnu+5)` na rovnakej úrovni;
- škálované rezíduá boli pod `1.4e-15`.

Jeho celkový REVIEW mal dve príliš prísne brány: požadoval plnú hodnosť aj pre
najvyšší odrezaný koeficient a požadoval `k`-nezávislosť pomerov, hoci rovnaká
mocnina mierky môže miešať gradientové a matter členy.

Skript 114 je neexecutovaný technický duplikát vytvorený pri zlyhaní Windows
`apply_patch` aktualizácie. Ostáva zachovaný a nepoužíva sa ako dôkaz.

Skript 115 urobil správny audit nulového smeru:

- matica má `rank=59/60`, ale jediný nulový smer leží v odrezaných
  koeficientoch `eta5` a `sigma5`;
- podmienenosť vyriešeného podpriestoru je `17.42–17.46`;
- maximálna projekcia nulového smeru do cieľových
  `h_x, eta_x, U_gamma, U_nu` je `8.32e-16`;
- všetkých 20 registrovaných kontrol prešlo.

Rozsudok: **PASS štandardných NID/NIV vstupov v požadovanej hĺbke**.

## Nová medzera v poradí mocnín

Nech `p=4-3 delta=3.93109`. Skripty 104 a 108 riešili čistý radiačný
podreťazec. Nenulová raná hmota však mení

`Hconf_x/Hconf = -1 + epsilon_m/2 + ...`

a photon–baryon Eulerova rovnica obsahuje navyše

`R_b = (3 f_b/(4 R_gamma)) epsilon_m`.

Po vložení nenulových relatívnych rýchlostí zo skriptu 104 je vážený Eulerov
zdroj v nasledujúcej mocnine presne nenulový. Skript 116 preto dokázal povinné
medzisektory:

| Mód | Najskorší čistý radiačný sektor | Povinný matter-dressed sektor | Starý šmykový sektor | Common fuel |
|---|---:|---:|---:|---:|
| NID | `p = 3.93109` | `p+1 = 4.93109` | `p+2 = 5.93109` | `p+3 = 6.93109` |
| NIV | `p-1 = 2.93109` | `p = 3.93109` | `p+1 = 4.93109` | `p+2 = 5.93109` |

Tieto medzisektory nemožno preskočiť ani vtedy, keď predchádzajúca rýchlosť
bola radiačne kompenzovaná. Baryónové zaťaženie kompenzáciu v nasledujúcej
mocnine poruší.

## Obmedzenie starších tvrdení

1. PASS skriptu 104 ostáva platný pre najskorší **čistý radiačný** relatívny
   sektor.
2. PASS skriptu 108 ostáva platný pre dve konkrétne šmykové sústavy, ktoré
   skutočne riešil.
3. Staršie tvrdenie, že 104 a 108 tvoria úplné vzostupné poradie až po common
   fuel, je auditom 116 obmedzené: pri `epsilon_m != 0` chýbajú NID `p+1` a
   NIV `p` a ich ďalšie rekurzívne vstupy.
4. Ash transfer nie je zdrojom tejto medzery. Jeho korekcia `delta_c` vzniká
   pri `p+1+n_c`, ale do Einsteinových stress členov vstupuje až o ďalšiu
   matter mocninu neskôr. Vo všetkých piatich módoch gravituje až po common
   fuel sektore.

## Ďalšia brána

BR3B-2f-5 musí vyriešiť celý zmiešaný reťazec:

- NID `p+1`, `p+2`, `p+3`;
- NIV `p`, `p+1`, `p+2`;
- pri každom kroku carried baryónové/CDM koeficienty, gradient, šmyk a všetkých
  deväť species/Einstein riadkov;
- nulový matter limit musí reprodukovať skripty 104 a 108;
- až posledná vrstva smie dostať common fuel stress zo skriptov 95/100/115.

## Primárne zdroje konvencií

- [CLASS `perturbations.c`](https://raw.githubusercontent.com/lesgourg/class_public/master/source/perturbations.c)
- [CAMB](https://github.com/cmbant/CAMB)

