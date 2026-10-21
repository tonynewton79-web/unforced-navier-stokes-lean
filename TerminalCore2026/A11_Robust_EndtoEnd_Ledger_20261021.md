# A.11 to the proposed unforced theorem — audited dependency ledger (21 October 2026)

**Current claim:** the full unforced Navier–Stokes Theorem 1.1 is NOT proved. The originating OpenAI paper constructs a solution with smooth compactly supported forcing.

## New rational whole-hull cone gate
Write f=Ns/E, q=Qs, ell=partial_y log(sqrt(X)E) over the entire A.11 hull of length 23/10: both prescribed supports and the width-17/10 gap. Under 0<lambda<=1/20, 0<h<=lambda/100, X>=9/lambda and |eta|<=1, assume reference bounds |f0|<=503lambda/2000, q0>=49lambda/50, -3lambda/2<=ell0<=-lambda/2, with actual discrepancies at most lambda/100 in each field.

The exact-rational proof yields |Ns|/E <=523lambda/2000 <lambda/2, a positive margin 477lambda/2000, and strict normalized cone >=4192747121/3763600000 >11/10. A new Lipschitz-cell theorem transfers certified center bounds and derivative errors across a complete rectangular support-and-gap covering. Its exact-rational checker rejects incomplete or overlapping cells, missing gauges and oversized derivative errors. A passing example is always labeled CONDITIONAL_SCALAR_PASS_SOURCE_NOT_AUTHENTICATED, NOT source certified.

## Start-to-finish Lean proof obligations

| ID | Requirement | Status |
|---|---|---|
| S00 | Exact smooth-step and A.9/A.11 corrections from the source | Source identities derived; fully formal source input OPEN |
| S01 | One simultaneous source-compatible Md,Td,Pstar,Tf,lambda,h tuple | OPEN |
| S02 | True A.9 pulse and A.11 correction roots and eta derivatives | Conditional reductions, full source proof OPEN |
| S03 | Same-profile terminal S(infinity)=0 and Pi(infinity)=0 with valid future integrals | OPEN jointly |
| S04 | Actual Ns/E, Qs, ell, X and E intervals through both supports AND gap | OPEN |
| S05 | Error-tolerant rational cone implication | PROVED conditionally; rational Lean file submitted |
| S06 | Actual authenticated derivative/Lipschitz mesh over full 23/10 hull | OPEN |
| S07 | All remaining pulse, exterior and terminal stress-cone intervals | OPEN |
| B00 | Outer pressure trace and numerically fixed common complex radii | Analytic path, numeric certificate OPEN |
| B01 | Appendix B nonlinear contraction with Lambda,C and ball | OPEN |
| C00 | Actual unforced n=1,n=2 startup solutions | Algebra audited; existence OPEN |
| C01 | All-order pressure/velocity convergence on common domain | Conditional results; source instantiation OPEN |
| C02 | Exact Cartesian unforced residual 0 and divergence-free regular reconstruction | OPEN |
| C03 | Claimed support, energy, singularity for unforced field | OPEN |
| C04 | Fully kernel-checked start-to-finish Lean theorem with no sorry/admit/user axioms | OPEN |

## Necessary terminal-gauge obstruction
The source formula (4.16) changes under arbitrary terminal integration functions C_S(eta), C_Pi(eta) by
[4h eta C_S-(1-eta²)C_S']/X +4(1/2+h)eta C_Pi-(1-eta²)C_Pi'.
Choosing C_S=K eta changes Ns(0) by -K/X. Local bump equations alone do not authenticate global S and Pi gauges.

## Files and claim boundary
New manuscript insert: A11_Robust_Whole_Hull_20261021_Insert.tex.
Scalar Lean: A11RobustHullScalar.lean (not an integral/PDE formalization).
Checker: a11_robust_hull_exact.py --selftest (exact conditional arithmetic, ten adversarial negative controls).
The comprehensive standalone research PDF and proof pack are supplied to the user. The live GitHub cumulative manuscript contains all prior A.11 inserts.

The next decisive work is to fix one genuine source-corrected parameter tuple, certify its root and terminal gauges, and produce fully authenticated outward interval cells with all derivative bounds. No complete unforced theorem has been established.
