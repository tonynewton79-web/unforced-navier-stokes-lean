#!/usr/bin/env python3
"""Independent exact energy-log-width, steepening and H2-flux algebra."""
from fractions import Fraction as F
from random import Random
import sympy as s
B,A=s.symbols("B A",positive=True)
L=4*B/A
assert s.simplify((A-A/4)/L-3*A*A/(16*B))==0
E,R,h,c,C=s.symbols("E R h c C",positive=True)
Fexpr=s.pi*R**2*C**2*E**s.Rational(1,4)*c**s.Rational(3,2)
assert s.simplify((Fexpr/(s.pi*R**2*C**2*E**s.Rational(1,4)))**s.Rational(2,3)-c)==0
assert s.simplify(s.Rational(4,3)*(1+h)-1)>0
rng=Random(20261025)
for _ in range(25000):
    ee=F(rng.randint(1,300),rng.randint(1,49))
    aa=F(rng.randint(1,300),rng.randint(1,57))
    width=ee/aa
    assert aa*width==ee
    ll=4*ee/aa
    assert F(3,4)*aa/ll==3*aa*aa/(16*ee)
print("PASS B/A logarithmic width and 3A^2/(16B) radial derivative")
print("PASS flux-to-H2 lower norm, nonintegrable squared-time exponent")
print("PASS 25000 independent Fraction concentration fixtures")
