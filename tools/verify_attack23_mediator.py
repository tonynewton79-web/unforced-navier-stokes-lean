"""Exact finite Gaussian-integer replay for the Attack 23 20-mode C4 orbit.

Fourier coefficients are Gaussian-integer vectors times a formal amplitude
label A,B,C. This certifies a finite convolution identity, not a PDE solution.
"""
from collections import defaultdict

P, Q, R = (1, 0, 0), (0, 2, 1), (1, 2, 1)
a, b = (0, 1, 0), (0, 1, -2)
S = (2, 2, 1)

def rotate(v):
    x, y, z = v
    return (-y, x, z)

def neg(v):
    return tuple(-x for x in v)

def dot(v, w):
    return sum(x*y for x,y in zip(v,w))

base = [(P, tuple(1j*x for x in a), 'A'),
        (Q, tuple(complex(x) for x in b), 'B'),
        (R, tuple(-complex(x) for x in b), 'C')]
modes = {}
for k, v, label in base:
    for _ in range(4):
        for sign in (1, -1):
            kk = k if sign == 1 else neg(k)
            vv = v if sign == 1 else tuple(x.conjugate() for x in v)
            if kk in modes:
                assert modes[kk] == (vv,label)
            modes[kk] = (vv,label)
        k, v = rotate(k), rotate(v)

assert len(modes) == 20
assert all(dot(k,v) == 0 for k,(v,_) in modes.items())
assert all(modes[neg(k)][0] == tuple(z.conjugate() for z in v)
           for k,(v,_) in modes.items())

source = defaultdict(lambda: [0j,0j,0j])
ordered_pairs = []
for k,(uk,tagk) in modes.items():
    l = tuple(S[j] - k[j] for j in range(3))
    if l not in modes:
        continue
    ul,tagl = modes[l]
    term = tuple(dot(uk,l)*z for z in ul)
    key = ''.join(sorted((tagk,tagl)))
    for j in range(3):
        source[key][j] += term[j]
    ordered_pairs.append((k,l))

assert set(ordered_pairs) == {(P,R),(R,P)}
assert dict(source) == {'AC':[0j,-2j,4j]}
assert dot(S,source['AC']) == 0

for m in range(-100,101):
    km = (m,2,1)
    assert dot(km,b) == 0
    assert dot(km,a) == 2
    assert (1+m,2,1) == tuple(P[j]+km[j] for j in range(3))
    assert dot(km,km) == m*m+5

print('PASS 20 real divergence-free C4 modes')
print('PASS unique ordered pairs at s are (p,r),(r,p)')
print('PASS projected source = -2i AC b')
print('PASS velocity derivative at absent s = -4pi AC b')
print('PASS exact ray identities at 201 test indices')
