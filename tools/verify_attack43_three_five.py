#!/usr/bin/env python3
"""Exact finite-dimensional source algebra checks for the 3+5 moment note.
Does NOT certify the actual five-moment discrepancy or the unforced NS PDE.
"""
from fractions import Fraction as F
from math import factorial
import sympy as s

def exp_interval(x,n=40):
    x=F(x)
    if x<0:
        lo,hi=exp_interval(-x,n); return 1/hi,1/lo
    assert x<32
    term=F(1);total=term
    for k in range(1,n+1):
        term*=x/k;total+=term
    return total,total+term*x/(n+1)/(1-x/(n+2))
def certify(x,a,b):
    lo,hi=exp_interval(x); assert F(a)<lo<=hi<F(b),(x,lo,hi,a,b)
def inverse_vandermonde_cap(xs):
    if len(xs)==2:
        (a,b),(c,d)=xs;gap=c-b;return max((b+d)/gap,F(2)/gap)
    sums=[F(0)]*3
    for i in range(3):
        js=[j for j in range(3) if j!=i]
        D=F(1)
        for j in js:
            gap=(xs[i][0]-xs[j][1]) if j<i else (xs[j][0]-xs[i][1])
            assert gap>0;D*=gap
        z,w=(xs[j][1] for j in js)
        for k,num in enumerate((z*w,z+w,F(1))):sums[k]+=num/D
    return max(sums)

for x,a,b in [
 (-F(99,128),F(46,100),F(48,100)),(-F(3,4),F(46,100),F(48,100)),
 (F(93,128),F(206,100),F(212,100)),(F(3,4),F(206,100),F(212,100)),
 (F(9,4),F(948,100),F(950,100)),(-F(33,64),F(59,100),F(61,100)),
 (F(81,20),F(57),F(58)),(F(9,25),F(143,100),F(144,100)),
 (F(3,20),F(116,100),F(117,100)),(F(3,100),F(103,100),F(104,100)),
 (-F(27,100),F(76,100),F(77,100)),(-F(9,50),F(83,100),F(84,100))]:
    certify(x,a,b)
heat=inverse_vandermonde_cap([(F(46,100),F(48,100)),(F(206,100),F(212,100)),(F(948,100),F(950,100))])
axial=inverse_vandermonde_cap([(F(1),F(1)),(F(143,100),F(144,100))])
azimuth=inverse_vandermonde_cap([(F(76,100),F(77,100)),(F(103,100),F(104,100)),(F(116,100),F(117,100))])
assert heat<2 and heat/F(59,100)<F(7,2)
assert axial<6 and azimuth<130 and azimuth/F(83,100)<160
assert 8*14**2*32000*F(1,10**8)<1
assert exp_interval(3)[1]<21 and exp_interval(8)[1]<3000
assert exp_interval(F(4,5))[1]<F(5,2)
assert F(9,5)-F(29,5)*F(1,100)>F(87,50)
assert 4000*F(87,50)/3000>2
assert 360*F(28,10**8)<F(1,9000)
eta,u,E,E0=s.symbols("eta u E E0",real=True)
U=4*eta+u
expr=s.expand((U**2-E**2/2-8*eta*U)-(16*eta**2-E0**2/2-32*eta**2))
assert s.simplify(expr-(u**2-(E**2-E0**2)/2))==0
print("PASS: source-derived heat 3x3 and joining 2+3 Vandermonde interval bounds")
print("PASS: exact five-moment quadratic row cancellation, ideal reference cone")
print("OPEN: authentic d5, corrected cone, full G1 and global unforced solution")
