# October 29 H8 recovery and source-specific amplitude gate (8 November 2026)

**Status: RESTRICTED. Unforced Navier–Stokes finite-time blow-up remains OPEN.** This cross-manuscript audit preserves October 29 priority and distinguishes older source-independent identities from later calculations for the invalid A.5 frozen diagnostic.

## Already established by October 29; do not rebrand as a new result

The attached 83-page October 29 edition, Appendix M and RELEASE_AUDIT establish:
- Exact implicit-q axial chain rule, rather than source-native q=tau off axis.
- A local homotopy vector potential (not yet a frozen shell gauge, shaper or periodic pressure).
- The full moving amplitude/translation/complementary decomposition u=beta U+a W+v for W=partial_z U, including the moving projections and quadratic regeneration.
- The identity c_A=0.5 M'/M+||grad U||²/M and the conditional beta->0 no-retention theorem if c_A>=kappa/tau and the total modal injection is o(1/tau).
- A local anisotropic H²-to-L-infinity sufficient condition with a separate exterior estimate.

The October 29 Appendix M is **already reproduced at pp. 90–92 of the 181-page November integrated manuscript**. Its adjacent Appendix Q (pp. 93–94) gives BOTH signed terminal-dyad necessary injections, under the stated carrier asymptotics and terminal retention:
integral_I J_A -> c0 log(2), and tau^(−D) integral_I J_T -> g0(1−2^(−D))/D.
Appendices R and T give global energy and moving-boundary inward flux restrictions.

**Additional local G1 issue:** The original 83-page paper at pp. 51–52, Proposition A.29, demonstrates that a shifted-ideal derivative estimate is unbounded in the factored analytic norm. Its valid weaker-pressure identity (A.63) is not a proof of the full nonlinear pressure composite bound (A.65), current-block bounds or differentiated reconstruction. This is not an impossibility theorem in a different norm, but it must be reconciled before treating the separate 16-page local-core convergence claim as independently certified.

The historical RELEASE_AUDIT records 51 passed tests. On November 8, the six Appendix M tests in the ZIP were separately rerun; **6/6 passed**. The other 45 were not rerun.

## New source-specific quantitative corollary, not a full solution

Take the explicit torque-calibrated A.5 diagnostic U^c with h=1/200 and scalar gauge c(t)=−a tau^(−h). Its true implicit chart and cutoff obey |eta|<1/4, X<1/64, q=tau/(1−eta²), hence r²=2qX<=tau/30.

The axial and gauged swirl components are q^(−A) times time-independent rescaled profiles; the radial component is q^(−1/2) times a fixed profile. The exact physical volume Jacobian implies M=||U^c||²=M0 tau^(97/200)+M1 tau^(99/200), M0>0, M1>=0.

Elementary one-dimensional horizontal Poincaré in each of the containing square's x and y directions gives ||grad U^c||²/M >=15 pi²/tau. Therefore
- tau*c_A >= 15 pi²−99/400, approximately 147.796566;
- liminf tau*c_A >=15 pi²−97/400, approximately 147.801566;
- if an exact unforced solution retains beta->1 relative to this prepared carrier, the **complete** signed amplitude injection H_A on every terminal dyad satisfies liminf integral_I H_A >=(15 pi²−97/400)log(2), approximately 102.448239.

This is not an estimate for the authentic convergent H8 hierarchy. The A.5 diagnostic already fails an inner-axis physical source test; its later torque-calibrated version independently fails a weighted toroidal-flux test. The full H_A includes geometric translation injection; the older Appendix Q hypotheses must be established before transferring the lower bound to the separate nonlinear J_A term.

## Next mathematical gate

Freeze ONE common implicit-coordinate and source-matched tuple Uc,pc,Ac,chi,shapers,E,rho,Rstar,p. First settle the local-core analytic pressure and derivative norm issue (G1); then calculate the complete rotating-frame seven-ray slice-flux condition, both signed amplitude and translation injections, the complementary nonlinearity, full periodic pressure and inward energy transport, and local-plus-exterior L-infinity retention. No Lean existential certificate follows from these finite results.

A three-page new proof note and exact symbolic verification are available separately from the current conversation. The 184-page PDF appends the note to the 181-page cumulative edition without altering its prior page text.
