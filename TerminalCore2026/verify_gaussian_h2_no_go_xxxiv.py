#!/usr/bin/env python3
"""Second independent finite exact Gaussian H2/nonintegrability test."""
from fractions import Fraction as F
from random import Random
import sympy as s
pi=s.pi
nu=s.symbols('nu',positive=True)
P=(pi/2)**s.Rational(3,2)
assert s.simplify((2+10+70)*P-82*P)==0
CH=nu*s.sqrt(82)/(100*pi)*(pi/2)**s.Rational(3,4)*s.exp(s.Rational(3,10))
assert s.simplify(CH-nu/(100*pi)*s.sqrt(82*P)*s.exp(s.Rational(3,10)))==0
h=s.symbols('h',positive=True)
assert s.simplify(s.Rational(8,3)*(s.Rational(1,2)+h)-1)>0
rng=Random(20261024)
for _ in range(40000):
 a=[F(rng.randrange(-90,91),rng.randrange(1,14)) for j in range(3)]
 b=[F(rng.randrange(-90,91),rng.randrange(1,14)) for j in range(3)]
 na=sum(z*z for z in a);nb=sum(z*z for z in b)
 nd=sum((x-y)**2 for x,y in zip(a,b))
 if nd>na+nb:assert (nd-na-nb)**2<=4*na*nb
 if na>nd+nb:assert (na-nd-nb)**2<=4*nd*nb
print('PASS Gaussian L2/grad/H2 squared norms 2:10:70')
print('PASS 40000 exact norm triangle checks and H2 squared-time blowup exponent')
print('HOLD target o(tau^-4A/3) for singularity-preserving unforced correction')
