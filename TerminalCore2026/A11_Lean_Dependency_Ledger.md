# Unforced Navier–Stokes: end-to-end Lean dependency ledger
Checkpoint: 21 October 2026. Source: OpenAI *Finite Time Blowup for Navier–Stokes* §4 and Appendix A; this source proves a **forced** whole-space theorem, not the user's proposed unforced theorem.

The new conditional support result: given all the actual A.11 moment/pressure gauges, stage slope bounds, certified coefficient constraints, and interpolation/radial-scale data, the source identity (4.16) implies |Ns|/E < lambda/2 on both prescribed correction supports. It also yields Qs>=lambda/4 and full cone margin >=21*p1²/40 on those supports under its additional hypotheses. A *simultaneously admissible source tuple has NOT been exhibited*.

| ID | Mathematical requirement | Current evidence | Lean status |
|---|---|---|---|
| A00 | Exact source 4.16 and all moment endpoint gauges | Formula verified algebraically; gauges still conditional | Not formalized |
| A01 | Support-specific U=M=J=0, pressure and S gauges for one corrected profile | Source requirements, not interval certified | Not formalized |
| A02 | Exact future-integral identity for Ns | Manuscript proof and SymPy check | Not formalized |
| A03 | True sigma-prime bump B0<=640/3, B1<=2000000/9 | Explicit analytic proof | Numeric scalar gates only |
| A04 | Weighted future energy <47/10 across plateau, -1 hold, terminal tail | Conditional analytic proof, rational regression | Numeric scalar gates only |
| A05 | Exact A.11 two nonlinear moment equations | Quadratic elimination and eta-derivative identity pass SymPy | Not formalized |
| A06 | Certified actual A.11 small root, deltaI and derivative | **OPEN** | Not formalized |
| A07 | One source-valid bound for Ebaseline on both supports | **OPEN** | Not formalized |
| A08 | Global S(infty)=Pi(infty)=0 and slope inequalities preserved by edits | **OPEN jointly** | Not formalized |
| A09 | Conditional |Ns|/E<lambda/2 | Manuscript mathematical implication | Final scalar margin candidate |
| A10 | Nonnegative Qs at interpolation exit; plateau and actual X lower bound | **OPEN jointly** | Not formalized |
| A11 | Conditional strict full cone on two A.11 supports | Source inequality with gap >=21*p1²/40 | Rational gap only |
| A12 | All pulse, exterior transition and stress endpoint cone margins | **OPEN** | Not formalized |
| B00 | Freeze full source Appendix-A admissible schedule/parameters | **OPEN** | Not formalized |
| B01 | Source-compatible pressure mass and Appendix-B nonlinear contraction | **OPEN** | Not formalized |
| C00 | Genuine unforced n=1,2 corrections and all-order analytic recurrence | **OPEN** | Not formalized |
| C01 | Differentiated physical-coordinate reconstruction with unforced residual zero | **OPEN** | Not formalized |
| C02 | Proposed global unforced Theorem 1.1 | **OPEN** | Not formalized |

Source-level interval inputs needed for A05–A11: lambda,h; certified DeltaI(eta), DeltaI_eta; positive bump integrals u,v0,w; selected quadratic small root c1,c2 and derivatives; unedited E baseline; source moment gauges; slope enclosures through -1 hold and terminal tail; Qs at interpolation exit; and minimum radial X. Tests with synthetic inputs are NOT source certificates.

Files: A11_Stress_Support_Certificate_Insert.tex; A11StressScalar.lean; a11_stress_exact.py; a11_quadratic_exact.py; a11_interval_gate.py. No sorry/axioms are intentionally introduced. Lean CI success has to be checked from completed runs, not inferred from file submission.

**External claim:** A conditional source-native stress support/cone lemma and exact nonlinear moment reduction. No full exterior stress-cone certificate, no Appendix-B fixed point, no unforced startup system, no physical residual, no new unforced finite-time blowup theorem.