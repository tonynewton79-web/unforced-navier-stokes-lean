"""Exact source A.19 support, quadratic and interval-threshold checks.
The actual exterior P_pre-D_post and pre-pulse moments remain unfrozen.
"""
from fractions import Fraction as Q
from math import factorial
import sympy as s
A,K,J1,J2,P,D,a1,a2,b1,b2=s.symbols("A K J1 J2 P D a1 a2 b1 b2")
F=s.expand(K*A**2+P-D+J1*(a1+b1*A)**2+J2*(a2+b2*A)**2)
assert s.expand(F-(K+J1*b1**2+J2*b2**2)*A**2-
 2*(J1*a1*b1+J2*a2*b2)*A-(P-D+J1*a1*a1+J2*a2*a2))==0
assert s.simplify(s.diff(F-K*A*A,A,2)-2*(J1*b1**2+J2*b2**2))==0
for lam in [Q(1,20),Q(1,40),Q(1,100)]:
 assert 13-Q(63,20)*lam>11
 assert 13/lam-1-Q(3,20)>13/lam-3+Q(3,20)
def exp_partial(z,n):
 return sum((z**k/Q(factorial(k)) for k in range(n+1)),Q())
assert exp_partial(Q(74,5),21)>2500000
assert exp_partial(Q(5137,200),28)>100000000000
Dl=(1+Q(1011,1000)*Q(55,2))*Q(4,10000000)
D1=Q(55,2)*Q(4,10000000)
Eb=Q(40,10**11)*20*Dl**2
Ea=Q(80,10**11)*20*Dl*D1
assert Eb<Q(2,10**18) and Ea<Q(4,10**18)
print("PASS exact polynomial, disjoint-support, exponential and")
print("conditional uniform bump energy and amplitude-derivative bounds")
print("No actual numerical exterior balance is certified.")
