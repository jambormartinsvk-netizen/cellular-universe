# A2-K4 / C7.7c / K7c.1 — predregistrácia projektovaného 13-zložkového stavu

Dátum: 2026-07-15  
Vstup: K7a PASS a K7b PASS  
Rozsah: reprezentácia a round-trip bez ODE, bez bodov

## Zmrazená druhová báza

Pôvodné poradie je

```text
[h, eta, delta_gamma, delta_fs, delta_b, delta_c,
 U_gamma, U_fs, sigma_fs, L3_fs, L4_fs, delta_f, U_f]
```

## Zmrazená projektovaná báza

K7c používa presne 13 premenných

```text
[h, eta, delta_gamma, D, delta_b, delta_c,
 U_gamma, M, sigma_fs, L3_fs, L4_fs, delta_f, U_f]
```

kde

\[
D=\Omega_\gamma\delta_\gamma+\Omega_{fs}\delta_{fs}
 +\Omega_b\delta_b+\Omega_c\delta_c+\Omega_f\delta_f,
\]

\[
M=(2\Omega_\gamma+1.5\Omega_b)U_\gamma
 +2\Omega_{fs}U_{fs}+1.5\delta\Omega_fU_f.
\]

`D,M` **nahrádzajú** `delta_fs,U_fs`. Nie sú pomocnými 14. a 15. nezávislými premennými.

## Inverzné mapovanie

\[
\delta_{fs}=\frac{D-\Omega_\gamma\delta_\gamma-\Omega_b\delta_b
-\Omega_c\delta_c-\Omega_f\delta_f}{\Omega_{fs}},
\]

\[
U_{fs}=\frac{M-(2\Omega_\gamma+1.5\Omega_b)U_\gamma
-1.5\delta\Omega_fU_f}{2\Omega_{fs}}.
\]

Transformácia je prípustná iba pri `Omega_fs > 0`. V uvedenom poradí má absolútny determinant `2*Omega_fs^2`.

## Povinné vstupy

- autoritatívne NID/NIV deep/shallow stavy exportu 174;
- rovnaký background, parametre a poradie ako K7b;
- rovnaké `D,M` definície ako K7a/K7b;
- žiadne náhodné vektory ako náhrada fyzikálnych stavov.

## Brány

1. obe bázy majú presne 13 jedinečných mien;
2. transformácia má rank 13 na všetkých štyroch plochách;
3. `Omega_fs > 0` a determinant súhlasí s `2*Omega_fs^2` relatívne do `1e-13`;
4. `cond_2(T) < 10`;
5. fyzikálny round-trip `y -> z -> y` má max škálovanú chybu `<5e-14`;
6. rekonštruované `delta_fs,U_fs` súhlasia s autoritatívnym stavom `<5e-14`;
7. export a každý podproces majú vnútorný aj vonkajší limit.

## Rozhodovanie

- PASS všetkých štyroch plôch povoľuje K7c.2/K7c.3 — krátky projektovaný ODE test.
- Algebraická, ranková alebo fyzikálna round-trip chyba pri správnych vstupoch zabíja túto reprezentáciu K7c.1.
- Timeout, parser alebo chýbajúci export je REVIEW, nie smrť K4.
- Tento krok nemení `66.5/100`.
