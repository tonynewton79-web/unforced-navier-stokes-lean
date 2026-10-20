# Start-to-finish Lean dependency ledger — unforced terminal-core theorem

20 October 2026. This is a proof-obligation graph, **not** a kernel-certified proof of Theorem 1.1.

## Source integral gates
- [x] Source equation (4.16) transcription and exact algebraic decomposition of (A.29)-(A.30) for w=N_s/(E Q_s). A new manuscript lemma and SymPy replay check the algebra.
- [x] Rational sufficient 10^-6 pulse ratio budget if four source-derived errors satisfy specified interval inequalities; checked by exact Fraction and finite Lean scalar *candidate*.
- [x] Audit showing the shear-only coefficient constraint c_i<=lambda/400000 is too weak to bound averaged-velocity residual after division by Q_s~lambda.
- [x] Stronger conditional axial end-bump residual bound using the true moment formula, pre-pulse envelope and an admissible-amplitude premise.
- [ ] Freeze a single source-compatible numerical tuple for Md,Td,Pstar,Tf,lambda,h and both A.9 and A.11 moment corrections. Verify the original source ordering.
- [ ] On a complete pulse subinterval cover, interval-enclose the **actual** E,U,M,M_eta,I,I_eta,J,J_eta,S,S_eta,Pi,Pi_eta and R,Rprime, including derivatives of the source amplitude and both end bumps.
- [ ] Derive eQ,eN and eta*m_eta from exact (4.16), prove Q_s>0, and certify the strict ratio error 10^-6. Never substitute an unspecified O(Cpre) with a numerical constant.
- [ ] Certify the two pulse cone polynomials, every other radial stage, both joining regions, the stress-cone endpoint and terminal moment/pressure matching.

## Inner analytic and PDE gates
- [ ] Freeze the actual Appendix A axis pressure datum in an analytic tube and verify all quantitative Appendix B contraction conditions for the **same** source tuple.
- [ ] Construct the actual unforced n=1 and n=2 coefficient solutions, certify pressure gauges, and prove all-index velocity/pressure bounds in the doubled/shifted spaces.
- [ ] Prove differentiated normal convergence, axis regularity, physical chain-rule reconstruction and exactly zero **unforced** Navier–Stokes residual.
- [ ] Develop trusted Lean definitions and proofs for smooth step functions, source stages, exact integrals, derivative bounds, interval arithmetic soundness, Banach inverses, stress cone, source normalization and physical PDE.
- [ ] Obtain a completed green Lean kernel build of the entire proof chain with no sorry/admit/nonstandard axiom and independent mathematical review.

## CI trust status
The current Lean A29A30PulseScalar.lean covers **finite scalar algebra** only. The exact Python scripts verify polynomial identities and conditional sufficient inequalities, not input source certificates. GitHub workflows must finish successfully before claiming those finite scalar declarations are kernel-checked.

The originating OpenAI whole-space theorem uses smooth compactly supported forcing. It cannot be repackaged as the proposed unforced Theorem 1.1 without proving the missing independent equations and physical reconstruction.
