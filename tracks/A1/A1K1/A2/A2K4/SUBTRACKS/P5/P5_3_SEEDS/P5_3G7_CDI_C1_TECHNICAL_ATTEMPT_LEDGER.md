# P5.3g7 CDI C1 — technický attempt ledger

**historical_packages_total:** `1`  
**consecutive_technical_failures:** `0/10`  
**Fyzikálny stav:** `CORE+COMMON PASS / PRIMARY [0,1] INSUFFICIENT / [0,3] REMAINDER OPEN`; K4 `LIVE / 60/100`

| Balík | Run | Stav | Vecný výsledok | Active counter po balíku |
|---:|---|---|---|---:|
| 1 | KMPC-034 | `TECHNICAL_COMPLETE` | script candidate `REVIEW_CDI_C1_SUPPORT_EXTENSION_REQUIRED`; main: `PASS_CDI_C1_CORE_AND_COMMON_COEFFICIENT_STABILITY_ONLY / REVIEW_CDI_C1_PRIMARY_01_INSUFFICIENT_EXTENDED_03_REMAINDER_NOT_YET_TESTED` | `0/10` |

Syntax, import, timeout, sandbox, serializácia a hash mismatch sú technické
chyby a nesmú zabiť CDI ani K4. Vecne úspešný core/tail výsledok — aj
interpretovateľný REVIEW — vynuluje active counter. Compile/help/smoke ho
nevynulujú. Po desiatich po sebe idúcich technických zlyhaniach sa zastaví
iba implementačná línia s presným dôvodom.
