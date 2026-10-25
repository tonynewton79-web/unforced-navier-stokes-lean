#!/usr/bin/env python3
"""Full transported jet commutator and Gaussian viscosity sign, exact SymPy."""
import sympy as S
x,y,z,t,nu,e,k=S.symbols('x y z t nu e k',real=True)
ax=lambda f:S.simplify(f.subs({x:0,y:0}))
A=lambda u,v:-2*S.diff(u,x,y)+S.diff(v,x,2)-S.diff(v,y,2)
B=lambda u,v:S.diff(u,x,2)-S.diff(u,y,2)+2*S.diff(v,x,y)
def Lam(u,v,w):
 a,b=ax(u),ax(v)
 return -(a*ax(A(u,v))+b*ax(B(u,v))+
          S.diff(b*ax(S.diff(w,x))-a*ax(S.diff(w,y)),z))/2
U=(1+t*z)+(2+t*z)*x+(z+3*t)*y+x*y*(2+z)+3*y*y
V=3+t+z*y+(1+t*z)*x+2*x*x+(1+z*t)*y*y+z*x*y
W=z+t+(2+z*t)*x+(3+z+t)*y+x*y+z*y*y
c=ax(W);D=lambda g:S.diff(g,t)+c*S.diff(g,z)
Hu,Hv,Hw=D(U),D(V),D(W)
a,b=ax(U),ax(V);Q=b*ax(S.diff(W,x))-a*ax(S.diff(W,y))
DQ=ax(Hv)*ax(S.diff(W,x))+b*ax(S.diff(Hw,x))-ax(Hu)*ax(S.diff(W,y))-a*ax(S.diff(Hw,y))
RHS=-(ax(Hu)*ax(A(U,V))+a*ax(A(Hu,Hv))+ax(Hv)*ax(B(U,V))+b*ax(B(Hu,Hv))+S.diff(DQ,z)-S.diff(c,z)*S.diff(Q,z))/2
assert S.simplify(D(Lam(U,V,W))-RHS)==0
g=e*S.exp(-(x*x+y*y+z*z))*(x+k*(x*x+y*y)*y)
u,v=S.diff(g,y),-S.diff(g,x)
L=S.factor(Lam(u,v,S.Integer(0)))
Lapl=lambda a:S.diff(a,x,2)+S.diff(a,y,2)+S.diff(a,z,2)
q=S.symbols('q')
heat=S.factor(S.diff(Lam(u+q*nu*Lapl(u),v+q*nu*Lapl(v),S.Integer(0)),q).subs(q,0))
assert S.simplify(L+4*k*e*e*S.exp(-2*z*z))==0
assert S.simplify(heat+16*k*nu*e*e*(2*z*z-7)*S.exp(-2*z*z))==0
print("PASS exact D0 Lambda jet commutator including -c_z Q_z")
print("PASS XLI Lambda initial and complete viscous derivative; signed z=0/z=2")
