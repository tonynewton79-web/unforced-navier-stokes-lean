# Edition XXXI — actual OpenAI Section 10 Fourier shell and correction upper bound

**Mathematical status:** source-derived symbolic shell witness and an independent exact correction stability estimate. The numerical source parameters and the singularity-preserving retention inequality have NOT been certified. Complete unforced Navier–Stokes singularity and its full Lean PDE proof remain OPEN.

## Source authentication

Read the original 166-page OpenAI *Finite Time Blowup for Navier–Stokes* PDF (2026), specifically Proposition 10.1, eqs. (10.4), (10.5), and the late-time swirl (10.21).
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

The actual localized physical field is u_B=curl(c A)+c B e_theta, where c and B are axisymmetric, with r<r0 and |z|<z0 on support. This gives exact spatial mean zero: the compact curl integrates to zero; the azimuthal unit vector integrates to zero over theta. For bounding purposes V=2 pi r0² z0 and R=sqrt(r0²+z0²).

## Quantitative authenticated shell-existence bound

At a fixed t<1 with m=||u_B(t)||_2>0, G=||grad u_B(t)||_2 finite, define

L=(5 pi²/(4 R² V))^(1/5); H=max(2L,4G/m); N=ceil(log2(H/L)); K_j=2^jL.

At least one of these N dyadic shells has b_Kj(t) >= m sqrt(13/(16N)) > 0.

The source gives nonzero m at late times through its e0>0 swirl asymptotic (10.21). For small tau, putting J=e0*tau^(-1/2-h)/2 and D=||grad u_B(1-tau)||_infty, the independent Lipschitz-ball estimate gives m(1-tau)>= (J/2)*sqrt(4pi/3)*(J/(2D))^(3/2).

Proof: mean zero and first moment yield low-frequency mass squared <=m²/8; H1 control yields high frequency <=m²/16; pigeonhole gives >=13m²/(16N).

**This does not identify a numerical K or numerical shell lower bound** because the source paper does not freeze numeric r0,z0,e0,D,G at a specified time, and the implementation has not independently reconstructed the complete profile.

## Independent correction estimate using the actual complete source

For an unforced comparison solution u=u_B+w, with x=||w0||_2, f_B the *full* Section 10 physical force, U=sup||u_B||_2, A=integral||grad u_B||_infty, F=integral||P f_B||_2, W=exp(A)(x+F), a_K=exp(-nu K²t), c_K=sqrt(K)/(sqrt(2)pi nu) and F_K=integral exp(-nu K²(t-s)) ||B_K P f_B(s)||_2 ds,

sup||w||_2 <= W,
delta_K=||B_Kw(t)||_2 <= a_K*x+F_K+c_K*(2U W+W²).

Combined with Edition XXX:
b_K <= 2a_K*x+c_K*x²+F_K+c_K*(2U W+W²).

This bound is independently proved by Gronwall for the exact difference equation and unitary Fourier Duhamel, with zero claim of a small correction.

## Conditional rejection and its unresolved gate

A quantitative lower bound on nonzero initial data arises if, separately, a singularity-preserving correction is shown to retain at least 1-kappa of the selected source shell:
delta_Kj <= kappa b_Kj, 0<=kappa<1.
Then x>= min_j 2(1-kappa)B/[a_Kj+sqrt(a_Kj²+4c_Kj(1-kappa)B)] with B=m sqrt(13/(16N)).
Neither the original paper nor the source-specific current GitHub run has established this retention inequality, so NO numerical initial-data rejection or admission can be announced.

In particular x=0, u=0, w=-u_B satisfies the exact unforced PDE and all unconditional bounds, but cancels the singular flow; any unconditional claim otherwise would be false.

## Verified finite computations and Lean limit

- Independent SymPy integrals: exact constants 1/8, 1/16, 13/16 and 4pi K.
- Independent Fourier-correction quadratic consistency and angular mean-zero.
- 25,000 exact rational energy partitions in each checker; independent exact forced-ramp vs unforced heat shear.
- Three-page scholarly PDF proof created and inspected.
- Lean file N1SourceShellEnergyScalar.lean includes finite partition and retention inequalities ONLY, not actual PDE; kernel CI queued/unverified.
- Unforced physical residual, correction spectrum and all-harmonic singularity persistence remain unproved. This gate is explicitly fail-closed.

**Next target:** extract a reproducible numerical profile/parameter tuple, obtain certified bounds on actual r0,z0,e0,D,G, project the full Section 10 cutoff residual, and independently prove a shell-retention bound for one nonzero initial-data correction. Without these, the conditions cannot discriminate any concrete source-backed budget.