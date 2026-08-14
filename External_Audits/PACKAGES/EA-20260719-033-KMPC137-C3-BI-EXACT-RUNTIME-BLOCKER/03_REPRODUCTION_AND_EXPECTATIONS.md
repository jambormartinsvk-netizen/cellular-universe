# Statická kontrola a očakávania

EA-033 nie je reprodukčný kapsul. Povinná je iba integrita a statický audit.

```powershell
External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 `
  -PackagePath External_Audits\PACKAGES\EA-20260719-033-KMPC137-C3-BI-EXACT-RUNTIME-BLOCKER
```

Očakávanie: exit `0`, všetky manifest/source/copy/runtime-map kontroly PASS.

## Povinné read-only kontroly

- v raw `017` overiť `runtime_limit_seconds=45.0` a
  `runtime_seconds=34.86000000000058`;
- v raw `016` overiť štyri úspešné coefficient payloady, oba exact
  `STAGE_WALL_TIMEOUT`, odstránený temporary handoff a nulový score effect;
- v source `019`, `023`, `024`, `025` a `027` overiť 80 dps, shape
  `104×104`, jeden exact solve a aktuálne runtime capy;
- potvrdiť, že raw `013` až `016` sú technické receipts bez pair verdiktu.

## Očakávaný auditný záver

Najmenšiu matematickú zmenu predstavuje osobitná exact-runtime výnimka,
pretože zachováva solver úspešne použitý v KMPC-112. Nie je však automaticky
schválená: auditor má posúdiť, či má byť výnimka lokálna iba pre dve BI/.15
exact varianty a aké runtime/negative guards sú povinné.

Ak auditor uprednostní nový rýchly solver alebo checkpointovanie, musí uviesť
minimálny dôkaz parity, nezávislý residual/holdout a package tier potrebný
pred zmenou autoritatívneho stavu.

## Zakázaná reprodukcia ako dôkaz tieru

Balík nemá transitive runtime closure. Official Python beh ani vzniknutý
generated JSON preto nie sú T2 dôkazom EA-033. Taký beh sa označí iba
`DECLARED_DEVIATION`.

