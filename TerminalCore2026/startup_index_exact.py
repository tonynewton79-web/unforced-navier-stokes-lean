"""All-index ordered-pair startup and physical Jacobian audit.

No certificate of existence, imported leading profile or full PDE.
"""
from fractions import Fraction
count=0
for n in range(1,2001):
    pairs={(i,n-i) for i in range(n+1)}
    current={(0,n),(n,0)}
    lower={(i,n-i) for i in range(1,n)}
    assert pairs==current|lower and not current&lower
    if n==1:assert lower==set()
    if n==2:assert lower=={(1,1)}
    assert all(i>0 and j>0 for i,j in lower)
    assert n-1<n
    assert (n-2<n if n>=2 else True)
    count+=len(pairs)
    omega_pairs={(i,n-1-i) for i in range(n)}
    assert all(i<n and j<n for i,j in omega_pairs)
print('PASS',count,'exact ordered source-pair partitions through n=2000')

for den in (101,200,500,1000):
    h=Fraction(1,den);D=Fraction(1,2)-h
    for eta in (Fraction(-1),Fraction(-1,3),Fraction(0),
                Fraction(2,5),Fraction(1)):
        L=1-2*h*eta**2
        assert L>0
        assert L-2*D*eta**2==1-eta**2
        assert 1-2*D==2*h
print('PASS 20 exact similarity Jacobian/shift sample triples')
print('Scope: combinatorial algebra and rational geometry ONLY')
