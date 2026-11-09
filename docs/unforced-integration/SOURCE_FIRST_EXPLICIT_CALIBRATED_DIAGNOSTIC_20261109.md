# Source-first full residual: one completely specified, torque-calibrated singular diagnostic

9 November 2026. **RELEASE STATUS: COUNTEREXAMPLE FOR THIS NEW DIAGNOSTIC SUPPORT CHOICE ONLY.** It is NOT an authentication or a no-go for the original analytic B.12/G1 core; it is NOT an unforced three-dimensional Navier–Stokes singularity solution.

## The prescribed data, fixed before any stress

On the periodic torus T³, t<1 and τ=1−t, set h=1/200, A=1/2+h, D=1/2−h, a=b=1/20, R=√τ, Z=τ^D, s=r/R, ξ=z/Z.

Let κ(v)=exp[−1/(1−v²)] on |v|<1, zero outside. Let σ(v) be the flat monotone step exp(−1/v²)/[exp(−1/v²)+exp(−1/(1−v)²)] on (0,1), zero below 0, one above 1. Put χ(s)=1−σ(8s−1), ζ(ξ)=1−σ(8|ξ|−1), ψ(s)=κ(64s−13),
c=(∫s³χ(s)ds)/(∫s³ψ(s)ds) (both integrals positive), B(s)=χ(s)−cψ(s).

Fix the full Cartesian vector potential and velocity
\[
 \mathcal A_\tau=\frac a2 τ^{-A} χ(s)ζ(ξ)(-x_2,x_1,0)
       -\frac b2 τ^{-A-1/2}r^2B(s)ζ(ξ)e_3,\quad
 u=\nabla\times\mathcal A_\tau.
\]
The spatial stress density, genuine proper orthogonal spatial frame and fixed baseline are
\[
 ρ=τ^{-1-h}κ(16s)κ(16ξ),\
 E=\mathrm{Rot}_{e_3}(τ^h\sin(2π z)),\
 R_0=b_0b_0^T-I/3,\quad b_0=(35,2,0)/\sqrt{1229}.
\]
These cutoffs/supports, parameters and nonconstant frame are defined *before* computing the source. The density has an open vacuum in the velocity's solid-rotation plateau.

The full unforced physical residual F=∂t u+(u·∇)u−Δu is given for all cutoffs by exact three-component cylindrical formulas in the standalone proof (conversation PDF/TeX). The preassigned projected source is
\[
 f_*=-\mathbb P[F+\nabla\cdot(ρ E R_0E^T)].
\]
The missing stress must satisfy \(\mathbb P\nabla\cdot(ρ E H E^T)=f_*\) with original one-sided seven-ray coefficient constraints. A single periodic pressure is determined by the unique zero-mean Poisson solution and cannot change solenoidal pairings.

## Three simultaneous tests on ONE source

Take W=κ(128(s−3/32))κ(16ξ), v=W(-x_2,x_1,0). Then v is smooth and divergence-free. Its support has 11/128<s<13/128, where ρ=0 identically but u=(-Ωx2,Ωx1,V), Ω=bτ^{-1-h}, V=aτ^{-A}. The FULL source there is exactly
\[
 F=(-\dot Ωx_2-Ω²x_1,\dot Ωx_1-Ω²x_2,\dot V),\qquad
 \nabla\times F=(0,0,2\dot Ω)\ne0.
\]
The prescribed source pairs as
\[
 \langle f_*,v\rangle=-\frac{201}{4000}\mathcal J τ^{49/100}<0,\
 \mathcal J=2π\int s³κ(128(s−3/32))ds\int κ(16ξ)dξ
 >36501/274877906944.
\]
Thus \(\langle f_*,-v\rangle>7336701/1099511627776000\ τ^{49/100}\); the one-sided cone dual support integral against -v is ZERO because ρ vanishes on the test support. Vacuum-annihilator compatibility, oriented cone duality and localized pressure-free toroidal torque all fail, simultaneously, for every 0<τ≤1. No arbitrary stress supported by ρ can solve this source, whether positive or not, with any periodic pressure.

Global axial angular momentum is already EXACTLY zero:
\(\int(x_1u_2-x_2u_1)dx=2\int \mathcal A_3 dx=0\),
by the exact counterrotating c. Thus this is not the trivial *global* angular-momentum failure. The velocity is smooth and divergence free for every t<1, has finite and decaying kinetic energy O(τ^(1/2−3h)), and has a central axial velocity aτ^(−A)→∞. It is a *prepared field*, NOT a solution.

## Proof integrity and limitations

The rational strict bound uses κ(v)>1/4 for |v|≤1/2, proved by a six-term rational upper Taylor bound e^(4/3)<4, the subintervals s∈[23/256,25/256], |ξ|≤1/32, and π>3. Exact SymPy checks verify the full local residual, curl, torque, divergence and similarity exponents. Nine independent exact-rational physical-coordinate checks compare all three full cylindrical residual components against their generic similarity formulas. A 65-digit independent integration found c≈5.33844925943 and J≈4.99972155090e−7, explicitly diagnostic only. The user-facing proof packet contains a 3-page scholarly PDF, editable TeX, both standalone verifiers and scope statement with SHA256 integrity checks.

**HARD SCIENTIFIC BOUNDARY:** this new, source-first singular preparation is NOT the authentic 2026 OpenAI nonlinear analytic core. It fails *inside* an artificial stress-vacuum annulus because its local field has nonzero unforced-residual curl. An **exact** local unforced G1 field would have zero residual curl in its actual core, so this no-go cannot be transferred to the original localization without computing that authentic shell source.

The next genuine milestone is to freeze an authenticated source-admissible original axis/fixed-point solution, a concrete physical localization vector potential, the true matching density/frame and pressure gauge, and then run this source-first collar/cone/toroidal test in the actual attachment shell. The original forced OpenAI theorem, proposed local G1 theorem, H8 source right inverse, nonlinear pressure closure, terminal retention and global unforced Navier–Stokes solution remain mathematically distinct. Keep this PR DRAFT.