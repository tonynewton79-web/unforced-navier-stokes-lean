#!/usr/bin/env python3
"""Edition XXII circulation identity and exact arithmetic audit.
Not a proof of the PDE maximum principle, not a singular unforced solution."""
import random
from fractions import Fraction as Q
import sympy as s

r,z,t,nu=s.symbols("r z t nu",positive=True)
U=s.Function("U")(r,z,t)
Vr=s.Function("Vr")(r,z,t)
Vz=s.Function("Vz")(r,z,t)
G=r*U
Ltheta=s.diff(U,r,2)+s.diff(U,r)/r+s.diff(U,z,2)-U/r**2
theta_res=s.diff(U,t)+Vr*s.diff(U,r)+Vz*s.diff(U,z)+Vr*U/r-nu*Ltheta
gamma_res=s.diff(G,t)+Vr*s.diff(G,r)+Vz*s.diff(G,z)-nu*(s.diff(G,r,2)-s.diff(G,r)/r+s.diff(G,z,2))
assert s.simplify(r*theta_res-gamma_res)==0

th=s.symbols("theta",real=True)
q=s.Function("q")(r,th,z,t)
v=s.Function("v")(r,th,z,t)
w=s.Function("w")(r,th,z,t)
p=s.Function("p")(r,th,z,t)
F=s.Function("F")(r,th,z,t)
lap=lambda a:s.diff(a,r,2)+s.diff(a,r)/r+s.diff(a,th,2)/r**2+s.diff(a,z,2)
az=(s.diff(q,t)+v*s.diff(q,r)+q*s.diff(q,th)/r+w*s.diff(q,z)+v*q/r
    -nu*(lap(q)-q/r**2+2*s.diff(v,th)/r**2)+s.diff(p,th)/r-F)
gg=r*q
circ=(s.diff(gg,t)+v*s.diff(gg,r)+q*s.diff(gg,th)/r+w*s.diff(gg,z)
      -nu*(lap(gg)-2*s.diff(gg,r)/r)
      -2*nu*s.diff(v,th)/r+s.diff(p,th)-r*F)
assert s.simplify(r*az-circ)==0

tau,R,h,c=s.symbols("tau R h c",positive=True)
assert s.simplify(R*s.sqrt(tau)*tau**(-s.Rational(1,2)-h)*c-R*c*tau**(-h))==0

rng=random.Random(20261024)
for i in range(50000):
    gain=Q(rng.randint(1,300),rng.randint(1,30))
    f=Q(rng.randint(1,100),rng.randint(1,20))
    e=-f/2+Q(rng.randint(0,100),rng.randint(1,50))
    M=gain*(f+e)+Q(rng.randint(0,100),rng.randint(1,40))
    J=Q(rng.randint(0,100),rng.randint(1,40))
    assert gain*f <=2*(M+J)
    assert e<=M/gain-f
for k in (1,2,3,4,8,12):
    gain=Q(4)*2**k # h=1/200, tau=2^(-200k)
    f=Q(1,3); M=Q(10)
    emax=M/gain-f
    assert gain*(f+emax)==M
assert Q(4)*Q(1,3)*2**12 > Q(10)
print("PASS: 50000 exact rational cases; both cylindrical identities; similarity power.")
print("HOLD: classical PDE comparison hypotheses, authentic source matching, full unforced theorem.")
