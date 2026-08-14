# Akčný plán v3.18 — K7b P0 uzavreté

Dátum: 2026-07-15

## Dokončené

- fail-open `.get()==.get()` odstránené guarded kontrolou existencie a presného typu;
- pozitívne NID fingerprinty 175/192 exact;
- NIV deep/shallow PASS;
- tri negatívne fault-injection prípady fail-closed;
- PF-012 a timeout 193 zachované s dôvodmi a nástupcami;
- korpusový checker 196 a register 200/68 zosúladené.

## P1 — nasleduje

Vytvoriť čistý samostatný RK4 nástupca 184/185 podľa `Questions/A2_K4_C7_7C_NEXT_RUN_PREREGISTERED_EXPECTATIONS.md`:

1. odstrániť iba nedosiahnuteľný legacy `solve_ivp` blok;
2. nemeniť RHS, seed, škálu, closure ani kroky;
3. reprodukovať 100/200 rozdiel `~1.44327e-6`, 200/400 `~3.93124e-6`, pomer `0.36–0.375`, dominantnú zložku M a verdict REVIEW;
4. exact regresná odchýlka endpoint metrík najviac `1e-12`;
5. každý nezávislý prípad checkpointovať podľa AR57;
6. P1 nepridáva body.

## P2 — po P1

Vytvoriť nový číslovaný M-prime term ledger; skript 186 sa nemení ani nespúšťa. Až ledger rozhodne medzi fsum, algebraickým preusporiadaním a vyššou presnosťou.

## Údržba pred Git/Zenodo

Po P1/P2 vykonať logické rozdelenie dokumentácie, aktualizovať aktuálny checker/register, zjednotiť read-first odkazy a až potom pripraviť Git commit a Zenodo changelog. P0 samo nemení tabuľku fyzikálnych predpovedí.
