# Attack 90 — One-sided radial sign, companion obstruction and physical ninth-jet cost

**22 November 2026 — Tony Newton — research proof note.**  
**Status: EXACT CONDITIONAL ANALYSIS / ACTUAL NUMERICAL SOURCE ENCLOSURES UNFROZEN.**  
**This is not an unforced Navier–Stokes blow-up proof, nor a full Lean PDE certificate.**

## Frozen source identities, not frozen source values

Source 1: OpenAI, *Finite Time Blowup for Navier–Stokes* (FORCED), Appendix B.5–B.6; B.22–B.26 and Lemma B.4:
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

Source 2: Tony Newton's original 122-page Case006, eqs. (199)–(210), Proposition 9.20, (255)–(257); original SHA-256
`56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`.

The source defines X0=4/Λ, Xi=110, L=1−2hη², M=Z*/L and the reference coefficient n=n_{s,r} by X∂X n+n=S/L. It does **not** fix a numerical tuple (h,j0,Λ,C,t1,P*,sigma*) together with bounds for its profile integrals. Its B.24/B.4 estimates contain unspecified constants in O(Λ^-1)+o_{t1}(1)+O(C^-2). No actual numerical enclosures for the source a,a0,b0,b1 can be inferred from that notation alone.

Define over |η|≤1/4 and X0≤X≤Xi:
- a0=sup_eta |n(X0,η)−M(η)|; a=sup_eta |∂η n(X0,η)−M'(η)|.
- b0=sup_{X,η}|S(X,η)−Z*(η)|; b1=sup_{X,η}|∂η(S(X,η)−Z*(η))|.

The exact integrating-factor identity gives
```
||n−M||∞ <= δ0 := max(a0, (48/47)b0)
||∂η n−M'||∞ <= δ1 := max(a, (48/47)b1+(384/2209)b0).
```
If all bounds are ≤1, then δ0≤48/47 and δ1≤2640/2209. This is conditional algebra and NOT a measured source interval.

## Theorem 90.1 — a signed radial slab fails the actual companion condition

Assume Attack88's source-factorized pressure theorem M'<−13 on |η|≤1/4, 0<h≤1/6, 0<j0≤1/20, and the exact axis value M(0)=−(4+α)j0 with α=1/2+h. For η∈[−1/4,−1/8],
```
M(η)>13/8−(4+α)j0 >= 167/120.
```
Hence if a0,b0≤1, the actual reference n satisfies
```
n(X,η)>167/120−48/47 = 2089/5640 >0,
∂Y G(Y,η)=−κ(Y/Λ)n(Y/Λ,η)/(2Λ)<−2089 κ/(11280 Λ)
```
on the B.26 region where κ>0.

But Case006 Proposition 9.20 requires Dη+U*(η)>0, where D=1/2−h and U*=4η+j0. On the very same slab,
```
Dη+U*=(4+D)η+j0 <= −(13/3)/8+1/20 = −59/120 <0.
```
**Therefore the easy fixed-slab radial-sign certificate cannot be used as the physical strong-Rayleigh patch.** This non-overlap conclusion does not require numerical pressure data.

The genuine admissible patch must be near the source-dependent root η0 of H*, with χ≥χc, positive companion flag and M>0. For that same interval I, a valid numerical gate is
```
inf_I M > δ0=max(a0,48 b0/47),
inf_I χ > χc,
inf_I (Dη+U*) >0.
```
The source proves qualitative existence after parameter selection but supplies no numerical lower margin inf_I M. A negative sign established on a different interval is not a replacement.

## Theorem 90.2 — exact ninth derivative of the physical radial cutoff

During B.26, y=log(X/X0), X=r²/(2q), q=1−t>0, X0=4/Λ. Let κ(0)=1, κ(t1)=κ0<1/2 and κ^(j)(0)=0 for 1≤j≤8. Put
```
r0=sqrt(8q/Λ), r1=r0 exp(t1/2), F(r)=κ(2 log(r/r0)).
```
Every derivative F^(j)(r0) for j=1,…,8 is zero. Taylor's integral remainder across [r0,r1] therefore implies
```
||∂r^9 F||∞ >= 9!(1−κ0)/[sqrt(8q/Λ)(exp(t1/2)−1)]^9
 > (9!/2)(Λ/(8q))^(9/2)/(exp(t1/2)−1)^9.
```
This is a genuine *physical radial derivative* loss. For fixed small t1 its raw size is comparable to q^(-9/2)Λ^(9/2)t1^(-9). It is **NOT** a lower bound on the complete Navier–Stokes residual, because products and nonlinear cancellations may remove terms. The cutoff width is fixed before the terminal q→0 limit; the large finite factor t1^(-9) can potentially be outweighed by subsequently proved terminal powers.

## Source-certified numerical enclosure decision

**HOLD.** Neither the original upstream Appendix B.4 nor the Case006 manuscript provides the fully numerical profile/parameter tuple or explicit constants needed to certify a,a0,b0,b1. An arbitrary example assigning them values ≤1 would not constitute source certification. Source-defined constraints, not just synthetic rational values, must be proved by interval integration of the actual analytic and post-cutoff profiles.

The next release checks are: freeze ordered outer/axis profiles and h,j0,Λ,C,t1; interval-bound Pi0, Pi0', Pi0'', n and S with derivatives; certify a,a0,b0,b1 and inf_I M on **one shared admissible interval**; account for every radial cutoff and moving frame in physical nine jets; reconstruct the four shapers, twelve mixed transports and full pressure; build all nine actual terminal couplings; prove ρ(M_terminal)<1 and the singular velocity trace.

## Reproducibility

Run `python research/attack90/verify_attack90.py`. It performs 40,000 exact rational checks, plus an endpoint-flat polynomial diagnostic. The JSON release gate at `research/attack90/source_release_gate.json` deliberately contains null physical inputs and remains HOLD. A passing finite test does not update the original G0–G8 full-PDE theorem gates.
