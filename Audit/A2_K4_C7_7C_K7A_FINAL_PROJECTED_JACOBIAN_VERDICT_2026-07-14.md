# A2-K4 / C7.7c / K7a — konečný verdikt projektovaného Jacobiánu

**Dátum:** 2026-07-14  
**Rozsudok K7a:** **PASS algebraickej/Jacobiánovej brány**  
**Rozsudok A2-K4:** **ŽIVÁ**  
**Jemná hĺbka:** bez zmeny, **66.5/100**  
**C7.7c:** stále otvorená; evolúcia nebola vykonaná

## 1. Čo K7a overila

K7a nahradila zle podmienené druhové premenné `delta_fs` a `U_fs` kompenzovanými zdrojmi

\[
D=\sum_A\Omega_A\delta_A,
\]

\[
M=(2\Omega_\gamma+1.5\Omega_b)U_\gamma
  +2\Omega_{fs}U_{fs}+1.5\delta\Omega_fU_f.
\]

Pre časovo závislú transformáciu \(z=T(x)y\) bol použitý úplný Jacobián

\[
A_z=(T'+TA_y)T^{-1}.
\]

Audit overil:

- kladné \(\Omega_{fs}\) a invertibilitu transformácie;
- prijateľnú podmienenosť \(T\);
- explicitne odvodené projektované rovnice proti transformovanému Jacobiánu;
- zamrznuté spektrum proti pôvodnej fyzikálnej báze;
- nulový radiačný limit;
- časovo závislý člen \(T'T^{-1}\);
- NID/NIV na hlbokom aj plytkom povrchu.

## 2. Konečné výsledky J4b

| Mód/povrch | rel. Frobeniova chyba | max. abs. chyba | \(\kappa_2(T)\) | \(\rho(A_z)\) | chyba bezpečného \(T'\) | Stav |
|---|---:|---:|---:|---:|---:|---|
| NID/deep | `9.94e-18` | `2.77e-16` | `4.7953814` | `3.4441515426` | `1.88e-16` | PASS |
| NID/shallow | `1.56e-17` | `4.44e-16` | `4.7953816` | `3.4441514022` | `2.14e-16` | PASS |
| NIV/deep | `9.94e-18` | `2.77e-16` | `4.7953814` | `3.4441515426` | `1.88e-16` | PASS |
| NIV/shallow | `1.56e-17` | `4.44e-16` | `4.7953816` | `3.4441514022` | `2.14e-16` | PASS |

Rezíduum nulového limitu bolo na všetkých štyroch povrchoch presne 0 v reportovanej double aritmetike. Použitý výpočet je

```text
ell = denominator_x / denominator
```

nie numericky nestabilné `ell = 2*(q+1)`.

## 3. Úplná postupnosť neúspešných nastavení

| Podkoľaj | Výsledok | Dôvod | Zachovaný dôkaz |
|---|---|---|---|
| J1 | mŕtva numerická podkoľaj | double centrálna diferencia odčítala dve matice rádu 1 pri \(T'\sim10^{-8}\); najlepšia rel. chyba `6.28e-6` | skript 159 a audit J1 |
| J2 | neuzavrela celý test | 80-ciferná FD prešla až na `1.67e-33`, ale stará double analytická cesta sa líšila o `1.51e-9` | skript 160 a audit J2 |
| J3 | PASS | priame \(B'/B\) odstránilo katastrofické odčítanie bez zmeny rovníc; chyba približne `2e-16` | skript 161 |
| J4/163 | mŕtva agregátorová podkoľaj | parser preskočil úroveň `zero_integration_jacobian_diagnostic`; fyzikálne podtesty nezlyhali | skript 163 a samostatný audit |
| J4b/164 | PASS | opravená iba preregistrovaná cesta parsera; všetky štyri povrchy prešli | skript 164 |

Žiadny chybný skript ani jeho výpočet nebol zmazaný. Prahy sa po neúspechoch neuvoľnili.

## 4. Čo tento PASS neznamená

K7a nedokazuje:

- správnosť počiatočných Puiseuxových koeficientov `D,M` pre každý mód;
- zachovanie Einsteinových constraintov pozdĺž nenulovej trajektórie;
- krokovú konvergenciu projektovanej evolúcie;
- zhodu deep/shallow koncových stavov;
- plnú fotónovú/neutrínovú Boltzmannovu hierarchiu;
- fyzikálnu životaschopnosť K4 v A3.

Preto zostáva skóre `66.5/100` a C7.7c zostáva otvorená.

## 5. Ďalší krok

Nasleduje **K7b — koeficientová a constraintová brána bez ODE**. Až po jej PASS možno preregistrovať prvý krátky projektovaný evolučný beh.

## 6. Reprodukčné skripty

- `scripts/159_script_A2_K4_C7_7c_K7a_projected_jacobian_audit.py`
- `scripts/160_script_A2_K4_C7_7c_K7a_J2_high_precision_Tprime_audit.py`
- `scripts/161_script_A2_K4_C7_7c_K7a_J3_cancellation_safe_Tprime_audit.py`
- `scripts/162_script_A2_K4_C7_7c_K7a_J4_safe_projected_jacobian_audit.py`
- `scripts/163_script_A2_K4_C7_7c_K7a_J4_composite_projected_jacobian_gate.py`
- `scripts/164_script_A2_K4_C7_7c_K7a_J4b_composite_parser_corrected_gate.py`

