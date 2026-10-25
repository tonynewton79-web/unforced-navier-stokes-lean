"""Exact source (4.16) algebra, A11 weighted-future and cone arithmetic.
Checks conditional hypotheses, NOT the actual moment-corrected schedule.
"""
from fractions import Fraction as F
import sympy as s
A,h,eta,J0,J1,H0,H1=s.symbols('A h eta J0 J1 H0 H1',real=True)
expr=4*h*eta*(J1/2)-(1-eta**2)*H1+4*A*eta*(-J0/2)-(1-eta**2)*(-H0)
rhs=2*eta*(h*J1-A*J0)+(1-eta**2)*(H0-H1)
assert s.expand(expr-rhs)==0
for h0 in (F(1,100),F(1,1000),F(1,10**8)):
    K=F(83,20)+F(1,2)+F(2,3)*h0**7
    assert K<F(47,10)
    coeff=F(47,10)*(2*(F(1,2)+2*h0)+1)
    assert coeff<=F(2397,250)
    assert coeff/F(20)<F(1,2)
for lam in (F(1,20),F(1,100),F(1,10**6)):
    gam=min(F(3,1280),F(9,8000000)*lam)
    gamp=F(3,10240)*lam
    assert F(640,3)*gam<=F(1,2)
    assert 2*F(2000000,9)*gam<=lam/2
    assert 2*F(640,3)*gamp<=lam/8
    assert (F(3,2)*lam/30)==lam/20
    assert 12*lam<F(9,8)
    assert F(35,4)>4*(2+3*lam)
assert F(9,8)-12*F(1,20)==F(21,40)
print("PASS exact 4.16 reduction; three future-energy envelopes; three bump/slope support budgets; cone margins")
print("UNVERIFIED: true c_i, c_i-eta, Ebaseline, post slopes and moment/pressure gauges")
