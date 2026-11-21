#!/usr/bin/env python3
"""Symbolic negative control for PDE similarity transport.
This does not prove existence of a full 3D solenoidal Navier-Stokes profile
or verify the unreleased external numerical interval certificate.
"""
import sympy as S
s,r,t=S.symbols('s r t',positive=True,real=True)
A=S.Function('A')(s,r)
W=A/r
linear=S.diff(W,s)+W/2+r*S.diff(W,r)/2
assert S.simplify(linear-(S.diff(A,s)+r*S.diff(A,r)/2)/r)==0
w=S.sin(s-2*S.log(r))/r
assert S.simplify(S.diff(w,s)+w/2+r*S.diff(w,r)/2)==0
assert S.simplify(w.subs(s,s+2*S.pi)-w)==0
b=S.Function('b')(s)
w2=b/r**2
assert S.simplify(S.diff(w2,s)+w2/2+r*S.diff(w2,r)/2-(S.diff(b,s)-b/2)/r**2)==0
U=S.Function('U')(s,r)
Q=S.exp(t/2)*r*U.subs({s:s+t,r:r*S.exp(t/2)},simultaneous=True)
identity=S.diff(Q,t)-r*S.exp(t/2)*(S.diff(U,s)+U/2+r*S.diff(U,r)/2).subs({s:s+t,r:r*S.exp(t/2)},simultaneous=True)
assert S.simplify(identity)==0
print('PASS: exact radial characteristic chain rule and log-periodic negative control')
print('HOLD: genuine 3D nonzero PDE profile, external interval certificate, Lean PDE theorem')
