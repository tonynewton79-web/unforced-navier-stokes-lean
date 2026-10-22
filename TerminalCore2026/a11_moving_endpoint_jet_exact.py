#!/usr/bin/env python3
"""Synthetic exact-rational and symbolic checks for moving-endpoint A11 jets.
Not an authentic source-profile certificate and not a PDE proof.
"""
from fractions import Fraction as F
from random import Random
import sympy as s
c1,c2,u,v,w,x,z=s.symbols("c1 c2 u v w x z",real=True)
p=s.Matrix([u*(c1+x*c2),2*v*(c1+z*c2)+w*(c1*c1+z*c2*c2)])
j=p.jacobian([c1,c2])
assert s.simplify(j.det()-2*u*(z*(v+w*c2)-x*(v+w*c1)))==0
d=s.symbols("d",real=True)
jets=s.simplify(j.inv()*s.Matrix([d,0]))
assert s.simplify(jets[0]-z*(v+w*c2)*d/(u*(z*(v+w*c2)-x*(v+w*c1))))==0
assert s.simplify(jets[1]+(v+w*c1)*d/(u*(z*(v+w*c2)-x*(v+w*c1))))==0
alpha,L,D,Lp,Dp=s.symbols("alpha L D Lp Dp",real=True)
Delta=-s.exp(-alpha*L)*D
assert s.simplify(s.diff(Delta,L)*Lp+s.diff(Delta,D)*Dp+
             s.exp(-alpha*L)*(Dp-alpha*Lp*D))==0
assert F(20,17)-1 < F(20,19)
assert F(1,4)+F(20,19)*F(1,8)==F(29,76)
assert F(3)*F(21)*F(20,19)*F(1,4)==F(315,19)<17
assert F(2)*F(21)*F(29,76)*F(1,4)==F(609,152)<5
assert F(184320,20**28)<F(1,4)
r=Random(20261022)
for _ in range(10000):
    q=F(r.randrange(2501),10000)
    dd=F(r.randrange(10**7),10**7)
    cc=F(3,2)*dd/(1-q)
    assert cc<=2*dd
print("PASS: Jacobian, total moving-endpoint derivative, 10,000 exact synthetic scalar tests")
print("AUTHENTIC SOURCE: HOLD (M, V and other stage bounds not certified)")
