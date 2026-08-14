# KMPC-108/109 — HP-M1 support checkpoint: výsledok a interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov a interný auditor:** Codex (OpenAI)  
**Autoritatívny stav:** `REVIEW_C2_BI_K0p15_HP_M1_CHECKPOINT_RECEIPT_EXACT_RESUME_ALLOWED`  
**Dopad na C2/P5/K4:** bez zmeny — C2 `5/10`, P5 `3.5/6`, K4 `LIVE / 60/100`

## Overené artefakty

- KMPC-108 checkpoint raw SHA:
  `683D867D19324B7B45F3724545FFB1D975DFBED883936298D790C12836E9D995`;
- vnútorný serialized-state SHA:
  `402B42E11C3582B4E3E46D047EA917A4C256E552F65C9DB070589150675EBF40`;
- KMPC-109 read-only receipt raw SHA:
  `21EF9A9BF8D6E437CC848BD76EC026C5621534F35C0D88F99D2BFAFAD28118F9`;
- receipt prešiel všetkými SHA/schema/order/fingerprint/false-set checks bez
  opakovania rovníc alebo solve.

## Vecný výsledok checkpointu

| Brána | Výsledok |
|---|---:|
| natívny HP-M1 CPQR a M1 boundary | PASS |
| accepted `[0,5]` F0/M3 | PASS |
| audit `[0,7]` F0 | PASS |
| audit `[0,7]` M3 rank/production contract | PASS |
| common koeficienty `0…5` | PASS |
| tail `6,7` | PASS |
| S-C0 actual coefficient guard | PASS |
| BI R-fs a background guard | PASS / N/A-pass |
| audit M3 driver | **REVIEW** |
| audit M3 independent holdout | PASS |

Jediný false check v audit supporte je `M3_driver`. Jeho najhorší relatívny
reziduál je `2.7715917114e-10` na `tight_coupling[7]`, teda nad zmrazeným
driver prahom `1e-10`. Najväčší absolute-fallback reziduál je
`2.3995061617e-17`. Nezávislý holdout v tej istej auditnej vetve prešiel:
najhorší relatívny riadok `Einstein_0i[7]` má `1.1636663777e-10 < 1e-9`.

Tento rozdiel sa nesmie vyhlásiť za PASS ani STOP. Float64 M3 driver je
presne numerická hranica, ktorú má samostatný exact-driver resume znovu
zostaviť a vyriešiť pri 80 dps. Receipt povoľuje tento test; nepredbieha jeho
výsledok.

## Integrita checkpointu

- M1 register má presne 11 stavov v autoritatívnom poradí a decimal90
  round-trip je presný pri 80 dps;
- audit F0 register má `delta_f,U_f` v `float.hex()` a binary64 round-trip
  je bitovo presný;
- kombinovaný register má presne 13 stavov v autoritatívnom poradí;
- serialized-state fingerprint bol v KMPC-109 nezávisle prepočítaný;
- V15 zmenil na decimal90 iba šesť diagnostických `mpf` hodnôt. Receipt
  overil presný počet aj cesty; resume register tým nebol zmenený.

## Technický lifecycle

- PF-107: monolit KMPC-105 prekročil vnútorných 45 s;
- PF-108: runner 350 nesprávne očakával priamy dict literal;
- PF-109: prvý dokončený checkpoint payload obsahoval diagnostický `mpf`;
- PF-110: KMPC-108 raw a summary vznikli, ale host shell timeoutol po publish;
- KMPC-109 immutable raw read-only overil a preto vecný checkpoint resetuje
  aktívny technický counter na `0/10`. História PF-107…110 zostáva.

## Autoritatívne rozhodnutie a ďalší krok

Checkpoint je dostatočne uzavretý na pokračovanie, nie na C2 PASS. Ďalší
predregistrovaný krok je jediný KMPC-110 exact resume:

1. fail-closed overiť SHA KMPC-108 aj receipt KMPC-109;
2. obnoviť HP-M1 z decimal90 a audit F0 z float-hex;
3. znovu zostaviť iba audit `[0,7]` 104×104 M3 maticu na zachytenie frozen
   matrix fingerprintu a overiť zhodu fuel registra s checkpointom;
4. na zachytenej matici vykonať 80-dps exact driver a independent non-fit
   holdout;
5. float64 `M3_driver` sa smie supersedovať iba ak exact driver, rank,
   matrix/fuel identity a holdout všetky prejdú pri nezmenených prahoch.

Žiadny iný C2 atóm, `[0,9]`, S-M, ODE, P5.4, G8/G9 ani dátový fit sa v
KMPC-110 nesmie spustiť.
