# Proof Attack 10 — Edition XV | 23 October 2026

STATUS: PASS_EXACT_MODEL_CONDITIONAL_SOURCE — NO UNFORCED BLOWUP PROOF.

From source Section 4, the characteristic inner exponents are
A=1/2+h, D=1/2-h, q=tau Q(Z), Q-Z^2 Q^(2h)=1.
For a fixed rescaled swirl profile U(R,Z) with some genuinely
nonzero third radial Cartesian derivative on a compact source chart,
the exact Jacobian tau^(1+D) gives
  ||uB(t)||H3 >= C_* tau^(-alpha),
  alpha = A+3/2-(1+D)/2 = 5/4+3h/2.
The derivative-nondegeneracy and agreement of the actual globally
corrected source with this profile are REQUIRED assumptions.
Neither has yet been authenticated for a frozen source instance.

Edition XIV's fixed-fraction contraction test T=theta*tau
therefore has a strictly positive background term growing as
tau^(-3/4-3h/2). Its sufficient smallness gate eventually fails
under the above assumption, irrespective of projected-residual F.
This is a failure of THAT sufficient gate, not a nonexistence theorem.
A variable step T~tau^p needs p>5/2+3h to make that background term
tend to zero (at equality coefficient smallness must be checked).

Exact globally smooth for t<1, divergence-free gaussian vortex
u=tau^(-A)(-Y,X,0) exp[-(X^2+Y^2+Z^2)] has
||d_x^3 u_y||2²=(105/4)(pi/2)^(3/2) tau^(-2alpha).
The full UNPROJECTED Gaussian residual (p=0) has radial
centrifugal component with third radial derivative
||d_x^3 R_x||2²=105(pi/4)^(3/2) tau^(-2beta),
beta=9/4+5h/2. This DOES NOT determine the authentic source's
Leray-projected residual beta or full source H3 constants.

Independent SymPy moment algebra, Jacobian/exponent replay,
and 10000/10000 exact rational h checks PASS.
GitHub Lean file N1TerminalH3ScalingScalar.lean is scalar-only;
Lean kernel CI is not a full functional/PDE formalization and
a completed kernel PASS must be independently checked.

HOLD: prove an explicit nonzero C_* for ONE authenticated source
and its later corrections; interval-certify full projected
H3 residual, pressure, cutoff transitions and matching; prove
a weighted force-free nonlinear correction retaining singularity;
nonzero smooth physical initial data; all-order convergence; and
complete Lean PDE theorem.

The source paper proves forced (not unforced) finite-time blowup.
The unforced 3D NSE regularity problem remains OPEN.

Cumulative GitHub LaTeX updated; Edition XV companion PDF is
a 31-page cumulative research addendum (new 2-page note + previous
29-page Edition XIV), not a newly compiled full master paper.
