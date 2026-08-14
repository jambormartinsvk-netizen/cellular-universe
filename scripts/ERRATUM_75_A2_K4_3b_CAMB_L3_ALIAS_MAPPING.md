# Erratum skriptu 75 — aliasy `J2/G2` pri `ell=3`

**Dátum:** 2026-07-14  
**Pôvodný skript:** `75_script_A2_K4_3b_exact_CAMB_hierarchy_coefficient_crosscheck.py`  
**Exit code pôvodného behu:** `1`  
**Fyzikálny rozsudok:** žiadny; ide o chybu audítorského mapovania aliasov

## Pozorovaný výsledok

Z 22 symbolických porovnaní bolo 20 nulových. Nenulové boli iba

```text
J_l3: 3*k*(-J_2(t) + pi_g(t))/7
G_l3: 3*k*(-G_2(t) + pi_r(t))/7
```

## Príčina

Lokálny `camb.symbolic` po zostavení hierarchy nahrádza

```text
J_2 -> pi_g
G_2 -> pi_r
J_1 -> q_g
G_1 -> q_r.
```

Skript 75 mapoval aliasy `J1/G1`, ale pri očakávanej pravej strane pre
`ell=3` nezamenil predchádzajúci multipól `J2/G2`. Rezíduá preto merali iba
rozdiel názvov symbolov.

## Oprava

Pôvodný skript a zlyhaný výstup sa zachovávajú. Následný skript 76 mapuje
oba páry aliasov a opakuje všetkých 22 exact porovnaní s rovnakým časovým
limitom. K4.3b sa podľa skriptu 75 nezabíja.

