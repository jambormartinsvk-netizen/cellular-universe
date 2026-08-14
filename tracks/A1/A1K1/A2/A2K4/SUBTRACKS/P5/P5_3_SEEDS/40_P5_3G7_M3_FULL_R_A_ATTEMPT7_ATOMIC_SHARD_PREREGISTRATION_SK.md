# P5.3g7-M3-FULL/R-A — pokus 7/10, predregistrácia atomických shardov

**Dátum:** 2026-07-16  
**Run ID:** `KMPC-028`  
**Route:** `A1-K1 -> A2-K4 -> P5 -> P5.3g7-M3-FULL/R-A`  
**Stav:** `ATTEMPT_7_PREREGISTERED / NOT_RUN`  
**Dôvod:** PF-068; pokus 6 zoskupil 18 solve blokov do jedného mode procesu  
**Fyzikálny dopad zmeny:** žiadny; iba granularita procesu  
**Hĺbka:** bez zmeny `60/100`

## 1. Čo sa mení a čo sa nesmie zmeniť

Jeden Python proces teraz vykoná presne jeden atóm
`mode × k × variant`, ale vnútri stále skutočne vyrieši primary aj `J+2`
F0/M3 systém a všetky jeho holdouty. Namiesto jedného AD procesu s 18
solve blokmi vznikne deväť AD procesov s dvoma F0 a dvoma M3 solve blokmi.

Nesmú sa meniť:

- rovnice, tlak PF-063, state/driver/holdout ani gauge;
- `rcond`, rank, driver, holdout, truncation a background prahy;
- supports, `z` plochy, tri dynamické `k` ani nominal/gamma0/af0 význam;
- frozen fyzikálny shared modul
  `full_ra_m3_seed.py`, SHA-256
  `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2`;
- conditional `Phi1 M3-TCA0` scope a všetky obmedzenia dokumentu 37.

Nový technický wrapper smie iba zavolať frozen interné solve funkcie pre
jeden atóm, pridať presný kontext chyby a pripraviť atomický JSON. Runner
272 nesmie obsahovať rovnice.

## 2. Povinné procesy a limity

Pred dátovými atómami prebehne jeden `py_compile` wrappera a runnera a
jeden `--help`. Prvý atóm `AD/k=0.05/nominal` je sentinel a zároveň platný
člen finálnej množiny; osobitný duplicitný smoke sa nevytvára.

Každý atóm má interný limit `4.8 s` a vonkajší limit `10 s`. Agregátor má
rovnaké limity, ale nesmie riešiť novú maticu. Celý balík je jeden technický
pokus `7/10`, nie 45 pokusov.

## 3. Úplná matica 45 atómov

Pre každý z módov `AD, CDI, BI, NID, NIV` sa povinne spustí kartézsky
súčin:

```text
k = 0.005, 0.05, 0.15 Mpc^-1
variant = NOMINAL, GAMMA0, AF0
```

Immutable názov každého atómu je

```text
RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_{MODE}_K{K_TOKEN}_{VARIANT}.json
K_TOKEN = 0p005 | 0p05 | 0p15
```

Tým sú jednoznačne predregistrované všetky názvy, napríklad
`..._AD_K0p005_NOMINAL.json`, `..._NID_K0p05_GAMMA0.json` a
`..._NIV_K0p15_AF0.json`. Finálny agregát je
`RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOMIC_ATTEMPT7.json`.

CLI voľba a hodnota poľa `variant` v JSON sú lowercase
`nominal|gamma0|af0`; iba token immutable názvu súboru je uppercase
`NOMINAL|GAMMA0|AF0`. Toto je formátovacia konvencia, nie nový variant.

Poradie vykonania je fail-closed: najprv samostatný sentinel
`AD/k=0.05/nominal`, ktorý sa už neopakuje. Až po jeho úspechu sa spustí
zvyšných 44 atómov v poradí zmrazenom v execution ledgeri; pri prvom
nenulovom exit code sa balík zastaví a agregátor sa nespustí.

## 4. Očakávanie jedného atómu

Pred každým atómom očakávame:

1. presný frozen source hash;
2. frozen B1 left-null/Bianchi reference PASS;
3. presný produkčný TCA0 weighted-Euler/Thomson bridge PASS;
4. actual state/driver/holdout contract PASS;
5. M1 accepted frozen helper PASS;
6. F0 primary/extended plný rank, driver a leading post-check PASS;
7. M3 primary/extended plný rank, driver, `00/0i` holdout, spectator-order
   a regularity PASS;
8. per-koeficientový `J/J+2` a per-state tail PASS;
9. variantová nulová brána PASS; power-law pomer zostáva diagnostic-only.

Atómový PASS nie je fyzikálny verdict módu ani K4. Atómový numerický REVIEW
sa zachová a zastaví balík bez automatickej smrti; invariantný fyzikálny
STOP stále vyžaduje nezávislú reprodukciu podľa dokumentu 37.

## 5. Povinný failure context

Každá zachytená výnimka po úspešnom CLI parsovaní, pokiaľ zostáva výsledkové
úložisko zapisovateľné, musí vytvoriť immutable JSON s:

```text
run_id, mode, k, variant, last_completed_phase,
error_type, error_message, traceback,
physics_verdict=NONE_TECHNICAL_FAILURE
```

Atómový failure názov má presný tvar

```text
RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_{MODE}_K{K_TOKEN}_{VARIANT}_TECHNICAL_FAILURE.json
```

Agregačný failure názov je

```text
RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_AGGREGATE_KNA_NA_TECHNICAL_FAILURE.json
```

Chyba samotného CLI pred úspešným parsovaním alebo chyba zápisu failure
JSON sa hlási iba exit code a stderr/stdout; nikdy sa neinterpretuje ako
fyzikálny ani numerický výsledok.

Ak timeout alebo technická chyba nastane v jedinom atóme, ďalšie atómy sa
nespúšťajú a pokus 7 sa uzavrie technicky. Už vytvorené atomické JSON sa
zachovajú, ale agregovaný fyzikálny výsledok nevznikne.

## 6. Agregátor

Agregátor musí fail-closed overiť:

- presne 45 očakávaných názvov a žiadny chýbajúci/extra atóm;
- run ID, mode, k, variant, frozen source hashe a prahy;
- presný interný limit `4.8 s`, `z` plochy a backgroundové `a` plochy;
- všetky atomické checks a PASS verdict;
- nominal-vs-af0 F0/M3 coefficient bridge pre každé `mode×k`;
- tri-k background spread a cross-mode background spread pri spoločnom
  `BACKGROUND_MAX_J=8` pre `D,H,rho_f,rho_ash` do `1e-12`;
- conditional S-C split do `1e-14`.

Agregátor nesmie dôverovať iba textu verdictu ani meniť prahy po výsledku.

## 7. Vopred zmrazené vetvy

### Technický PASS celého balíka

Všetkých 45 atómov a agregátor dobehnú; potom hlavný orchestrátor audituje
číselný obsah. Až ten môže udeliť scope-limited
`PASS_M3_TCA0_SEED_CONDITIONAL` alebo numerický/fyzikálny REVIEW.

### Technický FAIL

Compile, CLI, hash, timeout, serializácia, chýbajúci atóm alebo agregátor:

```text
ATTEMPT_7_TECHNICAL_FAILURE
PHYSICS_ATTEMPTS=0
K4 LIVE / 60/100
```

### Numerický alebo formulačný FAIL atómu

Atóm dobehne, ale rank/rezíduum/truncation/holdout neprejde. Výstup sa
zachová a balík sa zastaví. Hlavný orchestrátor musí najprv rozlíšiť
conditioning/truncation REVIEW od invariantného formulačného rozporu; text
`REVIEW` v atomickom JSON sám nezabíja koľaj.

## 8. Release hranica

Pokus 7 sám nemení predikčnú tabuľku ani Zenodo trigger:

```text
NO_NEW_TRIGGER
EXISTING_PT1_REMAINS_OPEN
PT2_NOT_ESTABLISHED
```

## 9. Statický audit a hash freeze

Tri nezávislé read-only kontroly pred prvým Python procesom overili fyzikálny
scope, matematickú agregáciu a dokumentačno-release hranicu. Pred freeze boli
opravené iba riadiace medzery: neautoritatívny agregovaný status, úplný frozen
scope, kryptografické zviazanie atómov s wrapperom, primary aj extended F0/M3
bridge a exact schema/surface/runtime kontroly. Fyzikálny modul ani jeho rovnice
sa nemenili.

| artefakt | frozen SHA-256 |
|---|---|
| `full_ra_m3_seed.py` | `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2` |
| `full_ra_m3_seed_attempt7_atomic.py` | `977082FF118645F8A7CD024EE6AE411D0F8995DA6F00552C0B53F19B520623F9` |
| runner `272/KMPC-028` | `65AD56720AD06B32BE0EC54C2924491F1D8D9DB1C84E04015E56521B8FF8813D` |

**Stav po freeze:** `ATTEMPT_7_FROZEN_READY / NOT_RUN`; counter zostáva
`6/10`, kým sa nespustí prvý Python proces.
