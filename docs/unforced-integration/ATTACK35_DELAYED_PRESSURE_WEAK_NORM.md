# Delayed pressure and mixed analytic norms — G1 source audit, 8 November 2026

**The full local-core G1 convergence theorem and global unforced 3D Navier–Stokes singularity remain OPEN.** This note is based on the source-native coefficient hierarchy (5.2)–(5.6) in OpenAI's *Finite Time Blowup for Navier–Stokes*, and extends the restricted estimates of Attacks 31–34.

## Exact pressure normal forms — not model substitutions

Let h in (0,1/100), A=1/2+h, D=1/2−h, d=1−eta², L=1−2h eta², lambda_j=2hj. The source incompressibility map is
V_j=X G_j, G_j=(2eta/L)U_j−[2eta(D+lambda_j)/L] A_X U_j−(d/L)A_X partial_eta U_j,
where A_X F=X^(−1)integral_0^X F.

For k=n−1>=1 and I_k=integral_0^X G_k,
Pi_n^(time) = −[V_k−lambda_k I_k +D eta partial_eta I_k]/(2L).

For j=n−2>=0 and C_XF=integral_0^X F(s)/s ds,
Pi_n^(double)= +(1/2)Z^[2]_(0,j) C_X V_j,
because C_X commutes with D_X and partial_eta on positive-valuation fields.

The ordered radial endpoint sum (i,j)=(0,k),(k,0) in Omega_k has pressure primitive −V_0V_k/(2X). The axial endpoints are −(1/2)C_X[U_0 Z_(0,k)V_k+U_k Z_(0,0)V_0]. The viscous pressure primitive is +V_(k,X). Therefore for n>=2 the **complete delayed linear pressure** source is exactly

Pi_n^(lin,lag) =
−[V_k−lambda_k I_k+D eta partial_eta I_k]/(2L)
−V_0V_k/(2X)
−(1/2)C_X[U_0Z_(0,k)V_k+U_k Z_(0,0)V_0]
+V_(k,X)
+(1/2)Z^[2]_(0,k−1) C_X V_(k−1).

The separate positive-index quadratic normal form of Attack 34 is added to obtain the full Omega pressure source.

## Composed velocity bounds are uniform — under leading analytic multiplier conditions

With doubled weights
w_(a,beta)=R^(−a)varrho^(−beta)(2a+beta)!/[(2a)!(a+1)^2(beta+1)^2]
and inherited ideal norm on I_n=X^n B, the radial-lift ratio is bounded whenever r<=2s:
w_(a,beta+r)/w_(a+s,beta) <= (s+1)^2 (2s)^r R^s varrho^(−r)(a+1)^r, s=1,2.

For U_k=X^a f(eta), p=a+1 and k<=a, the physical incompressibility field is
V_k=X^p[(2eta/L)(1−(D+2hk)/p) f−(d/L)p^(−1)f'].
Each Z acting on X^p is p times a first-order operator in p^(−1)partial_eta with bounded fixed coefficients. Applying the whole pressure-to-velocity composition:
- ||J1 Z_(−2A,n) Pi_n^(time)||_B <= C_T/n ||U_(n−1)||_B;
- ||J1 Z_(−2A,n) Pi_n^(double)||_B <= C_Z ||U_(n−2)||_B;
- the full two leading-index endpoints contribute <= C_E ||U_(n−1)||_B.

All constants are independent of n if the exact leading U0,V0/X and required fixed analytic multipliers share one inherited analytic domain. Bare D_X V and X V_XX are **not** bounded separately.

## Sharp strong-pressure obstruction and weaker repair

The standalone twice-shifted pressure includes the highest derivative
−X^(a+1)(d/L)^3 partial_eta^3 f/[2(a+1)^2].
Three eta derivatives with only one radial lift violate the inherited **strong pressure** weight:
w_(a,beta+3)/w_(a+1,beta)
=R varrho^(−3)*[(a+2)^2/(a+1)^2]*[(beta+1)^2/(beta+4)^2]
*(2a+1)(2a+2)(2a+beta+3) -> infinity.
The unboundedness is genuine for high-frequency e^(iN eta): the strong shifted-derivative norm ratio grows proportionally to N for any fixed radial degree a. A nonzero analytic multiplier (d/L)^3 and bounded lower derivative terms do not remove the principal high-frequency obstruction on a central subcore.

**Necessary repair:** define the one-eta-derivative-weaker pressure weights b_(a,beta)=w_(a,beta+1). Then the delayed twice-shifted pressure map B -> B^− with one radial lift is uniformly bounded, and the subsequent J1 Z operator maps the appropriately valued B^− pressure into the strong velocity space. This resolves a specific operator-topology problem, not the complete mixed-norm recurrence. The earlier scalar majorant with strong ||Pi_n||_B is not justified termwise by this pressure source.

## Source provenance, independent tests, open boundary

The original *forced* OpenAI paper's Appendix B, Proposition B.2, constructs joint-holomorphic leading axis profiles on a small subcore; these can enter the inherited coefficient algebra on a smaller domain by Cauchy bounds. Its Lemma 5.1 constructs each positive-order coefficient separately and explicitly allows order-dependent parameter neighborhoods. This source does **not** certify convergence of the unmodified infinite series.

The current checker independently verified 14 temporal/two-Z identities, 3 radial endpoint primitives, 2 **full Omega pressure ledgers**, 1,728 radial-lift and 2,664 weak-pressure coefficient ratios, and high-frequency strong-pressure diagnostics. The four-page mathematical supplement, original editable LaTeX, Python replay, and 205-page cumulative PDF (201 original pages unchanged) are user-facing artifacts in this conversation. No end-to-end Lean analytic/PDE certificate exists.

**Remaining G1:** derive a uniform mixed velocity/weak-pressure coefficient majorant accounting for all current and delayed terms; independently authenticate the actual leading multipliers and finite startup in one common holomorphic domain; then verify differentiated physical PDE reconstruction. H8 source-matched seven-ray stress, periodic nonlinear unforcing, and finite-time singularity remain OPEN.
