#!/usr/bin/env python3
"""Exact symbolic checks for Edition X coupled first-order axisymmetry.
No source-specific unforced PDE or Lean theorem is claimed.
"""
import sympy as s
from fractions import Fraction as Q
from random import Random
r,z,t,nu=s.symbols("r z t nu",positive=True,real=True)
e=s.exp(-r*r-z*z)
psi=r*r*e*s.exp(-t)
vr=-s.diff(psi,z)/r
vz=s.diff(psi,r)/r
U0=r*e
W=r*z*e*s.exp(-t)
p=r*r*z*e*s.exp(-t)
def lap(x):return s.diff(x,r,2)+s.diff(x,r)/r+s.diff(x,z,2)
def Lt(x):return lap(x)-x/r**2
assert s.simplify(s.diff(r*vr,r)/r+s.diff(vz,z))==0
om=s.diff(vr,z)-s.diff(vz,r)
assert s.simplify(om+(s.diff(psi,r,2)-s.diff(psi,r)/r+s.diff(psi,z,2))/r)==0
assert s.simplify(s.diff(Lt(vr),z)-s.diff(lap(vz),r)-Lt(om))==0
Fr=s.diff(vr,t)-nu*Lt(vr)+s.diff(p,r)-2*U0*W/r
Fz=s.diff(vz,t)-nu*lap(vz)+s.diff(p,z)
assert s.simplify(s.diff(Fr,z)-s.diff(Fz,r)-(
    s.diff(om,t)-nu*Lt(om)-2*s.diff(U0*W,z)/r))==0
assert s.simplify(s.diff(r*Fr,r)/r+s.diff(Fz,z)-(
    lap(p)-2*s.diff(U0*W,r)/r))==0
assert s.simplify(s.diff(U0*W,z).subs(z,0)-r*r*s.exp(-2*r*r-t))==0
v,w,ur,uz,ratio=s.symbols("v w ur uz ratio")
assert s.expand(2*ratio*v*w-w*(v*(ur+ratio)+uz)-w*(v*(ratio-ur)-uz))==0
rng=Random(20261022)
for _ in range(10000):
    a=Q(rng.randint(-100,100),rng.randint(1,100))
    b=Q(rng.randint(-100,100),rng.randint(1,100))
    assert abs(a*b)<=(a*a+b*b)/2
print("PASS divergence/streamfunction/curl/vector-Laplacian/pressure-Poisson")
print("PASS nonzero Gaussian swirl-vorticity forcing and energy cancellation")
print("PASS 10000/10000 exact rational Young inequalities")
print("OPEN source-specific annular corrector, nonlinear zero-force PDE, full Lean proof")
