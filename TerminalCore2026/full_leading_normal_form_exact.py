"""Exact audit of the complete 27-term source-native leading-pressure
normal form, source eqs. (18),(24),(26)-(28), Zenodo 23474915.
This is not a full Lean Banach-space certificate or a proof of the
complete Navier--Stokes lower-order recurrence.
"""
from fractions import Fraction as F
import sympy as s
r,m,A,E,Q=s.symbols("r m A E Q")
z=s.symbols("z")
u,v,K,B,G=[s.Function(t)(z) for t in ("u","v","K","B","G")]
H=[
 [(m*A,v*B),(A,u*G*s.diff(B,z)),(E*A,u*B**2),(r,K)],
 [(-m,v*G),(A,u*G*B),(-1,u*G*s.diff(G,z)),(-E,u*B*G)],
 [(-1,u*G**2)],[]
]
terms=[]; signatures=[]
for j in range(4):
    ar=[]
    for p,g in H[j]:
        ar.extend(((p*Q,B*g),(p,G*s.diff(g,z))))
    if j:
        ar.extend((p,G*g) for p,g in H[j-1])
    terms.append(ar); signatures.append([])
    for p,g in ar:
        poly=s.Poly(p,r,m,A,E,Q)
        assert len(poly.terms())==1
        powers,coef=poly.terms()[0]
        assert sum(powers)<=3-j
        signatures[-1].append((tuple(powers),int(coef)))
assert list(map(len,terms))==[8,12,6,1]
w0=B*A/r; w1=-G/r
hs=[
 v*w0+u*(G*s.diff(w0,z)+B*E*w0)/m+K/m,
 v*w1+u*(G*(w0+s.diff(w1,z))+B*E*w1)/m,
 u*G*w1/m, s.Integer(0)]
for j,ar in enumerate(terms):
    expected=(G*s.diff(hs[j],z)+B*Q*hs[j]+(G*hs[j-1] if j else 0))*r*m
    actual=sum((p*g for p,g in ar),s.Integer(0))
    assert s.expand(expected-actual).doit().simplify()==0
print("PASS: all 27 symbolic normal-form identities")
checked=0
for hh in (F(1,200),F(1,1000)):
    for k in range(1,13):
        for a in range(k,k+10):
            for c in (0,1,2,5,20,100,1000):
                rr=a+1;mm=a+c+1;tt=mm+k+1
                alpha=rr-(F(1,2)-hh)-2*hh*k
                epsilon=2*hh*k-rr
                theta=2*hh*k-1-mm
                assert 0<=alpha<=tt and -tt<=epsilon<=0 and -tt<=theta<=0
                vals=(rr,mm,alpha,epsilon,theta)
                for j,ar in enumerate(signatures):
                    for powers,coef in ar:
                        val=F(coef)
                        for x,degree in zip(vals,powers):val*=x**degree
                        assert abs(val)<=tt**(3-j),(a,k,c,j,val)
                        checked+=1
assert checked==45360
print("PASS exact index/shift polynomial majorants:",checked)
