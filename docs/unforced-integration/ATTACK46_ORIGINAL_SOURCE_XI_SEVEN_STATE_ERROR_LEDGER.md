# Attack 46 — original-source endpoint IVP and rigorous error ledger

**9 November 2026. Source-conditioned mathematical theorem, not a numeric original-source parameter certificate. The local G1 unforced series and global unforced Navier–Stokes blow-up remain OPEN.**

**Official primary source:** OpenAI (2026), *Finite Time Blowup for Navier–Stokes*, equations (4.15), (B.12)–(B.16), (B.22), (B.25)–(B.26), (B.32), (B.35), (B.40). Original paper proves a construction with compactly supported smooth FORCE, not a globally unforced one. https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

## Actual source-driven endpoint equations

At X0=4/Λ and Xi=110, y=log(X/X0), X=X0 exp y, v=log φ. True initial values are U(0,η)=U_*(η)+Λ^(-1)𝔲(4,η), v(0,η)=log φ_*(η)+log Φ(4,η), and FIVE NONZERO moments obtained by radial integration over the genuine analytic core [0,X0].

Source (B.22) defines U_r,φ_r and from these, reference p1_r and ns_r=Ns_r/L. Source (B.26) and the final convex cutoffs can be expressed using κ(y) (initial 1-(1-κ0)σ(y/t1), then κ0), b(y) (axial slope falls 1→0 after Xb=100) and α(y) (final azimuthal shear interpolates to a=4/5), all radial-only. The true seven-state driven IVP is:

U_y=−bκX ns_r/2;
v_y=−[(1−α)κp1_r+(4/5)α]/2;
M_y=XU;
I_y=2X² exp(v)/C;
J_y=2X² U exp(v)/C;
S_y=XU²−X² exp(2v)/C²;
(Cp)_y=X exp(2v)/C².

The two fields U,v are driven by the **actual** reference, which MUST independently be certified; the five moments then follow triangularly without another PDE solve. At Xi, Gi=U_i, ell_i=v_i+(1/2)log(2Xi), with five scaled row-transformed endpoint discrepancies from the accumulated five moments. The output requires SEVEN Xi input functions, not synthetic values.

## Non-asymptotic parameter-derivative error estimate

Set ||F||_(2)=Σ_(j=0)^2 ||∂η^jF||∞/j!. This is a unital Banach algebra and ||exp(v)−exp(ṽ)||_(2) ≤ exp(V)||v−ṽ||_(2) when both norms ≤V.

For two validated source computations with the SAME frozen cutoffs, radial scales and amplitude C, let ΔX=Xi−X0, L0=log(Xi/X0); eU0,ev0 initial field errors; eN,eP sup C² reference stress errors. Let εU=eU0+(ΔX/2)eN and εv=ev0+(L0/2)eP. Let H=max over both U norms, V=max over both v norms, and eM0,eI0,eJ0,eS0,eCp0 be initial moment errors. Then EXACT error bounds are:

||ΔGi||_(2) ≤ εU,
||Δell_i||_(2) ≤ εv,
||ΔMi||_(2) ≤ eM0+ΔX εU,
||ΔIi||_(2) ≤ eI0+(Xi²−X0²) exp(V) εv/C,
||ΔJi||_(2) ≤ eJ0+(Xi²−X0²) exp(V)(εU+H εv)/C,
||ΔSi||_(2) ≤ eS0+2HΔX εU+(Xi²−X0²)exp(2V)εv/C²,
||ΔCp_i||_(2) ≤ eCp0+2ΔX exp(2V)εv/C².

All source-profile and cutoff choices still must be independently authenticated; the bounds are not self-fulfilling source data.

## Two additional precise source-based facts

- The original symmetric smooth cutoff has ∫₀¹σ=1/2. The reference B.22 freeze at y=2t1 therefore has first-order term (3/2)t1∂yU_nat(0) (and the analogous log φ term), with an explicit ≤2t1² sup||∂y²U_nat||_(2) remainder. The first B.26 activation adds (1−κ0)t1 X0 ns_r(0)/4, with a ≤(1−κ0)t1² sup||∂y(Xns_r)||_(2)/4 remainder.
- Source (B.35) W=1−[2Dη Mhat+(1−η²)∂η Mhat]/x. C² input control of Mhat is NOT enough for C² stress; using M_n=n^(−2)sin(nη) gives bounded C² M_n but W_n,ηη(0)~n/x. A validated **C² stress** check requires at least **C³** moment inputs; this aligns with source Remark B.9.

## Current hard blocker, no fabricated numerical run

The source fixes (B.40) in the order outer parameters → axis j0,σ*,Λ → T_sh → C, X_R → κ0,t1 and the final narrow widths. Its (B.13), (B.23), (B.32) and B.5 use nonnumerical thresholds and reference comparison constants. In the present project there is still **no source-admissible explicit complete tuple**, no validated actual Φ,𝔲 C³ initial profiles and five moments at X0, and no interval enclosures of reference p1_r,ns_r through Xi. These are required before the seven functions can be reported as actual numeric intervals, the B.34 transition and B.8 five-bump Krawczyk solve can proceed, or corrected cone inequalities can be certified.

The conversation includes a visually checked 3-page scholarly PDF/LaTeX note, a 241-page cumulative research PDF preserving all previous 238 page-text SHA256 checks, exact SymPy and Fraction verifier, a rational endpoint error-budget tool which refuses the intentionally incomplete original-source input template, status audit, and SHA256-checked proof ZIP. Finite symbolic tests are not infinite-dimensional/PDE formalization.

**Keep PR draft. Status: VERIFIED_CONDITIONAL_SOURCE_ENDPOINT_TRANSPORT__ACTUAL_XI_INTERVAL_CERTIFICATE_OPEN.**