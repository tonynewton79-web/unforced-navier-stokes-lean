#!/usr/bin/env python3
"""Attack92: exact rational conditional parameter hierarchy; source hold mandatory.
No actual numerical Case006 source enclosure or full Navier-Stokes theorem."""
from fractions import Fraction as Q
from random import Random
from pathlib import Path
import json

V=Q(48,47)
D=Q(2640,2209)
M=Q(163,45)
assert M-V/4 == Q(7121,2115)
assert D/4 == Q(660,2209)
assert D == V+Q(1,6)*V**2
assert -13+Q(660,2209)/20 < -Q(129,10)

def ceilq(x): return -(-x.numerator//x.denominator)

def conditional_budget(j,A,B,K):
    """A,B,K are externally hypothetical majorants, NOT source measurements."""
    assert 0<j<=Q(1,20) and min(A,B,K)>=0
    Lam=max(2,ceilq(12*A/j)+1)
    C=max(2,ceilq(12*B/j)+1)
    t1=j/(24*(K+1))
    axis=A/Lam
    source=axis+B/C**2+K*t1
    assert axis<j/12 and source<j/4
    e0=max(axis,V*source)
    e1=max(axis,D*source)
    assert e0<Q(12,47)*j and e1<Q(660,2209)*j
    assert M*j-e0>Q(7121,2115)*j
    assert -13+e1<-Q(129,10)
    return Lam,C,t1

rng=Random(922026)
for _ in range(12000):
    j=Q(rng.randrange(1,100),rng.randrange(2000,12000))
    if j>Q(1,20): j=Q(1,20)
    A=Q(rng.randrange(0,1000),rng.randrange(1,101))
    B=Q(rng.randrange(0,1000),rng.randrange(1,101))
    K=Q(rng.randrange(0,1000),rng.randrange(1,101))
    conditional_budget(j,A,B,K)

for _ in range(15000):
    w=Q(rng.randrange(0,1001),1000)
    e0=Q(rng.randrange(-1000,1001),rng.randrange(1,200))
    es=Q(rng.randrange(-1000,1001),rng.randrange(1,200))
    e=w*e0+(1-w)*es
    assert min(e0,es)<=e<=max(e0,es)
    assert abs(e)<=max(abs(e0),abs(es))

for _ in range(5000):
    j=Q(rng.randrange(1,201),10000)
    Lam=rng.randrange(1,10000)
    unknown_O_constant=2*j*Lam
    assert unknown_O_constant/Lam>j
    assert unknown_O_constant/(100*Lam)<j

g=json.loads(Path(__file__).with_name("source_gate.json").read_text())
assert g["status"]=="NON_EFFECTIVE_EXISTENCE_ONLY__NUMERIC_SOURCE_OPEN"
assert all(g["actual_measured_errors"][k] is None for k in ("a0","a","b0","b1"))
assert all(v is None for v in g["effective_majorants"].values())
assert g["physical_parameter_tuple"] is None
assert g["M_terminal"] is None and not g["full_unforced_theorem_proved"]
print("PASS: 12000 majorant implications, 15000 convexity, 5000 O-constant tests")
print("EXACT CONDITIONAL: n>7121*j/2115; d_eta n<-129/10")
print("HOLD: no source-specific finite tuple, PDE norm, terminal matrix, or blow-up theorem")
