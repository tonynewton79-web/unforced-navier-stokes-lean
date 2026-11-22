#!/usr/bin/env python3
"""Attack 93: exact partial pressure and analytic-inverse gate, NOT full PDE."""
from fractions import Fraction as Q
from math import factorial
from random import Random
from pathlib import Path
import json

def pi(eta): return -Q(5,2)/(1+eta**2)**2
def pi1(eta): return 10*eta/(1+eta**2)**3
def pi2(eta): return 10*(1-5*eta**2)/(1+eta**2)**4

left,right=-Q(1,140),-Q(1,180)
Plo,Phi=pi(right),pi(left)
Dlo,Dhi=pi1(left),pi1(right)
DDlo,DDhi=pi2(left),pi2(right)
assert Plo == -Q(2624400000,1049824801)
assert Phi == -Q(960400000,384199201)
assert Dlo == -Q(537824000000,7530688538801)
assert Dhi == -Q(1889568000000,34015373377201)
assert DDlo == Q(1475412579200000000,147609026049038401)
assert DDhi == Q(11018259964800000000,1102132112794689601)
assert DDlo>Q(1999,200)

# A necessary, not sufficient, consequence of the actual source
# hierarchy when Md>=0. Diagnostic Pstar=2 and h=1/1000 fail.
assert Q(1,1000)>Q(1,2048)

def term(B,k):
    return (40*Q(B))**k/Q(factorial(k)*factorial(k+1))
def tail(B,K):
    r=40*Q(B)/Q((K+2)*(K+3))
    if r>=1: raise ValueError("insufficient factorial cutoff")
    return term(B,K+1)/(1-r)

for B,K in [(1,30),(10,69),(100,187)]:
    assert tail(B,K)<Q(1,2**64)
    assert sum((term(B,i) for i in range(K+1,K+31)),Q(0))<=tail(B,K)

rng=Random(932026)
for i in range(25000):
    j=Q(rng.randrange(1,1001),20000)
    if j>Q(1,20):j=Q(1,20)
    f=Q(rng.randrange(0,10001),10000)
    eta=-j*(Q(1,9)+f*(Q(1,7)-Q(1,9)))
    assert left<=eta<0
    assert -Q(5,2)<=pi(eta)<=Phi
    assert pi2(eta)>=DDlo
    if j==Q(1,20):
        assert Plo<=pi(eta)<=Phi
        assert Dlo<=pi1(eta)<=Dhi
        assert DDlo<=pi2(eta)<=DDhi

g=json.loads(Path(__file__).with_name("source_gate.json").read_text())
assert g["status"]=="EFFECTIVE_SUBCERTIFICATES_ONLY__FULL_SOURCE_OPEN"
assert g["numeric_parameter_tuple"] is None
assert g["complex_weighted_Mchi"] is None
assert all(g[k] is None for k in ("actual_a0","actual_b0","actual_a","actual_b1","M_terminal"))
assert g["full_unforced_theorem_proven"] is False
print("PASS: 25,000 exact pressure probes and factorial Neumann-tail bounds")
print("PASS: exact rational pressure curvature >=1999/200 Pstar²")
print("HOLD: source Mchi, numerical a0/b0/a/b1, full post-cutoff shear, PDE")
