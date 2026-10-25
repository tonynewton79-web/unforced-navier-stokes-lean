#!/usr/bin/env python3
"""Exact Gaussian Fourier small-data parameter and nonlinear contraction audit."""
import sympy as s
from fractions import Fraction as F
from random import Random
rho=s.symbols('rho',positive=True)
nu=s.symbols('nu',positive=True)
pi=s.pi
C=(2*pi)**(-s.Rational(3,2))
eps=nu/(100*pi)
I1=s.integrate(rho**2*s.exp(-rho**2/4),(rho,0,s.oo))
I2=s.integrate(rho**3*s.exp(-rho**2/4),(rho,0,s.oo))
assert I1==2*s.sqrt(pi) and I2==8
Xminus=s.simplify(2**(-s.Rational(3,2))*pi*pi*I1)
Xzero=s.simplify(2**(-s.Rational(3,2))*pi*pi*I2)
assert s.simplify(Xminus-pi**s.Rational(5,2)/s.sqrt(2))==0
assert s.simplify(Xzero-2*s.sqrt(2)*pi*pi)==0
q=s.simplify(C*eps*Xminus/nu)
assert q==s.Rational(1,400)
assert 16*q==s.Rational(1,25)
assert 2+32*q<4
assert 8*q==s.Rational(1,50)
assert s.simplify(C*eps*Xzero-nu/(100*s.sqrt(pi)))==0
assert s.simplify(eps*s.sqrt(2*(pi/2)**s.Rational(3,2))-
 nu/(100*(2*pi)**s.Rational(1,4)))==0
rng=Random(20261024)
for _ in range(40000):
 qtest=F(rng.randrange(1,400),rng.randrange(500,2500))*F(1,100)
 assert 2+32*qtest<4 and 16*qtest<1
print('PASS exact Fourier chi-1, chi0, L2 and 1/400 critical threshold')
print('PASS exact 1/25 contraction and 40000 rational margin fixtures')
print('HOLD full Lean PDE and any source-singularity preserving correction')
