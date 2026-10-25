#!/usr/bin/env python3
"""Source heat-pressure sign and moment-Jacobian replay.
These checks do NOT authenticate a full corrected source or unforced PDE."""
from fractions import Fraction as F
from random import Random
import sympy as s
import mpmath as m
m.mp.dps=60

q=s.symbols('q')
assert s.expand((1-q)**2-1+q*(2-q))==0
x=s.symbols('x',positive=True)
e=[-s.Rational(49,32),-s.Rational(17,32),s.Rational(1,2)]
fs=[x**a for a in e]
W=s.det(s.Matrix([[s.diff(f,x,k) for f in fs] for k in range(3)]))
assert s.simplify(W/x**(sum(e)-3))!=0
M=s.Matrix([[s.Rational(1,2**(49*i)) for i in range(3)],
            [-s.Rational(1,2**(17*i)) for i in range(3)],
            [s.Integer(2)**(16*i) for i in range(3)]])
assert M.det()!=0
rand=Random(20261022)
for _ in range(10000):
    chi=F(rand.randrange(1,100),100)
    d=F(rand.randrange(1,100),100)
    r=chi*d
    assert -2*r+r*r<0
def H(Z,h):
    return m.quad(lambda v:m.exp(-v)*v**h*(1+Z*v)**(-h),
                  [0,1,m.inf])/m.gamma(1+h)
for h in [m.mpf('.01'),m.mpf('.04')]:
    for eta in [m.mpf('-.75'),m.mpf('0'),m.mpf('.5'),m.mpf('1')]:
        Z=2*(1-eta**2)/100
        v=H(Z,h)
        assert 0<v<=1+m.mpf('1e-49')
        assert 0<=1-v+m.mpf('1e-48')<=h*(1+h)*Z+m.mpf('1e-48')
        dq=((1+m.mpf('.7')*(v-1))**2-1)/2
        if abs(eta)<1:assert dq<0
        else:assert abs(dq)<m.mpf('1e-40')
assert abs(m.det(m.matrix([
 [v**(-m.mpf('1.51')) for v in [1,m.mpf('1.25'),m.mpf('1.5')]],
 [-v**(-m.mpf('.51')) for v in [1,m.mpf('1.25'),m.mpf('1.5')]],
 [m.sqrt(2*v) for v in [1,m.mpf('1.25'),m.mpf('1.5')]]
])))>m.mpf('1e-12')
print('PASS symbolic sign, exact generalized Vandermonde and Wronskian')
print('PASS 10,000 rational sign falsifier tests, 8 genuine heat-kernel evaluations')
print('PASS endpoint control and separated-node three-moment determinant')
print('SOURCE AUTHENTICATION / FULL UNFORCED THEOREM: HOLD')
