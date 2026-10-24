"""Exact source-independent co-rotating m=+/-1 covariance rank audit."""
from random import Random
from fractions import Fraction as F
import sympy as s
a=s.Matrix(s.symbols("a1 a2 a3", real=True))
b=s.Matrix(s.symbols("b1 b2 b3", real=True))
q=2*(a*a.T+b*b.T)
assert s.factor(q.det())==0
assert s.simplify(q*a.cross(b))==s.zeros(3,1)
x=s.eye(3)
a1=x[:,0]; b1=x[:,1]; a2=x[:,2]
two=2*(a1*a1.T+b1*b1.T+a2*a2.T)
assert two==2*s.eye(3) and two.det()==8
rng=Random(20261024)
for _ in range(5000):
    aa=[F(rng.randint(-8,8),rng.randint(1,8)) for j in range(3)]
    bb=[F(rng.randint(-8,8),rng.randint(1,8)) for j in range(3)]
    t=s.Matrix([[2*(aa[j]*aa[k]+bb[j]*bb[k]) for k in range(3)] for j in range(3)])
    assert t.det()==0
print("PASS: symbolic determinant/kernel and 5000 rational single-pair witnesses")
print("PASS: two-frequency polarisation fixture Q=2I with determinant 8")
print("No source-matched H8 cone or unforced PDE solution implied.")
