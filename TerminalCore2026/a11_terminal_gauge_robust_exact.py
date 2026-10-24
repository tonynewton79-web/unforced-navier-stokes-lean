"""Exact-rational scalar gates for A11 terminal gauge residual robustness.

The true Appendix-A moment/pressure residual intervals remain unavailable.
No source-authenticated full stress or unforced PDE theorem is asserted.
"""
from fractions import Fraction as F
from math import factorial
x=F(6,5)
t=sum((x**k/F(factorial(k)) for k in range(6)),F())
t+=(x**6/F(720))/(1-x/F(7))
assert t==F(1504439,453125)<4
assert (F(1,2)+F(1,100))*F(23,10)==F(1173,1000)
b=F(11,10000)
g=F(1,100)
assert b+g==F(111,10000)<F(1,2)
assert F(1,2)-b-g==F(4889,10000)
cone=F(9,8)-F(151,5000)*F(111,9700)**2
assert cone==F(529254389529,470450000000)>F(1124,1000)
for lam in (F(1,100),F(1,1000),F(1,100000000)):
 for q in (F(0),F(1,5),F(99,100)):
  Estar=lam/F(1000); a=F(1,1000); h=lam/100; A=F(1,2)+h
  Cpi=q*(1-a)*Estar*lam/(400*4*A)
  assert 4*A*Cpi<=(1-a)*Estar*lam/400
  Emin=(1-a)*Estar/4
  assert 4*A*Cpi/Emin <=lam/100
for K in (1,10,100):
 # C_S(eta)=K eta is an adversarial missing-gauge witness at eta=0.
 assert -F(K,100)==(-K)/F(100)
print("EXACT_RATIONAL_SCALAR_PASS")
print("NEW stress ratio: 111/10000 lambda; slack: 4889/10000 lambda")
print("NEW strict cone ratio lower:",cone)
print("SOURCE_A11_PROFILE_AND_TERMINAL_INTEGRALS: NOT_CERTIFIED")
print("LEAN_WHOLE_UNFORCED_THEOREM: NOT_PROVED")
