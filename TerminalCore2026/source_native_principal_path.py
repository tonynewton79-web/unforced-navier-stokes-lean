"""Source-native symbolic jet composition for the delayed-pressure path.

Applies Z_q = L^-1[2q eta + d*d_eta -2 eta D_X] exactly on radial
monomials X^r, including derivatives of variable coefficients.
Tracks the complete jet polynomial and independently checks the
fourth derivative coefficient in source eqs. (22),(24),(27),(28),(26).
"""
import sympy as S
eta=S.symbols('eta')

def jet_z(P, r, q, d, L):
    ans={}
    for j,c in P.items():
        ans[j]=ans.get(j,0)+(2*q*eta*c-2*eta*r*c+d*S.diff(c,eta))/L
        ans[j+1]=ans.get(j+1,0)+d*c/L
    return {j:S.cancel(c) for j,c in ans.items()}

checks=0
for h in [S.Rational(1,200),S.Rational(1,300),S.Rational(1,150)]:
    D=S.Rational(1,2)-h
    A=S.Rational(1,2)+h
    d=1-eta**2
    L=1-2*h*eta**2
    for n in [2,3,6,11]:
        lam=lambda k:2*h*k
        k=n-2
        for a in [0,1,2,5]:
            V={0:(2*eta-2*eta*(D+lam(k))/(a+1))/L,
               1:-d/(L*(a+1))}
            O=jet_z(jet_z(V,a+1,lam(k),d,L),a+1,lam(k)-D,d,L)
            O={j:-c for j,c in O.items()}
            P={j:S.cancel(-c/(2*(a+1))) for j,c in O.items()}
            source=jet_z(P,a+1,-2*A+lam(n),d,L)
            U={j:S.cancel(c/(2*(a+2)**2)) for j,c in source.items()}
            assert max(U)==4
            principal=-d**4/(4*L**4*(a+1)**2*(a+2)**2)
            assert S.cancel(U[4]-principal)==0,(h,n,a)
            checks+=1
print(f'PASS: {checks} exact symbolic full variable-coefficient fourth-jet composites')
