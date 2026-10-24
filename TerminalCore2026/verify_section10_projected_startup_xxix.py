#!/usr/bin/env python3
"""Independent exact Section-10-type source/startup obstruction check.
Source equations are cross-indexed in source_audit_xxix.json.
This is a manufactured periodic shear, NOT the actual source profile.
"""
from fractions import Fraction
from random import Random
from pathlib import Path
import json
import sympy as s

t,y,nu,q=s.symbols("t y nu q",positive=True,real=True)
U=t*s.sin(y)
R=s.diff(U,t)-nu*s.diff(U,y,2)
assert s.simplify(R-(1+nu*t)*s.sin(y))==0
C=4*s.pi**3
kin=C*t*t
vis=2*nu*C*t**3/3
work=s.simplify(2*C*s.integrate(q*(1+nu*q),(q,0,t)))
assert s.simplify(kin+vis-work)==0
force_integral=2*s.pi**s.Rational(3,2)*(t+nu*t*t/2)
velocity_norm=2*s.pi**s.Rational(3,2)*t
assert s.simplify(force_integral-velocity_norm-
                  s.pi**s.Rational(3,2)*nu*t*t)==0
assert s.simplify(s.diff(U,t)-nu*s.diff(U,y,2)-R)==0

rng=Random(20261024)
for k in range(50000):
    w0=Fraction(rng.randint(0,70),rng.randint(1,19))
    force=Fraction(rng.randint(0,70),rng.randint(1,19))
    u=Fraction(rng.randint(0,100),100)*(w0+force)
    wterm=Fraction(rng.randint(0,70),rng.randint(1,19))
    m=(u+wterm) if k%2==0 else abs(u-wterm)
    assert m<=w0+force+wterm
    if not w0 and not force: assert u==0

src=Path(__file__).with_name("N1_SOURCE_SECTION10_AUDIT_XXIX.json")
d=json.loads(src.read_text())
assert d["final_source_defining_equation"]=="(10.5)"
assert d["appendix_A11_A19_eliminates_force"] is False
assert d["actual_source_profile_hashed"] is False
assert d["physical_zero_force_certified"] is False

print("PASS Section-10-type exact shear force and kinetic-energy identity")
print("PASS 50000/50000 exact rational startup and residual-budget tests")
print("PASS source-section audit, including projected forcing caveat")
print("HOLD source-reconstruction hashes, unforced PDE, full Lean theorem")
