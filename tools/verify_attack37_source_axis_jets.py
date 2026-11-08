#!/usr/bin/env python3
"""Finite exact source-axis checks; a full G1 convergence proof is not claimed."""
import sympy as s
x=s.symbols('x')
h,j,P0,P2,f0,f1,f2,f3,f4=s.symbols('h j P0 P2 f0 f1 f2 f3 f4')
A=s.Rational(1,2)+h;D=s.Rational(1,2)-h;b=-A-s.Rational(1,2)
L=1-2*h*x*x;d=1-x*x
def trim(q):
 return s.Add(*[v*x**k[0] for k,v in s.Poly(s.expand(q),x).terms() if k[0]<=5])
inv=sum((2*h*x*x)**r for r in range(4))
def Z(a,p,F):return trim((2*(a-p)*x*F+d*s.diff(F,x))*inv)
def T(a,p,F):return trim(((p-a)*F+D*x*s.diff(F,x))*inv)
def ZZ(a,lam,p,F):return Z(a+lam-D,p,Z(a+lam,p,F))
def at(F):return s.factor(s.expand(F).coeff(x,0))
u=4*x+j; P=P0+P2*x*x/2
f=f0+f1*x+f2*x*x/2+f3*x**3/6+f4*x**4/24
v=-Z(-A,0,u)
u0=trim((T(-A,0,u)+u*Z(-A,0,u)+Z(-2*A,0,P))/2)
phi0=trim((T(b,0,f)+v*f+u*Z(b,0,f))/4)
phi1=trim(-ZZ(b,0,0,f)/4);u1=trim(-ZZ(-A,0,0,u)/2)
v0next=trim(-Z(-A,1,u0)/2)
pi1=trim(-(T(0,1,v)+v*v/2+u*Z(0,1,v)-4*v0next)/2)
v1=trim(-Z(-A+2*h,1,u1)/2)
pi2=trim(2*v1+ZZ(0,0,1,v)/2)
phi2=trim(-ZZ(b,2*h,1,phi1)/12)
u2=trim((-ZZ(-A,2*h,1,u1)+Z(-2*A+4*h,1,pi2))/8)
assert s.simplify(at(u0)-(A+4)*j/2)==0
assert s.simplify(at(phi0)-((h-3)*f0+j*f1)/4)==0
assert s.simplify(at(u1)-A*j)==0
assert s.simplify(at(phi1)-((1+h)*f0/2-f2/4))==0
assert s.simplify(at(pi1)-((1+2*h)*P0-P2/2-12))==0
assert s.simplify(at(pi2))==0
assert s.simplify(at(u2)-s.Rational(9,16)*(1-4*h*h)*j)==0
assert s.simplify(at(phi2)-(f4+(12*h-24)*f2+(24-12*h-36*h*h)*f0)/48)==0
print('PASS: eight exact source-native axis jets; G1 full startup is open')
