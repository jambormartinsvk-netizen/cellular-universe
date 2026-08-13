# KMPC-131 až 133 — C3 CDI mode closure, interný audit

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PASS_C3_CDI_MODE_9_OF_9 / GLOBAL_C3_27_OF_45`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov a interný auditor:** Codex (OpenAI)  
**Autoritatívny dopad:** K4 `60/100`, P5 `3.5/6`, score/release/Zenodo bez
zmeny.

## 1. Záver

Celý CDI mód podmieneného C3 kontraktu prešiel `9/9`: tri historické nominal
atómy a šesť nulových atómov `gamma0/af0`.

CDI/.005 a CDI/.05 prešli priamo nezmeneným štvor-shardovým KMPC-131.
CDI/.15 malo pri prvom technicky úplnom receipte iba audit M3 driver
boundary; všetky ostatné brány prešli. Predregistrovaný KMPC-133 použil tri
korekcie na tej istej rank-104 matici a RHS. Driver klesol na približne
`1e-16`, kým tail zostal prakticky rovnaký. Ide o numerické uzavretie, nie
zmenu rovníc, supportu alebo prahu.

## 2. Immutable rawy

| Beh | Kandidát | SHA-256 |
|---|---|---|
| KMPC-131 CDI/.005 | `PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY` | `9E1BCC3D291858DE55E15A31246D33026CDD4B9774753304B8FC0BBA62BB3BA4` |
| KMPC-131 CDI/.05 | `PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY` | `DC38CD6C5E9EF15B0FB86878BF4125A431BBB04C537887874D1A38786F6F5A3F` |
| KMPC-131 CDI/.15 pre-refinement | `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED` | `A3D934512C5303AC22E4607CCB6D1FFF13A51972463D2D52A703953F477641B6` |
| KMPC-133 CDI/.15 refined | `PASS_C3_CDI_K0P15_ZERO_PAIR_SAME_MATRIX_REFINEMENT_CANDIDATE_ONLY` | `42BE1CAC74BC0BB879F7065B8B0FF36C0D1B8E382BC74537248DDAF02711717E` |

## 3. Priame CDI receipts

| k | support | gamma0 worst tail `.01` | af0 worst tail `.01` | výsledok |
|---:|---|---:|---:|---|
| .005 | `[0,7]→[0,9]` | `4.76773e-9` | `4.76772e-9` | PASS |
| .05 | `[0,5]→[0,7]` | `8.71681e-9` | `8.71681e-9` | PASS |
| .15 | `[0,5]→[0,7]` | `7.18373e-9` | `7.18373e-9` | pre-refinement core REVIEW |

Pri všetkých troch k prešli common, tail, background, nulové limity a `af0`
nominal bridges. `.15` REVIEW malo accepted solve PASS a audit holdout PASS;
jediný false core check bol `audit_solve` pre driver residual.

## 4. KMPC-133 audit

- source freeze base/runner:
  `96CD52283B9B992247FE79DD43903D15173560D73A3CF971B26F893BA743C092` /
  `878DC12A9065391817A0750B89AFEADC4236D488CDDFC3175FC14D54AA1E07B8`;
- compile/help/smoke/official: exit `0/0/0/0`; smoke `4/4`, bez fyziky;
- support `[0,5]→[0,7]`, M1 depth 7, rows/unknowns/rank `104/104/104`,
  `rcond`, matica, RHS a prahy bez zmeny;
- refinement: presne tri kroky, same-matrix-and-constant guard a selection
  rule PASS pri oboch variantoch;
- gamma0 driver `8.199227816e-10 → 1.056317952e-16`;
- af0 driver `3.844141885e-10 → 1.114992135e-16`;
- holdout, common, tail, S-C0, background, null a `af0` bridge ostali PASS;
- najhorší tail po refinement bol `7.183731831e-9`, teda numericky rovnaký
  ako pred refinement a hlboko pod `1e-6`;
- najpomalší worker `2.875 s < 4.8 s`, parent solver calls `0`.

## 5. Autoritatívne účtovanie

- CDI/.005: nominal + gamma0 + af0 = `3/3`;
- CDI/.05: nominal + gamma0 + af0 = `3/3`;
- CDI/.15: nominal + gamma0 + af0 = `3/3`;
- CDI C3 mód: `9/9 PASS`;
- globálne C3: nominal `15/15` + nulové varianty `12/30`, spolu
  `27/45 PASS`;
- aggregate zostáva zakázaný; K4 ostáva `60/100`, pretože conditional C3
  coverage sama neuzatvára fyzickú S-M mikrofyziku.

## 6. Ďalší zmrazený krok

Pokračovať prvým párom BI: `BI/k=.005/gamma0+af0`, accepted `[0,7]`, audit
`[0,9]`, M1 depth `9`, nominal autorita KMPC-078. Použiť nezmenený
KMPC-131 runner; najprv smoke, potom jediný official receipt. Pri REVIEW sa
uplatní fail-fast.

## 7. R5 súborová a auditná kontrola

Od EA-031 vzniklo pre štyri výpočtové atómy `8` live artefaktov: tri priame
rawy, predregistrácia 207, jeden overlay base, jeden runner, successor raw a
tento spoločný audit. Priemer je `2` artefakty na atóm; nevznikol technický
failure ani Python error-ledger zápis.

EA-032 má byť delta capsule s T2 reprodukciou KMPC-133 a transparentným
pre-refinement rawom. Staršie CDI/.005/.05 rawy sú v tomto dokumente viazané
presnou cestou a hashom, ale kvôli R5 single-copy limitu sa nekopíruje druhý
celý KMPC-131 runtime. Plán je `32` jedinečných source/runtime/evidence
kópií + `7` controls + `1` response = presne `40`.
