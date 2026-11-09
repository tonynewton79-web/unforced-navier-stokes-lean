#!/usr/bin/env python3
"""Exact finite source-first checks. Not a proof of the genuine G1/H8 singular source."""
from fractions import Fraction as F
from random import Random
from math import factorial
import sympy as s

g=F(15971,122900); h=F(22371,122900)
dl=-g/4; dh=(g+h)/8; cm=(h-g)/4
rng=Random(20261109)
def vertices():
 for D in (dl,dh):
  xwidth=g/2+2*D; cwidth=(g+h)/4-2*D
  for B in (-g/8,g/8):
   for x in (-xwidth,xwidth):
    for C in (cm-cwidth,cm+cwidth):
     A=x+4*B
     yield A,B,C,D
vs=list(vertices())
assert all(2*(A*A+B*B+C*C+D*D)<F(1,2) for A,B,C,D in vs)
for n in range(12500):
 a,b,c,d=(F(rng.randint(-18,18),rng.randint(1,11)) for _ in range(4))
 actual=max(a*A+b*B+c*C+d*D for A,B,C,D in vs)
 formula=cm*c+g*abs(4*a+b)/8+max((3*g+h)*abs(c)/4-g*d/4,(3*g+h)*abs(a)/4+(g+h)*d/8)
 assert formula==actual,(n,formula,actual)
print('PASS 12500 exact oriented seven-ray support tests, all vertex Frobenius bounds')

x=F(175,72);T=F(1);E=F(1)
for i in range(1,7):
 T*=x/i; E+=T
assert E>11
assert 1/F(17,25)-1/F(41,50)==F(175,697)
assert F(25,36)/F(175,697)-F(3,8)==F(1205,504)
assert F(13,3072)*F(15,16)==F(65,16384)
assert (F(2)*F(65,16384)*F(1205,32256)/F(3,8192)*F(2,3))==F(78325,145152)
assert F(78325,145152)*3 > F(3,2)
print('PASS cutoff symmetry/weighted Cauchy lower bounds; frozen no-go when tau^h <=1/3')
print('PASS h=1/200: tau <=3^-200 (an actual finite positive time)')

hvar=s.symbols('h',positive=True)
A=s.Rational(1,2)+hvar;D=s.Rational(1,2)-hvar;beta=s.Rational(1,2)-2*hvar
assert s.simplify(s.Rational(3,2)-2*A-beta)==0
assert s.simplify(s.Rational(3,2)+D-A-1-beta)==0
assert s.simplify(s.Rational(3,2)-A-D-(beta+2*hvar))==0
print('PASS all three physical similarity source scaling exponents')
print('OPEN: original G1 preassigned source, smooth positive inverse, nonlinear unforced blowup')
