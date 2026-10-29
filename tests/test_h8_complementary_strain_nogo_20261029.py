"""Exact symbolic regressions for Appendix K; does not certify unforced blow-up."""
import sympy as s

def integrate_xz(expr):
    x,z=s.symbols("x z",real=True)
    return s.simplify(s.integrate(s.integrate(s.expand_trig(s.expand(expr)),(x,0,2*s.pi)),(z,0,2*s.pi)))

def test_exact_periodic_witness():
    x,z,K=s.symbols("x z K",real=True)
    psi=s.sin(x)*s.cos(z)+s.cos(x)*s.sin(2*z)
    vx=s.diff(psi,z);vz=-s.diff(psi,x)
    assert s.simplify(s.diff(vx,x)+s.diff(vz,z))==0
    assert integrate_xz(vx*K*s.cos(z))==0
    assert integrate_xz(vx**2+vz**2)==7*s.pi**2
    assert integrate_xz(-K*vx*vz*s.cos(z))==s.Rational(3,2)*K*s.pi**2

def test_sharp_tracefree_constant():
    m=s.symbols("m",positive=True)
    S=s.diag(2*m,-m,-m)
    assert s.simplify(s.trace(S.T*S)-6*m*m)==0

def test_subleading_modulation_scaling():
    tau,h=s.symbols("tau h",positive=True)
    D=s.Rational(1,2)-h
    assert s.simplify(tau**D*tau**(-s.Rational(3,2))-tau**(-1-h))==0
