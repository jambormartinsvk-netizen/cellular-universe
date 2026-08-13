# Reprodukcia EA-047

## Prostredie a limity

Zmrazené projektové prostredie: CPython `3.11.3`, NumPy `2.4.4`, SciPy
`1.17.1`. Na inom podporovanom prostredí označte výsledok ako cross-platform
diagnostiku. Každý Python proces má vonkajší limit `60 s`; official vetvy
majú vnútorný limit `45 s`, agregácie `5 s`. Jeden timeout sa nepredlžuje
post-hoc a je technický REVIEW, nie fyzikálny STOP.

## Fresh-copy postup

Skopírujte iba adresár `REPRO/` do novej dočasnej cesty. V kópii vytvorte
prázdny adresár `scripts/results/release_v318_h0_s8`; package originál a
`EVIDENCE/` nemeníte. Z koreňa fresh copy spustite samostatne:

```powershell
C:\Python311\python.exe -m py_compile scripts\baseScripts\release_v318_h0_s8_legacy_sensitivity_dev.py scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --help
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --self-test --max-runtime-seconds 45
```

DEV self-test musí prejsť `31/31`, ale nie je fyzikálny dôkaz. Potom
vygenerujte šesť priamych buniek, každý príkaz presne raz:

```powershell
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --official-cell null-n2000 --max-runtime-seconds 45
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --official-cell null-n4000 --max-runtime-seconds 45
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --official-cell half-n2000 --max-runtime-seconds 45
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --official-cell half-n4000 --max-runtime-seconds 45
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --official-cell full-n2000 --max-runtime-seconds 45
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --official-cell full-n4000 --max-runtime-seconds 45
```

Pre n=8000 najprv spustite reference stage. Vypočítajte SHA-256 generated
reference rawu a vložte ho bez inej zmeny do `{REF_SHA}`:

```powershell
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --official-n8000-reference --max-runtime-seconds 45
```

Pre každý shard `null`, `half`, `full` samostatne vykonajte A, spočítajte
`{A_SHA}`, vykonajte B, spočítajte `{B_SHA}`, vykonajte C, spočítajte
`{C_SHA}` a až potom aggregate:

```powershell
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --official-n8000-bisect-a {SHARD} --reference-sha256 {REF_SHA} --max-runtime-seconds 45
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --official-n8000-bisect-b {SHARD} --reference-sha256 {REF_SHA} --predecessor-sha256 {A_SHA} --max-runtime-seconds 45
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --official-n8000-bisect-c {SHARD} --reference-sha256 {REF_SHA} --predecessor-sha256 {B_SHA} --max-runtime-seconds 45
C:\Python311\python.exe scripts\393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py --official-n8000-aggregate {SHARD} --reference-sha256 {REF_SHA} --model-sha256 {C_SHA} --max-runtime-seconds 5
```

## Očakávané výsledky a exact parity

Všetky official príkazy majú exit code `0`. Deväť finálnych rawov musí mať
`PASS_GRID_CELL_INTRINSIC`; direct guardy `7/7`, n8000 null/half `9/9` a
n8000 full `11/11`. Pri rovnakom grid n musí byť non-Delta fingerprint
rovnaký pre všetky tri shardy.

Pred rekurzívnym exact diffom generated rawu voči príslušnému `EVIDENCE`
rawu odstráňte z oboch objektov výlučne top-level `runtime_seconds`. To isté
platí pre reference a A/B/C continuation rawy. Po tejto jedinej
normalizácii musí byť rozdiel prázdny. Fyzikálne čísla, identity, hashe,
guardy, paths, prahy ani vnorené polia sa normalizovať nesmú.

High-grid body musia byť:

```text
DeltaNeff=0       H0=65.79213819466531  S8=0.8856095825403126
DeltaNeff=0.02675 H0=66.08320294879377  S8=0.8800254370658636
DeltaNeff=0.0535  H0=66.37433224357665  S8=0.874499891729803
```

Každá vetva musí spĺňať `abs(H0_8000-H0_4000)<=0.005` a
`abs(S8_8000-S8_4000)<=0.0005`. Endpoint musí dať
`Delta H0=+0.582194048911333 km/s/Mpc` a
`Delta S8=-0.0111096908105096` v double aritmetike rawov.

## Negatívny guard

V osobitnej fresh copy pred `null-n2000` vytvorte sentinel presne na jeho
cieľovej ceste. Official príkaz musí skončiť nonzero pred výpočtom, sentinel
nesmie zmeniť a nesmie zostať temp súbor. Tento guard je technický a nemení
fyzikálny verdict.

## Odchýlky

Zmena source, SHA, threshold, output path/name, runtime limitu, obídenie CLI,
ručné vloženie prijatých continuation rawov do fresh result cesty alebo
volanie solvera priamo je `DECLARED_DEVIATION` a nedosahuje T2 deklarovanej
vetvy.
