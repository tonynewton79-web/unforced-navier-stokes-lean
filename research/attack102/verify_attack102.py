#!/usr/bin/env python3
"""Attack102 exact source quadratic-torque and chart tests, NOT full PDE."""
from fractions import Fraction as Q
from random import Random
from pathlib import Path
import json
import sympy as S
R,Rc,U,m,E=S.symbols("R Rc U m E",real=True)
g=U-m*R**2/4+E
g0=U+m*Rc**2/4
g1=-m*Rc/2
err=E-m*(R-Rc)**2/4
assert S.expand(g-g0-g1*R-err)==0
assert S.expand(R**4-2*Rc*R**3+Rc**2*R**2-R**2*(R-Rc)**2)==0
assert Q(239,240)**2<Q(120,121)
assert Q(122,121)<Q(241,240)**2
assert Q(1,2*240*240)==Q(1,115200)
rng=Random(1022026)
for _ in range(20000):
 n=rng.randint(3,8)
 rs=[Q(rng.randint(1,80),rng.randint(20,100)) for j in range(n)]
 ts=[Q(rng.randint(-80,80),rng.randint(1,80)) for j in range(n)]
 ws=[Q(rng.randint(1,80),rng.randint(1,80)) for j in range(n)]
 es=[Q(rng.randint(-80,80),rng.randint(1,10000)) for j in range(n)]
 u=Q(rng.randint(-80,80),rng.randint(1,80))
 mass=Q(rng.randint(1,80),rng.randint(1,80))
 M2=sum((w*r*r*t for w,r,t in zip(ws,rs,ts)),Q(0))
 M3=sum((w*r**3*t for w,r,t in zip(ws,rs,ts)),Q(0))
 M4=sum((w*r**4*t for w,r,t in zip(ws,rs,ts)),Q(0))
 N=sum((w*r*r*(u-mass*r*r/4+ee)*t for w,r,t,ee in zip(ws,rs,ts,es)),Q(0))
 E2=sum((w*r*r*ee*t for w,r,t,ee in zip(ws,rs,ts,es)),Q(0))
 assert N==u*M2-mass*M4/4+E2
 rc=Q(11,20)
 D=sum((w*r*r*(r-rc)**2*t for w,r,t in zip(ws,rs,ts)),Q(0))
 assert M4-2*rc*M3+rc*rc*M2==D
for _ in range(10000):
 s=Q(6)+Q(rng.randrange(0,1001),10000)
 assert Q(239,240)**2<s/Q(121,20)<Q(241,240)**2
# Nontrivial quadratic torque kernel: compact projection and exact polynomial control.
y=S.symbols("y",real=True)
phi=(y-1)**4*(3-y)**4
Ik={k:S.integrate(S.expand(y**k*phi),(y,1,3)) for k in range(2,7)}
a=S.Rational(130257,127349);b=S.Rational(30511,127349)
assert Ik[3]-a*Ik[2]-b*Ik[4]==0
assert Ik[5]-a*Ik[4]-b*Ik[6]==0
assert Ik[4]-a*Ik[3]-b*Ik[5]==S.Rational(12873472,5736435705)>0
d=json.loads(Path(__file__).with_name("source_gate.json").read_text())
assert d["status"]=="SOURCE_NATIVE_QUADRATIC_TORQUE_IDENTITY__ORIGINAL_G_REMAINDER_UNFROZEN"
assert d["source_E_uniform_constant"] is None
assert not d["physical_coordinate_handoff_validated"]
assert not d["full_unforced_Navier_Stokes_proven"]
print("PASS: 20000 exact torque and 10000 shell tests, polynomial kernel witness")
print("HOLD: source E, original physical chart/H8 and full Navier-Stokes")
