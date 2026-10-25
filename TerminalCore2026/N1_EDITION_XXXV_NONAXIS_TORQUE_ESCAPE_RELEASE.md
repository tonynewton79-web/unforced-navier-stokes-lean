# Edition XXXV — large-data control and a sharp nonaxisymmetric transport-or-oscillation gate

24 October 2026. Tony Newton / Newton Astro Labs. Part of the cumulative unforced 3D Navier–Stokes research programme.

## Main mathematical advance

The existing Edition XXII circulation maximum principle already rules out an axisymmetric unforced solution with bounded initial r*u_theta that preserves OpenAI's particular growing forced swirl u_B,theta ~ e0*tau^(-1/2-h) at r_tau=sqrt(2 X_in tau), h>0. Edition XXXV does **not** claim this known obstruction is new.

The new explicit *large data* no-swirl test is
v0(x,y,z)=2*nu*exp(-(x*x+y*y+z*z))*(x*z,y*z,1-x*x-y*y).
It is a nonzero Schwartz divergence-free axisymmetric no-swirl field.
The exact unitary Fourier critical norm is sqrt(2)*pi²*nu.
Its dimensionless ratio C_F*||v0||_{X^-1}/nu=sqrt(pi)/2=0.886226925..., well beyond the self-contained 1/16 small-data contraction threshold of Edition XXXIV. Classical Ladyzhenskaya / Ukhovskii--Yudovich no-swirl theory nevertheless gives a smooth globally regular exactly unforced R³ solution for every nu>0. For the published viscosity-one source choose nu=1.

The azimuthal vorticity ratio is omega_theta/r=2*nu*(5-2*rho²)*exp(-rho²), with initial L-infinity value 10*nu, and satisfies a classical transported-diffused lifted equation. This solution has v_theta identically zero, so w=v-u_B has w_theta=-u_B,theta at all times and cancels the source swirl EXACTLY. No nonzero-data blowup has been obtained.

### New exact nonaxisymmetric Reynolds angular-momentum identity

For a smooth unforced solution u, Gamma=r*u_theta, bar for angular mean, prime for fluctuation,
(∂t+bar(u_r)∂r+bar(u_z)∂z)bar(Gamma)
 =nu(∂rr-r^-1∂r+∂zz)bar(Gamma)+T,
T= -r^-1∂r(r * overline(u_r' Gamma'))-∂z overline(u_z' Gamma').
No angular pressure term survives the exact average; no viscous nonaxisym cross term survives angular averaging.

The sharp zero-mean periodic angular H¹ trace inequality has constant sqrt(pi/6).

For an unforced flow retaining u_theta(r_tau,theta=0,z_tau,1-tau)>=(e0/4)tau^(-1/2-h),
the exact necessary budget is

integral_0^(1-tau)||T(s)||_infty ds
+sqrt(pi/6)||∂theta Gamma(r_tau,.,z_tau,1-tau)||_{L²theta}
 >= (sqrt(2 X_in)*e0/4)*tau^(-h) - ||bar(Gamma)(0)||_infty.

Therefore both terms cannot simultaneously be little-o(tau^-h). This is a **necessary escape dichotomy**. It does not prove the terms can be produced by any singularity-preserving unforced solution.

### Positive kinematic example (not a PDE solution)

Take on an annular plateau A_z=r cos(theta)+r³ sin(theta)=x+(x²+y²)y, extended by smooth spatial cutoffs, and u=curl(A_z e_z). Exactly div u=0, angular mean Gamma=0,
overline(u_r' Gamma')=r³ and T=-4r². Thus the Reynolds angular momentum flux is not structurally forced to vanish by incompressibility. The field is not claimed to solve time-dependent Navier–Stokes or provide a divergent torque.

## Verification

- Two independent symbolic derivations: Cartesian solenoidality, zero swirl, theta vorticity, exact Fourier critical integral, normalized amplitude ratio, annular Reynolds flux, and sharp angular H¹ trace constant.
- 15,000 exact Fraction large-data/flux fixtures and 25,000 independent angular-dichotomy fixtures; PASS locally.
- A finite Lean 4/Mathlib scalar module and dedicated GitHub CI workflow committed, but no kernel success claimed until runner completion.
- Original source parameters, spatial cutoffs, complete corrected physical residual, nonlinear nonaxisymmetric singularity construction and full end-to-end Lean PDE proof remain OPEN / FAIL-CLOSED.

## Definitive next gate

Produce a concrete nonaxisymmetric zero-force solution candidate and rigorously source-matched estimates for both (a) time-integrated Reynolds angular momentum transport T and (b) angular variation ∂theta Gamma on the shrinking circle. At least one must attain order tau^-h for the published-source swirl to survive. Achieving this alone would remain necessary, NOT sufficient, for a full unforced blowup theorem.

Source: OpenAI (2026), *Finite Time Blowup for Navier-Stokes*, Section 10 (forced); Gallay and Šverák (2015), *Remarks on the Cauchy problem for the axisymmetric Navier--Stokes equations*, no-swirl global result (established prior art).
