# KMPC-110–112 — BI/k=.15 exact resume: výsledok a interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C2 → BI/k=.15/nominal`  
**Autoritatívny stav:** `PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1`  
**Coverage:** `C2 6/10 PASS`; **K4:** `LIVE / 60/100`; **P5:** `3.5/6`  
**Triggery:** release `NONE`, Zenodo `NONE`, prediction table `NONE`

## Záver

Interný audit prijíma candidate KMPC-112 ako autoritatívny scoped PASS pre
atóm `BI/k=.15/nominal`. Lossless KMPC-108 checkpoint obnovil M1 z
decimal90 pri 80 dps a auditný fuel register bitovo z `float.hex()`. Exact
104×104 driver aj samostatný 16×104 non-fit holdout prešli pôvodnými
zmrazenými prahmi. Holdout riadky neboli použité pri fite.

Tým sa uzatvára šiesty z desiatich C2 atómov. Neuzatvára sa celé C2, P5.3,
P5 ani A2-K4 a fyzikálna hĺbka zostáva `60/100`.

## Auditná stopa

| Artefakt / kontrola | Overený výsledok |
|---|---|
| KMPC-108 checkpoint SHA | `683D867D19324B7B45F3724545FFB1D975DFBED883936298D790C12836E9D995` |
| KMPC-109 receipt SHA | `21EF9A9BF8D6E437CC848BD76EC026C5621534F35C0D88F99D2BFAFAD28118F9` |
| serialized-state SHA | `402B42E11C3582B4E3E46D047EA917A4C256E552F65C9DB070589150675EBF40` |
| KMPC-112 raw SHA | `FAF52256489BA7C105F9125C1ED9A68358C0187E5F7B8B1164E1BA036A6507A1` |
| source contract | `48/48`; všetky technické checks `true` |
| runtime | `34.8600000000006 s < 45.0 s` |
| audit payload parity | PASS po publish-kanonickom porovnaní |
| audit fuel parity | exact `float.hex()` PASS |
| register handoff | 13 stavov, M1/F0 owner merge PASS |
| matrix capture | presne `1×`, shape `104×104`, owners restored |
| exact driver solve | presne `1×`, 80 dps |
| holdout fit leakage | `rows_added_to_driver_solve=0` |

PF-111 a PF-112 sú technické incidenty bez fyzikálneho verdiktu. V18
opravil iba obnovu explicitného poradia registrov. V19 opravil iba spoločnú
JSON reprezentáciu pred parity porovnaním. V17 výpočet, checkpointové
hodnoty, rovnice, support, presnosť a prahy ostali byteovo nezmenené.

## Numerický výsledok

| Brána | Hodnota | Prah | Audit |
|---|---:|---:|---|
| pôvodný float64 audit M3 driver | `2.7715917114e-10` (`tight_coupling[7]`) | `1e-10` | historický false, presne jediný |
| exact driver max relative | `8.6147582237e-82` (`fuel_Euler[7]`) | `1e-10` | PASS |
| exact driver max absolute fallback | `1.6911687966e-101` | `1e-12` | PASS |
| exact holdout max relative | `7.0711904227e-15` (`Einstein_00[7]`) | `1e-9` | PASS |
| exact holdout max absolute fallback | `3.7039815525e-21` | `1e-12` | PASS |
| exact `Einstein_0i[7]` | `3.3965448411e-15` relative | `1e-9` | PASS |

Exact holdout má voči relatívnemu prahu rezervu približne `1.41×10^5` a
`Einstein_0i[7]` približne `2.94×10^5`. Driver nie je iba tesne pod prahom.
Matrix/constant fingerprinty, exact solution fingerprint a všetky capture,
receipt, false-set a no-CPQR-repeat brány sú uložené v raw.

## Fyzikálna interpretácia

Historický BI/k=.15 problém nebol dôkaz rozpadu supportu `[0,5]` ani
fyzikálneho rozporu. Bol spôsobený tým, že silne rušený downstream systém
používal binary64 M1 koeficienty. Po natívnom 80-dps M1 solve a presnom
downstream zostavení prešli driver aj nezávislé constraint holdouty bez
fitu. Float64 auditný `M3_driver` sa preto v tomto jednom atóme smie
podmienene supersedovať exact výsledkom; historická hodnota sa nemaže.

Rozsah výsledku zostáva úzky:

- iba `BI/k=.15/nominal`;
- accepted `[0,5]` voči auditu `[0,7]`;
- M1 je 80-dps, ale F0 a background vstupy ostávajú presne bridged binary64;
- nie je to dôkaz pre `[0,9]`, iný mód/k, S-M, ODE, plnú hierarchiu ani dáta.

## Autoritatívne rozhodnutie a ďalší krok

- C2 sa mení z `5/10 PASS` na `6/10 PASS`;
- aktívny technický counter sa po vecnom úspechu resetuje na `0/10`;
- K4 ostáva `LIVE / 60/100`, P5 `3.5/6`, bez fyzikálneho STOP;
- ďalší predregistrovaný atóm je `NID/k=.005/nominal` s frozen accepted
  supportom `[0,5]`, auditom `[0,7]`, M1 depth `7` a nezmenenými prahmi;
- pred jeho spustením sa musí uzavrieť externý auditný balík KMPC-110–112.
