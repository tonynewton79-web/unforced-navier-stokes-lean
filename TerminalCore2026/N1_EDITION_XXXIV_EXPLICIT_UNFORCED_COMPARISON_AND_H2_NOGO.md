# Edition XXXIV — explicit nonzero-data whole-space unforced comparison, and why the requested H² upper bound fails for it

24 October 2026. Tony Newton / Newton Astro Labs. Status: **EXACT ZERO-FORCE COMPARISON PROVED; SINGULARITY RETENTION FAILS; FULL UNFORCED BLOWUP UNPROVED**.

## Source
OpenAI, *Finite Time Blowup for Navier–Stokes*, 2026, Theorem 1.1, Section 10 (10.5), (10.20)–(10.21):
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

The source u_B is a smooth compactly supported **forced** flow for each t<1, with uniformly bounded L² and azimuthal amplitude tau^(-A)(e0+O(tau^(2h))) at its shrinking core, A=1/2+h, e0>0, 0<h<1/100.

## Explicit nonzero datum in the actual R³ geometry
Choose any viscosity nu>0 and set

v0(x,y,z)=nu/(100*pi)*(-2*y*exp(-r²),2*x*exp(-r²),0), r²=x²+y²+z².

This is nonzero, Schwartz, exactly divergence-free, finite energy, and has norm
||v0||_2=nu/[100*(2*pi)^(1/4)].

Using the unitary Fourier transform and C_F=(2*pi)^(-3/2), the critical norms of the underlying vortex phi are

||phi||_X^-1=pi^(5/2)/sqrt(2), ||phi||_X^0=2*sqrt(2)*pi²,
||phi||_2²=2*(pi/2)^(3/2).

Thus C_F||v0||_X^-1/nu=1/400. The global mild Banach norm
sup_t||v||_X^-1 + nu*integral||v||_X^1 admits a closed ball of radius 4 X0
and the Fourier Navier–Stokes mild map has Lipschitz constant <=1/25.
The resulting global solution v is smooth and satisfies the exact whole-space **unforced** PDE with the true pressure
p_v = sum_{i,j} R_i R_j(v_i v_j).
No force is omitted or hidden in the scalar pressure.

Explicit universal bound:
sup_{t>=0}||v(t)||_infty <= nu * exp(1/50)/(100 sqrt(pi)).

## Genuine uniform H² upper bound for v and two-sided bound for w
The ordered Sobolev derivative energy (3 first derivatives + 9 ordered second derivatives) gives
(1/2)d||v||_H²²/dt <=30||grad v||_infty||v||_H²².
Since the critical Fourier iteration supplies
integral||grad v||_infty <= 1/100 and the Gaussian initial squared norms have coefficients 2+10+70=82,

sup_t||v(t)||_H² <= C_H,nu :=
nu*sqrt(82)/(100*pi)*(pi/2)^(3/4)*exp(3/10).

For the specific correction w=v-u_B,
max(0,||Delta u_B||_2-C_H,nu) <= ||Delta w||_2 <= ||Delta u_B||_2+C_H,nu.

This is a genuine **upper** bound on the requested norm for a specified exact zero-force correction, but it is NOT the desired little-o bound.

## Sharp asymptotic obstruction from source growth
By the source (10.21) and bounded v, for small tau,
|w_theta(x_tau,1-tau)| >= e0*tau^(-A)/4.

Since ||w(t)||_2 <= M := ||v0||_2+sup_t||u_B(t)||_2, and the explicit H² Fourier interpolation constant is C2=4/(pi sqrt(2) 3^(7/8)),

||Delta w(1-tau)||_2 >= [e0/(4*C2*M^(1/4))]^(4/3) tau^(-4*A/3).

Its squared time integral diverges: 8A/3 > 1.
Because ||Delta u_B||_2 also diverges, the two-sided estimate yields
||Delta w(t)||_2/||Delta u_B(t)||_2 -> 1 as t->1.

Thus this exact **nonzero-data, zero-force** correction cancels the source blowup and inherits its full leading H² divergence. It cannot satisfy o(tau^(-4A/3)), as anticipated by the shrinking-core criterion. This is an adversarial negative control, NOT a proof that every special correction fails.

## Verification
Two independent exact SymPy/Gaussian checks verified critical Fourier integrals, small-data contraction margin, the exact Gaussian Sobolev 2:10:70 norms, 80,000 seeded rational numerical/algebraic checks, and the time-integrability threshold.
Standalone LaTeX/PDF prepared and visually checked, with SHA-256 manifest for the release packet.
Finite Lean scalar rational comparisons in N1GaussianUnforcedScalar.lean are NOT a kernel-checked proof of the PDE, and GitHub CI must report success before any claim of their formal compilation.

The complete actual source profile and cutoff numerical hashes are still missing, as recorded in FULL_UNFORCED_SOURCE_CERTIFICATE_REQUIRED_20261022.json.
The requested singularity-preserving nonzero-data unforced correction would solve an outstanding Navier–Stokes regularity question, and **remains unproved**.

## Research next gate
Any candidate construction must exploit a nontrivial dynamical mechanism beyond choosing an unforced comparison solution. The source-matched correction must satisfy its full projected equation AND gain a pointwise, high-frequency, or H² upper bound preventing core cancellation. The Gaussian comparison is a concrete benchmark rejecting proof claims based on initial data, Fourier energy, or a formal zero-force identity alone.
