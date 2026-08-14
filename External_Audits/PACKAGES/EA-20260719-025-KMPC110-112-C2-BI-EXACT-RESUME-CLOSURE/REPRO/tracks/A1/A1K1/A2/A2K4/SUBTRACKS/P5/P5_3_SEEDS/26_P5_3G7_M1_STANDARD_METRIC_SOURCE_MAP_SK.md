# A2-K4/P5.3g7-M1 — štandardný synchronný metrický seed: zdroj a mapovanie

**Dátum:** 2026-07-16  
**Verdikt:** `PASS_MAPY_STANDARD_NULL_LIMIT`; nie je to plný K4 seed ani
prechod P5.3g7.  
**Úloha:** opraviť staršie, užšie tvrdenie „chýba `h`“: chýbal v návratovom
vektore scriptu 84, nie v primárnej literatúre. Zostáva chýbať K4-backreacted
Puiseuxov rad pre `h,eta`.

## Zdroj a konvencia

Bucher--Moodley--Turok (BMT), rovnice (22)--(26), dáva pravidelné
synchronné rady (h,eta) pre AD, BI, CDI, NID a NIV
([PDF, str. 9--12](https://arxiv.org/pdf/astro-ph/9904231)). BMT výslovne
hovorí, že CDM-comoving voľba môže na začiatku nastaviť (	heta_c=0), ale
toto zachovanie na všetkých časoch predpokladá gravitačne izolované CDM.
To nie je predpoklad P5; P5 musí po štarte vyvíjať (U_c).

V tomto dokumente platí presne konvencia scriptu 84:

\[
y=k\tau,\qquad \omega_b=f_b\,\omega_m,\quad
\omega_c=f_c\,\omega_m,\quad \omega_m=\Omega_m H_0/\sqrt{\Omega_{r0}},
\]

kde (R_\nu=f_\nu), (R_\gamma=f_\gamma). BMT používa pri
BI/CDI normalizáciu, pre ktorú
\(Omega^{\rm BMT}_{i,0}\tau_{\rm BMT}=\omega_i\tau/4\).
Túto štvorku vynúti priame porovnanie ich (delta_i,eta) so scriptom 84;
nie je to nový parameter. NIV je navyše v BMT normovaný
(	heta_\nu=k), zatiaľ čo script 84 má (q_\nu=1), teda
(	heta_\nu=3k/4). Preto NIV dostáva faktor (3/4).

## Výsledný seed v konvencii scriptu 84

| mód | (h(\tau)), vedúci potrebný rad | (h'(\tau)) | kontrola mapy |
|---|---|---|---|
| AD | \(\frac12y^2\) | \(k^2\tau\) | (\eta=1-\frac{5+4R_\nu}{12(15+4R_\nu)}y^2+\dots\), presne script 84 |
| BI | \(x_b-\frac38x_b^2\), (x_b=\omega_b\tau\) | \(\omega_b(1-\frac34x_b)\) | (\eta=-x_b/6+x_b^2/16\), presne script 84 |
| CDI | \(x_c-\frac38x_c^2\), (x_c=\omega_c\tau\) | \(\omega_c(1-\frac34x_c)\) | (\eta=-x_c/6+x_c^2/16\), presne script 84 |
| NID | \(\frac{\omega_bR_\nu}{40R_\gamma}k^2\tau^3\) | \(\frac{3\omega_bR_\nu}{40R_\gamma}k^2\tau^2\) | (\eta=-\frac{R_\nu}{6(15+4R_\nu)}y^2+\dots\), presne script 84 |
| NIV | \(\frac{9\omega_bR_\nu}{32R_\gamma}k\tau^2\) | \(\frac{9\omega_bR_\nu}{16R_\gamma}k\tau\) | po BMT \(3/4\) amplitúdovej konverzii (\eta=-R_\nu y/(5+4R_\nu)+\dots\), presne script 84 |

Slovo „presne“ v poslednom stĺpci znamená algebraickú zhodu už uložených
(eta), hustôt a rýchlostí scriptu 84 po uvedenej konverzii. Neznamená to,
že sa BMT dá numericky použiť ako K4 solver bez ďalšieho odvodenia.

## Čo tento PASS umožňuje a čo nie

**Umožňuje:** M1 má nezávislú štandardnú amplitúdu `h,h'`; 261 ju nesmie
určovať z vlastného `00` či `0i` residualu. M2 môže legálne použiť
`U_c(tau_start)=0` ako počiatočnú gauge voľbu, ak bezprostredne potom drží
`U_c` v stave a vyhodnocuje jeho P5 RHS.

**Neumožňuje:**

- vložiť tieto rady ako hotový interagujúci K4 seed;
- vynechať Puiseuxov metrický príspevok paliva rádu
  (a^{4-3\delta}) a následný popolový príspevok;
- vyhlásiť `00`, `0i`, trace alebo traceless constraint za prejdený;
- zvoliť či normalizovať S1 paru.

Preto M1 je uzavretá mapa štandardného nulového limitu, M2 má historický
test-field dôkaz a M3/M4 aj vetva S zostávajú otvorené. Ďalší povolený krok
nie je nový runner: treba odvodiť K4-backreacted metriku M3 na dvoch
štartovacích plochách alebo samostatne uzavrieť S-M cez Q18/Q22. Až potom sa
smie pripraviť 261 podľa `25_P5_3G7_INPUT_RAILS_SK.md`.

## M3 — predregistrovaný derivčný kontrakt

M3 má jednu úlohu: pre každú z piatich štandardných báz rozšíriť vyššie rady
o najnižší K4/Puiseuxov príspevok a určiť `h, eta` z **trace a traceless
dynamických Einsteinových rovníc spolu so species RHS**. `00` a `0i` musia
ostať bokom ako nezávislé rezíduá; nesmú sa použiť na výber metrických
koeficientov.

| Položka | Predregistrácia |
|---|---|
| vstup | M1 štandardný rad, exact-A1 (E(a),X_i(a)), P5 species RHS a pevne označená vetva S-C alebo S-M |
| neznáme | všetky koeficienty `h,eta,delta_A,U_A,sigma_A,...` na prvom K4 rade, vrátane dynamického `U_c` |
| očakávaný PASS | konečný rad na dvoch plochách; štandardný vedúci limit M1; nulové trace/traceless rezíduá; potom nezávislé malé `00`,`0i` rezíduá |
| fyzikálny STOP/REVIEW | nenulový neodstrániteľný zdroj, singularita alebo porušenie regulárnosti pri fyzikálnych A1 parametroch |
| zakázané | pevné `K_MPC`, voľný fit koeficient, vynútené `U_c=0` po štarte, použitie `00`/`0i` na definovanie testovaného seedu |

Budúci Python beh, ak vznikne, má byť iba 261, s vnútorným limitom najviac 5 s
a vonkajším limitom najviac 10 s. Pred behom musí samostatný Markdown doplniť
konkrétny rad, tolerancie, očakávané absolútne aj relatívne rezíduá a dôvod,
ak sa tieto hranice oproti tejto registrácii zmenia.

## Korekcia staršieho statusu

`Audit/A2_K4_P5_G7_FULL_SEED_INPUT_CLOSURE_AUDIT_2026-07-16.md` bol správny
v tom, že script 84 samotný `h,h'` neexportuje. Tento dokument ho zužuje:
nejde o absenciu štandardného zdroja, ale o absenciu **K4-spätne viazaného**
metrického seedu a S1 korelácie. Starý audit sa nemaže; táto korekcia je jeho
sledovateľné spresnenie.
