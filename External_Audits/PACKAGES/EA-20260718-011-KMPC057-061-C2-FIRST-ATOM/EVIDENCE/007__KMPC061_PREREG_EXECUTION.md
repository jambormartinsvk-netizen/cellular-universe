# KMPC-061 — C2 Fourier guard-semantics successor: predregistrácia

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → S-C0 / C2 Fourier gate`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`

## Jediná oprava po KMPC-060

Guard oddelí dve presné množiny:

1. false checks pôvodného V1 guardu: `(BI,CDI)` v lexikografickom výstupe;
2. módy, kde historical S1 extended support nie je dnešný closed C1 support:
   `(AD,CDI,BI)` v mode-major poradí.

KMPC-060 tieto hodnoty priamo zmeral. V4 overlay zmení iba druhé očakávanie
z `(CDI,BI)` na `(AD,CDI,BI)`. Desiatka atómov, rovnice, support/depth mapa,
prahy, poradie, runtime, stop pravidlá a immutable C1 hashe ostávajú presne
podľa dokumentu 104. Stabilný runner harness z KMPC-059 sa znovupoužije bez
zmeny a tenký runner bude obsahovať iba nový manifest.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | KMPC-060 exact diagnostic: V1 false `(BI,CDI)`, historical diff `(AD,CDI,BI)` | `ROOT_CAUSE_CLOSED` |
| 2026-07-18 | jediná guard-semantics oprava a nezmenená fyzika zmrazené slovne | `PREREGISTERED` |
| 2026-07-18 | V4 overlay SHA `05253AFC92923386329F6A70FBEF7F34EB73B9C2D29E881F58E0C4D08F1DE519`; nezmenený harness SHA `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`; thin runner SHA `DF48D8335B3577F4180125638D92BCF040BF7F9F3B394D4456AD50314AC54F28`; žiadny KMPC-061 output | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile/help/smoke PASS; V1 false `(BI,CDI)`, historical diff `(AD,CDI,BI)`, všetky owner/publish fixtures PASS | `PREFLIGHT_PASS` |
| 2026-07-18 | prvý atóm AD/`.005` dokončený exit `0`; raw SHA `0952AF08B1DE291D015F71396954F70EAE2F78A962E1EE1D3A08ECA48A1F5DCD`; core/common/background PASS, tail FAIL | `REVIEW_C2_SUPPORT_EXTENSION_REQUIRED` |
