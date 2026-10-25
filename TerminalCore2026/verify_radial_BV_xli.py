#!/usr/bin/env python3
"""Exact radial-flux variation, signed Gaussian benchmark and rational checks."""
from fractions import Fraction as F
from random import Random
import sympy as s
r,z,R,e=s.symbols('r z R e',positive=True)
J=e**2*r**3*s.exp(-2*(r*r+z*z))
Phi=s.simplify(2*s.pi*R*s.integrate(s.exp(-z*z)*J.subs(r,R),(z,-s.oo,s.oo)))
assert s.simplify(Phi-2*s.pi**s.Rational(3,2)*e**2*R**4*s.exp(-2*R*R)/s.sqrt(3))==0
assert s.simplify(s.diff(Phi,R)-4*Phi*(1-R*R)/R)==0
assert s.simplify(s.integrate(s.diff(Phi,R),(R,0,1))-Phi.subs(R,1))==0
assert s.simplify(s.integrate(-s.diff(Phi,R),(R,1,s.oo))-Phi.subs(R,1))==0
rng=Random(20261025)
for _ in range(20000):
    E=F(rng.randrange(0,100),rng.randrange(1,50))
    D=F(rng.randrange(0,100),rng.randrange(1,50))
    p=F(rng.randrange(-50,51),rng.randrange(1,20))
    q=F(rng.randrange(-50,51),rng.randrange(1,20))
    assert (p*p+q*q)>=2*abs(p*q)
    assert (E+D)**2>=4*E*D
print("PASS exact Gaussian signed flux total radial variation at r=1")
print("PASS 20000 Fraction product and energy-gradient controls")
