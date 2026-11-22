#!/usr/bin/env python3
"""Independent fractions-only Attack102 physical coordinate handoff; no SymPy."""
from fractions import Fraction as Q
from math import comb
from random import Random
from pathlib import Path
import json
rng=Random(10222026)
for _ in range(24000):
 n=rng.randint(3,9)
 w=[Q(rng.randint(1,100),rng.randint(1,100)) for i in range(n)]
 r=[Q(rng.randint(1,80),rng.randint(25,100)) for i in range(n)]
 tau=[Q(rng.randint(-100,100),rng.randint(1,100)) for i in range(n)]
 rc=Q(rng.randint(1,200),rng.randint(25,100))
 ell=Q(rng.randint(1,25),rng.randint(100,1000))
 shift=rc-2*ell
 rr=[shift+ell*z for z in r]
 raw=[sum((ww*z**k*t for ww,z,t in zip(w,r,tau)),Q(0)) for k in range(5)]
 for k in (2,4):
  physical=ell*sum((ww*z**k*t for ww,z,t in zip(w,rr,tau)),Q(0))
  pullback=ell*sum((comb(k,j)*shift**(k-j)*ell**j*raw[j] for j in range(k+1)),Q(0))
  assert physical==pullback
 u=Q(rng.randint(-100,100),rng.randint(1,100))
 m=Q(rng.randint(1,100),rng.randint(1,100))
 E=[Q(rng.randint(-100,100),rng.randint(1,10000)) for i in range(n)]
 M2=ell*sum((ww*z**2*t for ww,z,t in zip(w,rr,tau)),Q(0))
 M4=ell*sum((ww*z**4*t for ww,z,t in zip(w,rr,tau)),Q(0))
 E2=ell*sum((ww*z*z*ee*t for ww,z,ee,t in zip(w,rr,E,tau)),Q(0))
 N=ell*sum((ww*z*z*(u-m*z*z/4+ee)*t for ww,z,ee,t in zip(w,rr,E,tau)),Q(0))
 assert N==u*M2-m*M4/4+E2
 for z,ee in zip(rr,E):
  slope=-m*rc/2; rem=ee-m*(z-rc)**2/4
  assert rem/slope==(z-rc)**2/(2*rc)-2*ee/(m*rc)
r=(Q(1),Q(2));tau=(Q(4),Q(-1));rc=Q(2);ell=Q(1,10)
assert sum((z*z*t for z,t in zip(r,tau)),Q(0))==0
assert ell*sum(((rc+ell*(z-2))**2*t for z,t in zip(r,tau)),Q(0))==Q(261,250)!=0
assert Q(239,240)**2<Q(120,121)
assert Q(122,121)<Q(241,240)**2
d=json.loads(Path(__file__).with_name("source_gate.json").read_text())
assert d["source_E_uniform_constant"] is None
assert not d["full_unforced_Navier_Stokes_proven"]
print("PASS: 24000 exact physical torque/chart/affine-remainder tests")
print("PASS: diagnostic M2=0 does not transfer to physical M2 under shifted shell")
