"""Fail-closed terminal-normalization A.11 arithmetic gate.

This code cannot authenticate submitted source enclosures. It only
checks a consequence of values that must be proved independently.
"""
from fractions import Fraction as F
import json,sys
def check(c):
    req=('lambda','h','Emax','Emin','Xmin','Dmax','Pmax','gmax',
         'Sdef','Sdef_eta','Pidef','Pidef_eta')
    absent=[x for x in req if x not in c]
    if absent:return {'status':'REFUSE','missing':absent}
    x={k:F(str(c[k])) for k in req}
    l,h=x['lambda'],x['h']
    if not(0<l<=F(1,20) and 0<h<=l/100
         and 0<x['Emin']<=x['Emax'] and x['Xmin']>0
         and 0<=x['Pmax']<=x['Dmax']
         and min(x[k] for k in ('gmax','Sdef','Sdef_eta','Pidef','Pidef_eta'))>=0):
       return {'status':'REFUSE','reason':'invalid or inconsistent enclosures'}
    must=('same_corrected_source_profile','terminal_integrals_convergent',
          'U_M_J_zero_on_both_supports','whole_future_slope_verified',
          'whole_future_eta_jet_verified','both_supports_covered')
    absent=[z for z in must if c.get(z) is not True]
    if absent:return {'status':'REFUSE','missing_proofs':absent}
    E,D,P,g=x['Emax'],x['Dmax'],x['Pmax'],x['gmax']
    tail=E*(4*h*D+4*(F(1,2)+h)*P+2*g*(D-P))
    gauge=(4*h*x['Sdef']+x['Sdef_eta'])/(x['Xmin']*x['Emin'])
    gauge+=(4*(F(1,2)+h)*x['Pidef']+x['Pidef_eta'])/x['Emin']
    return {'status':'CONDITIONAL_ARITHMETIC_ONLY' if tail+gauge<l/2 else 'REFUSE',
            'bound':str(tail+gauge),'target':str(l/2),
            'external_source_authentication':'NOT PERFORMED'}
if __name__=='__main__':
    if len(sys.argv)==2:
        print(json.dumps(check(json.load(open(sys.argv[1]))),indent=2))
    else:
        assert check({})['status']=='REFUSE'
        base={'lambda':'1/20','h':'1/2000','Emax':'1/80','Emin':'1/100',
              'Xmin':'1000','Dmax':'233/100','Pmax':'1/2',
              'gmax':'1/1000','Sdef':'0','Sdef_eta':'0',
              'Pidef':'0','Pidef_eta':'0',
              'same_corrected_source_profile':True,
              'terminal_integrals_convergent':True,
              'U_M_J_zero_on_both_supports':True,
              'whole_future_slope_verified':True,
              'whole_future_eta_jet_verified':True,
              'both_supports_covered':True}
        assert check(base)['status']=='CONDITIONAL_ARITHMETIC_ONLY'
        base['Pidef_eta']='1/100'
        assert check(base)['status']=='REFUSE'
        print('PASS fail-closed source A11 terminal tests; positive fixture never authenticates a profile')
