# KMPC-088 — BI/k=.15 Einstein_0i[7] coefficient attribution: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`

## Otázka

KMPC-087 vylúčil solve, holdout-assembly aj driver-assembly roundoff, ale
upstream M1, F0 a background generátory ostali binary64. KMPC-088 nemení
žiadny koeficient. Má iba zistiť, z ktorých presných konvolučných členov sa
skladá residual `Einstein_0i[7]` a ktoré upstream vlastníctvo musí byť
auditované ako prvé.

## Zmrazený rozsah

- iba `BI`, `k=0.15 Mpc^-1`, nominal, accepted `[0,5]`, audit `[0,7]`;
- identické source hashes, rovnice, 80 dps, support, prahy, vstupy a
  ekvilibrovaný exact-driver solve ako KMPC-087;
- holdout ostáva mimo solve; nepridá sa žiadny riadok ani korekcia;
- KMPC-087 raw neobsahuje 104-prvkový exact-driver vektor, preto sa
  deterministicky zopakuje rovnaký baseline HP solve a jeden exact-driver
  HP solve; nový solve sa nesmie interpretovať ako nový fyzikálny variant;
- jediný nový fyzikálno-diagnostický payload je riadok
  `Einstein_0i[7] = eta_x - momentum`;
- `eta_x` sa označí ako exact-driver/M3 príspevok;
- pre `gamma`, `fs`, `b`, `c` sa osobitne exportuje každé
  `background_standard[i] * U_fractional[j]` ako direct exact-driver/M3 a
  každé `background_fractional[i] * U_standard[j]` ako upstream
  background×M1;
- pre fuel sa druhá trieda označí background×F0; klasifikácia vychádza z
  kombinovaného state handoffu M1 + `_solve_fuel_zero` pred M3;
- každý term obsahuje mocniny `i,j`, oba koeficienty, faktor rovnice,
  znamienko, signed contribution a absolútnu veľkosť pri `i+j=7`;
- exportuje sa subtotal podľa druhu a species, fyzický súčet absolútnych
  termov, osobitne affine norm `abs(upstream constant subtotal) + sum(abs
  exact-driver terms)`, cancellation factor, poradie dominantných členov a
  exact reconstruction rozdiel voči KMPC-087 residualu;
- žiadny term sa nenuluje, nezaokrúhľuje, nefitne ani nepoužije na zmenu
  prahu.

## Brány

1. exact source/prerequisite hashe a BI/k/support identita;
2. rovnaké driver/holdout fingerprints a rovnaký KMPC-087 residual v rámci
   80-dps identickej aritmetiky;
3. presne dva HP solve celkom a `rows_added_to_driver_solve=0`;
4. každý nenulový konvolučný term je zaradený presne raz;
5. signed súčet termov rekonštruuje residual s absolútnou chybou `<=1e-70`;
6. zoskupený affine norm rekonštruuje uložený holdout norm s chybou
   `<=1e-70`; fyzický absolútny súčet ostáva osobitnou cancellation
   diagnostikou a nesmie sa s affine normom zameniť;
7. owner restore, compile/help/smoke, native JSON a immutable output.

## Zmrazená implementácia pred prvým spustením Pythonu

- attribution modul:
  `4AB2E440219E81B4F8E360BEA76693BF10534FB177FC3D74AB022CCD5933E96F`;
- runner 332:
  `39978AB9472EB6CA4D4C26C65998F56547CBF61D14A4192D7D79696B4975E355`;
- atomický harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- high-precision harness:
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `34/34` source/prerequisite hashov sedelo; všetkých
  `37` dlhých hash literálov malo presne 64 hex znakov.

Po freeze sa modul ani runner pred official behom nemenia.

## Predregistrované interpretácie

- všetky brány prejdú:
  `REVIEW_C2_BI_K0p15_UPSTREAM_ATTRIBUTION_COMPLETE`;
- identita alebo reconstruction neprejde:
  `TECHNICAL_ERROR / NO_PHYSICS_VERDICT`.

Aj úspešný ledger iba určí ďalší minimálny precision boundary. Najväčší
absolútny term sám nedokazuje pôvod chyby, pretože riadok môže byť silne
cancelačný. Autoritatívny stav ostáva do interného auditu C2 `5/10`, K4
`60/100`; release/Zenodo/prediction trigger `NONE`.
