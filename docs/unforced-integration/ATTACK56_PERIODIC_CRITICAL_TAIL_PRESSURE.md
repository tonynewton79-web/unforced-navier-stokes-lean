# Attack 56 — nonaxisymmetric time-periodic critical-tail trial with exact nonlinear pressure

**21 November 2026.** This is a reproducible *genuine PDE candidate audit*. **Not an exact unforced Navier–Stokes similarity profile; not an inverse certificate; not a final Lean proof.**

## Actual backward unforced Leray system

∂s W + 1/2(W+y·∇W) − ΔW + (W·∇)W + ∇q = 0,  div W=0.

Set R=|y|, H=1+R², and four globally smooth solenoidal modes:

    S0_B = (B×y)/H
    P0_C = ((2+R²)C+(C·y)y)/H^(3/2)
    S1_B = (B×y)/H²
    P1_C = ((2−R²)C+3(C·y)y)/H^(5/2).

P0 and P1 are curls of (C×y)H^-1/2 and (C×y)H^-3/2. S0,P0 decay 1/R; S1,P1 decay 1/R³.

### Critical-tail phase rigidity

For a genuine solution with |∇^j W|≤C(1+R)^(-1-j), j≤2 and |∇q|≤C(1+R)^-3, the actual PDE characteristic transport yields a(s,ω)=lim_(r→∞)rW(s,rω) **independent of s whenever this limit exists**.

For the modes above a=B0(s)×ω +C0(s)+(C0(s)·ω)ω. Its sphere means recover C0=(3/4)mean(a) and B0=(3/2)mean(ω×a). Hence B0,C0 must be constant. Do NOT rotate the leading 1/R tail.

### Fixed-tail, nonaxisymmetric periodic ansatz

    B0=e1, C0=e3, B1(s)=eps(cos(s)e2+sin(s)e3),
    W=S0_B0+P0_C0+S1_B1(s)+P1_C1(s).

This is smooth, solenoidal, periodic (P=2π, identity twist), nonaxisymmetric, and has the fixed nonzero critical tail a(e3)=−e2+2e3 of norm sqrt(5).

### Fully compatible nonlinear pressure

At each similarity time determine q uniquely (modulo a constant) by the actual Poisson equation

    -Δq = Σ_i,j (∂iWj)(∂jWi) = source,
    q(y)=∫source(z)/(4π|y-z|) dz.

Because the source angular degree is at most 6, this is **exactly** a finite spherical harmonic reconstruction:

    q(rω)=Σ_(ell=0)^6 Σ_(m=-ell)^ell q_ell,m(r) Y_ell,m(ω)
    q_ell,m(r)=1/(2ell+1)*
      [r^(-ell-1)∫_0^r ρ^(ell+2)src_ell,m(ρ)dρ
       +r^ell∫_r^∞ ρ^(1-ell)src_ell,m(ρ)dρ].

No finite-box artificial pressure boundary condition is used.

**Exact symbolic cross-pressure table:** For the mixed source of Si_B+Pj_C, i,j∈{0,1},

    source_ij^mix = g_ij(R) (B×C)·y,

    g00=-10/H^(7/2),
    g01=6(2R²−5)/H^(9/2),
    g10=2(2R²−5)/H^(9/2),
    g11=6(4R²−5)/H^(11/2).

Thus pressure gradient at origin is γij B×C with

    γ = [[-2/3,-6/5],[-2/5,-6/7]].

In particular the exact nonparallel critical-core pressure contribution is

    q00^mix=−(2/3)(B×C)·y/H^(3/2).

All four source identities and the beta integrals were checked by *independent exact SymPy* (no numerics).

### Theorem — unique periodic solution of exact centre compatibility

The full physical momentum residual **at y=0**, with its pressure included, is

    N(W,q)(s,0) =
       2 C1' + 11 C0 +31 C1
       +(4/3) B0×C0 +(4/5) B0×C1
       +(8/5) B1×C0 +(8/7) B1×C1.

Setting this to zero gives the linear time-periodic ODE

    2 C1' +[31 I+(4/5)[B0]_×+(8/7)[B1(s)]_×] C1
      = -11 C0-(4/3)B0×C0-(8/5)B1(s)×C0.

For any periodic continuous B1 the period-return map is an affine strict contraction: differences satisfy d/ds |d|²=−31|d|². Hence exactly **one periodic C1** makes the full momentum equation hold at the origin at every s. This centre-only theorem is **not** a solution on all of R³.

### Numerical physical-residual diagnostic (not interval certified)

Selected ε≈0.27666504 via a local one-parameter search with |B0|=|C0|=1 fixed. The centre equation has residual about 5e−16 in floating-point. The pressure multipole integrals reproduce the exact nonparallel-core closed formula at 3 points within 1.4e−15.

The *complete unforced Leray residual* computed with pressure harmonic quadrature at s=0 has norms:

    y=(1,0,0)             0.855321
    y=(0.5,0.4,0.8)       2.152410
    y=(0.2,-0.6,0.3)      1.609325

Over those 3 points and similarity times {0,1.3}, sampled RMS≈1.637004. This is a **finite-sample numerical diagnostic only** and provides neither a rigorous continuum norm nor a verified minimum. The residual is conspicuously nonzero.

### Theorem — unrestricted inverse is structurally impossible

For an **exact nonstationary periodic** solution W, differentiating the entire PDE gives

    L_W (∂sW) =0

with the derivative of pressure included. Thus the unrestricted periodic linearization L_W is not injective: it has a time-phase neutral mode. Ordinary-periodic profiles may also have rotational neutral modes Z_Ω=ΩW−(Ωy)·∇W. Fixing the leading tail can exclude rotations that change the tail, **but not ∂sW**, which is subleading. A *phase-pinned / bordered* linear operator, not the unrestricted L_W, is the correct candidate for an inverse estimate.

The contraction criterion 4M²Kδ<1 is appropriate **only after** M is a proved inverse norm for the correctly bordered operator, K is the bilinear bound, δ is the full continuum residual norm, and the correction preserves nonzero tail or another nontriviality lower bound. None has been certified here.

### Release gates and external source

PASSED: exact analytic solenoidality, critical-tail rigidity, cross-pressure algebra, centre ODE existence/uniqueness, exact Poisson harmonic representation, independent symbolic verification and numerical pressure benchmark.

NOT PASSED: exact global PDE, rigorous whole-domain δ, full bordered inverse M, bilinear K, 4M²Kδ<1, corrected nonzero profile, all 15 external CellSystemCondition fields, Lean continuum proof, third-party specialist review.

Alpöge–Buckmaster public 20 November 2026 repository (https://github.com/tristanbuckmaster/navier-stokes), checked on 21 November, still lacks the claimed data/validator; its Lean theorem is conditional. No novelty or millennium resolution is claimed. The associated 5-page PDF, LaTeX and full reproducible numerical scripts are available in the originating research session.
