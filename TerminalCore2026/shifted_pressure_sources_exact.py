"""Exact independent tests of three direct shifted-pressure source estimates.

Theorem proof is in Shifted_Pressure_Source_Closure_Insert.tex.
Checks do not prove the entire two-space recurrence or Theorem 1.1.
"""
from fractions import Fraction as Q
from math import factorial,comb
import sympy as S

def w(a,b,R,rho):
    return R**(-a)*rho**(-b)*Q(factorial(b)*comb(2*a+b,b),(a+1)**2*(b+1)**2)

counts=[0,0,0]
for R,rho in ((Q(1),Q(1)),(Q(3,2),Q(1,4)),(Q(1,7),Q(1,9))):
    for a in range(85):
        r=a+1
        for b in range(85):
            primitive=w(a,b,R,rho)/r/w(a+1,b+1,R,rho)
            ratio=R*rho*Q((a+2)**2*(b+2)**2*(2*a+1)*(2*a+2),
                        (a+1)**3*(b+1)**2*(2*a+b+1)*(2*a+b+2)*(2*a+b+3))
            assert primitive==ratio<=Q(16,3)*R*rho
            counts[0]+=1
            rad=r*w(a,b,R,rho)/w(a,b+1,R,rho)
            assert rad==rho*Q(r*(b+2)**2,(b+1)**2*(2*a+b+1))
            assert rad<=4*rho
            counts[1]+=1
            for j,cap in ((0,Q(16,3)*R*rho),(1,4*R),(2,8*R/rho)):
                assert w(a,b+j,R,rho)/(r**j*w(a+1,b+1,R,rho))<=cap
                counts[2]+=1
print("PASS axis primitive, Laplacian and time-pressure scalar ratios:",counts)

e,h=S.symbols('eta h');B=2*e/(1-2*h*e**2);G=(1-e**2)/(1-2*h*e**2)
D=S.Rational(1,2)-h
a=S.symbols("a")
assert S.factor(4*(a+1)**3*(2*a+3)-3*(a+2)**2)==a*(8*a**3+36*a**2+57*a+32)
assert S.factor(4*(a+1)**2*(2*a+3)-3*(a+2)**2)==a*(8*a**2+25*a+20)
cnt=0
for hh in (S.Rational(1,200),S.Rational(1,800)):
  for k in (1,2,5,9):
    for aa in (k,k+2,k+8):
      r=aa+1;lam=2*hh*k;L=1-2*hh*e*e;H=(S.Rational(1,2)-hh)*e/L
      bfun=B.subs(h,hh);gfun=G.subs(h,hh)
      alpha=1-(S.Rational(1,2)-hh+lam)/r
      f=1+e+e**2+e**3/7
      W=alpha*bfun*f-gfun*S.diff(f,e)/r
      assert S.cancel(r*W-(r*alpha*bfun*f-gfun*S.diff(f,e)))==0
      omega=(r-lam)*W/L+H*S.diff(W,e)
      c0=(r-lam)*alpha*bfun/L+H*alpha*S.diff(bfun,e)
      c1=-(r-lam)*gfun/(r*L)+H*(alpha*bfun-S.diff(gfun,e)/r)
      c2=-H*gfun/r
      assert S.cancel(omega-(c0*f+c1*S.diff(f,e)+c2*S.diff(f,e,2)))==0
      assert 0<=alpha<=1
      cnt+=1
print("PASS direct source-native symbolic coefficient identities:",cnt)
