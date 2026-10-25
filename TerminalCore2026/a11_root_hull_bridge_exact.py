"""Exact A.19 derivative / A.11 entire-hull stress certificate.
Only algebra and rational implications; source authenticity is NOT tested.
"""
from fractions import Fraction as Q
import sympy as S
v,veta,AD,AP,ADeta,APeta=S.symbols('v veta AD AP ADeta APeta', nonzero=True)
D=AD/(2*v**2);P=AP/(2*v**2);g=veta/v
c=2*g*(D-P)+(ADeta-APeta)/(2*v**2)-(AD-AP)*veta/v**3
assert S.simplify(c-(ADeta-APeta)/(2*v**2))==0
A,K,J1,J2,a1,a2,b1,b2,B=S.symbols("A K J1 J2 a1 a2 b1 b2 B")
F=K*A*A+B+J1*(a1+b1*A)**2+J2*(a2+b2*A)**2
assert S.simplify(S.diff(F,A,2)-2*(K+J1*b1*b1+J2*b2*b2))==0
width=Q(3,10);s1=-3-width/2;s2=-1+width/2
assert s1==-Q(63,20) and s2==-Q(17,20)
assert s2-s1==Q(23,10) and 2*width==Q(3,5)
lam=Q(1,20);h=lam/100
delta=11520*lam**28;jet=1280*lam**28
kappa=(1+delta)/(1-delta)
assert delta<Q(1,10**20)
assert kappa*kappa*(Q(93,40)+h**7/3)<Q(233,100)
assert kappa*kappa/2<Q(5000001,10000000)
assert Q(3,5)*jet*(1+delta)/(1-delta)**2<Q(1,100000)
bound=4*h*Q(233,100)+4*(Q(1,2)+h)*Q(5000001,10000000)+Q(1,100000)
assert bound<Q(503,500) and Q(503,2000)<Q(1,2)
assert Q(1,100000)*100000==1 # value-only does not control derivatives
print("PASS future-kernel parameter cancellation, complete hull+gap source-conditional stress margin")
print("SOURCE STATUS: exact C1 root, two endpoint tails, gauges, jets and complete unforced PDE are unverified")
