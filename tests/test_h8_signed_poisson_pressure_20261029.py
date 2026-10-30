"""Exact pressure-work counterexample: algebra only, no singular H8 theorem."""
import sympy as s
x,y,z,lam=s.symbols("x y z lam",real=True)
c=s.Rational(1,3)
f=s.sin(x)+c*s.sin(2*x)
U=s.Matrix([f*s.sin(y),s.diff(f,x)*s.cos(y),0])
v=s.Matrix([s.cos(2*y),0,0])
q=-f**2/2+(1+c*c)/4+(-(4*c*c+1)/4-s.Rational(9,10)*c*s.cos(x)+c*s.cos(3*x)/26)*s.cos(2*y)
coords=(x,y,z)
def div(F):return s.trigsimp(sum(s.diff(F[i],coords[i]) for i in range(3)))
def dd(F,G):return s.trigsimp(sum(s.diff(F[i]*G[j],coords[i],coords[j]) for i in range(3) for j in range(3)))
def lap(q):return sum(s.diff(q,k,2) for k in coords)
def test_exact_signed_poisson_pressure_work():
    assert div(U)==0
    assert div(v)==0
    assert f.subs(x,0)==0 and f.subs(x,s.pi)==0
    assert s.trigsimp(-lap(q)-dd(U,U))==0
    assert s.simplify(s.integrate(q,(x,0,2*s.pi),(y,0,2*s.pi)))==0
    diff=s.trigsimp(q.subs(x,s.pi)-q.subs(x,0))
    assert s.trigsimp(diff-s.Rational(112,195)*s.cos(2*y))==0
    mixed=dd(U,v)+dd(v,U)
    assert s.simplify(s.integrate(mixed*s.cos(2*y),(y,0,2*s.pi)))==0
    assert dd(v,v)==0
    work=s.simplify(s.integrate(diff*s.cos(2*y),(y,0,2*s.pi))*2*s.pi)
    assert s.simplify(work-s.Rational(224,195)*s.pi**2)==0
    u=U+lam*v
    assert div(u)==0
    assert s.trigsimp(u[0].subs(x,0)-lam*s.cos(2*y))==0
    assert s.trigsimp(u[0].subs(x,s.pi)-lam*s.cos(2*y))==0
    assert s.simplify(s.integrate((dd(u,u)-dd(U,U))*s.cos(2*y),(y,0,2*s.pi)))==0
    assert work>0
