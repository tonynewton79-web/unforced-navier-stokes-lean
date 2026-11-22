#!/usr/bin/env python3
"""Attack 89 exact rational signed continuation verifier.

Source: original Attack89_Signed_PostCutoff_Source_Gate research packet.
Checks algebra and deterministic examples, NOT numerical PDE source enclosure.
"""
from fractions import Fraction as F
from random import Random
import sympy as sp

Lmin=F(47,48)
Lder=F(1,6)
factor=1/Lmin + Lder/Lmin**2
assert factor == F(2640,2209) and factor < F(6,5)
assert -13 + factor < -F(59,5)

rng=Random(892026)
for i in range(30000):
    X0=F(rng.randrange(1,20),rng.randrange(2,30))
    X=X0*F(rng.randrange(1,150),rng.randrange(1,150))
    if X < X0:
        X = X0 * F(rng.randrange(1,150),rng.randrange(1,150))+X0
    e0=F(rng.randrange(-300,301),rng.randrange(1,70))
    q0=F(rng.randrange(-300,301),rng.randrange(1,70))
    q1=F(rng.randrange(-300,301),rng.randrange(1,70))
    source_mean=(q0+q1)/2
    e=X0/X*e0+(1-X0/X)*source_mean
    assert abs(e)<=max(abs(e0),abs(q0),abs(q1))

for i in range(10000):
    a=F(rng.randrange(0,300),rng.randrange(1,300))
    b0=F(rng.randrange(0,300),rng.randrange(1,300))
    b1=F(rng.randrange(0,300),rng.randrange(1,300))
    E=max(a,b1/Lmin+Lder*b0/Lmin**2)
    assert E>=a and E>=b1/F(47,48)+b0*F(1,6)/F(47,48)**2
    if a<=1 and b0<=1 and b1<=1:
        assert E <= factor < F(6,5)

t=sp.symbols('t')
rho=t**10*(1-t)**10
Beta=sp.integrate(rho,(t,0,1))
sigma=sp.integrate(rho,(t,0,t))/Beta
nine=sp.diff(sigma,t,9)
assert sigma.subs(t,0)==0 and sigma.subs(t,1)==1
for k in range(1,10):
    dk=sp.diff(sigma,t,k)
    assert dk.subs(t,0)==dk.subs(t,1)==0
assert nine != 0

print('PASS: 30,000 exact rational integrating-factor tests')
print('PASS: 10,000 exact rational source-error gate tests')
print('EXACT: derivative multiplier',factor,'< 6/5')
print('PASS: polynomial C9 cutoff has flat endpoint jets and nonzero ninth derivative')
print('NOT certified: numerical Case006 source errors, full nine-jet coupling, pressure, trace or unforced PDE')
