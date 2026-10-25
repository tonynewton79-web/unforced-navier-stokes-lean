#!/usr/bin/env python3
"""Exact symbolic + 5000 rational H8 ray-cone completion audit; NO unforced PDE proof."""
import random
from fractions import Fraction as F
import sympy as s

r,l,z=s.symbols("r l z",real=True)
sn,co=s.sin(z),s.cos(z)
t=s.Rational(1,4)
rays=[s.Matrix(a) for a in [(1,0,0),(1,t,0),(1,-t,0),
                             (1,0,t),(1,0,-t),(1,t,t),(1,t,-t)]]
a=s.Matrix([co,l*r*r*co,0]); b=s.Matrix([0,co,-l*r*sn]); d=s.Matrix([0,0,1])
Q=2*(a*a.T+b*b.T+d*d.T)
dd=s.Matrix([
  1,1+4*l*r*r*co*co,3-4*l*r*r*co*co,
  2+16*sn*sn+16*l*l*(r*r*sn*sn-r**4*co*co)+16*l*r*co*sn,
  2+16*sn*sn+16*l*l*(r*r*sn*sn-r**4*co*co)-16*l*r*co*sn,
  1-16*l*r*co*sn,1+16*l*r*co*sn])
pi=s.Rational(3,8)-2*co*co*(1+l*l*r**4)
K=s.Rational(85,8)+32*sn*sn+32*l*l*r*r*sn*sn-30*l*l*r**4*co*co
synth=sum((dd[j]*rays[j]*rays[j].T for j in range(7)),s.zeros(3,3))
assert all(s.trigsimp(s.expand(w))==0 for w in
           synth-(Q+K*s.diag(1,0,0)+pi*s.eye(3)))
mat=s.Matrix.hstack(*[s.Matrix([v[0]**2,v[1]**2,v[2]**2,
              v[0]*v[1],v[0]*v[2],v[1]*v[2]]) for v in rays])
assert mat.rank()==6 and mat.nullspace()[0]==s.Matrix([2,-2,0,-1,-1,1,1])
assert s.simplify(Q[0,0]-Q[1,1]+2*l*l*r**4*co*co)==0
assert s.simplify(s.diff(s.diff(K,r)+K/r,z)
      -(64/r+192*l*l*r+300*l*l*r**3)*sn*co)==0
assert s.Rational(5007,4096)>s.Rational(3,8)
assert s.Rational(39,64)>s.Rational(3,8)

rng=random.Random(20261024)
for _ in range(5000):
    rr=F(rng.randint(12,20),16)
    ll=F(rng.randint(-8,8),128)
    tt=F(rng.randint(-4,4),16)
    cc=(1-tt*tt)/(1+tt*tt)
    ss=2*tt/(1+tt*tt)
    x=[cc,ll*rr*rr*cc,F(0)]
    y=[F(0),cc,-ll*rr*ss]
    v=[F(0),F(0),F(1)]
    QQ=[[2*(x[i]*x[j]+y[i]*y[j]+v[i]*v[j]) for j in range(3)]
        for i in range(3)]
    pp=F(3,8)-2*cc*cc*(1+ll*ll*rr**4)
    kk=F(85,8)+32*ss*ss+32*ll*ll*rr*rr*ss*ss-30*ll*ll*rr**4*cc*cc
    common=2+16*ss*ss+16*ll*ll*(rr*rr*ss*ss-rr**4*cc*cc)
    D=[F(1),1+4*ll*rr*rr*cc*cc,3-4*ll*rr*rr*cc*cc,
       common+16*ll*rr*cc*ss,common-16*ll*rr*cc*ss,
       1-16*ll*rr*cc*ss,1+16*ll*rr*cc*ss]
    assert min(D)>=F(3,8) and kk>0
    vectors=[[F(v[i]) for i in range(3)] for v in rays]
    synth_rat=[[sum((D[k]*vectors[k][i]*vectors[k][j] for k in range(7)),
                    F(0)) for j in range(3)] for i in range(3)]
    target=[[QQ[i][j]+(kk if i==j==0 else 0)+(pp if i==j else 0)
             for j in range(3)] for i in range(3)]
    assert synth_rat==target
    assert QQ[0][0]-QQ[1][1]<=0

print("PASS symbolic six-component tensor equality, rank six and exact kernel")
print("PASS 5000/5000 independent Fraction tensor and cone-floor replay")
print("PASS direct-cone negative control and non-gradient carrier curl")
print("HOLD source-matched H8 stress, zero-force PDE, and complete Lean theorem")
