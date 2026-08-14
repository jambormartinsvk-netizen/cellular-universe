# A2-K4 / C7.7c — audit tvrdení o skriptoch 173–185

Dátum: 2026-07-15  
Auditor: Codex  
Stav A2-K4: **ŽIVÁ, 66.5/100**  
Stav K7b: **numerický PASS zostáva platný; publikačný gate potrebuje fail-closed spevnenie**  
Stav K7c: **REVIEW; bez bodu a bez fyzikálneho rozsudku smrti**

## Konečný rozsudok

Hlavné tvrdenie je **potvrdené**. Skript 170 zachytával high-precision register pri každom solve s rovnakým módom. Fyzikálny solve s `physical_mu` prebehol pred neskorším referenčným solve s `mu=0`, takže druhý solve prepísal `hp_standard_registry`. Skript 172 preto neporovnával dve presnosti toho istého riešenia, ale float64 fyzikálny stav proti HP registru nulového limitu.

Oprava v 174 obmedzila capture na `abs(mu-physical_mu) < 1e-30`. Pri opakovanom limitovanom audite 187 sa zmenilo iba toto kauzálne miesto oproti už slice-opravenému 171/172 reťazcu:

| veličina | pred opravou, 172 | po oprave, 175 |
|---|---:|---:|
| `abs(U_fs_float-U_fs_HP)` | `3.191525072e-9` | `0.0` v exportovanej presnosti |
| `abs(U_gamma_float-U_gamma_HP)` | `5.883620813e-10` | `0.0` v exportovanej presnosti |
| `D_activity_relative_error` | `8.5041561425e5` | `5.951092202e-3` |
| exit/verdict | `1 / REVIEW` | `0 / PASS` |

Zlepšenie D-aktivity je približne `1.43e8`-násobné. V tomto testovanom reťazci teda nejde o dve nezávislé fyzikálne príčiny: rýchlostná nezhoda aj extrémna D-aktivita mali spoločnú provenienčnú príčinu. Štvorpovrchový skript 176 následne prešiel, takže pôvodná obava, že K7c dedí register s `mu=0`, je odstránená.

## Rozsudok po jednotlivých tvrdeniach

| tvrdenie | audit | obmedzenie |
|---|---|---|
| 173 patchuje 171, ale capture marker je v 170 | **POTVRDENÉ** | 171 obsahuje vygenerovaný patchovací text v inom tvare; `source_text.count(old)` v 173 je nula a skript správne skončí pred fyzikou |
| 174 správne patchuje 170 a filtruje fyzikálne `mu` | **POTVRDENÉ** | potvrdzuje kód aj numerický prechod 172→175 |
| `condition_resolved` pochádza z pôvodnej matice | **POTVRDENÉ** | je odvodená zo singular values pôvodného `np.linalg.lstsq(matrix,rhs)`, nie z redukovaných normálnych rovníc |
| normálne rovnice pri kondícii asi 511 sú pri 80 dps numericky bezpečné | **POTVRDENÉ PRE PRESNOSTNÚ REZERVU** | odhad kondície normálnych rovníc je `511.1099² = 2.61233e5`; 80 dps má veľkú rezervu, ale normálne rovnice stále nie sú dôkazom fyzikálnej správnosti ani nevrátia cifry stratené pred konverziou z float64 |
| `mp.mpf(repr(float(x)))` je exaktný round-trip | **OBMEDZENE POTVRDENÉ** | po spätnom prevode reprodukuje ten istý binary64 float; nie je to exaktné vloženie pôvodnej pred-float hodnoty a neobnovuje už zaokrúhlené cifry |
| 180 opravuje vždy padajúce poradie JSON kľúčov | **POTVRDENÉ** | 178 používa `sort_keys=True`; 179 porovnával `tuple(dict)` s `NAMES`; 180 správne kontroluje množinu a stav skladá explicitne cez `NAMES` |
| 182 musí sondovať `S_j e_j` a deliť `S_j` | **POTVRDENÉ** | 181 sondoval fyzickú jednotku a aktivoval safety cap; algebraický návratový vektor všetkých 13 RHS je pri pevnom backgrounde lineárny v stave, preto je škálovaná sonda správny stĺpec v rámci float64 |
| physical RHS je bezvýhradne lineárna funkcia programu | **SPRESNENÉ** | vrátených 13 rovníc je lineárnych; call counter, deadline, finite test a safety cap sú stavovo závislé ochranné vetvy. Sondy 182 zostávajú pod capom, preto operátorová interpretácia pre ne platí |
| 185 exportuje pomer, ale negatuje ním PASS | **POTVRDENÉ** | chýba brána približne `8 < previous/current < 32`; aktuálny výsledok `0.367` by ju neprešiel |
| chýbajúca pomerová brána spôsobila falošný PASS 185 | **VYVRÁTENÉ** | 185 aj tak skončil REVIEW, lebo endpoint rozdiel `3.93124e-6` prekročil `1e-6`; ide o latentnú chybu budúceho gate, nie zmenu dnešného rozsudku |
| krokové mriežky 185 sa uzavreli | **POTVRDENÉ** | beh dosiahol 200/400 krokov a endpoint; binárna reprezentácia kroku nespôsobila aktuálny fail |
| niektoré checky sú tautologické/dekoratívne | **POTVRDENÉ** | podrobnosti nižšie |
| 172/175 obsahuje fail-open `.get()==.get()` | **POTVRDENÉ** | podrobnosti nižšie; skutočný payload 175 však oba kľúče obsahoval |
| fixed-RK4 necháva starý `solve_ivp` za skorým returnom | **POTVRDENÉ** | výsledok 183–185 tým nie je zmenený, ale nedosiahnuteľný text je pasca pre budúce source markery |

## Tautologické a závislé kontroly

- `metric_h_identity_residual` odčíta od `rhs[0]` presne výraz, ktorým sa `rhs[0]` v tom istom volaní definoval. Rovnako `metric_eta_identity_residual` porovnáva `rhs[1]` s `M`, pričom `rhs[1]=M`. Sú to implementačné identity, nie Einsteinov test.
- `delta_fs` a `U_fs` sa rekonštruujú priamo z definícií `D` a `M`; následný density/momentum súčet preto meria najmä float64 kanceláciu. Je legitímny ako `cancellation_monitor`, nie ako nezávislý dôkaz propagácie constraintu.
- V 178 sú `seed["D"] == D` a `seed["M"] == M` porovnania premennej s hodnotou, ktorú jej skript bezprostredne priradil. Sú dekoratívne. Ostatné kontroly zdroja a názvov tým automaticky nestrácajú platnosť.

Tieto položky nesmú prinášať body ani zvyšovať confidence. To už vecne pokrýva AR45; nový audit iba obmedzuje konkrétne staršie formulácie.

## Fail-open audit 172/175

Kontrola

```python
hp_solver.get("reduced_rank") == hp_solver.get("free_count")
```

vráti `True`, ak oba kľúče chýbajú. To je chybná individuálna brána. Aktuálny PASS sa však spätne neruší:

- payload 175 oba kľúče obsahuje;
- hodnoty sú `58` a `58`;
- chýbanie celého solver payloadu by navyše zhodilo iné hard-constraint kontroly.

Zostáva reálny latentný prípad, keď by chýbali iba rankové kľúče. Preto musí vzniknúť nemenná fail-closed náhrada pred ďalším autoritatívnym reťazením alebo publikáciou.

## Stav skriptov a zachovanie neúspešných koľají

- 173 zostáva zachovaný ako technicky mŕtva marker-path koľaj.
- 179 a 181 zostávajú zachované s pôvodnými dôvodmi smrti.
- 183 zostáva zachovaný ako technicky mŕtvy JSON export a zároveň ako zdroj nedosiahnuteľného legacy bloku.
- 185 zostáva REVIEW; nesmie sa prehlásiť za PASS ani za fyzikálnu smrť.
- 186 je **nedokončený a neautoritatívny**. Súbor končí markerom `__K7C3D_CONTINUE__`, nevytvára ledger ani verdikt. Nemaže sa a nebude sa ticho dopĺňať; náhrada dostane nové číslo skriptu.

SHA-256 nových stôp:

- 186: `9923ed61c47b696088d517dcd5697b260cbf89568b6c284facd2044ce68a36ff`
- 187: `7009b074df2a51e2dbb0da80b925a90445121465323929bbed3672eb2b0d991d`

## Dopad na stav a skóre

- A2-K4 nezomiera.
- K7b zostáva numericky prejdená, ale jej implementačná robustnosť vyžaduje fail-closed nástupcu.
- K7c zostáva otvorená na REVIEW kvôli neasymptotickému `M`, nie kvôli registru `mu=0`.
- Jemná hĺbka zostáva `66.5/100`. Audit nepridal evolučný dôkaz.

## Reprodukcia

Autoritatívny audit tvrdení je:

```text
C:\Python311\python.exe scripts\187_script_A2_K4_K7b_K7c_claim_audit.py --max-runtime-seconds 35 --child-timeout-seconds 15
```

Posledný beh skončil za `8.781 s`. Skript má limit 35 s a každý child limit 15 s. Nevykonáva novú fyzikálnu evolúciu ani nemení hĺbku.
