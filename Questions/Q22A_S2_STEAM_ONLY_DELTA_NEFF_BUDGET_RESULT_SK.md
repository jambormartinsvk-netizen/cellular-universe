# Q22a-S2 — výsledok sita priamej pary v rozpočte `Delta N_eff`

**Verdikt:** `K2_MŔTVA_V_DODANEJ_PERSISTENTNEJ_DIRECT_STEAM_FORME; K3_DIRECT_STEAM_PRISNE_OBMEDZENÁ`  
**Typ dôkazu:** `konzervatívne observačne ukotvené backgroundové sito; bez skóre`  
**Skripty a prílohy:** `scripts/259_script_Q22A_S2_steam_only_delta_neff_budget_screen.py`,
`RUN_Q22A_006...json` a `RUN_Q22A_007...json` v `scripts/results/q22a/`.

## Čo bolo fyzikálne fixované

Štandardné fotóny a neutrína sa držali oddelene s presným `a^-4` riedením.
Iba parný relikt zodpovedajúci už registrovanému `Delta N_eff=0.0535` mohol
prijímať priamy podiel `f_R q` z A1 transferu. Dnes má táto zásoba iba

```text
X_steam = 6.8100197e-7,
q_today = 9.7230674e-2,
X_steam/q_today = 7.0039828e-6.
```

To je pozorovateľný rozdiel oproti S1: neumožňuje spätne odobrať energiu
štandardnému CMB fotónovému/neutrínovému kúpeľu.

## Výsledok a konvergencia

| Beh | krok | prechádzajúci `f_R` | prvý neprechádzajúci `f_R` |
|---|---:|---:|---:|
| RUN 006 | `1e-4` | `3.1709671e-5` | `3.1948090e-5` |
| RUN 007 | `5e-5` | `3.1471252e-5` | `3.2424927e-5` |

Intervaly sa prekrývajú. Ich stredy sa líšia o približne `0.37 %`, pod
predregistrovanou hranicou `5 %`. Konzervatívny zápis výsledku je preto

```text
f_R,direct < približne 3.2e-5,
b = 1-f_R > približne 0.999968.
```

Čistá K2 (`f_R=1`) vedie pri spätnom behu k zápornej parnej hustote už na
prvom kroku (`|Delta ln a|<=1e-4`). Nemôže teda byť kontinuálnym priamym
voľno-relativistickým produktom registrovaného neskorého transferu `Q`.

## Presný rozsudok

* **Q22a-K2:** `MŔTVA — ARCHIVOVANÁ V DODANEJ FORME`. Dôvod smrti nie je
  algebra ani solver, ale rozpor medzi kontinuálnym priamym zdrojom a malým,
  pozorovateľne ukotveným dnešným parným rozpočtom.
* **Q22a-K3:** prežíva iba v limite, kde priamy voľno-relativistický podiel
  nehrá významnú energetickú úlohu. Tento výsledok **neodvodzuje** `b` a
  nedovoľuje ho fitovať; iba vylučuje väčšinu jeho rozsahu.

## Čo rozsudok nezabíja

Nevylučuje paru ako skorý relikt, už prítomnú pred neskorým A1 transferom,
ani energiu, ktorá sa najprv uloží v medzistave, neskôr sa reabsorbuje alebo
nemá relativistickú rovnicu stavu. To sú však iné, časovo štruktúrované
mechanizmy K4–K7 a potrebujú odvodený kernel; nesmú byť len premenovaním K2.

Plný BBN/CMB likelihood by hranicu mohol ďalej sprísniť. Na smrť K2 v jej
dodanej perzistentnej forme však nebol potrebný: už kladnosť a samostatný
registrovaný parný rozpočet ju vylučujú.

## Ďalší postup podľa fyzikálnej logiky

Priame súčasné `F->C+R` s pozorovateľne významnou parou už nie je perspektívne.
Ak má para patriť k deleniu, musí byť odvodený jeden z týchto mechanizmov:

1. skorý, ukončený reliktný kanál pred neskorým `Q`;
2. sekvenčný kanál s fyzikálne odvodeným časovým kernelom;
3. nerelativistický/medzistavový produkt, ktorý sa nesmie účtovať ako
   `Delta N_eff` bez samostatného testu.

Bez takého mechanizmu ostáva A1-K1 efektívny `F->C` ledger jedinou koľajou
kompatibilnou s týmto sitom.
