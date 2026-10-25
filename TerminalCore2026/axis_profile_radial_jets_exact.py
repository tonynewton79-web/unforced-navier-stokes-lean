"""Exact formal coefficient replay for Appendix-B equations B.12--B.15.

Symbolic Ustar, Wstar, Hstar, Zstar and g2 preserve the real source
dependencies. The pressure trace is NOT replaced by a surrogate.
"""
import sympy as s

eta,Y=s.symbols("eta Y")
L,H,W,Z,chi,zeta,g2=[s.Function(t)(eta)
                       for t in ("L","H","W","Z","chi","zeta","g2")]
Us=s.Function("Us")(eta)
p1,p2,q1,q2=[s.Function(t)(eta) for t in ("p1","p2","q1","q2")]
lam,h,A,D=s.symbols("Lam h A D",nonzero=True)
d=1-eta**2
Phi=1+p1*Y+p2*Y**2
u=q1*Y+q2*Y**2
Ayu=q1*Y/2+q2*Y**2/3
Wc=W+(-2*D*eta*Ayu-d*s.diff(Ayu,eta))/lam
Hc=H+d*u/lam
U=Us+u/lam
p=g2*(Y+p1*Y**2)
DX=lambda v:Y*s.diff(v,Y)
R1=((Wc+h*(1-2*eta*U)+d*u*zeta)*Phi
     +Wc*DX(Phi)+Hc*s.diff(Phi,eta))/L
R2=(A*(1-4*eta*Us)+d*s.diff(Us,eta))*u
R2+=-2*A*eta*u**2/lam+Wc*DX(u)+H*s.diff(u,eta)
R2+=d*u*s.diff(u,eta)/lam-4*A*eta*p+d*s.diff(p,eta)-2*eta*DX(p)
coeff=lambda f,k:s.expand(f).coeff(Y,k)
R10,R11=coeff(R1,0),coeff(R1,1)
R20,R21=coeff(R2,0),coeff(R2,1)
B1=-D*eta*q1-d*s.diff(q1,eta)/2
assert s.expand(R10-(W+h*(1-2*eta*Us))/L)==0
assert s.expand(R11-((2*W+h*(1-2*eta*Us))*p1
 +H*s.diff(p1,eta)+(B1-2*h*eta*q1)/lam+d*q1*zeta)/L)==0
assert R20==0
assert s.expand(R21-((A*(1-4*eta*Us)+d*s.diff(Us,eta)+W)*q1
 +H*s.diff(q1,eta)+d*s.diff(g2,eta)-(4*A+2)*eta*g2))==0
lhs1=2*(Y*s.diff(Phi,Y,2)+2*s.diff(Phi,Y))
lhs2=2*(Y*s.diff(u,Y,2)+s.diff(u,Y))
for a,b in [(coeff(lhs1+chi*Phi-R1/lam,0),
              4*p1+chi-R10/lam),
            (coeff(lhs1+chi*Phi-R1/lam,1),
              12*p2+chi*p1-R11/lam),
            (coeff(lhs2+Z/L-R2/lam,0),2*q1+Z/L),
            (coeff(lhs2+Z/L-R2/lam,1),8*q2-R21/lam)]:
    assert s.expand(a-b)==0
print("PASS eight symbolic source coefficients; first two radial jets and pressure source")
print("The Y-jets are not the separate n=1,n=2 time-similarity correction fields.")
