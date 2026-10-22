#!/usr/bin/env python3
"""Exact rational A.10/A.11 finite-gate verifier; no physical PDE certificate."""
from fractions import Fraction as F
from random import Random
import sympy as s

def exp_taylor(x,n):
    t=v=F(1)
    for j in range(1,n+1):
        t=t*x/j
        v+=t
    return v

assert exp_taylor(F(128,9),16)>10**6
assert exp_taylor(F(30),15)>10**10
assert exp_taylor(F(3),8)>20
entrance=F(40,17)/10**10+F(200,99)*(F(1,10**6)+F(1,10**10))
assert entrance < F(3,10**6)
assert F(21,95)==F(420,19)/100
assert F(63,95)<1
assert 2*21*entrance/100<F(1,100000)
assert F(184320,100**28)<F(1,4)

eta,q,rp,a,T = s.symbols('eta q rp a T', real=True)
g=(2/(1+eta**2))**q
assert s.simplify(s.diff(g,eta)+2*eta*q*g/(1+eta**2))==0
front=2*rp*s.exp(-a*T)/(1+eta**2)
assert s.simplify(s.diff(front,eta)+2*eta*front/(1+eta**2))==0

r=Random(20261022)
for _ in range(10000):
    lam=F(r.randrange(1,10001),10**6)
    k=F(r.randrange(0,2501),10000)
    d=F(r.randrange(0,100001),100000)
    assert 0<lam<=F(1,100)
    assert F(3,2)*d/(1-k)<=2*d

print("PASS A10 finite Taylor, rational/derivative identities, 10,000 synthetic gates")
print("AUTHENTIC FULL PDE SOURCE: HOLD; UNSFORCED NS THEOREM: OPEN")
