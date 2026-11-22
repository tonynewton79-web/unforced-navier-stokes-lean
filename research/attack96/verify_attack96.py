#!/usr/bin/env python3
"""Attack96 finite identities and source release gate (NOT the full Case006 PDE)."""
from fractions import Fraction as F
from random import Random
from pathlib import Path
import sympy as S
import json
r,z,nu=S.symbols("r z nu",positive=True)
A,B,C,D=[S.Function(t)(r,z) for t in "ABCD"]
E=A-4*B
fr=-S.diff(D,r)+S.diff(A,z)-D/r
fz=S.diff(A,r)+S.diff(D,z)+A/r
LE=lambda e:S.diff(e,r,2)-S.diff(e,z,2)+S.diff(e,r)/r-e/r**2
LD=lambda d:2*S.diff(d,r,z)+S.diff(d,z)/r
assert S.simplify(S.diff(fz,r)-S.diff(fr,z)-LE(E)-4*LE(B)-LD(D))==0
def norm(a,b,c,d):
    terms=[-F(3,2)*d,2*c-4*d,-2*c-4*d,2*a-8*b+4*d,-2*a+8*b+4*d,8*b,-8*b]
    n=max(8*abs(b),2*abs(c)+4*abs(d),2*abs(a-4*b)+4*abs(d))
    assert max(map(abs,terms))==n
    return n
rng=Random(962026)
for i in range(25000):
    k=F(rng.randrange(1,101),rng.randrange(101,1001))
    b=F(rng.randrange(-100,101),1000)*k
    c=F(rng.randrange(-100,101),1000)*k
    if 8*abs(b)>k or 2*abs(c)>k:continue
    d=F(rng.randrange(-100,101),100)*(k-2*abs(c))/4
    e=F(rng.randrange(-100,101),100)*(k/2-2*abs(d))
    a=4*b+e
    assert norm(a,b,c,d)<=k
    p=F(rng.randrange(-100,101),rng.randrange(1,90))
    s=F(rng.randrange(-100,101),rng.randrange(1,90))
    polar=max(k*abs(p)/2,abs(c)*abs(p)+(k-2*abs(c))*abs(s)/4)
    assert abs(e*p+d*s)<=polar
    assert polar+4*abs(b*p)<=k*(abs(p)+abs(s)/4)
psi=r**2*(r-1)**2*(2-r)**2*z**2*(1-z)**2
ur=-S.diff(psi,z)/r
uz=S.diff(psi,r)/r
w=(r-1)**2*(2-r)**2*z**2*(1-z)**2
assert S.simplify(S.diff(r*ur,r)/r+S.diff(uz,z))==0
Trr=ur**2-2*nu*S.diff(ur,r)
Ttt=w**2-2*nu*ur/r
Tzz=uz**2-2*nu*S.diff(uz,z)
Trt=ur*w-nu*(S.diff(w,r)-w/r)
Ttz=uz*w-nu*S.diff(w,z)
Trz=ur*uz-nu*(S.diff(ur,z)+S.diff(uz,r))
ffr=S.diff(Trr,r)+S.diff(Trz,z)+(Trr-Ttt)/r
fft=S.diff(Trt,r)+S.diff(Ttz,z)+2*Trt/r
ffz=S.diff(Trz,r)+S.diff(Tzz,z)+Trz/r
lap=lambda u:S.diff(u,r,2)+S.diff(u,r)/r+S.diff(u,z,2)
cr=ur*S.diff(ur,r)+uz*S.diff(ur,z)-w**2/r-nu*(lap(ur)-ur/r**2)
ct=ur*S.diff(w,r)+uz*S.diff(w,z)+ur*w/r-nu*(lap(w)-w/r**2)
cz=ur*S.diff(uz,r)+uz*S.diff(uz,z)-nu*lap(uz)
for x,y in ((ffr,cr),(fft,ct),(ffz,cz)):assert S.cancel(x-y)==0
phi=(r-1)**4*(2-r)**4
f=z**4*(1-z)**4
tau=S.diff(phi,r,2)/r**2
assert S.integrate(r**2*tau,(r,1,2))==0
assert S.integrate(r**3*tau,(r,1,2))==0
rad=S.integrate(S.expand(phi**2*S.diff(phi,r,2)**2),(r,1,2))
ax=S.integrate(S.expand((f*S.diff(f,z))**2),(z,0,1))
assert rad==F(524,13233463425)
assert ax==F(2,4508102925)
assert 2*rad*ax==F(2096,59657815174123018125)>0
assert norm(F(1,8)+4*F(1,64),F(1,64),F(1,16),F(1,32))==F(3,8)
for i in range(5000):
    m1=F(rng.randrange(1,100),rng.randrange(100,1000))
    m2=F(rng.randrange(1,100),rng.randrange(100,1000))
    g1=F(rng.randrange(11,20),10)
    g2=F(rng.randrange(21,30),10)
    det=m1*m2*(g2-g1)
    m0=F(rng.randrange(-100,101),rng.randrange(1,100))
    n0=F(rng.randrange(-100,101),rng.randrange(1,100))
    c1=(m2*n0-m2*g2*m0)/det
    c2=(m1*g1*m0-m1*n0)/det
    assert m0+c1*m1+c2*m2==0
    assert n0+c1*m1*g1+c2*m2*g2==0
d=json.loads(Path(__file__).with_name("release_gate.json").read_text())
assert d["status"]=="MANUFACTURED_COUPLED_POSITIVE_CONTROL__ACTUAL_H8_SOURCE_HOLD"
assert d["actual_case006_envelope"] is None and d["actual_case006_H8_cone_margin"] is None
assert d["M_terminal"] is None and not d["full_unforced_Navier_Stokes_proven"]
print("PASS: cylindrical PDE tensor and curl identities; exact cone polar")
print("PASS: 25000 rational cone trials, 5000 moment tests")
print("PASS: exact positive swirl-curl dual, both moments neutral")
print("HOLD: actual Case006 source, fixed rho, full PDE and terminal")
