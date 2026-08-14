# KMPC-058 — C2 Fourier support-guard successor: predregistrácia

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → S-C0 / C2 Fourier gate`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Predchodca:** KMPC-057 / PF-077; bez fyzikálneho atómu a bez JSON

## Povolená jediná zmena

KMPC-058 zachová presne tú istú maticu desiatich atómov, rovnice, supporty,
M1 depth, prahy, poradie, runtime a rozhodovací strom z dokumentu 104.
Versioned overlay smie zmeniť iba chybný contract guard:

- historická S1 mapa ostáva evidovaná ako `initial_extended`, nie ako dnešný
  uzavretý C1 support;
- aktuálna mapa je presne AD `[0,2]`, CDI/BI/NID `[0,5]`, NIV `[-1,4]`;
- jej autorita je viazaná na už zmrazené hashe KMPC-031/040/046/053/056;
- audit support je vždy aktuálny horný rád plus dva;
- negatívny fixture musí dokázať, že stará mapa pre CDI/BI/NID/NIV sa už
  nesmie prijať ako closed-C1 mapa;
- overlay musí po každom volaní obnoviť pôvodných ownerov.

Žiadna numerická korekcia, zmena fyziky, tolerancie ani prenos koeficientov
z `k=.05` nie sú dovolené. Prvý non-PASS atóm zastaví automatické poradie.

## Artefakty a proces

- overlay: `scripts/baseScripts/p5_general_synchronous/c2_fourier_coverage_v2_c1_closed_support.py`;
- runner: `scripts/302_script_KMPC_058_P5_3g7_C2_Fourier_coverage_guard_successor.py`;
- raw atómy a agregát používajú `KMPC_058`, aby sa technický pokus nemiešal
  s neplatným KMPC-057;
- preflight: compile overlay/runner, help, behaviorálny smoke s PF-077
  negatívnym fixture;
- potom najviac jeden official proces na atóm a agregát, interný limit
  presne `4.8 s`, vonkajší `10 s`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | PF-077 staticky izolovaný na obsolete-vs-closed support parity | `ROOT_CAUSE_CLOSED` |
| 2026-07-18 | fyzika, matica, supporty, prahy a stop pravidlá prevzaté bez zmeny z dokumentu 104 | `PREREGISTERED` |
| 2026-07-18 | overlay SHA `B563B919436B129E9B3C52AC011DC3190C6BA4773BD2B8094C35671AEE1B8A15`; runner SHA `AF74C032408F9232C3E185A2E79AB10A0AB7104AD6ADC26E85DA189666DB3A64`; žiadny KMPC-058 output | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile/help PASS; smoke exit `1` detailne dokázal old false checks iba `BI,CDI`, nie predpokladané štyri módy; PF-078; bez atómu/JSON | `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT` |
