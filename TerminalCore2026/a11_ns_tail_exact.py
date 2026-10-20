"""Exact rational gates for Appendix-A A.11 exterior-tail cone estimate.

The source-stage holomorphic/ODE assumptions are NOT generated here.
Finite arithmetic checks and synthetic interval examples do NOT by
themselves certify a particular fully admissible source realization.
"""
from fractions import Fraction as Q
import argparse,json
def F(v):return Q(str(v))
Tf=512
c=Q(1,10**6)
hD_upper=(c/2+15+Q(1,20)*(3+Q(1,3)))/25
eta_error=10240*Q(1,20)**27*(c/2+15+Q(7,40))
assert hD_upper<Q(61,100)
assert eta_error<Q(1,100)
assert hD_upper+Q(1001,1000)+eta_error<2
for d in (20,50,100,1000,10**6):
  lam=Q(1,d);a=2+3*lam;p=Q(9,2)
  assert p>=2*a
  assert 2*(1-a/p)**2-(a-2)>=Q(7,20)
print('PASS source A11 universal rational tail, amplitude and cone budgets')
def certify(z):
 lam,h=F(z['lambda']),F(z['h'])
 E,D,P,eps,Qlo,Xlo=[F(z[k]) for k in (
  'E_upper','tail_D_upper','tail_P_upper',
  'deta_logE_upper','Qs_lower','X_lower')]
 assert 0<h<=lam/100 and lam<=Q(1,20)
 assert min(E,D,P,eps,Qlo,Xlo)>=0
 ne=E*(4*h*D+4*(Q(1,2)+h)*P+2*eps*(D+P))
 ok=(ne<=lam/2 and Qlo>=lam/2 and Xlo>=9/lam)
 return {'status':'CONDITIONAL_PASS' if ok else 'UNRESOLVED',
   'Ns_over_E_bound':str(ne),'target':str(lam/2),
   'warning':'supplied source intervals are NOT verified by this checker'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--demo',action='store_true')
 ap.add_argument('source_json',nargs='?');args=ap.parse_args()
 if args.demo:
  z={'lambda':'1/20','h':'1/10000','E_upper':'1/1000',
     'tail_D_upper':'400','tail_P_upper':'1/2',
     'deta_logE_upper':'1/10000000000','Qs_lower':'1/40','X_lower':'180'}
  assert certify(z)['status']=='CONDITIONAL_PASS'
  z['E_upper']='100'
  assert certify(z)['status']=='UNRESOLVED'
  print('PASS synthetic-positive and synthetic-negative checks, NOT source data')
 elif args.source_json:
  with open(args.source_json) as f:z=json.load(f)
  print(json.dumps(certify(z),indent=2))
