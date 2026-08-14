# A2-K4 C7.7c-K3 — predregistrácia normalizovaného Radau behu

**Dátum:** 2026-07-14  
**Rodič:** C7.7c  
**Rozdiel od K2:** iba solver a časová rezerva

K3 zachováva:

- fyzickú ODE 136;
- 13 stavových komponentov;
- `w_i=y_i/max(abs(y_i_start),1e-300)`;
- normalized `rtol=1e-10`, `atol=1e-12`;
- `max_step=0.02`, segment `1 e-fold`, `x_final=-18`;
- rovnakú normalizovanú activity floor a všetky acceptance kritériá K2.

Mení:

```text
solver: DOP853 -> Radau
evolution internal limit: 45 s
audit wrapper limit:       50 s
external limit:            60 s
```

Radau PASS nesmie byť interpretovaný ako solverová konvergencia; iba ako
úspech C7.7c activity ledgeru. DOP853 timeout sa zachováva.

