# Original B.34 continuation: exact joining traces and C² kernel

Date: 8 November 2026. STATUS: partial theorem. The original OpenAI (2026) Navier–Stokes result is FORCED; full G1 locally unforced convergence and global unforced blowup remain OPEN.

Source: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf, Appendix B.5–B.8, especially source (B.33)–(B.39).

**Seven actual endpoint functions required at Xi=110:** Gi=U(110,eta), ell_i=log(C E(110,eta)), and five accumulated transformed source moment discrepancies D_M,D_I,D_J,D_S,D_C. The **six outputs** at Xsep are Gi−4eta and five B-traces. The source does not give a numerically certified original parameter tuple, seven Xi C² functions, or unique cutoff widths.

Let qi=(C P*)^(−10), qs=qi exp(T), T=T_sh, f=(1+eta²)^(−1), g=Gi−4eta, tau=ell_i−log f, w(y)=1−sigma(y/T). The exact source B.34 profile, 0≤y=log(X/110)≤T, is U=Gi, E=P* f (qi exp y)^(1/10) exp(w tau). Define K_{p,m}(z)=integral_0^T exp(−p(T−y))[exp(m w(y) z)−1]dy. Define exact restoration constants a_M=exp(−8)(1+I1), a_S=exp(−8)(1+I12), a_J=exp(−64/5)(5/8+I8/5), as verified in Attack44.

The five exact joining discrepancies after the B.34 transition AND axial restoration are:
d_M = D_M+(a_M−qi)g;
d_I = D_I+sqrt(2)P*f qs^(8/5) K_{8/5,1}(tau);
d_J = D_J+sqrt(2)P*f g [a_J−(5/8)qi^(8/5)+qs^(8/5)K_{8/5,1}(tau)];
d_S = D_S+(a_S−qi)g²−P*²f² qs^(6/5)K_{6/5,2}(tau)/2;
d_C = D_C+P*²f² qs^(1/5)K_{1/5,2}(tau)/2.
The artificial intermediate qs terms cancel exactly in the combined axial transport. These equations are determined by actual source moment identities, not a surrogate profile.

**Uniform source C² theorem.** The flat source step satisfies sigma(u)≤u and sigma(u)≤exp(4−u^(−2)) for 0<u≤1/2; its derivative supremum exceeds 3. By original B.33, T≥20||sigma'||∞(B0+||log f||∞)>60||tau||∞. For all three source pairs (p,m)=(8/5,1),(6/5,2),(1/5,2), define
beta_p(T)=(4/p)exp[4−(3/4)(pT)^(2/3)]+(1/p)exp(−pT/4).
Then for |z|≤||tau||∞,
|K(z)|≤m|z|beta_p, |partial_z K(z)|≤m beta_p, |partial_z² K(z)|≤m² beta_p.
Consequently writing Mj=||partial_eta^j tau||∞, j=0,1,2:
||K(tau)||∞≤mM0 beta, ||K_eta(tau)||∞≤mM1 beta, ||K_etaeta(tau)||∞≤(mM2+m²M1²) beta.
The proof splits s=T−y at T/2, uses sigma(s/T)≤s/T, and minimizes (p/4)s+T²/s². The bound contains no unquantified exponential e^(m||tau||).

The conversation-produced source PDF gives the complete three-page proof. Local independent checks: exact symbolic normalized exponents/row cancellations, direct five-moment quadrature and first-eta derivatives on clearly NON-SOURCE diagnostic traces; independently pure-rational cube-root and Taylor upper bounds for beta_p(T). A 238-page cumulative edition preserves the earlier 235 pages, and the complete ZIP passes SHA256 and integrity checks. The diagnostic T=1024 and tau bound 10 in the verifier are NOT authenticated original source inputs.

**Not established:** numeric validated C² enclosures of original seven Xi functions, actual six Xsep functions, nonlinear five-bump coefficients, corrected strict stress cone, local unforced G1, or global unforced NS singularity. This PR MUST remain draft.