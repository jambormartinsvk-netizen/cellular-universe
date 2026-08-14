# Pokyny externému auditorovi EA-039

1. Auditujte iba presnú otázku z dokumentu 00 a zachovajte hranicu T2;
   T3 sa netvrdí.
2. Z koreňa projektu spustite R6 package preflight cez PowerShell 7+ a
   zaznamenajte presný príkaz, exit code a wall time.
3. Overte manifest `25/25`, runtime mapu `22/22`, exact REPRO coverage
   `22/22`, package `32`, response `1`, nulové duplicate hash groups,
   placeholdery a temp súbory.
4. Originálny package nechajte read-only. V novej dočasnej kópii `REPRO/`
   zaznamenajte OS/architektúru a Python, potom oddelene vykonajte compile,
   help, smoke a official z dokumentu 03. Každý proces má vonkajší limit
   `10 s`.
5. Pre každý proces zapíšte presný príkaz, exit code, wall time,
   stdout/stderr a pri official generated JSON cestu aj SHA-256.
6. Overte, že smoke nevytvoril raw, má `physics_executed=false`, `6/6`
   checks a operation counts nula.
7. Official musí mať `20/20` vstupov, `15/15` pair a `5/5` authority pass,
   exact 45 unikátnych atómov, mode counts `9` každý a nulové workery,
   solvery, fyziku a matice.
8. Nezávisle zostavte očakávaný register v poradí
   `AD,CDI,BI,NID,NIV × .005,.05,.15 × nominal,gamma0,af0` a porovnajte ho
   s generated JSON; nepoužite agregátor na vytvorenie očakávaného zoznamu.
9. Porovnajte generated JSON s `EVIDENCE/003` podľa jedinej normalizácie v
   dokumente 03. Každý ďalší rozdiel je nález.
10. V dvoch fresh kópiách vykonajte missing-pair a missing-mode-authority
    guard. Oba musia skončiť nonzero bez success rawu a bez fyzikálneho
    verdiktu.
11. Každú odchýlku označte `DECLARED_DEVIATION`; vetva s odchýlkou nemôže
    dostať T2.
12. Pri tvrdeniach použite evidence tags a oddelte integritu, formálnu
    logiku, reprodukciu, fyzikálny rozsah a účtovanie.
13. Explicitne posúďte interný záver: C3 aggregate `45/45` je podporený,
    ale K4 ostáva `60/100`, P5 `3.5/6` a P5.4 `NOT RUN`.

Povinné ledger termíny: `generated JSON`, `exit code`, `wall time`,
`odchýlka`.
