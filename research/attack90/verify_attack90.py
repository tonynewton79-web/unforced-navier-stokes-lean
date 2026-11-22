#!/usr/bin/env python3
"""Attack90 exact rational and endpoint-flat polynomial audit.

These are CONDITIONAL algebraic checks, NOT numerical enclosures for the
actual upstream pressure/profile, PDE or terminal coupling matrix.
"""
from fractions import Fraction as F
from math import comb, factorial
from random import Random
from pathlib import Path
import json

a=F(48,47); b=F(1,6)*a*a
assert a+b==F(2640,2209)
assert F(13,8)-F(7,30)-a==F(2089,5640)
assert F(1,20)-F(13,3)/8==-F(59,120)

def amp_error(a0,b0):
    return max(a0,a*b0)
def derivative_error(a_endpoint,b0,b1):
    return max(a_endpoint,a*b1+b*b0)

rng=Random(902026)
for _ in range(20000):
    h=F(rng.randint(1,300),1800)
    j0=F(rng.randint(1,300),6000)
    eta=-F(rng.randint(600,1200),4800)
    D=F(1,2)-h
    alpha=F(1,2)+h
    Ustar=4*eta+j0
    assert D*eta+Ustar<=-F(59,120)
    # Uses the CONDITIONAL input M'<-13 from Attack88.
    lower=13*(-eta)-(4+alpha)*j0
    assert lower>=F(167,120)
    assert lower-amp_error(F(1),F(1))>=F(2089,5640)

for _ in range(20000):
    a_endpoint=F(rng.randrange(1000),1000)
    a0=F(rng.randrange(1000),1000)
    b0=F(rng.randrange(1000),1000)
    b1=F(rng.randrange(1000),1000)
    assert amp_error(a0,b0)<=F(48,47)
    assert derivative_error(a_endpoint,b0,b1)<=F(2640,2209)

# Build an exactly rational 9-flat transition in normalized radius
# as the integral of s^8(1-s)^8. Its derivatives of order 1..8
# vanish at BOTH endpoints, so the ninth-derivative Taylor theorem applies.
def deriv(coeff):
    return [i*coeff[i] for i in range(1,len(coeff))] or [F(0)]
def evalpoly(coeff,z):
    ans=F(0)
    for x in coeff[::-1]: ans=ans*z+x
    return ans

rho=[F(0)]*17
for j in range(9):
    rho[8+j]=F((-1)**j*comb(8,j))
anti=[F(0)]+[rho[i]/(i+1) for i in range(len(rho))]
N=evalpoly(anti,F(1))
assert N>0
k0=F(1,4)
step=[F(1)]+[F(0)]*(len(anti)-1)
for i,v in enumerate(anti):
    step[i]-=(1-k0)*v/N
assert evalpoly(step,F(0))==1
assert evalpoly(step,F(1))==k0
d=step
for i in range(1,10):
    d=deriv(d)
    if i<=8:
        assert evalpoly(d,F(0))==0
        assert evalpoly(d,F(1))==0
assert abs(evalpoly(d,F(0)))>=factorial(9)*(1-k0)

gate=json.loads(Path(__file__).with_name("source_release_gate.json").read_text())
assert gate["status"]=="HOLD_SOURCE_NUMERICAL_FREEZE"
for name in ("a","a0","b0","b1","m_I"):
    assert gate["physical_source_bounds"][name] is None
assert gate["terminal_matrix"] is None
assert gate["full_unforced_theorem_proved"] is False
print("PASS: 20,000 exact rational companion-sign/radial-envelope checks")
print("PASS: 20,000 exact rational source-error envelope checks")
print("PASS: flat eight-jet rational polynomial and ninth-derivative test")
print("PASS: conditional sign margin 2089/5640; companion flag <= -59/120")
print("HOLD: no physical Case006 numerical a,a0,b0,b1,m_I or terminal matrix")
