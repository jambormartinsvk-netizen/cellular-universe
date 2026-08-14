# EA-030 — KMPC-128 až 131, prvá C3 AD hranica

**Stav:** `SEALED_READY_FOR_EXTERNAL_AUDIT`  
**Target tier:** `T2_REPRODUCIBLE_CALCULATION`  
**Theory author:** Martin Jambor  
**Script creator/internal auditor:** Codex (OpenAI)  
**LIVE_FILES_CHANGED:** `20` pri uzavretí interného auditu 204  
**AUDIT_PACKAGE_COPIES:** `32` source/runtime kópií + `7` control súborov;
response šablóna je osobitný `1` súbor.

## Presná otázka

Je technická línia KMPC-128→131 auditovateľnou, rovnice nemenacou nápravou a
podporujú immutable rawy záver, že `AD/.005` nulový pár prešiel, kým
`AD/.05` má pri `[0,2]→[0,4]` iba tailový
`REVIEW_C3_SUPPORT_EXTENSION_REQUIRED` so všetkými netail a nulovými
bránami PASS?

## Poradie čítania

1. `EVIDENCE/001__KMPC128_C3_MATRIX_PREREG.md`;
2. `EVIDENCE/002__KMPC131_FOUR_SHARD_PREREG.md`;
3. `REPRO/scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_AD_K0p005_ZERO_VARIANT_PAIR.json`;
4. `REPRO/scripts/results/k_mpc_005/RUN_KMPC_131_P5_3G7_C3_AD_K0p05_ZERO_VARIANT_PAIR.json`;
5. `EVIDENCE/003__C3_AD_BOUNDARY_INTERNAL_AUDIT.md`;
6. reprodukčné pokyny a úplný runtime closure vrátane behaviorálne
   hashovaných zdrojov 88 a 26.

## Predregistrované hodnotenie

- `.005`: oba varianty musia mať core/common/tail/background/null PASS a
  `af0` nominal bridge PASS;
- `.05`: ak zlyhá iba tail pri nezmenenom `1e-6`, výsledok je REVIEW supportu,
  nie fyzikálny STOP ani null-limit FAIL;
- syntax, hash, schema, timeout alebo child-process chyba je iba technická;
- `.15` musí zostať NOT_RUN po `.05` fail-fast REVIEW.

## Nonclaims

Balík nepotvrdzuje plné AD C3, `45/45`, fyzickú `S-M` paru, finite opacity,
P5.4, G8/G9, CMB, `S8`, zmenu K4 score ani release trigger. Nepovoľuje
post-hoc zmenu supportu alebo prahu.

## Autorita

Externý audit je read-only odporúčanie. Projektový PASS/REVIEW/STOP môže
zapísať iba hlavný orchestrátor; aktuálne K4 ostáva `60/100`.
