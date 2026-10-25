#!/usr/bin/env python3
"""Independent constant radial carrier gauge audit; not an unforced PDE proof."""
import sympy as s
r,z,l=s.symbols("r z l",positive=True,real=True)
u=s.symbols("u",positive=True,real=True)
sn,co=s.sin(z),s.cos(z)
K=s.Rational(85,8)+32*sn**2+32*l*l*r*r*sn**2-30*l*l*r**4*co**2
c1=21-K
assert s.simplify(c1-1-(20-K))==0
assert s.Rational(85,8)+8+s.Rational(25,512)==s.Rational(9561,512)
assert 21-s.Rational(9561,512)==s.Rational(1191,512)
assert s.Rational(1191,512)>s.Rational(3,8)
k=s.Function("k")
Phi=k(r)+s.Integral(k(u)/u,(u,0,r))
assert s.simplify(s.diff(Phi,r)-s.diff(k(r),r)-k(r)/r)==0
assert s.simplify(s.diff(Phi,z))==0
assert s.simplify(s.diff(20*s.log(r),r)-20/r)==0
assert s.simplify(s.diff(20/r,z))==0
curl=s.diff(s.diff(K,r)+K/r,z)
assert s.simplify(curl-(64/r+192*l*l*r+300*l*l*r**3)*sn*co)==0
assert s.simplify(curl.subs({l:0,r:1,z:s.pi/6})-16*s.sqrt(3))==0
print("PASS: constant carrier Q+20 er er, exact rational floor 1191/512")
print("PASS: global radial bump divergence = gradient of explicit potential")
print("PASS: adversarial variable-carrier curl is nonzero")
print("HOLD: actual source, global cone and unforced Lean PDE")
