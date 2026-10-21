"""Exact-rational conditional A.11 hull certificate; NEVER authenticates source.
Input bounds must come from an independent validated integration of the
actual corrected Appendix-A source and its terminal gauges.
"""
import argparse, json, hashlib
from fractions import Fraction as F
def rat(v):
    if v is None or isinstance(v,bool): raise ValueError("non-rational")
    return F(str(v))
def check(data):
    keys=["lambda","h","y_min","y_max","x_lower",
          "terminal_S_zero_assumed","terminal_Pi_zero_assumed","cells"]
    if any(k not in data for k in keys): raise ValueError("missing data")
    lam,h=rat(data["lambda"]),rat(data["h"])
    y0,y1=rat(data["y_min"]),rat(data["y_max"])
    if not (0<lam<=F(1,20) and 0<h<=lam/100): raise ValueError("parameter gate")
    if not(y1>y0 and y1-y0==F(23,10)): raise ValueError("missing support/gap hull")
    if rat(data["x_lower"])<9/lam: raise ValueError("radial gate")
    if data["terminal_S_zero_assumed"] is not True or data["terminal_Pi_zero_assumed"] is not True:
        raise ValueError("terminal S/pressure assumptions missing")
    cells=[]
    names=["y0","y1","eta0","eta1","f_abs_center_upper","q_center_lower",
           "ell_center_lower","ell_center_upper","dy_f_upper","deta_f_upper",
           "dy_q_upper","deta_q_upper","dy_ell_upper","deta_ell_upper"]
    for i,row in enumerate(data["cells"]):
        if any(k not in row for k in names):raise ValueError("missing cell values")
        c={k:rat(row[k]) for k in names}
        if not(y0<=c["y0"]<c["y1"]<=y1 and -1<=c["eta0"]<c["eta1"]<=1):
            raise ValueError("bad cell domain")
        if not(0<=c["f_abs_center_upper"]<=F(503,2000)*lam and
               c["q_center_lower"]>=F(49,50)*lam and
               -F(3,2)*lam<=c["ell_center_lower"]<=c["ell_center_upper"]<=-lam/2):
            raise ValueError("bad cell center")
        dy,de=c["y1"]-c["y0"],c["eta1"]-c["eta0"]
        for g in ("f","q","ell"):
            d1,d2=c["dy_"+g+"_upper"],c["deta_"+g+"_upper"]
            if d1<0 or d2<0 or (d1*dy+d2*de)/2>lam/100:
                raise ValueError("unverified Lipschitz cell radius")
        cells.append(c)
    if not cells:raise ValueError("no cells")
    ys=sorted({y0,y1}|{v for c in cells for v in (c["y0"],c["y1"])})
    es=sorted({F(-1),F(1)}|{v for c in cells for v in (c["eta0"],c["eta1"])})
    for a,b in zip(ys,ys[1:]):
        for u,v in zip(es,es[1:]):
            yc,ec=(a+b)/2,(u+v)/2
            cov=sum(c["y0"]<=yc<=c["y1"] and c["eta0"]<=ec<=c["eta1"] for c in cells)
            if cov!=1:raise ValueError("uncovered or duplicated support/gap")
    cone=F(9,8)-F(151,1000)*(F(523,1940)**2)
    assert cone==F(4192747121,3763600000) and cone>F(11,10)
    return {"status":"CONDITIONAL_SCALAR_PASS_SOURCE_NOT_AUTHENTICATED",
            "source_certificate":False,"Lean_full_proof":False,
            "stress_over_E_upper":"523*lambda/2000",
            "cone_lower":str(cone),"cells":len(cells)}

def selftest():
    base={"lambda":"1/20","h":"1/2000","y_min":"0","y_max":"23/10",
          "x_lower":"180","terminal_S_zero_assumed":True,
          "terminal_Pi_zero_assumed":True,"cells":[{
              "y0":"0","y1":"23/10","eta0":"-1","eta1":"1",
              "f_abs_center_upper":str(F(503,2000)*F(1,20)),
              "q_center_lower":str(F(49,50)*F(1,20)),
              "ell_center_lower":"-3/40","ell_center_upper":"-1/40",
              **{k:"0" for k in ("dy_f_upper","deta_f_upper","dy_q_upper",
                                 "deta_q_upper","dy_ell_upper","deta_ell_upper")}}]}
    assert check(base)["source_certificate"] is False
    import copy
    tests=[]
    for key,value in (("terminal_S_zero_assumed",False),
                      ("terminal_Pi_zero_assumed",False),
                      ("x_lower","179"),("h","1/100")):
        x=copy.deepcopy(base);x[key]=value;tests.append(x)
    for key,value in (("y1","3/10"),("eta1","0"),("dy_q_upper","1"),
                      ("q_center_lower","0"),("ell_center_upper","0")):
        x=copy.deepcopy(base);x["cells"][0][key]=value;tests.append(x)
    x=copy.deepcopy(base);x["cells"].append(copy.deepcopy(x["cells"][0]));tests.append(x)
    for x in tests:
        try:check(x)
        except ValueError:pass
        else:raise AssertionError("negative control not rejected")
    print("PASS exact rational conditional fixture; 10 adversarial failure controls")
    print("No source authentication, nonlinear profile, or full Lean proof.")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--selftest",action="store_true")
    p.add_argument("--input")
    args=p.parse_args()
    if args.selftest:selftest()
    elif args.input:
        raw=open(args.input,"rb").read()
        try:result=check(json.loads(raw));code=0
        except (ValueError,KeyError,TypeError) as e:
            result={"status":"FAIL_CLOSED","error":str(e),"source_certificate":False};code=2
        result["input_sha256"]=hashlib.sha256(raw).hexdigest()
        print(json.dumps(result,indent=2));raise SystemExit(code)
    else:p.error("Supply --selftest or --input JSON.")
