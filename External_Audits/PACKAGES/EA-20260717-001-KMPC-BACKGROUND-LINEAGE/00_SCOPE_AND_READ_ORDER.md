# Scope — K_MPC, Fourierov mód a univerzálny background

- Package ID: `EA-20260717-001-KMPC-BACKGROUND-LINEAGE`
- Route: `A1-K1 / A2-K4 / P5`
- Audit mode: forenzný formula-lineage audit
- Autorita: externý auditor dáva odporúčanie; projektový verdikt nemení

## Presná otázka

Bol perturbatívny Fourierov mód `k`, historicky fixovaný ako
`K_MPC=0.05`, neprípustne prenesený do homogénneho K4 backgroundu? Ak áno,
je navrhnuté mapovanie integračnej amplitúdy na `A_f a^p` matematicky nutné
a bez nového skrytého fitu?

## Poradie čítania

1. `001` až `004`: auditné pravidlo, aktuálny stav a definícia otázky.
2. `005` až `012`: odvodenie palivového člena, koeficientov, species a
   projected transformácie.
3. `013` až `015`: neskorší STOP historického K7, P5 nástupca a formula
   provenance checklist.

## Zmrazené kritériá

- Homogénny `H(a)` nesmie závisieť od voľby perturbatívneho Fourierovho módu.
- Ak `z=ka/(H_0 sqrt(Omega_r0))`, musí byť presne uvedené, či `k` je mód,
  pivot alebo fyzikálna konštanta a v ktorej rovnici.
- Normalizácia `A_f` nesmie byť potichu nový post-data parameter.
- Neskorší backgroundový STOP nevyhlasuje smrť A2-K4; vylučuje iba
  historickú fixed-K backgroundovú implementáciu v uvedenom scope.

## Nonclaims

Tento balík neimplementuje CLASS, neodvodzuje hodnotu `A_f`, neuzatvára
perturbácie A2 a neporovnáva model s dátovou likelihood.

## Požadovaný výstup

Auditor má vytvoriť formula ledger
`zdroj -> zmena premennej -> base/runner použitý v histórii -> background`
a uviesť, či ide o `PRECHECK_EXCLUDED_SCOPE`, `COMPUTED_STOP_SCOPE`,
`REFERENCE_MISMATCH_ONLY` alebo iba otvorený review.
