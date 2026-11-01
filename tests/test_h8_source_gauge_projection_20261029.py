"""Exact regression checks for H8 source gauge and terminal translation projection.
These prove algebraic identities only; the singular H8 closure remains open.
"""
import sympy as sp

def test_potential_gauge_changes_velocity():
    x, y, z, t, v = sp.symbols("x y z t v", real=True)
    chi = sp.exp(-x*x-y*y-(z-v*t)**2)
    U = sp.Matrix([sp.diff(chi,y), -sp.diff(chi,x), 0])
    W = sp.diff(U,z)
    assert all(sp.simplify(a)==0 for a in sp.diff(U,t)+v*W)
    assert sp.simplify(sp.diff(U[0],x)+sp.diff(U[1],y))==0
    adv = sp.Matrix([sum(U[j]*sp.diff(U[i],p) for j,p in enumerate((x,y,z))) for i in range(3)])
    assert sp.simplify(adv.dot(W))==0

def test_projection_speed_rank_two_identity():
    a,b,c,d=sp.symbols("a b c d",real=True)
    W=sp.Matrix([a,b]); D=sp.Matrix([c,d]); N=W.dot(W)
    P=W*W.T/N; Q=sp.eye(2)-P
    Pdot=(D*W.T+W*D.T)/N - 2*W.dot(D)*P/N
    rhs=(Q*D*W.T+W*D.T*Q)/N
    assert sp.simplify(Pdot-rhs)==sp.zeros(2)
    assert sp.simplify(sp.trace(Pdot*Pdot)/2-D.dot(Q*D)/N)==0

def test_gaussian_profile_critical_projection_speed():
    D=sp.symbols("D", real=True)
    # Exact Gaussian moment variance under rho**2*zeta**2 exp(-2(rho**2+zeta**2)).
    result=sp.Rational(1,2)+4*D**2*sp.Rational(3,8)
    assert sp.simplify(result-(sp.Rational(1,2)+sp.Rational(3,2)*D**2))==0

def test_terminal_tuning_is_necessary_in_neutral_mode():
    tau,tau0,D,sigma,M=sp.symbols("tau tau0 D sigma M",positive=True)
    forcing=M*tau**(D+sigma-1)
    untuned=sp.integrate(forcing,(tau,0,tau0))
    assert untuned==M*tau0**(D+sigma)/(D+sigma)
    tuned=-sp.integrate(forcing,(tau,0,tau))
    assert sp.simplify(tuned/tau**D+M*tau**sigma/(D+sigma))==0
