# A2-K4 / C7.7c / K7b.3b — počiatočný REVIEW: prepísanie registra nulovým limitom

Dátum: 2026-07-15  
Stav fyzikálnej koľaje A2-K4: **ŽIVÁ, 66.5/100**  
Stav implementácie skriptu 172: **REVIEW — neplatný krížový porovnávací beh**

## Výsledok NID/deep

Skript `172_script_A2_K4_C7_7c_K7b3b_hard_constrained_constraint_gate.py` skončil za 2.58 s s verdiktom `REVIEW_C7_7C_K7B3B_HARD_CONSTRAINED_STANDARD_UNCLOSED`. Shallow sa podľa predregistrácie nespustil.

Tvrdé kotvy samotné prešli:

- 30 fixovaných a 58 voľných koeficientov;
- nulový konflikt tvrdých kotiev;
- maximálna chyba fixovaných hodnôt 0;
- redukovaná matica mala plnú hodnosť 58;
- high-precision rezíduum `2.09e-16` bolo menšie než float64 rezíduum `1.13e-14`.

Zlyhali však aktivita D-prime, rekonštrukcia `U_fs`, hybnostný constraint, rekonštrukcia stavu a Eulerova rovnica `U_gamma`.

## Audit príčiny

Toto zlyhanie zatiaľ nie je fyzikálny konflikt. Export 171 volá `solve_standard(mode, mu)` pre každý mód najmenej dvakrát:

1. s fyzikálnym `mu = physical_mu`, ktoré tvorí stavové plochy;
2. s `mu = 0` pre samostatnú kontrolu nulového matter-limit.

High-precision register bol ukladaný pri každom volaní s rovnakým módom. Druhé volanie preto prepísalo fyzikálny register nulovým limitom. Dôkazom je napríklad NID koeficient `U_gamma[1]`: fyzikálny float register má `-0.0018345684`, ale prepísaný HP register má presne `0`. Skript 172 následne porovnával HP štandardný sektor pri `mu=0` s frakčným sektorom a stavovými plochami pri fyzikálnom `mu`.

## Rozsudok

- Skript 172 sa zachováva ako neúspešný diagnostický artefakt.
- Výsledok nesmie zabiť K7b.3b ani A2-K4.
- Zakázané je uvoľniť fyzikálne tolerancie; musí sa opraviť výber registra.
- Ďalší krok je K7b.3b.1: nemenná oprava, ktorá zachytí HP register iba pri `mu = physical_mu`, potom zopakuje NID/deep.

