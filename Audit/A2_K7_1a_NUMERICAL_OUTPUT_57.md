# A2-K7.1a-K3 — symbolický výstup skriptu 57

**Dátum:** 2026-07-13  
**Generátor:**
`scripts/57_script_A2_K7_1a_K3_expansion_scalar_covariance_gate.py`

```text
operator = Q1=[(1-epsilon)Gamma
               +epsilon(1-delta)Theta_phi]rho_F
reference frame = donor fuel four-velocity u_phi

delta Q1 = epsilon(1-delta)rho_F delta Theta_phi
           +[(1-epsilon)Gamma
             +epsilon(1-delta)Theta_phi]delta rho_F

a delta Theta_phi = theta_phi-3 Phi'-3 Hconf Psi

R1 = Gamma/epsilon-Gamma+(1-delta)Theta_phi
limit epsilon*R1 = Gamma
```

```text
exact_FRW_Q1                         true
first_order_delta_Q1_product_rule    true
delta_Q1_scalar_gauge_transform      true
total_vector_ledger_cancels          true
epsilon_zero_rate_is_singular        true

mean_covariant_closure               PASS
microphysical_CTP_kernel             NOT_DERIVED
noise_correlator                     NOT_DERIVED
regular_epsilon_zero_limit           FAIL
verdict                              SURVIVES_FORMULATION_ONLY_NO_SCORE_INCREASE
```

Výstup nie je numerickým dôkazom stability. Je to symbolická kontrola
kovariancie a uzavretia ledgeru.

