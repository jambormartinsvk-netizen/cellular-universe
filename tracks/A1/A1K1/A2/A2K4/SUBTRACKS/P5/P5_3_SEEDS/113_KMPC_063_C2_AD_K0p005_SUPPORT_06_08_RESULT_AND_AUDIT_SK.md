# KMPC-063 — C2 AD/k=.005 support `[0,6]→[0,8]`: výsledok a audit

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C2 → AD/k=.005/nominal`  
**Autoritatívny stav:** `PASS_C2_AD_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY`  
**Skóre:** bez zmeny, K4 `60/100`, P5 `3.5/6`

## Immutable výsledok

`scripts/results/k_mpc_005/RUN_KMPC_063_P5_3G7_C2_AD_K0p005_SUPPORT_06_08.json`  
SHA-256 `CB0CEA5DD92BF85F0F0066FAD8DE77D5F8247B02B864FACF92FA374E0FBC85BD`.

Preflight compile/help/smoke prešiel. Oficiálny proces skončil za 2.484 s
vnútri limitu 4.8 s a vytvoril jediný nový raw. M1 depth 8 mal rank
`109/109`, driver `6.30315e-14` a holdout `2.58854e-13`; M1 prešiel.
Core, S-C0, common a background prešli. Najhorší background rozdiel bol
`1.15195e-16`.

| Vetva | `z=1e-4` | `z=.01` | Prah | Stav |
|---|---:|---:|---:|---|
| F0 tail `7,8` | `1.75163e-19` | `1.82700e-9` | `1e-6` | PASS |
| M3 tail `7,8` | `4.83170e-19` | `5.07464e-9` | `1e-6` | PASS |

Najhoršie relatívne stavy na `z=.01` boli `delta_f` pre F0 a `eta` pre
M3. Common `0…6` ostal stabilný: F0 `7.52810e-15`, M3 `7.28528e-13`,
oboje pod `1e-8`.

## Význam a hranice tvrdenia

Candidate support `[0,6]` je pre jediný atóm AD/k=.005/nominal adequate:
príspevok nových rádov `7,8` je na oboch zmrazených plochách pod tail
prahom. Toto uzatvára prvý z desiatich C2 atómov. Nepotvrdzuje ostatné
`k`, módy, varianty, C3, S-M, plnú hierarchiu, ODE ani dáta a nie je to
fyzikálny verdikt celej P5/K4.

Support je atom-local. Preto sa `[0,6]` neprenesie na AD/k=.15. Ďalší
predregistrovaný atóm má začať pôvodným C1 supportom AD `[0,2]` voči audit
`[0,4]`, M1 depth 5, s nezmenenými prahmi. Ak zlyhá tail, otvorí vlastný
support ladder; žiadny correction vector sa neprenáša.

Release, Zenodo a prediction-table trigger: `NONE`.
