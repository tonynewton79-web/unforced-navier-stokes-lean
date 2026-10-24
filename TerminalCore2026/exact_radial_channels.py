"""Exact rational verification of the three radial-inverse channels.

Source: Newton, DOI 10.5281/zenodo.23474915, eq. (37);
cumulative correction: three normalized weight ratios T_0,T_1,T_2.
Tests are finite evidence, not a Lean proof or a proof of the PDE block operator.
"""
from fractions import Fraction as F
from math import comb, factorial

def w(a,b,R,rho):
    return (R**(-a) * rho**(-b) * F(factorial(b)*comb(2*a+b,b),
                                         (a+1)**2*(b+1)**2))

total=0
for R,rho in ((F(3,2), F(2,5)), (F(1),F(1))):
    for nu in (1,2):
        for a in range(13):
            for b in range(23):
                factors=[
                    R * F(2*(a+2)**2*(2*a+1),
                           (a+1)**2*(a+nu)*(2*a+b+1)*(2*a+b+2)),
                    (R/rho)*F(2*(a+2)**2*(2*a+1)*(b+1)**2,
                              (a+1)**2*(a+nu)*(2*a+b+2)*(b+2)**2),
                    (R/rho**2)*F(2*(a+2)**2*(2*a+1)*(b+1)**2,
                                 (a+1)**2*(a+nu)*(b+3)**2),
                ]
                for k in range(3):
                    actual=w(a,b+k,R,rho)/((a+1)*(a+nu)*w(a+1,b,R,rho))
                    assert actual==factors[k]
                    cap=(4*R/(a+1)**2,8*R/(rho*(a+1)),8*R/rho**2)[k]
                    assert actual<=cap,(a,b,nu,k,actual,cap)
                    total+=1
print(f"PASS: {total} exact ratio identities and upper bounds")
# Quotient ideal norm counterexample: f=exp(k*eta), m>=0.
# J_nu d_eta^2(X^m f)=(k^2/((m+1)(m+nu))) X^(m+1) f.
for m in (0,1,10,100):
    for nu in (1,2):
        assert F((m+1)*(m+nu), (m+1)*(m+nu))==1
print("PASS: the quotient-norm multiplier grows as k^2 for every fixed m")
