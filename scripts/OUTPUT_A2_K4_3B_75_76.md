# Výstup skriptov 75 a 76 — exact CAMB hierarchy koeficienty

**Dátum:** 2026-07-14

## Skript 75 — zachovaný chybný auditný mapping

- vnútorný limit: `20 s`;
- vonkajší limit: `30 s`;
- exit code: `1`;
- hlásené trvanie: `0.969 s`;
- výsledok: `COEFFICIENT_MISMATCH_REVIEW`.

Z 22 kontrol prešlo 20. Dve rezíduá boli

```text
J_l3 = 3*k*(-J_2(t) + pi_g(t))/7
G_l3 = 3*k*(-G_2(t) + pi_r(t))/7
```

Audit zdrojového kódu ukázal, že ide o nezamenené CAMB aliasy
`J_2->pi_g`, `G_2->pi_r` v očakávanej strane skriptu 75. Nejde o fyzikálny
koeficientový nesúlad. Podrobnosti sú v
`scripts/ERRATUM_75_A2_K4_3b_CAMB_L3_ALIAS_MAPPING.md`.

## Skript 76 — aliasovo opravený následník

**Príkaz:** `python scripts\\76_script_A2_K4_3b_exact_CAMB_hierarchy_coefficients_alias_fixed.py --max-runtime-seconds 20`  
**Vonkajší limit:** 30 s  
**Exit code:** 0  
**Hlásené trvanie:** 1.0 s  
**Verdikt:** `PASS_EXACT_CAMB_HIERARCHY_COEFFICIENTS_ALIAS_FIXED`

```json
{
  "CAMB_version": "1.6.6",
  "ell_range": [2, 8],
  "exact_checks": 22,
  "correction": "map J_2->pi_g and G_2->pi_r in expected l=3 backward coupling",
  "all_symbolic_residuals": "0",
  "verdict": "PASS_EXACT_CAMB_HIERARCHY_COEFFICIENTS_ALIAS_FIXED"
}
```

Všetkých sedem `J_l`, sedem `G_l`, sedem `E_l` porovnaní a polarizačný
zdroj mali po oprave presné symbolické rezíduum nula.

## Fyzikálny dosah

Skript 76 spevňuje B1 hierarchy ledger. Nerieši sedem konečno-štartových
radov, presný K4 background ani evolúciu transferov. Celá K4.3b preto ostáva
neuzavretá a K4 ostáva živá na 60/100.

