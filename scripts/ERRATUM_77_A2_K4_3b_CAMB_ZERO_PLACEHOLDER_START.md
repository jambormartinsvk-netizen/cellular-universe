# Erratum skriptu 77 — nulové riadky pred interným CAMB štartom

Skript `77_script_A2_K4_3b_RG_collective_CAMB_regular_seed_audit.py` pri
predvolenom `k tau_min=2e-4` vybral prvý požadovaný riadok ako seed. Lokálny
CAMB 1.6.6 však pred svojím interným iniciačným časom vracia presné nulové
placeholdery. Výsledná hodnosť `0` preto nebola fyzikálnym výsledkom.

Diagnostický rerun s `k tau_min=0.002` v tom istom skripte dal hodnosť `5`.
Opravený skript 78 nulový prefix explicitne deteguje, vyberie prvý spoločný
aktívny riadok všetkých módov a nuly nikdy nepoužije ako fyzikálne dáta.

Skript 77 sa nemaže. Zostáva dôkazom chyby auditného odberu. Jeho prvý
`REVIEW_REQUIRED/rank=0` výstup nesmie byť citovaný ako smrť fyzikálnej
koľaje ani ako lineárna závislosť módov.
