# A2-K4.3a — audit druhového ledgeru, anisotropného stresu a nulových limitov

**Dátum:** 2026-07-14  
**Rozsah:** prvá podbrána K4.3/G7  
**Stav koľaje A2-K4:** **ŽIVÁ, 60/100**  
**Rozsudok K4.3a:** **PREŠLA IBA FORMULAČNÁ PODBRÁNA**  
**Čo tento rozsudok neznamená:** K4 ešte neprešla úplnou Einsteinovou–Boltzmannovou bránou G7 a nesmie dostať 70/100.

## 1. Audítorská otázka

K4.2 pracovala s baryónmi, popolom, palivom a jednou ideálnou radiačnou tekutinou pri predpoklade nulového anisotropného stresu, teda s `Psi = Phi`. K4.3 musí tento skrátený systém nahradiť fyzikálne úplným lineárnym rozhraním pre fotóny, neutrína a paru. Otázka K4.3a je užšia:

> Dá sa zostaviť konzervatívny a znamienkovo konzistentný ledger druhov, zdrojov a Einsteinových rovníc, ktorý v deklarovaných nulových limitoch reprodukuje K4.2?

K4.3a ešte netestuje rekombináciu, tight coupling, fotónovú polarizáciu, uzáver vysokej multipólovej hierarchie ani fyzikálne prenosové funkcie.

## 2. Pevná konvencia

Používame konformnú Newtonovu gauge

\[
ds^2=a^2\left[-(1+2\Psi)d\eta^2+(1-2\Phi)\delta_{ij}dx^i dx^j\right],
\]

konformný Hubbleov parameter \(\mathcal H=a'/a\), Fourierov mód \(k\) a rýchlostnú divergenciu \(\theta_A\) v rovnakej konvencii ako v K4.2. Znamienka sa nesmú miešať s dokumentmi používajúcimi opačnú definíciu \(\theta\).

## 3. Ledger druhov a interakcií

| Symbol | Druh | Pozadie | Lineárne stupne voľnosti | Nekozmologický zdroj |
|---|---|---|---|---|
| \(c\) | popol / tmavá hmota | \(p_c=0\) | \(\delta_c,\theta_c\) | prijíma energiu a hybnosť iba od \(f\) |
| \(f\) | palivo / dark-energy-like zložka | \(w_f=-1+\delta\) | \(\delta_f,\theta_f\) | odovzdáva energiu a opačnú hybnosť \(c\) |
| \(b\) | baryóny | štandardné | \(\delta_b,\theta_b\) | Thomsonov prenos s fotónmi |
| \(\gamma\) | fotóny | \(w=1/3\) | teplota, rýchlosť, multipóly a polarizácia | Thomsonov rozptyl |
| \(\nu\) | štandardné voľne letiace neutrína | \(w=1/3\) v bezhmotnom limite | \(\delta_\nu,\theta_\nu,\sigma_\nu,F_{\nu\ell}\) | bez kolízií po decouplingu |
| \(s\) | para, vetva S1 | \(w=1/3\) | \(\delta_s,\theta_s,\sigma_s,F_{s\ell}\) | v S1 bez kolízií |

K4 interakcia je obmedzená na tmavý pár. Na pozadí

\[
Q_c=+\Gamma\rho_f,\qquad Q_f=-\Gamma\rho_f,
\]

a kovariantne musí platiť

\[
Q_c^\mu+Q_f^\mu=0.
\]

Rovnaká párová anulácia musí platiť pre perturbovaný energetický zdroj aj pre hybnostný zdroj. Fotóny, neutrína ani para nesmú dostať skrytý K4 zdroj bez založenia novej fyzikálnej koľaje.

### 3.1 Vetvy pary

- **S1 — voľne letiaca para:** prvá testovaná možnosť; zodpovedá doterajšiemu CAMB referenčnému nastaveniu, kde bola \(\Delta N_\mathrm{eff}\) pridaná ako massless free-streaming radiation.
- **S2 — samointeragujúca ideálna para:** samostatná čakajúca koľaj s \(\sigma_s=0\); nie je numericky totožná so S1.
- **S3 — sieťovo odvodený kolízny kernel:** čaká na mikroskopické odvodenie.

Úmrtie S1 samo osebe nezabíja S2 ani S3. S1 je konzistentná parametrizácia, ale zatiaľ nie je odvodená z bunkovej mikrofyziky.

## 4. Einsteinove constrainty po povolení anisotropného stresu

Pri \(\delta T^0{}_0=-\delta\rho\) sa používajú

\[
k^2\Phi+3\mathcal H(\Phi'+\mathcal H\Psi)
=-4\pi G a^2\delta\rho,
\]

\[
k^2(\Phi'+\mathcal H\Psi)
=4\pi G a^2\sum_A(\rho_A+p_A)\theta_A,
\]

\[
k^2(\Phi-\Psi)
=12\pi G a^2\sum_A(\rho_A+p_A)\sigma_A.
\]

Kontrolná stopa pre dynamickú rovnicu je

\[
\Phi''+\mathcal H(\Psi'+2\Phi')
 +(2\mathcal H'+\mathcal H^2)\Psi
 +\frac{k^2}{3}(\Phi-\Psi)=4\pi G a^2\delta p.
\]

Z toho vyplývajú dve povinné opravy oproti skrátenému rozhraniu K4.2:

1. pri neutrínach alebo voľne letiacej pare všeobecne neplatí \(\Psi=\Phi\);
2. evolúcia z `0i` má štruktúru \(\Phi_x=-\Psi+M\), nie automaticky \(-\Phi+M\).

V limite celkového anisotropného stresu \(\sum(\rho+p)\sigma=0\) dostávame \(\Psi=\Phi\), a teda presne staré rozhranie \(\Phi_x=-\Phi+M\). To je deklarovaný nulový limit K4.3a.

## 5. Spodné momenty štandardných zložiek

Pri kladnej Thomsonovej miere \(\dot\kappa=a n_e\sigma_T\) sú spodné momenty

\[
\delta_\gamma'=-\frac43\theta_\gamma+4\Phi',
\]

\[
\theta_\gamma'=k^2\left(\frac14\delta_\gamma-\sigma_\gamma\right)
+k^2\Psi+\dot\kappa(\theta_b-\theta_\gamma),
\]

\[
\delta_b'=-\theta_b+3\Phi',
\]

\[
\theta_b'=-\mathcal H\theta_b+c_b^2k^2\delta_b+k^2\Psi
+\frac{4\rho_\gamma}{3\rho_b}\dot\kappa(\theta_\gamma-\theta_b).
\]

Pre bezhmotné voľne letiace neutrína

\[
\delta_\nu'=-\frac43\theta_\nu+4\Phi',
\qquad
\theta_\nu'=k^2\left(\frac14\delta_\nu-\sigma_\nu\right)+k^2\Psi,
\]

\[
\sigma_\nu'=\frac4{15}\theta_\nu-\frac3{10}kF_{\nu3},
\]

\[
F_{\nu\ell}'=\frac{k}{2\ell+1}
\left[\ell F_{\nu,\ell-1}-(\ell+1)F_{\nu,\ell+1}\right],\qquad \ell\ge3.
\]

Vetva pary S1 má rovnaký bezkolízny tvar s indexom \(s\). Fotónové vyššie momenty vrátane polarizácie a všetkých kolíznych koeficientov sa v K4.3b musia prevziať z overeného Einsteinovho–Boltzmannovho backendu alebo proti nemu presne otestovať. K4.3a ich zámerne nedopisuje odhadom.

## 6. Dve algebraické konzervačné brány

### 6.1 Thomsonova hybnosť

Fotónový kolízny člen vážený entalpiou je

\[
\frac43\rho_\gamma\dot\kappa(\theta_b-\theta_\gamma),
\]

baryónový člen je

\[
\rho_b\frac{4\rho_\gamma}{3\rho_b}\dot\kappa
(\theta_\gamma-\theta_b).
\]

Ich súčet je identicky nula. Thomsonov rozptyl teda redistribuuje hybnosť, ale nevytvára ju.

### 6.2 Agregovaný radiačný limit

Pre konštantné podiely \(R_i=\rho_i/\rho_r\), \(i\in\{\gamma,\nu,s\}\), \(\sum_iR_i=1\), definujeme

\[
\delta_r=\sum_iR_i\delta_i,\qquad
\theta_r=\sum_iR_i\theta_i,\qquad
\sigma_r=\sum_iR_i\sigma_i.
\]

Bez Thomsonovej výmeny a pri spoločnej metrike potom

\[
\delta_r'=-\frac43\theta_r+4\Phi',
\]

\[
\theta_r'=k^2\left(\frac14\delta_r-\sigma_r\right)+k^2\Psi.
\]

Ak navyše \(\sigma_r=0\), \(\Psi=\Phi\) a jednotlivé radiačné zložky zdieľajú rovnaký mód, systém reprodukuje ideálnu radiačnú tekutinu K4.2. Mimo tohto deklarovaného limitu nie je jedna perfektná radiačná tekutina exaktnou náhradou Boltzmannových hierarchií.

## 7. Automatizované overenie

Skript `scripts/72_script_A2_K4_3a_species_ledger_and_anisotropic_stress_audit.py` s vnútorným limitom kontroluje:

1. nulový súčet pozadových a perturbovaných zdrojov K4;
2. nulový súčet párovej tmavej hybnosti;
3. nulový-anisotropný limit \(\Psi\to\Phi\);
4. návrat `0i` rozhrania ku K4.2;
5. agregáciu radiačnej kontinuity a Eulerovej rovnice;
6. presné vyrušenie Thomsonovej hybnosti;
7. redukciu spodných momentov S1 na perfektnú radiáciu po explicitnom vynulovaní hierarchie.

Strojový výsledok je uložený v `scripts/OUTPUT_A2_K4_3A_72.md`.

## 8. Rozsudok a skóre

**K4.3a prešla formuláciou a algebraickými nulovými limitmi.** Nenašla sa porucha lokálnej celkovej konzervácie ani rozpor medzi anisotropným Einsteinovým constraintom a limitom K4.2.

To však nie je observačný ani úplný dynamický výsledok. Koľaj **A2-K4 ostáva ŽIVÁ na 60/100**. Na 70/100 smie postúpiť až po spoločnom splnení:

- K4.3b: úplná fotónová a neutrínová/parná hierarchia, tight coupling, rekombinácia a regulárne superhorizontové počiatočné podmienky;
- K4.3c: implementačný nulový test voči nezávislému overenému backendu;
- K4.3d: spojený K4 beh s constraintmi a fyzikálnymi prenosovými funkciami.

Najbližší krok je **K4.3b**, nie A3.

## 9. Primárne teoretické kotvy

- Ma & Bertschinger, *Cosmological Perturbation Theory in the Synchronous and Conformal Newtonian Gauges*, arXiv:astro-ph/9506072.
- Blas, Lesgourgues & Tram, *The Cosmic Linear Anisotropy Solving System (CLASS) I*, arXiv:1104.2932.
- Lewis, Challinor & Lasenby, *Efficient Computation of CMB Anisotropies in Closed FRW Models*, arXiv:astro-ph/9911177 (CAMB/line-of-sight metodika).

