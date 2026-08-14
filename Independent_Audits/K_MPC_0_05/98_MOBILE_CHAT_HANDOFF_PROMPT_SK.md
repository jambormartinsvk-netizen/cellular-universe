# Text na vloženie do mobilného chatu

Som autor teórie bunkového priestoru. Potrebujem, aby si bol prísny fyzikálny
auditor, nie obhajca teórie. Pomôž mi odvodiť alebo vyvrátiť zmysluplný
význam parametra `K_MPC=0.05`.

## Overený stav

V aktuálnej K7 formule je:

```text
z = k a/(H0 sqrt(Omega_r))
mu = H0 Omega_m/(sqrt(Omega_r) k)
g2 = 0.15 (H0/k)^2 sqrt(Omega_r)
D = 1 + mu z + z^p [1 + g2(1/(p+1)-1/2)z^2]
p = 3.93109
```

Presný audit dokázal:

```text
D(a,k) = 1 + Omega_m a/Omega_r + k^p A(a).
```

Teda `mu*z` a `g2*z²` sú nezávislé od `k`, ale palivový člen nie. Nemôžeme
preto súčasný zápis použiť ako univerzálny kozmologický background `H(a)`;
globálna expanzia nesmie závisieť od Fourierovho módu poruchy.

## Čo chcem riešiť

1. Vysvetli mi ľudskou rečou rozdiel medzi Fourierovým módom `k` a pevným
   fyzikálnym scale `k_*`.
2. Vytvor iba malé množstvo hypotéz, vždy s názvom, predpokladom,
   matematickým dôsledkom, novými parametrami a testom smrti.
3. Začni prioritne hypotézou:

```text
K-N2: pri palivovom term-e chýba normalizácia
(H0 sqrt(Omega_r)/k_*)^p,
takže fyzikálny palivový člen je úmerný a^p, nie (k a)^p.
```

4. Audituj, či táto normalizácia môže vyplynúť z bezrozmernosti alebo
mechanizmu siete, bez nového empirického fit parametra.
5. Alternatívne audituj K-N1: `K_MPC=0.05` je pevná inverse correlation
length siete `k_*`, nie Fourierov mód. Táto koľaj prežije len ak sa hodnota
odvodí z existujúcich konštánt teórie.
6. Označ ako mŕtve pre globálny background:
   - `K_MPC` je súčasne konkrétny Fourierov mód aj background scale;
   - 0.05 je len ľubovoľný publikačný pivot;
   - zmeniť `p` na 0 iba preto, aby zmizla k-závislosť.

## Pravidlá

- Nevymýšľaj nový parameter potichu.
- Hypotéza môže byť živá iba ak dá jediné k-nezávislé `H(a)`.
- Ak hypotéza zmení publikované predpovede, označ to ako dôvod na novú verziu
  a changelog, nie ako tichú opravu.
- Pri každej koľaji vypíš: stav, dôvod, ďalší test a čo by ju zabilo.
