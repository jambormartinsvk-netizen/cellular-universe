# Statický audit a očakávania EA-042

EA-042 je T1 family-map/formula capsule. Povinný je package preflight a
nezávislý ručný audit; official Python vetva neexistuje.

```powershell
pwsh -NoProfile -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 `
  -PackagePath External_Audits\PACKAGES\EA-20260723-042-B6B-FAMILY-MAP
```

Očakávanie: exit code `0`, všetky manifest/source/copy/runtime-map kontroly
PASS a wall time zapísaný auditorom.

## Povinné nezávislé kontroly

1. zostaviť klasifikačnú tabuľku rozlišovacích znakov MF1–MF4;
2. pri MF3/MF4 sledovať reservoir, event identity a všetky `Q_A^mu` tak,
   aby tá istá energia alebo udalosť nevstúpila dvakrát;
3. overiť C0 rozklad `S_D^mu=S_s^mu+S_M,birth^mu` a následný `M->C` transfer;
4. oddeliť proof of empty set od failure-to-find-a-witness;
5. overiť, že PH1 nevstupuje ako skrytá preferovaná rodina;
6. sledovať forward reťazec od kernelu cez perturbation moments po S8 a
   potvrdiť, že S8 nie je vstupom definície funkcie;
7. posúdiť, či analytická source-moment obálka na rovnakej hĺbke môže lacno
   vyradiť rodinu pred detailnou mikrofyzikou.

Správny audit môže potvrdiť scope, nájsť presnú medzeru alebo odmietnuť
konkrétnu časť mapy. Nemôže z T1 balíka vyhlásiť existenciu alebo
neexistenciu fyzikálnej funkcie, T2 reprodukciu, numerický S8 výsledok, nový
fyzikálny bod ani STOP teórie. Žiadny generated JSON sa neočakáva.
