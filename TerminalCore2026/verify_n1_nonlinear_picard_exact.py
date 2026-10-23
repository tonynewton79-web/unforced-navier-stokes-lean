#!/usr/bin/env python3
"""Exact finite Picard scalar test; actual PDE and Lean proof remain HOLD."""
from fractions import Fraction as F
from random import Random
import sympy as s
T,A,f,g,M=s.symbols('T A f g M',positive=True)
assert s.expand((T*f+g*(2*A*M+M*M)-M)-(g*(2*A+M)-s.Rational(1,2))*M).subs(T*f,M/2)==0
rng=Random(20261023)
for _ in range(10000):
 h=F(rng.randrange(1,50),rng.randrange(1,70))
 r=F(rng.randrange(1,50),rng.randrange(1,70))
 a=F(rng.randrange(1,50),rng.randrange(1,70))
 m=2*h*r
 gam=F(rng.randrange(1,50),rng.randrange(50,110))/(4*(2*a+2*m))
 assert gam*(2*a+2*m)<=F(1,2)
 assert h*r+gam*(2*a*m+m*m)<=m
assert F(1)*(2*F(1)+4*F(1)*F(1))>F(1,2)
z,t,k,nu,amp=s.symbols('z t k nu amp',positive=True)
shear=amp*s.exp(-nu*k*k*t)*s.sin(k*z)
assert s.simplify(s.diff(shear,t)-nu*s.diff(shear,z,2))==0
print('PASS 10000 exact rational Picard ball and contraction tests; known shear control')
print('HOLD actual source H3 constants and unforced singularity')
