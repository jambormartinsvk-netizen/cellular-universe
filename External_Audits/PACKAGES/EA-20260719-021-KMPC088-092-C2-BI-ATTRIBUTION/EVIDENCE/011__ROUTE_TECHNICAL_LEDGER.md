# C2 BI/k=.15 high-precision technický ledger

**historical_packages_total:** `12` (`KMPC-081…092`)  
**consecutive_technical_failures:** `0/10` po vecnom KMPC-092  
**Fyzikálny stav:** `REVIEW_C2_BI_K0p15_UPSTREAM_ATTRIBUTION_COMPLETE`; C2 `5/10`, K4 `60/100`

| Balík | Technický výsledok | Dopad na aktívny counter |
|---|---|---|
| KMPC-081 | PF-086, CLI runtime harness | `1/10` |
| KMPC-082 | PF-087, vnútorný deadline | `2/10` |
| KMPC-083 | vecný 80-dps REVIEW | reset `0/10` |
| KMPC-084 | PF-089, hash owner | `1/10` |
| KMPC-085 | PF-090, chybný decimal-exact fixture | `2/10` |
| KMPC-086 | vecný holdout-assembly REVIEW | reset `0/10` |
| KMPC-087 | vecný driver-assembly REVIEW | zostáva `0/10` |
| KMPC-088 | PF-092, neuskutočniteľná round-trip tolerancia | `1/10` |
| KMPC-089 | PF-093, fixture opustil 80-dps context pred porovnaním | `2/10` |
| KMPC-090 | PF-094, ledger zmenil poradie float-product/bridge | `3/10` |
| KMPC-091 | PF-095, nested owner checker použil mutable outer referenciu | `4/10` |
| KMPC-092 | vecný 73-term coefficient-attribution REVIEW | reset `0/10` |

KMPC-092 úspešne dokončil interpretovateľný ledger a counter resetoval na
`0/10`. Technický incident nikdy nevydáva fyzikálny STOP.
