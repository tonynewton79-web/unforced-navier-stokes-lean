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
   slope and first-eta bounds. The analytic source-tail theorem now reduces and proves
   |N_s|/E < lambda/2 on both supports, under source-stage assumptions
   and lambda <= min(10^-6/(T_d+513), 1/[10(1+log P_*)],1/20),
   with h <= lambda/100, and the genuine S(infinity)=Pi(infinity)=0
   normalizations. Together with the prior Q_s >= lambda/2 and a
   selectable radial scale X >=9/lambda, this closes the scalar cone
   implication ON THESE SUPPORTS ONLY. Independently freezing a source
   schedule and verifying those source-stage hypotheses remains open.
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

## Remaining proof tasks after the A.11 axial-tail reduction

- Kernel-certify `A11NsExteriorTail.lean` finite scalar gates. The complete tail integrals and parameter-domain proof are still conventional mathematics, not formalized Lean definitions.
- Formalize the source-compliant (A.11) smooth-step-derivative correction, pressure-neutrality, S(infinity)=0 and future-stage nonpositive slope bounds; the interval script accepts but does not manufacture source bounds.
- Validate one compatible parameter tuple, entire source stage map and all cone margins, including pulse o(1) remainders and endpoints. The A.11 result alone does not imply them.
- Finish Appendix B complex analytic fixed point and actual separate unforced n=1,2 correction systems; then all-index coefficient estimates, convergence and physical unforced PDE equality. Never use `axiom`/`sorry` to disguise any missing obligation.
