"""Exact H8 Appendices N/O identities. Conditional source, no singular PDE claim."""
import sympy as sp
from sympy import Rational as Q


def test_implicit_chart_jacobian():
    tau, X, eta, h = sp.symbols("tau X eta h", positive=True)
    D = Q(1, 2)-h
    d = 1-eta**2
    L = 1-2*h*eta**2
    q=tau/d
    r=sp.sqrt(2*q*X)
    z=q**D*eta
    assert sp.simplify(r*sp.diff(r,X)*sp.diff(z,eta) -
                       tau**(1+D)*L/d**(2+D)) == 0


def test_mass_and_gradient_scalings():
    h=sp.symbols("h")
    D=Q(1,2)-h
    A=Q(1,2)+h
    p=1+D-2*A
    assert sp.simplify(p-(Q(1,2)-3*h)) == 0
    assert sp.simplify((1+D-3)-(-A-1)) == 0
    assert sp.simplify((1+D-2)-(-A)) == 0


def test_explicit_exact_solenoidal_return_profile():
    X,eta,h=sp.symbols("X eta h", positive=True)
    A=Q(1,2)+h
    D=Q(1,2)-h
    d=1-eta**2
    L=1-2*h*eta**2
    H=X*(1-X)**4
    phi=(1-eta**2)**4
    vz=sp.diff(H,X)*phi
    ez=(-2*A*eta*vz+d*sp.diff(vz,eta)-2*eta*X*sp.diff(vz,X))/L
    vr=-((d*sp.diff(phi,eta)+2*D*eta*phi)*H-2*eta*X*sp.diff(H,X)*phi)/(L*sp.sqrt(2*X))
    assert sp.simplify(sp.diff(sp.sqrt(2*X)*vr,X)+ez)==0
    assert sp.integrate(vz,(X,0,1))==0


def test_sharp_return_flow_amplitude():
    m,r0,R=sp.symbols("m r0 R", positive=True)
    neg=m*r0**2/(R**2-r0**2)
    assert sp.simplify((R**2-r0**2)*neg-m*r0**2)==0


def test_support_amplitude_coefficient_threshold():
    h,dstar,Xstar,J1sq=sp.symbols("h dstar Xstar J1sq",positive=True)
    p=Q(1,2)-3*h
    lower=J1sq*dstar/(2*Xstar)-p/2
    assert sp.simplify(lower.subs(Xstar,J1sq*dstar/p))==0


def test_logarithmic_amplitude_injection():
    t0,eps,c=sp.symbols("t0 eps c",positive=True)
    F=c/sp.Symbol("s",positive=True)
    s=next(iter(F.free_symbols - {c}))
    integral=sp.integrate(F,(s,eps,t0))
    assert sp.simplify(integral/sp.log(t0/eps)-c)==0
