# 21 October 2026: parity, terminal gauge and complete-Lean boundary

This is a **mathematical dependency ledger, not a complete unforced proof**.
Source: OpenAI, *Finite Time Blowup for Navier–Stokes*, eqs. (4.15)–(4.16),
(A.11), (A.19), (A.21)–(A.23). The source's Theorem 1.1 is FORCED.

**Proved source-conditional implications.**

- The two A.11 correction equations do not alone establish the true
  terminal conditions. The A.11 pressure-neutral integral together with
  source datum (A.21) yields Pi(infinity)=0. The COMPLETE corrected
  pulse A.19 root is needed to impose S(infinity)=0.
- Symmetry of the actual A.10 data and uniqueness of the A.11 small branch
  force c_i(-eta)=c_i(eta); the corrected E,S,Pi are even and Ns is odd.
  Hence Ns(X,0)=0 exactly, not numerically.
- Under the tightened source coefficient estimates
  |c_i|<=54 lambda^28, |c_i,eta|<=6 lambda^28,
  sup beta_i<=640/3, disjoint support length <=3/5,
  and future baseline ell<=0, the EXACT future-support tail
  derivative term is <=768 lambda^28*(1+delta)/(1-delta)^2
  <769 lambda^28, delta=11520 lambda^28.
- With source-authenticated baseline E_b<=lambda/[4(1+delta)],
  D_b<=233/100, P_b<=1/2 on the full closed hull, h<=lambda/100,
  terminal gauges, and same eta-jet hypotheses, strict conditional
  |Ns|/E<503 lambda/2000<lambda/2 holds with
  reserve >497 lambda/2000. The base D_b,P_b ODEs on
  the constant-slope hull are monotone/constant and reduce the
  continuum maxima to the two hull endpoints.

**Still required:** one compatible full source tuple and actual corrected
moment roots; terminal S and Pi matching; independently sound future-tail
interval envelopes and coverage of both supports PLUS their gap; Qs,
slope, full pulse/exterior/terminal stress cones; Appendix B analytic
contraction; actual force-free n=1,2 startup, all-order recurrence and
physical zero-force PDE; complete trusted Lean formalization.

**Code:** A11_Terminal_Parity_And_Improved_Tail_20261021_Insert.tex,
A11ParityAndTailArithmetic.lean and a11_parity_tail_exact.py.
The algebra script is reproducible. Lean status is PENDING until a
finished successful Actions run; neither integral nor PDE is formalized.

No release as a solved Millennium problem or as a complete Lean proof.
