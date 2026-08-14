# Audit A2-K4.3b-RG BR3B-2e — NID/NIV hierarchia

Dátum: 2026-07-14  
Rozsudok K4: **ŽIVÁ**  
Maximálna hĺbka: **60/100 = G6**  
Aktuálne: **G7/BR3B-2e prešla, BR3B-2f otvorená**

## Dopad na K4

Tento krok citeľne znížil riziko, že NID alebo NIV skryjú skorú ne-regulárnu vetvu:

- najskoršie relatívne rýchlostné módy sú regulárne a metrické nulové módy;
- prvé hustotno-gradientovo-šmykové sektory majú jedinečné konečné riešenia;
- presná kompenzácia nie je zničená background dressingom;
- dva Einsteinove/Bianchiho integrability testy sú presne nula;
- numerická odozva je dobre podmienená a rezíduá sú na úrovni `10^-15`.

K4 tým prešla ďalšou podstatnou časťou G7, ale kanonické skóre sa nesmie interpolovať medzi bránami. Kým chýba celý ordered fuel + `l>=3` systém a plný backend, ostáva 60/100.

## Najskoršie relatívne módy

Pre NID je prvý nový exponent `3.93109`, pre NIV `2.93109`. V oboch prípadoch background slope núti fotónovú a neutrínovú rýchlosť opačne. Vážený súčet základného módu, zdroja aj indukovanej odozvy je presne nulový. Hustota, metrika a šmyk v tejto najskoršej vrstve ostávajú nulové.

Rozsudok: **PASS**, nie iba numerická malá hodnota.

## Audit mapovania NIV šmyku

Oficiálny CLASS master uvádza v NIV inicializácii `shear_ur = k tau/(4Rnu+15)`, zatiaľ čo susedné NIV rýchlostné výrazy sú označené ako malé rozdiely oproti CAMB. Pri priamom vložení tohto izolovaného šmyku s `eta=-Rnu k tau/(4Rnu+5)` nevychádza vedúca traceless Einsteinova rovnica.

Skript 105 mal získať symbolické CAMB premenné, ale bez Fortran kompilátora skončil `ERROR_UNCLOSED`. Nebol použitý ako fyzikálny dôkaz.

Skript 106 použil iba predkompilované CAMB 1.6.6 premenné a odvodil šmyk z massless-neutrino Eulerovej rovnice:

`sigma = delta_nu/4 - (3/4) d q_nu/d(k tau)`.

Výsledok `0.150326` sedí s `1/(4Rnu+5)=0.150321` a vylučuje `1/(4Rnu+15)=0.060051` pri predregistrovanej absolútnej tolerancii `5e-3`. Vedúce traceless relatívne rezíduum je `8.73e-5`.

Rozsudok: v BR3B rekurencii sa používa **samo-konzistentný koeficient `1/(4Rnu+5)`**. Nejde o úpravu teórie ani fit; ide o opravu mapovania po nezávislom backendovom audite.

## Obmedzenie starších tvrdení

1. PASS skriptu 84 platí pre jeho deklarovaný vektor `delta_g, delta_b, delta_c, delta_nu, q_g, q_nu, eta_s`. Šmyk v ňom nebol, preto tento PASS nikdy nemohol potvrdiť NIV `shear_ur`.
2. Skript 104 správne uzavrel najskorší rýchlostný sektor. Jeho informatívna položka NIV base shear z CLASS sa nesmie použiť v ďalšej rekurencii; nahrádza ju skript 106.
3. Skript 107 nepreukázal fyzikálny fail. Bol externe ukončený po 15 s, keď exaktný `linsolve` blokoval kontrolu limitu.
4. Skript 108 nemení fyziku 107. Exact ponecháva základné rovnosti a Bianchiho identity; iba riešenie 9×7 sústavy vykonáva SVD s auditom hodnosti, podmienenosti a rezídua.

## Výsledok prvých šmykových sektorov

NID `p+2=5.93109`:

- `rank=7`, condition `49.73`;
- Bianchi `0,0`;
- škálované absolútne rezíduum `2.48e-15`.

NIV `p+1=4.93109`:

- `rank=7`, condition `43.91`;
- Bianchi `0,0`;
- škálované absolútne rezíduum `5.56e-15`.

Rozsudok: **PASS BR3B-2e-2**. K4 nie je mŕtva a nebola potrebná žiadna voľná koľaj ani fitový koeficient.

## Zostávajúce brány do G7

1. BR3B-2f: zostaviť spoločný fuel sektor s už známym skorším riešením v správnom poradí.
2. Pridať prvý `l=3` feedback a regulárnu rekurziu vyšších multipólov v neskorších mocninách.
3. BR3C: overiť všetky štyri Einsteinove rezíduá pri dvoch hĺbkach a nezávislej zmene kroku/presnosti.
4. BR4: plný fotónový/neutrínový backend, nulový limit a referenčný cross-check.

## Primárne referencie

- CLASS master `perturbations.c`: https://raw.githubusercontent.com/lesgourg/class_public/master/source/perturbations.c
- CAMB: https://github.com/cmbant/CAMB

