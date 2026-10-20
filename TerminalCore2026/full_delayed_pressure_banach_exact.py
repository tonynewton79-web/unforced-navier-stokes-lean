"""Independent exact checks of the full delayed-viscosity pressure
coefficient symbol and the stronger simultaneous (a+n)-slot bound.

Finite checks support but do not replace the analytical theorem in
DelayedPressureBanach_Insert.tex, much less prove the full PDE recurrence.
"""
from fractions import Fraction as F
from math import comb, factorial
import sympy as S

eta=S.symbols("eta")
def zstep(P,r,q,h):
    d=1-eta**2
    L=1-2*h*eta**2
    out={}
    for j,c in P.items():
        out[j]=out.get(j,0)+(d*S.diff(c,eta)+2*eta*(q-r)*c)/L
        out[j+1]=out.get(j+1,0)+(d/L)*c
    return {j:S.cancel(v) for j,v in out.items()}

count=0
for h in [S.Rational(1,200),S.Rational(1,300),S.Rational(1,150)]:
    D=S.Rational(1,2)-h
    A=S.Rational(1,2)+h
    for n in [2,3,6,11]:
        for a in [n-2,n,n+4,n+10]:
            r=a+1
            B=2*eta/(1-2*h*eta**2)
            G=(1-eta**2)/(1-2*h*eta**2)
            k=n-2
            P={0:B*(r-D-2*h*k),1:-G}
            for q in [2*h*k,2*h*k-D,-2*A+2*h*n]:
                P=zstep(P,r,q,h)
            assert max(P)==4
            assert S.cancel(P[4]+G**4)==0
            count+=1
print("PASS full differential normal-form principal coefficient",count)

def wt(a,b,R,rho):
    return R**(-a)*rho**(-b)*F(factorial(b)*comb(2*a+b,b),(a+1)**2*(b+1)**2)

count=0
for R,rho in [(F(1),F(1)),(F(3,2),F(1,4)),(F(1,7),F(1,9))]:
    for n in range(2,14):
        for a in range(n-2,n+18):
            for b in range(18):
                for j in range(5):
                    lhs=(a+n+1)**(4-j)*wt(a,b+j,R,rho)/(F((a+1)**2*(a+2)**2)*wt(a+2,b,R,rho))
                    rhs=54*R**2*rho**(-j)*F(25,(j+1)**2)*3**(4-j)
                    assert lhs<=rhs,(n,a,b,j)
                    count+=1
print("PASS strong two-index coefficient inequalities",count)
assert 22*87**3==14487066
print("PASS exact coefficient-composition constant")
