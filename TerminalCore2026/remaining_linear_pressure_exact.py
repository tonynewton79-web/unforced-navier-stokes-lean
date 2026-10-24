"""Exact audit of the two remaining direct linear pressure terms in Omega_(n-1).
Source eqs (17),(18),(24),(26)--(28), DOI 10.5281/zenodo.23474915.
Tests are exact finite replay, NOT a full uniform analytic PDE proof.
"""
from fractions import Fraction as F
from math import comb, factorial
import sympy as S
z=S.symbols('z')
def Z(P,r,q,h):
    B=2*z/(1-2*h*z*z)
    G=(1-z*z)/(1-2*h*z*z)
    O={}
    for j,v in P.items():
        O[j]=O.get(j,0)+G*S.diff(v,z)+B*(q-r)*v
        O[j+1]=O.get(j+1,0)+G*v
    return {j:S.cancel(v) for j,v in O.items()}
def T(P,r,q,h):
    D=F(1,2)-h
    L=1-2*h*z*z
    O={}
    for j,v in P.items():
        O[j]=O.get(j,0)+((r-q)*v+D*z*S.diff(v,z))/L
        O[j+1]=O.get(j+1,0)+D*z*v/L
    return {j:S.cancel(v) for j,v in O.items()}
checks=0
for h in [S.Rational(1,200),S.Rational(1,400),S.Rational(3,700)]:
    D=S.Rational(1,2)-h
    A=S.Rational(1,2)+h
    L=1-2*h*z*z
    B=2*z/L
    G=(1-z*z)/L
    for n in [2,3,5,9]:
        k=n-1
        for a in [k,k+1,k+4]:
            r=a+1
            H={0:B*(r-D-2*h*k),1:-G}
            lap={j:S.cancel(v/(2*r*r)) for j,v in Z(H,a,2*h*n-2*A,h).items()}
            time={j:S.cancel(-v/(4*r*r*(r+1)**2))
                  for j,v in Z(T(H,r,2*h*k,h),r,2*h*n-2*A,h).items()}
            assert max(lap)==2 and max(time)==3
            assert S.cancel(lap[2]+G**2/(2*r*r))==0
            assert S.cancel(time[3]-G**2*D*z/(4*r*r*(r+1)**2*L))==0
            checks+=1
print("PASS exact symbolic two pressure paths",checks)
def w(a,b,R,rho):
    return R**(-a)*rho**(-b)*F(factorial(b)*comb(2*a+b,b),(a+1)**2*(b+1)**2)
checked=0
for R,rho in [(F(1),F(1,5)),(F(3,2),F(1,7)),(F(1,8),F(1,4))]:
    for n in range(2,23):
        for a in range(n-1,n+8):
            r=a+1
            for b in range(20):
                for j,C in [(0,4*R),(1,8*R/rho),(2,8*R/rho**2)]:
                    lhs=F(r**(2-j),r*r)*w(a,b+j,R,rho)/w(a+1,b,R,rho)
                    assert lhs<=C
                    checked+=1
                for j in range(4):
                    lhs=F(r**(3-j)*n,r*r*(r+1)**2)*w(a,b+j,R,rho)/w(a+2,b,R,rho)
                    rhs=54*R**2*rho**(-j)*F(25,(j+1)**2)*3**(4-j)
                    assert lhs<=rhs
                    checked+=1
print("PASS exact rational weight/shift bounds",checked)
assert 13*89==1157 and 13*8*89==9256
# Each endpoint term of the original quadratic Omega sum appears once
# when k>=1; all middle pairs are in the positive-index remainder.
for k in range(1,201):
    all_pairs={(i,k-i) for i in range(k+1)}
    boundary={(0,k),(k,0)}
    internal={(i,k-i) for i in range(1,k)}
    assert all_pairs==boundary|internal and not boundary&internal
print("PASS endpoint/interior decomposition for all k=1..200")
