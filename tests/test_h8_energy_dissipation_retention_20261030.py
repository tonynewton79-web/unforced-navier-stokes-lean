"""Appendix AD exact exponent checks, Hilbert estimates and Fourier audit."""
import sympy as s
import numpy as np
h=s.symbols('h',positive=True);p=s.Rational(1,2)-3*h
A=s.Rational(1,2)+h;eta=s.Rational(1,4)-h/2

def test_product_rule_scales():
    assert s.simplify((p-1)/2-s.Rational(1,2)-(p/2-1))==0

def test_integrated_correction_gradient_scale():
    assert s.simplify(p/2+A-(s.Rational(3,4)-h/2))==0

def test_dyadic_dissipation_power():
    assert s.simplify(p+2*A-1-(s.Rational(1,2)-h))==0

def test_excluded_retention_threshold():
    assert s.simplify(s.Rational(1,2)-h-2*eta)==0
    assert eta.subs(h,s.Rational(1,10))==s.Rational(1,5)

def test_threshold_is_stronger_than_regular_near_correction():
    for H in (s.Rational(1,100),s.Rational(1,10),s.Rational(3,20)):
        assert eta.subs(h,H)>H

def test_time_cauchy_schwarz():
    rng=np.random.default_rng(20261030)
    for _ in range(200):
        x=np.abs(rng.normal(size=250))
        assert np.mean(x*x)+1e-12>=np.mean(x)**2

def test_tensor_pressure_contraction():
    rng=np.random.default_rng(25)
    for _ in range(300):
        k=rng.integers(-7,8,size=3)
        if not k.any(): continue
        T=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
        m=np.einsum('i,j,ij->',k,k,T)/(k@k)
        assert abs(m)<=np.linalg.norm(T)+1e-10

def test_stress_polarization():
    U=s.Matrix(s.symbols('a b c',real=True));w=s.Matrix(s.symbols('d e f',real=True))
    S=U*w.T+w*U.T+w*w.T
    assert (S-(U+w)*(U+w).T+U*U.T).applyfunc(s.simplify)==s.zeros(3)

def test_dyadic_budget():
    for E in (1,4,12):
        c=s.Rational(1,5);n=int(E/c)+1
        assert n*c>E

def test_rate_substitution():
    t,C,d=s.symbols('t C d',positive=True)
    assert s.simplify(C*t**(s.Rational(1,2)-h)/(t**eta)**2-C)==0
