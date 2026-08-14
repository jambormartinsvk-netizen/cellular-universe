# EA-037 — KMPC-131 C3 NIV T2 runtime closure

**Stav:** `SEALED_READY_FOR_EXTERNAL_T2_AUDIT`  
**Target tier:** `T2_REPRODUCIBLE_CALCULATION` pre nezmenený KMPC-131
`NIV/k=0.15`  
**Autorita:** hlavný posudok EA-036 určuje výlučne opravný scope  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov/interný orchestrátor:** Codex (OpenAI)  
**LIVE_FILES_CHANGED_FOR_PHYSICS:** `0`; runner, base, rovnice, prahy a raw
sú exact kópie  
**AUDIT_PACKAGE_COPIES:** `30` manifestových kópií + `7` controls + `1`
response šablóna; spolu `38 < 40`

## Presná otázka

Odstraňuje tento versioned opravný balík presne nálezy EA-036 F-001 až
F-003 tak, že:

1. official KMPC-131 NIV/k=.15 vetva je self-contained a dobehne bez
   odchýlky s `exit 0`, technicky úplným generated rawom a rovnakým REVIEW;
2. runtime closure obsahuje runner, `20` transitive importov, dva JSON
   vstupy a oba hardcoded exact-hash vstupy script 88/source-map 26;
3. generated raw je field-identický s reference `005` po normalizácii iba
   šiestich presne pomenovaných wall-time hodnôt a absolútneho koreňa jednej
   provenance cesty pri zachovanom relatívnom suffixe a source SHA-256;
4. R6 preflight odhalí vynechanie ktoréhokoľvek z dvoch nových hardcoded
   vstupov ešte pred tvrdením T2 pripravenosti;
5. oprava nemení fyziku, REVIEW, NIV `7/9`, C3 `43/45` ani K4 `60/100`?

## Poradie čítania

1. `EVIDENCE/001__EA036_EXTERNAL_AUDIT.md` a nálezy F-001 až F-003;
2. `EVIDENCE/002__EA036_MAIN_ASSESSMENT.md`;
3. preregistrácia `003`, interný audit `004` a reference raw `005`;
4. manifest, runtime mapa a single-copy `REPRO/`;
5. reprodukčné pokyny a package history.

## Tier hranica

T2 vznikne iba po R6 preflighte, fresh compile/help/smoke/official bez
odchýlky, corrected field parity a dvoch negatívnych official guardoch pre
script 88 a source-map 26. Forenzné čítanie reference bez generated rawu je
iba T1. T3 ani druhý equation builder sa netvrdí.

## Autorita

EA-037 opravuje auditnú dodávku, nie vedecký výsledok. Externý posudok
nemôže sám zmeniť REVIEW na PASS/STOP ani otvoriť refinement. Autoritatívne
spracovanie patrí hlavnému orchestrátorovi.

## Nonclaims

- Nijaký source, rovnica, support, depth, prah ani nominal autorita sa
  nemení.
- Balík nespúšťa ani nepredregistruje same-matrix refinement.
- T2 reprodukcia existujúceho REVIEW nepridáva logický PASS.
- Prediction table, release, Zenodo a K4 score sa nemenia.
