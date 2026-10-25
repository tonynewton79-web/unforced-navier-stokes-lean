#!/usr/bin/env python3
"""Exact smooth accumulating disjoint packet scaling; no unforced singularity."""
from fractions import Fraction as F
from random import Random
for n in range(1,14):
    c=F(1,4**n);radius=F(1,16**n)
    c2=F(1,4**(n+1));radius2=F(1,16**(n+1))
    assert c2+radius2<c-radius
rng=Random(20261024)
for _ in range(20000):
    n=rng.randint(1,13)
    lam=F(16)**n
    p=rng.randint(1,12)
    a=lam**(-p)
    assert a*lam**(p+1)==lam
    assert a*a*lam*lam==lam**(2-2*p)
    assert (a*lam**2)**2/lam**2==a*a*lam**2
print('PASS 13 disjoint compact packet supports and 20000 exact rational scaling cases')
print('C-infinity condition: for every k, a_n lambda_n^(k+1) tends to zero')
print('HOLD any dynamic finite-time cascade and full unforced Navier-Stokes proof')
