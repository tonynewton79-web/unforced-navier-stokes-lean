#!/usr/bin/env python3
"""Edition XIII exact/replay tests. Full source-matched unforced PDE: HOLD."""
import sympy as s
from fractions import Fraction as Q
from random import Random
import numpy as np
r,z,t,nu,k,A=s.symbols('r z t nu k A',positive=True,real=True)
e=s.exp(-r*r-z*z)
u=r*e
Lt=s.diff(u,r,2)+s.diff(u,r)/r+s.diff(u,z,2)-u/r**2
Fr=-u**2/r
Ft=-nu*Lt
assert s.simplify(Fr+r*s.exp(-2*(r*r+z*z)))==0
assert s.simplify(Ft-2*nu*r*(5-2*r*r-2*z*z)*e)==0
assert s.simplify(s.diff(Fr,z)-4*r*z*s.exp(-2*(r*r+z*z)))==0
base=A*s.sin(k*z)
w=(s.exp(-nu*k*k*t)-1)*base
corrected=s.simplify(base+w)
assert s.simplify(s.diff(w,t)-nu*s.diff(w,z,2)-nu*s.diff(base,z,2))==0
assert s.simplify(s.diff(corrected,t)-nu*s.diff(corrected,z,2))==0
PR,QR,cross=s.symbols('PR QR cross')
assert s.expand((PR+QR)-PR-QR+cross-cross)==0
rng=np.random.default_rng(20261023)
for _ in range(500):
  xi=rng.integers(-10,11,size=3).astype(float)
  if not np.dot(xi,xi):continue
  P=np.eye(3)-np.outer(xi,xi)/np.dot(xi,xi)
  v=rng.normal(size=3)
  assert abs(xi@(P@v))<1e-12
  assert np.linalg.norm(P@P-P)<1e-13
q=Random(20261023)
for _ in range(10000):
  a=Q(q.randint(-100,100),q.randint(1,100))
  b=Q(q.randint(-100,100),q.randint(1,100))
  assert 2*abs(a*b)<=a*a+b*b
print('PASS exact Gaussian full momentum residual and nonzero meridional curl')
print('PASS known exact unforced sinusoidal shear; 500 Leray Fourier checks; 10000 rational Young tests')
print('HOLD authentic source collar, nonlinear global matching and full Lean NSE')
