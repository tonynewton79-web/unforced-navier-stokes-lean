#!/usr/bin/env python3
"""Exact conservation/flux/reynolds benchmark; not an unforced blowup proof."""
from fractions import Fraction as F
from random import Random
import sympy as s
r,z,t,nu,e,R,X,tau=s.symbols("r z t nu e R X tau",positive=True,real=True)
g=s.Function('g')(r,z,t);a=s.Function('a')(r,z,t);bb=s.Function('b')(r,z,t)
eq=s.diff(g,t)+s.diff(r*a,r)/r+s.diff(bb,z)-nu*(s.diff(g,r,2)-s.diff(g,r)/r+s.diff(g,z,2))
fr=r*a-nu*(r*s.diff(g,r)-2*g)
fz=r*bb-nu*r*s.diff(g,z)
assert s.simplify(s.diff(r*g,t)+s.diff(fr,r)+s.diff(fz,z)-r*eq)==0
j=e**2*r**3*s.exp(-2*(r*r+z*z))
adv=s.simplify(2*s.pi*R*s.integrate(s.exp(-z*z)*j.subs(r,R),(z,-s.oo,s.oo)))
assert s.simplify(adv-2*s.pi*e**2*R**4*s.exp(-2*R**2)*s.sqrt(s.pi/3))==0
assert s.simplify(adv.subs(R,s.Rational(1,2))-
s.pi**s.Rational(3,2)*e**2*s.exp(-s.Rational(1,2))/(8*s.sqrt(3)))==0
Rt=s.sqrt(2*X*tau)
assert s.simplify(Rt*(-s.diff(Rt,tau)))==-X
rng=Random(20261025)
for _ in range(30000):
    aa=F(rng.randint(-120,120),rng.randint(1,51))
    cc=F(rng.randint(-120,120),rng.randint(1,51))
    dd=F(rng.randint(-120,120),rng.randint(1,51))
    assert 2*abs(aa*cc)<=aa*aa+cc*cc+dd*dd
print("PASS moving-cylinder conservation and exact source-independent Gaussian control")
print("PASS 30000 exact Fraction nonlinear flux inequalities; NO blowup claimed")
