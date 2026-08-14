# A2-K7.1a-K3.1-K2.2 — problém kúpeľa, šumu a podkoľaje

**Dátum:** 2026-07-13  
**Východisko:** K2.1 prežila iba rozmerovú backgroundovú existenciu  
**Akceptované skóre K7:** `30/100`

## Problém

Pozitívna Onsagerova matica nestačí. Ak má byť disipácia fyzikálna, musí
existovať konkrétny stav prostredia, z ktorého sa odvodia retarded kernel,
noise kernel, transportné koeficienty a ich rozsah lokálnosti. Stress-energy
tohto prostredia sa zároveň nesmie stratiť z A1 účtovníctva.

## Rozdelenie podkoľají

| Podkoľaj | V čom je iná | Hlavná výhoda | Hlavná stena | Stav | Max. hĺbka |
|---|---|---|---|---|---:|
| K3.1-K2.2-K1 | lokálny termálny bath s približným KMS a white noise | priamo realizuje lokálnu Onsagerovu formuláciu | bath nesie energiu/tlak; treba `tau_bath H << 1` | `AKTÍVNA` | `5/100` |
| K3.1-K2.2-K2 | vákuový kvantový bath pri `T=0` s farebným spektrálnym kernelom | nemusí zaviesť reálnu termálnu populáciu | white-noise limit spravidla neplatí; memory a renormalizácia | `ČAKÁ` | `5/100` |
| K3.1-K2.2-K3 | netermálny produkovaný bath s farebným šumom | môže vzniknúť priamo pri delení buniek | stav treba dynamicky evolvovať; detailná rovnováha/KMS chýba | `ČAKÁ` | `5/100` |

Tieto podkoľaje sa nesmú zlúčiť. Termálny white noise, vákuové kvantové
fluktuácie a netermálny farebný šum majú odlišnú fluctuation-dissipation
väzbu a odlišný stress-energy budget.

## Poradie

Najprv sa testuje K1, pretože K3.1-K2 použila lokálnu pozitívnu noise
covariance a práve K1 má najväčšiu šancu tento predpoklad legitimizovať.
Ak K1 zomrie, jej dokumenty a skripty zostanú zachované a pokračuje K2;
K3 sa otvorí až po presnom verdikte K2.

## Akceptačná brána K1

K1 prejde iba ak súčasne:

1. je definovaný bath stav a jeho teplota bez fitovania na `S_8`;
2. retarded a noise kernel spĺňajú pozitivitu a lokálnu KMS/FDT väzbu;
3. je dokázaná separácia časových škál `tau_bath H << 1` v celom rozsahu;
4. `rho_bath,p_bath` sú zahrnuté v A1 ledgeri alebo je explicitne dokázaná
   ich už započítaná/renormalizovaná forma;
5. z kernelu sa odvodia `ell,zeta,alpha`, nie iba ich kladnosť;
6. nevznikne dvojité započítanie pary, mediátora alebo popola;
7. limit vypnutia vráti K7.0.

Ak zlyhá bath budget alebo Markovovský limit, K1 dostane kód `M-014d`.
To nebude automaticky zabíjať K2 ani K3, pretože tie lokálny termálny bath
nepredpokladajú.

