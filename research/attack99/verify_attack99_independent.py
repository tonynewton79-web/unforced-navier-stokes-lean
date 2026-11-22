#!/usr/bin/env python3
"""Independent source-class rational Gram test; no SymPy."""
from fractions import Fraction as Q
from random import Random
from pathlib import Path
import json
I0=Q(65536,109395);I2=Q(65536,2078505)
L0=Q(131072,45045);L2=Q(131072,255255)
d1=L0-I0**2/(4*I2);d2=L2-I0/4
Dmin=((Q(9,4)*d1+Q(1,16)*d2)*I0*I2)/(16*(Q(25,4)*I0+Q(9,16)*I2))
assert Dmin>0
rng=Random(9911234)
for _ in range(16000):
 x=Q(rng.randrange(-9999,10000),10000)
 a=2+x/2; d=-(1+x/2)/2; p=-2*x/(1-x*x)**2
 g11=a*a*L0+d*d*L2;g12=-I0/8
 g22=I0*(p*a+Q(1,2))**2+I2*(p*d-Q(1,4))**2
 D=g11*g22-g12*g12
 assert D>=Dmin
 beta=Q(rng.randrange(-100,101),rng.randrange(1,101))
 gamma=Q(rng.randrange(-100,101),rng.randrange(1,101))
 c1=(beta*g22-gamma*g12)/D;c2=(gamma*g11-beta*g12)/D
 assert (g11*c1+g12*c2,g12*c1+g22*c2)==(beta,gamma)
g=json.loads(Path(__file__).with_name('release_gate.json').read_text())
assert g['physical_source_tuple'] is None
assert not g['full_unforced_Navier_Stokes_theorem_proven']
print('PASS: 16000 independent exact rational Gram inversions')
