# Edition XL extension — moving-radius energy-dissipation exclusion
25 October 2026 | Tony Newton | Newton Astro Labs

## Revision of the decisive target
The original Edition XL constructed a single globally smooth exactly unforced Gaussian evolution with signed inward angular-momentum flux F(R,t)<0 for all sufficiently small R over a common initial time interval, magnitude O(R^4). That positive result stands.

The later hypothesis that one exactly unforced finite-energy solution could have persistent |F(sqrt(2X tau),1-tau)| >= c tau^-h at every sufficiently small tau for h>=0 is **ruled out**, rather than merely penalized by an H² lower estimate. This statement concerns the full radial *advective* cylinder flux, not the radial derivative of its Reynolds stress, the angular trace, the viscous or axial terms.

## Radial trace and finite time-energy proof
For Gamma=r u_theta, eta bounded and F_eta(R,t)=R²∫∫eta u_r u_theta dtheta dz, a direct radial fundamental-theorem/physical-volume Cauchy bound gives
  |F_eta(R,t)|/R <= ||eta||infty ||u(t)||2 ||partial_r u(t)||2
                 <= ||eta||infty ||u(t)||2 ||grad u(t)||2.
For **any measurable positive** radius R(t), the exact unforced energy identity gives
  ∫_0^S |F_eta(R(t),t)|² / R(t)² dt
     <= ||eta||infty² E0²/(2nu), E0=||u0||2².

For R(t)=sqrt(2X(1-t)), this implies
  ∫_(1-tau)^1 |F_eta(R(t),t)| dt
    <= ||eta||infty E0 sqrt(X/(2nu))*tau.
If |F_eta| >= c tau^-h on every terminal time, the squared energy
integral would dominate (c²/(2X))∫_0^tau0 tau^(-1-2h)dtau, which
diverges for h>=0. Therefore liminf_tau↓0 |F_eta|=0.

For a measurable time set W_tau⊂[1-2tau,1-tau] with
|F_eta|>=c tau^-h, its duration obeys
  |W_tau| <= [2X ||eta||infty² E0²/(nu c²)] tau^(1+2h).
Hence short intermittent flux spikes are *not* categorically excluded.

## Verification and release
The source-independent Gaussian radial trace was integrated symbolically and
checked against 25,000 exact rational samples.
An independent rational test checked 25,000 moving-radius
time-coherence/energy budgets.
The three-page mathematical note was compiled twice with pdflatex,
rendered and inspected: no overfull lines or unresolved references.
The cumulative manuscript includes the XL extension and the
original XL section now explicitly corrects its earlier conditional
terminal-flux interpretation.
The Lean file checks only limited scalar algebra and its dedicated
GitHub CI cannot be reported passed unless a runner returns success.

## Source and open mathematical target
The OpenAI Navier--Stokes construction has external forcing;
its separate unforced blowup theorem is for Euler.
Original published Section 10 exact profile and numerical source certificate
remain unfrozen: FAIL_CLOSED_MISSING_SOURCE_DATA.

The terminal positive *derivative torque*, intermittent advective
transport, angular oscillation, viscosity/axial leakage control,
and actual pointwise singularity retention remain genuinely open.
No exactly unforced Navier--Stokes finite-time singularity or
end-to-end Lean PDE proof has been obtained.
