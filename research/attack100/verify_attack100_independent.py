#!/usr/bin/env python3
"""Independent Attack100 exact-fraction verification; no SymPy."""
from fractions import Fraction as Q
from random import Random
import json
from pathlib import Path
rng=Random(1000099)
for i in range(40000):
 p=Q(rng.randrange(-100,101),rng.randrange(1,200))
 h=Q(rng.randrange(1,501),rng.randrange(1,200))
 hx=Q(rng.randrange(-500,501),rng.randrange(1,200))
 c=Q(rng.randrange(-500,501),rng.randrange(1,200))
 cx=Q(rng.randrange(-500,501),rng.randrange(1,200))
 k=p*h+hx
 assert cx*h*h+2*c*h*hx+2*p*c*h*h-2*c*h*k==cx*h*h
for i in range(20000):
 t=Q(rng.randrange(1,100),rng.randrange(10000,100000))
 if t>=Q(1,100): continue
 z=1-t
 w=-2*z/(1-z*z)**2
 wz=-2*(1+3*z*z)/(1-z*z)**3
 assert abs(w)>Q(1,4)/t**2
 assert abs(wz)/w**2<5*t
 assert w*w*t**4>Q(1,16)
 assert t**(-4)>100*t**(-2)
L0=Q(131072,45045);L2=Q(131072,255255)
Gleft=Q(9,4)*L0+Q(1,16)*L2
Gright=Q(25,4)*L0+Q(9,16)*L2
assert Gright-Gleft==4*L0+L2/2>0
beta=-Q(2135,10000)
assert beta/Gright>beta/Gleft
d=json.loads(Path(__file__).with_name('source_gate.json').read_text())
assert not d['original_physical_source_frozen']
assert not d['full_unforced_Navier_Stokes_proven']
print('PASS 40000 independent exact source coefficient identities')
print('PASS 20000 flat-edge scaling comparisons, distinct Gram endpoint control')
