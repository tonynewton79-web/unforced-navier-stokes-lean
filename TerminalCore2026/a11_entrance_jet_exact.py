"""Independent Appendix A.10 entrance and A.11 scalar replay. Source geometry
is used, not a synthetic angular moment. Full interval/PDE checks remain open.
"""
from fractions import Fraction as Q
from math import factorial
import sympy as S
eta,theta=S.symbols('eta theta',real=True)
J=S.log(1+eta*eta)
G=S.exp((1-theta)*(J-S.log(2)))
assert S.simplify(S.diff(G,eta)-(1-theta)*S.diff(J,eta)*G)==0
assert S.simplify(S.diff(G,eta)-S.diff(J,eta)*G+theta*S.diff(J,eta)*G)==0
z=Q(1197,400)
part=sum((z**k/Q(factorial(k)) for k in range(21)),Q())
remainder=z**21/Q(factorial(21))/(1-z/22)
assert part+remainder<20
assert Q(1,20)<Q(1,16)
assert (Q(40,17)+Q(20,19))*5<18
assert Q(40,17)*5<12
assert 1/(Q(4,5)*(6-Q(1,7)))==Q(35,164)
assert 8*Q(3,2)**2*320*18*Q(1,20)**28<1
assert Q(3,2)*640*54*Q(1,20)**28<Q(1,2)
assert 2*Q(35,164)*12<6
print('PASS exact eta derivative cancellation, finite-exp certificate,')
print('both-support moment jet (18/12) and genuine correction jets (54/6)')
print('STATUS: source analytic lemma; NOT a terminal gauge or unforced PDE certificate')
