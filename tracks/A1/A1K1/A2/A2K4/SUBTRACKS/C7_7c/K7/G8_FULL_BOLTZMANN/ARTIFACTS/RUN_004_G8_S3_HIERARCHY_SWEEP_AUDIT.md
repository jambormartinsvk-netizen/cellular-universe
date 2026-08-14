# RUN-004 — audit G8 SCREEN-S3: hierarchy-tail convergence

**Verdikt:** `PASS_G8_SCREEN_S3_HIERARCHY_CONVERGENCE`  
**Skóre:** `0`; support/WBS ostáva `90/100`  
**Rozsah:** len tri dynamické hierarchické rodiny, nie plný G8 backend.

**SHA-256 JSON:** `AECA9A260B94136D761B56557B7E2068B37E0A8BF19382DAE99F234F9EBA197A`

## Výsledok

| Porovnanie | Výsledok | Predregistrovaná hranica | Stav |
|---|---:|---:|---|
| nízke momenty `lmax=12 → 16` | `5.294×10^-16` | `<=1×10^-5` | PASS |
| nízke momenty `lmax=8 → 12` | `3.529×10^-16` | `<=5×10^-4` | PASS |
| najväčší chvost (G, `lmax=8`) | `4.541×10^-70` | `<=1×10^-6` | PASS |
| maximum RHS volaní | `837` | `<=100000` | PASS |

Všetky behy dosiahli `x=-22`, boli konečné a pod safety cap. Použitý bol
nenulový radiačne-asymptotický closure; nešlo o starý closure `L_(lmax+1)=0`.
Celý sweep trval `0.328 s` interne a `1.9 s` procesne, pod limitmi.

## Presná hranica tvrdenia

S3 potvrdzuje, že pri zamrznutej K4 radiácii je odrezanie troch aktívnych
hierarchických rodín stabilné a prakticky nezávislé od `lmax`. Dynamické
počty sú `21/33/45` pre `lmax=8/12/16`; plné G8 registre `32/44/56` ešte
nebežali, lebo ich metrické, hustotné, baryónové a palivové zložky nie sú v
tomto screen-e súčasne integrované. Preto tento výsledok nedokazuje plný
Einstein-Boltzmann systém, fyzikálnu opacitu, rekombináciu ani CMB.

## Ďalší krok

S0–S3 sú uzavreté. Pred FULL treba implementovať zdrojovo auditovateľný
32/44/56‑stavový backend s presným K4 backgroundom, štandardnou atómovou
kinetikou, TCA switchom, plnými constraintmi a tým istým `lmax` sweepom.
Až takýto beh môže získať G8 `+5` a posunúť support na 95/100.
