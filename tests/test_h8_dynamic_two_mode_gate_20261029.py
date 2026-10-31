"""Exact Appendix L regression tests; not a proof of singular H8 existence."""
import sympy as s

def test_amplitude_and_translation_orthogonality():
    z=s.symbols('z',real=True)
    U=s.sin(z)+2*s.cos(2*z)
    assert s.simplify(s.integrate(U*s.diff(U,z),(z,0,2*s.pi)))==0

def test_exact_singular_shear_source_channels():
    tau,A,z=s.symbols('tau A z',positive=True)
    U=tau**(-A)*s.sin(z)
    G=-s.diff(U,tau)-s.diff(U,z,2)
    W=s.diff(U,z)
    m=s.integrate(U**2,(z,0,2*s.pi))
    n=s.integrate(W**2,(z,0,2*s.pi))
    c=s.simplify(s.integrate(G*U,(z,0,2*s.pi))/m)
    assert s.simplify(c-A/tau-1)==0
    assert s.integrate(G*W,(z,0,2*s.pi))==0
    assert s.simplify(G-c*U)==0
    assert s.simplify(c+s.diff(m,tau)/(2*m)-s.integrate(s.diff(U,z)**2,(z,0,2*s.pi))/m)==0

def test_exact_canceling_unforced_shear():
    t,t0,T,A,z=s.symbols('t t0 T A z',positive=True)
    K=(T-t)**(-A)
    B=(T-t0)**(-A)*s.exp(-(t-t0))
    U=K*s.sin(z);u=B*s.sin(z);w=u-U
    assert s.simplify(s.diff(u,t)-s.diff(u,z,2))==0
    assert s.simplify(s.diff(w,t)-s.diff(w,z,2)+s.diff(U,t)-s.diff(U,z,2))==0
    assert s.limit(B/K-1,t,T,dir='-')==-1

def test_linearized_shear_invariant_subspace():
    t,y,z,eps=s.symbols('t y z eps',real=True)
    C=s.Function('C')(t);K=s.Function('K')(t)
    Z=eps*s.exp(-t)
    vx=C*s.sin(y)*s.cos(z)
    vz=Z*s.sin(y)
    assert s.simplify(s.diff(vz,t)-s.diff(vz,y,2))==0
    lhs=s.diff(vx,t)-s.diff(vx,y,2)-s.diff(vx,z,2)+vz*K*s.cos(z)
    assert s.simplify(lhs/(s.sin(y)*s.cos(z))-(s.diff(C,t)+2*C+Z*K))==0

def test_quadratic_amplitude_regeneration():
    y,z,K,C,Z=s.symbols('y z K C Z',real=True)
    U=K*s.sin(z);W=K*s.cos(z)
    nonlinear=-Z*C*s.sin(y)**2*s.sin(z)
    b=lambda f:s.integrate(s.integrate(f,(y,0,2*s.pi)),(z,0,2*s.pi))
    assert s.simplify(b(nonlinear*U)/b(U**2)+Z*C/(2*K))==0
    assert b(nonlinear*W)==0

def test_core_energy_and_retention_exponents():
    h,eps=s.symbols('h eps',positive=True)
    A=s.Rational(1,2)+h
    D=s.Rational(1,2)-h
    assert s.simplify(-2*A+1+D)==s.Rational(1,2)-3*h
    assert s.simplify(A+D-1)==0
