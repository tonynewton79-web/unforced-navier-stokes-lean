# Edition XXXIII: shrinking-core gradient and frequency cancellation gate

24 October 2026 — Tony Newton, Newton Astro Labs.

## Source-specific inputs authenticated
OpenAI, *Finite Time Blowup for Navier--Stokes*, source PDF:
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
Section 10, (10.20)--(10.21), proves source growth
u_B,theta(x_tau,1-tau)=tau^(-A)(e0+O(tau^(2h))) with A=1/2+h,
0<h<1/100 and e0>0, along x_tau=(sqrt(2 X_in tau),0,0).
The same source theorem bounds B=sup_t ||u_B(t)||_2<infinity.

## Exact new source-targeted mathematical gate
Let u be any smooth finite-energy exactly unforced comparison flow on [0,1),
with ||u0||_2=x, w=u-u_B, M=x+B. By the unforced energy inequality,
||w(t)||_2 <= M.

If |u_theta(x_tau,1-tau)| <= (e0/4)tau^(-A), then necessarily
  ||grad w(1-tau)||_infty >= [(pi/24)*(e0/4)^5/M^2]^(1/3) tau^(-5A/3),
  ||Delta w(1-tau)||_2   >= [e0/(4 C2 M^(1/4))]^(4/3) tau^(-4A/3),
where C2=4/(pi sqrt(2) 3^(7/8)).
These are *both* necessary if the stated norms are finite.

The sharp elementary ball estimate is ||v||_infty^5 <=
(24/pi)||v||_2^2||grad v||_infty^3.
A constructive admissible H² interpolation constant, proved by exact
unitary Fourier splitting and optimization, is
||v||_infty <= C2||v||_2^(1/4)||Delta v||_2^(3/4).

## Moving high-frequency dichotomy
Set K_tau=[pi sqrt(6)e0/(8M)]^(2/3) tau^(-2A/3).
The unitary Fourier low-frequency inequality gives
||P_<=K_tau w||_infty <= (e0/8) tau^(-A).
Consequently a correction which cancels the source core must satisfy
|(P_>K_tau w)(x_tau,1-tau)| >= (e0/8) tau^(-A).
If the high-frequency tail is o(tau^(-A)), the completed flow retains
the source's unbounded pointwise velocity.
The frequency growth exponent is 2A/3=1/3+2h/3<1/2.
This is strictly below the characteristic inverse source radial
similarity scale tau^(-1/2). It is NOT a theorem that the source
Fourier transform has compact support at that radial scale.

## Independent exact verification and limits
Exact SymPy low/high Fourier radial integrals, optimized constant,
the pi/24 ball bound, and moving K_tau were checked.
A separate divergence-free Gaussian field yielded exact
||v||_2²=2(pi/2)^(3/2) and ||Delta v||_2²=70(pi/2)^(3/2),
which independently satisfies the bound.
30,000 rational arithmetic gap-control cases passed.

These inequalities do **not** contradict the trivial unforced
solution u=0 and w=-u_B: its correction may have all requisite
high frequencies and derivative growth. No actual nonzero-data
singularity-preserving unforced correction is constructed.
Full Lean Navier--Stokes PDE certification remains OPEN.
Finite scalar Lean lemmas are committed but must not be declared
kernel checked until the correct GitHub CI run finishes.
Actual source numerical cutoffs/profile are not frozen: status remains
FAIL_CLOSED_MISSING_SOURCE_DATA.

## Next proof target
Construct a *specific* zero-force, nonzero-initial-data correction
with global energy and an upper bound of order
o(tau^(-4A/3)) for ||Delta w(1-tau)||_2,
or a high-frequency tail bound o(tau^(-A)) at x_tau.
Such estimates would ensure singularity inheritance, but
obtaining them under the exact forced-source cancellation
equation is still an open and potentially impossible step.
