"""Independent exact 3D periodic Navier--Stokes algebra checks.
These are finite symbolic identities, NOT a singular-PDE existence certificate.
"""
import sympy as s
x,y,z,t=s.symbols('x y z t',real=True)
coords=(x,y,z)
def dt(V):return s.Matrix([s.diff(v,t) for v in V])
def lap(V):return s.Matrix([sum(s.diff(v,q,2) for q in coords) for v in V])
def div(V):return s.expand(sum(s.diff(V[i],coords[i]) for i in range(3)))
def adv(F,H):return s.Matrix([sum(F[k]*s.diff(H[i],coords[k]) for k in range(3)) for i in range(3)])
def exact_zero(V):return all(s.trigsimp(s.expand(v))==0 for v in V)

def test_nontrivial_3d_coupled_residual_identity():
    U=s.Matrix([(1+t)*s.sin(y),(2-t)*s.sin(x)+s.cos(z),s.sin(x)])
    W=U.diff(z)
    v=s.Matrix([t**2*s.cos(y),t*s.cos(x),t**2*s.cos(y)])
    alpha=t/3; a=t**2/5
    w=alpha*U+a*W+v
    G=dt(U)-lap(U)+adv(U,U)
    L=lambda f:lap(f)-adv(U,f)-adv(f,U)
    lhs=dt(U+w)-lap(U+w)+adv(U+w,U+w)
    rhs=s.diff(alpha,t)*U+s.diff(a,t)*W+dt(v)-L(v)+(1+alpha)*G+alpha*adv(U,U)+a*G.diff(z)+adv(w,w)
    assert div(U)==0 and div(W)==0 and div(v)==0 and div(w)==0
    assert exact_zero(lhs-rhs)

def test_pressure_poisson_sign_and_double_divergence():
    U=s.Matrix([s.sin(y),s.sin(x)+s.cos(z),s.sin(x)])
    assert div(U)==0
    n=adv(U,U); pressure=s.cos(x)*s.cos(y)
    d2=sum(s.diff(U[i]*U[j],coords[i],coords[j]) for i in range(3) for j in range(3))
    assert s.trigsimp(s.expand(div(n)-d2))==0
    assert s.simplify(div(n)+lap(s.Matrix([pressure]))[0])==0
    assert div(n+s.Matrix([s.diff(pressure,q) for q in coords]))==0

def test_periodic_energy_cancellation_with_exact_gradient_norm():
    U=s.Matrix([s.sin(y),s.sin(x)+s.cos(z),s.sin(x)])
    nonlinear=s.expand(sum(U[i]*adv(U,U)[i] for i in range(3)))
    integral=lambda f:s.integrate(f,(x,0,2*s.pi),(y,0,2*s.pi),(z,0,2*s.pi))
    assert s.simplify(integral(nonlinear))==0
    gradnorm=sum(s.diff(U[i],q)**2 for i in range(3) for q in coords)
    assert s.simplify(integral(gradnorm)-16*s.pi**3)==0

def test_periodic_poisson_inverse_commutes_with_axial_derivative():
    H=s.cos(x)*s.cos(z)+3*s.sin(2*y+z)
    P=-s.cos(x)*s.cos(z)/2-3*s.sin(2*y+z)/5
    assert s.simplify(lap(s.Matrix([P]))[0]-H)==0
    assert s.simplify(lap(s.Matrix([s.diff(P,z)]))[0]-s.diff(H,z))==0

def test_cylindrical_inverse_requires_radial_multiplier():
    r=s.symbols('r',positive=True)
    K=s.Function('K')(r,z); M=s.Function('M')(r,z); fr=s.Function('fr')(r,z)
    correct=K+r*(s.diff(K,r)+s.diff(M,z)-fr)
    radial=lambda L:s.diff(K,r)+(K-L)/r+s.diff(M,z)
    assert s.simplify(radial(correct)-fr)==0
    incorrect=K+r*s.diff(K,r)+s.diff(M,z)-fr
    assert s.simplify(radial(incorrect)-fr)!=0

def test_implicit_chart_physical_axial_derivative():
    q,eta,X,D,h=s.symbols('q eta X D h',positive=True)
    d=1-eta**2; L=1-2*h*eta**2
    dz=q**D*L/d
    dq=2*q*eta/d; dX=-2*X*eta/d
    F=q**2*X**3*(1+eta**2)
    direct=(s.diff(F,eta)+dq*s.diff(F,q)+dX*s.diff(F,X))/dz
    transformed=q**(-D)/L*(d*s.diff(F,eta)+2*eta*q*s.diff(F,q)-2*eta*X*s.diff(F,X))
    assert s.simplify(direct-transformed)==0
