#!/usr/bin/env python3
"""Attack44 exact rational source smooth-restore integral regression.
NEVER substitute diagnostic values for the original Gi or inner moment traces.
"""
from fractions import Fraction as Q
import sympy as s

DEN=2**40
def outward(x):
    return Q(x.numerator*DEN//x.denominator,DEN),Q(-((-x.numerator*DEN)//x.denominator),DEN)
def eb_pos(x):
    assert x>=0
    if x==0:return Q(1),Q(1)
    m=max(1,int(2*x)+1);z=x/m;term=sm=Q(1)
    for k in range(1,19):term*=z/k;sm+=term
    err=term*z/19/(1-z/20)
    return sm**m,(sm+err)**m
def eb(x):
    a,b=eb_pos(abs(x))
    if x<0:a,b=1/b,1/a
    return outward(a)[0],outward(b)[1]
def step(x):
    if x==0:return Q(0),Q(0)
    if x==1:return Q(1),Q(1)
    if x>Q(1,2):
        a,b=step(1-x);return 1-b,1-a
    z=1/x**2-1/(1-x)**2
    if z>=40:return Q(0),Q(1,2**40)
    a,b=eb(z)
    return outward(1/(1+b))[0],outward(1/(1+a))[1]
N=8192
steps=[step(Q(i,N)) for i in range(N+1)]
vals=[]
for p,power in [(Q(1),1),(Q(1),2),(Q(8,5),1)]:
    lo=hi=Q(0)
    for i in range(N):
        t=Q(i,N);T=Q(i+1,N)
        a,_=eb(p*t);_,b=eb(p*T)
        lo+=a*(1-steps[i+1][1])**power/N
        hi+=b*(1-steps[i][0])**power/N
    vals.append((lo,hi))
thresholds=[(Q(650848,10**6),Q(651130,10**6)),(Q(602312,10**6),Q(602583,10**6)),(Q(770655,10**6),Q(771080,10**6))]
assert all(a<lo<hi<b for (lo,hi),(a,b) in zip(vals,thresholds))
derived=[]
for i,(a,b) in enumerate(thresholds):
    el,eu=eb(Q(-8) if i<2 else Q(-64,5))
    base=Q(1) if i<2 else Q(5,8)
    derived.append((el*(base+a),eu*(base+b)))
for (a,b),(lo,hi) in zip(derived,[(Q(55379,10**8),Q(55390,10**8)),(Q(53751,10**8),Q(53761,10**8)),(Q(3853,10**9),Q(3855,10**9))]):
    assert lo<a<b<hi
eta,g,alpha,E0,dE=s.symbols("eta g alpha E0 dE")
U0=4*eta
U=U0+g*alpha
E=E0+dE
assert s.expand((U*E-U0*E0)-4*eta*(E-E0)-g*alpha*(E0+dE))==0
assert s.expand((U**2-E**2/2)-(U0**2-E0**2/2)-8*eta*(U-U0)-(g*alpha)**2+E0*dE+dE**2/2)==0
assert eb(Q(8))[1]<3000
assert Q(9000,3000)*Q(3,7)*Q(87,50)>2
print("PASS exact 8192-cell rational restore-integral certificates, five-row cancellation and conditional cone scale")
print("NO actual Gi, five source traces, correction solution or corrected cone certified")
