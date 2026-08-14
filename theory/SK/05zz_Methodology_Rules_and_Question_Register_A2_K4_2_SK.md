# Dodatok k 05 — metodické pravidlá a register otázok: A2-K4.2 (SK)

**Dátum:** 2026-07-14  
**Nadväzuje na:** Q54 a AR14, AR25, AR28, AR29  
**Autoritatívny audit:** `Audit/A2_K4_2_HIGH_K_SUBHORIZONTOVY_AUDIT_A_ROZSUDOK.md`

## Kontrola duplicity pravidiel

K4.2 nepotrebuje nové auditné pravidlo. Úplná regulárna báza je už pokrytá
AR28, rozdiel medzi absolútnym transferom a referenčným gainom AR25, význam
skóre AR14 a časové limity AR29. Tieto pravidlá sa nemenia ani neduplikujú.

## Q56 — Prešla A2-K4 high-k a subhorizontovou bránou K4.2?

**Stav:** `ÁNO V PERFECT-RADIATION ROZSAHU; K4 PREŽÍVA 59/100.`

Hlavný symbol má charakteristické rýchlosti `0x4`, `±1` a `±1/sqrt(3)`.
Interakcia je iba v nižšom ráde `k^0`, nemení charakteristiky a má správny
`lambda=0` limit. Propagujúce palivové a radiačné bloky sú
diagonalizovateľné, s kladnými efektívnymi kinetickými a gradientovými
znamienkami.

CDM a baryónové nulové bloky sú Jordanove bloky beztlakového prachu. Tento
defekt je prítomný aj pri `lambda=0`; nie je novou K4 nestabilitou a rozsudok
ho zachováva ako obmedzenie efektívnej fluidnej aproximácie.

Úplná trojica regulárnych módov prešla na `q=30,300,1000`. Najväčší
`1e-5 T_max` bol `0.240017`, najhoršie aktívne bodové relatívne `00`
rezíduum `4.41484e-8` a všetky tri konvergenčné brány q=300 prešli. K4 mala
na každom q menší `T_max` než nulový limit, preto veľký subhorizontový rast
nie je interakčne vyvolaná high-k explózia.

## Čo Q56 nedokazuje

Q56 nedokazuje mikroskopickú akciu, fundamentálnu UV no-ghost vetu, plnú
fotónovú/neutrínovú Boltzmannovu hierarchiu, CMB zhodu ani správne `S8`.
Historický M-011 zostáva zachovaný, ale jeho všeobecný dosah obmedzili K4.1
a K4.2 na starý neregulárny velocity seed a chybnú interpretáciu
referenčného gainu.

## Následná otvorená otázka Q56a — Prejde K4 plnou Einstein–Boltzmannovou bránou?

**Stav:** `OTVORENÁ — K4.3.`

Treba doplniť samostatné fotónové a neutrínové hierarchie, anizotropný stres,
baryón-fotónovú väzbu, rekombináciu, gauge/implementačný krížový test a
CMB-normalizované transfery. Až potom sa smie vyhodnotiť `sigma8`, `S8` a
likelihood v A3.

