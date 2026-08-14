# P5.3a — výsledok auditu pôvodu seedov

**Výstup:** `scripts/results/k_mpc_005/RUN_KMPC_005_P5_3A_SEED_PROVENANCE_AUDIT.json`  
**Čas / limit:** 0.031 s / 5 s  
**Verdikt auditu:** `PASS_P5_3A_PROVENANCE_GAP_MAPPED`  
**Fyzikálny stav:** `P5.3_SEED_REGULARITY_UNCLOSED_STANDARD_GAMMA0_EXTENSION_IDENTIFIED`

## Čo bolo zistené

- skript 84 výslovne deklaruje regular seed iba v limite `Gamma=0`;
- BR2 89 aj 90 importujú tento štandardný seed a začínajú nulovým stavovým
  vektorom;
- pre štandardné módy explicitne nenastavujú `delta_f`, `U_c` ani `U_f`;
- testové pole 86 robí rovnaké nuly, ale samo sa označuje za fixed-metric.

## Rozsudok

Nuly nových dark-sector premenných v starom BR2 štarte sú zatiaľ neodvodené
rozšírenie štandardného seedu. Nie sú dokázanou gauge voľbou ani dôkazom,
že regulárny exact-A1 seed ich musí mať nulové. To nie je smrť A2-K4, ale
záväzný blocker P5.3: bez odvodenia vedúcich koeficientov sa nesmie spustiť
P5.4 evolúcia ani preniesť staré BR2 stability výsledky na P5.

## Ďalší krok

P5.3b musí odvodiť najnižšie prípustné mocniny a koeficienty
`delta_f`, `U_c`, `U_f` z plnej RHS a constraintov, aspoň pre adiabatický
mód a s `gamma→0` kontrolou. Až potom sa rozšíri na isokurvatúrne módy a
dve štartové plochy.
