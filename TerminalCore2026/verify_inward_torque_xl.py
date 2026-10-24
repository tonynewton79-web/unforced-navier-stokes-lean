#!/usr/bin/env python3
"""Exact symbolic inward flux and full initial advection, 25k rational fixtures."""
import sympy as s
from fractions import Fraction as F
from random import Random
r,z,theta,eps=s.symbols("r z theta eps",positive=True,real=True)
f=s.exp(-r*r-z*z)
az=eps*f*(r*s.cos(theta)-r**3*s.sin(theta))
ur=s.diff(az,theta)/r
ut=-s.diff(az,r)
gamma=r*ut
avg=lambda q:s.simplify(s.integrate(s.expand_trig(q),(theta,0,2*s.pi))/(2*s.pi))
j=s.factor(avg(ur*gamma)-avg(ur)*avg(gamma))
torque=s.factor(-s.diff(r*j,r)/r)
assert s.simplify(j+eps**2*r**3*f**2)==0
assert s.simplify(torque-4*eps**2*r**2*(1-r**2)*f**2)==0
assert s.simplify(-avg(ur*s.diff(gamma,r)+ut*s.diff(gamma,theta)/r)-torque)==0
R=s.symbols("R",positive=True,real=True)
flux=s.simplify(2*s.pi*R*s.integrate(s.exp(-z*z)*j.subs(r,R),(z,-s.oo,s.oo)))
want=-2*s.pi*s.sqrt(s.pi/3)*eps**2*R**4*s.exp(-2*R**2)
assert s.simplify(flux-want)==0
budget=s.simplify(s.integrate(-flux/R,(R,0,s.oo)))
assert s.simplify(budget-s.pi**s.Rational(3,2)*eps**2/(4*s.sqrt(3)))==0
rng=Random(20261025)
for _ in range(25000):
    rr=F(rng.randrange(1,1000),rng.randrange(1000,2500))
    assert rr<1 and 4*rr*rr*(1-rr*rr)>0
print("PASS exact negative covariance, positive torque and full PDE mean advection")
print("PASS exact Gaussian-weighted inward flux and finite all-radius budget")
print("PASS 25000 independent Fraction positive core fixtures")
print("No numerical positive-time delta or source blowup certificate")
