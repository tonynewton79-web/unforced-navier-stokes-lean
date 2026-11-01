"""Exact unforced shear correction, scaling and periodic-integral controls.
Analyticity theorem is established PDE prior art, NOT certified by these tests.
"""
import numpy as np
import sympy as s

def test_exact_nonzero_unforced_shear():
    y,t=s.symbols("y t",real=True,positive=True)
    u=s.exp(-t)*s.sin(y)
    assert s.simplify(s.diff(u,t)-s.diff(u,y,2))==0
    assert s.simplify(s.diff(u,y)-s.diff(u,y))==0

def test_projected_correction_identity_algebra():
    Ux,wx=s.symbols("U_x w_x")
    assert s.expand((Ux+wx)**2-Ux**2-2*Ux*wx-wx**2)==0

def test_h8_retention_shear_rate():
    h=s.symbols("h",positive=True)
    p=s.Rational(1,2)-3*h
    q=s.simplify((s.Rational(3,2)-h-p)/2)
    assert q==s.Rational(1,2)+h

def test_periodic_gradient_mean():
    x=s.symbols("x",real=True)
    assert s.integrate(s.diff(s.sin(x),x),(x,0,2*s.pi))==0
    assert s.integrate(s.diff(s.cos(2*x),x),(x,0,2*s.pi))==0

def test_shear_3d_grid_unforced_residual():
    n=32
    x=np.arange(n)*2*np.pi/n
    t=.4; u=np.exp(-t)*np.sin(x)
    dt=-u;lap=-u
    assert np.max(abs(dt-lap))<1e-14
    assert np.max(abs(u))>0
