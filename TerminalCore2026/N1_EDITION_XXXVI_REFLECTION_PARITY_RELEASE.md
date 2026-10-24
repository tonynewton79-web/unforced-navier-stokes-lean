# Edition XXXVI — reflection parity obstruction in the nonaxisymmetric route

24 October 2026. Tony Newton / Newton Astro Labs. **Exact classical symmetry application and a concrete global unforced negative control; desired nonaxisymmetric finite-time singularity remains OPEN.**

## Actual source and exact theorem scope

OpenAI's 2026 *Finite Time Blowup for Navier–Stokes* is a forced-NS construction, not an unforced one. The original Section 10 asymptotic is positive along x_tau=(sqrt(2 X_in tau),0,0), i.e. theta=0:
u_B,theta(x_tau,1-tau)=(e0+o(1))tau^(-1/2-h), e0>0.

Reflect across y=0 with R=diag(1,-1,1) and (Script R u)(x,y,z)=R u(x,-y,z). Any smooth unforced solution whose initial data is reflection invariant remains invariant by classical smooth uniqueness. At theta=0 the physical u_theta=u_y=0 exactly, so that solution cannot retain the published positive swirl, regardless of how large the initial data is. Gamma=r*u_theta is odd in theta; u_r,u_z are even; their angular covariances with Gamma vanish and the averaged torque T of Edition XXXV vanishes exactly. This is a **discrete parity obstruction** in addition to the existing continuous-axisymmetry obstruction. It is not a new global regularity theorem.

## Exact parity-odd PDE

Write u^+=(u+Script R u)/2 and u^-=(u-Script R u)/2.
For an exactly unforced smooth solution, the parity-odd part obeys

  ∂t u^- -nu Δu^- +P[(u^+·∇)u^-+(u^-·∇)u^+]=0.

By taking L² energy and Gronwall,
||u^-(t)||₂<=q exp(J(t)), q=||u^-(0)||₂,
J(t)=∫_0^t||∇u^+(s)||∞ ds.
At the source plane y=0, u_y=(u^-)_y. Thus any retained u_theta(x_tau,1-tau)≥c tau^-A with A=1/2+h forces q>0 and

  ||∇u^-(1-tau)||∞ ≥ [pi c^5/(24 q² exp(2J))]^(1/3) tau^(-5A/3),

  ||Δu^-(1-tau)||₂ ≥ [c/(C2 q^(1/4) exp(J/4))]^(4/3) tau^(-4A/3),

C2=4/(pi sqrt(2) 3^(7/8)). A sufficiently large parity-even strain integral J can weaken these conditions. No positive lower bound on growth from initial parity breaking alone is claimed.

## Explicit large critical norm, genuinely nonaxisymmetric, globally regular negative control

v0(x,y,z)=2nu exp(-[(x-1)^2+y²+z²])*((x-1)z,yz,1-(x-1)^2-y²).

Exactly divergence free and reflection symmetric. It is axisymmetric-no-swirl about the **displaced** axis x=1,y=0, but genuinely nonaxisymmetric relative to the source axis x=y=0. Its critical ratio C_F||v0||_X^-1/nu=sqrt(pi)/2>1/16, unchanged by translation, and classical no-swirl global existence supplies a smooth exactly unforced whole-space solution.

Relative to the original z-axis, its initial azimuthal angular momentum is
Gamma_0=2nu*r*z exp[-(r²+1-2r cos(theta)+z²)]sin(theta).
At (r,z,theta)=(1,1,pi/2) this equals 2nu exp(-3)>0,
hence ||∂theta Gamma_0(1,.,1)||_2≥2nu exp(-3)sqrt(6/pi)>0.

Nevertheless Gamma_0 is odd in theta, its mean and radial/axial covariance torque vanish, and this reflection parity persists in the global zero-force evolution. Along theta=0, v_theta=0 identically, so its correction to OpenAI's forced background cancels the particular proposed singular swirl.

## Independent validation and limitations

Two distinct exact SymPy derivations (Cartesian divergence, displaced Gamma, reflection parities, nonlinear odd-component equation) passed. An independent 20,000 seeded exact-rational check exercised the fifth-power interpolation budget. Source field numerical cutoff/profile and authenticated A.11/A.19 residual still missing; original source is forced. Dedicated finite Lean scalar file and CI workflow committed, **not** a kernel proof of parity invariance or the PDE. Lean CI success must be checked; until then status is QUEUED/UNVERIFIED.

**Genuinely open next step:** Construct an exact unforced solution with nonzero reflection-odd initial component and source-compatible projected residual cancellation, quantify its parity-odd strain and pointwise growth on the collapsing source trajectory, and certify its finite-time singularity. That would still be a solution of an outstanding major open problem; it has NOT been achieved here.

Source grounding: OpenAI's main README https://github.com/openai/NavierStokesAndEuler/blob/main/README.md confirms that its Navier–Stokes theorem allows forcing, while its unforced singularity is for Euler.
