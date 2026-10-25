"""Exact rational A11 two-support stress gate. Conditional source hypotheses NOT verified."""
from fractions import Fraction as F
support=2*F(3,10)
hull=F(23,10)
assert support==F(3,5) and hull-support==F(17,10)
a=b=F(1,1000)
Aplus5h=F(2503,5000)
coefficient=(2*(1+a)**2*Aplus5h+support*(1+a)*b)/(1-a)
assert coefficient==F(2509510003,2497500000)
assert coefficient<F(201,200)
assert F(201,200000)<F(1,2)
print("PASS exact A11 support measure, gap, and conditional cone arithmetic")
print("HOLD: authentic A11 eta-jet, terminal gauges, full source cone, Lean integral/PDE proof")
