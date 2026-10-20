# Start-to-finish Lean proof dependency ledger (20 October 2026)

**The proposed unforced terminal-core Theorem 1.1 is NOT proved.**
A full Lean certificate requires a kernel-checked proof term for each
mathematical obligation below, not an abstract theorem with axiom
hypotheses that merely assume the PDE or profile existence.

1. Freeze a source-admissible Appendix A tuple: moment corrections,
   true smooth-step-derivative bumps, (M_d,P_*,T_f,lambda,h,X_R),
   terminal cutoff and pressure datum.
2. Formalize the complete source equations (4.11), (4.15), (4.16)
   and stagewise radial integrals and first eta derivatives.
3. Produce validated interval enclosures for all corrected
   stages. Inner and joining stages require the relaxed cone (4.21).
   The indicated outer stages require the full cone (4.22).
4. The new (A11ConeMargin.lean) proves **only real-algebra**
   cone-margin identities and rational bounds (pending successful CI).
   The exact checker tests implications of input intervals; it does NOT
   generate or validate source data.
5. For the two (A.11) azimuthal corrections, retain the established
   slope and first-eta bounds. The new paper proves conditionally
   (Q_sgelambda/2); the outstanding support inputs are
   (|N_s|/Elelambda/2) and (Xge9/lambda).
6. Certify the pulse's source-specific (o(1)) errors, positive
   stress-direction margins, terminal endpoint factorization,
   pressure-neutral moment corrections and exact exterior tail.
7. Quantitatively certify the Appendix B analytic leading profile
   for the SAME parameter tuple, including the outer pressure datum.
8. Construct the distinct unforced (n=1,2) correction solutions
   with their true pressure gauges and the full all-order recurrence.
9. Formalize two-space analytic convergence and all differentiated
   terminal-core limits.
10. Formalize zero physical *unforced* Navier--Stokes residual,
    divergence-free condition, axis regularity, and the stated
    time/local domain. Only then close the actual theorem.

The publicly available OpenAI forced Navier--Stokes Lean project
formalizes a DIFFERENT theorem with smooth compactly supported forcing.
It does not prove the user's proposed unforced result.

No `sorry`, `axiom`, numerical demo, or assumption of the desired
PDE residual may be represented as a completed proof.

Source: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
Sections 4.2--4.3 and Appendix A.5.
