# Edition XXXIX — one-flow exact cylinder and dyadic angular-momentum budgets

25 October 2026 | Tony Newton | Newton Astro Labs

**ANALYTIC CONSERVATION AND ENERGY BOUNDS: PROVED.**
**POSITIVE NONLINEAR TERMINAL CASCADE: NOT PROVED.**
**UNFORCED 3D NSE FINITE-TIME BLOWUP AND FULL LEAN PDE PROOF: OPEN.**

## Exact physical angular-momentum balance
For any smooth, finite-energy, exactly unforced three-dimensional NSE flow, Gamma=r*u_theta, angular means bar, and axial eta(z):
d/dt M_{R,eta}=-F_adv-F_visc+F_axial+F_sweep.
The four terms and full derivation are specified in
N1_Moving_Cylinder_Dyadic_Transfer_Edition_XXXIX_20261025_Insert.tex.
Pressure's direct angular derivative disappears on full revolution,
but the velocity still depends on pressure.

## New quantitative constraints
Let R_j=2^-j R0 and E0=||u(0)||_2². The complete nonlinear
radial flux through the annular *band average* satisfies
sum_{j>=0} integral_0^T integral_{R_{j+1}}^{R_j}
|F_adv(r,t)| dr/r dt <= T||eta||_infinity E0/2.
This gives an l1 budget across all dyadic radii and excludes
a uniform positive radially averaged flux budget in infinitely
many bands, but does NOT bound spikes at one moving radius.

The axial-flux absolute bound is
|F_axial| <= R ||eta'||_infinity E0/2
+ nu sqrt(pi/2) R² ||eta''||_2 sqrt(E0).
The viscous radial-flux band average is bounded by
nu sqrt(pi(b²-a²)) ||eta||_2 ||partial_r u_theta-u_theta/r||_{L2(a<r<b)}.
The radial shear must be independently certified.

Angular Fourier covariance modes obey a sharp elementary tail:
|sum_{|m|>N}u_{r,m}Gamma_{-m}| <=
||partial_theta u_r||_{L2theta}||partial_theta Gamma||_{L2theta}
 /[2pi (N+1)²], with analogous axial covariance bound.
This tracks angular-frequency leakage explicitly.

Also |M_{R,eta}|<=sqrt(pi/2)R²||eta||_2 sqrt(E0),
so an integrated angular-momentum balance alone cannot establish
the singular value at a single source trajectory.

## Exact negative controls
The Gaussian zero-force solution from Edition XXXVII yields,
at initial time and with eta=e^-z²,
M'_R(0)=-2pi epsilon²R⁴e^-2R² sqrt(pi/3), nonzero exactly.
For the moving source radius R=sqrt(2X(1-t)), RR'=-X and
F_sweep=-2pi X integral eta barGamma dz.
An apparent tau^-h contribution can be caused by the boundary
moving across an already-growing field; it is not proof of nonlinear
transport. Angular pressure torque is zero, but physical pressure
itself remains an unremoved evolution constraint.

## Reproducibility / release
Two exact SymPy conservation/Gaussian/mode audits completed,
plus 60,000 seeded Fraction Cauchy and angular-tail tests.
Four-page standalone PDF compiled and page-rendered for layout.
ZIP contains PDF, complete LaTeX, both Python scripts, finite Lean
scalar file, README, source status, and SHA256 manifest, all verified.
The new Lean file is not a complete formalization of PDE or analytic
conservation; kernel compilation must be confirmed independently by CI.
The original actual A.11/A.19 and Section 10 numerical profiles and
zero-force singularity-preserving residual certificate remain FAIL CLOSED.

**Next decisive mathematical gate:** for one and the same smooth-data
exact unforced evolution, quantify a signed, space-time flux lower bound
through a specified shrinking cylinder or band plus all viscosity,
axial, moving-boundary and high-angular-mode errors, and prove it
forces pointwise source-compatible swirl growth. No such lower bound
or unforced finite-time blowup theorem has been obtained.
