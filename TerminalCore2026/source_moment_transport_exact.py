"""Source A.7 + source cumulative moments 4.15: exact SymPy audit.
Does not freeze Appendix-A exterior coefficients.
"""
import sympy as s
X,XR,eta,P=s.symbols('X XR eta P',positive=True)
f=(1+eta**2)**(-1);E=P*f*(X/XR)**s.Rational(1,10)
U=4*eta;H=s.sqrt(2*X)*E
assert s.simplify(s.integrate(U,(X,0,XR))-4*eta*XR)==0
assert s.simplify(s.integrate(U*H,(X,0,XR))-
     s.Rational(5,2)*eta*XR*s.sqrt(2*XR)*P*f)==0
assert s.simplify(s.integrate(U*U-E*E/2,(X,0,XR))-
     XR*(16*eta**2-s.Rational(5,12)*P**2*f**2))==0
y=s.symbols('y',real=True)
u=s.Function('u')(y);e=s.Function('e')(y)
xx=XR*s.exp(y); hh=s.sqrt(2*XR)*s.exp(y/2)*e
ell=s.Rational(1,2)+s.diff(e,y)/e
mm=s.Function('M')(y);jj=s.Function('J')(y);ss=s.Function('S')(y);tt=s.Function('T')(y)
m=mm/(xx*e);j=jj/(xx*hh*e);q=ss/(xx*e**2);d=tt/(xx*e**2)
sub={s.diff(mm,y):xx*u,s.diff(jj,y):xx*u*hh,
     s.diff(ss,y):xx*(u*u-e*e/2),s.diff(tt,y):-xx*e*e/2}
for lhs,rhs in ((m,u/e-(ell+s.Rational(1,2))*m),
 (j,u/e-(2*ell+s.Rational(1,2))*j),
 (q,(u/e)**2-s.Rational(1,2)-2*ell*q),
 (d,-s.Rational(1,2)-2*ell*d)):
 assert s.simplify(s.diff(lhs,y).subs(sub)-rhs)==0
h,ET,XT,t,lam=s.symbols('h ET XT t lam',positive=True)
assert s.simplify(s.integrate(ET**2*XT*t**(-1-2*h)/2,(t,1,s.oo))
                    -XT*ET**2/(4*h))==0
assert s.simplify(s.exp(13/lam)*s.exp(-2*(s.Rational(1,2)+lam)*13/lam)-s.exp(-26))==0
print('PASS exact M/J/S reference anchor, 4 normalized moment ODEs, exterior tail and e^-26 pulse factor')
