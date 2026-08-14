# Erratum 66B — SymPy `charpoly` vytvoril menovca s inými predpokladmi

**Dátum:** 2026-07-14  
**SHA-256 verzie po oprave JSON a pred opravou 66B:**
`AE67B3A4DC399A081BE9C81E88230D2D50E6C3649C164D2364C0A41F445AB0FA`

Druhý beh úspešne dokončil všetky integrácie. Vypísal zhodné faktorizácie,
ale kontrola `characteristic_check` vrátila `false`. Diagnostika ukázala, že
`matrix.charpoly(p)` vytvoril nový symbol s rovnakým menom `p`, ale s inými
SymPy predpokladmi:

```text
same_symbol False
```

Rozdiel preto obsahoval dve algebraicky totožné skupiny zapísané cez dva
interné symboly. Nešlo o rozdiel polynómov ani fyzikálnych rovníc.

Oprava počíta charakteristický polynóm priamo ako

```text
det(p I - M)
```

s pôvodným symbolom `p`. Matica, očakávaná faktorizácia, numerické
eigenvalues, integrácie, prahy a fyzikálne výsledky sa nemenia. Celý skript
sa po oprave musí znovu spustiť; druhý beh zostáva diagnostickým neúspechom,
nie fyzikálnym verdiktom.

