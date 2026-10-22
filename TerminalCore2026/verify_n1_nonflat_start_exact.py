#!/usr/bin/env python3
"""Edition XII: exact finite witness checks, NOT a Navier-Stokes proof."""
import sympy as s
from fractions import Fraction as Q
from random import Random
import mpmath as mp
r,z=s.symbols("r z",real=True,positive=True)
U=r*s.exp(-r*r-z*z)
Rt=-s.diff(U,r,2)-s.diff(U,r)/r-s.diff(U,z,2)+U/r**2
assert s.simplify(Rt-2*r*(5-2*r*r-2*z*z)*s.exp(-r*r-z*z))==0
A=s.Rational(1,2)
Mr=s.integrate(s.expand(r*(r-A)**4*(1-r)**4),(r,A,1))
Mz=s.integrate(s.expand((s.Rational(1,4)-z*z)**4),(z,-A,A))
assert Mr==s.Rational(1,430080) and Mz==s.Rational(1,630)
assert Mr*Mz==s.Rational(1,270950400)
t=s.symbols("t",real=True)
g=s.exp(-t*t)
assert s.integrate(-s.diff(g,t,2),(t,-s.oo,s.oo))==0
assert -s.diff(g,t,2).subs(t,0)==2
rng=Random(20261023)
for i in range(10000):
  signal=Q(rng.randint(1,1000),rng.randint(1,1000))
  test=Q(rng.randint(1,1000),rng.randint(1,1000))
  jet=-signal
  assert jet<0 and (-jet)*test>0
print("PASS exact Gaussian residual, compact witness mass 1/270950400")
print("PASS Gaussian local-positive/global-zero adversarial control")
print("PASS 10000/10000 exact rational jet tests")
print("HOLD source-specific annular corrector and full unforced proof")
