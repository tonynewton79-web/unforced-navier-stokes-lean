"""Source-independent exact C4 planar pressure moment tests, not full H8."""
import sympy as s
import numpy as np
from numpy.polynomial.legendre import leggauss
r=s.symbols("r",positive=True)
eps=s.symbols("eps",real=True)
F=(1-r*r)**6;G=r**4*F
I=s.simplify(s.integrate(-2*s.pi*r**3*s.diff(F,r)*s.diff(G,r)-8*s.pi*r**2*s.diff(F,r)*G,(r,0,1)))

def test_exact_rational_moment():
    assert s.simplify(I-8*s.pi/1001)==0
    assert s.simplify(12*I-96*s.pi/1001)==0

def test_pressure_m4_coefficient():
    a=s.symbols("a",positive=True)
    assert s.simplify(12*I*eps/(16*s.pi*a**4)-6*eps/(1001*a**4))==0

def test_signed_boundary_work():
    th,a=s.symbols("th a",positive=True,real=True)
    P=12*eps*s.cos(4*th)/(1001*a**4)
    assert s.simplify(a*s.integrate(P*s.cos(4*th),(th,0,2*s.pi))-12*s.pi*eps/(1001*a**3))==0
    assert s.integrate(s.cos(4*th),(th,0,2*s.pi))==0

def test_patch_cross_terms():
    v=s.symbols("v0:4")
    avg=sum(v)/4
    diag=sum(x*x for x in v)/16
    off=sum(v[j]*v[k] for j in range(4) for k in range(4) if j!=k)/16
    assert s.expand(avg**2-diag-off)==0
    assert len([(j,k) for j in range(4) for k in range(4) if j!=k])==12

def test_exterior_harmonic_mode():
    R,th=s.symbols("R th",positive=True,real=True)
    f=s.cos(4*th)/R**4
    assert s.simplify(s.diff(f,R,2)+s.diff(f,R)/R+s.diff(f,th,2)/R**2)==0

def test_independent_polar_quadrature_moment():
    rr,ww=leggauss(80);rr=(rr+1)/2;ww=ww/2
    th=2*np.pi*np.arange(192)/192;R=rr[:,None];T=th[None,:]
    f=(1-R*R)**6;fp=-12*R*(1-R*R)**5
    g=R**4*f;gp=4*R**3*f+R**4*fp
    for e in (-.3,.1,.8):
        ur=-4*e*g/R*np.sin(4*T)
        ut=-fp-e*gp*np.cos(4*T)
        m=12*np.sum(ww[:,None]*R**3*np.exp(4j*T)*(ur+1j*ut)**2)*2*np.pi/192
        assert abs(m-96*np.pi*e/1001)<1e-12

def test_independent_green_kernel_pressure():
    rr,ww=leggauss(80);rr=(rr+1)/2;ww=ww/2
    th=2*np.pi*np.arange(192)/192;R=rr[:,None];T=th[None,:]
    F=(1-R*R)**6;Fp=-12*R*(1-R*R)**5
    G=R**4*F;Gp=4*R**3*F+R**4*Fp;e=.4
    ur=-4*e*G/R*np.sin(4*T);ut=-Fp-e*Gp*np.cos(4*T)
    ux=ur*np.cos(T)-ut*np.sin(T);uy=ur*np.sin(T)+ut*np.cos(T)
    xx=R*np.cos(T);yy=R*np.sin(T)
    wt=ww[:,None]*R*(2*np.pi/192)
    vals=[]
    for phi in np.arange(32)*2*np.pi/32:
        dx=2*np.cos(phi)-xx;dy=2*np.sin(phi)-yy;d2=dx*dx+dy*dy
        vals.append(np.sum(wt*(-(ux*ux+uy*uy)/d2+2*(ux*dx+uy*dy)**2/d2**2))/(2*np.pi))
    assert abs(np.fft.fft(vals)[4]/32-6*e/(1001*16))<1e-12

def test_shaper_quadratic_m4_orthogonality():
    theta=s.symbols("theta",real=True)
    base,aa,bb=s.symbols("base aa bb",real=True)
    v=s.exp(4*s.I*theta)*(s.I*base+aa*s.sin(4*theta)+s.I*bb*s.cos(4*theta))**2
    z=s.simplify(s.integrate(s.expand_trig(s.expand_complex(v)),(theta,0,2*s.pi)))
    assert s.diff(z,aa,2)==s.diff(z,bb,2)==s.diff(z,aa,bb)==0
