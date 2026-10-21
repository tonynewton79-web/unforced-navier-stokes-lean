"""Exact A.11 endpoint perturbation scalar audit.

This checks conditional bounds and their algebra. It does not
authenticate any Appendix-A source numerical endpoint values.
"""
from fractions import Fraction as F
import sympy as s
for lam in (F(1,20),F(1,24),F(1,100),F(1,10**6)):
    delta=40960*lam**28
    eps=2560*lam**28/(1-delta)
    ell=38400000*lam**28/(1-delta)
    mix=2400000*lam**28/(1-delta)**2
    kappa=((1+delta)/(1-delta))**2
    assert delta<F(1,10**31) and kappa<=1+8*delta
    assert ell<lam/2 and eps<5120*lam**28
    assert mix<5000000*lam**28
c,cp,b,db=s.symbols('c cp b db')
assert s.expand(cp*db*(1+c*b)-c*db*cp*b-cp*db)==0
y,lam,D0,P0=s.symbols('y lam D0 P0',positive=True)
D=1/(4*lam)+(D0-1/(4*lam))*s.exp(2*lam*y)
P=1/(2*(1+2*lam))+(P0-1/(2*(1+2*lam)))*s.exp((1+2*lam)*y)
assert s.simplify(s.diff(D,y)-(2*lam*D-s.Rational(1,2)))==0
assert s.simplify(s.diff(P,y)-((1+2*lam)*P-s.Rational(1,2)))==0
print('PASS all rational A.11 bump and endpoint identities')
print('CONDITIONAL_ARITHMETIC_ONLY__NO_ACTUAL_SOURCE_ENDPOINT_CERTIFICATE')
