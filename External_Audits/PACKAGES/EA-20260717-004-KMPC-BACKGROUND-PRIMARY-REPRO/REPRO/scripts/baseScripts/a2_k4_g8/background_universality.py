"""Exact k-universality audit for the frozen K7 background formula."""
from __future__ import annotations
import time
import sympy as sp

def audit(max_runtime_seconds: float) -> dict[str, object]:
    if not 0 < max_runtime_seconds <= 10: raise ValueError('max_runtime_seconds must be in (0,10]')
    start=time.monotonic()
    k,a,H0,Or,Om,p=sp.symbols('k a H0 Or Om p', positive=True, nonzero=True)
    z=k*a/(H0*sp.sqrt(Or)); mu=H0*Om/(sp.sqrt(Or)*k); g2=sp.Rational(3,20)*(H0/k)**2*sp.sqrt(Or); C=1/(p+1)-sp.Rational(1,2)
    fuel=sp.simplify(z**p*(1+g2*C*z**2)); denominator=sp.simplify(1+mu*z+fuel)
    if time.monotonic()-start>max_runtime_seconds: raise TimeoutError('background universality algebra deadline exceeded')
    residual_matter=sp.simplify(mu*z-Om*a/Or)
    residual_g2=sp.simplify(g2*z**2-sp.Rational(3,20)*a**2/sp.sqrt(Or))
    residual_homogeneous=sp.simplify(k*sp.diff(fuel,k)-p*fuel)
    derivative=sp.factor(sp.diff(fuel,k))
    factor=sp.simplify(fuel/k**p)
    p_value=sp.Rational(393109,100000)
    derivative_at_p=sp.simplify(derivative.subs(p,p_value))
    checks={'mu_z_k_independent':residual_matter==0,'g2_z2_k_independent':residual_g2==0,'fuel_homogeneous_degree_p':residual_homogeneous==0,'fuel_derivative_nonzero_for_p_3_93109':derivative_at_p!=0}
    return {'test':'A2-K4 K7 frozen background exact Fourier-k universality audit','physics_executed':False,'score_effect':0,
      'definitions':{'p':'3.93109','fuel_factor':'z^p*(1+g2*(1/(p+1)-1/2)*z^2)'},
      'residuals':{'mu_z_minus_Om_a_over_Or':str(residual_matter),'g2_z2_minus_3a2_over_20sqrtOr':str(residual_g2),'k_dfuel_dk_minus_pfuel':str(residual_homogeneous),'dfuel_dk_at_p_3_93109':str(derivative_at_p)},
      'fuel_over_k_to_p':str(factor),'denominator':str(denominator),'checks':checks,
      'verdict':'STOP_BACKGROUND_K_DEPENDENCE_UNRESOLVED' if all(checks.values()) else 'REVIEW_ALGEBRA_UNCLOSED',
      'runtime_limit_seconds':max_runtime_seconds,'runtime_seconds':time.monotonic()-start}
