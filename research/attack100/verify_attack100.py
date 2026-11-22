#!/usr/bin/env python3
"""Attack100 symbolic full angular forcing and flat-edge no-go gate.
Continuum dual proof is in the note; this is finite exact regression."""
import sympy as s
from random import Random
from fractions import Fraction as Q
from pathlib import Path
import json
x,z,w,wp=s.symbols('x z w wp',real=True)
A=2+x/2;D=-(1+x/2)/2;p=-2*x/(1-x*x)**2
h=A+D*z;k=p*h+s.diff(h,x)
c1=s.Function('c1')(x);c2=s.Function('c2')(x)
R2=c1*h*h;R1=2*c1*D*h-c2*h*k;R0=c1*D*D-c2*D*k
Z1=-c1*h*k;Z0=-c1*D*k+c2*k*k
rad=lambda a:s.diff(a,x)+2*p*a
assert s.simplify(rad(R2)+2*Z1-s.diff(c1,x)*h*h)==0
u=-D-h*w;v=k
f=rad(c1*u*u+c2*u*v)+s.diff(c1*u*v+c2*v*v,z)+2*w*(c1*u*v+c2*v*v)+s.diff(c1*u*v+c2*v*v,w)*wp
P1=rad(R1)+s.diff(Z1,z)+2*Z0
P0=rad(R0)+s.diff(Z0,z)
assert s.simplify(f-(s.diff(c1,x)*h*h*w*w+Z1*wp+P1*w+P0))==0
b=-2*z/(1-z*z)**2
t=s.symbols('t',positive=True)
assert s.limit(t**2*b.subs(z,1-t),t,0,dir='+')==-s.Rational(1,2)
assert s.limit(t**3*s.diff(b,z).subs(z,1-t),t,0,dir='+')==-1
I0,I2,L0,L2=s.symbols('I0 I2 L0 L2',positive=True)
G11=A*A*L0+D*D*L2
assert s.simplify(G11.subs(x,1)-G11.subs(x,-1))==4*L0+L2/2
# Torque: M(z)/[rho0*I0*b(z)]=m0+m1*z-(n0+n1*z)*b'(z)/b(z).
m0,m1,n0,n1=s.symbols('m0 m1 n0 n1')
moment=m0+m1*z-(n0+n1*z)*b
poly=s.Poly(s.cancel(moment*(1-z*z)**2),z)
mat=s.Matrix([[s.diff(coeff,t0) for t0 in (m0,m1,n0,n1)] for coeff in poly.all_coeffs()])
assert mat.rank()==4
# Exact finite rational witness for a polynomial proxy; not the actual flat source moments.
bz=(1-z*z)**4
ivals={I0:s.integrate(bz*bz,(z,-1,1)),
       I2:s.integrate(z*z*bz*bz,(z,-1,1)),
       L0:s.integrate(s.diff(bz,z)**2,(z,-1,1)),
       L2:s.integrate(z*z*s.diff(bz,z)**2,(z,-1,1))}
g11=G11.subs(ivals);g12=-ivals[I0]/8
g22=ivals[I0]*(p*A+s.Rational(1,2))**2+ivals[I2]*(p*D-s.Rational(1,4))**2
beta=-s.Rational(2135,10000);gamma=s.Rational(1895,10000)
cv=(beta*g22-gamma*g12)/(g11*g22-g12*g12)
assert s.diff(cv,x).subs(x,0)>s.Rational(13,100)
rng=Random(1002026)
for _ in range(30000):
    tt=Q(rng.randrange(1,200),rng.randrange(20000,200000))
    if tt>=Q(1,100):continue
    zz=1-tt
    ww=-2*zz/(1-zz*zz)**2
    assert abs(ww)>Q(1,4)/tt**2
    assert ww*ww*tt**4>Q(1,16)
    assert tt**(-4)>100*tt**(-2)
gate=json.loads(Path(__file__).with_name('source_gate.json').read_text())
assert gate['status']=='AD_ANGULAR_WEIGHTED_WEAK_NO_GO__ORIGINAL_CASE006_HOLD'
assert gate['original_physical_source_frozen'] is False
assert gate['full_weighted_H8_inverse_proven'] is False
assert gate['full_unforced_Navier_Stokes_proven'] is False
print('PASS exact full angular source decomposition, c1prime*h² leading coefficient')
print('PASS distinct Gram endpoints, log-jet limits, torque polynomial rank four')
print('PASS 30000 exact rational edge-power regressions')
print('HOLD original Case006 C4 source, H8, true torque N[G] and full NS')
