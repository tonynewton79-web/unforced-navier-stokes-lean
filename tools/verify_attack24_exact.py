#!/usr/bin/env python3
"""Exact Gaussian-integer/Fraction replay of the 20-mode C4 interaction graph.

Source coefficients are polynomials in formal real A,B,C; all arithmetic
is performed over integers and fractions, without floating-point inputs.
No claim of PDE closure, sustained cascade, carrier smallness or blow-up.
"""
from dataclasses import dataclass
from collections import defaultdict, Counter
from fractions import Fraction

@dataclass(frozen=True)
class G:
    x: int = 0
    y: int = 0
    def __add__(self, other):
        if not isinstance(other,G): other=G(other)
        return G(self.x+other.x,self.y+other.y)
    __radd__=__add__
    def __neg__(self): return G(-self.x,-self.y)
    def __mul__(self,other):
        if not isinstance(other,G): other=G(other)
        return G(self.x*other.x-self.y*other.y,
                 self.x*other.y+self.y*other.x)
    __rmul__=__mul__
    def conj(self): return G(self.x,-self.y)
    def __bool__(self): return bool(self.x or self.y)

def rot(t): return (-t[1],t[0],t[2])
def neg(t): return tuple(-z for z in t)
def plus(t,u): return tuple(x+y for x,y in zip(t,u))
def gv(t): return tuple(G(z) for z in t)
def igv(t): return tuple(G(0,z) for z in t)
def conj(v): return tuple(z.conj() for z in v)
def mul(v,c): return tuple(c*z for z in v)
def dot(v,k): return sum((v[i]*k[i] for i in range(3)),G())
def herm(v,w): return sum((v[i]*w[i].conj() for i in range(3)),G())

def build(sign):
    p,q,r=(1,0,0),(0,2,1),(1,2,1)
    a,b=(0,1,0),(0,1,-2)
    modes={};members=defaultdict(set)
    for j in range(4):
        for k,v,label in [(p,igv(a),'A'),(q,gv(b),'B'),
                          (r,mul(gv(b),G(sign)),'C')]:
            for eps in (1,-1):
                kk=k if eps==1 else neg(k)
                vv=v if eps==1 else conj(v)
                if kk in modes: assert modes[kk]==(vv,label)
                modes[kk]=(vv,label)
                members[kk].add(j)
        p,q,r,a,b=map(rot,(p,q,r,a,b))
    assert len(modes)==20
    for k,(v,_) in modes.items():
        assert dot(v,k)==G()
        assert modes[neg(k)][0]==conj(v)
    return modes,members

def convolution(modes):
    B=defaultdict(lambda: defaultdict(lambda:[G(),G(),G()]))
    pairs=defaultdict(list)
    for p,(up,ap) in modes.items():
        for q,(uq,aq) in modes.items():
            k=plus(p,q)
            if k==(0,0,0):continue
            name=''.join(sorted(ap+aq))
            fac=dot(up,q)
            for i in range(3):B[k][name][i]=B[k][name][i]+fac*uq[i]
            pairs[k].append((p,q))
    return B,pairs

def nonzero(k,poly):
    n2=sum(t*t for t in k)
    for v in poly.values():
        d=dot(v,k)
        if any(G(n2)*v[i]+G(-k[i])*d for i in range(3)):
            return True
    return False

def poly_norm(K,B):
    P=defaultdict(Fraction);Im=defaultdict(Fraction)
    for k in K:
        n2=sum(t*t for t in k)
        for n,v in B[k].items():
            for m,w in B[k].items():
                value=G(n2)*herm(v,w) + G(-1)*dot(v,k)*dot(w,k).conj()
                key=''.join(sorted(n+m))
                P[key]+=Fraction(value.x,n2)
                Im[key]+=Fraction(value.y,n2)
    assert all(v==0 for v in Im.values())
    return {k:v for k,v in sorted(P.items()) if v}

def run(sign):
    modes,members=build(sign)
    B,pairs=convolution(modes)
    active={k for k in B if nonzero(k,B[k])}
    missing=active-set(modes)
    assert (len(B),len(active),len(missing))==(170,124,108)
    assert Counter(k[2] for k in missing)=={-2:20,-1:24,0:20,1:24,2:20}
    local={k for k in missing if any(members[p]&members[q]
                                    for p,q in pairs[k])}
    cross=missing-local
    assert len(local)==16 and len(cross)==92
    assert all(all(members[p]&members[q] for p,q in pairs[k]) for k in local)
    H={k for k in missing if sum(z*z for z in k)>6}
    L={k for k in missing if sum(z*z for z in k)<6}
    assert len(H)==72 and len(L)==28 and len(missing-H-L)==8
    total=poly_norm(missing,B)
    expected={
      'AABB':Fraction(176),'AACC':Fraction(8000,33),
      'BBBB':Fraction(1600,3),'BBCC':Fraction(1796592,1105),
      'CCCC':Fraction(25376,35)}
    assert total==expected,(total,expected)
    assert poly_norm(local,B)=={'AABB':Fraction(160),'AACC':Fraction(160)}
    assert poly_norm(cross,B)=={
      'AABB':Fraction(16),'AACC':Fraction(2720,33),
      'BBBB':Fraction(1600,3),'BBCC':Fraction(1796592,1105),
      'CCCC':Fraction(25376,35)}
    assert poly_norm(H,B)=={
      'AABB':Fraction(8),'AACC':Fraction(2256,11),
      'BBBB':Fraction(1600,3),'BBCC':Fraction(262432,221),
      'CCCC':Fraction(25376,35)}
    s=(2,2,1)
    assert B[s]['AC']==[G(),G(0,2*sign),G(0,-4*sign)]
    # At k*=(3,2,1), only p+(p+r) contributes at second order.
    # The first derivative at s=(2,2,1) is (-2*pi*i)*B_s.
    # After the second outer multiplier the exact acceleration is
    # 16*pi*pi*sign*A*A*C*b; this checks the rational vector factor.
    kstar=(3,2,1); p=(1,0,0)
    assert kstar not in B and kstar not in modes
    next_pairs={(ell,plus(kstar,neg(ell)))
                for ell in modes
                if plus(kstar,neg(ell)) in missing}
    assert next_pairs=={(p,s)}, next_pairs
    normalized=[G(0,2)*z for z in B[s]['AC']]
    assert normalized==[G(),G(-4*sign),G(8*sign)]
    assert dot(normalized,kstar)==G()
    assert sum(sum(z.x*z.x+z.y*z.y for z in v)
               for v,_ in modes.values())==84
    assert sum(sum(t*t for t in k)*sum(z.x*z.x+z.y*z.y for z in v)
               for k,(v,_) in modes.items())==444
    return total

if __name__=='__main__':
    negative=run(-1);positive=run(+1)
    assert negative==positive
    print('PASS: C4 20 -> 170 sums -> 124 active -> 108 new')
    print('PASS: 92 cross-only, 16 intra; 72 high, 8 equal, 28 low')
    print('PASS: exact rational leakage, cross-sector and high-shell quartics')
    print('PASS: sigma phase flip invariance and initial energy/dissipation')
    print('PASS: second-generation nonclosure at k=(3,2,1)')
