"""Exact Appendix-B axis-data fence audit (rational part).

Validates universal rational constants and a diagnostic axis tuple;
does not certify the source's exterior pressure datum or B.2.
"""
from fractions import Fraction as F
import sympy as s

zbound=F(6,5);hmax=F(1,100);jmax=F(1,20)
Lloss=2*hmax*zbound**2
Hprime=F(1,2)+4+12*zbound**2+2*jmax*zbound
Hmag=F(1,2)*zbound+(1+zbound**2)*(4*zbound+jmax)
assert 1-Lloss==F(607,625)
assert 1+Lloss==F(643,625)<F(103,100)
assert Hprime==F(219,10)<22
assert Hmag==F(6217,500)<13
assert F(1)-F(22,100)>F(3,4)
assert F(103,100)*13*F(16,9)<25
assert F(11,10)+F(1,10)/100<F(6,5)
print("PASS universal exact rational complex-tube envelopes")

z=s.symbols("z")
h=s.Rational(1,200);j=s.Rational(1,50)
D=s.Rational(1,2)-h; U=4*z+j;L=1-2*h*z**2
H=s.expand(D*z+(1-z**2)*U)
W=s.expand(1-(1-z**2)*s.diff(U,z)-2*D*z*U)
assert H==-4*z**3-z**2/50+s.Rational(899,200)*z+s.Rational(1,50)
assert s.expand(-W-(3-8*h*z**2+(1-2*h)*j*z))==0
assert H.subs(z,-s.Rational(1,200))==-s.Rational(99,40000)
assert H.subs(z,-s.Rational(1,250))==s.Rational(63123,31250000)
assert 3-8*h-(1-2*h)*j==s.Rational(14701,5000)>s.Rational(28,10)
print("PASS diagnostic polynomial, unique nearby sign bracket and W* lower bound")
print("CERTIFICATION LIMIT: geometric axis data only; actual Pi0, B.2, Lambda0, C0 missing")
