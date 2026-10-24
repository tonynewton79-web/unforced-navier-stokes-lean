"""Conditional interval pressure-mass enclosure for source Appendix A.

The original Appendix A does NOT freeze the moment-corrected exterior
parameters. This requires already-certified stage slope enclosures.
The demo below is NOT a source-admissible Navier--Stokes profile.
All exp functions are evaluated with outward-rounded mpmath.iv.
"""
import argparse,json
from fractions import Fraction
from mpmath import iv
iv.dps=65
def rat(x):
    a=Fraction(str(x))
    return iv.mpf(a.numerator)/iv.mpf(a.denominator)
def integral(s,d):
    if s==0:return rat(d)
    return (iv.exp(2*rat(s)*rat(d))-1)/(2*rat(s))
def evaluate(data):
    P=Fraction(str(data['Pstar']))
    h=Fraction(str(data['h']))
    assert P>0 and h>0
    clo=chi=rat(P)
    low=high=iv.mpf(0)
    detail=[]
    for j,stage in enumerate(data['stages']):
        d=Fraction(str(stage['length']))
        sl=Fraction(str(stage['l_min']))-Fraction(1,2)
        su=Fraction(str(stage['l_max']))-Fraction(1,2)
        assert d>0 and sl<=su
        jl=(clo**2*integral(sl,d)).a
        ju=(chi**2*integral(su,d)).b
        low+=jl
        high+=ju
        clo=(clo*iv.exp(rat(sl)*rat(d))).a
        chi=(chi*iv.exp(rat(su)*rat(d))).b
        detail.append(dict(stage=stage.get('label',j),lower=str(jl),upper=str(ju)))
    inner=5*rat(P)**2
    tlo=(clo**2/(1+2*rat(h))).a
    thi=(chi**2/(1+2*rat(h))).b
    return dict(status="CONDITIONAL; STAGE BOUNDS NOT INDEPENDENTLY CERTIFIED",
      mass_lower=str(((inner+low+tlo)/2).a),
      mass_upper=str(((inner+high+thi)/2).b),
      stages=detail)
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("json",nargs="?")
    args=ap.parse_args()
    if args.json:
        with open(args.json) as f:data=json.load(f)
    else:
        data={'Pstar':'2','h':'1/200','stages':[{
         'label':'NOT_SOURCE_ADMISSIBLE_TEST','length':'1',
         'l_min':'0','l_max':'0'}]}
    result=evaluate(data)
    assert result['mass_lower'] and result['mass_upper']
    print(json.dumps(result,indent=2))
