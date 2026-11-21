# Attack 53 — a source-independent far-field PDE transport gate

**Date:** 21 November 2026. **Status:** self-contained analytic necessary-condition theorem; symbolic transport regression passed. **NOT** a nonzero similarity-profile construction, numerical certificate, or Lean proof of Navier–Stokes breakdown.

## Actual PDE hypotheses

Let W: R×R³→R³ and q: R×R³→R be smooth solutions of the **unforced** backward Leray equation

    ∂s W + (1/2)W + (1/2)(y·∇)W - ΔW + (W·∇)W + ∇q = 0,
    div W = 0.

Assume C≥0 and, for j=0,1,2,

    |∇^j W(s,y)| ≤ C/(1+|y|)^(j+1),
    |∇q(s,y)| ≤ C/(1+|y|)^3.

These are the smooth-profile decay hypotheses from the public Alpöge–Buckmaster lean/Challenge.lean, not data from their unreleased numerical certificate. Norms of higher derivatives are operator norms.

## Theorem 53.1 — exact characteristic transport

Define A(s,r,ω)=r W(s,rω), for r>0 and ω∈S², and K=4C+C². For every σ≥0,

    |A(s+σ, r exp(σ/2), ω) - A(s,r,ω)|
      ≤ K (1-exp(-σ))/r².

If W is periodically twisted by an orthogonal isometry R,

    W(s+P,y)=R W(s,R^-1 y),    P>0,

then

    |R A(s,r exp(P/2),R^-1 ω)-A(s,r,ω)|
      ≤ K (1-exp(-P))/r².

### Full analytic proof

Write F=ΔW-(W·∇)W-∇q. The physical PDE is exactly

    ∂s W +(1/2)[W+(y·∇)W]=F.

From the displayed pointwise bounds,

    |ΔW| ≤ 3C/(1+|y|)^3,
    |(W·∇)W| ≤ C²/(1+|y|)^3,
    |∇q| ≤ C/(1+|y|)^3,

so |F|≤K/(1+|y|)^3. Put y(σ)=r exp(σ/2)ω. The chain rule gives

    d/dσ [r exp(σ/2) W(s+σ,y(σ))]
       = r exp(σ/2) F(s+σ,y(σ)).

Its magnitude is ≤ K r^-2 exp(-σ). Integration from 0 to σ proves the estimate. At σ=P, use the exact twisted-periodicity relation and orthogonality of R to obtain the second inequality.

**This proof uses the actual PDE, not an assumed weak-form estimate, manufactured forcing or finite rational surrogate.**

## Corollary 53.2 — classical two-term far-field rigidity

Suppose the angular limits exist for each s,ω:

    a(s,ω)=lim_{r→∞} A(s,r,ω),
    b(s,ω)=lim_{r→∞} r[A(s,r,ω)-a(s,ω)].

Then the characteristic estimate forces

    a(s+σ,ω)=a(s,ω),
    b(s+σ,ω)=exp(σ/2)b(s,ω).

If W also has the twisted period with P>0 and b(s,·) is bounded on S², then b≡0 and a(ω)=R a(R^-1ω). Indeed twisted periodicity preserves the angular supremum norm of b, whereas the characteristic law multiplies that norm by exp(P/2)>1.

Thus a uniform classical expansion W(s,rω)=a(ω)/r+b(s,ω)/r²+o(r^-2), **if independently proved to exist**, necessarily has b=0.

## Corollary 53.3 — nonzero classical 1/r tail has infinite direct L2 energy

If A(s,r,·) converges uniformly to a nonzero L²(S²) field a(·), then

    ∫_{R³}|W(s,y)|² dy
      = ∫_0^∞ ∫_{S²}|A(s,r,ω)|² dω dr = ∞.

This does not forbid a **localized** finite-energy blow-up construction, but a bare global similarity profile is not itself the final finite-energy witness.


## Theorem 53.4 — nonlinear maximum-speed pressure gate

Suppose in addition that W satisfies the same twisted period with P>0, and set M=sup over all s,y of |W(s,y)|. Spatial decay and twisted periodicity ensure that M is attained (after reducing s modulo P and rotating y accordingly). At any maximum point (s*,y*) of the full spacetime speed, the **complete nonlinear Leray PDE** implies

    -W(s*,y*)·∇q(s*,y*) ≥ M²/2+|∇W(s*,y*)|²,
    |∇q(s*,y*)| ≥ M/2.

To prove this, let S=|W|²/2 and take the inner product of the genuine PDE with W:

    ∂s S +(y/2+W)·∇S - ΔS + S+|∇W|² = -W·∇q.

At the global maximum, ∂s S=0, ∇S=0 and ΔS≤0. The inequality follows, without dropping any nonlinear convection or viscosity. **Corollary:** any decaying twisted-periodic Leray profile with identically zero pressure gradient is trivial.

This is a necessary physical pressure test for *any* candidate nonzero periodic similarity profile, not an existence theorem. It is independent of the numerical certificate and complementary to the far-field transport test.

## Required negative control: log-periodic nonconvergent tails

The decay bound W=O(r^-1) alone does not force a to exist. The scalar transport-model field

    w(s,r)=sin(s-2 log r)/r,  r>0,

satisfies

    ∂s w +(1/2)w +(r/2)∂r w=0,
    w(s+2π,r)=w(s,r),
    |∂r^j w|=O(r^(-1-j)), j=0,1,2,

but r w(s,r) has no radial limit. **This is a negative control for the linear transport mechanism only, NOT a three-dimensional divergence-free Navier–Stokes solution.** Therefore Corollary 53.2 cannot be invoked under the decay hypotheses alone.

## Public certificate integration and Lean HOLD

The Alpöge–Buckmaster public repository (https://github.com/tristanbuckmaster/navier-stokes), latest inspected public head ad53419de079eb8f95f60313473374624a348546, contains a conditional formal proof from PeriodicSimilarityProfileExists / CellSystemCondition, but its 128-bit interval certificate and verification code are absent. Reported certificate hash:

    3f7a335b84b6c7631742cacc5343dfcd11cf72f5221ff79b2b9268790b4b22c5

When a genuine profile is available, this theorem gives a direct finite-radius condition on the real fields to test with rigorous interval bounds; a violation disproves the candidate's claimed PDE plus decay data. Formalizing the characteristic calculus in the actual PDE types, providing certificate data, proving the interval conditions and bridging to the final unforced theorem are all separate **OPEN** gates.

**Exact external Lean certificate fields (15):** The imported declaration is Breakdown.CellLayerSystem.CellSystemCondition in lean/Breakdown/CertCell/StatementDefs.lean, lines 6223–6242. Its named fields are:

1. cell
2. shape_valueSets
3. entry_conditions
4. enclosure_numbers
5. coerciveL2_ge
6. coercivePin_ge
7. certificate
8. instantiation
9. offset_expansion
10. shift_numbers
11. frozen_form
12. adjoint_quadratic
13. adjoint_links
14. potential_entries
15. adjoint_defect

This is an *exact type-declaration inventory*, not verified evidence that any concrete data satisfy those fields. A complete independent release requires actual D, X, R, T, Y, N, B objects, proofs or sound checkers for all 15 fields, certificate integrity, a successfully rebuilt patched Lean package and a closed theorem without an unresolved CellSystemCondition hypothesis.

The companion tools/verify_attack53_farfield.py is a symbolic negative-control regression, not a Lean certificate. Similarity-variable and discretely self-similar Navier–Stokes methods have considerable prior art. This note makes **no priority or novelty claim** without a specialist review.
