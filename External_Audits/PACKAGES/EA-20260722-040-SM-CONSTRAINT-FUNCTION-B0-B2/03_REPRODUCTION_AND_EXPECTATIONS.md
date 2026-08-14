# Statický audit a očakávania EA-040

EA-040 je T1 formula capsule. Povinný je package preflight a nezávislý
ručný audit rovníc; official Python vetva neexistuje.

```powershell
pwsh -NoProfile -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 `
  -PackagePath External_Audits\PACKAGES\EA-20260722-040-SM-CONSTRAINT-FUNCTION-B0-B2
```

Očakávanie: exit code `0`, všetky manifest/source/copy/runtime-map kontroly
PASS a wall time zapísaný auditorom.

## Povinné nezávislé kontroly

Auditor má bez preberania záveru dokumentu overiť:

1. rozmery
   `Q_D=[energia][objem]^-1[čas]^-1`,
   `R_J=[objem]^-1[čas]^-1`, `E_J=[energia]`;
2. bezrozmernosť
   `nu_J=R_J V_P t_P`, `epsilon_J=E_J/E_P` a
   `j_D=Q_D V_P t_P/E_P=nu_J epsilon_J`;
3. algebraický slabý limit prompt pary
   `j_s~(2/g_*)nu_J epsilon_J^3`;
4. integrovanú komovingú energetickú identitu vrátane tlakovej práce;
5. B0 rovnosť `R_sM,x=(2/g_*)y_x^2` iba pre deklarovaný prompt kandidát;
6. B1 nerovnosť `y_x<=exp(-3 delta N)` pri nezápornom odvode a jej
   logaritmický rád pre `delta=0.02297`, `N=1280`;
7. identifikovateľnosť: samotné pozadie určuje iba `R_J E_J`, nie oba
   faktory osobitne.

## Očakávaná hranica záveru

Správny audit môže potvrdiť mapu, nájsť presnú medzeru alebo odmietnuť
konkrétnu rovnicu. Nemôže z T1 balíka vyhlásiť odvodenú mikrofyziku,
jedinečnú funkciu, T2 reprodukciu, nový fyzikálny bod ani STOP celej teórie.

Žiadny generated JSON sa neočakáva. Ak auditor použije vlastný skript alebo
novú funkciu, ide o deklarovanú odchýlku a iba pomocnú kontrolu.

