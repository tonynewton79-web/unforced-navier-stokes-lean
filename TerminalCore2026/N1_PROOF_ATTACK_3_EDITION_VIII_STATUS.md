# Proof Attack 3 — Edition VIII: n=1 terminal collar obstruction
Date: 22 October 2026

**Mathematical result: conditional/source-local exact nonvanishing.**
The originating OpenAI forced construction, Section 5.2 and Appendix
A.12, has u_theta,0 = K(r,t) f_o(y) in the outer collar with
f_o=1-rho_o[1-sigma((y-1)/2)], rho_o=c_o h>0.
The physical similarity identity is
d_zz(K f_o)=K q^(-2D)[a_z^2 f_o,yy+b_z f_o,y].
At eta=0, a_z=0, b_z=-2. At y=2,
sigma'(1/2)=8 and f_o,y(2)=4rho_o.
Therefore -d_zz(Kf_o)=8 K q^(-2D)rho_o>0.

Under the actual source support schedule, the n=1 positive-order
slow profiles vanish in the terminal collar and the surviving
angular order-one exterior residual is -d_zz u_theta,0. Hence
the prescribed SLOW FIELD cannot solve the zero-residual angular
equation on the collar by simply removing T_1. The source relation
(d_R+2/R)T_{1,theta}=-r_{theta,1} forces T_1 not identically zero.

This is NOT a general nonexistence theorem for an unforced
Navier--Stokes solution: oscillatory momentum flux, a redesigned
leading exterior, or a different n=1 correction could cancel the
residual. The original whole-space construction uses forcing.

Independent verification:
- exact symbolic az/bz and logistic-step midpoint: PASS
- physical coordinate implicit q(z) reconstruction and finite
  differences: 18/18 PASS, max relative error < 1e-5
- negative constant-cutoff and rho=0 controls: PASS
- initial diagnostic sign mistake in the replay was corrected
- Lean N1FirstOrderCollarScalar.lean is only a FINITE SCALAR
  candidate; CI results must be independently checked

Next decisive target:
Prove or falsify existence of an order-one *force-free* correction
mechanism on the annulus, with consistent nonzero smooth initial
data, global incompressibility, pressure, and cancellation of
the actual physical momentum residual. No global unforced theorem
or end-to-end Lean proof has been obtained.
