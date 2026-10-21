"""A.11 Ns/E exact-rational, CONDITIONAL interval implication checker.

Inputs are NOT automatically source-authenticated; a passing result proves
only arithmetic, not the actual stress cone or unforced Navier--Stokes.
"""
from fractions import Fraction as F

def cell(E,u,v,w):
    E,u,v,w=map(F,(E,u,v,w))
    if not (0<=E<=F(1,4) and 0<=u<=F(61,100)
            and 0<=v<=F(1001,1000) and 0<=w<=F(1,100)):
        raise ValueError("source-analytic budget not met")
    bound=E*(u+v+w)
    assert bound<=F(1621,4000)
    return bound,F(1,2)-bound

def verify_cover(cells):
    """Local fixed-bump coordinate t in [-3/20,3/20] and eta in [-1,1].
    The source must separately prove the cells' numerical input bounds."""
    lo,hi=F(-3,20),F(3,20)
    X=sorted(set([lo,hi]+[F(c[k]) for c in cells
         for k in ('t_lo','t_hi')]))
    Y=sorted(set([F(-1),F(1)]+[F(c[k]) for c in cells
         for k in ('eta_lo','eta_hi')]))
    if not cells or X[0]!=lo or X[-1]!=hi or Y[0]!=-1 or Y[-1]!=1:
        raise ValueError("incomplete cover")
    for x0,x1 in zip(X,X[1:]):
        for y0,y1 in zip(Y,Y[1:]):
            midx,midy=(x0+x1)/2,(y0+y1)/2
            if not any(F(c['t_lo'])<=midx<=F(c['t_hi'])
                and F(c['eta_lo'])<=midy<=F(c['eta_hi'])
                for c in cells):
                raise ValueError("uncovered support cell")
    for c in cells:
        cell(c['E_over_lam'],c['four_hD'],c['two_A'],c['two_eps'])
    return True

def selftest():
    c=dict(t_lo='-3/20',t_hi='3/20',eta_lo='-1',
           eta_hi='1',E_over_lam='1/4',four_hD='61/100',
           two_A='1001/1000',two_eps='1/100')
    assert verify_cover([c.copy()])
    assert cell('1/4','61/100','1001/1000','1/100')==(
        F(1621,4000),F(379,4000))
    try:
        wrong=c.copy();wrong['eta_hi']='0'
        verify_cover([wrong])
    except ValueError: pass
    else: raise AssertionError("bad cover accepted")
    try:
        wrong=c.copy();wrong['four_hD']='9/10'
        verify_cover([wrong])
    except ValueError: pass
    else: raise AssertionError("bad budget accepted")
    assert F(1,2)-F(3,20)*F(1621,2000)**2==F(32117077,80000000)
    print("PASS exact conditional A11 Ns slack, cone margin and negative controls")
    print("NO SOURCE INTERVALS AUTHENTICATED; THEOREM 1.1 OPEN")

if __name__=="__main__":selftest()
