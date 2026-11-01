"""Exact H8 finite-arithmetic checks supporting Appendices AP, AQ, AR.
No assertion here certifies a complete unforced Navier--Stokes solution.
Run: python -m pip install sympy; python tests/test_h8_full_paper_20261101.py
"""
from fractions import Fraction as Q
from sympy import symbols, Rational, simplify, integrate, diff, expand, pi

def rays(A, B, C, D):
    return [-Q(3, 2)*D, 2*C-4*D, -2*C-4*D,
            2*A-8*B+4*D, -2*A+8*B+4*D, 8*B, -8*B]

def floors(A, B, C, D):
    base = [Q(172,1229),Q(172,1229),Q(236,1229),
            Q(172,1229),Q(172,1229),Q(172,1229),Q(172,1229)]
    return [x+y for x,y in zip(base,rays(A,B,C,D))]

def test_axial_witness():
    A=Q(51113,245800); B=Q(15971,983200)
    C=Q(16,1229); D=Q(19171,491600)
    assert min(floors(A,B,C,D)) == Q(1,100)

def test_joint_hexagon():
    g=Q(15971,122900); u=Q(19171,122900)
    lo=Q(47913,245800); hi=Q(54313,245800)
    m=Q(16,1229); a=Q(51113,245800)
    vertices=[(-g/2,-g),(g/2,-g),(a,m),
              (g/2,u),(-g/2,u),(-a,m)]
    for A,C in vertices:
        assert -g<=C<=u and abs(A)-C<=lo and abs(A)+C<=hi
        D=(g+Q(22371,122900))/8 if C==m else -g/4
        B=g/8 if A>0 else -g/8
        assert min(floors(A,B,C,D))>=Q(1,100)

def test_case006_band():
    t=Q(-4443,9832); b=Q(15971,122900)
    assert (t-b,t+b)==(Q(-143017,245800),Q(-79133,245800))

def test_trigonometric_tensor():
    r,l,s,c=symbols('r l s c')
    C4=2+16*s*s+16*l*l*(r*r*s*s-r**4*c*c)+16*l*r*c*s
    C5=2+16*s*s+16*l*l*(r*r*s*s-r**4*c*c)-16*l*r*c*s
    C6=1-16*l*r*c*s; C7=1+16*l*r*c*s
    Pi=Rational(3,8)-2*c*c*(1+l*l*r**4)
    difference=simplify((C4+C5+C6+C7)/16-2*(1+l*l*r*r*s*s)-Pi)
    assert simplify(difference-2*(s*s+c*c-1))==0

def test_sharp_scalar_floor():
    assert 3+4*Q(15,16)==Q(27,4)
    assert Q(27,4)-Q(105,16)==Q(3,16)
    # Equality at d_1=...=d_7=mu establishes sharpness.
    for mu in [Q(-2),Q(0),Q(7,3)]:
        assert 7*mu-4*mu/16==Q(27,4)*mu

def test_fourfold_integrals():
    X,z=symbols('X z',real=True)
    f=(1-X)**4; g=(1-z*z)**4
    q=X*X*(6*f+2*X*diff(f,X))
    rad=integrate(expand(q*q)/2,(X,0,1))
    axial=integrate(expand(g*g),(z,-1,1))
    assert rad==Rational(4,5005)
    assert axial==Rational(65536,109395)
    assert simplify(16*rad*axial)==Rational(4194304,547521975)
    assert simplify(256*rad*axial)==Rational(67108864,547521975)

if __name__=="__main__":
    for f in [test_axial_witness,test_joint_hexagon,test_case006_band,
              test_trigonometric_tensor,test_sharp_scalar_floor,
              test_fourfold_integrals]:
        f()
    print("PASS: six independent exact arithmetic groups")
    print("Scope: finite polynomial and cone identities only.")
