# Verification log — nezávislá rekonštrukcia externého auditu 2

**Dátum:** 2026-08-14  **Prostredie:** `Python 3.11.15`, numpy 2.4.4, scipy 1.17.1

Raw výstupy nižšie sú nemenené. Skripty sú v tom istom adresári.

## `verify_background.py`

```text
k_mean = 15.53545746435112  delta = 0.022969782752802058  w_f = -0.977030217247198
ash from transfer = 0.027078783712161908
omega_m(rec)      = 2.4113627265547715e+17  Planck 0.1431 +- 0.0012 -> sigma = 2.009468938795643e+20
forced Om0        = 5.474177915790595e+17

 lam    Om0      S8(rel)   
 0.00  0.3246   ash=0.00000
 0.05  0.3337   ash=0.00910
 0.10  0.3427   ash=0.01813
 0.15  0.3517   ash=0.02708
 0.20  0.3606   ash=0.03595
```

## `verify_spectra_and_windows.py`

```text
CORRECTED omega_m(rec) = 0.14299  (audit says 0.14299)
  sigma vs Planck 0.1431+-0.0012: -0.09

n_s(C=28) = 0.965545
  best: n_s=0.9649 -> C=27.20
  1s-: n_s=0.9607 -> C=22.63
  1s+: n_s=0.9691 -> C=33.01
  2s-: n_s=0.9565 -> C=18.95
  2s+: n_s=0.9733 -> C=40.64
  3s-: n_s=0.9523 -> C=15.91
  3s+: n_s=0.9775 -> C=51.13
  C=28: n_s=0.9655, sigma=0.15
  C=56: n_s=0.9790, sigma=3.36
  C=118: n_s=0.9888, sigma=5.68

   30.00 GHz : steam/CMB = 17.81 %
   53.21 GHz : steam/CMB = 9.82 %
  100.00 GHz : steam/CMB = 2.41 %
  217.00 GHz : steam/CMB = 0.04 %
  rho_steam/rho_CMB = 1.216 %   (2 dof vs 2 dof)
  Wien freq peak of 0.905K: 53.21 GHz

  S8*H0 = [58.266, 58.155, 58.044] spread = 0.381 %
```

## `verify_network_moments.py`

```text
M=  60000 seed=1  <D2>=1.7982 <D4>=4.4756  xi=0.124446  Omega_cell=c/(2.158 l0)
M= 200000 seed=1  <D2>=1.8088 <D4>=4.5128  xi=0.124745  Omega_cell=c/(2.164 l0)
M= 200000 seed=7  <D2>=1.8075 <D4>=4.5165  xi=0.124937  Omega_cell=c/(2.163 l0)
```

## `verify_loop_nullchecks.py`

```text
  LI, cutoff=inf, m= 0.01:  integral =  8.527e-14  (quad err 5.4e-09)   -> B-A =  2.160e-15
  LI, cutoff=inf, m= 0.20:  integral =  1.180e-16  (quad err 5.1e-10)   -> B-A =  2.988e-18
  LI, cutoff=inf, m= 1.00:  integral = -7.199e-17  (quad err 1.2e-08)   -> B-A = -1.824e-18
  LI, cutoff=inf, m= 5.00:  integral =  2.711e-20  (quad err 2.2e-13)   -> B-A =  6.866e-22

  k_max = 3.8978
  LI + cutoff, m=0.20: B-A = -6.901448e-05   analytic -1/(96 pi^2 kmax^2) = -6.946964e-05
  LI + cutoff, m=1.00: B-A = -5.923578e-05   analytic -1/(96 pi^2 kmax^2) = -6.946964e-05
  -> audit quotes -6.9468e-5 ; 16pi^2*(B-A) = -0.01097
```

## `verify_escape_scales.py`

```text
  electron  ln(L/m)= 51.5  dc2/c2 = 3.532e-02
  proton    ln(L/m)= 44.0  dc2/c2 = 3.045e-02
  Higgs     ln(L/m)= 39.1  dc2/c2 = 2.727e-02

  --- how much suppression is needed ---
  limit 1e-16: suppression 2.83e-15 -> (M/Lambda) = 5.32e-08  i.e. EFT cutoff M = 6.49e+11 GeV  (Lambda=M_Pl)
  limit 1e-19: suppression 2.83e-18 -> (M/Lambda) = 1.68e-09  i.e. EFT cutoff M = 2.05e+10 GeV  (Lambda=M_Pl)
  limit 1e-23: suppression 2.83e-22 -> (M/Lambda) = 1.68e-11  i.e. EFT cutoff M = 2.05e+08 GeV  (Lambda=M_Pl)

  --- anomalous dimension route (audit III.6c) ---
  limit 1e-16: Delta = 0.650
  limit 1e-19: Delta = 0.785
  limit 1e-23: Delta = 0.963
```

