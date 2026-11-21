#!/usr/bin/env python3
"""Exact symbolic Attack56 nonlinear pressure identities. No existence or Lean claim."""
import sympy as S
x,y,z=S.symbols('x y z',real=True)
rr=S.symbols('r',positive=True)
V=S.Matrix([x,y,z])
H=1+V.dot(V)
B=S.Matrix([1,0,0]); C=S.Matrix([0,0,1])
modesS=[B.cross(V)/H,B.cross(V)/H**2]
modesP=[((2+V.dot(V))*C+(C.dot(V))*V)/H**S.Rational(3,2),
        ((2-V.dot(V))*C+3*(C.dot(V))*V)/H**S.Rational(5,2)]
g=[
  -10/(1+rr**2)**S.Rational(7,2),
  6*(2*rr**2-5)/(1+rr**2)**S.Rational(9,2),
  2*(2*rr**2-5)/(1+rr**2)**S.Rational(9,2),
  6*(4*rr**2-5)/(1+rr**2)**S.Rational(11,2)]
cs=[-S.Rational(2,3),-S.Rational(6,5),-S.Rational(2,5),-S.Rational(6,7)]
for k,(i,j) in enumerate([(0,0),(0,1),(1,0),(1,1)]):
    Ds=modesS[i].jacobian([x,y,z])
    Dp=modesP[j].jacobian([x,y,z])
    src=S.factor(2*S.trace(Ds*Dp))
    expected=g[k].subs(rr,S.sqrt(V.dot(V)))*B.cross(C).dot(V)
    assert S.simplify(src-expected)==0
    assert S.simplify(S.integrate(rr*g[k],(rr,0,S.oo))/3)==cs[k]
    print('PASS mixed nonlinear pressure',i,j,cs[k])
qcross=-S.Rational(2,3)*B.cross(C).dot(V)/H**S.Rational(3,2)
assert S.simplify(-sum(S.diff(qcross,t,2) for t in [x,y,z])
  -g[0].subs(rr,S.sqrt(V.dot(V)))*B.cross(C).dot(V))==0
for U in modesS+modesP:
    assert S.simplify(sum(S.diff(U[i],v) for i,v in enumerate([x,y,z])))==0
for i,U in enumerate(modesP):
    lap=S.Matrix([sum(S.diff(U[j],t,2) for t in [x,y,z]) for j in range(3)])
    assert lap.subs({x:0,y:0,z:0}) == (-10 if i==0 else -30)*C
print('PASS nonparallel exact Poisson pressure and all solenoidal centre terms')
print('HOLD genuine nonzero PDE profile, whole-domain inverse M, K, delta and Lean')
