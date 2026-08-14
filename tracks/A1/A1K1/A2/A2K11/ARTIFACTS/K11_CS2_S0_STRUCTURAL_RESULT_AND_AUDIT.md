# K11-CS2/S0 — výsledok exact structural auditu

**Dátum:** 2026-07-16  
**Autorita verdiktu:** hlavný orchestrátor  
**Predregistrácia:**
`K11_CS2_S0_STRUCTURAL_IMPLEMENTATION_PRERUN.md`  
**Autoritatívny raw výsledok:**
`scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_S0_002.json`  
**Verdikt:** `PASS_K11_CS2_S0_STRUCTURAL_ONLY`  
**Fyzikálna evolúcia:** nevykonaná  
**Skórovací účinok:** `0`; K11 zostáva `10/100 = G1`

> **Neskoršie autoritatívne obmedzenie PF-062:** koeficientové identity
> zostávajú PASS, ale state register chybne obsahoval `E_0,E_1`. State-count
> časť tohto výsledku je STOP/SUPERSEDED. Pozri
> `K11_CS2_S0_STATE_REGISTER_PF062_ERRATUM.md`.

## 1. Čo bolo dokázané

Štrukturálna revízia K11-CS2 prešla všetkých `36/36` kontrol. Každé
symbolické rezíduum je presne `0`:

- K11-R relatívna drag sadzba `d_c+d_f=Gamma/H`;
- vážená momentum reakcia medzi popolom a palivom;
- interaction-only determinant `-d_c g/delta`;
- párové vyrušenie A1 backgroundového transferu;
- nulová závislosť backgroundovej sumy od Fourierovho `k`;
- jednoznačné, neduplikované stavové registre;
- CAMB 1.6.6 fotónové `J_l`, free-streaming `G_l`, polarizačné `E_l`
  koeficienty pre `l=2...8`;
- presný polarization source.

RUN-002 exportoval interné v001 počty

```text
lmax=4 -> 27,
lmax=6 -> 35,
lmax=8 -> 43,
count  = 4*lmax+11.
```

Register explicitne obsahuje `W_c`, `W_f`, samostatné neutrína a paru,
ale neskorší PF-062 audit zistil dve nadbytočné CAMB E-mode položky
`E_0,E_1`. Správne fyzické počty sú `25/33/41`; v001 state-contract PASS
sa preto ruší.

## 2. Execution audit

### RUN-001

Obsahovo prešiel, ale shell skončil external timeoutom `124`. Zostal preto
iba recoverable REVIEW dôkaz. Runner 262 je zachovaný ako
`DO_NOT_RUN_TECHNICAL`; podrobný záznam je v
`K11_CS2_S0_RUN001_EXTERNAL_EXIT_TIMEOUT_AUDIT.md`.

### Technická oprava 1/2 a RUN-002

Runner 263 zmenil iba output obal: pri zápise immutable JSON vytlačil na
stdout krátke zhrnutie namiesto celého payloadu. Výsledok:

```text
internal runtime = 0.828 s < 5 s,
external wall    = 5.3 s < 10 s,
shell exit       = 0,
false checks     = 0/36,
physics evolution executed = false,
score effect = 0.
```

RUN-001 a RUN-002 sú po normalizovaní jediného poľa `runtime_seconds`
obsahovo presne rovnaké. Oprava teda nezmenila fyziku ani algebraický
výsledok.

## 3. Čo výsledok nedokazuje

S0 **nie je**:

- úplná numeric RHS;
- dôkaz photon-baryon opacity/TCA handoffu;
- Frobeniova regulárna fyzická báza;
- propagácia `00`, trace, traceless a Bianchi holdoutov;
- dôkaz stability K11-R;
- subhorizontový rast, CMB alebo `S8` likelihood;
- odvodenie mikrofyziky dragu alebo noise/FDT.

Presné CAMB koeficienty iba dokazujú správny štandardný multipólový ledger.
Neuzatvárajú custom dark riadky s metrikou a constraintmi.

Preto je zakázané citovať tento výsledok ako `K11 PASS`, `G2 PASS` alebo
ako vyvrátenie M-009.

## 4. Následný jediný krok

S0 base revízia je po vytvorení dôkazu zmrazená. Plný propagátor musí
vzniknúť ako nový versioned modul v `scripts/baseScripts/a2_k11_cs2/` a
musí importovať alebo presne pinovať S0 identity bez ich tichého prepisu.

Pred jeho prvým Python behom musí prerun dodatok určiť:

1. presný stav a row manifest vrátane opacity/slip;
2. finite-`k` Frobeniovu fyzickú bázu a jej očakávaný rank;
3. exact-A1 a `lambda=0` backgrounds;
4. netautologické `00`, trace, traceless a Bianchi holdouty;
5. tri `k`, dva štarty, closure a metódovú konvergenciu;
6. očakávaný `ln` relative transfer `10–13` a zmrazené STOP/REVIEW vetvy;
7. limit `<=5 s` interne a `<=10 s` externe pre každý Python proces.

Ak plný modul nevie splniť rozsah v limite, výsledkom bude
`REVIEW_BLOCKED_IMPLEMENTATION`, nie smrť koľaje.

## 5. Kontrolné súčty

| Artefakt | SHA-256 |
|---|---|
| S0 base | `19263A674E1F342E06E6D0D3999E65E58687CCFF20E5EE083A05D06D7BB107FF` |
| package `__init__.py` | `8FB3EB481E1061C5F238AA0612A936B6BF0D46393A65D82494263BD5DD2F61E1` |
| runner 263 | `F008465A16681DCECBDDD0A8E1A00B8B4FBC7D0BB3017C75D158D5894291DF45` |
| RUN-002 JSON | `AD112474E1432DC797B76E05B2FE565ACB3D063F75213359F7CD8CAC92DBE65B` |
| pinned CAMB `symbolic.py` | `F380B56A15F678F6D8DBA8981BBE5A4E57377050945ADE91C6CD4B9262C7A608` |

## 6. Release

Žiadny release trigger. S0 nemení publikovaný mechanizmus ani tabuľku
predikcií.
