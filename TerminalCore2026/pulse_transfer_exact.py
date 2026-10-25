"""Symbolic check of the exact Appendix-A axial pulse integrating factors.

Source: OpenAI 2026, Appendix A.9 and equations (4.15)-(4.16).
No full pulse certificate or unforced Navier--Stokes theorem is claimed.
"""
import sympy as s
y,eta=s.symbols("y eta",real=True)
lam=s.symbols("lam",positive=True)
a=s.Function("a")(y,eta);ae=s.diff(a,eta)
alpha=s.Rational(1,2)-lam
beta=s.Rational(1,2)-2*lam
for c,forcing in ((alpha,a),(alpha,ae),(beta,a),(beta,ae)):
    F=s.Function("F")(y);q0=s.symbols("q0")
    q=s.exp(-c*y)*(q0+F)
    residual=s.diff(q,y)+c*q-forcing
    assert s.simplify(residual.subs(s.diff(F,y),s.exp(c*y)*forcing))==0
for force in (a*a-s.Rational(1,2),2*a*ae):
    F=s.Function("F")(y);q=s.exp(2*lam*y)*(s.symbols("q0")+F)
    assert s.simplify((s.diff(q,y)-2*lam*q-force).subs(
       s.diff(F,y),s.exp(-2*lam*y)*force))==0
c,Y=s.symbols("c Y")
gamma=1-lam;kappa=1+2*lam
i=1/gamma+(c-1/gamma)*s.exp(-gamma*y)
ie=c*s.exp(-gamma*y)
p=-1/(2*kappa)+(c+1/(2*kappa))*s.exp(-kappa*(Y-y))
pe=c*s.exp(-kappa*(Y-y))
assert s.simplify(s.diff(i,y)+gamma*i-1)==0
assert s.simplify(s.diff(ie,y)+gamma*ie)==0
assert s.simplify(s.diff(p,y)-s.Rational(1,2)-kappa*p)==0
assert s.simplify(s.diff(pe,y)-kappa*pe)==0
eb=s.symbols("eb",positive=True)
E=eb/(1+eta**2)*s.exp(-(s.Rational(1,2)+lam)*y)
ell=s.simplify(s.Rational(1,2)+s.diff(E,y)/E)
g=s.simplify(s.diff(E,eta)/E)
assert ell==-lam and s.diff(ell,eta)==0
assert s.simplify(g+2*eta/(1+eta**2))==0
assert s.simplify(s.diff(g,y)-s.diff(ell,eta))==0
print("PASS six exact convolution solutions, four stable source transfers, and E/g/ell consistency")
print("TRUE Appendix-A moment-matched coefficients and stress ratio NOT CERTIFIED")
