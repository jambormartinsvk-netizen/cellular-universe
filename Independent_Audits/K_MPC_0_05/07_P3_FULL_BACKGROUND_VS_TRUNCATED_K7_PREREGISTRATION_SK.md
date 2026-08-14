# K-N2/P3 — predregistrácia: plný A1 background verzus skrátený K7 rad

**Stav pred behom:** `PRIPRAVENÉ`  
**Skript:** `scripts/235_script_KMPC_002_full_A1_vs_truncated_K7_background.py`  
**Vonkajší limit:** 10 s. **Vnútorný limit:** 5 s.

## Čo sa počíta ľudskou rečou

Zoberie sa rovnaké zmrazené A1 pozadie, z ktorého P2a určila
`A_f=7809.27010196`, a jeho plná Friedmannova funkcia sa zapíše

```text
D_A1(a) = E_A1(a)^2 a^4 / Omega_r0.
```

Porovná sa so skorým, po `k`-cancelácii opraveným K7 radom

```text
D_K7,trunc(a) = 1 + (Omega_m0/Omega_r0)a
  + A_f a^p [1 + (1/(p+1)-1/2) lambda a^2/sqrt(Omega_r0)].
```

Test neobsahuje nový fit, ODE porúch ani CLASS. Pýta sa iba, či možno
skrátený K7 rad poctivo extrapolovať ako plný background až po `a=1`.

## Očakávania a rozsudok

- **A1-PASS:** `D_A1` je konečné a kladné na `x=-18,-16,...,-2,0`.
- **K7-PASS:** `D_K7,trunc` je kladné na celom intervale `a in [exp(-18),1]`.
- **K7-STOP:** prechod K7 radu cez nulu zabíja iba tvrdenie, že je plným
  neskorým backgroundom; skorá asymptotika a výsledok P2a sa spätne nemenia.
- **Bezpečnostný STOP:** nekonečnosť, timeout alebo nekladný A1 background
  znamená, že P3 nemožno uzavrieť.

## Ďalší postup

Pri A1-PASS + K7-STOP musí budúca formulácia používať presné `D_A1(a)`, nie
extrapolovaný skorý rad. Pri dvojitom PASS by ešte nasledovala kontrola
presnosti a dnešnej normalizácie.

## Poznámka k prvému technickému pokusu (2026-07-15)

Prvý beh skončil pred verdiktom na chýbajúcom checkpointovom zázname
`x=-16.0` (PF-037). Chybné poradie cieľov nezmenilo rovnice ani vstupy a
nevytvoril sa výsledný JSON; identická predregistrovaná brána sa opakuje po
oprave poradia.

## Výsledok druhého behu

**A1-PASS, K7-STOP.** Úplný výsledok a presné čísla sú v
`08_P3_FULL_BACKGROUND_VS_TRUNCATED_K7_RESULT_SK.md`. Skončila iba
extrapolácia skráteného K7 radu na celý background; P2a ani jeho skorý limit
sa tým neprepisujú.
