"""Exact rational proof gates for the true sigma'-bump of source (A.5).
No numerical source moment or unforced solution is inferred.
"""
from fractions import Fraction as F
from math import factorial
width=F(3,10)
# sigma(1/4)=1/(1+exp(128/9))<1/20; symmetry and Cauchy-Schwarz.
assert F(128,9)>4
assert sum((F(4**k,factorial(k)) for k in range(5)),F())>19
B2lower=2*F(9,10)**2/width
B2upper=F(64)/width
assert B2lower==F(27,5)>5 and B2upper==F(640,3)
assert F(8*133,65536)<1   # sigma' tail <1; center <=64
def trunc_exp(z,n):
 return sum((z**k/F(factorial(k)) for k in range(n+1)),F())
assert trunc_exp(F(74,5),21)>2500000
assert trunc_exp(F(5137,200),28)>10**11
C=F(57605,2000);eps=F(4,10**7);dcy=F(1,10**11)
value=8*B2upper*20*dcy*(C*eps)**2
deriv=16*B2upper*20*dcy*(C*eps)*(F(55,2)*eps)
assert value<F(5,10**17) and deriv<F(1,10**16)
print('PASS true source bump: 27/5<B2<=640/3; error<5e-17 and dA<1e-16 conditional on source moments')
print('Numerical exterior balance and startup system NOT CERTIFIED.')
