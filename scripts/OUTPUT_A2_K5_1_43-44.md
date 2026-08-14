# A2-K5.1 — výstup auditu limitu `delta->0`

**Dátum:** 2026-07-13

## Skript 43 — neúspešný API beh

```text
AttributeError: module 'a1_k1_audit_base'
has no attribute 'omega_radiation_today'
```

Nevznikol fyzikálny výsledok.

## Skript 44 — finálny výsledok

| `delta` | `varphi_x` | `beta` | `beta varphi_x` |
|---:|---:|---:|---:|
| `2.297e-2` | `2.113475e-1` | `1.528833` | `0.3231150962` |
| `2.297e-4` | `2.113475e-2` | `15.288332` | `0.3231150962` |
| `2.297e-6` | `2.113475e-3` | `152.883320` | `0.3231150962` |
| `2.297e-8` | `2.113475e-4` | `1528.833197` | `0.3231150962` |

```text
beta ratios = 10, 10, 10
varphi_x ratios = 0.1, 0.1, 0.1
product spread = 1.11e-16
status = PASS_SINGULAR_LIMIT_CONFIRMED
```
