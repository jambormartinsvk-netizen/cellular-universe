# EA-047-R1 — opravený parity contract

## Parent evidence

Parent package manifest:
`646D81CE21B6CF5CCC3E3125B3DFC10DFF3E54ECE947272C3892997DD459F6B7`.
Parent external response:
`2E6316559D687F545286DD4442489BD177D94D61006B61C0EEF10B5E8CC92E6D`.

Parent T2 reprodukoval 9 final cells a fresh hash chain. Táto revízia nemení
žiadny vedecký bajt ani príkaz a neautorizuje nový Python.

## Opravená hierarchia kontrol

### 1. Fresh-chain integrity — exact, bez normalizácie

Pri fresh reprodukcii musí vždy platiť:

- A.`reference_stage_sha256 = SHA256(fresh reference file)`;
- B/C.`reference_stage_sha256 = SHA256(fresh reference file)`;
- B.`predecessor_segment_sha256 = SHA256(fresh A file)`;
- C.`predecessor_segment_sha256 = SHA256(fresh B file)`;
- aggregate reference/model SHA sa rovnajú fresh reference/C file hashom.

Tieto identity sú exact a nesmú sa normalizovať ani nahradiť accepted hashmi.

### 2. Accepted-copy parity — presný field contract

- direct cells: povolený rozdiel iba top-level `runtime_seconds`;
- reference: povolený rozdiel iba top-level `runtime_seconds`;
- A: povolené rozdiely iba top-level `runtime_seconds` a
  `reference_stage_sha256`;
- B/C: povolené rozdiely iba top-level `runtime_seconds`,
  `reference_stage_sha256` a `predecessor_segment_sha256`;
- final aggregate cells: exact byte parity je najsilnejší výsledok; minimálne
  exact recursive parity po odstránení iba top-level `runtime_seconds`.

Po odobratí presne uvedených pathov musí byť recursive diff prázdny. Žiadne
fyzikálne číslo, state, bracket, iteration count, guard, threshold, identity,
schema, path, frozen input, comparator alebo verdict nie je povolená výnimka.

### 3. Prečo to nie je oslabenie

Dynamické provenance SHA sa nekontrolujú proti historickej hodnote, ale voči
skutočnému fresh súboru, ktorý označujú. To je silnejšia relevantná
integrity kontrola. Stabilný vedecký obsah sa naďalej kontroluje exact voči
accepted evidence.

## Očakávaný P0 výsledok

`PASS_P0_CONTROL_REPAIR` znamená iba, že rozpor control textu je odstránený
pri byte-identických parent evidence. Parent výsledok ostáva:

```text
DeltaNeff=0       H0=65.79213819466531  S8=0.8856095825403126
DeltaNeff=0.02675 H0=66.08320294879377  S8=0.8800254370658636
DeltaNeff=0.0535  H0=66.37433224357665  S8=0.874499891729803
```

Tieto body sú conditional legacy diagnostics, nie likelihood, interval,
fit ani tvrdé v3.18 predikcie.

