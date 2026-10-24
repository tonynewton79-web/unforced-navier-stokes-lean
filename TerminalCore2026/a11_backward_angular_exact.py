"""Exact rational scalar replay for backward source A.11 angular gauge.
All source root and terminal gauges are prerequisites, not certified here.
"""
from fractions import Fraction as F
from math import factorial
lam=F(1,100);B0=F(640,3);B1=F(1715200,9)
z=B0*54*lam**28
assert z<F(1,100)
assert B1*54/(1-z)<11000000
assert B0*6/(1-z)<1300
assert (B1*6/(1-z)+B1*54*B0*6*lam**28/(1-z)**2)<1300000
assert (1-lam+11000000*lam**28)*F(23,10)<3
q=sum((F(3**k,factorial(k)) for k in range(16)),F())
q+=F(3**16,factorial(16))*F(5,4)
assert q<21
assert F(100,99)*F(23,10)*21*11000000<600000000
assert 2*F(23,10)*21*1300000<130000000
assert 130000000+2*1300<131000000
assert 600000000+F(131000000,2)<700000000
assert F(99,100)-F(700000000,100**27)>F(49,50)
a=F(43,20);p=9*F(49,50);w=F(503,2000)/F(49,50)
assert a/p<F(1,4) and w==F(503,1960)
cone=2*(1-F(1,4))**2-F(3,20)*w*w
assert cone==F(85676973,76832000) and cone>F(11,10)
print("CONDITIONAL SCALAR PASS:",cone)
print("NOT A SOURCE CERTIFICATE: terminal S/pressure gauges, N_s tail, full exterior unresolved")
