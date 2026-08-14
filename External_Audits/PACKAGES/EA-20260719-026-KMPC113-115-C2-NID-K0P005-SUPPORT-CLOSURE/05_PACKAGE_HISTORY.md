# História balíka EA-026

## 2026-07-19 — DRAFT_NOT_DELIVERED

Balík zhromažďuje ucelené uzavretie C2 atómu NID/k=.005: nominal
KMPC-113, verdict-free support checkpoint KMPC-114, resume KMPC-115,
PF-113, tri immutable rawy a interný audit dokument 183.

Theory author: Martin Jambor. Script creator/internal auditor: Codex
(OpenAI). Pracovná zmena nepoužila nový base modul; oba support runnery
znovupoužívajú byteovo nezmenenú auditovanú checkpoint architektúru.

Pred sealom musí prejsť package preflight, negatívny missing-prerequisite
guard a tri nezávislé field-level reprodukcie všetkých troch rawov.

## 2026-07-19 — DRAFT REPRODUCTION DESIGN CORRECTION

Prvý nezapečatený test skúsil použiť čerstvo vygenerovaný KMPC-113 raw ako
prerequisite KMPC-114. KMPC-113 obsahovo prešiel, ale jeho file SHA
`107DB1456E60DCAC4F64AC79F44D13C8641652E71D1C71EAEF5217C297C39144`
sa pre odlišný `runtime_seconds` správne nerovnal zmrazenému prerequisite
SHA `DD5B3075...3B533`. KMPC-114 smoke preto skončil exit `2` v
`static_hash_guard`, bez fyziky a bez raw KMPC-114.

Náprava balíka: REPRO obsahuje pôvodné hashované KMPC-113/114 prerequisites
a tri fázy sa reprodukujú v oddelených fresh copies. Field parity smie
odrátať runtime polia, ale generated raw sa nikdy nepoužije na obídenie
exact-hash checkpoint reťazca. Balík stále zostáva `DRAFT_NOT_DELIVERED`.

Prvá nezávislá KMPC-113 vetva následne prešla compile/help/smoke/official.
Prvé field porovnanie našlo okrem runtime iba absolútny fresh-copy root v
`frozen_B1_left_null_Bianchi.frozen_algebra_source`; relatívny source suffix
bol identický. Pred sealom sa preto povoľuje presne táto jediná root-prefix
normalizácia. Iné path pole alebo vedecká hodnota sa nesmie odrátať.

## 2026-07-19 — SEALED_READY_FOR_EXTERNAL_AUDIT

Balík má `75` source/copy manifest riadkov a `34` runtime-map riadkov.
Kompaktnosť je zámerná: živý projekt nepridal nový base modul a package
obsahuje iba úplný import/runtime closure troch malých runnerov. Draft
preflight po náprave reprodukčného dizajnu prešiel `463/463`.

Izolované behaviorálne kontroly prešli:

- negatívna vetva bez KMPC-053 NID prerequisite skončila v
  `static_hash_guard`, exit `2` za `1.648 s`, bez fyziky a bez success raw;
- KMPC-113 vetva: compile/help/smoke/official exit `0` za
  `0.150/1.300/1.020/3.750 s`; generated raw SHA
  `F983093721FE4A536623A0182ECFE951F063A80EFCDEB7B5257F6C816528640F`;
- KMPC-114 vetva: compile/help/smoke/official exit `0` za
  `0.130/1.340/0.930/2.810 s`; generated raw SHA
  `82B420921BEB064B84143008157D93E82FA9B98FE994E0B1CB0B1AF0736D0D02`;
- KMPC-115 vetva: compile/help/smoke/official exit `0` za
  `0.120/1.420/1.260/2.750 s`; generated raw SHA
  `9E541CB6B0E1B84C9C2604A38A8896FB4E083AEA77B2AA4277B8F538D5A83376`;
- všetky tri generated rawy majú field parity s Evidence 004/006/008 po
  odrátaní iba `runtime_seconds` a normalizácii jediného deklarovaného
  `frozen_algebra_source` root prefixu;
- kandidáti sú presne REVIEW support extension, checkpoint-only bez verdictu
  a scoped PASS v predregistrovanom poradí.

Generated raw jednej vetvy nebol použitý ako prerequisite inej vetvy.
Všetky dočasné fresh-copy adresáre boli pred final preflightom bezpečne
odstránené. Od tohto seal bodu sú evidence, runtime strom, manifesty,
control docs a response template immutable; oprava vyžaduje nový package ID.
