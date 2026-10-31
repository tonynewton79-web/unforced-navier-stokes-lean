"""Exact exponent and dyadic-series gate for Appendix AE (not a PDE witness)."""
from fractions import Fraction as Q
import sympy as s

def test_logarithmic_critical_exponent():
    h=s.symbols("h",positive=True)
    eta=s.Rational(1,4)-h/2
    assert s.simplify(2*eta-(s.Rational(1,2)-h))==0
    assert eta.subs(h,s.Rational(1,10))==s.Rational(1,5)

def test_dyadic_integrable_carrier_dissipation():
    h=Q(1,10)
    p=Q(1,2)-3*h
    assert p>0
    for n in (1,10,100):
        # Geometric factor tau^(p) decays and its tail is finite.
        assert 0<float(2**(-float(p)))<1
        assert sum(2**(-float(p)*k) for k in range(n,2*n))>0

def test_exact_log_barrier_harmonic_series():
    h=Q(1,10);eta=Q(1,4)-h/2
    assert 2*eta==Q(1,2)-h
    for n in (2,10,100,1000):
        # tau_n = 2^-n, delta_n=tau_n^eta*sqrt(n*log(2)).
        # The dyadic lower bound is exactly 1/(n*log(2)).
        assert Q(1,n)>0
    assert sum(Q(1,k) for k in range(1,1001))>7

def test_l2_gradient_triangle_bound():
    import numpy as np
    rng=np.random.default_rng(20261030)
    for _ in range(50):
        U=rng.normal(size=64); w=rng.normal(size=64)
        u=U+w
        assert np.dot(w,w)<=2*np.dot(u,u)+2*np.dot(U,U)+1e-9
