"""Regression checks for axisymmetric return-flow and amplitude spectral gate.

Not a source-matched H8 seven-ray construction or a proof of blow-up.
"""
import sympy as s

def test_streamfunction_divergence():
    X,e,h=s.symbols('X e h', positive=True)
    A=s.Rational(1,2)+h
    phi=s.Function('Phi')(X,e);d=1-e**2;L=1-2*h*e**2
    Z=lambda a,f:(2*a*e*f+d*s.diff(f,e)-2*e*X*s.diff(f,X))/L
    vz=s.diff(phi,X)
    vr=-Z(1-A,phi)/s.sqrt(2*X)
    divergence=s.sqrt(2*X)*s.diff(vr,X)+vr/s.sqrt(2*X)+Z(-A,vz)
    assert s.simplify(divergence)==0

def test_exact_compact_axial_return_flux():
    X,e=s.symbols('X e', real=True)
    phi=X*(1-X)**5*(1-4*e**2)**6
    vz=s.diff(phi,X)
    assert s.simplify(s.integrate(vz,(X,0,1)))==0
    assert vz.subs({X:0,e:0})==1

def test_bessel_constrained_radial_eigenvalue():
    z=s.symbols('z',positive=True)
    j2=s.nsolve(s.besselj(2,z),5.1)
    j1=s.nsolve(s.besselj(1,z),3.8)
    assert 26.3746<float(j2**2)<26.3747
    assert 14.6819<float(j1**2)<14.6821
    assert abs(complex(s.N(2*s.besselj(1,j2)-j2*s.besselj(0,j2))))<1e-14

def test_dyadic_amplitude_injection():
    tau,C,s0=s.symbols('tau C s0',positive=True)
    assert s.simplify(s.integrate(C/s0,(s0,tau/2,tau))-C*s.log(2))==0
