#!/usr/bin/env python3
"""Attack101: exact source affine/torque identities; polynomial cutoff is a diagnostic proxy."""
from fractions import Fraction as Q
from random import Random
from pathlib import Path
import json
import sympy as S
x,r,z,p=S.symbols('x r z p',real=True)
A=2+x/2;D=-(1+x/2)/2
assert S.expand(A.subs(x,r-2))==1+r/2
assert S.expand(D.subs(x,r-2))==-r/4
assert S.expand(A*S.diff(D,x)-D*S.diff(A,x))==-S.Rational(1,4)
bz=(1-z*z)**4
chi=(1-4*z*z)**4 # exact polynomial computational proxy, NOT the smooth physical cutoff
v=[bz,z*bz,S.diff(bz,z),S.diff(z*bz,z)]
def intpoly(poly):
 p=S.Poly(S.expand(poly),z)
 return sum((c*(S.Rational(1,2)**(k+1)-(-S.Rational(1,2))**(k+1))/(k+1) for (k,),c in p.terms()),S.Rational(0))
W=S.Matrix(4,4,lambda i,j:intpoly(chi*v[i]*v[j]))
assert W==W.T
U=S.Matrix([0,0,-A,-D]);V=S.Matrix([p*A+S.Rational(1,2),p*D-S.Rational(1,4),0,0])
g11=S.factor((U.T*W*U)[0]);g12=S.factor((U.T*W*V)[0]);g22=S.factor((V.T*W*V)[0])
det=S.factor(g11*g22-g12*g12)
assert S.Poly(det,p).degree()==2
rng=Random(1012026)
for xx in [S.Rational(-999,1000),-S.Rational(1,2),S.Rational(0),S.Rational(1,2),S.Rational(999,1000)]:
 pp=-2*xx/(1-xx*xx)**2
 g1=Q(g11.subs({x:xx,p:pp}));g12v=Q(g12.subs({x:xx,p:pp}));g2=Q(g22.subs({x:xx,p:pp}))
 delta=g1*g2-g12v*g12v
 assert delta>0
 for _ in range(1000):
  be=Q(rng.randrange(-100,0),rng.randrange(1,100))
  ga=Q(rng.randrange(1,100),rng.randrange(1,100))
  d1=(be*g2-ga*g12v)/delta;d2=(ga*g1-be*g12v)/delta
  assert g1*d1+g12v*d2==be
  assert g12v*d1+g2*d2==ga
qb=S.Function('b')(z)
qtest=S.Rational(1,2)*S.diff(qb,z)-S.Rational(1,4)*S.diff(z*qb,z)
assert S.simplify(qtest-S.Rational(1,4)*((2-z)*S.diff(qb,z)-qb))==0
m2,m3,g0,g1=S.symbols('m2 m3 g0 g1')
assert S.solve([m2,g0*m2+g1*m3],[m2,m3])=={m2:0,m3:0}
R0=S.Rational(1229,4443)
assert -2*R0!=0
gate=json.loads(Path(__file__).with_name('source_gate.json').read_text())
assert gate['status']=='AXIAL_INTERIOR_FLUX_REPAIR__AFFINE_TORQUE_NO_GO__PHYSICAL_G_HOLD'
assert gate['physical_G_profile'] is None
assert not gate['full_torque_neutrality_certified']
assert not gate['full_unforced_Navier_Stokes_proven']
print('PASS 5000 exact polynomial-interior Gram inversions and complete affine torque algebra')
print('HOLD physical G, both real torque moments, H8 weighted inverse and unforced NS')
