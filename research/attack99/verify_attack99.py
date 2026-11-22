#!/usr/bin/env python3
"""Attack99 exact Appendix AD toroidal-flux algebra; not full Case006 H8."""
from fractions import Fraction as Q
from random import Random
import sympy as S
from pathlib import Path
import json
x,z=S.symbols('x z',real=True)
b=(1-z*z)**4
I0=S.integrate(b*b,(z,-1,1)); I2=S.integrate(z*z*b*b,(z,-1,1))
L0=S.integrate(S.diff(b,z)**2,(z,-1,1)); L2=S.integrate(z*z*S.diff(b,z)**2,(z,-1,1))
assert (I0,I2,L0,L2)==(S.Rational(65536,109395),S.Rational(65536,2078505),S.Rational(131072,45045),S.Rational(131072,255255))
A=2+x/2; B=-(1+x/2)/2; v=S.symbols('v',real=True)
ax=(A+B*z)*b
u=-S.diff(ax,z)
w=(v*(A+B*z)+S.diff(A,x)+S.diff(B,x)*z)*b
G11=S.integrate(S.expand(u*u),(z,-1,1))
G12=S.integrate(S.expand(u*w),(z,-1,1))
G22=S.integrate(S.expand(w*w),(z,-1,1))
assert S.simplify(G11-(A*A*L0+B*B*L2))==0
assert S.simplify(G12+I0/8)==0
assert S.simplify(G22-(I0*(v*A+S.Rational(1,2))**2+I2*(v*B-S.Rational(1,4))**2))==0
assert S.simplify(A*S.diff(B,x)-B*S.diff(A,x)+S.Rational(1,4))==0
D1=L0-I0**2/(4*I2);D2=L2-I0/4
assert D1>0 and D2>0
Dmin=((S.Rational(9,4)*D1+S.Rational(1,16)*D2)*I0*I2)/(16*(S.Rational(25,4)*I0+S.Rational(9,16)*I2))
assert Dmin>0
H0,H1,J0,J1=S.symbols('H0 H1 J0 J1')
poly=S.Poly(S.expand((-2*x)*(A*H0+B*H1)+(1-x*x)**2*(S.diff(A,x)*H0+S.diff(B,x)*H1+A*J0+B*J1)),x)
M=S.Matrix([[S.diff(c,t) for t in (H0,H1,J0,J1)] for c in poly.all_coeffs()])
assert M.rank()==4
rng=Random(992026);beta=Q(-2135,10000);gamma=Q(1895,10000)
for _ in range(12000):
 xx=Q(rng.randint(-999,999),1000); v0=-2*xx/(1-xx*xx)**2
 A0=2+xx/2;B0=-(1+xx/2)/2
 g11=A0*A0*Q(L0)+B0*B0*Q(L2);g12=-Q(I0)/8
 g22=Q(I0)*(v0*A0+Q(1,2))**2+Q(I2)*(v0*B0-Q(1,4))**2
 dd=g11*g22-g12*g12
 assert dd>Q(Dmin)
 c1=(beta*g22-gamma*g12)/dd;c2=(gamma*g11-beta*g12)/dd
 assert (g11*c1+g12*c2,g12*c1+g22*c2)==(beta,gamma)
br=(35*S.sqrt(S.Rational(91,200))+S.sqrt(2))/S.sqrt(1229)
bt=-S.Rational(21,2)/S.sqrt(1229)
bz=(-35*S.sqrt(S.Rational(91,200))+S.sqrt(2))/S.sqrt(1229)
betar=S.simplify(br*bt);gammar=S.simplify(bz*bt);alphar=S.simplify(br*bz)
assert alphar==-S.Rational(4443,9832)
assert S.simplify(betar+147*S.sqrt(182)/9832+21*S.sqrt(2)/2458)==0
assert S.simplify(gammar-147*S.sqrt(182)/9832+21*S.sqrt(2)/2458)==0
assert betar<0 and gammar>0
assert S.Rational(4443,4916)*(-S.Rational(1,2))==alphar
t=S.symbols('t',positive=True)
for a0,b0 in ((S.Rational(3,2),-S.Rational(1,4)),(S.Rational(5,2),-S.Rational(3,4))):
 g11=a0*a0*L0+b0*b0*L2
 g22=I0*(t*a0+S.Rational(1,2))**2+I2*(t*b0-S.Rational(1,4))**2
 dd=g11*g22-(I0/8)**2
 c1=(S.Rational(-1,5)*g22-S.Rational(1,5)*(-I0/8))/dd
 c2=(S.Rational(1,5)*g11-S.Rational(-1,5)*(-I0/8))/dd
 assert S.limit(c1,t,S.oo)==S.Rational(-1,5)/g11
 assert S.limit(c2*t,t,S.oo)==0
g=json.loads(Path(__file__).with_name('release_gate.json').read_text())
assert g['status']=='AD_NONSEPARABLE_FLUX_RIGHT_INVERSE__ORIGINAL_SOURCE_OPEN'
assert g['physical_source_tuple'] is None
assert all(v is None for v in g['authentic_case006'].values())
assert not g['weighted_H8_inverse_certified'] and not g['full_unforced_Navier_Stokes_theorem_proven']
print('PASS: exact Gram identities, strictly positive uniform proxy bound')
print('PASS: separable profile impossibility rank 4')
print('PASS: 12000 rational two-flux inversions and flat endpoint checks')
print('HOLD: original H8 source, source torque, pointwise cone, NS PDE')
