"""Exact rational regression for Appendix A pulse-entrance source envelopes.

Requires the source's stated stage bounds and parameter-order compatibility;
does not certify a frozen moment-matched exterior or a Navier–Stokes theorem.
"""
from fractions import Fraction as Q
from math import factorial
def partial_exp(x,n):
 return sum((Q(x)**k/Q(factorial(k)) for k in range(n+1)),Q(0))
assert partial_exp(Q(9,2),14)>90
assert partial_exp(15,13)>10**6
assert partial_exp(10,4)>100
assert partial_exp(9,3)>64
assert partial_exp(17,16)>11*10**6
assert Q(40,10**6)+Q(8,90)<Q(9,100)
assert Q(11,12)+Q(320,10000)<1
assert Q(10,9)<Q(9,8)
c=Q(1,10**6)
assert 120*c*Q(17,11)<Q(1,5000)
q=Q(5000,4999)
forward=c*q*Q(9,16)*Q(15,11)+Q(1,4*4999)
backward=c/2+15*c*Q(17,11)+c/Q(11)*(Q(3,4)+Q(1,3*100**7))
assert forward<Q(1,10000)
assert backward<Q(1,40000)
assert Q(1,10000)+Q(1,40000)==Q(1,8000)
assert Q(1,8000)+Q(5,10**17)<Q(1,2500)
print("PASS 5 exponential lower bounds and 7 exact rational source-envelope gates")
print("Conditional: fixed Tf and source azimuthal moment-correction slope bounds required")
