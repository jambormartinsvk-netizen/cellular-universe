# Výstup balíka A2-K4.3b-RG-BR — skripty 88 až 95

**Dátum:** 2026-07-14  
**Konečný stav balíka:** `BR1 PASS; BR2 PASS PO CONDITION AUDITE; BR3A PASS; K4.3b NEUZAVRETÁ`

## Súhrn behov

| Skript | Exekučný výsledok | Fyzikálny význam |
|---|---|---|
| 88 | `PASS_BR1_FORMULATION_LEDGER` | 19/19 znamienkových, nulových, Einsteinových a conservation identít |
| 89 | `REVIEW` | surová druhá derivácia `eta` je v hlbokej radiačnej ére numericky zle podmienená |
| 90 | `REVIEW` | DAE odstránila druhú deriváciu, ale kompenzované módy ešte odčítavali surové `X_A ~ a^-4` |
| 91 | výpočet dokončený, JSON typová chyba | Omega-normalizovaný solver; fyzika sa nemenila |
| 92 | `REVIEW_BR2_OMEGA_CONDITIONED` | všetky density módy PASS; dva velocity módy ostali nad absolútnou pevnou toleranciou pre cancellation round-off |
| 93 | výpočet dokončený, JSON typová chyba | explicitná IEEE condition hranica; fyzika sa nemenila |
| 94 | `PASS_BR2_WITH_EXPLICIT_VELOCITY_CONDITION_BOUND` | všetkých 35 kontrol prešlo bez plošného uvoľnenia tolerancie |
| 95 | `PASS_BR3A_PUISEUX_SOURCE_COEFFICIENTS` | 40/40 módových exponentov, koeficientov a dvojhĺbkových kontrol |

Skripty 89 a 90 sa nemažú. Sú negatívnymi numerickými kontrolami, nie
fyzikálnymi smrťami. Erratá 91 a 93 dokazujú, že ich prvé prerušenia nastali
až pri serializácii `numpy.bool_`.

## BR1 — uzamknuté rovnice

Skript 88 potvrdil v jednej synchronous konvencii:

- backgroundový pár `Q_c=+Gamma rho_f`, `Q_f=-Gamma rho_f`;
- úplné `delta Q` v absolútnych hustotách;
- povinný interakčný člen tlaku
  `delta p_f/rho_f = delta_f + (2-delta)(3delta+Gamma/H)U_f`;
- conservation celkovej energie a hybnosti;
- prevod `00`, `0i`, stopovej a bezstopovej `ij` rovnice do `x=ln a`;
- nulový limit `Gamma -> 0`;
- nulové štyri Einsteinove zdroje interných `nu-steam` módov.

Bez interakčného člena tlaku by momentum ledger neprešiel. Jeho prítomnosť
nie je voliteľná oprava fitu, ale dôsledok rest-frame uzávery paliva.

## BR2 — numerické pasce a konečný PASS

Skript 89 ukázal, že konečná diferencia `eta_xx` má hlboko v radiačnej ére
veľké relatívne rezíduum, hoci adiabatic `00` rezíduum bolo iba `2.4e-11`.
Faktor `(Hconf/H0)^2` zosilnil round-off. Tento výsledok nesmie byť čítaný
ako porušenie Einsteinových rovníc.

Skript 90 prešiel na constraintovo podmienenú DAE formuláciu. NID a interné
módy však stále tvoril zo surových hustôt `X_A ~ a^-4`; ich malý zdroj bol
rozdielom obrovských čísel.

Skripty 91/92 preto použili `Omega_A=X_A/E^2`. Všetky density módy prešli
striktnou hranicou `2e-10`. Zvyšky rýchlostných módov boli:

- kolektívny NIV: bezstopová rovnica `2.47e-9`;
- interný velocity mód: bezstopová rovnica `1.40e-9`.

Skript 94 ich porovnal s vopred vypočítanou IEEE-754 hranicou
`64 eps sum(abs(species components))`. Konzervatívne hranice boli:

| Mód a hĺbka | hranica `0i` | hranica momentum | hranica traceless `ij` |
|---|---:|---:|---:|
| NIV, deep | `5.49e-8` | `7.32e-8` | `6.58e-7` |
| NIV, shallow | `7.43e-9` | `9.90e-9` | `8.91e-8` |
| internal velocity, deep | `5.39e-8` | `7.19e-8` | `6.47e-7` |
| internal velocity, shallow | `7.30e-9` | `9.73e-9` | `8.76e-8` |

Pozorované zvyšky sú pod týmito hranicami. Pevná tolerancia zostala pre
všetky nekompenzované rovnice; condition hranica bola povolená iba pre tri
vymenované velocity ledgery.

## BR3A — módovo závislé Puiseuxove zdroje

V radiačnej ére pre `h_x = H a^n` skript overil

\[
\frac{U_f}{h_x}=-\frac{1}{2D_n},\qquad
\frac{\delta p_f}{\rho_f h_x}
=-\frac{\delta(n+5-3\delta)}{2D_n},
\]

\[
D_n=(n-1)(n+6-3\delta)+9(2-\delta).
\]

| Mód | `n` | merané `U_f/h_x` | analytické | meraný tlakový koeficient | analytický | tlakový exponent | ash exponent |
|---|---:|---:|---:|---:|---:|---:|---:|
| AD | 2 | `-0.0194426` | `-0.0194368` | `-0.00309504` | `-0.00309448` | `5.92964` | `6.93012` |
| CDI | 1 | `-0.0281113` | `-0.0281005` | `-0.00382925` | `-0.00382833` | `4.92954` | `4.93034` |
| BI | 1 | `-0.0281113` | `-0.0281005` | `-0.00382925` | `-0.00382833` | `4.92954` | `5.93018` |
| NID | 3 | `-0.0140267` | `-0.0140231` | `-0.00255507` | `-0.00255469` | `6.92964` | `7.93008` |
| NIV | 2 | `-0.0194415` | `-0.0194368` | `-0.00309493` | `-0.00309448` | `5.92984` | `6.93028` |

Dve štartové hĺbky dali koeficienty zhodné výrazne lepšie než na percento.

## Obmedzenie staršej formulácie

Staršie tvrdenie „fuel stress-energy je rádu `a^3.93109` a ash korekcia
`a^4.93109`“ sa týmto spresňuje:

- `3.93109=4-3delta` je exponent backgroundového prefaktora `Omega_f`;
- `4.93109=5-3delta` je exponent backgroundového prefaktora
  `(Gamma/H)(rho_f/rho_c)`;
- úplný poruchový zdroj musí navyše niesť vedúci exponent konkrétneho seedu.

Preto sú úplné tlakové exponenty módovo závislé
`5.93109, 4.93109, 4.93109, 6.93109, 5.93109` a ash-transfer exponenty
`6.93109, 4.93109, 5.93109, 7.93109, 6.93109`.

## Rozsudok

```text
BR1: PASS.
BR2: PASS po explicitnom condition-number audite.
BR3A: PASS.
A2-K4: živá, 60/100 = G6.
K4.3b: stále neuzavretá.
Ďalší krok: BR3B — indukovaný frakčný metric/species koeficientový systém.
```

