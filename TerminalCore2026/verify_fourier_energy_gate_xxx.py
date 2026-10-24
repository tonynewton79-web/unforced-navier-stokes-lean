#!/usr/bin/env python3
"""Edition XXX: exact analytic Fourier heat tests, source-independent."""
from fractions import Fraction as F
from random import Random
import sympy as s
nu,t,z=s.symbols("nu t z", positive=True, real=True)
for n2 in (1,2,3,4,5,8,9,16):
    integral=s.sqrt(n2)*s.integrate(
        s.exp(-nu*n2*(t-z))*s.exp(-2*nu*z),(z,0,t))
    target=(s.sqrt(n2)*t*s.exp(-2*nu*t) if n2==2
        else s.sqrt(n2)*(s.exp(-2*nu*t)-s.exp(-nu*n2*t))
            /(nu*(n2-2)))
    assert s.simplify(integral-target)==0
X,y,A,n=s.symbols("X y A n", real=True, positive=True)
U=A*s.exp(-nu*n*n*t)*s.sin(n*y)
assert s.simplify(s.diff(U,t)-nu*s.diff(U,y,2))==0
V=t*s.sin(n*y)
assert s.simplify(s.diff(V,t)-nu*s.diff(V,y,2)
            -(1+nu*n*n*t)*s.sin(n*y))==0
assert s.simplify((2*s.pi)**(-s.Rational(3,2))
            *s.sqrt(4*s.pi*X)/nu
            -s.sqrt(X)/(s.sqrt(2)*s.pi*nu))==0
rng=Random(20261024)
for i in range(40000):
    a,b,c,d=[F(rng.randint(-30,30),rng.randint(1,9))
             for j in range(4)]
    assert (a*c+b*d)**2 <= (a*a+b*b)*(c*c+d*d)
print("PASS 8 exact Poincare/heat convolution kernels, including resonant k^2=2")
print("PASS exact unforced/forced periodic shear and R3 Fourier shell constant")
print("PASS 40000 exact rational Cauchy fixtures")
print("NO CLAIM of authenticated Section 10 spectral mass or an unforced blowup theorem")
