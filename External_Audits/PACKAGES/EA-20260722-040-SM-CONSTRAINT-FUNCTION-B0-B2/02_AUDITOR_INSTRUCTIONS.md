# Pokyny externému auditorovi EA-040

1. Auditujte iba presnú otázku a hranicu T1 z dokumentu 00.
2. Z koreňa projektu spustite R6 package preflight cez PowerShell 7+ a
   zapíšte presný príkaz, exit code a wall time.
3. Overte manifest `15/15`, source/copy paritu, prázdnu runtime mapu pri
   nulových `REPRO` súboroch, package počet `22`, response `1`, nulové
   duplicate physical hash groups a nulové
   dočasné súbory.
4. Nevykonávajte Python. Balík nemá výpočtový runtime ani generated JSON.
5. Nezávisle skontrolujte rozmery `Q_D=R_J E_J`, `nu_J`, `epsilon_J`, `j_D`
   a slabý limit `j_s~(2/g_*) nu_J epsilon_J^3`.
6. Overte znamienka a faktor `a^3` v integrovanej energetickej identite.
7. Skontrolujte, že okamžitý prompt branch, sekvenčný prechod hmoty do
   popola a kohortová completion diagnostika nie sú zmiešané do jedného
   neoznačeného mechanizmu.
8. Pri B0/B1 vypíšte všetky predpoklady potrebné pre záver. Ak z nich
   neplynie uvedený scope, označte presnú chybu; nerozširujte záver na
   všetky možné parné mechanizmy.
9. Skontrolujte, že `2/g_*` je iba podmienený high-temperature birth ratio,
   nie druhý multiplikátor energie a nie pozorovaný zákon.
10. Posúďte, či B2 naozaj ponecháva samostatne otvorené eventové,
    relaxačné a iné prompt operátory a či bez vyšších momentov netvrdí
    Poissonovský šum.
11. Každé tvrdenie označte evidence tagom a každú odchýlku klasifikujte ako
    package-integrity, formal, dimensional, conservation, physical,
    documentation alebo scope/tier.
12. Vlastnú novú funkciu auditora uveďte iba ako neautoritatívne
    odporúčanie a `DECLARED_DEVIATION`; nesmie zmeniť tier ani projektový
    verdikt.
13. Aplikujte `EVIDENCE/015` ako exact AR66.2 formula-provenance checklist;
    textový scope audit nesmie byť povýšený na computed alebo physics PASS.

Povinné ledger termíny: `generated JSON`, `exit code`, `wall time`,
`odchýlka`.
