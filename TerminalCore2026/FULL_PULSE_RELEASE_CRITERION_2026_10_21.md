# Full-pulse source certificate audit — 21 October 2026

**Decision: The proposed unforced Theorem 1.1 is NOT proved.**

## Passed mathematical/finite replay checks

- Exact 2×2 Appendix-A (A.9) axial moment cancellation, including parameter derivatives; the negative control rejects frozen correction derivatives.
- Conditional pulse-end lower bound Q_s > lambda/2 under independently assumed entrance |i|,|i_eta| <=100.
- Source-native A.29–A.30 residual identity and exact rational acceptance inequality.
- Exact finite full-domain rectangular covering criterion, plus six adversarial negative controls for holes/incorrect bounds/missing input provenance.
- 93-page PDF compiled locally: original 16-page source unchanged plus revised 77-page cumulative amendment.
- The source test implementation is `TerminalCore2026/full_pulse_cover_gate.py`, which imports `a29a30_source_interval_gate.py`.
- Run `python TerminalCore2026/full_pulse_cover_gate.py --selftest`.
- The finite scalar Lean submission is `TerminalCore2026/FullPulseCoverageGates.lean`; successful GitHub Actions kernel execution is still required. This is **NOT** the integral or PDE proof.

## Critical missing data and proof obligations

1. A frozen, simultaneously admissible Appendix-A source parameter tuple, pulse and all correction coefficients and eta derivatives.
2. Authenticated rational enclosures for E,H,U,M,M_eta,I,I_eta,J,J_eta,S,S_eta,Pi,Pi_eta,R,R_xi, including the exact infinity-pressure gauge, for each cell of a finite cover of [0,13] × [-1,1].
3. Verified A.29–A.30 uniform budget on every covered cell and strict Q_s>0, including boundary cells.
4. Full stress-cone inequalities on both distinct A.11 correction supports, every exterior transition and the terminal joining region, with a **single** parameter realization.
5. Appendix-B nonlinear profile contraction on one verified common complex domain; genuine order-1/2 unforced corrections and all-order series convergence.
6. Physical cylindrical/Cartesian reconstruction with exact zero external force, divergence, momentum residual, axis and boundary conditions.
7. End-to-end Lean kernel formalization and independent review of integral, interval, Banach-space and PDE steps.

## How the checker reports results

- It never declares source authenticity from a hash alone.
- A geometric coverage or local interval arithmetic success is reported as `CONDITIONAL_SOURCE_ENCLOSURES_NOT_INDEPENDENTLY_VERIFIED`.
- It rejects gap covers, wrong parameters, nonpositive denominators, incompatible H^2=2XE^2 and missing file hashes.
- No valid source-derived full pulse interval dataset has been supplied for this revision.
- The OpenAI global construction used here as prior art has **smooth compactly supported forcing**. Its formalization does not establish an unforced theorem.

The complete mathematical reading PDF and 84-entry reproducibility ZIP are attached to the 21 October email release. Do not refer to them as a proof of an unforced singularity or as Lean-certified end-to-end.
