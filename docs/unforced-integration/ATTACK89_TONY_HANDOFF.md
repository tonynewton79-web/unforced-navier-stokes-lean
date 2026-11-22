# Attack 89 → Attack 90: source-native signed continuation handoff

**Research owner:** Tony Newton  
**Date:** 22 November 2026  
**Status:** CONDITIONAL_SOURCE_GATE_DERIVED; ACTUAL_CASE006_NUMERIC_FREEZE_OPEN  
**Branch origin:** `feature/attack56-periodic-critical-tail-gauge-20261121`. Main is unchanged.

This note transfers the exact mathematical scope of Attack 89 from the working proof packet to Tony's **original** unforced Navier–Stokes repository. The companion exact-rational test is in `research/attack89/verify_signed_continuation.py`. Earlier attacks 80–89 were researched elsewhere; **their prior GitHub commits are not assumed to have been migrated** by creating this branch.

## Established conditional lemma

The reference coefficient of the **forced** upstream Navier–Stokes construction obeys
[
X\partial_X n+n= S/L,quad X_0=4/\Lambda,quad
L(\eta)=1-2h\eta^2,quad M=Z_*/L.
]
For `X >= X0`, the source error has the exact integrating-factor form
[
\partial_\eta n(X,\eta)-M'(\eta)
= (X_0/X)[\partial_\eta n(X_0,\eta)-M'(\eta)]
+(1/X)\int_{X_0}^{X}
\partial_\eta[(S-Z_*)/L](s,\eta)\,ds.
]

For `|eta|<=1/4` and `0<h<=1/6`, we have `L>=47/48` and `|L'|<=1/6`. Let

- `a=sup_eta |d_eta n(X0,eta)-M'(eta)|`
- `b0=sup_(X,eta)|S(X,eta)-Z*(eta)|`
- `b1=sup_(X,eta)|d_eta(S(X,eta)-Z*(eta))|`

Then
[
\|\partial_\eta n-M'\|_\infty
\le \max\{a,(48/47)b_1+(1/6)(48/47)^2b_0\}.
]
The exact rational multiplier at `a,b0,b1<=1` is `2640/2209<6/5`. If **also** the separately proved Attack 88 source assumption `M'<-13` holds, it follows conditionally that `d_eta n < -59/5`.

For the actual B.26 continuation, if `kappa>=0` and independent of `eta`,
[
G_\eta(Y) \ge G_\eta(4)+
(59/(10\Lambda))\int_4^Y\kappa(s/\Lambda)\,ds.
]
The actual source parameters **have not been frozen to demonstrate `a,b0,b1<=1`**.

## Separate ninth-jet obstruction

For a `C^9` activation cutoff dropping from 1 to `0<kappa0<1/2` across a log-radial interval of width `t1>0`, with derivatives 1 through 8 vanishing at the start,
[
\|\kappa^{(9)}\|_\infty \ge 9!(1-\kappa_0)/t_1^9 > 9!/(2t_1^9).
]
This is a bound for the **cutoff**, not automatically the full nonlinear PDE residual; it cannot be silently removed by source error estimates only involving axial derivatives.

## Attack 90 proof obligations (all OPEN until sourced)

1. Freeze an actual admissible `(h,j0,Lambda,C,t1)` selection and the upstream profiles.
2. Derive rigorous numerical interval bounds `a,b0,b1<=1` from the original source, in the stated parameter order.
3. Certify radial shear on the one-sided Case006 shell, not merely axial shear.
4. Prove nine-jet bounds including the `t1^-9` transition loss and all moving frame derivatives.
5. Freeze four transported patch fields, all twelve ordered nonlinear cross interactions and **complete periodic pressure**.
6. Evaluate the nine real operator blocks of `M_terminal`, prove `rho(M_terminal)<1` and preserve the terminal singular trace.
7. Produce a correctly typed full PDE Lean formalization with no added axioms; no current result proves an unforced singularity.

## Source provenance

Original Case006 source: `Carrier_Independent_Structured_Stress_Route_CASE006_122PAGE-4-1.pdf`; SHA-256 `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`. Original 74-page unforcing paper: SHA-256 `c5a6f28992f48a60b9eec4bd927c753b7f2df58f8e143aa80ebb7c4a194efc60`. Upstream OpenAI *Finite Time Blowup for Navier–Stokes* (2026), Appendix B.25/B.26 and Lemma B.4, describes a **forced** construction.

**Reproducibility:** `python research/attack89/verify_signed_continuation.py`. This checks rational identities and deterministic examples only, not actual source-specific numerical envelopes, PDE pressure, or a millennium theorem.

**Release notice:** ALL G0–G8 full-PDE gates remain open unless individually established elsewhere. The main branch and earlier archival paper are not upgraded to a solved status by this handoff.
