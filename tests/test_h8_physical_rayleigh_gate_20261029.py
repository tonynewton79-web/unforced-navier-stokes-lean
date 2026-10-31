"""Appendix N: exact symbolic powers and conditional Dirichlet threshold.
The downloadable research release includes the full 7-test symbolic and
independent numerical quadrature module. No singular H8 PDE solution is asserted.
"""
import sympy as sp

def test_similarity_exponent_ledger():
    h=sp.symbols("h",positive=True)
    A=sp.Rational(1,2)+h
    D=sp.Rational(1,2)-h
    p=1+D-2*A
    assert sp.simplify(p-sp.Rational(1,2)+3*h)==0
    assert sp.simplify(1+D-2+A)==0
    assert sp.simplify(p/2-1+sp.Rational(3,4)+3*h/2)==0

def test_physical_jacobian_exact_chain():
    eta,h,tau=sp.symbols("eta h tau",positive=True)
    D=sp.Rational(1,2)-h
    d=1-eta**2
    L=1-2*h*eta**2
    z=tau**D*eta*d**(-D)
    dz=sp.diff(z,eta)
    assert sp.simplify((dz-tau**D*L*d**(-D-1)).rewrite(sp.exp))==0
    J=tau/d*dz
    assert sp.simplify((J-tau**(1+D)*L*d**(-D-2)).rewrite(sp.exp))==0

def test_projected_source_norm_scaling():
    h,p,tau,M0,kappa=sp.symbols("h p tau M0 kappa",positive=True)
    p=sp.Rational(1,2)-3*h
    bound=kappa*sp.sqrt(M0*tau**p)/tau
    expected=kappa*sp.sqrt(M0)*tau**(-sp.Rational(3,4)-3*h/2)
    assert sp.simplify(bound-expected)==0

def test_strict_support_criterion_implies_positive_rayleigh_margin():
    h=sp.Rational(1,100)
    p=sp.Rational(1,2)-3*h
    dstar=sp.Rational(3,4)
    # Lower rational bound j_{0,1}^2 > 5 is sufficient for this test.
    Xstar=sp.Rational(1,1)
    assert 5*dstar/(2*Xstar)-p/2>1
