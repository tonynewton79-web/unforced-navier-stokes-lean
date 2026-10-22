# Complete Lean roadmap: source A.11 to a genuine unforced theorem
This checkpoint proves an exact source-tail stress perturbation identity
in the mathematical manuscript and rational full-hull implications in Lean
candidates. The support **gap** is included. A complete unforced
Navier--Stokes theorem is NOT proved.

**Still required, with trusted formal sources:** (1) source sigma and its
two fixed corrections; (2) source-admissible joint parameter tuple and
moment-correction roots with eta jets; (3) true S(infinity)=Pi(infinity)=0
and sound interval bounds for every cell from first to second support;
(4) all other pulse, exterior and terminal cone intervals;
(5) Appendix B full analytic leading profile and contraction;
(6) actual n=1,n=2 force-free startups; (7) all-order velocity and
pressure convergence; (8) physical-coordinate divergence and *zero*
Navier-Stokes forcing; (9) a fully kernel-verified Lean theorem matching
the claimed initial data, regularity, energy and blowup properties.

The scalar Lean module does not formalize integral facts. The originating
OpenAI global Theorem 1.1 is FORCED. Do not promote it to an unforced proof.


## 22 Oct 2026: explicit A.11 source-amplitude cutoff

New independent source-stage lemma
`A11_Explicit_Profile_Size_20261022_Insert.tex` shows
`E_c<=16 Pstar lambda^45 exp(-13/(2lambda))` throughout
both A.11 supports **and their gap**, assuming the true
source-specific root coefficient bound
`|c_i|<=54 lambda^28` and the original A.6--A.11 stages.
Thus `64 Pstar lambda^44<=1` suffices for `E_c<=lambda/4`.

For source-fixed `Pstar>exp(Td)` and an admissible fixed
`Tf=512`, choose
`Q=1+Td+512+log(Pstar)`,
`lambda=10^-20/[(1+Pstar)Q]`,
`h=lambda exp(-Td)/10^6`. All stated scalar size
inequalities are compatible. This is not a frozen full source
profile and does not replace other later source-dependent
smallness thresholds. The exact verifier
`a11_explicit_profile_size_exact.py` passes. Lean
`A11ExplicitProfileSizeScalar.lean` contains ONLY finite
algebraic cutoff lemmas; its kernel status is pending.

**Implication for source interval programme:** The E_c/lambda
input of existing conditional A.11 whole-hull stress theorems
can now be discharged analytically from the true prescribed
stages and a certified A.11 root. Still OPEN:
same-profile S(infinity)=Pi(infinity)=0, future tail integrals,
genuine c_i/eta-jet source authentication, Q_s/ell/X throughout
the full corrected hull, stress cone on other stages, Appendix B
contraction, unforced n=1,n=2, zero physical residual, and an
entire trusted Lean/mathlib proof.
