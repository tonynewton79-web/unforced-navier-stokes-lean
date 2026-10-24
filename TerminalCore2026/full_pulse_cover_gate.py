"""Fail-closed rational covering of the entire actual Appendix-A pulse.

No source-derived interval dataset has been certified. A pass is ALWAYS
conditional on separate mathematical proof of input enclosures.
"""
from fractions import Fraction as F
import argparse,json
from a29a30_source_interval_gate import audit_cell,iv

class GateError(ValueError):pass
def q(x):
    if isinstance(x,float):raise GateError("Floats forbidden")
    return F(str(x))
def box(c):
    x,y=c["xi"],c["eta_range"]
    if len(x)!=2 or len(y)!=2:raise GateError("Bad rectangle")
    a,b,z,t=q(x[0]),q(x[1]),q(y[0]),q(y[1])
    if not (0<=a<b<=13 and -1<=z<t<=1):raise GateError("Bad domain")
    return a,b,z,t
def cover(cells):
    boxes=[box(c) for c in cells]
    if not boxes:raise GateError("No source boxes")
    xs=sorted(set([F(0),F(13)]+[v for c in boxes for v in c[:2]]))
    ys=sorted(set([F(-1),F(1)]+[v for c in boxes for v in c[2:]]))
    for a,b in zip(xs,xs[1:]):
      for z,t in zip(ys,ys[1:]):
        if not any(x<=a and b<=y and u<=z and t<=v for x,y,u,v in boxes):
            raise GateError("Gap in exact xi/eta pulse covering")
    return boxes,(len(xs)-1,len(ys)-1)
def interval_pair(v):
    return (q(v[0]),q(v[1])) if isinstance(v,list) else (q(v),q(v))
def audit(doc):
    cells=doc["cells"]
    boxes,shape=cover(cells)
    if doc.get("domain")!="full_pulse_xi_0_13_eta_-1_1":
        raise GateError("Missing full pulse domain declaration")
    for key in ("source_pdf_sha256","coefficient_derivation_file_sha256","interval_proof_file_sha256"):
        h=doc.get(key,"")
        if not isinstance(h,str) or len(h)!=64 or any(ch not in "0123456789abcdef" for ch in h):
            raise GateError("No source evidence hash: "+key)
    params=None
    outputs=[]
    for k,(cell,rect) in enumerate(zip(cells,boxes)):
        d=cell["fields"]
        if interval_pair(d["eta"])!=(rect[2],rect[3]):
            raise GateError("Unmatched eta interval")
        par=(interval_pair(d["lambda"]),interval_pair(d["h"]))
        if params is None:params=par
        if par!=params:raise GateError("Parameters differ between cells")
        X,E,H=(iv(d[i]) for i in ("X","E","H"))
        a,b=(H**2),(2*X*(E**2))
        if a.hi<b.lo or b.hi<a.lo:
            raise GateError("Incompatible source H²=2XE²")
        check=audit_cell(d)
        outputs.append({"cell":k,"local_residual_budget_pass":check["all_pass"]})
    return {"status":"CONDITIONAL_SOURCE_ENCLOSURES_NOT_INDEPENDENTLY_VERIFIED",
       "full_domain_covered":True,"grid_shape":shape,
       "all_residual_cells_pass":all(x["local_residual_budget_pass"] for x in outputs),
       "unforced_theorem_1_1_proved":False,
       "note":"Hashes identify files, not the truth of source enclosures.",
       "checks":outputs}
def selftest():
    cells=[{"xi":["0","5"],"eta_range":["-1","0"]},
           {"xi":["5","13"],"eta_range":["-1","0"]},
           {"xi":["0","13"],"eta_range":["0","1"]}]
    cover(cells)
    tests=[cells[:2],
       [{"xi":["0","6"],"eta_range":["-1","1"]},{"xi":["7","13"],"eta_range":["-1","1"]}],
       [{"xi":["0","13"],"eta_range":["-1","0"]},{"xi":["0","13"],"eta_range":["1/10","1"]}],
       [{"xi":["0","14"],"eta_range":["-1","1"]}],
       [{"xi":["0","13"],"eta_range":["1","-1"]}]]
    for t in tests:
        try:cover(t)
        except GateError:continue
        raise AssertionError("Invalid cover accepted")
    try:audit({"cells":cells,"domain":"full_pulse_xi_0_13_eta_-1_1"})
    except GateError:pass
    else:raise AssertionError("Missing hashes accepted")
    print("PASS full rational pulse covering and six negative controls")
    print("NO certified Appendix-A source-field intervals supplied")
if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("--selftest",action="store_true");a.add_argument("--input")
    opt=a.parse_args()
    if opt.selftest:selftest()
    elif opt.input:
        with open(opt.input) as f:doc=json.load(f)
        print(json.dumps(audit(doc),indent=2))
    else:a.error("Supply a certified interval file, or run --selftest")
