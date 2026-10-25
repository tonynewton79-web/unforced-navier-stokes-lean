#!/usr/bin/env python3
import sympy as s
from fractions import Fraction as F
from random import Random
r,R=s.symbols('r R',positive=True)
f=s.exp(-r*r)
I=s.simplify(s.integrate(r*f**2,(r,R,s.oo)))
D=s.simplify(s.integrate(r*s.diff(f,r)**2,(r,R,s.oo)))
assert s.simplify(4*I*D-R**2*f.subs(r,R)**4)==s.exp(-4*R*R)/2
rng=Random(20261025)
for _ in range(25000):
 a=F(rng.randrange(1,100),rng.randrange(1,90))
 assert 4*F(1,4)*(a*a+F(1,2))-a*a==F(1,2)
print('PASS radial Gaussian trace and 25000 rational fixtures')
