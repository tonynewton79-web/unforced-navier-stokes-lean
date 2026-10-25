#!/usr/bin/env python3
"""Independent closed heat semigroup and pressure-complete half-turn parity."""
import sympy as S
x,y,z,s,nu,e,k=S.symbols('x y z s nu e k',real=True,positive=True)
G=s**(-S.Rational(3,2))*S.exp(-(x*x+y*y+z*z)/s)
F=e*G*(x/s+k*y*(x*x+y*y)/s**3+2*k*(s-1)*y/s**2)
u=S.diff(F,y);v=-S.diff(F,x)
ax=lambda h:S.simplify(h.subs({x:0,y:0}))
A=-2*S.diff(u,x,y)+S.diff(v,x,2)-S.diff(v,y,2)
B=S.diff(u,x,2)-S.diff(u,y,2)+2*S.diff(v,x,y)
L=S.factor(-(ax(u)*ax(A)+ax(v)*ax(B))/2)
assert S.simplify(L+4*e*e*k*S.exp(-2*z*z/s)/s**7)==0
assert S.simplify(4*nu*S.diff(L,s).subs(s,1)+16*nu*e*e*k*(2*z*z-7)*S.exp(-2*z*z))==0
u0,v0=u.subs(s,1),v.subs(s,1)
assert all(S.simplify(h.subs({x:-x,y:-y})-h)==0 for h in (u0,v0))
N1=x*(1+z)+x*y*y;N2=y*(2+z)+x*x*y;N3=x*x+y*y
q=S.symbols('q')
def lmb(u,v,w):
 Q=ax(v)*ax(S.diff(w,x))-ax(u)*ax(S.diff(w,y))
 return -(ax(u)*ax(-2*S.diff(u,x,y)+S.diff(v,x,2)-S.diff(v,y,2))+ax(v)*ax(S.diff(u,x,2)-S.diff(u,y,2)+2*S.diff(v,x,y))+S.diff(Q,z))/2
assert S.simplify(S.diff(lmb(u0+q*N1,v0+q*N2,q*N3),q).subs(q,0))==0
assert S.simplify((4*nu*S.diff(L,s).subs(s,1)).subs({k:1,z:2})-16*nu*e*e*S.exp(-8))==0
print("PASS independent exact heat Lambda(t,z)=-4 k eps^2 s^-7 exp(-2z^2/s)")
print("PASS half-turn odd/even pressure-complete nonlinear cross term vanishes")
