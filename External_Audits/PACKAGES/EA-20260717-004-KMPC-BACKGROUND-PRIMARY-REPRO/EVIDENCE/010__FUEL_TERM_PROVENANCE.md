# Proveniencia palivového členu a význam `k`

**Stav:** `AUDITOVANÉ — zdroj exponentu je určený; normalizácia do globálneho backgroundu je REVIEW/STOP.`  
**Rozsah:** vysvetľuje, odkiaľ pochádza skorý palivový člen K4/K7. Neodvodzuje
mikroskopický pôvod samotnej interakcie `Q^mu`.

## 1. Čo je palivový člen

V skorom radiačnom limite nejde o holú hustotu paliva, ale o jej pomer k
žiareníu:

```text
y_f = rho_f/rho_r.
```

Pre A1-K1 je

```text
w_f = -1 + delta,
Q = lambda H0 rho_f,
rho_f,x = -3 delta rho_f - lambda (H0/H) rho_f,
rho_r,x = -4 rho_r.
```

Preto presne platí

```text
y_f,x = [4 - 3 delta - lambda H0/H] y_f.
```

Prvý exponent teda nevznikol fitovaním ani z Fourierovej fyziky:

```text
p = 4 - 3 delta = 3.93109  (pre delta = 0.02297).
```

Je to rozdiel medzi riedením radiácie (`a^-4`) a takmer-vákuového paliva
(`a^-3delta`). Ak by sa prenos paliva do popola v ranej ére zanedbal,
platilo by jednoducho `rho_f/rho_r propto a^p`.

## 2. Odkiaľ sa vzalo `z`

Pri odvodení skorých **porúch** sa zaviedla praktická bezrozmerná premenná

```text
z = k a/(H0 sqrt(Omega_r0)) = k/Hconf_r,
```

kde `Hconf_r = H0 sqrt(Omega_r0)/a` je konformný Hubbleov parameter čisto
radiačného pozadia. Zápisy K7 výslovne používajú aj `s=k/Hconf`.

Preto `k` v tomto kroku znamená **komovú Fourierovu vlnovú hodnotu práve
evolvovanej poruchy**. `z` je vhodná na superhorizontový rozvoj: meria,
aká je vlna veľká oproti konformnému horizontu. Nie je to v tomto odvodení
samostatne odvodená mierka bunkovej siete.

## 3. Ako vznikol celý skorý fuel/ash rad

V radiačnom limite `H = H0 sqrt(Omega_r0) a^-2`. Preto

```text
lambda H0/H = lambda a^2/sqrt(Omega_r0) = g2 z^2,
g2 = lambda (H0/k)^2 sqrt(Omega_r0).
```

Rovnica pre palivo sa integruje na

```text
y_f = Phi z^p exp(-g2 z^2/2)
    = Phi z^p [1 - g2 z^2/2 + O(z^4)].
```

To je pôvod implementovaného výrazu

```text
fuel_piece = Phi z^p,
Omega_f = fuel_piece (1 - g2 z^2/2)/D.
```

Z rovnakého prenosu `Q` vzniká skorý popol (CDM/ash) v poradí

```text
(rho_ash/rho_r)_source = Phi g2 z^(p+2)/(p+1) + O(z^(p+4)).
```

Členy palivo a popol teda tvoria energeticky párovaný skorý rad; koeficienty
`-g2/2` a `g2/(p+1)` nie sú nezávislé voľné parametre.

## 4. Kde vzniká problém pre globálny background

V poruchovom rozvoji možno bez škody písať `y_f=Phi z^p`, pretože pracujeme
s **jedným vybraným módom** `k` a `Phi` je koeficient definovaný v týchto
súradniciach.

Fyzikálny homogénny pomer však musí mať tvar

```text
y_f(a) = A_f a^p + O(a^(p+2)),
```

kde `A_f` je nezávislé od aktuálne evolvovaného Fourierovho módu. Porovnanie
oboch zápisov dáva povinné mapovanie koeficienta

```text
Phi(k) = A_f [H0 sqrt(Omega_r0)/k]^p.
```

Inými slovami: faktor `k^p` v `z^p` sa musí zrušiť v koeficiente `Phi`, alebo
sa musí nahradiť fyzikálne odvodenou pevnou referenčnou škálou `k_*` spolu s
normalizáciou. Bez toho sa z poruchovej súradnice omylom stane parameter
globálneho `D(a)` a následne `H_K4(a)`.

## 5. Čo presne urobil starý kód

Skripty K7/K7c nastavili `k_mpc` (v integrovanom behu `K_MPC`) na `0.05` a
pri palive použili `Phi=1`, teda priamo `fuel_piece=z^p`. Tým vybrali jednu
normalizáciu pre jeden konkrétny mód/pivot, ale nezdokumentovali prechod na
`A_f a^p`. To vysvetľuje presný výsledok RUN-FULL-002:

```text
D(a,k) = 1 + Omega_m a/Omega_r + k^p A(a).
```

Výsledok nie je smrť palivového mechanizmu ani exponentu `p`; je to STOP
pre použitie tohto nenormalizovaného poruchového zápisu ako univerzálneho
FLRW backgroundu.

## 6. Záväzný ďalší krok

Koľaj K-N2 má odvodiť `A_f` (alebo ekvivalentne `Phi(k)`) zo zmrazených
konštánt teórie. Musí potom súčasne prejsť:

1. `D_univ(a)` je nezávislé od voľby Fourierovho módu;
2. `H_K4^2=H0^2 Omega_r0 D_univ/a^4` je kladné a správne normalizované dnes;
3. normalizácia nepridá nový empirický fit;
4. skorý fuel/ash rad a energetická bilancia zostanú konzistentné.

## Proveniencia

- `Questions/A1_rozhodnutie_Q19_a_kovariantny_background_v3.18.md`, FRW
  rovnice pre `rho_f`, `rho_c`, `rho_r` a `Q=lambda H0 rho_f`.
- `Questions/A2_K4_BR3C_A_PREREGISTRATION_AND_BREADTH_TRIAGE_DECISION.md`,
  definície `z=k a/(H0 sqrt(Omega_r))` a `s=k/Hconf`.
- `scripts/128_script_A2_K4_3b_RG_BR3B2g_exact_order_and_hierarchy_audit.py`,
  normalizácia `(rho_f/rho_r)/(Phi z^p)` a párovaný ash rad.
- `scripts/213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py`,
  realizácia `K_MPC=0.05`, `fuel_piece=z^p` a `Phi=1` implicitne.
