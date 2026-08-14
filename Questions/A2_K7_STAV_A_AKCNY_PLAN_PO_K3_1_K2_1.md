# A2-K7 — stav a akčný plán po K3.1-K2.1

**Dátum:** 2026-07-13  
**Kanonický stav K7:** `PREŽÍVA K7.0 — 30/100`  
**Najhlbšia podkoľaj:** K7.1a-K3.1-K2.1 — `39/100`  
**Aktívna podkoľaj:** K7.1a-K3.1-K2.2-K1

## Stav

| Podkoľaj | Stav | Max. hĺbka | Dôvod/stena |
|---|---|---:|---|
| K7.1a-K1 | `MŔTVA M-014a` | `32/100` | konštantná on-shell šírka nevie generovať povinný člen `H rho_F` |
| K7.1a-K2 | `PREŽÍVA IBA REKONŠTRUKCIU` | `34/100` | `Upsilon(phi)` nie je odvodený kernel; chýba memory/noise |
| K7.1a-K3.0 | `PREŽILA FORMULAČNÚ BRÁNU` | `36/100` | kovariantné `Theta_phi` prešlo, mikrofyzika nie |
| K7.1a-K3.1-K1 | `MŔTVA M-014b` | `38/100` | holá cross matica má zápornú vlastnú hodnotu |
| K7.1a-K3.1-K2 | `PREŽÍVA IBA TERMODYNAMICKÚ FORMULÁCIU` | `38/100` | pozitívne diagonálne doplnenie existuje |
| K7.1a-K3.1-K2.1 | `PREŽÍVA IBA ROZMEROVÚ BACKGROUNDOVÚ EXISTENCIU` | `39/100` | 18/24 bodov PASS; bath, kernel, `ell_hat` a noise nie sú odvodené |
| **K7.1a-K3.1-K2.2-K1** | **`AKTÍVNA`** | **`5/100`** | lokálny termálny/KMS bath ešte neauditovaný |
| K7.1a-K3.1-K2.2-K2 | `ČAKÁ` | `5/100` | vákuový farebný kernel |
| K7.1a-K3.1-K2.2-K3 | `ČAKÁ` | `5/100` | netermálny farebný bath |
| K7.1a-K4 | `ČAKÁ` | `5/100` | threshold realizácia |

## Rozsudok K2.1

Rozmerovo konzistentná pozitívna transportná matica kompatibilná s
registrovaným backgroundom existuje. Nie je však odvodené, že ju vytvára
bunkový priestor. Diagnostický parameter `ell_hat` sa preto nesmie zapísať
ako nový parameter teórie ani použiť na fit `S_8`.

## Akčný plán K2.2-K1

1. zvoliť explicitný minimálny bath field/content a zapísať jeho lokálny
   stress-energy;
2. odvodiť retarded spektrálnu hustotu a noise kernel;
3. overiť spektrálnu pozitivitu, KMS/FDT a kauzalitu;
4. odvodiť korelačný čas a otestovať `tau_bath H << 1` od rekombinácie po
   dnešok;
5. z nulofrekvenčného limitu odvodiť `ell,zeta,alpha` vrátane rozmerov;
6. znovu uzavrieť A1 ledger s `rho_bath,p_bath`;
7. vytvoriť skript 60 s predregistrovanými bránami a konvergenčným testom;
8. pri neúspechu označiť K1 `MŔTVA M-014d`, ponechať výpočet a prejsť na
   K2; pri prežití ešte nepromovať K7, kým sa neuzavrie celý krok `40/100`.

## Čo sa zatiaľ nesmie robiť

- nespúšťať K7.1b lineárne perturbácie s voľným `delta ell`;
- nezamieňať `N proportional to 2 T L` za určenú amplitúdu bez `T`;
- neschovať bath do pary alebo popola bez explicitného ledgerového dôkazu;
- nevyberať `ell_hat` podľa výsledného `S_8`.

