# A2-K4.3b — audit hierarchií, regulárnych módov a rekombinačného rozhrania

**Dátum:** 2026-07-14  
**Koľaj:** A1-K1 / A2-K4 / K4.3-S1  
**Rozsudok K4.3b:** **`NEUZAVRETÁ — POKRAČOVAŤ K4.3b-RG`**  
**Stav A2-K4:** **`ŽIVÁ — 60/100 = G6`**  
**Nový dôvod smrti:** **nevydáva sa**

## 1. Výsledok v jednej vete

Úplný rovnicový ledger teplotných, polarizačných, neutrínových a S1 parných
hierarchií je konzistentný s CAMB 1.6.6 a nulové rekombinačné rozhranie
prešlo, ale rozšírený systém má **sedem**, nie tri štandardne regulárne
analytické skalárne módy. Dva velocity-isocurvature módy sú regulárne v
gauge-invariantnom zmysle, hoci Newtonove potenciály a premenná `U` použitá
v K4.1 divergujú ako `1/(k tau)`. K4.3b preto nemožno uzavrieť pred
odvodením a reziduálnym testom siedmich konečno-štartových radov v regulárnej
gauge.

## 2. Čo sa testovalo

1. presný photon-temperature a polarization hierarchy ledger;
2. massless-neutrino hierarchy;
3. S1 free-streaming steam hierarchy;
4. Thomsonov collision block a tight-coupling parameter;
5. nulový CAMB rekombinačný interface;
6. rozklad `nu + steam` na kolektívny a interný mód;
7. dimenzia štandardnej analytickej primordiálnej bázy;
8. raný limit K4 interakcie `lambda/E`.

Netestovala sa ešte integrácia modifikovaného Einsteinovho–Boltzmannovho
backendu. Tá patrí K4.3c.

## 3. Konvencie a úplný hierarchy ledger

Metrika ostáva

\[
ds^2=a^2[-(1+2\Psi)d\eta^2+(1-2\Phi)dx^idx_i].
\]

Používame brightness multipóly Ma–Bertschinger
\(F_{\gamma\ell}\), kde

\[
F_{\gamma0}=\delta_\gamma,\qquad
F_{\gamma1}=\frac{4\theta_\gamma}{3k},\qquad
F_{\gamma2}=2\sigma_\gamma,
\]

a polarizačné multipóly \(G_{\gamma\ell}\). Kladná opacity je
\(\dot\kappa=a n_e\sigma_T\).

### 3.1 Fotónové spodné momenty

\[
\delta_\gamma'=-\frac43\theta_\gamma+4\Phi',
\]

\[
\theta_\gamma'=k^2\left(\frac14\delta_\gamma-\sigma_\gamma\right)
+k^2\Psi+\dot\kappa(\theta_b-\theta_\gamma),
\]

\[
F_{\gamma2}'=\frac8{15}\theta_\gamma-\frac35kF_{\gamma3}
-\frac9{10}\dot\kappa F_{\gamma2}
+\frac1{10}\dot\kappa(G_{\gamma0}+G_{\gamma2}).
\]

Pre \(\ell\ge3\)

\[
F_{\gamma\ell}'=\frac{k}{2\ell+1}
[\ell F_{\gamma,\ell-1}-(\ell+1)F_{\gamma,\ell+1}]
-\dot\kappa F_{\gamma\ell}.
\]

### 3.2 Polarizácia

Definujeme

\[
\Pi_\gamma=F_{\gamma2}+G_{\gamma0}+G_{\gamma2}.
\]

Potom pre všetky \(\ell\ge0\)

\[
G_{\gamma\ell}'=\frac{k}{2\ell+1}
[\ell G_{\gamma,\ell-1}-(\ell+1)G_{\gamma,\ell+1}]
+\dot\kappa\left[-G_{\gamma\ell}
+\frac12\Pi_\gamma\left(\delta_{\ell0}+\frac15\delta_{\ell2}\right)
\right].
\]

Pre skalárny mód sa nepoužíva nezávislý `B` seed. Budúci backend môže
použiť ekvivalentnú optimálnu `E` hierarchiu CAMB; mapovanie symbolov musí
byť explicitné a nesmie miešať normalizáciu `F/G` s `J/E`.

### 3.3 Neutrína a para S1

Pre \(i\in\{\nu,s\}\)

\[
\delta_i'=-\frac43\theta_i+4\Phi',
\qquad
\theta_i'=k^2\left(\frac14\delta_i-\sigma_i\right)+k^2\Psi,
\]

\[
\sigma_i'=\frac4{15}\theta_i-\frac3{10}kF_{i3},
\]

\[
F_{i\ell}'=\frac{k}{2\ell+1}
[\ell F_{i,\ell-1}-(\ell+1)F_{i,\ell+1}],\qquad \ell\ge3.
\]

S1 teda nie je perfektná tekutina. S2 a S3 zostávajú odlišné koľaje.

## 4. Tight coupling a uzáver

Collision-only blok pre
\([F_{\gamma2},G_{\gamma0},G_{\gamma2}]\) je

\[
\dot\kappa
\begin{pmatrix}
-9/10&1/10&1/10\\
1/2&-1/2&1/2\\
1/10&1/10&-9/10
\end{pmatrix}.
\]

Jeho determinant je \(-3/10\), takže má plnú hodnosť a v nultom
tight-coupling ráde je jediným collision-equilibrium riešením nulový
kvadrupól a nulová polarizácia. Nenulové hodnoty vznikajú perturbatívne v

\[
\epsilon_{\rm TCA}=\max(k\tau_c,\mathcal H\tau_c),\qquad
\tau_c=1/\dot\kappa.
\]

Hodnota `epsilon=0.1` použitá skriptom 74 je iba predregistrovaný
diagnostický bod rozhrania, nie tvrdenie o internom CAMB switchi.

Pre priamu testovaciu hierarchiu K4.3c sa predregistruje
`lmax=8,12,16`; ak fyzický backend používa line-of-sight alebo vlastné
aproximácie, porovná sa default s vyššími accuracy nastaveniami. Konvergencia
sa nesmie vybrať až podľa želaného transferu.

## 5. Rekombinačný nulový interface

Skript 74 použil lokálny CAMB 1.6.6 s parametrami nulovej referencie
`H0=66.37`, `Omega_m0=0.3517`, `Neff=3.0995` a konštantným
`w=-0.97703` surrogate.

| Diagnostika | Výsledok |
|---|---:|
| peak visibility | `z=1088.1713` |
| \(\int g\,d\eta\) | `1.00001921` |
| \(x_e\) rozsah | `0.000209917 – 1.16483642` |
| `epsilon_TCA`, `z=10^6`, `k=0.2/Mpc` | `4.79614e-6` |
| prvý zostupný bod `epsilon>=0.1` | `z=2184.9904` |

Všetkých osem interface kontrol prešlo. Tento beh však používa surrogate,
nie presnú A1-K1 expanziu. Rekombinácia závisí aj od expanznej rýchlosti,
preto sa táto história nesmie mechanicky vložiť do K4 bez backendu, ktorý
počíta atómovú kinetiku na presnom K4 backgrounde. Štandardná atómová
fyzika sa nemení; mení sa iba vstupný background.

## 6. Radiačné podiely S1

Z registrovaného `Delta Neff=0.0535` vychádza

| Zložka | Podiel na celkovej radiácii |
|---|---:|
| fotóny \(R_\gamma\) | `0.5868901247` |
| štandardné neutrína \(R_\nu\) | `0.4059792483` |
| para S1 \(R_s\) | `0.0071306270` |
| všetko free-streaming \(R_{fs}\) | `0.4131098753` |

Súčet je presne jedna v použitej racionálnej konvencii.

## 7. Prečo je módov sedem

Neutrína a S1 para majú identický lineárny bezkolízny operátor. Preto sa
exaktne rozložia na

\[
F_{fs,\ell}=\frac{R_\nu F_{\nu\ell}+R_sF_{s\ell}}{R_{fs}},
\qquad
D_\ell=F_{\nu\ell}-F_{s\ell}.
\]

Kolektívna hierarchia gravituje. Interná hierarchia sa vyvíja samostatne.
Ak \(F_{s\ell}=-(R_\nu/R_s)F_{\nu\ell}\), jej celkový príspevok k
energeticko-hybnostnému tenzoru je presne nula pre každý multipól.

V štandardnej analytickej skalárnej triede sú potom módy:

1. adiabatický;
2. CDM-density isocurvature;
3. baryónový density isocurvature;
4. kolektívny free-streaming density isocurvature;
5. interný `nu-steam` density isocurvature;
6. kolektívny free-streaming velocity isocurvature;
7. interný `nu-steam` velocity isocurvature.

Skript 73 zostavil ich nezávislé vedúce seed descriptors a dostal hodnosť
sedem. Kompenzované density a momentum súčty vyšli presne nula.

### 7.1 Rozsah slova „úplná“

Tento počet predpokladá štandardnú analytickú/local-isotropy podmienku:
density seed generuje \(F_\ell=O[(k\tau)^\ell]\) a velocity seed
\(F_0=O(k\tau)\), \(F_1=O(1)\),
\(F_{\ell\ge2}=O[(k\tau)^{\ell-1}]\). Ľubovoľné konštantné primordiálne
vyššie multipóly sa do tejto triedy nezaraďujú.

Ak má bunková mikrofyzika vytvárať anisotropnú primordiálnu distribúciu
pary s nezávislými vyššími multipólmi, musí vzniknúť nová S3-like kinetická
koľaj s vlastným generátorom počiatočných dát. Nemožno ju potichu pridať k
S1.

## 8. Kritické gauge zistenie

Pre velocity seed je \(F_1=O(1)\) a

\[
\theta=\frac34kF_1,
\qquad
U=\frac{\mathcal H\theta}{k^2}
=\frac{3F_1}{4k\tau}=O[(k\tau)^{-1}].
\]

Premenná `U` K4.1 a Newtonove zero-shear potenciály teda divergujú, hoci
frame-invariantná Weylova veličina a mód ako celok sú regulárne. Toto je
známa vlastnosť neutrínového velocity-isocurvature módu, nie automatická
fyzikálna nestabilita.

Z toho vyplýva:

- trojica K4.1 bola úplná iba pre jej deklarovaný perfect-radiation systém;
- po rozšírení druhov ju nemožno používať ako úplnú bázu G7;
- velocity módy sa musia odvodiť v regulárnej gauge alebo frame-invariantnej
  báze a až potom mapovať na konečný Newtonov štart;
- divergence jednej gauge premennej sama osebe nie je kill kritérium.

## 9. Raný limit K4

V radiačnej ére \(E\sim\sqrt{\Omega_r}a^{-2}\), preto

\[
\frac{\lambda}{E}\propto a^2.
\]

Skript 73 dostal

```text
lambda/E(x=-20) = 6.52081e-17
lambda/E(x=-22) = 1.19433e-18
pomer = exp(4) = 54.5981500331
```

K4 interakcia teda nemení vedúci radiačný počet módov. Stále však vytvára
podvedúce konečno-štartové korekcie; ich zanedbanie sa musí otestovať
rezíduom, nie iba označiť za malé.

## 10. Rozsudok po podbránach

| Časť K4.3b | Stav | Dôvod |
|---|---|---|
| B1 hierarchy ledger | **PREŠLA** | rovnice a CAMB symbolic inventory sú konzistentné |
| B2 tight-coupling/closure interface | **PREŠLA FORMULÁCIOU** | collision block a predregistrované konvergenčné osi sú uzavreté |
| B3 recombination interface | **PREŠLA IBA NULOVÁ REFERENCIA** | presný K4 background ešte nie je v backende |
| B4 úplná regulárna báza | **NEUZAVRETÁ** | počet 7 je odvodený, ale chýbajú všetky finite-start koeficienty v regulárnej gauge |
| B5 automatizované plné constrainty | **ČAKÁ** | potrebuje B4 a modifikovateľnú implementáciu |

Preto je celkový rozsudok

```text
K4.3b NEUZAVRETÁ — ŽIADNA FYZIKÁLNA SMRŤ.
A2-K4 OSTÁVA ŽIVÁ NA 60/100.
```

## 11. Bezprostredný krok K4.3b-RG

1. zvoliť regulárnu evolučnú gauge, ktorá nepredpokladá geodetické CDM po
   zapnutí K4 sily; vhodný kandidát je total-matter alebo všeobecná
   synchronous gauge bez trvalého `theta_c=0`;
2. odvodiť sedem radov aspoň po rády potrebné pre `00`, `0i`, slip a `ij`;
3. zahrnúť podvedúce `lambda/E=O(a^2)` členy K4;
4. mapovať každý rad na konečný Newtonov štart a overiť gauge-invariantné
   entropie a relatívne rýchlosti;
5. vytvoriť časovo ohraničený reziduálny skript;
6. až po PASS označiť K4.3b za uzavretú a prejsť na K4.3c.

## 12. Reprodukčné artefakty

- `scripts/73_script_A2_K4_3b_hierarchy_and_regular_mode_taxonomy_audit.py`;
- `scripts/74_script_A2_K4_3b_CAMB_recombination_interface_reference.py`;
- `scripts/OUTPUT_A2_K4_3B_73_74.md`.

## 13. Primárne zdroje

- Ma & Bertschinger, arXiv:astro-ph/9506072;
- Bucher, Moodley & Turok, arXiv:astro-ph/9904231;
- Ghosh, Kumar & Tsai, arXiv:2107.09076;
- CAMB Notes, `https://cosmologist.info/notes/CAMB.pdf`;
- lokálne zmrazený CAMB 1.6.6 `camb.symbolic` a binárny rekombinačný backend.

