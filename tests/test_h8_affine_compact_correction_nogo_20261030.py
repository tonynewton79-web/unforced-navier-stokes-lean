"""Scoped affine-seed pressure-repair test: arithmetic, not PDE existence."""
import sympy as s
import numpy as np

def test_affine_scaling():
    h=s.symbols("h",positive=True)
    A=s.Rational(1,2)+h
    D=s.Rational(1,2)-h
    assert s.simplify(A+D-1)==0
    assert s.simplify(2*A+D-s.Rational(3,2)-h)==0

def test_small_correction_time_scale():
    assert s.Rational(1,2)+1==s.Rational(3,2)

def test_small_correction_vertical_advection():
    h=s.symbols("h")
    A=s.Rational(1,2)+h;D=s.Rational(1,2)-h
    assert s.simplify(A+D+s.Rational(1,2)-s.Rational(3,2))==0

def test_axial_laplacian_exponent():
    h=s.symbols("h")
    D=s.Rational(1,2)-h
    assert s.simplify(s.Rational(1,2)+2*D-s.Rational(3,2)+2*h)==0

def test_vertical_self_convection_exponent():
    h=s.symbols("h")
    D=s.Rational(1,2)-h
    assert s.simplify(1+D-s.Rational(3,2)+h)==0

def test_affine_transverse_axial_derivative_zero():
    x,y,z,t=s.symbols("x y z t")
    U_z=2*z/t
    assert s.diff(U_z,x)==s.diff(U_z,y)==0

def test_affine_residual_coefficient():
    x,y,z,t=s.symbols("x y z t",positive=True)
    u=s.Matrix([-x/t,-y/t,2*z/t])
    vars=[x,y,z]
    acc=-u.diff(t)+s.Matrix([sum(u[j]*s.diff(u[i],vars[j]) for j in range(3)) for i in range(3)])
    assert acc==s.Matrix([0,0,6*z/t**2])

def test_pressure_symbol_rank_one():
    rng=np.random.default_rng(20261030)
    for e in [1.,.3,.1,.01]:
        for _ in range(80):
            k=rng.normal(size=3);k[2]*=e
            projection=np.outer(k,k)/(k@k)
            assert abs(np.linalg.norm(projection)-1)<1e-12

def test_stress_difference_factor_epsilon():
    e,u,w=s.symbols("e u w")
    assert s.expand((u+e*w)**2-u**2-2*e*u*w-e*e*w*w)==0

def test_h8_volume_energy_exponents():
    h=s.symbols("h")
    A=s.Rational(1,2)+h;D=s.Rational(1,2)-h;p=s.Rational(1,2)-3*h
    assert s.simplify(1+D-2*A-p)==0
