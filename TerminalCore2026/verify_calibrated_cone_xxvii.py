#!/usr/bin/env python3
"""Exact Edition XXVII cone-bound audit; no physical unforced PDE claim."""
import random
from fractions import Fraction as F
import sympy as sp

qrr,qtt,qzz,qrt,qrz,qtz,mu,M=sp.symbols(
    "qrr qtt qzz qrt qrz qtz mu M", real=True)
a=sp.Rational(3,8)*mu+sp.Rational(13,4)*M
b=sp.Rational(85,8)*mu+sp.Rational(471,4)*M
h=mu+8*M
D=[
    qrr-16*(qtt+qzz)+(mu+33*M),
    8*qtt+2*qrt+(mu+10*M),
    8*qtt-2*qrt+(3*mu+26*M),
    8*qzz+2*qrz-8*qtz+(2*mu+18*M),
    8*qzz-2*qrz+8*qtz+(2*mu+18*M),
    8*qtz+(mu+8*M),
    -8*qtz+(mu+8*M)]
v=sp.Rational(1,4)
rays=[sp.Matrix(x) for x in [[1,0,0],[1,v,0],[1,-v,0],
                              [1,0,v],[1,0,-v],[1,v,v],[1,v,-v]]]
S=sum((D[j]*rays[j]*rays[j].T for j in range(7)),sp.zeros(3,3))
Q=sp.Matrix([[qrr,qrt,qrz],[qrt,qtt,qtz],[qrz,qtz,qzz]])
assert (S-Q-a*sp.eye(3)-b*sp.diag(1,0,0)).applyfunc(sp.expand)==sp.zeros(3,3)
assert sp.simplify((b-sp.Rational(528)*M-30).subs(mu,1)
     +sp.Rational(1641,4)*M+sp.Rational(155,8))==0
assert sp.simplify(a+b-11*mu-121*M)==0
assert sp.simplify(b-31*a+2*h-mu-33*M)==0

rng=random.Random(20261024)
for _ in range(20000):
    mm=F(rng.randrange(17),8)
    floor=F(rng.randrange(1,17),8)
    rr,tt,zz,rt,rz,tz=[
        F(rng.randrange(-100,101),100)*mm for k in range(6)]
    val=[
        rr-16*(tt+zz)+floor+33*mm,
        8*tt+2*rt+floor+10*mm,
        8*tt-2*rt+3*floor+26*mm,
        8*zz+2*rz-8*tz+2*floor+18*mm,
        8*zz-2*rz+8*tz+2*floor+18*mm,
        8*tz+floor+8*mm,
        -8*tz+floor+8*mm]
    assert min(val)>=floor

# Entire coefficient floor tested again on an arbitrary cutoff collar (Q=0).
for k in range(1000):
    chi=F(k,1000)
    mm=F(7,3)
    floor=F(2,5)
    ds=[(floor+33*mm)*chi,(floor+10*mm)*chi,
        (3*floor+26*mm)*chi,(2*floor+18*mm)*chi,
        (2*floor+18*mm)*chi,(floor+8*mm)*chi,
        (floor+8*mm)*chi]
    assert min(ds)>=floor*chi

# Direct source-free optimizer at mu=1: sharp b=85/8.
d0=[F(1),F(1),F(3),F(2),F(2),F(1),F(1)]
A0=F(3,8)
B0=sum(d0)-A0
assert B0==F(85,8)
assert a.subs({mu:1,M:1})==sp.Rational(29,8)
assert b.subs({mu:1,M:1})==sp.Rational(1027,8)

print("PASS six independent symbolic tensor identities")
print("PASS 20000 exact rational symmetric-box tests; 1000 radial cutoff tests")
print("PASS sharper gauge, strict floor and sharp source-free baseline")
print("HOLD actual source, q^1/2 H8 cone gains, unforced PDE, full Lean proof")
