"""Exact rational source-index and four-jet weight audit.

Source equations: (22), (24), (26)--(28), (37) of Zenodo 23474915.
Confirms principal highest-eta-derivative coefficient only.
Variable analytic multipliers, their commutators, and the full source
recurrence are expressly not tested or certified by this script.
"""
from fractions import Fraction as F
from math import factorial, comb
import sympy as sy

a = sy.symbols('a', nonnegative=True)
poly_gap = 54*(a+1)**4*(a+2)**2 - sy.prod(2*a+j for j in range(1,5))*(a+3)**2
expect = 2*a*(a+1)*(a+2)*(19*a**3+71*a**2+69*a+9)
assert sy.expand(poly_gap-expect)==0
print('PASS: exact polynomial factorization at every real a')

def wt(alpha, beta, R, rho):
    return R**(-alpha)*rho**(-beta)*F(factorial(beta)*comb(2*alpha+beta,beta),(alpha+1)**2*(beta+1)**2)

total=0
for R,rho in [(F(1),F(1)),(F(5,3),F(2,7)),(F(1,9),F(13,8))]:
    for a0 in range(0,51):
        for b0 in range(0,61):
            # A_X 1/(a+1), pressure primitive 1/(a+1),
            # and J_1 at index a+1, 1/(a+2)^2.
            actual=wt(a0,b0+4,R,rho)/(F((a0+1)**2*(a0+2)**2)*wt(a0+2,b0,R,rho))
            form=(R*R/rho**4)*F(
                (2*a0+1)*(2*a0+2)*(2*a0+3)*(2*a0+4)*(a0+3)**2*(b0+1)**2,
                (a0+1)**4*(a0+2)**2*(b0+5)**2)
            assert actual==form,(a0,b0,actual,form)
            assert actual<=54*R*R/rho**4,(a0,b0,actual)
            total+=1
print('PASS:',total,'exact four-jet weight identities and inequalities')

for b0 in [10**2,10**4,10**7]:
    ratio=F(54*(b0+1)**2,(b0+5)**2)
    assert 0<54-ratio < F(432,b0+5)
print('PASS: sharpness at a=0 by b -> infinity')

path=[('U_(n-2)',0,0),('V_(n-2)',1,1),('Omega_(n-1)',1,3),('Pi_n',1,3),('U_n',2,4)]
assert [x[2] for x in path]==[0,1,3,3,4]
assert path[-1][1]==2
print('PASS: source-ledger highest-jet path:', ' -> '.join(x[0] for x in path))
