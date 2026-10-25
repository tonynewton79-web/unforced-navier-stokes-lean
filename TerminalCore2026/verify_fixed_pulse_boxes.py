"""Fail-closed replay of A.5 pulse formula fields (NOT Qs, Ns or Navier-Stokes)."""
import copy,json
from fractions import Fraction as F
from source_pulse_exact_boxes import generate,one
def audit(doc):
    if doc.get("type")!="SOURCE_DERIVED_FIXED_PULSE_ONLY":raise ValueError("untrusted model")
    boxes=doc.get("cells")
    if not isinstance(boxes,list) or not boxes:raise ValueError("empty cells")
    xx={F(0),F(13)};yy={F(-1),F(1)};rect=[]
    for c in boxes:
        x0,x1=map(F,c["xi"]);y0,y1=map(F,c["eta_range"])
        if not (0<=x0<x1<=13 and -1<=y0<y1<=1):raise ValueError("bad cell")
        expected=one(x0,x1)
        for name in ("R0","R0_xi","R0_eta","R0_xi_eta","phi","sigma_cut"):
            lo,hi=map(F,c[name]);reflo,refhi=map(F,expected[name])
            # ref already includes exact 2^-120 mathematical guard
            if lo>reflo or hi<refhi or lo>=hi:raise ValueError("unsupported source enclosure "+name)
        xx|={x0,x1};yy|={y0,y1};rect.append((x0,x1,y0,y1))
    X=sorted(xx);Y=sorted(yy)
    for a,b in zip(X,X[1:]):
      for c,d in zip(Y,Y[1:]):
        if not any(i<=a and b<=j and k<=c and d<=l for i,j,k,l in rect):
            raise ValueError("uncovered source rectangle")
    return len(boxes),len(X)-1,len(Y)-1
def selftest():
    o=generate(); assert audit(o)==(40,20,2)
    tests=0
    for mode in range(7):
        x=copy.deepcopy(o)
        if mode==0:x["cells"].pop()
        if mode==1:x["cells"][0]["R0"]=["0","0"]
        if mode==2:x["cells"][0]["R0_xi"]=["0","0"]
        if mode==3:x["cells"][0]["R0_eta"]=["0","0"]
        if mode==4:x["cells"][0]["xi"]=["-1","1/50"]
        if mode==5:x["cells"][0]["eta_range"]=["-1/2","0"]
        if mode==6:x["type"]="UNFORCED_NS_PROVED"
        try:audit(x)
        except (ValueError,KeyError):tests+=1
        else:raise AssertionError("false source interval accepted")
    print("PASS 40 exact source formula cells; 7 adversarial rejects")
    print("UNPROVED: physical Q_s,N_s, cone, exterior, full Lean PDE theorem")
if __name__=="__main__":selftest()
