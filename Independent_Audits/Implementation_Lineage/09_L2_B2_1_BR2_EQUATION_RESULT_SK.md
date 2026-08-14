# L2-B2.1 — výsledok source-equation auditu BR2 (89/90)

**Dátum:** 2026-07-15  
**Výstup:** `scripts/results/k_mpc_005/RUN_LINEAGE_L2_B2_1_BR2_EQUATION_AUDIT.json`  
**Limit / čas:** 5 s / pod 0.1 s  
**Verdikt:** `PASS_L2_B2_1_BR2_CORE_CONTRACT`

## Výsledok

Všetkých 16 predregistrovaných kontrol prešlo: osem v 89 a osem v 90.
Oba zdroje obsahujú rovnaké auditované jadro:

- `g=lambda/E` a entalpicky vážené `beta`;
- energy-frame `U_d=(1-beta)U_c+beta U_f`;
- CDM kontinuitu s `-s²U_c`, metric členom a transferom;
- CDM Euler s ťahom k `U_f`;
- palivový Euler s pólom `1/delta` a členom `(2U_f-U_d)`;
- `0i` hybnosť s CDM, palivom a baryónmi;
- `k` ako argument perturbatívneho módu, bez pevného `K_MPC=0.05` v backgrounde.

## Záver pre prenos formulácie

Počiatočná formulácia sa nestratila všade. Stratila sa v projektovanom K7
a jeho potomkoch, ale BR2 89/90 ju zachováva v auditovanom skorom jadre.
P5 preto môže vychádzať z rovnakého covariantného kontraktu a porovnávať sa
s 90. K7 zostáva historická redukovaná vetva, nie základ ďalšieho dôkazu.

## Čo ešte neprešlo

PASS nehodnotí plnú palivovú kontinuitu, všetky `00/0i/trace/slip`
constrainty, gauge transformáciu, nulový limit `lambda→0`, plnú hierarchiu,
numerickú konvergenciu ani CMB/S8. Nepridáva žiadne skóre.

## Ďalší krok

`P5.2`: nový čistý constraint ledger pre plný stav s `U_c`, `U_b`, `U_f`
a `U_d`; BR2 90 je porovnávací zdroj, nie autorita bez ďalšieho auditu.
P5.2 musí mať explicitné constrainty a nulové limity, stále bez ODE.
