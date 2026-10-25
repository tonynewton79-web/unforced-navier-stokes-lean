# Edition XLII — exact full projected near-axis Lambda evolution and short-time positivity
25 October 2026 | Tony Newton | Newton Astro Labs

## Precise inherited variable
Edition XLI defines Lambda(z,t)=-4J3-d_z K2 where
J3=[a(-2 Uxy+Vxx-Vyy)+b(Uxx-Uyy+2Vxy)]/8,
K2=(b W_x-a W_y)/2,
a=U|axis,b=V|axis, U=u_x,V=u_y,W=u_z, axis x=y=0.
Lambda is the coefficient of r² in the mean Reynolds torque.

## Proved full unforced PDE equation
Use D0=partial_t+W_axis partial_z and the exact jet generator
H_i^alpha=[nu Lap partial^alpha u_i -partial^alpha partial_i p
 -partial^alpha(u.grad u_i)+W_axis partial_z partial^alpha u_i]|axis.
The cumulative theorem contains every H term in D0 Lambda, including the
commutator -partial_z(W_axis) partial_z Q with Q=b W_x-a W_y.
Pressure solves -Lap p=partial_i partial_j(u_i u_j) and is nonlocal.
Derivative orders up to fourth for velocity and third for pressure are
genuinely required. No positive finite 2-jet ODE is proved.

## Exact global nonzero-data zero-force constructive control
Take nu>0, epsilon=nu/1000, and
u0=curl(epsilon exp(-x²-y²-z²)[x-(x²+y²)y] e_z).
The Fourier small-data bound q<=1/(100 sqrt(pi))<1/16 gives a unique
global smooth exact unforced solution, as in the prior Edition XXXVII theorem.
Its initial coefficient and full physical pressure-correct PDE derivative are
Lambda(0,z)=4 epsilon² exp(-2z²),
partial_t Lambda(0,z)=16 nu epsilon²(2z²-7) exp(-2z²).
At z=2, positive derivative =16 nu epsilon² exp(-8).
At z=0, negative derivative =-112 nu epsilon².
By smooth time continuity there exists some delta>0 with
partial_t Lambda(t,2)>=8 nu epsilon²exp(-8) for t in [0,delta].
The value delta has not been numerically certified.

## Full pressure cancellation explained, without dropping it
Let S be physical rotation by pi around z. S u0=-u0.
The full projected quadratic acceleration N=-Pdiv(u0 tensor u0),
including its nonlocal pressure, has S N=N.
Lambda is a rotationally invariant *quadratic* transverse-jet scalar,
so its odd-even polarization d Lambda(u0)[N]=0 exactly at t=0.
Thus this example's initial positive coefficient growth is viscous,
NOT driven by the nonlinear strain or pressure.

## Independent double checks
One SymPy script directly verifies the full axial-transport jet formula,
including the -c_z Q_z commutator, and derives the Gaussian viscous jets.
A separate script evolves the Gaussian analytically by the heat semigroup,
obtaining Lambda_heat=-4 k epsilon² s^-7 exp(-2z²/s),
s=1+4nu t, and verifies the half-turn mixed-parity cancellation.
10,000 seeded exact rational simple bilinear fixtures and independent analytic
checks passed locally. A two-page standalone PDF was compiled twice and
rendered/visually inspected. Files were packaged with SHA256 verification.
The limited Lean source only proves algebraic scalar implications,
not analytic Fourier/pressure/NSE theorems. Lean CI success is unconfirmed.

## Research status — fail closed
This is an exact, actual **short-time** positive amplification result in
a globally smooth regular flow. It gives NO terminal tau^-h lower bound,
NO sustained positive *nonlinear* strain mechanism, NO pointwise blowup,
and NO end-to-end formalized Lean NSE theorem. The original OpenAI
Section 10 numerical profile remains unfrozen, and its Navier–Stokes
blowup uses external forcing.

Next decisive target: identify quantitatively the **cubic pressure-complete
nonlinear contribution** to D0 Lambda for a genuinely mixed-parity smooth
datum, and prove a signed lower bound over an interval with the fourth-order
viscous-jet costs and all angular-frequency leakage controlled. Then separately
connect that coefficient to source-compatible terminal growth. Nothing close to
an unforced finite-time singularity has been proved.
