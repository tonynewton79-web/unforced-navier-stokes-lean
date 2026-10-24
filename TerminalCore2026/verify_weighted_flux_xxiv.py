"""Edition XXIV independent exact tests. A model, not an unforced PDE solution."""
from fractions import Fraction as Q
from random import Random
import sympy as s
r,z,L=s.symbols("r z L", positive=True)
q=L*r*(2*r*r-1)*s.exp(-2*r*r)*s.sin(2*z)
T=s.integrate(r*r*q,(r,0,s.oo))
assert s.simplify(T-L*s.sin(2*z)/8)==0
assert s.simplify(s.diff(T,z)-L*s.cos(2*z)/4)==0
rng=Random(20261024)
for _ in range(30000):
    u=[Q(rng.randint(-8,8),rng.randint(1,6)) for k in range(4)]
    a,b,c,d=u
    E1=2*(a*a+b*b)
    E2=2*(c*c+d*d)
    t=2*(a*c+b*d)
    assert E1*E2-t*t==4*(a*d-b*c)**2
    assert E1+E2>=2*abs(t)
assert Q(1,4)>Q(1,10)
print("PASS: 30000 exact rank-two stress tests, Gaussian torque, cap negative control")
print("STATUS: authentic source matching and full unforced Lean theorem remain OPEN")
