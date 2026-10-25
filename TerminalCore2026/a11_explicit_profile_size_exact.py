"""Exact source A.11 stage-amplitude gate, NOT a full source/PDE certificate."""
from fractions import Fraction as F
from math import factorial
s8=sum((F(2**k,factorial(k)) for k in range(9)),F(0))
assert s8+F(2**9,factorial(9))/(1-F(2,10))<8
assert (F(1,2)+F(1,20))*F(63,20)==F(693,400)<2
assert 11520*F(1,100)**28<1
for P in (F(2),F(10**6),F(10**100)):
 for Q in (F(1),F(512),F(10**6)):
  lam=F(1,10**20)/((1+P)*Q)
  assert 64*P*lam**44<1
  assert 16*P*lam**45<lam/4
print("PASS exact exp(2), support, corrected-profile and cofinal lambda inequalities")
print("CONDITIONAL: terminal S/Pi gauges, tail and full stress cone not authenticated.")
