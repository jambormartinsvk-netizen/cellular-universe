# KMPC-132 a C3 AD mód — výsledok a interný audit

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PASS_C3_AD_MODE_9_OF_9 / GLOBAL_C3_21_OF_45`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov a interný auditor:** Codex (OpenAI)  
**Autoritatívny dopad:** K4 `60/100`, P5 `3.5/6`, score/release/Zenodo bez
zmeny.

## 1. Záver

Celý AD mód podmieneného C3 kontraktu prešiel: tri historické nominal atómy
a šesť nulových atómov `gamma0/af0` tvoria `9/9 PASS`.

KMPC-132 potvrdil, že REVIEW z KMPC-131 na `AD/.05` nespôsobila chyba
rovníc, nulového limitu ani zaokrúhlenie. Pri najbližšom predregistrovanom
supporte `[0,4]→[0,6]` klesol najhorší tail z približne `3.2817e-3` na
`4.6829e-8 < 1e-6`. Hlbší nominal checkpoint sa zhodol s historickým
nominalom na spoločnom supporte a oba nulové varianty prešli.

Následný už predregistrovaný `AD/.15` receipt prešiel bez ďalšej zmeny
supportu. Neexistuje fyzikálny STOP; zároveň conditional seed coverage sama
neuzatvára fyzickú S-M mikrofyziku a nezvyšuje K4 score.

## 2. Immutable rawy

| Beh | Kandidát | SHA-256 |
|---|---|---|
| KMPC-131 AD/.005 | `PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY` | `D3FB5710390B3395212067B8BC968E48AEBA04AF9A0D38A4313195A39C6B3DAA` |
| KMPC-131 AD/.05, pôvodný support | `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED` | `1D239D5C94D24C4FD52AC094043A505D41CBDADCA62E6E98A9B2F76A9BAE76E1` |
| KMPC-132 AD/.05, `[0,4]→[0,6]` | `PASS_C3_AD_K0P05_ZERO_PAIR_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY` | `DCF6D7D957365FCDA127B1F0F5E27068625A3FB83DFDD1E367E1A052158D8D82` |
| KMPC-131 AD/.15 | `PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY` | `FFEB802BADF663F812023914C1B8C34AA150070A763BBF123E41A55E7BFE4C47` |

## 3. KMPC-132 technický a vedecký audit

- source freeze base/runner:
  `3A47EF9CFAC68E100FCB7A03AD9CD478C99C5BB74DA5210F7844AE619E94F867` /
  `A9E8FD5E6DC0D8208DDF0C15500A8E0B81199F60E63AAF8425551F1E4847092C`;
- compile/help/smoke/official: exit `0/0/0/0`; smoke `6/6`,
  `physics_executed=false`;
- šesť workerov skončilo v `1.969–2.922 s < 4.8 s`; parent nemal solver
  calls a zapísal jeden immutable raw;
- successor contract, source parity, B1 left-null/Bianchi, production TCA0,
  M1, combined-R_fs, accepted/audit solve a S-C0: všetko PASS;
- nominal checkpoint lineage PASS; najhorší old-audit `[0,4]` →
  new-accepted `[0,4]` relatívny rozdiel bol `7.1014e-12 < 1e-8`;
- `af0` nominal bridges na accepted aj audit supporte mali maximálny rozdiel
  `0`;
- oba nulové limity, background, common bridges a taily prešli.

Najhoršie tail hodnoty na `z=.01`:

| vetva | F0 | M3 | limit |
|---|---:|---:|---:|
| deeper nominal checkpoint | `2.01747e-8` | `4.68286e-8` | `1e-6` |
| gamma0 | `2.01744e-8` | `4.68288e-8` | `1e-6` |
| af0 | `2.01747e-8` | `4.68286e-8` | `1e-6` |

## 4. AD/.15 audit

Nezmenený KMPC-131 base/runner mal source hashe
`7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` /
`45EB5E641FB9C4F5868A4754E84A2518C1DA0D64475520027B73EAE1A6AEBBB2`.
Smoke bol `4/4` bez fyziky a official skončil exit `0`.

| variant | F0 worst tail `.01` | M3 worst tail `.01` | výsledok |
|---|---:|---:|---|
| gamma0 | `9.14144e-9` | `1.51953e-8` | PASS |
| af0 | `9.14145e-9` | `1.51953e-8` | PASS |

Worker parity, core, common, background, null limit, B1/TCA0 a `af0` bridge
boli PASS. Najpomalší worker trval `2.766 s < 4.8 s`.

## 5. Autoritatívne účtovanie

- AD/.005: nominal + gamma0 + af0 = `3/3`;
- AD/.05: nominal + gamma0 + af0 = `3/3`;
- AD/.15: nominal + gamma0 + af0 = `3/3`;
- AD C3 mód: `9/9 PASS`;
- globálne C3: historické nominal `15/15` + nulové varianty `6/30`, spolu
  `21/45 PASS`;
- C3 aggregate zostáva zakázaný, kým nebude `45/45`;
- K4 ostáva `60/100`, pretože fyzická S-M para a ďalšie brány ešte nie sú
  uzavreté.

## 6. Ďalší zmrazený krok

Pokračovať prvým párom módu CDI: `CDI/k=.005/gamma0+af0`, accepted
`[0,7]`, audit `[0,9]`, M1 depth `9`, nominal autorita KMPC-073. Rovnice,
plochy, prahy aj štvor-shardová architektúra KMPC-131 zostávajú nezmenené.
Najprv smoke, potom jediný official receipt. Pri REVIEW sa uplatní fail-fast
a ďalšie CDI k sa nespustí bez vyhodnotenia.

## 7. R5 súborová a auditná kontrola

Od zapečatenia EA-030 vzniklo pre dva výpočtové atómy presne `6` nových live
artefaktov: predregistrácia 205, jeden base, jeden runner, dva rawy a tento
spoločný audit. To je priemer `3` na atóm; nevznikol technický failure ani
nový error-ledger zápis. Centrálne registre sa aktualizujú jedným batchom až
teraz pri mode closure.

EA-031 má byť delta capsule: T2 reprodukcia KMPC-132, immutable T1 dôkaz
AD/.15 a explicitný chain na EA-030 pre staršiu `.005/.05` líniu. Rozpočet
je najviac `32` jedinečných source/runtime/evidence kópií + `7` controls +
`1` response = presne `40`; bez duplicitných fyzických kópií.
