# Pokyny externému auditorovi EA-042

1. Auditujte iba otázky a T1 hranicu z dokumentu 00.
2. Z koreňa projektu spustite R6 package preflight cez PowerShell 7+ a
   zapíšte presný príkaz, exit code a wall time.
3. Overte manifest `14/14`, source/copy paritu, package `21`, response `1`,
   `REPRO=0`, runtime rows `0`, nulové duplicity a dočasné súbory.
4. Nevykonávajte Python; balík nemá runtime ani generated JSON.
5. Overte source chain `e -> s+M`, následné `M->C` a spoločný vertex-level
   conservation ledger.
6. Skontrolujte úplnosť a rozlíšenie MF1–MF4. Najmä oddeľte stavový switch
   MF3 od skutočne paralelných konzervatívnych kanálov MF4.
7. Overte, že `z`, prah aj transition weight MF3 musia byť odvodené z
   lokálneho kernelu a že nedochádza k double-count.
8. Skontrolujte, či `F_D=empty` vyžaduje univerzálny argument a bounded
   nenájdenie svedka ostáva `REVIEW/UNRESOLVED`.
9. Overte, že PH1 nie je zvolený zákon, ale iba podmienený MF2 kandidát.
10. Posúďte S8 iba ako holdout po uzavretí perturbation moments; background
    source sám nesmie určovať S8.
11. Posúďte B6b-1 ako najmenšiu ďalšiu hĺbku bez výberu mikrofyziky.
12. Každý hlavný záver označte dôkazovým tagom a použite `EVIDENCE/009` ako
    exact formula-lineage checklist.

Povinné ledger termíny: `generated JSON`, `exit code`, `wall time`,
`odchýlka`.
