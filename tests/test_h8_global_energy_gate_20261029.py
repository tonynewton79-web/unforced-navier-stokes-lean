"""Supporting algebraic regressions for H8 Appendix R, not an NS proof."""
import sympy as s
from mpmath import besseljzero

def test_terminal_dyad_energy_ratio():
    p,R,M,t=s.symbols("p R M t",positive=True)
    z=s.symbols("z",positive=True)
    lhs=M*t**p*(1-2**(-p))
    rhs=2*R*M*s.integrate(z**(p-1),(z,t/2,t))
    assert s.simplify(rhs/lhs-2*R/p)==0

def test_similarity_exponents_and_L2_gate():
    h=s.symbols("h",positive=True)
    A=s.Rational(1,2)+h
    D=s.Rational(1,2)-h
    p=s.Rational(1,2)-3*h
    assert s.simplify(A+p-2*D)==0
    assert s.simplify(-A+(1+D)/2-p/2)==0
    assert s.simplify(2*A+p-1-D)==0

def test_prototype_strict_spectral_gap():
    j01=float(besseljzero(0,1))
    assert j01>2
    assert s.Rational(3,8)*j01**2>2
    assert s.Rational(3,8)*j01**2>s.Rational(1,10)

def test_amplitude_sign_equivalence():
    p,R=s.symbols("p R",positive=True)
    c0=R-p/2
    assert s.solve(s.Eq(c0,0),R)==[p/2]
    assert s.simplify((2*R/p)-1-2*c0/p)==0

def test_appendix_Q_prototype_integrals():
    import math
    c0=27.0163023544
    g0=0.0477816887268
    D=0.4
    assert abs(c0*math.log(2)-18.726273806107372)<1e-11
    assert abs(g0*(1-2**(-D))/D-0.02892485034318264)<1e-12
