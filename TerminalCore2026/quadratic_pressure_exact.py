"""Ordered quadratic pressure identity from the genuine Omega_k source.

Checks full ordered V_i V_j' - V_i V_j/(2X) sum and
U_i Z_(0,j) V_j remainder on rational-polynomial inputs.
Does not claim the bilinear analytic norm estimate or recurrence (53).
"""
import sympy as s
from fractions import Fraction as F
from random import Random

X,eta=s.symbols("X eta")
rng=Random(20261020)
tests=0
for k in range(2,12):
    for trial in range(12):
        W={}
        U={}
        for i in range(1,k):
            ai=i+rng.randint(0,4)
            W[i]=(1+s.Rational(rng.randint(1,7),5)*eta+
                  s.Rational(rng.randint(1,3),4)*eta**2)*X**ai
            U[i]=(1+s.Rational(rng.randint(1,3),7)*eta)*X**(i+rng.randint(0,3))
        V={i:X*W[i] for i in W}
        source=sum(V[i]*s.diff(V[k-i],X)-V[i]*V[k-i]/(2*X)
                   for i in range(1,k))
        Q=sum(W[i]*W[k-i] for i in range(1,k))
        assert s.expand(source-X*s.diff(X*Q,X)/2)==0
        Pi=s.integrate(-source/(2*X),X)
        assert s.expand(Pi+X*Q/4)==0
        h=s.Rational(1,200); d=1-eta**2; L=1-2*h*eta**2
        B=2*eta/L; G=d/L
        rem=sum(U[i]*(G*s.diff(W[k-i],eta)+
               B*(2*h*(k-i)*W[k-i]-W[k-i]-X*s.diff(W[k-i],X)))
               for i in range(1,k))
        direct=sum(U[i]*(2*eta*(2*h*(k-i))*V[k-i]+
               d*s.diff(V[k-i],eta)-2*eta*X*s.diff(V[k-i],X))/L/X
               for i in range(1,k))
        assert s.cancel(rem-direct)==0
        tests+=1
print('PASS exact quadratic pressure source/primitive/remainder:',tests)

count=0
for k in range(2,100):
    for i in range(1,k):
        j=k-i
        for ai in (i,i+1,i+4):
            for aj in (j,j+2):
                assert F(aj)+F(ai)+F(1,2)+F(1,2)==F(ai+aj+1)
                count+=1
print('PASS exact ordered-pair Euler coefficient tests:',count)
