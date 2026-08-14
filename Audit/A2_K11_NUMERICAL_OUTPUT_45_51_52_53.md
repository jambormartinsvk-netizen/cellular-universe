# A2-K11 — zachovaný numerický výstup skriptov 45, 51, 52 a 53

**Dátum:** 2026-07-13  
**Účel:** reprodukovateľná stopa aj pre neúspešné behy

## Skript 45 — opravená revízia auditovaná v tomto kroku

**SHA-256:**
`61558FAF0D08E35B9B6D6CAFE30FFD55FD2E3FB2399D2A69F92D534EFC590CB1`

| Beh | Transfer relatívnej rýchlosti | max. absolútne `00` rezíduum | globálne relatívne rezíduum |
|---|---:|---:|---:|
| coupled coarse, krok `1.25e-4` | `1.8941192609735247e-13` | `8.254964054289152e-10` | `1.0` |
| coupled fine, krok `6.25e-5` | `1.8941939847209883e-13` | `8.255147703519102e-10` | `1.0` |
| coupled half-k | `1.8942041453433046e-13` | `8.255147703519103e-10` | `1.0` |
| `uncoupled_fine`, v skutočnosti iba `gamma=0` | `2696.770544149779` | `658.5927739401154` | `1.0` |

Ďalšie vytlačené hodnoty:

```text
coupled_to_null_transfer_gain = 7.023934568071226e-17
step_log_transfer_relative_difference = 1.3466416117156893e-6
k_log_transfer_relative_difference = 1.8310658508698322e-7
solver rtol = 1e-8
solver atol = 1e-10
printed verdict = PASS_S8_K1b_SUPERHORIZON_GATE
audited verdict = REJECTED PASS
```

`step_converged` bolo `true` iba cez vetvu `or is_damped`. Constraint bol
označený za kontrolovaný iba cez absolútny prah napriek relatívnej hodnote
`1.0`.

## Skript 51 — audit znamienok a úplnejších rovníc

- prvý beh bol ukončený timeoutom po približne `124 s`;
- druhý beh dokončil konečné plusové vetvy, ale pri testovaní predloženého
  mínusového projektora prešiel Radau do overflow a následne `inf/NaN` po
  približne `165 s`;
- keďže pád nastal pred serializáciou, skript 52 zachoval už konečné vetvy
  bez opakovania analyticky anti-dampingovej vetvy;
- tento pád sa nemaže: je súčasťou dôvodu, prečo predložené mínusové
  znamienko nemožno označiť za drag.

Poznámka k staršej formulácii v docstringu 51: veta, že skript 45 ostal
nezmenený, sa vzťahovala na snapshot viditeľný pri vzniku skriptu 51.
Skript 45 bol neskôr používateľom opravený; preto tento audit vždy používa
vyššie uvedený SHA-256 a nie názov súboru ako identitu revízie.

## Skript 52 — konečné vetvy opravených rovníc

| Beh | Transfer | max. relatívne aktívne `00` rezíduum |
|---|---:|---:|
| K1 energy transfer, bez drag | `1.78002595` | `1.459e-4` |
| fyzikálny plusový drag, krok `2.5e-4` | `1.9548997e-12` | `1.0` |
| fyzikálny plusový drag, krok `1.25e-4` | `1.3399033e-12` | `1.0` |
| plusový drag, polovičné `k` | `1.9548265e-12` | `1.0` |

```text
drag_gain_relative_to_correct_K1 = 7.5274e-13
step_log_transfer_relative_difference = 1.38172e-2
k_log_transfer_relative_difference = 1.389e-6
```

Tieto behy ukázali smer tlmenia pri plusovom projektore, ale neprešli
krokovou konvergenciou a konečné amplitúdy boli pod absolútnou toleranciou.
Hodnota `1.7800` je absolútny transfer vo zvolenom móde, nie historický
K1 coupled/null faktor `2.014e5`; tieto dve veličiny sa nesmú zameniť.

## Skript 53 — test tolerančnej podlahy a linearity

Rovnaká lineárna sústava bola spustená s počiatočnou amplitúdou `1` a
`10^12`.

| Beh | Transfer | max. relatívne aktívne `00` rezíduum |
|---|---:|---:|
| amplitúda `1`, krok `2.5e-4` | `1.9548996937140064e-12` | `1.0` |
| amplitúda `1e12`, krok `2.5e-4` | `3.373703900635275e-15` | `1.0` |
| amplitúda `1e12`, krok `1.25e-4` | `3.3827438162234293e-15` | `1.0` |

```text
amplitude_log_transfer_relative_difference = 0.19092301942036957
resolved_step_log_transfer_relative_difference = 8.031007911756745e-5
amplitude_scaling_1e12 = false
resolved_step_convergence = false
resolved_constraint_relative = false
verdict = FAIL_NUMERICAL_RESOLUTION
```

Lineárny transfer nie je invariantný voči spoločnému škálovaniu amplitúdy.
To dokazuje, že numerický výsledok tlmenia zatiaľ nie je rozlíšený.

## Kanonický záver

- žiadny z týchto behov nedokazuje `S8`;
- `PASS` skriptu 45 je zamietnutý;
- neúspešné skripty, výstupy a dôvody zostávajú uložené;
- správne formulovaný momentum-transfer kandidát pokračuje iba ako
  `A2-K11 PREŽÍVA FORMULAČNÚ BRÁNU — 15/100`.

