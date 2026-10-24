"""Exact source-stage bounds and conditional Appendix-B angular inverse gates.

Does NOT numerically determine M0 or verify the unforced startup system.
"""
from fractions import Fraction as F
import sympy as s
x,Td,P=s.symbols('x Td P',positive=True,real=True)
early=5*P**2+P**2*s.integrate(s.exp(-x),(x,0,1+Td))
assert s.simplify(early-(6-s.exp(-1-Td))*P**2)==0
h,c,y=s.symbols('h c y',positive=True)
tail=s.integrate(c**2*s.exp(-(1+2*h)*y),(y,0,s.oo))
assert s.simplify(tail-c**2/(1+2*h))==0
print('PASS exact early-stage pressure-atom bound and infinite outer tail')
assert F(2704,9)<301 and 64*301==19264 and 40*19264==770560
for b in range(10000):
    assert F((b+1)**2,8**b)<=1
print('PASS all 10,000 exact chi Cauchy weight tests')
for m in (F(1),F(10000)):
 for j in (F(1,50),F(1,1000)):
    sigma=j/(72000*(1+m))
    assert sigma>0 and sigma<j/(72000*m)
for B in (F(1),F(200)):
 for a1,a2,l1,l2,r in ((F(3),F(4),F(1),F(2),F(1,2)),
                      (F(7),F(2),F(11),F(13),F(1,4))):
    Lam=2*max(40*B*a1/r,80*a2/r,40*B*l1,80*l2)
    assert 20*B*a1/Lam<=r/4 and 40*a2/Lam<=r/4
    assert 20*B*l1/Lam<=F(1,4) and 40*l2/Lam<=F(1,4)
print('PASS conditional nonlinear-contraction budget inequalities')
