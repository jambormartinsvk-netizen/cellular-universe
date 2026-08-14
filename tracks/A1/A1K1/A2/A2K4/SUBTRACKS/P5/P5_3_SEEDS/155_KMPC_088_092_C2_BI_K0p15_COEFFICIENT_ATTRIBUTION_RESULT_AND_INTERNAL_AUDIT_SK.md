# KMPC-088 až KMPC-092 — BI/k=.15 coefficient attribution: výsledok a interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov a interný audítor:** Codex (OpenAI)  
**Stav:** `INTERNALLY_AUDITED / VALID_DIAGNOSTIC_REVIEW`  
**Autoritatívny výsledok:** `REVIEW_C2_BI_K0p15_UPSTREAM_ATTRIBUTION_COMPLETE`

## Dôkazová identita

- frozen predregistrácia KMPC-088: `E21C1E887E4AB3275A7582497FFD2D84A3741D4E8D85C03B0FCBA2F5622F453A`;
- technické successor predregistrácie KMPC-089 až 092:
  `5A06D995...5DEE`, `57D8AF97...4300`, `0C724039...1BFE`,
  `52A07F64...3B35`;
- runner 336: `E67BD2D15FACD3F23D11F9CAA39D68FABBDEB7D95234F11895C8CE0A46647677`;
- V5 modul: `DDBF6EB49DA5FC46CBDB82694AEBD19A9C43EF0233973525D8BEE4035EC662D8`;
- immutable raw KMPC-092:
  `73C3F00B7969291C7EF89E3FEAB56591D0FDEB8A1D65B0D2050B88360D300606`;
- term ledger má `73` členov a SHA fingerprint
  `9BB2F02965DD2E9215EBC89129EB24D228AABCB8EFCD6933BDFA54D29825B5EA`;
- compile, help, behaviorálny smoke a official beh KMPC-092 prešli; všetkých
  `40/40` deklarovaných source/prerequisite hashov sedelo pred prvým behom.

## Technická línia bez fyzikálneho verdiktu

| Balík | Incident | Stav |
|---|---|---|
| KMPC-088 | PF-092: `1e-70` gate ignoroval 50-cifernú serializáciu referencie | `DO_NOT_RUN_AUDIT_TECHNICAL` |
| KMPC-089 | PF-093: fixture porovnával hodnotu po opustení 80-dps contextu | `DO_NOT_RUN_AUDIT_TECHNICAL` |
| KMPC-090 | PF-094: ledger zmenil poradie binary64 produktu a exact bridge | `DO_NOT_RUN_AUDIT_TECHNICAL` |
| KMPC-091 | PF-095: nested owner checker použil mutable outer referenciu | `DO_NOT_RUN_AUDIT_TECHNICAL` |
| KMPC-092 | opravil iba owner expectation; matematika V1–V4 nezmenená | `VALID_DIAGNOSTIC_REVIEW` |

PF-092 až PF-095 sú implementačné chyby, nie fyzikálne výsledky. Úspešný
vecný KMPC-092 resetuje aktívny technický counter na `0/10`; úplná história
ostáva zachovaná.

## Výsledok atribúcie Einstein_0i[7]

| Veličina | Hodnota |
|---|---:|
| reconstructed residual | `-5.4970171428314830743e-17` |
| physical absolute term sum | `4.8965432763492801743e-8` |
| cancellation factor | `8.9076369040157e8` |
| exact-driver subtotal | `+7.0661910851206176294e-9` |
| upstream constant subtotal | `-7.0661911400907890577e-9` |
| fractional background × M1 | `-7.0481888048771900027e-9` (`34` členov) |
| fractional background × F0 | `-1.8002335213599055018e-11` (`8` členov) |
| standard background × exact M3 | `+6.0747803075947824819e-10` (`30` členov) |
| exact M3 eta term | `+6.4587130543611393812e-9` (`1` člen) |

Rekonštrukcia rezídua sa od immutable referencie líši iba
`2.30e-67 < 2e-66`; rekonštrukcia affine normy iba
`4.41e-58 < 2e-57`. Holdout fingerprint sa zhoduje s KMPC-087, počet
holdout riadkov pridaných do solve je nula a počet high-precision solve je
presne dva.

Najväčšie jednotlivé členy sú:

1. `+7.842177643e-9`: `Ofs_fractional[0] × U_fs_standard[7]`;
2. `-7.613888957e-9`: `Ofs_fractional[2] × U_fs_standard[5]`;
3. `+6.458713054e-9`: exact-driver `eta_x`;
4. `-6.124939927e-9`: `Ofs_fractional[1] × U_fs_standard[6]`;
5. `-4.213056641e-9`: `Og_fractional[1] × U_gamma_standard[6]`.

## Interný audit a interpretácia

1. Ledger rozkladá presne frozen KMPC-087 rovnicu
   `eta_x - 2 Og U_gamma - 2 Ofs U_fs - 1.5 Ob U_b - 1.5 Oc U_c - 1.5 delta Of U_f`.
   Každý konvolučný člen má súčet mocnín `7`; owner a species registre sú úplné.
2. Správne poradie fuel faktora je binary64 `1.5*delta` a až potom exact
   bridge. Oprava zmenila osem fuel členov, žiadny non-fuel člen, a nemení
   frozen rovnicu ani fyzikálny prah.
3. F0/fuel je malý príspevok: približne `0.255 %` veľkosti dominantného
   upstream subtotalu. Nemá preto prioritu pre ďalší drahý rebuild.
4. Dominantný owner `BACKGROUND_FRACTIONAL_X_M1` je bilineárny. Samotná
   atribúcia nevie rozhodnúť, či rozhodujúce binary64 obmedzenie vzniká v
   generátore fractional backgroundu alebo v štandardnom M1 stave.
5. KMPC-083/086/087 už vylúčili solve, holdout assembly aj driver assembly
   roundoff. Ďalší test musí izolovať jednu stranu dominantného bilineárneho
   súčinu, nie meniť prah alebo pridať holdout do solve.

Toto nie je PASS BI/k=.15, dôkaz chybnej rovnice ani fyzikálny STOP.
C2 zostáva `5/10 PASS`, P5 `3.5/6`, K4 `LIVE / 60/100`. Release, Zenodo a
prediction-table trigger sú `NONE`.

## Ďalší predregistrovaný krok

Zdrojový audit musí najprv potvrdiť, či živá C2 pipeline používa raw
float64 M1 solve alebo už KMPC-037 numericky refined stav. Ak používa raw
solve, najmenší informačný test je high-precision reassembly a solve iba
štandardného M1 systému pri nezmenenom exact-bridged backgroundu; nový M1
stav sa vloží do inak nezmeneného F0/M3/holdout pipeline. Ak je M1 už
refined, priorita sa presunie na high-precision fractional-background
generator. V oboch prípadoch ostávajú rovnice, support, prahy a non-fit
holdout zmrazené.
