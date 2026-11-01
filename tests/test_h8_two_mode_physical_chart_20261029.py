"""Exact symbolic Appendix M regression subset. H8 nonlinear existence remains OPEN."""
import sympy as s

def test_exact_implicit_axial_operator():
    q,eta,h,X=s.symbols("q eta h X",positive=True)
    D=s.Rational(1,2)-h; L=1-2*h*eta**2
    dq=2*q**(1-D)*eta/L
    de=q**(-D)*(1-eta**2)/L
    assert s.simplify((1-eta**2)*dq-2*q*eta*de)==0
    assert s.simplify(D*q**(D-1)*eta*dq+q**D*de-1)==0
    F=s.Function("F")(q,X,eta)
    lhs=s.diff(F,q)*dq+s.diff(F,eta)*de-s.diff(F,X)*X*dq/q
    rhs=q**(-D)/L*((1-eta**2)*s.diff(F,eta)-2*eta*X*s.diff(F,X)+2*eta*q*s.diff(F,q))
    assert s.simplify(lhs-rhs)==0

def test_homotopy_curl_polynomial():
    x,y,z,r=s.symbols("x y z r",real=True)
    P=s.Matrix([x,y,z])
    A=s.integrate(r*s.Matrix([r*y,-r*x,0]).cross(P),(r,0,1))
    curl=s.Matrix([s.diff(A[2],y)-s.diff(A[1],z),s.diff(A[0],z)-s.diff(A[2],x),s.diff(A[1],x)-s.diff(A[0],y)])
    assert s.simplify(curl-s.Matrix([y,-x,0]))==s.zeros(3,1)

def test_two_mode_rotating_shear():
    t,T,t0,A,v=s.symbols("t T t0 A v",positive=True)
    K=(T-t)**(-A);theta=v*(t-t0)
    B=(T-t0)**(-A)*s.exp(-(t-t0))
    beta=B/K*s.cos(theta);a=B/K*s.sin(theta)
    c=s.diff(K,t)/K+1
    assert s.simplify(s.diff(beta,t)+c*beta+s.diff(theta,t)*a)==0
    assert s.simplify(s.diff(a,t)+c*a-s.diff(theta,t)*beta)==0
    assert s.limit(beta,t,T,dir="-")==0
    assert s.limit(a,t,T,dir="-")==0

def test_anisotropic_exponent():
    h=s.symbols("h")
    A=s.Rational(1,2)+h;D=s.Rational(1,2)-h
    assert s.simplify((1+D)/2-A-(s.Rational(1,4)-3*h/2))==0
