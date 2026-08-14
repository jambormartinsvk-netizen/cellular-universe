# Šablóna viac-kolového auditu koľaje

Nový thread patrí do `AUDIT_THREADS/Tnnn_NAZOV/` vlastníckej koľaje:

```text
00_SCOPE_AND_PARTICIPANTS.md
00_CURRENT_THREAD_STATUS.md
ROUND_01/01_AUDIT.md
ROUND_01/02_RESPONSE.md
ROUND_01/03_EVIDENCE_MANIFEST.md
ROUND_01/04_OPEN_POINTS.md
ROUND_02/...
90_THREAD_SUMMARY.md
99_THREAD_DECISION.md
HISTORY/00_EVENT_LEDGER.md
```

Auditné tvrdenie má stabilné ID. Odpoveď používa `ACCEPTED`,
`PARTIALLY_ACCEPTED`, `REJECTED_WITH_EVIDENCE` alebo `OPEN`. Nové kolo
neprepisuje staré. Každé kolo pinne plné názvy, SHA-256, base verzie,
výsledky a presný scope. Rozhodnutie threadu samo nemení stav koľaje; koľaj
dostane samostatnú HISTORY udalosť a aktualizáciu `00_CURRENT_DECISION` alebo
`00_TRACK`.

