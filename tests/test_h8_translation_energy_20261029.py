"""Source-independent symbolic checks for Appendix J.
These tests do not verify the authentic H8 source or a full Lean theorem.
"""
import sympy as s

def test_translation_energy_periodic_shear():
    t,z=s.symbols('t z', real=True)
    U=s.exp(-t)*s.sin(z-t*t)
    W=s.diff(U,z)
    G=s.diff(U,t)-s.diff(U,z,2)
    N=s.integrate(W**2,(z,0,2*s.pi))
    b_rhs=s.diff(N,t)/(2*N)+s.integrate(s.diff(W,z)**2,(z,0,2*s.pi))/N
    b_lhs=s.integrate(s.diff(G,z)*W,(z,0,2*s.pi))/N
    assert s.simplify(b_lhs-b_rhs)==0

def test_gaussian_radial_and_axial_quotients():
    rho,z=s.symbols('rho z',real=True,positive=True)
    f=rho*s.exp(-rho**2)
    g=z*s.exp(-z**2)
    radial=s.integrate((s.diff(f,rho)**2+f*f/rho**2)*rho,(rho,0,s.oo))
    mass_r=s.integrate(f*f*rho,(rho,0,s.oo))
    assert s.simplify(radial/mass_r-4)==0
    # g is an odd Gaussian for the axial integral, integrate over the real line
    z0=s.symbols('z0',real=True)
    g=z0*s.exp(-z0*z0)
    assert s.simplify(s.integrate(s.diff(g,z0)**2,(z0,-s.oo,s.oo))/
                      s.integrate(g*g,(z0,-s.oo,s.oo))-3)==0

def test_nonzero_cross_advection():
    x,y,a=s.symbols('x y a',real=True)
    psi=s.sin(x)+s.sin(y)+s.sin(x+y)
    phi=s.cos(2*x+y)+s.cos(x)+s.cos(y)
    v=s.Matrix([s.diff(psi,y),-s.diff(psi,x)])
    W=s.Matrix([s.diff(phi,y),-s.diff(phi,x)])
    tr=lambda p,q:s.Matrix([p[0]*s.diff(q[i],x)+p[1]*s.diff(q[i],y) for i in range(2)])
    integ=lambda f:s.simplify(s.integrate(s.integrate(s.expand_trig(s.expand(f)),(x,0,2*s.pi)),(y,0,2*s.pi)))
    assert integ(v.dot(W))==0
    assert integ(v.dot(tr(v,W)))==s.pi**2
    assert s.simplify(integ(-v.dot(tr(v+a*W,v+a*W)))+a*s.pi**2)==0
