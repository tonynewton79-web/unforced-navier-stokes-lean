"""Exact source-full-hull stress implication. NOT an authenticated source enclosure."""
from fractions import Fraction as F
L=F(23,10); lm=F(1,20)
dd=11520*lm**28; ee=1280*lm**28
assert 0<dd<F(1,10000) and 0<ee<F(1,10000)
h=lm/100; delta=epsilon=F(1,10000)
A=F(1,2)+h
B=1+2*h*(1+F(47,10))+2*(A+L*h)*(2*delta+delta**2)+L*(1+delta)*epsilon
assert B<F(101,100)*(1-delta)
assert (lm/4)*B/(1-delta) <= F(101,400)*lm
assert F(1,2)-F(101,400)==F(99,400)
print("PASS exact full-hull 101/400 lambda margin; inputs CONDITIONAL")
