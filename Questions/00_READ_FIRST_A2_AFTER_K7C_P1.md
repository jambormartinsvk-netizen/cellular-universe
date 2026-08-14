# READ FIRST — A2 po K7c P1

Dátum: 2026-07-15

Aktuálne: **A2-K4 je ŽIVÁ na `66.5/100`; P1 reprodukcia PASS, fyzikálna K7c evolúcia REVIEW.**

- Čistý skript 197 bez legacy adaptívneho bloku presne reprodukoval starý 100/200 a 200/400 výsledok.
- Rozdiely sú `1.44327268769215e-6` a `3.93123964056996e-6`.
- Pomer je `0.367129`, nie očakávaných približne 16; dominantná zložka je `M`.
- Toto vylučuje nedosiahnuteľný `solve_ivp` ako príčinu, ale nepotvrdzuje fyzikálnu konvergenciu.
- Skóre sa nemení; P1 je regresný audit.
- Aktuálny corpus checker je 198: 202 ostatných `.py`, 69 karanténnych položiek.
- Skript 186 je neúplný a nesmie sa spustiť.
- Najbližší vedecký krok je P2: nový číslovaný term-by-term ledger `M'` na uložených stavoch, bez zmeny RHS.

Kľúčový audit: `Audit/A2_K4_K7C_P1_CLEAN_STANDALONE_RK4_FINAL_AUDIT_2026-07-15.md`.

## Orientačná mapa po organizačnom audite

Aktuálna cesta je A1K1 → A2K4 → C7.7c → K7 → K7c. K1 až K6 boli
alternatívne numerické formulácie C7.7c, nie rovnaké etapy a/b/c. Písmená
vznikli až v K7: K7a je projektovaná algebra/Jacobián, K7b počiatočné
koeficienty a constrainty bez ODE, K7c evolúcia/konvergencia a K7d plánovaná
úplná activity brána. Preto neexistuje historický K1c; K1 sa zastavila na 28
nerozlíšených activity kontrolách.

V scorecarde C7-W1 má aktuálna K7:

- validovanú podporu 40/100;
- blokujúcu evidenciu G5 konvergencie 20/100;
- otvorenú váhu 40/100;
- auditované pokrytie PASS+FAIL 60/100.

Toto nie je pravdepodobnosť ani náhrada hĺbky celej A2-K4 66.5/100.
Najvyššiu prioritu má G5, pretože jej váha je väčšia než váha runtime,
formátových a korelovaných reprodukčných monitorov.

Autoritatívne organizačné podklady:

- Audit/A2_K4_C7_7C_K1_K7_LINEAGE_GATE_COVERAGE_AND_WEIGHT_AUDIT_2026-07-15.md
- Questions/DIRECTORY_STRUCTURE_AND_MIGRATION_PROPOSAL_V2_STATIONS_ROUTES_AND_AUDIT_THREADS_2026-07-15.md
- Questions/BASESCRIPTS_VERSIONED_ARCHITECTURE_AND_MIGRATION_2026-07-15.md
- Questions/EXTERNAL_AUDIT_PACKAGE_STANDARD_AND_K7C_RK4_PILOT_2026-07-15.md
## Stabilné ID a ochrana vedeckého P2

Staré krátke P2 má odteraz plné ID
SCI-A2K4-C7G5-K7C-P2-MLEDGER. Jeho rozsah sa organizačnou zmenou nezmenil:
nový číslovaný diagnostický skript na uložených checkpointoch, deväť členov
M-prime, porovnanie float64, math.fsum a 80-dps referencie, bez zmeny RHS a
bez bodov. Skript 186 zostáva DO_NOT_RUN_TECHNICAL.

Organizačné fázy sa označujú ORG-V2-P1/P2, base pilot
BASE-V001-PARITY-197 a externý audit AUD-C7G5-K7C-P1-RK4.

- glossary: Questions/00_ABBREVIATION_AND_IDENTIFIER_REGISTER_SK.md
- scope freeze P2: Questions/A2_K4_K7C_P2_SCOPE_FREEZE_AND_ORG_NAMESPACE_2026-07-15.md
- neinvazívny strom: tracks/00_READ_FIRST.md
## Supersession po P2

Tento dokument zachováva stav po P1. Aktuálny pokračovací bod je
`Questions/00_READ_FIRST_A2_AFTER_K7C_P2.md`. P2 už prebehlo: jednoduchá
fsum hypotéza je STOP a aktívna je P3a kontrola presných nulových
koeficientov. Staré P1 čísla ani ich význam sa nemenia.

