#!/usr/bin/env python3
"""Attack47 source-locked exact Fraction five-moment C3 uncertainty evaluator.
No diagnostic source values may be used to imply the original theorem.
"""
from fractions import Fraction as F
import json,sys
from pathlib import Path
fields=['Lambda','C','phi_axis_norm_C3','U_axis_norm_C3','Z_axis_norm_C3',
'chi_eta_deriv_bound_1','chi_eta_deriv_bound_2','chi_eta_deriv_bound_3',
'Phi_nonlin_remainder_norm_C3','u_nonlin_remainder_norm_C3']
def evaluate(obj):
    absent=[k for k in fields+['original_source_admissibility_certificate'] if obj.get(k) is None]
    if absent:raise ValueError('REFUSED_UNCERTIFIED_ORIGINAL_SOURCE_INPUT: '+', '.join(absent))
    if obj['original_source_admissibility_certificate']!='independently_validated':
        raise ValueError('REFUSED: source parameters are not independently certified')
    if any(not isinstance(obj[k],(str,int)) or isinstance(obj[k],bool) for k in fields):
        raise ValueError('Exact rational strings only: floats forbidden')
    d={k:F(obj[k]) for k in fields}
    L,C=d['Lambda'],d['C']
    if not L>0 or not C>0:raise ValueError('Lambda,C must be positive')
    if any(v<0 for v in d.values()):raise ValueError('All upper bounds must be nonnegative')
    P,U,Z=(d[k] for k in ('phi_axis_norm_C3','U_axis_norm_C3','Z_axis_norm_C3'))
    a,b,c=(d[f'chi_eta_deriv_bound_{j}'] for j in (1,2,3))
    ep,eu=(d[k] for k in ('Phi_nonlin_remainder_norm_C3','u_nonlin_remainder_norm_C3'))
    if ep>=F(265,1000):raise ValueError('No certified comparison positivity')
    Q=1+a+(b+F(2,3)*a*a)/2+(c+2*a*b+a**3/3)/6
    pc,pa=P*Q,P*(Q+ep)
    uc,ua=U+4*Z/L,U+(4*Z+eu)/L
    dp,du=P*ep,eu/L
    return {key:str(val) for key,val in {
      'M':4*du/L,
      'I':16*dp/(C*L*L),
      'J':16*(du*pa+uc*dp)/(C*L*L),
      'S':4*du*(ua+uc)/L+8*dp*(pa+pc)/(C*C*L*L),
      'Cp':4*dp*(pa+pc)/(C*C*L)}.items()}
if __name__=='__main__':
  if len(sys.argv)!=2:raise SystemExit('Usage: script INPUT.json')
  try:print(json.dumps(evaluate(json.loads(Path(sys.argv[1]).read_text())),indent=2))
  except ValueError as e:print(e,file=sys.stderr);sys.exit(2)
