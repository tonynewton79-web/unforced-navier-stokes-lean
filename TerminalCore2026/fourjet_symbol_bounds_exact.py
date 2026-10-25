"""All derivative orders k<=4 with a two-step radial lift, exact rational.

The all-index proof is the product estimate stated in manuscript; this
program is an independent finite regression, not an end-to-end PDE proof.
"""
from fractions import Fraction as F
from math import comb, factorial

def wt(a,b,R,rho):
    return R**(-a)*rho**(-b)*F(factorial(b)*comb(2*a+b,b),(a+1)**2*(b+1)**2)

checks=0
for R,rho in [(F(1),F(1)),(F(3,2),F(1,3)),(F(2,7),F(5,4))]:
    for a in range(0,33):
        n=a+2
        for b in range(0,31):
            for k in range(0,5):
                ratio=wt(a,b+k,R,rho)/(F((a+1)**2*(a+2)**2)*wt(a+2,b,R,rho))
                lhs=(n+1)**(4-k)*ratio
                rhs=54*R*R*rho**(-k)*F(25,(k+1)**2)*3**(4-k)
                assert lhs<=rhs,(a,b,k,lhs,rhs)
                formula=R*R*rho**(-k)*F(
                    (a+3)**2*F(factorial(2*a+4),factorial(2*a))*
                    F(factorial(2*a+b+k),factorial(2*a+b+4))*(b+1)**2,
                    (a+1)**4*(a+2)**2*(b+k+1)**2)
                assert ratio==formula,(a,b,k)
                checks+=1
print('PASS',checks,'two-step mixed derivative/shift weight bounds with exact rational arithmetic')
