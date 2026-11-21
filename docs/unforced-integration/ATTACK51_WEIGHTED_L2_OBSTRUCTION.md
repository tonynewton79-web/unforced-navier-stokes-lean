# Attack 51 — a weighted space–time L2 obstruction for the fixed diagnostic

**Date:** 21 November 2026. **Scope:** fixed source-first Attack49 carrier ONLY.
**Status:** independently checked exact arithmetic and an analytic weak-form proof
conditional on the already stated source pairing and support estimates.
The complete PDE theorem has NOT been checked by Lean.

Let tau=1-t, h=1/200, A=1/2+h and beta=1/2-2h=49/100.
Use Attack49's toroidal solenoidal test V_tau, with its actual pressure-free
source pairing

    <N(U),V_tau>=(201/4000) J tau^beta,
    J>36501/274877906944.

On support S_tau the original estimates are

    |S_tau| <= tau^(3/2-h)/128,
    |V_theta| <= sqrt(tau)/8,
    |d_t V_theta| <= 17*tau^(-1/2)/8,
    |Delta V_theta| <= 83968*tau^(-1/2),
    |r W_r| <= 32, |d_z(rW)| <= 4*tau^h.

For any smooth solenoidal w so that U+w is an *exact unforced solution* with
periodic pressure on 1-2T <= t <= 1-T, define

    q=(sqrt(tau)*w_r, tau^A*w_theta, tau^A*w_z),
    Q_T^2=T^(-beta-1) integral_T^(2T) tau^(-1-h)
         integral_(S_tau) |q|^2 dx d tau.

**Theorem (weighted velocity-only no-go).** For every 0<T<=1/2,

    Q_T > 815189/2408518875348992000 > 3.38e-13.

This is stronger in topology than Attack50's weighted L-infinity obstruction:
it requires no pointwise correction bounds and no derivative smallness.
It forbids Q_T tending to zero; it does not forbid an order-one correction
such as w=-U, which destroys the singular carrier.

**Proof.** Multiply the test by chi(y)=16(y-1)^2(2-y)^2, y=tau/T in [1,2].
Then 0<=chi<=1, |chi'|<=8, and integral_1^2 chi =8/15.
Weak integration by parts (time endpoints vanish) eliminates pressure and
transfers all derivatives to the known test. The mixed convective contraction
is bounded by (17/40)*tau^(-1-h)*|q|. The quadratic contraction is bounded by

    tau^(-1-h)*(32|q_r q_theta|+4|q_z q_theta|)
       <=18*tau^(-1-h)*|q|^2.

The time-test bound becomes (33/8)*tau^(-1/2), and the normalized support
mass M_T <=(1/128) integral_1^2 y^beta dy <1/64.
Cauchy--Schwarz therefore yields

    2445567/687194767360000
        < [(83968+33/8+17/40)/8] Q_T + 18 Q_T^2.

If Q_T<=1, the right side is at most (1682331/160) Q_T.
Exact rational division gives the stated bound; Q_T>1 is immediate.

**Lean gate:** UnforcedPatching/Attack51WeakL2Arithmetic.lean checks exact
arithmetic and the abstract implication from the weak estimate, not the
physical weak estimate or the analytic source pairing.
**Python gate:** tools/verify_attack51_l2.py checks rational and symbolic
coefficients only.

**Separate CI repair:** TerminalCore2026/NormalizedMomentPulseScalar.lean had
a genuine 'No goals to be solved' Lean tactic-order failure; use
field_simp [...] <;> ring to avoid running ring after field_simp closes a goal.

**Still OPEN:** authentic B.12 G1/H8 source matching, nonlinear right inverse,
pressure, terminal retention, exact unforced periodic blow-up and full
unforced Lean theorem. No general Navier--Stokes regularity result is claimed.

Full 3-page manuscript and editable TeX are delivered in the corresponding
ChatGPT session for independent review.
