# H8 translation-energy and complementary stability gate (29 October 2026)

## Exact results (source-independent)

Let U be a smooth periodic solenoidal carrier, W=∂_z U, N=||W||_2²>0, and G=U_t−ΔU+P div(U⊗U). Then

b=<∂_zG,W>/N = N'/(2N) + ||∇W||²/N + ∫ W·(W·∇)U /N.

If w=aW+v, v⊥W, is an exact unforcing correction, then the moving projection satisfies <P'_t v,v>=0. Further, the complementary L² identity is

(1/2) d||v||²/dt + ||∇v||²
= −∫v·(v·∇)(U+aW) − <G+a∂_zG+a²(W·∇)W,v>.

The pure v⊗v term cancels; this is not a global H8 existence theorem.

## Conditional L² conclusion

Set τ=T−t and A=1/2+h. If the actual source and nonlinear trajectory satisfy

−∫v·(v·∇)(U+aW) ≤ κ_s ||v||²/τ, κ_s<A,

and ||Q[G+a∂_zG+a²(W·∇)W]||_2 ≤ M τ^{−A−1+σ} with σ>0,
then ||v||_2=o(τ^{-A}). This is **only L²**, not the pointwise terminal-retention bound.

## Adversarial diagnostic

The whole-space toroidal Gaussian U=τ^{-A}ρΦeθ, Φ=−(1/2)exp(−ρ²−ζ²), gives
b=(A/2+4)/τ + 3τ^{−1+2h}. It shows the small-κ_b requirement of Appendix I is not automatic. This is not a periodic H8 singular source.

## Missing source-specific work

1. Freeze U_c,p_c,A_c,χ, H8 shapers, ray coefficients, density, frame and one periodic pressure.
2. Verify the three terms in b and the restricted one-sided strain form.
3. Verify Q(G+a∂_zG+a²(W·∇)W) has a positive source gain.
4. Prove nonlinear terminal compatibility and an L∞-controlling correction estimate.
5. Compile an assumption-free Lean existential witness only after the analytic theorem exists.

**Global theorem remains OPEN.** GitHub Actions results cannot be inferred from a local pytest report.
