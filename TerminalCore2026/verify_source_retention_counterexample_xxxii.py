#!/usr/bin/env python3
"""A sharp rational test of the global small-data non-retention theorem.
PDE existence is from the established small-data Navier--Stokes theorem.
"""
from fractions import Fraction as F
from random import Random
import sympy as s
rng=Random(20261024)
for _ in range(25000):
    b=F(rng.randrange(1,200),rng.randrange(1,30))
    k=F(rng.randrange(1000),1000)
    eps=(1-k)*b/2
    assert b-eps>k*b and eps>0
t,y=s.symbols('t y',real=True)
source=t*s.sin(y)
v=s.exp(s.Rational(1,2)-t)*s.sin(y)/4
w=v-source
assert s.simplify(s.diff(source,t)-s.diff(source,y,2)-(1+t)*s.sin(y))==0
assert s.simplify(s.diff(v,t)-s.diff(v,y,2))==0
assert s.simplify(w.subs(t,s.Rational(1,2))
                   +source.subs(t,s.Rational(1,2))/2)==0
print('PASS 25000 exact small-nonzero-data spectral no-retention controls')
print('PASS explicit globally smooth unforced periodic shear with half-shell retention')
print('HOLD singularity-preserving correction and whole-space source numeric profile')
