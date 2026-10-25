"""Exact-rational required input tests for the source A.11 correction supports.
No real source parameters are loaded by default. This is a negative-control
fixture and MUST NOT be called a source-certified interval result.
"""
import json,sys
from fractions import Fraction as Q
def audit(d):
 q=lambda k:Q(str(d[k]))
 lam,h=q('lambda'),q('h')
 g,ge=q('coefficient_sup'),q('coefficient_eta_derivative_sup')
 Eb,X=q('unedited_E_support_sup'),q('X_support_inf')
 flags=('endpoint_gauges_source_verified','post_support_slopes_source_verified',
 'U_M_J_zero_on_supports_source_verified',
 'interpolation_exit_Qs_source_verified',
 'unedited_plateau_source_verified','nonlinear_A11_roots_source_verified')
 tests={
 'parameters':0<lam<=Q(1,20) and 0<h<=min(Q(1,100),lam/8),
 'A11_coefficients':g<=min(Q(3,1280),Q(9,8000000)*lam),
 'A11_eta_derivatives':ge<=3*lam/10240,
 'baseline_E':Eb<=lam/30,
 'radial_X':X>=35/lam}
 tests.update({k:bool(d.get(k,False)) for k in flags})
 return {'SOURCE_CERTIFIED':all(tests.values()),'checks':tests,
   'scope':'Only A.11 support cone, never full exterior or unforced PDE'}
if __name__=='__main__':
 d=json.load(open(sys.argv[1])) if len(sys.argv)>1 else dict(
 lambda_='1/100')
 if len(sys.argv)==1:
  d={'lambda':'1/100','h':'1/10000','coefficient_sup':'1/1000000000',
  'coefficient_eta_derivative_sup':'1/100000000','unedited_E_support_sup':'1/10000',
  'X_support_inf':'4000'}
 print(json.dumps(audit(d),indent=2))
