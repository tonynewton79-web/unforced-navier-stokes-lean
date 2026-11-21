#!/usr/bin/env python3
"""Attack52 exact polynomial dual and rational ledger; not a PDE existence proof."""
from fractions import Fraction as F
import sympy as S
x,y=S.symbols("x y",real=True)
K=(1-x*x)**4
assert S.expand(S.diff(K,x)+8*x*(1-x*x)**3)==0
assert S.expand(S.diff(K,x,2)+8*(1-x*x)**3-48*x*x*(1-x*x)**2)==0
for a in (-1,1):
    for j in range(4): assert S.diff(K,x,j).subs(x,a)==0
I0=S.integrate(K,(x,-1,1)); I2=S.integrate(x*x*K,(x,-1,1))
assert (I0,I2)==(S.Rational(256,315),S.Rational(256,3465))
Jpi=S.factor(S.Rational(2,128**4*16)*(1728*I0+36*I2)*I0)
assert Jpi==S.Rational(529,993484800)
assert F(3,8192)*4<F(1,512)  # |S_tau| =3*pi/8192*tau^(3/2-h), pi<4
h=F(1,200);A=F(1,2)+h; D=F(1,2)-h; beta=F(1,2)-2*h
assert (A+D,beta)==(1,F(49,100))
vt=F(1,8)*(128*8*F(1,8)/2+16*8*F(1,2)*F(1,16))
assert vt==F(17,2)
lap=3*128*8+F(1,8)*128**2*56+F(1,8)*16**2*56
assert lap==119552
mixed=F(1,20)*16+F(1,160)*16+F(1,160)*128
assert mixed==F(17,10)
qr,qt,qz=S.symbols("qr qt qz",real=True)
SOS=S.expand(72*(qr**2+qt**2+qz**2)-(128*qr*qt+16*qz*qt)-(64*(qr-qt)**2+8*(qz-qt)**2+8*qr**2+64*qz**2))
assert SOS==0
chi=16*(y-1)**2*(2-y)**2
assert S.integrate(chi,(y,1,2))==S.Rational(8,15)
assert S.expand(S.diff(chi,y)-32*(y-1)*(2-y)*(3-2*y))==0
source=F(201,4000)*F(3)*F(529,993484800)*F(8,15)
assert source==F(35443,827904000000)
linear=(F(lap)+F(21,2)+mixed)/16
total=linear+72
assert (linear,total)==(F(597821,80),F(603581,80))
lower=source/total
assert lower==F(35443,6246339052800000)>F(567,10**14)
print("PASS: exact J/pi =",Jpi,", all derivative bounds, quadratic SOS and rational margin")
print("PASS: Q_T >",lower,"~",float(lower))
print("HOLD: genuine analytic G1 and all physical Navier-Stokes existence gates")
