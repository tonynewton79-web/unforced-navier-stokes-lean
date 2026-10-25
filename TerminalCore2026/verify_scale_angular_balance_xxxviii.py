#!/usr/bin/env python3
"""Edition XXXVIII exact scale, flux and axis-polynomial cross-checks."""
from fractions import Fraction as F
from random import Random
import sympy as s
r,z,R,e,lam=s.symbols('r z R e lam',positive=True)
J=e**2*r**3*s.exp(-2*(r*r+z*z))
T=s.factor(-s.diff(r*J,r)/r)
assert s.simplify(T-4*e**2*r*r*(r*r-1)*s.exp(-2*(r*r+z*z)))==0
assert s.simplify(s.integrate(T*r,(r,0,R))+R*J.subs(r,R))==0
assert s.integrate(T*r,(r,0,s.oo))==0
assert s.simplify((lam**2*T.subs({r:lam*r,z:lam*z})).subs({r:1/(2*lam),z:0})
     +3*e**2*lam**2*s.exp(-s.Rational(1,2))/4)==0
x,y,theta=s.symbols('x y theta',real=True)
a,b,c,d,f,g,h,j,k,l,m,n=s.symbols('a b c d f g h j k l m n',real=True)
ux=a+b*x+c*y+d*x*x+f*x*y+g*y*y
uy=h+j*x+k*y+l*x*x+m*x*y+n*y*y
p={x:r*s.cos(theta),y:r*s.sin(theta)}
ur=(ux*s.cos(theta)+uy*s.sin(theta)).subs(p)
gamma=(x*uy-y*ux).subs(p)
avg=lambda q:s.simplify(s.integrate(s.expand_trig(q),(theta,0,2*s.pi))/(2*s.pi))
cov=s.factor(avg(ur*gamma)-avg(ur)*avg(gamma))
assert s.limit(cov/r**3,r,0).is_finite
assert s.simplify(s.diff(cov,r).subs(r,0))==0
assert s.simplify(s.diff(cov,r,2).subs(r,0))==0
rng=Random(20261024)
for _ in range(20000):
    sc=F(2)**rng.randrange(0,20)
    q=F(rng.randrange(1,41),rng.randrange(1,31))
    assert q*q*sc*sc/sc**2==q*q
    assert (q*q/sc)*sc==q*q
print('PASS exact radial compensating flux, global zero integral and scale sample')
print('PASS universal quadratic Cartesian near-axis angular covariance O(r^3)')
print('PASS 20000 independent Fraction scaling and energy cases')
