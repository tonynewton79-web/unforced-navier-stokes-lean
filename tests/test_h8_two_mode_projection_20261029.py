"""Exact independent amplitude/translation projections of a full 3D periodic residual.
A finite algebraic test, not a Navier--Stokes existence theorem.
"""
import sympy as s
x,y,z,t=s.symbols("x y z t",real=True)
C=(x,y,z)
def lap(F):return s.Matrix([sum(s.diff(f,q,2) for q in C) for f in F])
def adv(F,H):return s.Matrix([sum(F[j]*s.diff(H[i],C[j]) for j in range(3)) for i in range(3)])
def tim(F):return s.Matrix([s.diff(f,t) for f in F])
def ip(F,H):
    return s.simplify(s.integrate(sum(F[i]*H[i] for i in range(3)),(x,0,2*s.pi),(y,0,2*s.pi),(z,0,2*s.pi)))

def test_two_mode_projection_from_full_physical_residual():
    U=s.Matrix([(1+t)*s.sin(y),(2+t)*s.cos(z),(1-t)*s.sin(x)])
    W=U.diff(z)
    v=s.Matrix([t**2*s.cos(y),t*s.cos(x),t**2*s.cos(y)])
    alpha=t/s.Integer(3); a=t**2/s.Integer(5); beta=1+alpha
    w=alpha*U+a*W+v
    M=ip(U,U); N=ip(W,W)
    assert all(s.simplify(ip(F,H))==0 for F,H in [(U,W),(U,v),(W,v)])
    G=tim(U)-lap(U)+adv(U,U)
    Luv=lap(v)-adv(U,v)-adv(v,U)
    residual=tim(U+w)-lap(U+w)+adv(U+w,U+w)
    cA=ip(G,U)/M; gT=ip(G,W)/N
    bT=ip(G.diff(z),W)/N; eT=ip(adv(U,U),W)/N
    JA=(-ip(adv(w,w),U)+ip(Luv,U)+ip(v,tim(U)))/M
    JT=(-ip(adv(w,w),W)+ip(Luv,W)+ip(v,tim(W)))/N
    assert s.simplify(ip(residual,U)/M-(s.diff(beta,t)+cA*beta-a*N*gT/M-JA))==0
    assert s.simplify(ip(residual,W)/N-(s.diff(a,t)+bT*a+beta*gT+alpha*eT-JT))==0
