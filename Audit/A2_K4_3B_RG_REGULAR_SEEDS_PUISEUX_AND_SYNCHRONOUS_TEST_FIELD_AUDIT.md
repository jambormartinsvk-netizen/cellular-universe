# A2-K4.3b-RG — audit regulárnych seedov, Puiseuxových rádov a synchronous test-field odpovede

**Dátum:** 2026-07-14  
**Verdikt:** `ČIASTOČNE PREŠLA; NEUZAVRETÁ; ŽIADNA FYZIKÁLNA SMRŤ`  
**Kanonické skóre A2-K4:** `60/100 = G6`

## 1. Auditná otázka

K4.3b-RG mala zistiť, či sa sedem módov rozšíreného systému dá inicializovať
bez gauge artefaktu a či K4 na presnom A1-K1 backgrounde zachová regulárny
raný limit. Táto etapa ešte nemala právo vyhlásiť G7, pretože plné
back-reacted Einsteinove rovnice a fotónová/neutrínová evolúcia neboli
implementované.

## 2. Päť kolektívnych módov

Predkompilovaný CAMB 1.6.6 poskytuje päť štandardných počiatočných
podmienok. Prvý auditný beh odhalil, že pred interným iniciačným časom vracia
presné nulové placeholdery. Nuly nie sú fyzikálne počiatočné dáta.

Opravený skript 79 vybral prvý spoločný aktívny riadok `k tau=0.0016`.
Invariantný descriptor matrix mal hodnosť päť a najmenšiu singulárnu hodnotu
`0.703951`. Módy preto nie sú numericky takmer lineárne závislé.

Skript 84 potom prepísal analytické synchronous koeficienty z verejnej
implementácie CLASS, ktorá používa Bucher–Moodley–Turok bázu. Proti CAMB
prešli všetky módy s relatívnym L2 rezíduom najviac `1.52e-5`.

Tým sa odstránila potreba získavať CDI/BI koeficienty nestabilným odčítaním
odvodených Newtonovských potenciálov hlboko mimo horizontu.

## 3. Dva interné `nu-steam` módy

Pre S1 majú neutrína a free-streaming para rovnaký bezkolízny operátor.
Pre každý multipól preto platí

\[
R_\nu F_{\nu\ell}+R_sF_{s\ell}=0,
\qquad
F_{s\ell}=-\frac{R_\nu}{R_s}F_{\nu\ell}.
\]

Skript 80 zostavil density aj velocity rad do `lmax=12`. Koeficientové
rezíduá `c_{n+1}(n+1)-A c_n` boli presne nulové a maximálny vážený zdroj
všetkých multipólov bol `4.93e-32`. Species-resolved seed matrix má hodnosť
sedem.

Tento PASS je podmienený S1 definíciou: K4 prenáša energiu medzi palivom a
popolom, nie priamo do už decouplovanej parnej hierarchie. Ak sa táto
mikrofyzika zmení, musí vzniknúť nová kinetická koľaj; tento dôkaz sa nesmie
potichu preniesť.

## 4. Prečo obyčajný Taylorov rad nestačí

Presný A1-K1 background dal

\[
\frac{\lambda}{E}\sim a^2,
\quad
\frac{\rho_f}{\rho_c}\sim a^{3-3\delta}=a^{2.93109},
\]

\[
\frac{\rho_f}{\rho_r}\sim a^{4-3\delta}=a^{3.93109},
\quad
\frac{\lambda}{E}\frac{\rho_f}{\rho_c}
\sim a^{5-3\delta}=a^{4.93109}.
\]

Namerané exponenty súhlasili s týmito hodnotami na `3e-6` alebo lepšie.
Plný rad preto musí mať celočíselnú štandardnú vetvu a frakčné K4 vetvy.
Zaokrúhlenie `3.93109` na štvrtý rád by bolo tichou zmenou rovníc.

## 5. Negatívny Newtonovský test skriptu 85

Vedúce synchronous NID/NIV série sú regulárne, ale Newtonovské potenciály
vznikajú po zrušení viacerých vedúcich density a momentum členov. Skript 85
nemal všetky vyššie koeficienty potrebné pre transformáciu. Vyrobil preto
falošné `delta_c≈2.85e5` a zlyhal v nulovom limite.

Toto nie je fyzikálna nestabilita. Je to prísnejšie ohraničenie staršej
formulácie „mapovať pri konečnom čase“: konečný čas sám nestačí; zdrojový rad
musí obsahovať všetky rády, ktoré prežijú cancellation v cieľovej gauge.

Skript 85 a jeho výpočty zostávajú archivované s erratom.

## 6. General-synchronous oprava

Skript 86 použil synchronous gauge s nulovým lapse. Na počiatočnom povrchu
sa zhoduje so štandardným CDM frame, ale po zapnutí K4 sa `theta_c` normálne
integruje; nie je umelo fixované na nulu.

Test-field rovnice v premenných `U_A=Hconf theta_A/k^2` boli

\[
\delta_{c,x}=-\frac{k^2}{\mathcal H^2}U_c-\frac{h_x}{2}
+\frac{\lambda}{E}r(\delta_f-\delta_c),
\]

\[
U_{c,x}=-(1-h_c)U_c+\frac{\lambda}{E}r\beta(U_f-U_c),
\]

\[
\delta_{f,x}=-3(2-\delta)\delta_f
-\delta\frac{k^2}{\mathcal H^2}U_f
-9(2\delta-\delta^2)U_f-\frac{\delta h_x}{2}
-3\frac{\lambda}{E}(2-\delta)U_f,
\]

\[
U_{f,x}=(h_c+2)U_f+\frac{\delta_f}{\delta}
+\frac{\lambda/E}{\delta}(2U_f-U_d).
\]

Tu `h_c=d ln(Hconf)/dx`, `r=rho_f/rho_c` a
`U_d=(1-beta)U_c+beta U_f`.

Všetkých päť módov prešlo dve štartové hĺbky, nulový limit a konečnosť.
Najhoršie absolútne `lambda=0` rezíduum `delta_c` bolo `2.48e-11`; štartové
rozdiely boli najviac `2.22e-12`.

## 7. Čo tento PASS nedokazuje

Metrika `h_x` bola držaná na štandardnej analytickej hodnote. Test teda
nezahŕňal spätný zdroj paliva, ktorý vstupuje prvýkrát v ráde
`a^(4-3delta)=a^3.93109`, ani následnú K4 korekciu popola rádu `a^4.93109`.

Neoveril sa spoločný reziduálny systém:

- `00` Hamiltonov constraint;
- `0i` momentum constraint;
- bezstopový slip constraint;
- stopová `ij` rovnica.

Preto sa K4.3b ani G7 neuzatvárajú a skóre sa nemení.

## 8. Rozsudok podbrán

| Podčasť | Stav |
|---|---|
| päť kolektívnych regulárnych seedov | **PASS** |
| dva interné `nu-steam` módy | **PASS pod S1 no-direct-coupling podmienkou** |
| presný Puiseuxov register backgroundu | **PASS** |
| general-synchronous voľba gauge | **PASS pre test-field** |
| K4 dark-sector test-field odpoveď | **PASS** |
| full back-reacted Puiseux koeficienty | **CHÝBAJÚ** |
| spoločné štyri Einsteinove rezíduá | **CHÝBAJÚ** |

Celkový rozsudok:

```text
A2-K4.3b-RG je čiastočne úspešná, ale neuzavretá.
A2-K4 ostáva živá na 60/100 = G6.
Nevznikol nový dôvod smrti.
```

## 9. Bezprostredný ďalší krok

Vytvoriť `K4.3b-RG-BR`: back-reacted general-synchronous Puiseux solver,
ktorý pridá fuel stress-energy v ráde `a^3.93109`, ash correction v ráde
`a^4.93109` a pre všetkých sedem módov naraz overí `00`, `0i`, slip a `ij`
na dvoch štartových hĺbkach.

## 10. Primárne zdroje a reprodukcia

- [Bucher, Moodley & Turok — Characterising the Primordial Cosmic Perturbations](https://arxiv.org/abs/astro-ph/0007360)
- [Ma & Bertschinger — Cosmological Perturbation Theory](https://arxiv.org/abs/astro-ph/9506072)
- [CLASS `perturbations.c`](https://raw.githubusercontent.com/lesgourg/class_public/master/source/perturbations.c)
- [CAMB transfer-variable conventions](https://camb.readthedocs.io/en/latest/transfer_variables.html)
- skripty 77–86 a ich erratá v `scripts`;
- `scripts/OUTPUT_A2_K4_3B_RG_77_86.md`.

