# Q1R6 → Q1R7 — ordered transition a complete-source preregistrácia

**Stav:** `DRAFT_UNFROZEN / NO_SOURCE_OPERATION / NO_PYTHON`  
**Dátum:** 2026-07-27  
**Route:** `A1_K1_A2_K4 / P5.3 / B6b-2.10 / H_RDIV-MF1-v1 / C01-RW1`  
**Autor teórie:** Martin Jambor  
**Autor procesného artefaktu:** Codex, task `/root`  
**Účel:** mechanicky otvoriť nasledujúci zmrazený kandidát Q1R7 a ešte pred
prvým prístupom k jeho zdroju uzavrieť úplnú acquisition/screen metodiku.

## 1. Autoritatívny vstup a poradie

Zmrazený ordered ledger:

```text
PATH: tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/264_B6B2_10_H_RDIV_C01_RW1_V1_W10_RAW_V2_SOURCE_COVERAGE_RESULT_SK.md
SHA256: DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A
EXACT_ROW: 111
FAMILY: F-A
QUERY: Q1
ORDERED_RANK: 7
TITLE: Hydrodynamics of ultra-relativistic bubble walls - ScienceDirect
URL: https://www.sciencedirect.com/science/article/pii/S0550321316000535
FROZEN_PREVIOUS_STATUS: NOT_REACHED_AFTER_Q1_R3_INACCESSIBLE_BLOCKER / NOT_OPENED
```

Q1R7 sa vyberá iba z tohto riadku. Názov, URL, PII ani poradie sa po prvom
source prístupe nesmú meniť. Q1R3 `24/24_TERMINAL`, Q1R5
`15/15_TERMINAL` a Q1R6 `1/1_TERMINAL` zostávajú bez resetu; Q1R6 je iba
`REFERENCE_INTERFACE_MODEL_ONLY`, nie complete W10 ani refutácia.

## 2. Predmet testu

Q1R7 prejde iba vtedy, ak jedna bibliograficky zviazaná verzia toho istého
diela poskytne úplný primárny model a všetky povinné W10 passport objekty.
Publisher article, DOI landing, author manuscript a arXiv verzia sa smú
považovať za tú istú prácu iba pri exact title/author a DOI/PII/arXiv
cross-bindingu. Fyzikálne objekty z rôznych prác sa nesmú skladať.

Presná auditná otázka:

> Obsahuje Q1R7 v jednom koherentnom modeli source-exact `Z_rec`, kumulatívne
> `W_rec`, pointwise nezáporný `P_rec=D_uW`, pozitívny cycle-frozen `W_*`,
> disjunktný conservation ledger, parent-cell `u_cell` a konečnú invariantnú
> mieru, temporal first upward crossing, reset mapu, source-off identitu a
> noncircularity, alebo je iba ďalším čiastkovým interface modelom?

## 3. Source-operation cap, durable journal a deterministické poradie

Jedna **source operation** je jeden začatý top-level HTTP request. Interné
redirecty toho istého requestu sa zapíšu ako redirect chain, nie ako nové
operácie. Parser/command chyba pred odoslaním requestu spotrebuje nulu;
transportná chyba po odoslaní spotrebuje jednu. `MAX_REQUESTS=6`; finálny
stav je `n/6_TERMINAL` a preskočené sloty sú permanentne retired, bez resetu.

Povolené poradie:

Pred requestom sa cez exclusive `CreateNew` vytvorí journal 283C. Každý
request má odlišný `STEP_ID` a request ordinal. Bezprostredne pred odoslaním
sa zapíše a `Flush(true)` riadok `REQUEST_RESERVED`; po ukončení sa zapíše
`REQUEST_COMPLETED` a znova `Flush(true)`. `REQUEST_RESERVED` bez
`REQUEST_COMPLETED`, nečakaný exit, timeout celého procesu alebo poškodený
journal znamená terminal technical failure a zakazuje rerun. Cap sa teda po
páde procesu nedá resetovať.

Frozen work title vznikne z display title v §1 odstránením exact ASCII
suffixu ` - ScienceDirect` práve raz z konca. Iný alebo chýbajúci suffix je
identity failure. Normalizácia titulu aj autorov je: Unicode NFKC, trim,
každý súvislý rad `U+0009/U+000A/U+000D/U+0020` → jeden `U+0020`, potom
Unicode invariant lowercase; žiadna interpunkcia ani diakritika sa nemaže.
Author set sa porovnáva ako zoradená množina celých normalizovaných mien.

Presný schedule:

1. `O1_PUBLISHER`: exact `GET`
   `https://www.sciencedirect.com/science/article/pii/S0550321316000535`;
2. `O2_DECLARED_FULLTEXT_OR_CROSSREF`: z O1 vyberie full-text URL iba ak
   existuje **práve jeden** HTTPS link, ktorého resolved host je
   `sciencedirect.com`/jeho subdoména alebo `elsevier.com`/jeho subdoména,
   resolved URI obsahuje exact PII `S0550321316000535` a path končí `.pdf`
   alebo query obsahuje token `pdf`. Viac než jeden je `AMBIGUOUS` a žiadny
   sa nevyberie. Ak je počet nula alebo ambiguity, O2 je namiesto toho exact
   `GET https://api.crossref.org/works?query=S0550321316000535&rows=3&select=DOI%2Ctitle%2Cauthor%2CURL`;
3. `O3_ARXIV_EXACT_TITLE_QUERY`: exact `GET`
   `https://export.arxiv.org/api/query?search_query=ti%3A%22Hydrodynamics%20of%20ultra-relativistic%20bubble%20walls%22&start=0&max_results=3&sortBy=relevance&sortOrder=descending`;
4. `O4_ARXIV_ABSTRACT`: iba ak O3 má práve jeden entry s exact normalized
   work title a buď exact DOI z O1/O2, alebo exact author-set z O1/O2;
   URI je `https://arxiv.org/abs/<ID>`, kde `<ID>` je exact canonical ID z
   tohto entry. Inak `SKIPPED_PRECONDITION`;
5. `O5_ARXIV_EPRINT`: iba ak O4 body opakuje exact title, author-set a ID;
   URI je `https://export.arxiv.org/e-print/<ID>`. Inak
   `SKIPPED_PRECONDITION`;
6. `O6_DOI_BINDING`: iba ak O1/O2 poskytlo práve jeden DOI a žiadny accepted
   source ešte neexistuje; URI je `https://doi.org/<percent-encoded DOI>`.
   O6 je provenance-only a nesmie sa premapovať na neohlásený download.

Crossref record je eligible iba ak O1 už poskytlo neprázdny bound author-set,
record má exact normalized work title a exact rovnaký normalized author-set.
Eligible musí byť práve jeden record; inak Crossref DOI/author metadata sú
`AMBIGUOUS` alebo `MISSING` a nesmú sa použiť v O4/O6. DOI normalizácia je
NFKC, trim, invariant lowercase a odstránenie najviac jedného exact prefixu
`https://doi.org/` alebo `http://dx.doi.org/`; výsledok musí mať práve jeden
neprázdny registrant segment pred prvým `/` a neprázdny suffix. „Práve jeden
DOI“ znamená jednu distinct hodnotu po tejto normalizácii naprieč eligible
O1/O2 metadata. O6 path vznikne percent-encodingom každého DOI segmentu cez
RFC3986 UTF-8 s uppercase hex a spojením segmentov literal `/`; query a
fragment sú zakázané.

Každý nevykonaný krok dostane `SKIPPED_PRECONDITION`; po accepted source sa
všetky zvyšné sloty zapíšu `SKIPPED_SOURCE_ALREADY_ACCEPTED`. Finálny stav
je vždy `n/6_TERMINAL` a všetky nepoužité sloty sú navždy retired. Žiadny
všeobecný web search, upravený query, hádanie identifikátora, retry, mirror,
subresource load ani siedma operácia nie sú povolené.

## 4. Transport, identita a F-001 closure

Frozen transport contract:

```text
METHOD: GET only
USER_AGENT: Teoria-Q1R7-CompleteSource/1.0
ACCEPT_ENCODING: identity
AUTOMATIC_DECOMPRESSION: NONE
CONNECT_TIMEOUT: 10 s
RESPONSE_HEADERS_TIMEOUT: 30 s
PER_REQUEST_BODY_TIMEOUT: 90 s
WHOLE_PROCESS_TIMEOUT: 600 s
MAX_REDIRECTS: 5
MAX_HEADER_BYTES: 65536
MAX_BODY_BYTES: 67108864
RETRIES: 0
RANGE_REQUESTS: 0
COOKIES: 0
SUBRESOURCE_LOADS: 0
```

Redirect musí zostať HTTPS; downgrade, userinfo, non-443 explicit port alebo
redirect loop failne daný request. O1/O2 direct fulltext/O4/O5/O6 final host
musí patriť k hostom povoleným jeho stepom; O3 zostáva
`export.arxiv.org`. Hashujú sa exact HTTP entity-body bytes po odstránení
transfer framingu, ale pred akýmkoľvek content decodingom; preto sa žiada
`identity` a ak server napriek tomu vráti non-identity `Content-Encoding`,
body je neakceptovateľné, no jeho wire-entity hash a length sa zapíšu.

Každá vykonaná operácia zapíše do jediného receiptu:

- ordinal, UTC start/end, requested URL, redirect chain a final URL;
- HTTP status, MIME, Content-Length aj skutočný byte length;
- SHA-256 celého body, prvých 16 magic bytes a transportnú chybu;
- title, authors, DOI, PII a arXiv ID presne tak, ako sa nachádzajú v body
  alebo hlavičkách; absent hodnoty sú `MISSING`, nie domyslené;
- cross-binding mapu `identifier -> exact archive/PDF SHA256`.

Accepted source musí uzavrieť bibliografický binding, ktorý v EA-046 tvoril
minor F-001. Samotný názov lokálneho súboru alebo charterové tvrdenie nestačí.

## 5. Complete-source akceptácia

Povolené typy accepted source:

### A. Source archive

- povolený je iba raw POSIX TAR s `ustar` signature na offsete 257 alebo
  RFC1952 GZIP s práve jedným memberom, bez trailing/concatenated bytes,
  ktorého dekomprimovaný obsah je TAR alebo jeden strict-text TeX súbor;
  ZIP, 7z, RAR, nested container a neznámy formát sú zakázané;
- iba regular files/directories, bez absolute path, `..`, linkov, device a
  nested archive/container položiek;
- compressed body ≤ 64 MiB, decompressed total ≤ 256 MiB, najviac 512
  entries, regular entry ≤ 32 MiB, ratio ≤ 200 a parse deadline 60 s;
- path sa musí používať s `/`; zakázané sú backslash, empty segment, `.`,
  `..`, leading `/`, UNC, drive prefix, colon/ADS, trailing dot/space a
  Windows reserved basenames `CON,PRN,AUX,NUL,COM1..9,LPT1..9`; exact aj
  `OrdinalIgnoreCase` normalized-path kolízia je FAIL;
- každá regular položka dostane path/type/length/SHA256;
- content-based classifier sa aplikuje na všetky položky bez extension
  výnimky. Frozen binary signatures sú PDF `%PDF-`, PNG
  `89504E470D0A1A0A`, JPEG `FFD8FF`, GIF `GIF87a/GIF89a`, PostScript `%!PS`,
  TIFF `II2A00/MM002A`, BMP `BM`, OLE `D0CF11E0A1B11AE1`, ELF, PE `MZ`, ZIP,
  GZIP, RAR a 7z. Inak strict UTF-8, potom strict CP1252 s byte-roundtrip;
  undefined CP1252 bytes failnú. Raw NUL/DEL a C0 okrem HT/LF/FF/CR failnú;
  decoded Unicode category `Cc` okrem týchto štyroch a každé `Cf` okrem
  jedného leading U+FEFF failnú. Unknown nontext je FAIL;
- musí existovať práve jeden strict-text `.tex` root obsahujúci exact
  normalized work title, celý bound author-set, abstract, najmenej jednu
  substantive body section, najmenej jeden equation/math environment a
  references (`thebibliography` alebo bound bibliography target). Cover,
  preview, first-page alebo abstract-only root je FAIL. Staticky sa
  rekurzívne riešia `input`, `include`, `includegraphics`, `bibliography`,
  `bibliographystyle`, `addbibresource`; macro/dynamic path je FAIL. Všetky
  TeX, deklarované appendix/supplement, bibliography/style a graphics targets
  musia byť prítomné a closure musí mať nula chýbajúcich či cyklicky
  neukončených cieľov. Každá regular entry sa navyše kontroluje na nested raw
  TAR cez `ustar` signature na byte offsete 257; táto signatúra je nested
  container FAIL rovnako ako ZIP/GZIP/RAR/7z.

### B. Canonical full article PDF

- body začína `%PDF-`, MIME/length nie sú HTML error page;
- title a authors sú v PDF text layer alebo primary metadata;
- PDF obsahuje úplný článok od title/abstract cez rovnice až po references,
  bez `preview`, `first page`, `abstract only` alebo chýbajúcich strán;
- pred networkingom musia `pdfinfo -v`, `pdftotext -v`, `pdftoppm -v`
  existovať; exact verzie sa zapíšu. Bounded commands sú
  `pdfinfo <blob>`,
  `pdftotext -layout -enc UTF-8 -nopgbrk <blob> <temp.txt>` a
  `pdftoppm -png -r 144 -f 1 -l <N> <blob> <temp-prefix>`;
- každý command timeout 120 s; nonzero exit, encryption, password request,
  stderr s `Error`, `Syntax Error` alebo `Warning`, page count mimo 1..200,
  render count iný než N, zero-size page alebo temp render total > 512 MiB
  znamená uncertified source;
- text SHA-256, page count, title/authors, abstract, equations/sections,
  appendix declarations a references heading sa zapíšu. Každý passport
  equation claim musí byť mapovateľný na stránku a čitateľný buď v text
  layer alebo v povolenom full-page renderi; inak je source uncertified.

Ak accepted source nespĺňa A ani B, výsledok je
`REVIEW_Q1R7_SOURCE_UNIVERSE_NOT_CERTIFIED_NO_PHYSICAL_INFERENCE`.

## 6. Publikačný kontrakt

Povolené nové live artefakty tohto atómu:

```text
283  preregistrácia (tento súbor)
283A accepted source bytes, exact path:
     tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/283A_B6B2_10_Q1R7_PRIMARY_SOURCE_BLOB.bin
283B acquisition/source-universe receipt a commit marker, exact path:
     tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/283B_B6B2_10_Q1R7_COMPLETE_SOURCE_RECEIPT.txt
283C durable operation journal, exact path:
     tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/283C_B6B2_10_Q1R7_SOURCE_OPERATION_JOURNAL.txt
284  physics/result document, exact path:
     tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/284_B6B2_10_H_RDIV_C01_RW1_V1_Q1R7_S0_S13_RESULT_SK.md
```

Pred networkingom musia 283A/283B/283C aj temp adresár absent. Journal 283C
sa vytvorí prvý cez `CreateNew` a ostáva live. Acquisition beží v jednom
bounded PowerShell 7 procese. Accepted blob a receipt vzniknú ako temp súbory
v tom istom adresári. Po ukončení source operácií sa journal doplní o
`READY_TO_COMMIT`, flushne, zavrie a už sa nemení; jeho SHA je v receipte.

Commit order je: (1) preflight všetkých cieľov pred sieťou; (2) pri accepted
source close/hash temp 283A, same-volume move na 283A, znovu hash; (3) vytvoriť
283B s exact hashom 283A a 283C, close/hash, move 283B **posledný** ako commit
marker. Pri evidence-incomplete výsledku bez source sa 283A nevytvorí a 283B
commitne terminal operation ledger + journal hash. 283A bez 283B, 283B s
nezhodným cross-hashom, journal bez commit receiptu, target collision,
neodstránený temp alebo abnormal exit je terminal technical failure, bez
fyziky a bez rerun.

## 7. S0–S13 a vetvenie

S0 sa vyhodnotí až po `SOURCE_UNIVERSE_COMPLETE=PASS` a exact identity
bindingu. Pri neúplnom source sú S0–S12
`NOT_ASSESSABLE_EVIDENCE_INCOMPLETE`, S13 je iba process-integrity PASS/FAIL.

Pri úplnom source sa mapujú:

```text
S0  primary identity + complete-source provenance
S1  one-model closure a units/sign/orientation
S2  Z_rec a kumulatívne W_rec
S3  P_rec = D_u W >= 0
S4  0 < W_* < infinity a cycle freeze
S5  disjoint stored/dissipated/export/loss/residual ledger
S6  parent-cell u_cell, congruence/worldtube a finite invariant measure
S7  temporal first upward crossing
S8  R_reset^Z, zero daughter credit a residual bookkeeping
S9  covariance, regularity, causality, stability a convergence
S10 noncircularity voči downstream observables a targetom
S11 jedna provisional Y_div bez dodatočnej fyziky
S12 source-off/no-growth/no-event nulové limity
S13 provenance, caps, process a nonfit integrita
```

Outcome precedence je záväzná a prvá zodpovedajúca vetva vyhráva:

1. technical/provenance/S13 failure → `TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE`;
2. uncertified source alebo identity →
   `REVIEW_Q1R7_SOURCE_UNIVERSE_NOT_CERTIFIED_NO_PHYSICAL_INFERENCE`;
3. certified source so source-exact kontradikciou required W10 row → iba
   candidate-local exclusion v presne odvodenej miere, nie global no-go;
4. inak aspoň jeden required `MISSING` →
   `PASS_Q1R7_REFERENCE_OR_COMPONENT_MODEL_ONLY / REVIEW_Q1R7_NOT_A_COMPLETE_W10_WITNESS`;
5. všetky S0–S13 PASS →
   `COMPLETE_W10_CANDIDATE_PENDING_INDEPENDENT_RESULT_AUDIT`.

P4 work atom sa môže zvýšiť `3→4` iba po complete-source výsledku,
nezávislom result audite a main acceptance. Physical witness attempts sa
zvýšia `0→1` iba ak je predložený kompletný W10 kandidát na všetkých
passport poliach, nezávislý result audit prejde a main orchestrátor ho
prijme; partial/reference screen zostáva `0`.

## 8. Zakázané interpretácie

Bez nového author inputu je zakázané:

- skladať passport z Q1R6 a Q1R7 alebo iných prác;
- premenovať fluid/wall velocity na `u_cell`, pressure na `P_rec`, latent
  heat/barrier na `W_*` alebo spatial wall profile na temporal crossing;
- doplniť reset, mieru, ledger alebo source-off identitu z filozofie teórie;
- meniť K4/P5 skóre, hĺbku, A3 stav alebo `RUN_AUTHORIZED`;
- spustiť Python, solver, fit, S8/H0 alebo P5.4/G8/G9.

## 9. Handoff capsule

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R7-ORDERED-TRANSITION-PREREG-AUDIT-20260727-284
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit
INTERNAL_AUDITOR_TASK_ID: /root/c01_q1r3_access_result_audit
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED_PACKAGE_CURATOR_Q1R7
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_EXTERNAL_AUDITOR_Q1R7
SEPARATION_OF_DUTIES_CHECK: /root != /root/c01_q1r3_access_prereg_audit; /root != /root/c01_q1r3_access_result_audit; NOT_ASSIGNED_PACKAGE_CURATOR_Q1R7 != NOT_ASSIGNED_EXTERNAL_AUDITOR_Q1R7
ROUTE: A1_K1_A2_K4/P5.3/B6b-2.10/H_RDIV-MF1-v1/C01-RW1/Q1R7
CURRENT_PHASE: DRAFT_UNFROZEN_PREREGISTRATION
PARENT_DECISION: task282 accepted EA-046 scoped external closure and authorized independently audited Q1R7 preregistration before source access
CLAIM: freeze one ordered Q1R7 identity, bounded acquisition and fail-closed complete-source/S0-S13 contract
NONCLAIMS: no source access; no Q1R7 physics; no complete W10/reference/exclusion; no score/depth/A3/run change
ALLOWED_NEXT_ACTION: independent read-only prereg audit only
ALLOWED_READS: mandatory bootstrap; this document; doc264; current/K4/P5 state; event ledger; prior Q1R6 result/audit only for frozen boundary
ALLOWED_WRITES: NONE_FOR_AUDITOR
FORBIDDEN_ACTIONS: source operation; edit; Python; physics verdict; score/depth/run change
FROZEN_THRESHOLDS: source_cap=6; connect=10s; headers=30s; body=90s; process=600s; redirects=5; headers=65536B; body=67108864B; archive_decompressed=268435456B; entries=512; entry=33554432B; ratio=200; archive_deadline=60s; PDF_pages=1..200; PDF_command=120s; PDF_temp=536870912B
RULESET_PATHS_AND_SHA256: AGENTS=226710D6467FE923D6F2CBAFF02CE9235F1B48C07C4A9DACD95C6B06486B2B29; OS=519BDCBAE2CD9BF62351586E357DE3C9A28E60AD79CDB653661DD2821D65B6E7; METHODOLOGY=AB29543ACD4F132276DF59E1020EEA6FB3A042C78FAAA1B7DDD448F5479D0FF1
AUDITOR_RULESET_PATHS_AND_SHA256: N/A_INTERNAL_PREREG_AUDIT
AUDITOR_ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
IMMUTABLE_INPUT_PATHS_AND_SHA256:
  doc264=DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A
  current=2C96C5726A73B6CC947B064A7E5D559D8B6665BB8323E0F4E71EC2CED97480C7
  K4=35650DC42EE905C1B4B3B183B9F605C3F639C8BE25C12A6F3FA57BD33B99DC9D
  P5=D5751DD696936BD3F854D58040EF4C9507EEC4F2E1408068FC071EC280831332
  ledger_through282=32CD37978FE0D62451082D70E1E128D0D0E138F5BAE7FE2EAEB06C9F7803DFB4
PREREG_SHA256: PENDING_AFTER_INDEPENDENT_AUDIT
RUN_AUTHORIZED: false
TIMEOUT_AND_OUTPUT_GUARDS: auditor read-only; no process/source; acquisition later uses section4/5 limits, exclusive journal and 283B-last commit marker
OUTPUT_PATHS: auditor chat response only; later exact 283A/283B/283C/284 paths in section6
LIVE_FILE_BUDGET: maximum 5 live scientific artifacts document283+283A+283B+283C+result284; central registers batch only after state change
DONE_WHEN: auditor verifies rank identity, source cap/order, bibliographic binding, complete-source classifier, atomic publication, S0-S13 mapping, accounting and nonclaims; returns PASS or exact corrections
NEXT_ROLE: main_orchestrator correction/freeze, then bounded non-Python acquisition
```

## 10. Stav pred auditom

```text
Q1R7_SOURCE_OPERATIONS: 0/6
Q1R7_SOURCE_OPERATION_JOURNAL: ABSENT
Q1R7_ACCEPTED_SOURCE: ABSENT
SOURCE_UNIVERSE_COMPLETE: NOT_RUN
PHYSICAL_INTERPRETATION: NONE
P4_WORK_ATOMS: 3
PHYSICAL_WITNESS_ATTEMPTS: 0
K4: 60/100
P5: 3.5/6
RUN_AUTHORIZED: false
PYTHON_PROCESSES: 0
```
