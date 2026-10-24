#!/usr/bin/env python3
"""Independent Fourier-angle leakage check, with 30000 exact Fraction cases."""
import sympy as s
from fractions import Fraction as F
from random import Random
t=s.symbols('t',real=True)
a=2*s.cos(t)+3*s.cos(3*t);b=5*s.cos(t)-7*s.cos(3*t)
avg=lambda z:s.simplify(s.integrate(s.expand_trig(z),(t,0,2*s.pi))/(2*s.pi))
assert avg(a*b)==-s.Rational(11,2)
assert avg(2*s.cos(t)*5*s.cos(t))==5
assert avg(3*s.cos(3*t)*(-7*s.cos(3*t)))==-s.Rational(21,2)
p=s.sqrt(s.integrate(s.diff(a,t)**2,(t,0,2*s.pi))*
         s.integrate(s.diff(b,t)**2,(t,0,2*s.pi)))/(2*s.pi*9)
assert s.simplify(p-s.sqrt(85*466)/18)==0 and float(p)>10.5
rng=Random(20261025)
for _ in range(30000):
    aa=[F(rng.randint(-35,35),rng.randint(1,19)) for i in range(8)]
    bb=[F(rng.randint(-35,35),rng.randint(1,19)) for i in range(8)]
    n=rng.randrange(0,7)
    q=sum((aa[k]*bb[k] for k in range(n+1,8)),F(0))
    da=sum((k*k*aa[k]*aa[k] for k in range(n+1,8)),F(0))
    db=sum((k*k*bb[k]*bb[k] for k in range(n+1,8)),F(0))
    assert (n+1)**4*q*q<=da*db
print("PASS exact Fourier leakage at N=2, and 30000 rational tail controls")
print("HOLD source spectral data and full Lean PDE proof")
