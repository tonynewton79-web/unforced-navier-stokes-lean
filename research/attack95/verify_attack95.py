#!/usr/bin/env python3
"""Attack95 exact source-curl, moment and 9-jet finite verification ONLY."""
from fractions import Fraction as F
from random import Random
import json
from pathlib import Path
import sympy as sp
ratio=F(60,61)**5
assert ratio==F(777600000,844596301)
assert 1-ratio>F(79,1000)
assert F(60,61)**23<F(927,1000)**5
r,z=sp.symbols('r z',positive=True)
u=sp.Function('u')(r,z)
w=sp.Function('w')(r,z)
p=sp.Function('p')(r,z)
q=(u+w)**2-u**2
dfr=sp.diff(p,r)-q/r
dfz=sp.diff(p,z)
assert sp.simplify(sp.diff(dfr,z)-sp.diff(dfz,r)+sp.diff(q/r,z))==0
assert sp.expand(q-(2*u*w+w**2))==0
rng=Random(952026)
for i in range(25000):
    M0=F(rng.randrange(-500,501),rng.randrange(1,100))
    N0=F(rng.randrange(-500,501),rng.randrange(1,100))
    M1=F(rng.randrange(1,501),rng.randrange(1,100))
    M2=F(rng.randrange(1,501),rng.randrange(1,100))
    g1=F(rng.randrange(-500,501),rng.randrange(1,100))
    g2=F(rng.randrange(-500,501),rng.randrange(1,100))
    if g1==g2:continue
    N1=M1*g1;N2=M2*g2
    det=M1*N2-M2*N1
    assert det!=0
    c1=(M2*N0-N2*M0)/det
    c2=(N1*M0-M1*N0)/det
    assert M0+c1*M1+c2*M2==0
    assert N0+c1*N1+c2*N2==0
for i in range(1,301):
    h=F(i,90000);D=F(1,2)-h;gamma=F(1,2)+h
    assert -gamma-F(9,2)+(1+D)/2==-F(17,4)-F(3,2)*h
    assert -gamma-1-F(9,2)+(1+D)/2==-F(21,4)-F(3,2)*h
    assert 1-2*D==2*h
y=sp.symbols('y')
J=sp.integrate(y**9*(1-y)**9,(y,0,1))
assert J==sp.factorial(9)**2/sp.factorial(19)
g=json.loads(Path(__file__).with_name('release_gate.json').read_text())
assert g['status']=='KINEMATIC_REPAIR_CONSTRUCTED__SOURCE_CURL_HOLD'
assert g['physical_meridional_force_reconstructed'] is False
assert g['H8_cone_margin_certified'] is False
assert g['M_terminal'] is None
assert g['full_unforced_blowup_proven'] is False
print('PASS: exact compact multiplier amplitude ratio, centrifugal pressure curl')
print('PASS: 25000 exact two-moment compensation tests')
print('PASS: 300 anisotropic H9 identities, endpoint-flat bump identity')
print('PASS: source cone, full PDE and terminal claims remain OPEN')
