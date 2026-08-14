# FULL RUN-002 — rozsudok univerzálnosti K4 backgroundu

**Verdikt:** `STOP_BACKGROUND_K_DEPENDENCE_UNRESOLVED`  
**Dopad:** CLASS K4 adapter sa nesmie implementovať.  
**Nedopad:** nie je to smrť A2-K4, G8 ani A1-K1; je to neuzavretá definícia
globálneho backgroundu.  
**Skóre:** bez zmeny, `90/100`.

## Presný výsledok

Audit prešiel všetky štyri symbolické kontroly:

- `mu*z = Omega_m a/Omega_r` — k‑nezávislé;
- `g2*z² = 3a²/(20 sqrt(Omega_r))` — k‑nezávislé;
- palivový faktor `F=z^p[1+g2(1/(p+1)-1/2)z²]` spĺňa presne
  `k dF/dk = pF`;
- pri `p=3.93109` je `dF/dk` nenulová funkcia `a,k`.

Po dosadení definícií má denominator tvar

```text
D(a,k) = 1 + Omega_m a/Omega_r + k^p * A(a),
```

kde `A(a)` už `k` neobsahuje. Preto je surový K7 výraz pivotovo/módovo
závislý a nemožno ho vložiť do CLASS ako jedno `H_K4(a)`.

## Čo sa tým nepreukázalo

Tento audit nepovie, že bunkový mechanizmus je nesprávny. Môže chýbať
globálna normalizácia palivového termu, alebo `K_MPC` v starej formulácii
nemal znamenať Fourierov mód, ale pevný rozmerový referenčný scale. Ani jednu
interpretáciu však nesmieme doplniť potichu: každá vedie k inému globálnemu
backgroundu a musí byť odvodená z teórie, nie vybraná kvôli CLASS.

## Povolený ďalší krok

Samostatná vetva `A1-K1 / background normalization` musí odvodiť význam a
normalizáciu `K_MPC` a preukázať k‑nezávislé `H_K4(a)`. Až potom možno
obnoviť FULL adapter. Štandardný CLASS/HyRec reference backend ostáva
platný a pripravený.

**JSON SHA-256:**
`1564DDE5AA4C4C37DAEDFD5B2CE639C1AA905B71F9BE7B9EE6C04C941988C0FC`.
