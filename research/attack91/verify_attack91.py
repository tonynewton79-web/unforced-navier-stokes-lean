#!/usr/bin/env python3
"""Attack91: source-pressure cone and companion-compatible wedge.

Exact rational verification of comparison bounds, plus adversarial samples.
Does NOT compute source-specific a,a0,b0,b1 or certify unforced Navier--Stokes.
"""
from fractions import Fraction as Q
from random import Random
from pathlib import Path
import json

z=Q(1,19600)
bracket=(1-z)*(1-3*z)+Q(1,2)*(1-2*z)
geom=Q(51,100)*(1+Q(1,2520))*Q(5,9)+Q(20,9)
H_floor=Q(3,7)*(1-z)-Q(1,14)
curvature_floor=(1-5*z)/(1+z)**4
assert bracket>Q(149,100)
assert geom<3
assert H_floor>Q(1,3)
assert curvature_floor>Q(9,10)
assert Q(149,90)*4-3==Q(163,45)
assert Q(163,45)-Q(48,47)==Q(5501,2115)
assert Q(16,25)>Q(3,10) # source chi_c≈0.28234558927

rng=Random(910026)
for _ in range(12000):
    j=Q(rng.randrange(1,1001),20000)
    h=Q(rng.randrange(1,101),10100)
    x=Q(1,9)+(Q(1,7)-Q(1,9))*Q(rng.randrange(0,1001),1000)
    eta=-j*x
    alpha=Q(1,2)+h
    D=Q(1,2)-h
    d=1-eta**2
    L=1-2*h*eta**2
    U=4*eta+j
    H=D*eta+d*U
    sigma=j*Q(rng.randrange(1,1001),4000)
    chi=H**2/(H**2+sigma**2)
    assert H>j/3 and chi>Q(16,25)
    assert D*eta+U>=Q(5,14)*j
    assert U>0 and eta<0 and L>0
    P=Q(rng.randrange(200,600),100)
    Jin=5*P**2/(1+eta**2)**2
    outer0=Q(rng.randrange(0,300),rng.randrange(1,100))
    outer1=outer0*Q(rng.randrange(0,1001),1000)
    J0=Jin+outer0
    J1=Jin+outer1
    Pi=-J0/2
    Pip=2*eta*J1/(1+eta**2)
    Zg=-alpha*(1-2*eta*U)*U-4*H
    Zp=-d*Pip+4*alpha*eta*Pi
    M=(Zg+Zp)/L
    assert Zg>-3*j
    assert Zp>Q(298,45)*j
    assert M>Q(163,45)*j
    assert M-Q(48,47)*j>Q(5501,2115)*j

for _ in range(2000):
    eta=-Q(rng.randrange(1,1000),140000)
    P=Q(rng.randrange(200,500),100)
    ratio=(1-5*eta**2)/(1+eta**2)**4
    assert ratio>Q(9,10)
    assert 10*P*P*ratio>9*P*P

gate=Path(__file__).with_name("source_release_gate.json")
if gate.exists():
    d=json.loads(gate.read_text())
    assert d["status"]=="HOLD_ACTUAL_CONTINUATION_ENCLOSURES"
    assert d["actual_source_bounds"]["a0"] is None
    assert d["actual_source_bounds"]["b0"] is None
    assert d["terminal_matrix"] is None
    assert d["full_unforced_theorem_proven"] is False

print("PASS: exact rational M>163j/45, companion>=5j/14, chi>16/25")
print("PASS: 12,000 pressure-moment and 2,000 curvature adversarial checks")
print("IF a0,b0<=j: n>5501j/2115, source inequalities NOT certified")
print("HOLD: full pressure/profile upper bounds, actual continuation, 4 patches, 9 jets, terminal")
