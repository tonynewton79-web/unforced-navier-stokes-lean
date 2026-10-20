"""Outward-interval A.19 remainder certificate with EXTERNAL source bounds.
The --demo fixture is deliberately not a verified Appendix-A schedule.
"""
from fractions import Fraction as Q
from mpmath import iv
import argparse,json
iv.dps=90
def v(x):
    q=Q(str(x));return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def audit(lam,mom,bias,beta_l2=Q(5)):
    lam,mom,bias,beta_l2=map(Q,(lam,mom,bias,beta_l2))
    assert 0<lam<=Q(1,20) and min(mom,bias,beta_l2)>=0
    L=v(lam);M=v(mom);B=v(beta_l2)
    D0=M*iv.exp(-v(Q(2,5))*(v(13)/L-v(3)))
    D1=v(Q(55,2))*iv.exp(-v(Q(2,5))*(v(2)/L-v(3)))
    J=2*L*B*iv.exp(-v(26)+v(Q(63,10))*L)
    C=(2/L)*(D0+v(Q(1011,1000))*D1)
    Cp=(2/L)*D1
    Eb=J*C*C;Ea=2*J*C*Cp
    return {"scope":"CONDITIONAL; pre-pulse moments and exterior energy balance must be source-certified",
            "lambda":str(lam),"assumed_moment_bound":str(mom),
            "assumed_bias_bound":str(bias),
            "bump_error_interval":str(Eb),"A_derivative_interval":str(Ea),
            "value_gate_if_inputs_verified":bool(v(bias)+Eb<v(Q(1,2500))),
            "derivative_gate_if_inputs_verified":bool(Ea<v(Q(1,100)))}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--demo",action="store_true")
    p.add_argument("--lambda-value")
    p.add_argument("--pre-moment-bound")
    p.add_argument("--exterior-bias-bound")
    args=p.parse_args()
    if args.demo: q=(Q(1,20),Q(1),Q(39,100000))
    else:
        if not all((args.lambda_value,args.pre_moment_bound,args.exterior_bias_bound)):
            p.error("Provide all 3 source-certified values, or --demo")
        q=(args.lambda_value,args.pre_moment_bound,args.exterior_bias_bound)
    print(json.dumps(audit(*q),indent=2))
