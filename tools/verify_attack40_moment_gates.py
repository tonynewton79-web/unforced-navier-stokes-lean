#!/usr/bin/env python3
"""Attack40 finite exact-rational checks of the stated elementary bounds.
These samples are NOT a proof of full G1 or a numerical Cpre estimate.
"""
from fractions import Fraction as F

def e_bounds(x, n=32):
    x=F(x)
    if x<0:
        a,b=e_bounds(-x,n)
        return 1/b,1/a
    S=F(1); T=F(1)
    for k in range(1,n+1):
        T=T*x/k; S+=T
    rem=T*x/(n+1)/(1-x/(n+2))
    return S,S+rem

for x,lower,upper in [
    (F(2),F(7),F(8)),(F(15,8),F(6),F(7)),
    (F(3,4),F(2),F(3)),(F(1,8),F(1),F(8,7)),
    (F(27,160),F(1),F(6,5))]:
    a,b=e_bounds(x)
    assert lower<a<=b<upper,(x,a,b)

# Matrix inverse and nonlinear coefficient margins.
assert F(57,41)<F(3,2)
assert F(14,41)<F(3,2)
assert F(15,14)<F(9,8)
assert F(576,7)<83
assert 8*F(3,2)**2*83*F(1,1500)<1
assert F(360,1500)<F(1,4)
assert 192000*F(1,10**6)/(1-360*F(1,1500))<F(1,2)

# Universal source bump sigma' and sigma'' analytic maxima.
assert 133/F(2**14)<1
assert F(19245,2**14)<2
assert F(5592,F(9,100))<64000

# Source's A.10 and A.12 slope constants.
assert F(36)*F(7,10)/256<F(1,10)
assert F(18,100)/(1-F(1,10000))<F(1,4)
print("PASS_ATTACK40 exact rational inequalities: source two-bump inverse, nonlinear angular correction, slope selectors")
print("Cpre, actual normalized moment discrepancies, and complete G1 remain UNVERIFIED")
