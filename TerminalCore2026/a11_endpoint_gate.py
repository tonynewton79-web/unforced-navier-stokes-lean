"""Conditional A.11 endpoint stress arithmetic; never source-authenticated.

All endpoint data here must later be derived from a genuine Appendix-A
profile by an independently replayable source interval generator.
"""
import sys,json
from fractions import Fraction as F
def q(x):
    if isinstance(x,(float,bool)):raise ValueError("Use exact rational strings")
    return F(str(x))
def check(d):
    keys=['lambda','h','Ebase_left_over_lambda_upper','Db_left_upper',
          'Db_right_upper','Pb_left_upper','Pb_right_upper',
          'source_parameter_tuple_hash']
    if any(k not in d for k in keys):raise ValueError("Missing source endpoint")
    if not d['source_parameter_tuple_hash']:raise ValueError("No source tuple")
    lam,h=q(d['lambda']),q(d['h'])
    if not (0<lam<=F(1,20) and 0<h<=lam/100):
        raise ValueError("Invalid parameter range")
    bounds={k:q(d[k]) for k in keys[2:7]}
    if min(bounds.values())<0:raise ValueError("Negative tail bound")
    delta=40960*lam**28;kappa=((1+delta)/(1-delta))**2
    eps=2560*lam**28/(1-delta)
    D=max(bounds['Db_left_upper'],bounds['Db_right_upper'])
    E=(1+delta)*bounds['Ebase_left_over_lambda_upper']
    a=4*h*kappa*D;b=1+2*h;c=2*eps*(kappa*D+F(1,2))
    arithmetic=(E<=F(1,4) and a<=F(61,100)
         and b<=F(1001,1000) and c<=F(1,100))
    return dict(status='CONDITIONAL_ONLY__NO_AUTHENTICATED_SOURCE_PROFILE',
      arithmetical_thresholds_met=arithmetic,source_validated=False,
      E_over_lambda=str(E),four_h_D=str(a),two_A=str(b),
      two_eps_D_plus_half=str(c),
      N_over_E_over_lambda_upper=str(E*(a+b+c)),
      source_terminal_moment_and_pressure_gauge='NOT_VERIFIED',
      future_corrected_slope='NOT_VERIFIED')
def selftest():
    data=dict(zip(['lambda','h','Ebase_left_over_lambda_upper',
          'Db_left_upper','Db_right_upper','Pb_left_upper',
          'Pb_right_upper','source_parameter_tuple_hash'],
          ['1/20','1/2000','1/8','1','2','1/4','1/3','SYNTHETIC_NOT_SOURCE']))
    assert check(data)['arithmetical_thresholds_met']
    for k,v in [('lambda','1/2'),('Db_left_upper','-1'),
                 ('Pb_right_upper',0.5)]:
        bad=data.copy();bad[k]=v
        try:check(bad)
        except ValueError:pass
        else:raise AssertionError('accepted invalid input')
    print(json.dumps(check(data),indent=2))
if __name__=='__main__':
    if len(sys.argv)>1:print(json.dumps(check(json.load(open(sys.argv[1]))),indent=2))
    else:selftest()
