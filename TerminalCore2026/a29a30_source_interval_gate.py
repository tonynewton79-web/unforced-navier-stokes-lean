"""Exact rational interval acceptance for A.29--A.30 residual certificates.
The caller MUST supply validated enclosures for actual source functions.
No source realization is bundled. Output is conditional on input integrity.
"""
import json,argparse
from fractions import Fraction as F
class I:
 def __init__(self,lo,hi=None):
  self.l=F(lo);self.u=F(hi) if hi is not None else self.l
  assert self.l<=self.u
 def __add__(self,v):
  v=ii(v);return I(self.l+v.l,self.u+v.u)
 __radd__=__add__
 def __neg__(self):return I(-self.u,-self.l)
 def __sub__(self,v):return self+-ii(v)
 def __rsub__(self,v):return ii(v)+-self
 def __mul__(self,v):
  v=ii(v);z=[x*y for x in (self.l,self.u) for y in (v.l,v.u)]
  return I(min(z),max(z))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=ii(v)
  if v.l<=0<=v.u:raise ZeroDivisionError('zero in interval denominator')
  return self*I(1/v.u,1/v.l)
 def __rtruediv__(self,v):return ii(v)/self
 def sq(self):
  return I(0,max(self.l**2,self.u**2)) if self.l<=0<=self.u else I(min(self.l**2,self.u**2),max(self.l**2,self.u**2))
 def absmax(self):return max(abs(self.l),abs(self.u))
def ii(v):
 if isinstance(v,I):return v
 if isinstance(v,(int,str,F)):return I(v)
 if isinstance(v,list) and len(v)==2:return I(v[0],v[1])
 raise ValueError('unrecognized rational interval')
KEYS='eta X E H U M Meta I Ieta J Jeta S Seta Pi Pieta R Rp'.split()
def audit(box):
 lam=ii(box['lambda']);h=ii(box['h'])
 assert 0<lam.l and lam.u<=F(1,10**14)
 assert 0<h.l and h.u<=lam.l/F(10000)
 d={k:ii(box[k]) for k in KEYS}
 eta,X,E,H,U,M,Meta,V,Veta,J,Jeta,S,Seta,Pi,Pieta,R,Rp=[d[k] for k in KEYS]
 assert X.l>0 and E.l>0 and H.l>0 and eta.absmax()<=1
 D=ii(F(1,2))-h;A=ii(F(1,2))+h;beta=ii(F(1,2))-lam
 one=ii(1);d=one-eta.sq();g=(-2*eta)/(one+eta.sq())
 c=-D*eta*g;q0=(lam-h+c)/(one-lam)
 assert q0.l>0
 m=M/(X*E);meta=(Meta-g*M)/(X*E)
 W=one-(2*D*eta*M+d*Meta)/X
 Q=-W+((one-h)*V-D*eta*Veta-d*Jeta+2*(h-D)*eta*J)/(X*H)
 N=-W*U+(D*(M-eta*Meta)+4*h*eta*S-d*Seta)/X+4*A*eta*Pi-d*Pieta
 em=m-R/beta+lam*Rp/(beta.sq())
 eQ=Q-q0;eN=N/E+R-(D+c)*m+D*eta*meta
 Cd=lam*(D+c)*(one-lam)/(beta.sq()*(lam-h+c))
 w0=2*R-Cd*Rp
 if Q.l<=0:return {'status':'FAIL_Qs_not_positive'}
 gates={'eQ':(eQ/q0).absmax()<=F(1,10**10),
        'em':(em/q0).absmax()<=F(1,10**7),
        'eta_meta':(eta*meta/q0).absmax()<=F(2,10**7),
        'eN':(eN/q0).absmax()<=F(1,10**7)}
 w=N/(E*Q)
 gates['direct_ratio']=(w-w0).absmax()<F(1,10**6)
 return {'conditional_pass':all(gates.values()),'gates':gates,
         'max_abs_ratio_fraction':str((w-w0).absmax())}
if __name__=='__main__':
 ap=argparse.ArgumentParser()
 ap.add_argument('source_intervals_json')
 x=ap.parse_args()
 with open(x.source_intervals_json) as f:obj=json.load(f)
 if not obj.get('source_evidence'):
  raise ValueError('external source integral/correction interval evidence required')
 result=[audit(c) for c in obj['cells']]
 print(json.dumps({'status':'CONDITIONAL_ON_EXTERNAL_SOURCE_INTERVAL_PROOFS',
                   'all_pulse_cells_pass':all(x.get('conditional_pass',False) for x in result),
                   'results':result},indent=2))
