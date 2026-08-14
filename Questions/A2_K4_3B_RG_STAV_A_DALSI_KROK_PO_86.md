# A2-K4.3b-RG — stav a ďalší krok po skripte 86

**Stav:** `ČIASTOČNE PREŠLA; NEUZAVRETÁ; NIE MŔTVA`  
**Kanonická maximálna hĺbka:** `60/100 = G6`  
**Aktívny balík:** `K4.3b-RG-BR`

## 1. Stav jednotlivých RG krokov

| RG krok | Stav | Poznámka |
|---|---|---|
| RG1 — regulárna gauge | **PASS pre test-field** | general synchronous, `A=0`; `theta_c` sa po K4 vyvíja |
| RG2 — sedem seed smerov | **PASS** | päť kolektívnych + dva interné, rank 7 |
| RG3 — úplné rady | **ČIASTOČNE** | interné rady exact; kolektívna test-field odpoveď PASS; backreaction chýba |
| RG4 — konečný Newtonov map | **NEUZAVRETÝ** | vyžaduje vyšší rád NID/NIV; nie je potrebný pre synchronous evolúciu |
| RG5 — štyri Einsteinove rezíduá | **ČAKÁ** | chýba fuel a ash backreaction |
| RG6 — rozsudok K4.3b | **ČAKÁ** | bez RG5 sa nesmie uzavrieť |

## 2. K4.3b-RG-BR — akčný plán

1. **BR1 — metric ledger:** zapísať general-synchronous premenné `h`, `eta`
   a jednoznačné `00`, `0i`, bezstopové a stopové `ij` rovnice v rovnakých
   znamienkach ako audit A2.1.
2. **BR2 — Puiseux exponenty:** vytvoriť spoločný register celočíselných
   radiačno-hmotových mocnín a frakčných vetiev
   `4-3delta=3.93109`, `5-3delta=4.93109`.
3. **BR3 — fuel koeficienty:** nahradiť nulový test-field štart explicitným
   regulárnym particular radom `delta_f,U_f` pre AD/CDI/BI/NID/NIV.
4. **BR4 — backreaction:** vložiť fuel `delta rho`, `delta p`, momentum do
   Einsteinových rovníc a následnú korekciu popola.
5. **BR5 — interné módy:** znovu potvrdiť nulový metrický a dark-sector
   zdroj oboch kompenzovaných `nu-steam` módov v spoločnom solveri.
6. **BR6 — dve hĺbky:** vyhodnotiť všetkých sedem módov aspoň na dvoch
   štartových povrchoch; nulové placeholdery sa nesmú použiť.
7. **BR7 — rezíduá:** samostatne reportovať absolútnu aj škálovanú normu
   `00`, `0i`, slip a `ij`, plus energy/momentum ledger.
8. **BR8 — nulový limit:** `lambda->0` musí reprodukovať analytické
   CLASS/CAMB seedy a perfect-radiation limit staršej K4.1 iba v jeho
   deklarovanom rozsahu.
9. **BR9 — rozsudok:** iba úplný PASS otvorí K4.3c. TIMEOUT alebo chýbajúci
   backend znamená `NEUZAVRETÁ`, nie smrť.

## 3. Kill kritériá BR

K4.3b môže dostať fyzikálnu smrť iba ak sa po vylúčení gauge a numerických
artefaktov preukáže aspoň jedno z:

- invariantný mód diverguje;
- neexistuje spoločné riešenie štyroch Einsteinových rovníc a conservation
  ledgeru;
- `lambda=0` limit je fyzikálne nesprávny;
- fuel/ash backreaction vytvorí zápornú kinetickú normu alebo iný už
  potvrdený patologický stav.

Placeholder, chýbajúci kompilátor, nedostatočný rád gauge mapy ani timeout
nie sú kill kritériá.

## 4. Časové limity

- symbolické koeficienty: interne najviac 30 s, externe 40 s;
- numerické rezíduá: interne najviac 50 s, externe 60 s;
- polling: najviac 10 s;
- pri limite sa úloha rozdelí; skript a čiastkový výstup zostanú zachované.

