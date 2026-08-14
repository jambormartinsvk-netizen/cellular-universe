# Hlavný posudok externého auditu EA-035

**Dátum:** 2026-07-20  
**Externá odpoveď:** `00_AUDITOR_AUDIT.md`  
**SHA-256 externej odpovede:**
`C7BAB2F8A6D92269C8E95B1B14D5802E601792B3540871C494F9D06FF8984C43`  
**Auditor:** Claude Code / Claude Fable 5, Anthropic  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Autorita spracovania:** hlavný orchestrátor  
**Výsledok spracovania:** `ACCEPTED_AGREE_IN_SCOPE`

## 1. Autoritatívny rozsudok

```text
PACKAGE_INTEGRITY_AT_RECEIPT = PASS_171_OF_171
POST_ASSESSMENT_PREFLIGHT = 169_OF_171_EXPECTED_LIVE_PLAN_ADVANCE
KMPC145_TIER = T2_REPRODUCIBLE_READ_ONLY_COMPOSITION
KMPC131_142_143_144_TIER = T1_PRIMARY_FORMULA_AND_RECEIPT_FORENSICS
PROJECT_C3_NID = PASS_9_OF_9_CONFIRMED
GLOBAL_C3 = 39_OF_45_PASS_UNCHANGED
K4_DEPTH = 60_OF_100_UNCHANGED
PHYSICS_STOP = NONE
EXTERNAL_AUDIT_PAUSE = CLOSED
```

Externý audit sa prijíma v celom deklarovanom scope. Neudeľuje nový
fyzikálny verdikt; nezávisle potvrdzuje interný audit 231, účtovanie
`33+6=39/45` a odstraňuje externú reprodukčnú neistotu read-only kompozície
KMPC-145.

## 2. Prijaté výsledky

1. Package preflight prešiel `171/171`; manifest má `29/29` source/copy
   paritu, runtime mapa `3/3`, balík `36` súborov a odpoveď jeden súbor,
   bez duplicitných fyzických hash skupín. Manifest SHA-256 je
   `DA09F7256985F97C69B2058BC6216215586316A6C7A69E0ECA8B0B1DEA109E5C`.
2. Auditor v čistej kópii vykonal compile/help/smoke/official KMPC-145 s
   exitmi `0/0/0/0`. Official generated raw má SHA-256
   `0D3D0968F85D9B5F00AA5186119CFB6647274C1CA7327F0106B573EAA5DC8C1C`.
3. Generated raw sa od reference `017` líšil iba povoleným top-level
   `runtime_seconds`; po jeho odstránení zostalo `0` rozdielov.
4. Smoke input checks prešli `10/10`, official correction checks `14/14`,
   pair je PASS a read-only vetva nevykonala worker, solver ani CPQR.
5. Oba samostatné missing-input guardy skončili exit `2`, so správou
   `immutable input missing or hash-mismatched` a bez success rawu.
6. Protected snapshot pred/po je identický:
   `EBD4021F5BC285551D2EE8DC521E0A9DE23BA6D61CDE5D6DEBAE473BAA2FD97D`.
   KMPC-145 opravil presne dve parity projekcie a odvodené polia.
7. T1 forenzná kontrola potvrdila `.005` pair PASS, `.05` dve cielené
   same-matrix opravy a `.15` af0/audit opravu. Accepted solve ostal
   invariantný, holdout nebol fitovaný a frozen prahy sa nezmenili.
8. PF-127 a PF-128 sú technické/formálne false-negatives bez fyzikálneho
   STOP. Auditor nezistil nepravdivú aktívnu fyzikálnu bránu.
9. Účtovanie je nezávisle rekonštruované: tri nominal NID atómy už boli v
   `33/45`; šesť nulových atómov dáva NID `9/9` a globálne `39/45`.

Bezprostredne pred zápisom tohto posudku kontrolný preflight znovu prešiel
`171/171`. Po autoritatívnej aktualizácii živého
`tracks/00_CURRENT_EXECUTION_PLAN.md` dáva historický preflight očakávane
`169/171`: neprejdú iba `manifest-source-hash` a
`manifest-source-copy-parity` pre tento živý plán. Zapečatená kópia
`EVIDENCE/002__CURRENT_EXECUTION_PLAN.md` ostala na pôvodnom správnom hashi
`78A33B4F...A7CE`; nejde o mutáciu balíka, ale o doložený posun živého zdroja
po uzavretí auditu.

## 3. Tier obmedzenie

KMPC-131/142/143/144 numerika nebola v EA-035 opakovane spustená a zostáva
T1. Auditor ju forenzne potvrdil z primárnych runnerov, zdrojov, provenance
a immutable rawov. T2 sa vzťahuje iba na self-contained read-only KMPC-145.

Toto obmedzenie bolo vopred deklarované, auditor ho dodržal a nejde o
dôkazovú chybu. T3 nezávislý equation builder sa netvrdí.

## 4. Spracovanie nálezov

| ID | Spracovanie | Dopad a náprava |
|---|---|---|
| F-01 | `ACCEPTED_MINOR_FUTURE_PACKAGES` | EA-035 odkazuje aj na účtovné errátum 223, ale jeho fyzickú kópiu neobsahuje. Auditor účtovanie nezávisle rekonštruoval z rawov a priložených dokumentov, preto nejde o evidence gap ani dopad na tier. Zapečatený EA-035 sa nemení. Preflight checklist odteraz vyžaduje každé rozhodujúce referované errátum alebo explicitnú coverage poznámku s cestou a hashom. |
| F-02 | `ACCEPTED_EDITORIAL_STATICALLY_DEMONSTRATED` | Nulové operation counts v runneri 389 sú literály, nie runtime-inštrumentované počítadlá. Statická kontrola zdroja potvrdila absenciu numerických importov a volaní. Frozen runner sa neprepisuje. Budúce read-only balíky musia rozlíšiť `RUNTIME_INSTRUMENTED` od `STATICALLY_DEMONSTRATED` a pri druhom stave vyžadovať source scan auditora. |

Oba nálezy sú bez dopadu na fyziku, NID/C3 register a K4. Nevzniká opravný
balík ani ďalší NID runner. Jedna deklarovaná metodologická odchýlka auditora
iba zopakovala zachytenie stdout synchronným spôsobom; official on-disk JSON,
exit kódy a výsledok sa nezmenili.

## 5. Stav po spracovaní

- C3 NID ostáva autoritatívne `9/9 PASS`;
- globálne C3 ostáva `39/45 PASS`;
- zostáva šesť NIV nulových atómov;
- C3 aggregate ostáva zakázaný do `45/45`;
- K4 ostáva živá na `60/100`;
- S-M mikrofyzická para, P5.4, G8 a G9 ostávajú otvorené alebo zablokované;
- nevzniká release, prediction-table ani Zenodo trigger.

## 6. Ďalší postup

Externá auditná pauza NID je ukončená. Ďalší krok je výhradne read-only
kontrola C3 `NIV/k=.005/gamma0+af0`: overiť nominal authority, frozen
support/depth, leading `j=-1`, nekolidujúci output, runtime realizovateľnosť
a kompatibilitu štvor-shardového kontraktu. Python sa smie spustiť až po
samostatnej predregistrácii a source freeze. Pri REVIEW sa prahy nemenia;
vznikne iba najmenší cause-derived successor.

Stav balíka: `ASSESSED_BY_MAIN_ORCHESTRATOR`.  
Stav projektu: `C3_39_OF_45 / NEXT_NIV_K0P005_READ_ONLY_PREREGISTRATION`.
