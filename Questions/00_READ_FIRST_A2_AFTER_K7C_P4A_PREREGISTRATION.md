# READ FIRST — A2 po preregistrácii K7c P4a

Dátum: 2026-07-15

Aktuálne: **P3b kroková RK4 brána PASS; P4a metódová/tolerančná brána je
PREREGISTERED / NOT RUN. A2-K4 ostáva `66.5/100`.**

P4a bude porovnávať rovnakú kanonickú RHS a P3b grid400 endpoint s tromi
samostatnými prípadmi:

- DOP853 `rtol=1e-9`, `atol=1e-11`;
- DOP853 `rtol=1e-11`, `atol=1e-13`;
- Radau `rtol=1e-10`, `atol=1e-12`.

Štyri metódové/tolerančné rozdiely musia byť `<=1e-8`. Každý prípad má
vlastný interný 20 s a externý 25 s limit a vlastný immutable JSON. Offline
agregát nesmie spúšťať deti.

Najbližšie poradie:

1. vytvoriť jednopřípadový runner 209 bez spustenia;
2. skriptom 210 dokázať source-delta paritu fyzickej RHS so skriptom 205;
3. vykonať syntax/CLI preflight a versioned corpus checker 211;
4. až potom po jednom spustiť tri prípady;
5. skript 212 iba offline agreguje výsledky.

Autoritatívna preregistrácia:
`Questions/A2_K4_C7_7C_K7C_P4A_G5_METHOD_TOLERANCE_PREREGISTRATION_2026-07-15.md`.
