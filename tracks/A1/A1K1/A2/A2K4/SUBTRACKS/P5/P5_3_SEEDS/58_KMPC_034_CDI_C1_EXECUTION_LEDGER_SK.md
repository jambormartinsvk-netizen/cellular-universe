# KMPC-034 — CDI C1 execution ledger

**Stav:** `EXECUTED / MAIN VERDICT IN DOCUMENT 59`  
**Interný limit:** `4.8 s`; **vonkajší limit:** `10 s` na proces

## Očakávania pred procesmi

| Fáza | Proces | Očakávanie | PASS → | Odchýlka → | Stav |
|---:|---|---|---|---|---|
| 1 | `py_compile cdi_c1_coverage.py` | ticho, exit 0 | fáza 2 | technická chyba | `PASS / exit 0 / 0.5 s` |
| 2 | `py_compile runner 278` | ticho, exit 0 | fáza 3 | technická chyba | `PASS / exit 0 / 0.5 s` |
| 3 | `--help` | iba fixed CDI C1 CLI, exit 0 | fáza 4 | technická chyba | `PASS / exit 0 / 0.6 s` |
| 4 | `--smoke --max-runtime-seconds 4.8` | support/count derivation, S-C0 source hash a negatívny wrong-support fixture; pri PASS bez JSON | fáza 5 | technická chyba a failure JSON; audit zakázaný | `PASS / exit 0 / 1.1 s` |
| 5 | `--audit --max-runtime-seconds 4.8 --output ...` | immutable vecný JSON; core/tail výsledok podľa dokumentu 57 | tri read-only audity | failure JSON bez fyziky | `TECHNICAL_COMPLETE / exit 0 / 1.8 s` |

## Ľudský výsledok, ktorý budeme hľadať

Najdôležitejšie nie je „všetko zelené“, ale správne oddelenie príčiny.
Ak rovnice/holdouty prejdú, ale spoločné koeficienty sa neustália alebo sú
nové mocniny 2–3 ešte veľké, ide o živú koľaj s neuzavretou
konvergenciou/supportom. Ak zlyhá core, najprv sa kontrolujú
vzorce, znamienka a implementácia; fyzikálny STOP sa bez reprodukcie
neudelí.

## Výsledky

Sekcia sa doplní po každom samostatnom Python procese. Predbehové
očakávania sa spätne nemenia.

### Pred procesom 1 — zdieľaný modul

**Pripravené:** 2026-07-16. Spustí sa iba
`py_compile cdi_c1_coverage.py`. Očakáva sa exit `0` bez výstupu do
`10 s`. Proces nepočíta fyzikálny výsledok, nepridáva skóre a pri chybe
sa eviduje výlučne technické zlyhanie pred vecným auditom.

**Výsledok procesu 1:** `PASS_TECHNICAL_COMPILE`, exit `0`, wall time
`0.5 s`, bez výstupu. Fyzikálny stav a počítadlo vecných výsledkov sa
nemenia.

### Pred procesom 2 — runner 278

Spustí sa iba `py_compile` runnera 278. Očakáva sa exit `0` bez výstupu
do `10 s`. PASS povoľuje kontrolu rozhrania `--help`; chyba sa zapíše
ako technická chyba runnera bez fyzikálneho rozsudku.

**Výsledok procesu 2:** `PASS_TECHNICAL_COMPILE`, exit `0`, wall time
`0.5 s`, bez výstupu. Fyzikálny audit sa ešte nespustil.

### Pred procesom 3 — rozhranie runnera

Spustí sa `--help`. Očakáva sa exit `0`, stručné pevné CDI C1
rozhranie s režimami `--smoke`/`--audit`, interným časovým limitom a
cestou výstupu; nesmie vzniknúť auditný JSON ani fyzikálny výsledok.

**Výsledok procesu 3:** `PASS_TECHNICAL_HELP`, exit `0`, wall time
`0.6 s`. Rozhranie obsahuje výlučné `--smoke`/`--audit`, interný limit
a výstup; nevznikol fyzikálny výsledok.

### Pred procesom 4 — smoke

Spustí sa `--smoke --max-runtime-seconds 4.8` s vonkajším limitom
`10 s`. Očakáva sa správne odvodenie supportov a počtov, zhoda hashov
zdrojov, odmietnutie zámerne nesprávneho supportu a pri PASS žiadny
výsledkový JSON. Smoke nie je vecný výpočet a neresetuje technické
počítadlo.

**Výsledok procesu 4:** `PASS_TECHNICAL_SMOKE`, exit `0`, wall time
`1.1 s`, `smoke_pass=true`. Nevznikol kanonický auditný výsledok a
technické počítadlo sa týmto testom neresetuje.

### Pred procesom 5 — vecný audit CDI C1

Spustí sa jediný vecný proces `--audit --max-runtime-seconds 4.8` s
vonkajším limitom `10 s`. Očakávaný PASS vyžaduje súčasne core brány,
stabilitu spoločných koeficientov primárneho a rozšíreného supportu,
malý čistý príspevok nových mocnín 2–3 na `z=1e-4` aj `z=1e-2` a
presnú podmienenú S-C0 mapu skutočných nízkych momentov. Ak prejde core,
ale zlyhá spoločný koeficient alebo chvost, očakáva sa príslušné
`REVIEW`; core chyba vyžaduje audit vzorcov. Žiadna z týchto vetiev sama
neudeľuje fyzikálny STOP ani body.

**Výsledok procesu 5:** `TECHNICAL_COMPLETE`, exit `0`, wall time
`1.8 s`, vnútorný runtime `0.75 s`. Kanonický výsledok:
`RUN_KMPC_034_P5_3G7_CDI_C1_PRIMARY_EXTENDED_COVERAGE.json`, SHA-256
`37FB4453CBFF38710CF5694C21104689F1B070742FB02324011AA389508DCE20`.

Strojový kandidát, nie rozsudok orchestrátora:
`REVIEW_CDI_C1_SUPPORT_EXTENSION_REQUIRED`.

- core: PASS; hodnosti M3 `26/26` a `52/52`, driver aj nezávislé
  `00/0i` holdouty PASS;
- spoločné koeficienty: PASS, maximum relatívneho rozdielu
  `5.061250322927873e-15`;
- presná podmienená S-C0 mapa skutočných nízkych momentov: PASS;
- čistý pridaný chvost mocnín 2–3: FAIL voči predregistrovanému
  relatívnemu limitu `1e-6`;
- pri `z=1e-4` je najhorší bežný relatívny príspevok
  `delta_f = 3.136478085397359e-5`; viacero nenulových stavov leží
  približne na `3.03e-5`;
- pri `z=1e-2` je `delta_f = 3.14477004101659e-3` a bežné hustoty
  približne `3.05e-3`; hodnota `sigma_fs ~ 1` je samostatne citlivá na
  takmer nulový vedúci základ a sama nie je použitá ako jediný dôvod.

Proces priniesol čiastočný vecný výsledok bez technického pádu, preto sa
aktívne technické počítadlo tejto vetvy resetuje na `0/10`. Autoritatívny
PASS/REVIEW/STOP zostáva do troch nezávislých posudkov nepridelený.
