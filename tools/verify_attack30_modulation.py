#!/usr/bin/env python3
"""Independent exact-scaling replay for the October 29/November 8 H8 cross-audit.

This is an algebraic diagnostic for the already-obstructed frozen A.5 seed,
not a PDE, analytic-norm, pressure/stress, or Lean existential certificate.
"""
import sympy as sp

h = sp.Rational(1, 200)
A = sp.Rational(1, 2) + h
D = sp.Rational(1, 2) - h
p = 1 + D - 2*A
tau, eta, X = sp.symbols('tau eta X', positive=True)
d = 1 - eta**2
ell = 1 - 2*h*eta**2
q = tau/d
assert p == sp.Rational(97, 200)
assert p + 2*h == sp.Rational(99, 200)
assert sp.simplify(q**D*ell/d - sp.diff(q**D*eta,eta)) == 0
dpos=sp.symbols('dpos',positive=True)
assert sp.simplify((tau/dpos)**(1+D)/(tau**(1+D)/dpos**(1+D)))==1
R2factor = 2*sp.Rational(16,15)*sp.Rational(1,64)
assert R2factor == sp.Rational(1,30)
M0,M1=sp.symbols('M0 M1',positive=True)
M=M0*tau**p+M1*tau**(p+2*h)
Md=-sp.diff(M,tau)
ratio=sp.factor(tau*Md/M)
assert sp.simplify(ratio+p+2*h*M1*tau**(2*h)/(M0+M1*tau**(2*h)))==0
assert sp.limit(ratio,tau,0,dir='+') == -p
kappa=15*sp.pi**2-(p+2*h)/2
kappa0=15*sp.pi**2-p/2
assert sp.simplify(kappa-(15*sp.pi**2-sp.Rational(99,400)))==0
assert sp.simplify(kappa0-(15*sp.pi**2-sp.Rational(97,400)))==0
assert float(kappa.evalf(30))>147
s=sp.symbols('s',positive=True)
assert sp.integrate(1/s,(s,sp.Rational(1,2),1))==sp.log(2)
print("PASS: implicit-q physical Jacobian and A.5 compact radial support")
print("PASS: diagnostic energy exponents 97/200 and 99/200")
print("PASS: c_A uniform and terminal-asymptotic source bounds")
print("PASS: dyadic complete-amplitude injection bound")
print("kappa_uniform",sp.N(kappa,17))
print("kappa_asymptotic",sp.N(kappa0,17))
print("dyadic",sp.N(kappa0*sp.log(2),17))
