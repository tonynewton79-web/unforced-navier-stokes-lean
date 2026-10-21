"""Exact-rational A.11 authentic correction-root/eta-jet gates.

Uses the source A.10 interpolation derivative and two-bump matrix
bounds as proved analytic inputs. NO claim of actual terminal S/Pi
gauges or fully authenticated interval data.
"""
from fractions import Fraction as F
import sympy as s
L=F(1,100);powmax=L**28
assert F(20,17)*21*L < F(1,4)
assert 3*21*L < F(63,100)+F(1,10**30)
assert 1920*powmax<F(1,100)
assert F(3,2)*F(63,100)+1920*powmax<2
assert F(3,2)*F(1,4)/(1-1920*powmax)<1
assert F(640,3)*2*powmax<F(1,10**4)
u,v,w,x,z,k,t=s.symbols("u v w x z k t",real=True)
c1=k-x*t
poly=s.expand(2*v*(c1+z*t)+w*(c1**2+z*t**2))
A=w*(x*x+z);B=2*v*(z-x)-2*w*x*k;C=2*v*k+w*k*k
assert s.expand(poly-(A*t*t+B*t+C))==0
assert s.simplify(s.diff(poly,t)-(2*v*(z-x)+2*w*(-x*(k-x*t)+z*t)))==0
print("PASS source A11 root coefficients, differentiated row and exact")
print("rational λ<=1/100 contraction/η-derivative margin.")
print("CONDITIONAL ON true A10 interpolation and initial η-independent moment ratio.")
print("NOT CERTIFIED: terminal S∞/Pi∞; full A11 integral cells; unforced NS.")
