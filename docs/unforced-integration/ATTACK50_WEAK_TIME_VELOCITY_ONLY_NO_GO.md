# A weak-in-time terminal-velocity obstruction for a frozen source-first singular preparation

**Independent 9 November 2026 audit — partial NEGATIVE theorem only.** The original OpenAI (2026) result has smooth forcing. The actual proposed analytic G1/H8 unforced carrier, source-first compact right inverse, nonlinear periodic pressure, and global unforced blowup remain OPEN. This theorem applies to the *fully specified diagnostic preparation* of Attack 49, not the original B.12 analytic source.

## New theorem (no derivative-smallness assumptions)

Set tau=1−t, h=1/200, A=1/2+h, D=1/2−h and use the source-first divergence-free, torque-calibrated, finite-energy prepared velocity from Attack 49. Its density rho=tau^(−1−h)k(16s)k(16xi), s=r/sqrt(tau), xi=z/tau^D, vanishes on 11/128<s<13/128, |xi|<1/16. On that same annulus its exact velocity is u_r=0, u_theta=(1/20)tau^(−A)s, u_z=(1/20)tau^(−A). The true fixed residual F=N(u), where N(u)=u_t+div(u⊗u)−Delta u, has strictly positive pressure-free pairing with the moving divergence-free test v_tau=rW_tau e_theta, W_tau=k(128(s−3/32))k(16xi):

< F,v_tau > = (201/4000) J tau^beta, beta=1/2−2h=49/100, J>36501/274877906944. This is the EXACT independently verified Attack49 source, NOT a manufactured matching stress.

If any smooth divergence-free correction w makes u+w an exact unforced viscosity-one Navier–Stokes solution with one periodic pressure, define
epsilon_T = sup_{T<=tau<=2T, x in supp(v_tau)} max{ tau^(1/2)|w_r|, tau^A |w_theta|, tau^A|w_z|}.
Then, for EVERY 0<T<=1/2,
**epsilon_T>7336701/1443658767269888000>5.08e-12.**

In particular epsilon_T cannot tend to zero. No bound on w_t, grad w, Delta w, global kinetic energy, or exterior halo is imposed. The correction need not be axisymmetric. The result is also valid if an additional stress is present but supported inside the prescribed rho region, because the test is entirely in vacuum.

### Exact time-integrated proof constants

The globally analytic compact cutoff k(q)=exp[−1/(1−q²)] on |q|<1 (otherwise zero) satisfies ||k'||<=2, ||k''||<40. On the test support:
|v_theta|<=sqrt(tau)/8,
|partial_t v_theta|<=17 tau^(−1/2)/8,
|r W_r|<=32,
|partial_z(rW)|<=4tau^h,
|Delta v_theta|<=83968 tau^(−1/2),
|supp v_tau|<=tau^(3/2−h)/128.

The **exact nonlinear toroidal contractions**, valid for general non-axisymmetric w, are
(u⊗w+w⊗u):grad v=(u_z w_theta+u_theta w_z)partial_z(rW)+u_theta w_r r W_r,
(w⊗w):grad v=w_r w_theta r W_r+w_z w_theta partial_z(rW).
They are bounded pointwise by (17/40)epsilon tau^(−1−h) and 36epsilon² tau^(−1−h). Integrate the unforced equation against v_tau over t∈[1−2T,1−T], transferring ALL derivatives from w onto the known v_tau using periodic integration by parts. With beta=49/100, the resulting error terms divided by T^(beta+1) are bounded by
- time derivative: (39/1024)epsilon,
- viscosity: 1312 epsilon,
- linear convection: (17/2560)epsilon,
- quadratic convection: (9/16)epsilon².

For epsilon<=1, the sum is <1313 epsilon. The signed fixed-source term is >(7336701/1099511627776000)T^(beta+1). Thus the theorem. If epsilon>1, the claimed lower bound holds trivially.

### NEW uniformity in exponent

The identical argument applies to the entire explicitly prepared diagnostic family 0<h<1/100, since A+D=1 and beta=1/2−2h∈(0,1). The signed source constant is (1+h)J/20>J/20. Hence every such prepared diagnostic, for every 0<T<=1/2, has the uniform necessary bound
**epsilon_T>36501/7218293836349440>5e-12.**

The exact leading correction w=−u makes the unforced zero solution; it has epsilon_T>=1/20, consistent with the obstruction, but it DESTROYS the prepared singular trace. This theorem forbids terminal-subleading recovery of the frozen source, not arbitrary unforcing or global NS blowup by any possible alternative carrier.

## Independent checks / release boundary

A 3-page scholarly TeX/PDF note was compiled twice and visually inspected; no overfull lines. The standalone exact Fraction/SymPy verifier passes the cutoff derivative, support volume, time-integration, all rational inequalities and two nonlinear toroidal identities. The Attack49 original full source checker and independent nine-polynomial complete cylindrical residual checker passed again; all included in the complete local proof packet with SHA256 manifest. This is **not a Lean formalization**. No 245-page existence manuscript update is made for a negative diagnostic result.

**Authentic source-first next step:** obtain the actual entire G1/G3/G4 prepared residual (not a diagnostic), freeze the true density, all cutoffs and spatial frame, and run simultaneous zero-collar, oriented cone, toroidal slice and weighted velocity-only weak tests. The original analytic source has not yet passed or failed these tests.