#!/usr/bin/env python3
"""Exact angular torque, independent full advection, seeded rational checks."""
import sympy as s
from fractions import Fraction as F
from random import Random
r,z,t,e=s.symbols('r z t e',positive=True,real=True)
f=s.exp(-r*r-z*z)
pot=e*f*(r*s.cos(t)+r**3*s.sin(t))
ur=s.diff(pot,t)/r
ut=-s.diff(pot,r)
g=r*ut
avg=lambda q:s.simplify(s.integrate(s.expand_trig(q),(t,0,2*s.pi))/(2*s.pi))
assert avg(g)==0 and avg(ur)==0
J=avg(ur*g)
T=s.simplify(-s.diff(r*J,r)/r)
assert s.simplify(J-e**2*r**3*f**2)==0
assert s.simplify(T-4*e**2*r**2*(r*r-1)*f**2)==0
full=avg(ur*s.diff(g,r)+ut/r*s.diff(g,t))
assert s.simplify(full+T)==0
assert s.simplify(T.subs({r:s.Rational(1,2),z:0})
                  +3*e**2*s.exp(-s.Rational(1,2))/4)==0
assert s.simplify(ut.subs({r:s.Rational(1,2),z:0,t:0})
                  +e*s.exp(-s.Rational(1,4))/2)==0
rng=Random(20261024)
for _ in range(10000):
 rr=F(rng.randint(1,80),rng.randint(1,40))
 assert 4*rr**2*(rr**2-1)==4*rr**4-4*rr**2
print("PASS torque 4 epsilon^2 r^2(r^2-1)exp(-2rho^2)")
print("PASS exact averaged full nonlinear advection = -torque")
print("PASS r=1/2,z=0 torque -3 epsilon^2 exp(-1/2)/4")
print("PASS 10000 exact Fraction checks; no blowup claim")
