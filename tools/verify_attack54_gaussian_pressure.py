#!/usr/bin/env python3
"""Attack54 exact full-PDE no-go controls. This is NOT a nonzero decay profile or Lean proof."""
import sympy as S
x,y,z,r,zz,a,b,ad,bd = S.symbols('x y z r zz a b ad bd', real=True)
xyz=(x,y,z); f=S.exp(-x*x-y*y-z*z)
S0=S.Matrix([-y*f,x*f,0])
P0=S.Matrix([4*x*z*f,4*y*z*f,4*(1-x*x-y*y)*f])
W=a*S0+b*P0
assert S.simplify(sum(S.diff(W[i],xyz[i]) for i in range(3)))==0
# Full PDE, including physical nonlinear transport: pressure is eliminated only by curl.
F=ad*S0+bd*P0+S.Matrix([
    (W[i]+sum(xyz[j]*S.diff(W[i],xyz[j]) for j in range(3)))/2
    -sum(S.diff(W[i],xyz[j],2) for j in range(3))
    +sum(W[j]*S.diff(W[i],xyz[j]) for j in range(3))
    for i in range(3)])
C=S.diff(F[0],z)-S.diff(F[2],x) # theta curl at y=0, x=r
assert S.simplify(C.subs({x:1,y:0,z:0})-2*S.exp(-1)*(43*b+6*bd))==0
assert S.simplify(C.subs({x:2,y:0,z:0})+4*S.exp(-4)*(53*b+6*bd))==0
assert S.simplify(C.subs({x:1,y:0,z:1,b:0,bd:0})-4*a*a*S.exp(-4))==0
# Independent cylindrical PDE derivation (not a substitution into the Cartesian formula).
g=S.exp(-r*r-zz*zz)
Vr=4*b*r*zz*g; Vtheta=a*r*g; Vz=4*b*(1-r*r)*g
lap=lambda u:S.diff(u,r,2)+S.diff(u,r)/r+S.diff(u,zz,2)
Nr=4*bd*r*zz*g+(Vr+r*S.diff(Vr,r)+zz*S.diff(Vr,zz))/2 -(lap(Vr)-Vr/r**2)+Vr*S.diff(Vr,r)+Vz*S.diff(Vr,zz)-Vtheta**2/r
Nz=4*bd*(1-r*r)*g+(Vz+r*S.diff(Vz,r)+zz*S.diff(Vz,zz))/2-lap(Vz)+Vr*S.diff(Vz,r)+Vz*S.diff(Vz,zz)
CC=S.diff(Nr,zz)-S.diff(Nz,r)
for R,Z in [(1,0),(2,0),(1,1)]:
    assert S.simplify(C.subs({x:R,y:0,z:Z})-CC.subs({r:R,zz:Z}))==0
# Construct nonzero pressure-bearing exact backward profile outside decay class.
U=S.Matrix([x,-y,0]); q=-x*x
assert sum(S.diff(U[i],xyz[i]) for i in range(3))==0
assert all(S.simplify((U[i]+sum(xyz[j]*S.diff(U[i],xyz[j]) for j in range(3)))/2
    -sum(S.diff(U[i],xyz[j],2) for j in range(3))
    +sum(U[j]*S.diff(U[i],xyz[j]) for j in range(3))
    +S.diff(q,xyz[i]))==0 for i in range(3))
# Established forward self-similar Lamb-Oseen pressure-control PDE.
t,rr=S.symbols('t rr', positive=True, real=True)
v=(1-S.exp(-rr**2/(4*t)))/rr
assert S.simplify(S.diff(v,t)-S.diff(v,rr,2)-S.diff(v,rr)/rr+v/rr**2)==0
assert S.simplify(S.limit(v/rr,rr,0)-1/(4*t))==0
print('PASS: nonzero exact backward affine profile with full pressure')
print('PASS: all 3 Gaussian pressure-free curl witnesses, checked twice independently')
print('PASS: full nonlinear Cartesian/cylindrical PDE and forward Oseen control')
print('HOLD: nonzero decaying twisted-periodic profile and external 15-field certificate')
