# A2-K12 — dvojzložkový popol s opačným nábojom

**Stav:** `LIVE_BACKUP / WAITING_FOR_PAIR_KERNEL_AND_SEPARATION_MODE_LEDGER`  
**Workflow fáza:** `CONTRACT_DRAFT_NOT_OPEN / ACTIVE_ERROR_BATCH_NOT_STARTED`  
**Post-error stav:** `R8 PRE-SOLVER BLOCKER MAPPED — 2026-07-16`  
**FS-GATE-01:** `NONEMPTY_WITNESS_K12_K3_1_PAIR_MOMENT_CONE`, ale tri
scoped K3.1 STOP; K12-K1 ostáva `M-016`; bez zmeny skóre  
**Max. hĺbka:** `10/100`

K12 skúma, či dva druhy popola s opačným nábojom môžu zvýšiť rozptyl a
zmeniť momentum/energetický prenos. Samotná párová produkcia však neurčuje
jednoznačne tlak, hybnosť, noise ani znamienko makroskopického účinku.

Scoped STOP K12-K1 a troch K3.1 prienikov sa neprenáša na rodiča. Nový
párový-kernel contract začne vlastný batch `0/10`.

Ďalší krok je konkrétny párový collision kernel s conservation,
pozitivitou, nulovým limitom a observačnými stopami; slovné odpudzovanie
alebo priťahovanie nestačí.

Pokus o postup ku G5 sa zastavil na G2. Symetrická K12-K1 zostáva
`STOP M-016`; otvorené K12-K2/K3 potrebujú explicitný párový kernel a
úplný momentum/pressure/noise ledger.

Už bez presného kernelu možno požadovať kladnú energiu páru, nulový čistý
náboj pri neutrálnej produkcii a nulovú produkciu bez paliva/kanála.
K12-K1 je prázdna podmnožina, lebo presná symetria bez produkcie dá `q=0`,
kým A1 vyžaduje `q>0`; K12-K2/K3 ostávajú otvorené.

FS-GATE našla pozitívny cold neutral pair momentový svedok s korelovaným
PSD number noise. Zároveň dokázala, že opačné náboje nemôžu zrušiť kladný
kinetický tlak: trvalá dispersia + exact pressureless A1 je prázdny
prienik. Pri presnej symetrii sa vnútorné sily zrušia v total COM rovnici,
takže cold K3.1 total/fuel blok zostáva K1-like a neopravuje M-009. Bežný
smooth 1->2 rozpad navyše nemá finite rate presne na cold prahu.

Rodič zostáva otvorený cez K12-K2 alebo rozšírenú K12-K3 s coherent/cold
produkciou a novým externým momentum/field ledgerom. Taký ledger musí
stabilizovať separation mód a nesmie iba pridať net fifth force či nový
`S8` fit. Úplný výsledok je v
`ARTIFACTS/FS_GATE_01_K12_K3_1_PAIR_PRODUCTION_MOMENT_RESULT_AND_AUDIT.md`.
