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


## Normalized A.29–A.30 source jets: next kernel and interval obligations

The source (4.15) five cumulative moments and their eta-derivatives now
have an exact **ten-state** scale-free transport system. With
\`y=log(X/X_R), H=sqrt(2X)E, a=U/E, ell=(log H)_y\`, put
\`m=M/(XE), i=I/(XH), j=J/(XHE), s=S/(XE^2), p=Pi/E^2\`.

Source-normalized transport:
\`m_y=a-(ell+1/2)m\`;
\`i_y=1-(ell+1)i\`;
\`j_y=a-(2ell+1/2)j\`;
\`s_y=a^2-1/2-2ell*s\`;
\`p_y=1/2+(1-2ell)*p\`.
Differentiating gives five sensitivity equations with exact
\`a_eta,ell_eta\` terms. The pressure must be integrated backwards
from the true radial-infinity gauge
\`p_T=-1/[2(1+2h)], (p_eta)_T=0\`.

With \`g=E_eta/E\`, the source stress formulas (4.16) now have a
scale-free representation in these moments and sensitivities;
in particular \`eta*m_eta\` is a directly propagated state.
The complete derived equations and SymPy replay live in the
**emailed research ZIP**. GitHub also has the research-specific
TeX theorem and the \`NormalizedMomentPulseScalar.lean\`
algebraic proof candidates.

**The target ratios are very demanding.** At eta=0 and
lambda=10^-14, q0 is of order 10^-14: the acceptance gates
require absolute enclosure widths around 10^-24 for eQ and
10^-21 for eN. Ordinary double precision cannot certify them.
A rational interval gate with synthetic positive and negative
controls is supplied in the research packet; this does not
construct or authenticate real source intervals.

Still missing: an independently frozen source schedule, a full
pulse covering, validated forcing/eta-jet enclosures on every
Appendix-A stage, sound interval ODE continuation, an actual
source stress-cone proof, Appendix-B contraction, distinct n=1,2
unforced systems, and physical residual zero.
**No full Lean proof of proposed unforced Theorem 1.1 is claimed.**


## Update: first actual formula-derived pulse cells (21 October 2026)

- [x] Algebraic derivation of the fixed A.5 smooth step and its
  first xi derivative, plus exact zero eta jets for R0 alone.
- [x] Rational Taylor/geometric-exp bounds and monotone 16-panel
  quadrature with a written analytic enclosure proof.
- [x] 40 source-derived rectangles covering xi=[0,13],
  eta=[-1,1], with 2^-120 positive containment guard and
  strict R0>=99/100 on [1,10].
- [x] Fail-closed exact rational replay and eight negative
  controls in the local proof packet (GitHub equivalent checks
  supplied). Mathematical field scope is only fixed pulse.
- [ ] Formalize sigma (including flat endpoints), its derivative,
  exponential remainder bounds, phi integration, R0 and source
  interval soundness in Lean; current scalar lemmas are insufficient.
- [ ] Freeze one valid Appendix-A tuple and independently derive
  first eta jets for actual A.9/A.11 corrected source coefficients.
- [ ] Supply source-backed ten-state ODE cells for E,U,M,J,S,Pi
  and their eta derivatives, not synthetic assumed bounds.
- [ ] Verify Q_s,N_s, e_Q,e_N and every strict physical stress
  margin for every closed pulse cell with the necessary cancellation
  precision (centerline may require ~1e-24 absolute control).
- [ ] Verify the complete exterior transitions, terminal
  stress-cone and pressure gauge under that same parameter tuple.
- [ ] Establish Appendix-B nonlinear contraction, separate
  n=1,2 UNFORCED corrections, all-order recurrence, PDE residual,
  axis regularity and exact theorem statement.
- [ ] Complete kernel verification of every analytic and physical
  implication; examine #print axioms and absence of sorry/axiom.

**External result:** rigorously derived fixed-pulse source
enclosures and replayable cell certificates, not a new
unforced Navier–Stokes singularity or end-to-end Lean proof.
