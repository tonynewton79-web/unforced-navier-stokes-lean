"""Exact Fraction A.5 fixed-pulse enclosures; never a full physical cone/PDE certificate."""
from fractions import Fraction as F
from functools import lru_cache
import json
def q(x):
    if isinstance(x,float):raise TypeError("float endpoint forbidden")
    return F(str(x))
class I:
    def __init__(self,a,b=None):
        self.a=q(a);self.b=q(a if b is None else b)
        if self.a>self.b:raise ValueError("reversed interval")
    def __add__(self,x):
        x=iv(x);return I(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,x):return self+-iv(x)
    def __mul__(self,x):
        x=iv(x);p=[u*v for u in (self.a,self.b) for v in (x.a,x.b)]
        return I(min(p),max(p))
    __rmul__=__mul__
    def data(self):return [str(self.a),str(self.b)]
    def widen(self,e):return I(self.a-e,self.b+e)
def iv(x):return x if isinstance(x,I) else I(x)
@lru_cache(None)
def exp_plus(x):
    x=q(x);assert 0<=x<=80
    n=110+2*(x.numerator//x.denominator);t=F(1);p=t
    for k in range(1,n+1):t*=x/k;p+=t
    next_t=t*x/(n+1);r=x/(n+2)
    assert r<1
    return I(p,p+next_t/(1-r))
@lru_cache(None)
def sigma(t):
    t=q(t)
    if t<=0:return I(0)
    if t>=1:return I(1)
    z=1/t**2-1/(1-t)**2
    if z>=80:return I(0,F(1,1+2**80))
    if z<=-80:return I(1-F(1,1+2**80),1)
    e=exp_plus(abs(z))
    return I(1/(1+e.b),1/(1+e.a)) if z>=0 else I(1-1/(1+e.a),1-1/(1+e.b))
def sig_range(a,b):return I(sigma(a).a,sigma(b).b)
def sig_prime(a,b):
    if b<=0 or a>=1:return I(0)
    if a<=0 or b>=1:return I(0,64)
    s=sig_range(a,b)
    return I(0,min(F(64),min(F(1,4),s.b*(1-s.a))*(2/a**3+2/(1-b)**3)))
@lru_cache(None)
def phi(x):
    x=q(x)
    if x<=0:return I(0)
    if x>=F(1,50):return I(x-F(1,100))
    h=x/16
    return I(h*sum((sigma(50*k*h).a for k in range(16)),F()),
             h*sum((sigma(50*(k+1)*h).b for k in range(16)),F()))
def one(a,b):
    a=q(a);b=q(b)
    p=I(phi(a).a,phi(b).b);t=sig_range(50*a,50*b)
    cutoff=I(1)-sig_range(a-10,b-10)
    deriv=t*cutoff-p*sig_prime(a-10,b-10)
    e=F(1,2**120)
    return dict(xi=[str(a),str(b)],R0=(p*cutoff).widen(e).data(),
      R0_xi=deriv.widen(e).data(),R0_eta=I(0).widen(e).data(),
      R0_xi_eta=I(0).widen(e).data(),phi=p.widen(e).data(),
      sigma_cut=cutoff.widen(e).data(),guard=str(e))
def generate():
    x=[F(0),F(1,50),F(1),F(10)]+[F(10)+F(k,16) for k in range(1,17)]+[F(13)]
    y=[F(-1),F(0),F(1)]
    return {"type":"SOURCE_DERIVED_FIXED_PULSE_ONLY",
      "formula":"R0=phi_b*(1-sigma(xi-10)), phi_b=int_0^xi sigma(50v)dv, A.5 smooth step",
      "cells":[dict(one(a,b),eta_range=[str(c),str(d)])
        for a,b in zip(x,x[1:]) for c,d in zip(y,y[1:])],
      "Qs_Ns_cone_certified":False,"unforced_theorem_proved":False}
if __name__=="__main__":
    o=generate()
    with open("SOURCE_FIXED_PULSE_EXACT_INTERVALS.json","w") as f:json.dump(o,f,indent=2)
    print("SOURCE fixed-pulse cell count",len(o["cells"]))
