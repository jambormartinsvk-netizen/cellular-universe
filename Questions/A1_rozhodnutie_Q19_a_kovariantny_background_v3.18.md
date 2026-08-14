# A1: rozhodnutie Q19 a kovariantný background pre v3.18

**Dátum:** 2026-07-13  
**Stav:** čaká na jedno rozhodnutie autora  
**Krok:** A1 — určiť príjemcu (Q^\mu) a pripraviť opravu A16  
**Nadväzuje na:** `doplnenie_otazok_a_krokov_po_fyzikalnom_audite_2026-07-13.md`, otázka Q19

## 1. Auditný záver

Pre verziu 3.18 odporúčam zvoliť:

\[
Q_c^\mu=Q u_c^\mu,\qquad Q=\Gamma\rho_f,\qquad
\Gamma\equiv\lambda H_0>0,
\]

pričom neskorý prenos (Q^\mu) vytvára **iba studenú tmavú hmotu (CDM)**. Baryóny, žiarenie a ostatné štandardnomodelové zložky tento bunkový prenos neprijímajú.

Baryónová asymetria musí mať osobitný skorý mechanizmus aktívny pred BBN. Tvrdenie o „vzácnych zlyhaniach“, z ktorých vzniká obyčajná hmota, preto vo v3.18 môže zostať iba ako otvorená hypotéza baryogenézy, nie ako interpretácia neskorého člena (Q=\lambda H_0\rho_f).

Toto je najmenšia zmena kompatibilná s doterajším jadrom v3.17. Nevyžaduje prechod na v4.0, pretože odstraňuje nejednoznačnosť spoločnej (Omega_m) a zhoduje sa s explicitným čítaním skriptu 08.

## 2. Prečo je táto voľba odporúčaná

| Evidencia v projekte | Dôsledok |
|---|---|
| `scripts/08_script_Q7_sound_horizon_H0.py` definuje `om_c = om_m - om_b` a tvorí iba časť CDM | Numerický test Q7 už používa voľbu „(Q\to\mathrm{CDM})“ |
| Skript 09 evolvuje iba spoločnú (Omega_m) | Na backgrounde nevie rozlíšiť baryóny od CDM; nie je to dôkaz, že (Q) vytvára baryóny |
| Úvod a popularizačný text odlišujú „popol“ ako tmavú hmotu od vzácneho vzniku obyčajnej hmoty | Dva produkty vyžadujú dva fyzikálne kanály, nie jeden nerozlíšený (Q) |
| Baryónová hustota ovplyvňuje BBN a výšky akustických píkov CMB | Neskorá tvorba baryónov by vyžadovala nový parameter, mikrofyziku a samostatný dátový test |
| Geodetický prenos paralelný s (u_c^\mu) je štandardne skúmaná trieda interakcie tmavého sektora | Dá sa formulovať bez dodatočnej sily na CDM v jeho pokojovej sústave, ale poruchy stále treba odvodiť v A2 |

Planck meria baryónovú a CDM hustotu osobitne, približne (Omega_bh^2=0.0224) a (Omega_ch^2=0.120), čo potvrdzuje, že ich nemožno v presnom CMB výpočte nahradiť jedinou nerozlíšenou tekutinou: [Planck 2018, kozmologické parametre](https://arxiv.org/abs/1807.06209).

Kovariantné interakcie môžu mať rovnaký background, ale rozdielne poruchy a pozorovateľné spektrá podľa voľby prenosového štvorvektora: [De-Santiago, Wands a Wang, 2012](https://arxiv.org/abs/1209.0563). Geodetický scenár s interakciou vákuovej zložky a CDM bol analyzovaný s úplnou lineárnou perturbačnou teóriou napríklad v [Martinelli et al., 2019](https://arxiv.org/abs/1902.10694). Tieto práce sú oporou pre matematickú triedu efektívneho modelu, nie dôkazom bunkovej mikrofyziky.

## 3. Navrhovaná kovariantná sústava

### 3.1 Zložky

Použijú sa štyri efektívne tenzory energie a hybnosti:

\[
T_{\rm tot}^{\mu\nu}
=T_f^{\mu\nu}+T_c^{\mu\nu}+T_b^{\mu\nu}+T_r^{\mu\nu}.
\]

- (f): palivová zložka s (p_f=w_f\rho_f), (w_f=-1+\delta),
- (c): CDM/popol s (p_c=0),
- (b): baryóny s (p_b\simeq0) na úrovni backgroundu,
- (r): fotóny a ostatné relativistické zložky s (p_r=\rho_r/3).

Pre každú ideálnu tekutinu platí

\[
T_i^{\mu\nu}=(\rho_i+p_i)u_i^\mu u_i^\nu+p_i g^{\mu\nu}
\]

pri konvencii metriky ((-+++)). Na presne homogénnom FRW backgrounde majú všetky zložky spoločnú komohybovú štvorrýchlosť; pri poruchách sa ich rýchlosti všeobecne líšia.

### 3.2 Bunkový prenos

Navrhované rovnice po ukončení skorého baryogenetického mechanizmu sú

\[
\nabla_\mu T_f^{\mu\nu}=-Q^\nu,
\]

\[
\nabla_\mu T_c^{\mu\nu}=+Q^\nu,
\]

\[
\nabla_\mu T_b^{\mu\nu}=C_b^\nu,
\qquad
\nabla_\mu T_r^{\mu\nu}=C_r^\nu,
\]

\[
Q^\nu=\Gamma\rho_f u_c^\nu,
\qquad
\Gamma=\lambda H_0,
\qquad
C_b^\nu+C_r^\nu=0.
\]

Členy (C_b^\nu,C_r^\nu) označujú iba štandardné baryónovo-fotónové kolízne členy. Nie sú novou bunkovou interakciou. Na homogénnom backgrounde používanom vo V1 sa ich energetická časť zanedbá a dostaneme obvyklé škálovanie (ho_b\propto a^{-3}), (ho_r\propto a^{-4}). V budúcom Boltzmannovom výpočte sa štandardné kolízne členy prevezmú z CLASS/CAMB.

Súčet štyroch rovníc dáva

\[
\nabla_\mu T_{\rm tot}^{\mu\nu}
=-Q^\nu+Q^\nu+C_b^\nu+C_r^\nu=0.
\]

Celkový tenzor energie a hybnosti je teda zachovaný identicky. Toto uzatvára backgroundovú Bianchiho kontrolu, nie mikroskopické odvodenie (Q^\nu).

### 3.3 FRW limita

Pre (x=\ln a), čiarku (d/dx), (H=\dot a/a) a (Q=\lambda H_0\rho_f) dostaneme

\[
\rho_f'=-3\delta\rho_f-\lambda\frac{H_0}{H}\rho_f,
\]

\[
\rho_c'=-3\rho_c+\lambda\frac{H_0}{H}\rho_f,
\]

\[
\rho_b'=-3\rho_b,
\qquad
\rho_r'=-4\rho_r.
\]

Po sčítaní:

\[
\rho_{\rm tot}'
=-3\delta\rho_f-3\rho_c-3\rho_b-4\rho_r.
\]

Keďže

\[
p_{\rm tot}=(-1+\delta)\rho_f+\frac13\rho_r,
\]

platí presne

\[
\rho_{\rm tot}'=-3(\rho_{\rm tot}+p_{\rm tot}).
\]

Prenosové členy sa z celkovej rovnice vyrušia so správnym znamienkom. Energia paliva sa nestráca; rovnaký člen vstupuje do CDM.

### 3.4 Bezrozmerné premenné pre kód

Aby sa nezamieňala okamžitá hustotná frakcia s hustotou normalizovanou dnešnou kritickou hustotou, odporúčam v kóde používať

\[
X_i(x)\equiv\frac{\rho_i(x)}{\rho_{\mathrm{crit},0}},
\qquad E(x)=\frac{H(x)}{H_0}.
\]

Pre plochý model potom

\[
E^2=X_f+X_c+X_b+X_r
\]

a

\[
X_f'=-3\delta X_f-\lambda\frac{X_f}{E},
\]

\[
X_c'=-3X_c+\lambda\frac{X_f}{E},
\]

\[
X_b'=-3X_b,
\qquad X_r'=-4X_r.
\]

Okamžitá hustotná frakcia je (Omega_i(x)=X_i(x)/E^2(x)). Súčasné skripty označujú symbolom `Om` často premennú typu (X_i); v3.18 má túto konvenciu výslovne uviesť alebo premenné premenovať.

## 4. Vzťah k existujúcemu skriptu 09

Definujme spoločnú hmotovú premennú

\[
X_m\equiv X_b+X_c.
\]

Potom

\[
X_m'=-3X_m+\lambda\frac{X_f}{E}.
\]

To je presne backgroundová rovnica, ktorú používa skript 09. Jeho doterajšie backgroundové riešenie sa preto voľbou (Q\to\mathrm{CDM}) algebraicky nemení, ak `Om` znamená (X_b+X_c).

Rozdelenie je však povinné pre:

- baryónové zaťaženie zvukovej rýchlosti,
- výšky akustických píkov CMB,
- baryónovo-fotónové oscilácie,
- odlišné počiatočné podmienky a rast (delta_b,delta_c),
- dnešný baryónový podiel.

Skript 09 teda možno ponechať iba ako backgroundový test. Nemôže po A1 predstavovať presný výpočet rastu ani CMB.

## 5. Hranica medzi A1 a A2

Voľba

\[
Q^\mu=Q u_c^\mu
\]

znamená, že CDM neprijíma prenos hybnosti vo vlastnej pokojovej sústave. Z toho možno vyvodiť, že v Eulerovej rovnici CDM nevzniká dodatočná sila z kolmého prenosu hybnosti.

**Nemožno z toho vyvodiť**, že celé lineárne rovnice rastu zostávajú štandardné. Kontinuitná rovnica hustotnej poruchy CDM všeobecne obsahuje interakčné členy a treba určiť minimálne:

- lokálnu poruchu (\delta Q),
- poruchy a zvukovú rýchlosť palivovej zložky,
- gauge a gauge-invariantné kombinácie,
- počiatočné podmienky,
- stabilitu superhorizontových a gradientových módov.

Tieto položky patria do A2. Opravená A16 vo v3.18 smie tvrdiť iba uzavretie backgroundu a nulový kolmý prenos hybnosti do CDM, nie štandardný rast V3.

## 6. Prečo neodporúčam (Q\to b+c) vo v3.18

Ak by sa neskorý prenos delil medzi baryóny a CDM, bolo by potrebné zaviesť aspoň vetviaci podiel (f_b):

\[
Q_b^\mu=f_b Q^\mu,
\qquad
Q_c^\mu=(1-f_b)Q^\mu.
\]

Teória zatiaľ (f_b) neodvodzuje. Takáto vetva by navyše potrebovala:

1. mechanizmus tvorby baryónového čísla, náboja a hmotnostného spektra,
2. zachovanie elektrickej neutrality,
3. súlad s BBN a CMB baryónovou hustotou,
4. test spektrálnych a tepelných dôsledkov neskoro vytvoreného plynu,
5. nový plný likelihood a nové poruchové rovnice.

Pre v3.18 by to nebola oprava nejednoznačnosti, ale nový fyzikálny model. Podľa prijatej verziovacej brány by takáto zmena smerovala skôr do v4.0.

## 7. Jediné potrebné rozhodnutie autora

Potvrdzuje autor pre v3.18 nasledujúcu vetu?

> Bunkový prenos (Q^\mu=\lambda H_0\rho_f u_c^\mu) po skončení skorého baryogenetického obdobia vytvára iba CDM/popol. Baryónový tenzor neprijíma tento prenos; vznik baryónovej asymetrie je samostatná otvorená úloha ranej kozmológie.

Odporúčaná stručná odpoveď: **„Áno, Q vytvára iba CDM.“**

Ak autor odpovie áno, Q19 sa uzavrie a možno bezpečne:

1. prepísať A16 v slovenskej aj anglickej verzii,
2. opraviť tvrdenie o poruchách v A16.4,
3. označiť `Om` v skripte 09 ako súčet baryónov a CDM,
4. upraviť popularizačný text tak, aby neskorý (Q) nezamieňal s baryogenézou,
5. označiť A1 ako dokončené a prejsť na A2.
