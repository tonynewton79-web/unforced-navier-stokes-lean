#!/usr/bin/env python3
"""Independent exact-periodic shear negative control for the source-corrector equation."""
import sympy as s
from fractions import Fraction as F
from random import Random
nu,t,y,amp=s.symbols("nu t y amp",positive=True)
forced=t*s.sin(y)
f=s.simplify(s.diff(forced,t)-nu*s.diff(forced,y,2))
assert s.simplify(f-(1+nu*t)*s.sin(y))==0
unforced=amp*s.exp(-nu*t)*s.sin(y)
w=unforced-forced
assert s.simplify(s.diff(unforced,t)-nu*s.diff(unforced,y,2))==0
assert s.simplify(s.diff(w,t)-nu*s.diff(w,y,2)+f)==0
th=s.symbols("th",real=True)
assert s.integrate(s.sin(th),(th,0,2*s.pi))==0
assert s.integrate(s.cos(th),(th,0,2*s.pi))==0
rng=Random(20261024)
for _ in range(10000):
    sq=F(rng.randint(1,400),rng.randint(1,37))
    lo=sq*F(rng.randint(0,1),8)
    hi=sq*F(rng.randint(0,1),16)
    assert sq-lo-hi>=F(13,16)*sq
print("PASS second independent manufactured forced-vs-unforced exact shear")
print("PASS axisymmetric angular zero-mean and 10000 exact rational partitions")
print("HOLD authentication of actual OpenAI source constants")
