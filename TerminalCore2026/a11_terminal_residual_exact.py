"""Source-gated A.11/A.19 terminal residual implication; NOT an actual source solve.
Exact-rational and symbolic replay. A missing source interval is a refusal.
"""
from fractions import Fraction
import sympy as sp
def q(v): return Fraction(str(v))
def certificate(d):
    names=["lambda","h","alpha","beta","F_abs","F_eta_abs","G_abs","G_eta_abs","baseline_ratio_abs"]
    missing=[k for k in names if k not in d]
    if missing:return {"status":"REFUSE_MISSING_INPUT","missing":missing}
    try:v={k:q(d[k]) for k in names}
    except Exception:return {"status":"REFUSE_BAD_RATIONAL"}
    lam,h=v["lambda"],v["h"]
    if not (0<lam<=Fraction(1,20) and 0<h<=lam/100):return {"status":"REFUSE_PARAMETER_DOMAIN"}
    if any(v[k]<0 for k in names[2:]):return {"status":"REFUSE_NEGATIVE_ENCLOSURE"}
    A=Fraction(1,2)+h
    err=v["alpha"]*((2+4*h)*v["F_abs"]+v["F_eta_abs"])+v["beta"]*(2*A*v["G_abs"]+v["G_eta_abs"]/2)
    total=v["baseline_ratio_abs"]+err
    return {"status":"PASS_CONDITIONAL" if total<lam/2 else "FAIL_MARGIN",
            "error":str(err),"total":str(total),"slack":str(lam/2-total),
            "source_intervals":"NOT AUTHENTICATED BY THIS SCRIPT"}
def symbolic():
    t,h,A,X,K,F,Fe,G,Ge=sp.symbols("t h A X K F Fe G Ge")
    d=1-t*t
    lhs=(4*h*t*K*F-d*K*(Fe-4*t*F/(1+t*t)))/X+2*A*t*G-d*Ge/2
    rhs=K/X*((4*h*t+4*t*d/(1+t*t))*F-d*Fe)+2*A*t*G-d*Ge/2
    assert sp.cancel(lhs-rhs)==0
    c1,c2,v1,v2,w1,w2,r1,r2=sp.symbols("c1 c2 v1 v2 w1 w2 r1 r2")
    g=2*v1*c1+w1*c1*c1+2*v2*c2+w2*c2*c2
    assert sp.expand(sp.diff(g,c1)*r1+sp.diff(g,c2)*r2-2*((v1+w1*c1)*r1+(v2+w2*c2)*r2))==0
if __name__=="__main__":
    symbolic()
    demo=dict(zip(["lambda","h","alpha","beta","F_abs","F_eta_abs","G_abs","G_eta_abs","baseline_ratio_abs"],
                  ["1/100","1/100000","10","100","1/100000000000","1/100000000000",
                   "1/1000000000000","1/1000000000000","1/50000"]))
    assert certificate({})["status"]=="REFUSE_MISSING_INPUT"
    assert certificate(demo)["status"]=="PASS_CONDITIONAL"
    for k in ("F_abs","F_eta_abs","G_abs","G_eta_abs"):
        assert certificate({**demo,k:"1"})["status"]=="FAIL_MARGIN"
    assert certificate({**demo,"lambda":"1/10"})["status"]=="REFUSE_PARAMETER_DOMAIN"
    print("PASS source-agnostic exact arithmetic/identity; NOT an interval certificate of actual A.11 profile")
