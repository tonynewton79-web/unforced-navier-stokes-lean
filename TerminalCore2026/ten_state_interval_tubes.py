"""Conditional exact-rational interval ODE tubes for Appendix-A normalized moments.

All source coefficient ranges MUST be independently validated; a passing
fixture is not a source-admissible profile or a Navier--Stokes theorem.
Full reproducible version and negative controls are in the research ZIP.
"""
from fractions import Fraction as F

class I:
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        if self.lo>self.hi:raise ValueError("reversed interval")
    def __add__(self,x):
        x=iv(x);return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,x):return self+-iv(x)
    def __rsub__(self,x):return iv(x)+-self
    def __mul__(self,x):
        x=iv(x);v=[a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __pow__(self,k):
        if k!=2:raise ValueError("only square supported")
        if self.lo<=0<=self.hi:return I(0,max(self.lo**2,self.hi**2))
        return I(min(self.lo**2,self.hi**2),max(self.lo**2,self.hi**2))
    def mag(self):return max(abs(self.lo),abs(self.hi))
    def contains(self,x):return self.lo<=F(x)<=self.hi
    def meet(self,x):
        x=iv(x);u=max(self.lo,x.lo);v=min(self.hi,x.hi)
        if u>v:raise ArithmeticError("inconsistent interval source")
        return I(u,v)
    def hull(self,x):
        x=iv(x);return I(min(self.lo,x.lo),max(self.hi,x.hi))
    def aslist(self):return [str(self.lo),str(self.hi)]
def iv(x):
    if isinstance(x,I):return x
    if isinstance(x,(list,tuple)) and len(x)==2:return I(*x)
    return I(x)
def affine(bds,reverse=False):
    a,ae,l,le=[iv(bds[k]) for k in ("a","a_eta","ell","ell_eta")]
    if reverse:
        c=2*l-1
        return [[c,I(0)],[2*le,c]],[-iv(F(1,2)),I(0)]
    n=8;A=[[I(0) for _ in range(n)] for _ in range(n)]
    c=[l+F(1,2),l+1,2*l+F(1,2),2*l]
    for k in range(4):A[k][k]=-c[k];A[k+4][k+4]=-c[k]
    A[4][0]=-le;A[5][1]=-le;A[6][2]=-2*le;A[7][3]=-2*le
    return A,[a,I(1),a,a**2-F(1,2),ae,I(0),ae,2*a*ae]
def multiply(A,z,b):
    return [sum((x*y for x,y in zip(row,z)),I(0))+v for row,v in zip(A,b)]
def tube(initial,source,length,reverse=False,iterations=6):
    d=F(length)
    if d<=0:raise ValueError("nonpositive stage length")
    z0=[iv(x) for x in initial];A,b=affine(source,reverse)
    if len(z0)!=len(b):raise ValueError("wrong state dimension")
    L=max(sum(v.mag() for v in row) for row in A)
    B=max(x.mag() for x in b);M=max(x.mag() for x in z0)
    if d*L>=1:raise ValueError("d*L>=1: source stage must be subdivided")
    S=(M+d*B)/(1-d*L)
    box=[I(-S,S) for _ in z0]
    for _ in range(iterations):
        f=multiply(A,box,b)
        box=[u.meet(z.hull(z+I(0,d)*v)) for u,z,v in zip(box,z0,f)]
    end=[z+d*v for z,v in zip(z0,multiply(A,box,b))]
    return {"tube":[v.aslist() for v in box],
            "endpoint":[v.aslist() for v in end],
            "L":str(L),"S":str(S),
            "source_certified_by_script":False}
if __name__=="__main__":
    P=F(10**9);eub=F(1000,999)
    src={"a":"0","a_eta":["4/1000000000",str(4*eub/P)],
         "ell":"3/5","ell_eta":"0"}
    z0=[0,F(5,8),0,-F(5,12),[str(4/P),str(4*eub/P)],
        0,[str(F(5,2)/P),str(F(5,2)*eub/P)],0]
    f=tube(z0,src,"1/100")
    target=[0,F(5,8),0,-F(5,12),4/P,0,F(5,2)/P,0]
    assert all(iv(r).contains(t) for r,t in zip(f["endpoint"],target))
    h=F(1,1000);p=-1/(2*(1+2*h))
    g=tube([str(p),"0"],
           {"a":"0","a_eta":"0","ell":str(-h),"ell_eta":"0"},
           "1/100",reverse=True)
    assert iv(g["endpoint"][0]).contains(p) and iv(g["endpoint"][1]).contains(0)
    try:tube([0]*8,src,"1")
    except ValueError:pass
    else:raise AssertionError("unsafe step not rejected")
    print("PASS two exact source-native reference/tail controls and unsafe-step rejection")
    print("SOURCE PROFILE, FULL PULSE COVER, STRESS RATIO AND THEOREM 1.1 UNVERIFIED")
