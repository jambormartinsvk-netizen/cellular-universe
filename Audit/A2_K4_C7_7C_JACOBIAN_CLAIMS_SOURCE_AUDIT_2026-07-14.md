# A2-K4 / C7.7c — zdrojový audit námietok k Jacobianu 151/152

**Dátum:** 2026-07-14  
**Rozsah:** skripty 136, 142, 146, 147, 151 a 152  
**Skóre pred/po:** `66.5/100`  
**Fyzikálny stav A2-K4:** bez zmeny, **ŽIVÁ / C7.7c otvorená**

## Súhrnný rozsudok

Námietka je z väčšej časti správna. Diagnostika 151/152 meria numerickú reprezentáciu v analyticko-obálkových súradniciach, nie škálovo invariantnú fyzikálnu tuhosť. `max|J|`, singulárne hodnoty a odvodený condition proxy sa nesmú interpretovať ako fyzikálne invarianty. Condition proxy zo skriptu 151 sa týmto **formálne sťahuje ako nedôveryhodný**.

Námietka o možnej nelinearite a chýbajúcej funkcii `rhs` sa na tento konkrétny reťazec nevzťahuje: registrovaný RHS je striktne lineárny v 13 stavových premenných, jeho koeficienty závisia iba od `x`, a funkcia `rhs(x_value,y)` je definovaná v skripte 136. Skripty 151 a 152 ju reálne vykonali a skončili verdictom `CAPTURED`, nie `NameError`.

## 1. Obálkový FD krok a lokalita

Použitá škála je

`S_i=max(|y_i,start|,|y_i,series(-18)|,10^-300)`

a FD perturbácia bola `Delta y_i=10^-7 S_i`. Je pravda, že pri komponentoch s veľkým budúcim rastom môže byť táto perturbácia oveľa väčšia než ich počiatočná hodnota.

Všeobecne by to pri nelineárnom alebo vetvenom RHS zneplatnilo lokálnu interpretáciu. Konkrétny BR3C RHS však obsahuje iba lineárne kombinácie stavov:

- backgroundové koeficienty sú funkcie `x`, nie `y`;
- nevyskytuje sa `y_i y_j`, mocnina stavu, `clip`, stavová vetva ani stavový limiter;
- jediná vetva v RHS je časová deadline kontrola nezávislá od hodnoty stavu.

Pre exaktnú aritmetiku je preto centrálna diferencia rovnaká pre ľubovoľný nenulový krok. Zostáva iba floating-point chyba. Správnejšie je tu Jacobian zostaviť priamo z lineárnych koeficientov alebo pôsobením na bázové vektory; FD nie je potrebný.

**Verdikt k bodu 1:** správna všeobecná výhrada, ale nelineárny „nelokálny Jacobian“ v tomto RHS nevzniká. Povinný zostáva step-sweep alebo priamy bázový Jacobian na odhad roundoff chyby.

## 2. Miešanie dynamiky s headroomom obálky

Táto námietka je správna. Pri `y=S w` platí

`J_w=S^-1 J_y S`,

takže `(J_w)_ij=(J_y)_ij S_j/S_i`. Preto:

- `max|J_w|` závisí od `S`;
- singulárne hodnoty a 2-norm condition číslo závisia od `S`;
- `f_i/S_i` nie je invariantná „relatívna rýchlosť“ `f_i/|y_i|`;
- top couplings v 151/152 sú top couplings zvolenej numerickej normy, nie automaticky top fyzikálne interakcie.

Spektrum je pri exaktnej diagonálnej podobnostnej transformácii invariantné. Pozorovaný spektrálny polomer `≈3.4441515426` preto zostáva užitočnou kontrolou transformácie, nie však samostatným dôkazom fyzikálnej stability celej neautonómnej evolúcie.

Veľké `max|J_w|` malo legitímny užší význam: vysvetľovalo, prečo konkrétna obálkovo normalizovaná reprezentácia spôsobuje solveru numerické ťažkosti. Nemalo sa označovať za fyzikálnu tuhosť pôvodnej sústavy.

**Verdikt k bodu 2:** správny; predchádzajúca interpretácia sa týmto obmedzuje na kondíciu numerických súradníc.

## 3. Condition proxy zo skriptu 151

Skript používal vyriešené singulárne hodnoty nad prahom

`sigma > sigma_max × 10^-14`.

Tento prah nebol odvodený z chyby centrálnej diferencie s krokom `10^-7`, z porovnania krokov ani z analytického Jacobianu. Navyše SVD sama závisí od diagonálnej normy `S`.

Preto sa čísla

- `scaled_jacobian_resolved_condition_proxy≈1.06×10^6` pre NID a
- `≈2.48×10^11` pre NIV

nesmú používať v ďalšom fyzikálnom ani numerickom rozsudku. Ostávajú v pôvodnom JSON iba ako archivovaný chybný diagnostický návrh.

**Verdikt k bodu 3:** správny; condition proxy je **STIAHNUTÝ**.

## 4. Odporúčané náhrady

1. Pre tento lineárny RHS vytvoriť fyzikálny Jacobian priamo z koeficientov alebo `J[:,j]=rhs(x,e_j)-rhs(x,0)`.
2. Osobitne reportovať fyzikálny `J_y`, lokálne škálovaný `J_local` a obálkový `J_env`; žiadny z ich SVD údajov nezamieňať za invariant bez uvedenia normy.
3. Ak sa FD napriek linearite použije, porovnať aspoň kroky `10^-4...10^-8` alebo relatívny krok a výsledok proti priamemu Jacobianu.
4. Spektrum porovnať medzi fyzikálnym, lokálnym a obálkovým Jacobianom. Nezhoda nad odhadom roundoff chyby znamená FD artefakt.
5. Condition číslo reportovať iba s deklarovanou normou a cutoffom odvodeným z nameranej numerickej chyby. Pomer vlastných čísel nie je všeobecnou náhradou condition čísla pri nenormálnej matici.

## 5. Dopad na doterajšie rozsudky

- **C7.7c-K4 ostáva mŕtva numerická podkoľaj**, pretože jej skutočné evolučné behy opakovane timeoutovali. Dôvod sa spresňuje na zlyhanie obálkovej numerickej reprezentácie, nie fyzikálnu nestabilitu.
- **C7.7c-K5 ostáva mŕtva**, lebo evolúcia nedokončila prvý segment a maticové vyváženie zmenilo error metriku. Jej rozsudok sa nesmie opierať o stiahnutý condition proxy.
- **C7.7c-K6 a condition mapa 155/156 nie sú dotknuté**: K6 používala fyzikálny stav a mapa 155/156 počítala priamo termové cancellation hranice, nie SVD zo skriptu 151.
- **K7 projektovaná kompenzovaná báza zostáva ďalším krokom**, lebo ju motivuje nezávislý termový audit NID zdroja pod roundoff hranicou.

## 6. Nevyriešená numerická kontrola

Plánovaný päťkrokový FD sweep a priamy bázový Jacobian nebol v tomto kroku vykonaný, pretože pomocná shell vrstva opakovane nevracala ani krátke procesy. Audit vyššie je exaktný zdrojový a algebraický rozsudok. Nové konkrétne FD chybové čísla sa nesmú tvrdiť, kým časovo obmedzený krížový skript reálne neprebehne.
