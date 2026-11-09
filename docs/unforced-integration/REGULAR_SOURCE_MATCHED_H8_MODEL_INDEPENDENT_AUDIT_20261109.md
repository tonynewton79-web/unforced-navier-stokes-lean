# Independently checked source-matched stress: a fully explicit REGULAR positive control

**9 November 2026. Critical scope note.** The user's 245-page research manuscript, printed pp. 45–46, **already contains** Theorem A.6, a smooth compact seven-ray stress, corresponding projected source and exact nonlinear correction. It is *not* an inverse for the preassigned singular carrier residual, and does not imply unforced finite-time blow-up. This change independently verifies its quantitative model with explicit small values, rather than appending more pages that claim to close G1.

### Explicit numerical model

On T^3 let κ(s)=exp[-1/(1−16s²)] inside |s|<1/4, flat 0 outside; gamma=15971/122900, eps=gamma/8, b=(35,2,0)/sqrt(1229), R0=b b^T−I/3, H*=eps(e1 e3^T+e3 e1^T). Fix **a=10^(-7)** and **delta=10^(-50)**, ρδ=delta∏κ(xj), Eδ=proper rotation about e2 of angle delta sin(2πx1), Sδ=ρδ Eδ(R0+H*)Eδ^T.

Define genuine-for-this-model f_H8=P div(ρδ Eδ H*Eδ^T), full force Gδ=−P div Sδ. This source is *defined AFTER prescribing the stress*. It must not be confused with the authentic **preassigned** f_H8 from a singular carrier's complete nonlinear residual.

The exact ray map (A,B,C,D)↦(−3D/2,2C−4D,−2C−4D,2A−8B+4D,−2A+8B+4D,8B,−8B) gives c_min=172/1229=1/100+gamma, while H*=H(eps,0,0,0) changes only ray 4 and ray 5 by ±2eps. Thus EVERY original one-sided ray weight is ≥ρδ(1/100+3gamma/4), including the flat collar. The normalized quotient extends smoothly.

**Nonzero source.** The k=(1,0,0) Fourier component of the bump product exceeds 1/65536, because κ̂(0)>1/32 and κ̂(1)>1/64. H*e1=eps e3 with eps>1/64, while tilting costs at most 13delta² in the projected mode. Therefore |f̂_H8,3(k)|>delta/10^6; the full Gδ is nonzero too, using (R0+H*)21=70/1229.

**Explicit H4 operator bound.** A complex-Cauchy estimate with t=1−16s² and radius t/64 gives ||κ^(n)||∞≤n!(54n)^n for n≤4. The complex rotation entries are bounded by 8, and ||R0+H*||F<1. This yields ||∂^α(Sδ/delta)||L∞(F)≤576·24·216^4 for |α|≤4, and the exact Fourier norm expansion gives
||Sδ||H4≤481469424205824·delta<5·10^14delta.

The periodic Fourier embedding ≤2 gives the product estimate ||u⊗u||H4≤32||u||H4², and the integrated heat–Leray divergence estimate is ≤sqrt(2/e)<1. The initial u0=a sin(2πx2)e1 has H4 norm <2000a=2·10^(-4). On X=C([0,1];H4_sol), the forced mild map has invariant radius R=2(||u0||H4+||Sδ||H4)<1/2000, and Lipschitz ≤64R<1/2. Hence a smooth forced solution Uδ exists with unique zero-mean pressure
ΔPδ=−∂i∂j(Uδ,i Uδ,j+Sδ,ij).
Its FULL equation is N(Uδ,Pδ)=−div Sδ, not merely the projected one.

The regular exact unforced shear v(t,x)=a exp(−4π²t) sin(2πx2)e1 has pressure 0. Set wδ=v−Uδ,qδ=−Pδ. This solves the exact full nonlinear correction, and
sup_[0,1]||wδ||H4<10^(−35), sup|wδ|<2·10^(−35).
At x2=1/4, |v(t,x)|>10^(−25) through time 1. BOTH flows remain smooth at time 1, so no singular trace is retained.

### Why this does not solve the actual problem

The direction of construction is reversed: this model sets Sδ first, then defines f_H8 and a smooth carrier. The true singular-source problem sets U_prep, its full projected residual f*=−P(∂t U_prep+div(U_prep⊗U_prep)−ΔU_prep)−Pdiv(ρR*), and then requires a compact symmetric stress H constrained by the original one-sided cone such that Pdiv(ρ E H E^T)=f*. The model gives no right inverse for that f*. Its uniform CtH4 contraction also **excludes** a terminal singularity rather than preserving one.

Next necessary gate: freeze the actual source, density, full physical frame and cutoff; test the *oriented* one-sided cone dual inequality (not an absolute-value symmetric surrogate), and test curl-flatness on the zero-density collar. Only then try a scale-sharp smooth inverse with one global pressure and a weighted terminal-subleading nonlinear correction. Missing these is an existence gap, not a minor omitted constant.

Local complete three-page PDF/LaTeX proof and exact-rational Python checker are available in the conversation as **Regular_Compact_Stress_Independent_Audit**. No formal Lean proof of this model or of unforced blowup is claimed. Maintain this as a draft research audit, separate from the clean manuscript.
