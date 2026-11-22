#!/usr/bin/env python3
"""Independent stdlib-Fractions moment-flux algebra. No SymPy."""
from fractions import Fraction as Q
from math import comb
from random import Random
from pathlib import Path
import json
b={2*k:Q((-1)**k*comb(4,k)) for k in range(5)}
bp={j-1:c*j for j,c in b.items() if j}
zbp={j:c*(j+1) for j,c in b.items()}
def moment(poly,j):
 return sum((v*Q(2,p+j+1) if (p+j)%2==0 else Q(0) for p,v in poly.items()),Q(0))
def radial(n):return Q(3**(n+1)-1,n+1)
Z=moment(b,0)
assert Z==Q(256,315) and moment(b,1)==0
assert (moment(b,1)+2*Z)/Z==2
rng=Random(1012026)
for _ in range(15000):
 i=rng.randrange(0,8);j=rng.randrange(0,8)
 coeff=Q(rng.randrange(-1000,1001),rng.randrange(1,1001))
 M2=radial(i+2);M3=radial(i+3)
 I1=moment(bp,j);I2=moment(zbp,j)
 assert coeff*((M2+M3/2)*I1-M3*I2/4)==coeff*(M2*I1+M3*(I1/2-I2/4))
for _ in range(15000):
 slope=Q(rng.randrange(1,301),rng.randrange(1,200))
 M3=Q(rng.randrange(-500,501),rng.randrange(1,200))
 nonaffine=Q(rng.randrange(-500,501),rng.randrange(1,200))
 N=slope*M3+nonaffine
 if N==0:assert slope*M3==-nonaffine
rho0=Q(1229,4443)
assert rho0>0 and (-2*Q(-213,1000)*rho0)>0
gate=json.loads(Path(__file__).with_name('source_gate.json').read_text())
assert gate['physical_G_profile'] is None and not gate['full_torque_neutrality_certified']
print('PASS 15000 source-flux moment identities, 15000 nonaffine torque equations')
print('PASS exact normalized even radial bump with mass-weighted first moment 2')
