"""Fail-closed rational A11 Qs/Ns/cone gate.

This is NOT source authentication. Intervals supplied by a caller must
be independently derived from one original Appendix A source schedule.
"""
from fractions import Fraction as F
import argparse,json
required=["lambda","h","r_center","r_center_eta","c","c_eta",
          "E_over_lambda","D","P","cancel","X_lambda","S_gauge",
          "Pi_gauge","future_slope"]
def run(data):
    missing=[key for key in required if key not in data]
    if missing:return dict(status="REFUSED_MISSING_INPUTS",missing=missing)
    if any(data[k] is not True for k in ["S_gauge","Pi_gauge","future_slope"]):
        return dict(status="REFUSED_MISSING_GAUGE_OR_SLOPE")
    l=F(str(data["lambda"]));h=F(str(data["h"]))
    if not 0<l<=F(1,20) or not 0<h<=l/100:
        return dict(status="REFUSED_PARAMETERS")
    num={key:F(str(data[key])) for key in required[:11]}
    c=num["c"];cp=num["c_eta"]
    if any([num["r_center"]>64*l**28,
            num["r_center_eta"]>64*l**28,
            c>192*l**28,cp>12*l**28]):
        return dict(status="REFUSED_MISSING_MOMENT_DERIVATIVE_CERTIFICATE")
    delta=F(640,3)*c
    if not delta<F(1,2):return dict(status="REFUSED_CORRECTION_POSITIVITY")
    rb_err=F(5,4)*max(num["r_center"],num["r_center_eta"])
    rb=1/(1-l)+rb_err
    if rb>=2:return dict(status="REFUSED_BASELINE_MOMENT")
    rerr=2*delta*rb/(1-delta)
    jeterr=(rb_err+F(640,3)*cp*rb)/(1-delta)
    Q=(l-h)/(1-l)-(1-h)*rerr-(F(1,2)-h)*jeterr
    if Q<=F(49,50)*l:return dict(status="REFUSED_QS_BOUND")
    E=num["E_over_lambda"];D=num["D"];P=num["P"];canc=num["cancel"]
    if not (E<=F(1,4) and D<F(233,100)
            and P<=(1+8*delta)/2 and canc<F(1,1000)):
        return dict(status="REFUSED_N_SOURCE_INPUTS")
    N=E*(4*h*D+4*(F(1,2)+h)*P+canc)
    if N>=F(63,250):return dict(status="REFUSED_NS_BOUND")
    if num["X_lambda"]<9:return dict(status="REFUSED_RADIUS")
    if N/(Q/l)>=F(13,50):return dict(status="REFUSED_SHEAR_RATIO")
    if (2+3*l)/(num["X_lambda"]*(Q/l))>=F(1,4):
        return dict(status="REFUSED_CONE_SCALE")
    return dict(status="CONDITIONAL_ONLY_NOT_SOURCE_AUTHENTICATED",
                Qs_over_lambda_lower=str(Q/l),
                Ns_over_E_over_lambda_upper=str(N),
                cone_rational_lower="55743/50000",
                theorem11_open=True)
def selftest():
    l=F(1,20);h=l/100;delta=40960*l**28
    good=dict(zip(required,[
       str(l),str(h),str(64*l**28),str(64*l**28),
       str(192*l**28),str(12*l**28),"1/4","2329/1000",
       str((1+8*delta)/2),"1/1001","9",True,True,True]))
    out=run(good);assert out["status"]=="CONDITIONAL_ONLY_NOT_SOURCE_AUTHENTICATED",out
    for key,value in [("r_center_eta",None),("r_center_eta","1/5"),
      ("S_gauge",False),("Pi_gauge",False),("future_slope",False),
      ("E_over_lambda","1"),("D","5"),("X_lambda","2")]:
        bad=good.copy()
        if value is None:bad.pop(key)
        else:bad[key]=value
        assert run(bad)["status"].startswith("REFUSED"),(key,run(bad))
    assert F(350000,20**27)<F(1,100)
    assert F(63,250)/F(49,50)==F(9,35)<F(13,50)
    assert F(9,8)-F(3,20)*F(13,50)**2==F(55743,50000)
    print("PASS exact conditional source algebra and 8 fail-closed negative controls")
    print(json.dumps(out,indent=2))
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--selftest",action="store_true")
    p.add_argument("--input");a=p.parse_args()
    if a.selftest:selftest()
    elif a.input:
        with open(a.input) as f:inp=json.load(f)
        print(json.dumps(run(inp),indent=2))
    else:p.error("Provide --selftest or --input")
