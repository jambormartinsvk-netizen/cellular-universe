# KMPC-139 — lokálny exact deadline-owner successor

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → BI/.15`  
**Stav:** `PREREGISTERED / SOURCE_HASH_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Autorita 45 s:** výslovná voľba používateľa  
**Technický predchodca:** KMPC-138 / PF-124

## 1. Jediná oprava

KMPC-138 už zmrazil správne vonkajšie limity, ale inherited KMPC-128
deadline factory odmietol exact child argument `45.0` ešte pred fyzikou.
KMPC-139 smie iba v procesnej role `--worker-exact-variant`:

1. uložiť pôvodný `scientific._make_deadline` owner;
2. dočasne nainštalovať lokálny factory, ktorý prijme iba presne `45.0 s`;
3. použiť monotonic deadline a pri prekročení fail-closed vyhodiť timeout;
4. po úspechu aj výnimke obnoviť pôvodného ownera;
5. pridať do payloadu checks `local_45s_owner_active` a
   `original_deadline_owner_restored`.

Coefficient child roly overlay nikdy neinštalujú a ostávajú pod frozen
KMPC-128 `≤4.8 s` guardom.

## 2. Nemenný kontrakt

Všetky vedecké a procesné položky KMPC-138 ostávajú nezmenené: identita,
supporty, checkpointy, 4+2 vlny, exact 80 dps `104×104`, holdout `16×104`,
rovnice, RHS, thresholdy, supersession scope, coefficient `4.8 s`, exact
`45 s`, parent `49 s`, vonkajší `50 s` a jeden immutable raw/receipt.

Frozen wrapper SHA-256:
`489ED57D2F874CAC60E7733050C7DB4E8D59AABAD197827965F6322B80515D0D`.

## 3. Smoke a hodnotenie

Exact smoke musí bez fyziky dokázať:

- inherited owner pred overlayom odmieta `45.0 s`;
- lokálny owner prijíma presne `45.0 s`;
- hodnotu odlišnú od `45.0 s` odmieta;
- po scope je inherited owner identity obnovená.

Official PASS/REVIEW/technical vetvenie je byte-semantic rovnaké ako v
KMPC-138. BI mód sa uzavrie až interným auditom.

## 4. R5 rozpočet

Nový base nevzniká. Tento technický successor pridáva jednu predregistráciu,
jeden runner a jeden raw; interný audit zostáva spoločný pre výslednú BI
closure.

## 5. Source freeze

| artefakt | SHA-256 |
|---|---|
| frozen KMPC-137 wrapper | `489ED57D2F874CAC60E7733050C7DB4E8D59AABAD197827965F6322B80515D0D` |
| runner 383 | `36C04196BAAE6B40188822B961B43655A550702D2886B2EE55B7DC96DE7610B4` |
