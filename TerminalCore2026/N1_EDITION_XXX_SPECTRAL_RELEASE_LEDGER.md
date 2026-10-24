# Edition XXX — source-facing Fourier shell necessary condition

**24 October 2026.** Theorems and independent exact finite replays verified. No proof of unforced 3D Navier--Stokes blowup or full Lean theorem.

## True source

OpenAI, *Finite Time Blowup for Navier--Stokes*, Section 10, equations (10.4)-(10.5), in the 166-page published PDF: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf. The actual background u_B is cutoff to vanish for an initial time interval, and the physical forcing f_B is the full residual defined *after* cutoffs. The authored source has forcing; OpenAI's separate unforced singularity theorem is for Euler. The precise source profile and a full reproduced 3D residual have not been frozen/hashed in this repo.

## Mathematically proved source-independent necessary inequalities

On the 2π three-torus with normalized measure for every nonzero integer k, a smooth unforced flow satisfies

    |u_hat_k(t)| <= exp(-nu |k|²t)|u_hat_k(0)|
                    + E0*(1-exp(-nu|k|²t))/(nu|k|),

where E0=||u0||². With *mean-zero* initial velocity, Poincare adds the sharper nonlinear convolution kernel G_k(t)=|k|(exp(-2nu t)-exp(-nu|k|²t))/(nu(|k|²-2)), including the resonant value |k|t exp(-2nu t) at |k|²=2.

In actual whole space R³ a pointwise Fourier value **cannot** be bounded by total L² energy. Use the dyadic shell B_K, K<=|xi|<=2K. For u=u_B+w, u_B(0)=0, x=||w0||₂, R_t=integral||P residual||₂, b_K=||B_K u_B(t)||₂, delta_K=||B_K w(t)||₂,

    (b_K-delta_K)_+ <= exp(-nu K²t)*x
                      + sqrt(K)/(sqrt(2)*pi*nu)*(x+R_t)² + R_t.

For exactly unforced R_t=0 and h=(b_K-delta_K)_+>0, the necessary nonzero initial norm is

    x >= 2h/(a+sqrt(a²+4ch)),
    a=exp(-nu K²t), c=sqrt(K)/(sqrt(2)*pi*nu).

This is a **necessary** bound, not an existence theorem, proof of source compatibility, or blowup obstruction. The shell coefficient sqrt(K)/(sqrt(2)*pi*nu) grows with high frequency, making the bound too weak on its own to exclude energy-concentrating blowup.

## Verification

- Exact SymPy convolution integrals at mode lengths squared 1,2,3,4,5,8,9,16; includes resonance |k|²=2.
- Exact unforced heat shear and forced ramp-shear negative controls.
- Exact three-dimensional *unitary* Fourier annulus integral 4*pi*K and scalar constant.
- 40,000 seeded exact Fraction Cauchy and budget cases.
- Independent 1,200 divergence-free finite Fourier fields at four wavevectors, each using the exact Leray-projected quadratic convolution: 4,800 tests.
- Two-page LaTeX proof compiled, rendered and visually inspected, included in a hash-verified reproducibility archive.
- Finite Lean scalar lemmas and a pinned CI workflow committed. Lean kernel pass has not yet been verified; no actual PDE Fourier energy formalization is claimed.

## Missing physical and formal inputs — DO NOT PROMOTE

Actual source profile SHA256, source spectral shell b_K(t), correction spectral shell delta_K(t), nonzero smooth initial velocity x, exact projected zero-force physical PDE residual, nonlinear all-frequency convergence and singularity inheritance, and a complete Lean proof are all unavailable/unverified. The proper output remains **HOLD**.

Next target: authentically reconstruct the Section 10 source, freeze its profile/time derivative data and compute a rigorously lower-bounded shell b_K(t) for a source-backed K and time, then prove a *separate* upper bound on delta_K(t) for a singularity-preserving correction with an admissible x. Until these inputs are certified there is no full unforced Navier--Stokes theorem.
