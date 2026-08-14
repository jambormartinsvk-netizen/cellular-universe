# ERRATUM skriptov 38/39 — skalárna entalpia v 0i constrainte

**Dátum:** 2026-07-13  
**Neúspešný beh:** skript 38  
**Opravený nástupca:** skript 39

Skript 38 použil v 0i Einsteinovom zdroji a v počiatočnom nulovaní celkovej
hybnosti výraz

```text
X_f E^2 varphi_x^2/3,
```

čím započítal `X_f` dvakrát. Z kanonickej identity

```text
varphi_x^2 = 3 delta X_f/E^2
```

vyplýva správne

```text
(rho_phi+p_phi)/(3 H0^2 Mpl^2)
= E^2 varphi_x^2/3
= delta X_f.
```

Chybu odhalila povinná 00 brána: globálne relatívne rezíduum skriptu 38 bolo
`0.1066`, vysoko nad prahom `1e-5`. Jeho fyzikálny transfer sa preto nesmie
citovať.

Skript 39 opravuje iba túto implementáciu. Rovnice pohybu, počiatočný fyzikálny
mód, kroky, vlnové čísla a pass/kill prahy zostávajú rovnaké. Skript 38 sa
nemaže, aby zostala úplná stopa chyby a jej odhalenia.
