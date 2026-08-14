# FULL RUN-002 — očakávanie presného auditu univerzálnosti backgroundu

Testuje sa algebra zo zmrazeného skriptu 213, nie ODE ani dáta:

```text
z = k a/(H0 sqrt(Or))
mu = H0 Om/(sqrt(Or) k)
g2 = 0.15 (H0/k)^2 sqrt(Or)
D = 1 + mu*z + z^p [1 + g2 (1/(p+1)-1/2) z^2]
```

Očakáva sa, že `mu*z` a `g2*z²` budú presne k‑nezávislé. Pri nenulovom
`p=3.93109` však očakávame, že palivový člen bude homogénny stupňa `p` v
`k`, teda `k dF/dk = pF`, nie `dF/dk=0`.

**PASS brány:** iba ak sa nájde v existujúcej definícii dodatočná
k‑normalizácia, ktorá celý `D(a)` urobí nezávislým od `k`.  
**Očakávaný STOP/REVIEW:** ak surový `F` nesie `k^p`, adapter sa nesmie
vytvoriť; treba odvodiť alebo explicitne doplniť fyzikálnu normalizáciu v
samostatnej vetve. To nie je smrť A2-K4 ani výsledok G8.

Limit: interný 10 s, externý 15 s; pred behom `py_compile`, `--help` a
`--smoke`. Výstup je immutable JSON a nemení skóre.
