# Scope — KMPC-047 NID C1 primary/extended

- Package ID: `EA-20260718-006-KMPC047-NID-C1`
- Route: `A1-K1 / A2-K4 / P5/P5.3g7 / GLOBAL_C1 / NID`
- Theory author: **Martin Jambor**
- Script creator: **Codex (OpenAI)**
- Audit mode: independent external reproduction and result assessment
- Package state: `SEALED_READY_FOR_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový `PASS/REVIEW/STOP` nemení

## Presná otázka

1. Prejde priložený official runner bez obídenia guardov a reprodukuje
   `core_pass=true`, `common_coefficient_pass=true`, combined-`R_fs` PASS a
   `pure_tail_pass=false`?
2. Potvrdzuje nezávislé čítanie primárneho kódu, že NID používa primary
   `[0,3]`, extended `[0,5]`, leading `j=0`, common powers `0…3` a
   cancellation-safe envelope tail iba `4,5`?
3. Potvrdzuje M1 seed combined-`R_fs` kompenzáciu, nie chybné použitie
   samotného `R_nu`?
4. Je projektový záver `REVIEW_NID_C1_SUPPORT_EXTENSION_REQUIRED` primeraný
   a bez neoprávneného fyzikálneho STOP alebo zvýšenia skóre?

## Poradie čítania

1. `EVIDENCE/001–002`: auditný protokol a frozen support kontrakt.
2. `EVIDENCE/003–004`: predregistrácia/execution a autoritatívny výsledok.
3. `EVIDENCE/005`: reference raw JSON.
4. `EVIDENCE/006–007`: official runner a NID base.
5. `EVIDENCE/008`: Python error ledger a známe preventívne pravidlá.
6. `04_RUNTIME_DEPENDENCY_MAP.tsv`: úplný runtime closure.
7. `03_REPRODUCTION_AND_EXPECTATIONS.md`: presné príkazy a očakávania.

## Zmrazené kritériá

```text
identity                 = NID / k=0.05 Mpc^-1 / nominal
primary -> extended      = [0,3] -> [0,5]
leading_j                = 0
common powers            = 0..3
added-tail powers        = 4,5
z surfaces               = 1e-4, 1e-2
common relative          = 1e-8
tail relative            = 1e-6
absolute norm/tolerance  = 1e-12 / 1e-12
```

Reference result: core, common a combined-`R_fs` prešli. Tail na `z=.01`
zlyhal s worst F0 `1.8692725e-2` (`U_f`) a worst M3 `4.3921947e-2`
(`U_f`). Prahy sa po výsledku nemenia.

## Nonclaims

Balík nie je T3; používa rovnaký equation builder. Neuzatvára NID support
`[0,5]`, NIV, iné `k`/varianty, S-M, nekonečný rad, plnú hierarchiu,
finite opacity, ODE/P5.4, G8/G9, CLASS, CMB, BBN ani `S8/H0`.

```text
SCORE_EFFECT=NONE
PREDICTION_TABLE_EFFECT=NONE
RELEASE_TRIGGER=NONE
ZENODO_TRIGGER=NONE
```

## Požadovaný výstup

Auditor vyplní priloženú response template: manifest, prostredie, presné
príkazy, exit code, wall time, generated JSON SHA-256, tag dôkazu pri každom
hlavnom tvrdení, nonclaims a oddelený package-tier versus physics-verdict
dopad.

