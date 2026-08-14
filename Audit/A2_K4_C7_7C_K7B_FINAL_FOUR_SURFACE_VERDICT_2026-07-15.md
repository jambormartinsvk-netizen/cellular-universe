# A2-K4 / C7.7c / K7b — konečný štvorpovrchový verdikt

Dátum: 2026-07-15  
Rozsudok K7b: **PASS**  
Rozsudok A2-K4: **ŽIVÁ**  
Jemná hĺbka: **66.5/100, bez zmeny**  
Nasledujúca brána: **K7c — evolučná reprezentácia bez nového stupňa voľnosti**

## 1. Čo bolo overené

K7b overila počiatočné projektované premenné

\[
D=\sum_A\Omega_A\delta_A,
\qquad
M=(2\Omega_\gamma+1.5\Omega_b)U_\gamma+2\Omega_{fs}U_{fs}
  +1.5\delta\Omega_fU_f
\]

proti registrovaným Puiseuxovým koeficientom, rekonštrukcii druhových premenných, Einsteinovým `00`/`0i` identitám a všetkým 13 projektovaným RHS rovniciam. Nevykonala ODE evolúciu.

## 2. Autoritatívny štvorpovrchový výsledok

Skript 176 skončil za 6.313 s s verdiktom `PASS_C7_7C_K7B_FINAL_FOUR_SURFACE_GATE`.

| Mód/povrch | Autoritatívny skript | D activity rel. chyba | Najhorší stav / allowance | Najhorší RHS / allowance | Stav |
|---|---|---:|---:|---:|---|
| NID/deep | 175 | `5.9511e-3` | `9.4022e-6` | `8.5918e-13` | PASS |
| NID/shallow | 175 | `1.0921e-4` | `8.0083e-6` | `6.3485e-12` | PASS |
| NIV/deep | 166 | nevyžadované | `3.2127e-5` | `3.5503e-11` | PASS |
| NIV/shallow | 166 | nevyžadované | `3.8442e-5` | `2.6233e-10` | PASS |

Všetky zobrazené pomery sú hlboko pod jednotkovou acceptance hranicou. Každý podbeh mal vnútorný a vonkajší časový limit.

## 3. Prečo bola potrebná tvrdá high-precision vetva

Pôvodný float64 audit 166 formálne prešiel, ale na NID/deep mala derivácia `D` neaktívny fyzikálny signál prekrytý koeficientovým floorom. Skript 167 ukázal lineárne škálovanie rezídua s amplitúdou, teda floor koeficientov, nie chybu K7a Jacobiánu.

K7b.3a prepočítala mäkký least-squares solve pri 80 dps. Mala menšie maticové rezíduum, ale posunula fyzikálne kotvy, zničila rekonštrukciu a activity bránu. Preto je K7b.3a mŕtva: vyššia presnosť nesmie meniť presne zadané počiatočné podmienky na mäkké kompromisy.

K7b.3b vyňala registrované počiatočné a hierarchické kotvy zo zoznamu voľných neznámych. Opravený solve mal 30 fixovaných a 58 voľných koeficientov, nulovú chybu kotiev, plný redukovaný rank 58 a HP rezíduum `2.09e-16` oproti double rezíduu rádovo `1e-15` až `1e-14`.

## 4. Zachované neúspešné podkoľaje

| Skript/podkoľaj | Stav | Presný dôvod | Dopad na fyziku |
|---|---|---|---|
| 168/169 — K7b.3a | MŔTVA | mäkké LS riadky dovolili posunúť fyzikálne kotvy; D activity a constrainty zlyhali | fyzikálne nepoužiteľná numerická formulácia |
| 170 | technicky MŔTVA | mpmath nepodporilo rez `matrix[:, list]`; `TypeError: unhashable type: list` | žiadny fyzikálny výpočet |
| 171 | čiastočný PASS exportu | opravil rez matice, ale HP register sa neskôr prepísal solve pri `mu=0` | zdroj pre stav bol platný, HP provenance nebola jednoznačná |
| 172 | REVIEW, neautoritatívny | porovnal HP štandardný sektor pri `mu=0` so stavom a frakčným sektorom pri `physical_mu` | nesmie zabiť K4 ani K7b.3b |
| 173 | technicky MŔTVA | wrapper hľadal marker v nesprávnej transformačnej vrstve a skončil pred výpočtom | žiadny fyzikálny výpočet |
| 174/175 | PASS | register sa zachytil iba pri `mu=physical_mu`; pôvodné tolerancie ostali | autoritatívna NID oprava |
| 176 | PASS | zložený NID/NIV deep/shallow audit bez ODE | konečný K7b verdikt |

Žiadny z týchto skriptov sa nemaže. Prahy sa po výsledku neuvoľnili.

## 5. Čo PASS neznamená

K7b nedokazuje:

- stabilnú nenulovú projektovanú ODE trajektóriu;
- zachovanie constraintov pozdĺž trajektórie;
- deep/shallow zhodu koncového stavu;
- krokovú alebo tolerančnú konvergenciu;
- aktivitu všetkých 13 komponentov počas evolúcie;
- plnú fotónovú/neutrínovú Boltzmannovu hierarchiu;
- observačný výsledok pre CMB alebo `S8`.

Preto sa skóre nemení. Až K7c smie definovať evolučný stav a až úplný K7d PASS môže podľa pôvodnej predregistrácie pridať `+0.2` bodu.

## 6. Ďalší krok

Pred spustením ODE sa musí v K7c explicitne zvoliť invertibilná 13-zložková reprezentácia, v ktorej `D,M` nahradia presne dva degenerované druhové smery. Nesmú sa pridať ako 14. a 15. nezávislá premenná. Potom nasleduje krátky segmentovaný deep/shallow evolučný test s constraint ledgerom a pevnými limitmi.
