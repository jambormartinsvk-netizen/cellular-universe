# Statický audit a očakávania EA-041

EA-041 je T1 formula/definition capsule. Povinný je package preflight a
nezávislý ručný audit; official Python vetva neexistuje.

```powershell
pwsh -NoProfile -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 `
  -PackagePath External_Audits\PACKAGES\EA-20260722-041-SM-EVENT-CATALOG-LINEAGE-B3-B5
```

Očakávanie: exit code `0`, všetky manifest/source/copy/runtime-map kontroly
PASS a wall time zapísaný auditorom.

## Povinné nezávislé kontroly

1. pre F1–F3 dosadiť `nu_J` a `epsilon_J` do `nu_J epsilon_J`;
2. pri distribuovanej energii overiť, že prvý a steam-weighted moment sa
   nesmú nahradiť funkciou priemernej energie;
3. v A7 identifikovať párový `Gamma rho_f` transfer a neprítomnosť
   produktového `+3 delta rho_f` protipólu;
4. v A12 overiť, že energia udalosti zostáva otvorená;
5. spočítať presných osem Q4-P0 definícií a oddeliť ich od G0/AR46 momentov;
6. skontrolovať, či minimálny nový passport uzatvára background aj
   perturbovaný štvorvektorový/momentový ledger bez cieľového fitu.

Správny audit môže potvrdiť scope, nájsť presnú medzeru alebo odmietnuť
konkrétnu rovnicu. Nemôže z T1 balíka vyhlásiť odvodenú mikrofyziku,
jedinečnú funkciu, T2 reprodukciu, nový fyzikálny bod ani STOP teórie.
Žiadny generated JSON sa neočakáva.
