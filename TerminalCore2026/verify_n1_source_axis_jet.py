#!/usr/bin/env python3
"""Symbolic Appendix B leading source axis jet; full PDE remains OPEN."""
from fractions import Fraction as F
from random import Random
import sympy as s
import mpmath as mp
j,ss,Lam,C,h,R,p2=s.symbols('j ss Lam C h R p2',positive=True)
chi=j*j/(j*j+ss*ss)
p1=(-chi+(-3+h)/Lam)/4
u=R*(1+Lam*p1*R**2/2+Lam*Lam*p2*R**4/4)/C
assert s.simplify(s.diff(u,R,3).subs(R,0)+3*(Lam*chi+3-h)/(4*C))==0
rng=Random(20261023)
for _ in range(10000):
 hh=F(rng.randrange(1,100),rng.randrange(10100,11000))
 jj=F(rng.randrange(1,50),1000); sig=F(rng.randrange(1,50),1000)
 ll=F(rng.randrange(1,1000),rng.randrange(1,100));cc=F(rng.randrange(1,1000),rng.randrange(1,100))
 mass=F(3,4)/cc*(ll*jj*jj/(jj*jj+sig*sig)+3-hh)
 assert mass>=F(897,400)/cc>0
mp.mp.dps=75;hh=mp.mpf(1)/200;jj=mp.mpf(1)/50;sig=mp.mpf(1)/100;ll=mp.mpf(100);cc=mp.mpf(10)**8
pp=(-jj*jj/(jj*jj+sig*sig)+(-3+hh)/ll)/4
jet=-mp.mpf(3)/(4*cc)*(ll*jj*jj/(jj*jj+sig*sig)+3-hh)
def v(x):return x/cc*(1+ll*pp*x*x/2+ll*ll*(mp.mpf(1)/12)*x**4/4)
errors=[]
for dx in [mp.mpf('.005'),mp.mpf('.0025'),mp.mpf('.00125')]:
 approx=(v(2*dx)-2*v(dx)+2*v(-dx)-v(-2*dx))/(2*dx**3)
 errors.append(abs((approx-jet)/jet))
assert errors[0]>errors[1]>errors[2] and abs(errors[1]/errors[0]-mp.mpf('.25'))<mp.mpf('1e-20')
print('PASS source Appendix B axis jet, 10k exact rational signs, 75-digit diagnostic third differences')
print('HOLD complete modified source and unforced Navier-Stokes PDE')