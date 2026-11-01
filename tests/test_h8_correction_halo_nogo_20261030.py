"""Appendix AB algebra/pressure replay. Tests necessary bounds, not a blow-up solution."""
import sympy as sp
import numpy as np
h=sp.symbols("h",positive=True)
A=sp.Rational(1,2)+h
D=sp.Rational(1,2)-h
p=sp.Rational(1,2)-3*h
T=sp.Rational(3,2)+2*h

def test_geometry_volume_and_energy():
    assert sp.simplify(1+D-(sp.Rational(3,2)-h))==0
    assert sp.simplify((1+D-1)-p-2*h)==0

def test_pressure_mixed_and_self_gap():
    assert sp.simplify(2*A-(A+sp.Rational(1,2))-h)==0
    assert sp.simplify(2*A-1-2*h)==0

def test_all_nonpressure_fluxes_subcritical():
    for e in (2-h-sp.Rational(3,2),2-h-(sp.Rational(1,2)+1),1+D-1):
        assert sp.simplify(e-p-2*h)==0

def test_correction_pressure_gradient_threshold():
    assert sp.simplify((2-h)-p-T)==0

def test_far_halo_distance_exponent():
    beta=sp.simplify(T/4)
    assert beta==sp.Rational(3,8)+h/2
    assert beta.subs(h,sp.Rational(1,10))==sp.Rational(17,40)

def test_separation_power_saving():
    for hh in (sp.Rational(1,100),sp.Rational(1,10),sp.Rational(3,20)):
        critical=(sp.Rational(3,2)+2*hh)/4
        for eta in (sp.Rational(1,100),sp.Rational(1,50)):
            beta=critical-eta
            assert sp.simplify(sp.Rational(3,2)+2*hh-4*beta-4*eta)==0

def test_automatic_local_retention_ratio():
    assert sp.simplify((1+D-1-p)/2-h)==0

def test_boundary_to_volume_pressure_identity_exact():
    x,y=sp.symbols("x y",real=True)
    w=sp.cos(y)
    q=sp.cos(x)*sp.cos(y)
    boundary=sp.integrate((q.subs(x,sp.pi)-q.subs(x,0))*w,(y,0,2*sp.pi))*(2*sp.pi)
    volume=sp.integrate(w*sp.diff(q,x),(x,0,sp.pi),(y,0,2*sp.pi))*(2*sp.pi)
    assert sp.simplify(boundary+4*sp.pi**2)==0
    assert sp.simplify(volume-boundary)==0

def test_full_periodic_pressure_polarization_fft():
    n=24;x=np.arange(n)*2*np.pi/n
    X,Y=np.meshgrid(x,x,indexing="ij")
    Ux=np.sin(Y);Uy=np.sin(X)
    Wx=np.cos(2*Y);Wy=np.sin(2*X)
    k=np.fft.fftfreq(n,d=1/n);K,L=np.meshgrid(k,k,indexing="ij")
    den=K*K+L*L;den[0,0]=1
    def pressure(a,b):
        t=a[0]*b[0];s=(a[0]*b[1]+a[1]*b[0])/2;z=a[1]*b[1]
        f=-(K*K*np.fft.fft2(t)+2*K*L*np.fft.fft2(s)+L*L*np.fft.fft2(z))/den
        f[0,0]=0
        return np.fft.ifft2(f).real
    PP=pressure((Ux,Uy),(Ux,Uy))
    cross=2*pressure((Ux,Uy),(Wx,Wy))
    self=pressure((Wx,Wy),(Wx,Wy))
    assert np.linalg.norm(cross)>0 and np.linalg.norm(self)>0
    for e in (.25,.125,.0625):
        whole=pressure((Ux+e*Wx,Uy+e*Wy),(Ux+e*Wx,Uy+e*Wy))
        assert np.max(abs(whole-(PP+e*cross+e*e*self)))<1e-12

def test_pressure_gradient_kernel_power():
    d=sp.symbols("d",positive=True)
    assert sp.diff(d**-3,d)==-3*d**-4
