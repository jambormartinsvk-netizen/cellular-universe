# Erratum A2.2 — menovateľ K4 rovnice pre `u_f`

**Dátum:** 2026-07-13  
**Týka sa:** `Audit/A2_2_odvodenie_a_test_A2_K3_A2_K4.md`, sekcia 5.2

## Nejednoznačný typografický zápis

V auditnom dokumente je člen zapísaný ako

```text
(lambda/E delta)[(2-beta)u_f-(1-beta)u_c].
```

Tento zápis je typograficky nejednoznačný. Správny a použitý vzťah je

```text
lambda/(E delta)[(2-beta)u_f-(1-beta)u_c].
```

Teda `delta=1+w_f` patrí do menovateľa. Skripty 28–30 od začiatku používajú správny kód

```python
(lam_over_e / d) * ((2.0-zeta)*u_f-(1.0-zeta)*u_c)
```

Numerické výsledky, konvergencia ani verdikt sa nemenia. Pôvodná formulácia zostáva zachovaná a toto erratum musí byť čítané spolu s ňou.

