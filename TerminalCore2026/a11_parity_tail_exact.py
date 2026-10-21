"""A.11 stress-tail source identities and strict rational arithmetic.

Finite exact replay only. Source gauge, source profile, and sound interval
cover remain independent unproven inputs for the proposed unforced theorem.
"""
import sympy as s
from fractions import Fraction as F
E,D,P,g,h,A,eta,Deta,Peta=s.symbols('E D P g h A eta Deta Peta')
S=E**2*D;Pi=-E**2*P
Ns=(4*h*eta*S-(1-eta**2)*E**2*(2*g*D+Deta)) +4*A*eta*Pi-(1-eta**2)*(-E**2*(2*g*P+Peta))
assert s.simplify(Ns-E**2*(4*eta*(h*D-A*P)-(1-eta**2)*(2*g*(D-P)+Deta-Peta)))==0
lam=F(1,20)
delta=11520*lam**28
epsilon=1280*lam**28
assert delta<F(1,10**30)
K=((1+delta)/(1-delta))**2
T=F(3,5)*epsilon*(1+delta)/(1-delta)**2
assert T<769*lam**28
B=4*(lam/100)*K*F(233,100)+4*(F(1,2)+lam/100)*(K/2)+T
assert B/F(4)<F(503,2000)
assert F(1,2)-B/F(4)>F(497,2000)
print('PASS: exact (4.16) stress algebra and improved local future-support rational bound')
print('PASS: conditional |Ns|/E < 503 lambda/2000 and strict slack >497 lambda/2000')
print('NOT SOURCE CERTIFIED; actual integral and interval hypotheses have not been verified')
