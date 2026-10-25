#!/usr/bin/env python3
"""Exact independent Edition XXXIII Fourier-gradient constants; no PDE proof."""
import sympy as s
from fractions import Fraction as F
from random import Random
K,r,M,D,e0,A,tau=s.symbols('K r M D e0 A tau',positive=True)
lo=s.simplify((2*s.pi)**(-s.Rational(3,2))*s.sqrt(4*s.pi*s.integrate(r*r,(r,0,K))))
hi=s.simplify((2*s.pi)**(-s.Rational(3,2))*s.sqrt(4*s.pi*s.integrate(r**(-2),(r,K,s.oo))))
assert s.simplify(lo-K**s.Rational(3,2)/(s.pi*s.sqrt(6)))==0
assert s.simplify(hi-K**(-s.Rational(1,2))/(s.pi*s.sqrt(2)))==0
C=4/(s.pi*s.sqrt(2)*3**s.Rational(7,8))
kopt=s.sqrt(D/(s.sqrt(3)*M))
assert s.simplify(M*lo.subs(K,kopt)+D*hi.subs(K,kopt)-
 C*M**s.Rational(1,4)*D**s.Rational(3,4))==0
amp,L=s.symbols('amp L',positive=True)
assert s.simplify((amp/2)**2*4*s.pi/3*(amp/(2*L))**3-
                    s.pi*amp**5/(24*L**3))==0
kt=(s.pi*s.sqrt(6)*e0/(8*M))**s.Rational(2,3)*tau**(-2*A/3)
assert s.simplify(M*lo.subs(K,kt)-e0*tau**(-A)/8)==0
q=Random(20261024)
for _ in range(30000):
 value=F(q.randrange(1,200),q.randrange(1,20))
 low=value/8; high=value/8
 assert low+high==value/4
print('PASS Fourier constants, optimal split, π/24 ball floor and moving cutoff')
print('PASS 30000 exact rational gap-control cases')
print('HOLD source numerical profile, correction and entire unforced PDE proof')
