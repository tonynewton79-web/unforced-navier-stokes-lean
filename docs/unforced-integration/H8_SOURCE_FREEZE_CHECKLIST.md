# Authentic H8 source freeze and zero-force integration gates

The exact seven-ray cone is now better constrained by its coupled
axial--azimuthal hexagon, but **the authentic H8 source is not frozen**.
This checklist is a missing-input contract, not a certificate of existence.

## One immutable source record (G1--G4)

For a single commit/hash of the originating Case 006 analysis, select
and record the *same* normalized parameter tuple throughout:

| Field | Required authentic object and independent verification |
|---|---|
| Source provenance | SHA-256, source equations, revision, base geometry and parameter domain |
| Physical frame | `E(t,r,theta,z) in SO(3)`, coordinate convention, derivatives in all three spatial variables and time |
| Core | Actual vector potential and three-variable cutoff `chi` with full transition geometry, rather than a diagnostic radial cutoff |
| Shapers | Every `Psi_i`, radial envelope `b_i`, toroidal field, relative phase and all 12 ordered quarter-turn overlaps |
| Reference fields | Nonnegative `rho`, complete physical `R_star`, weighted support and regularity bounds |
| Pressure | One periodic representative `p` with `-Delta p = partial_i partial_j(u_i u_j)`, both axial endcap traces, radial and angular terms |
| Residual | Complete time-dependent `g`, the `partial_t u` marginal, nonlinear interactions, viscous second jets of all *independent* cutoffs |
| Compatibility | Global mean/moments, compact support collar, cylinder axis continuation, Leray projection tails and pressure gauge |

The physical stress is `K=E H E^T`, where

```
H = [[-D, C, A], [C, 0, B], [A, B, D]].
```

The *one-sided* ray floors are the admissibility requirements. The
original symmetric absolute budget is a narrower, separately conditional
test and must never silently replace those floors. The exact `(A,C)`
projection is now the joint hexagon in the manuscript's theorem
`Exact joint axial--azimuthal seven-ray cone`.

## Continuum source and pressure gate (G4)

1. Compute the full Cartesian `div(E H E^T)` including every derivative
   of `E`, then verify the cylindrical `-D/r`, `2C/r` and `A/r` terms.
2. Derive angular and axial slice identities with rigorous
   differentiation/integration interchange. Retain both combined
   axial `K_zz+p` and azimuthal `K_theta z` endcaps.
3. Include the temporal source primitive and both independent cutoff
   second jets; only collapse them when equality of physical profiles
   is explicitly proved.
4. For each radial slice, certify the **joint** axial/torque source
   primitive in the aligned frame. Under spatial tilt use the entire
   four-field rotated dual and the corrected angular-test enclosure.
5. Search for a compact symmetric tensor with exact source matching
   `P div H = g - P div(rho R_star)` and all seven lower floors, or
   exhibit a certified divergence-free dual violation for the *same*
   source, pressure and support.

In the variable-frame cell enclosure, the test
`G(theta)=e_r(theta) tensor e_z` varies independently of `E`.
Either integrate `rho * sigma(lambda(E_j^T G(x) E_j))` over the cell,
or certify both `delta_j>=sup||E-E_j||_F` and
`eta_j>=sup||G-G_j||_F`; a valid rational error is
`sum_j m_j*(2*delta_j+eta_j)`. A frame-only mass-times-centre
approximation is not a theorem.

If `rho=0`, the one-sided ray floors imply `A=B=C=D=0`. A residual
remaining in a density-zero transition collar cannot be repaired by
this constrained tensor except for a permissible pressure gradient.
In particular, the full Cartesian source `f=div(E H E^T)+grad(p)` must
satisfy `curl(f)=0` throughout such an open collar. If `rho` is flat
at a smooth support boundary point, **every derivative of `curl(f)`
must vanish there**. The manuscript's flat-edge proposition proves
this necessary condition directly; the finite zero-density coefficient
statement also has a dedicated Lean declaration and exact Python
tests. This is a new source-side screen to apply *after* source freeze,
not evidence that the authentic H8 source violates it.

**Quadratic-vacuum refinement.** At a density-zero point whose Hessian
is `lambda*n tensor n` with `n=E(x0)e_3`, let
`omega=E(x0)^T curl(f)(x0)`. The new local necessary and sharp jet
screen is `omega_3=0`,
`|omega_1| <= (15971/983200)*lambda`, and
`|omega_2+4*omega_1| <= (17571/122900)*lambda`.
It follows by applying the same seven-ray floors to second directional
jets; it is pressure-independent and immune to frame-derivative terms
at the zero. It has an exact rational corner/witness regression in
`h8_vacuum_curl_gate.py` and a new *finite* parallelogram Lean
declaration, whose hosted kernel receipt must still be checked.
Neither this local necessary screen nor its manufactured sharpness
model supplies the missing authentic H8 density Hessian or source.

## Signed periodic pressure-work gate (Appendix V; still OPEN)

For one common authenticated H8 core and exterior correction, calculate
the **full** zero-mean periodic Poisson pressure, not just the source's
local pressure ansatz:

```
pi[u] = (-Delta)^(-1)_0 partial_i partial_j(u_i u_j)
u = U + w
pi[u] = pi[U] + 2 Q(U,w) + pi[w]
```

On a smooth moving interface with `U=0` in an open collar, set
`g=w dot n`; the exact gauge-invariant signed pressure work is
`int_boundary pi[u] g dS`. Computing `osc_boundary pi`
or identifying the critical pressure amplitude `tau^(-2A)`
does **not** determine the sign. The diagnostic in Appendix V gives
the fully recomputed periodic Poisson work
`(224*pi^2/195)*lambda` for smooth solenoidal Fourier data,
demonstrating exact sign reversal under a boundary-trace reversal.
It is **not** the authentic H8 carrier.

A source-specific release packet must supply:

- One frozen physical `U`, `w` and all cutoffs, frames and
  overlap fields at a common source revision, including a reproducible
  hash/parameter manifest.
- The complete periodic Poisson pressure for `U+w`, including
  `Q(U,w)` and `pi[w]` with independently checked Fourier tails.
- The actual boundary normal trace `g=w dot n`, mean-zero compatibility,
  interface cofactor, normal orientation, and gauge-invariant
  signed pressure-work integral with rigorous enclosure.
- Matching signed convection, viscous and moving-boundary work on
  each terminal dyad; these must meet Appendix T's positive inward
  energy requirement without dropping any term.
- A zero-residual certificate for the whole nonlinear unforced
  PDE and compatible positive seven-ray stress, rather than merely
  satisfying the boundary inequality.

**Status: HOLD / no authentic H8 pressure-work coefficient.**
Neither the new Fourier test nor the pressure-exponent calculation
discharges G4--G8.

## Exact leading signed pressure coefficient (Appendix W)

Appendix U's pressure-oscillation exponent alone is not a work
certificate. On the fixed anisotropic interface
`Omega(t)=x0+diag(tau^(1/2),tau^(1/2),tau^D)*Omega0` with
`D=1/2-h`, `A=1/2+h`, `p=1/2-3h`, verify the
**actual** uniform traces

```
tau^(2A) * (pi[u](t,x0+S_tau*y) - c(t)) -> Pi(y)
tau^(1/2) * w_perp(t,x0+S_tau*y) -> V_perp(y)
tau^(1/2) * w_z(t,x0+S_tau*y) = O(1)
```

If the genuine periodic unforced solution locally retains a
carrier `U=0` near the boundary and Appendix T applies, then the
leading signed pressure coefficient is

```
C_pi = int_boundary_Omega0 Pi(y) * (V_perp(y) dot n_perp(y)) dS0
```

and the **necessary** full-flux inequality is
`C_pi+C_other <= -M0*(R0-p/2)`.
The axial pressure interface contribution is lower by `tau^h`
under these specific boundary assumptions; never discard it
without checking the assumptions. Incompressibility forces the
limiting lateral normal flux to have zero mean, making `C_pi`
gauge independent.

**A rigorous finite-mode pass/fail path is available:**
with `K>=1`, Fourier sum `W_K`, actual boundary
`g=u dot n`, and Fourier-normalized tensor Sobolev norm,

```
abs(W-W_K) <= sqrt(26/3) * K^(-3/2)
              * norm_L1_boundary(g) * norm_H3_F(u tensor u).
```

Acquire source-authenticated enclosures for the finite coefficients,
interface geometry, `g` and Sobolev tail on every requested
terminal dyad. A positive finite sum without a certified
tail or signed normal correlation is insufficient.

**Current authenticated-source state: HOLD.** No common original H8
vector potential, cutoff, rotating frame, shapers, density, stress
centre, residual and exterior correction were located in the
research branch; Appendix W gives a conditional, classical
Fourier estimate and the needed scalar coefficient only.

## Axisymmetric pressure-mode filter (Appendix X)

For the shrinking H8 chart, first test whether the pressure contribution
comes only from a compact axisymmetric leading swirl. Under a
differentiated transverse limit and an exterior boundary profile
`w_perp=tau^-1/2 V_perp`, `w_z=tau^-1/2 V_z`, solenoidality forces
`div_perp V_perp=0` because the axial term is `tau^h` smaller.

If the leading carrier self-pressure `Pi_U` satisfies the regular
axisymmetric transverse equation

```
-Delta_perp Pi_U = -(1/R) * partial_R(v_theta**2)
partial_R Pi_U = v_theta**2 / R,
```

and the original core swirl vanishes in a collar of a smooth circular
reference interface, then `Pi_U` is radially constant on that collar.
Its critical pressure-work coefficient therefore cancels:

```
C_pi_U = int_boundary Pi_U * (V_perp dot n_perp) dS0 = 0
```

The **full** pressure `Pi` can still have nonaxisymmetric modes,
including source shapers and cross/self terms from the exterior
correction. With boundary lateral normal trace `q`, the next
source-authenticated target is the exact angular coefficient

```
C_pi = 2*pi*int a(eta)*sum_{m != 0} Pi_m(eta)*q_{-m}(eta) deta.
```

Here `q_0=0` slice-by-slice. Sign closure requires an interval
enclosure for the nonzero angular mode pairing, the independent
`C_other` flux, and the required inequality
`C_pi+C_other <= -M0*(R0-p/2)` under Appendix T's
retention hypotheses.

**Important scope:** the transverse Poisson limit is an assumption
for this model, not yet proved for the original Case 006 rotating-frame
or nonaxisymmetric H8 source. No authentic `Pi_m`, `q_m`,
or `C_other` coefficients are available. Never count a radial
diagnostic cancellation as a source-specific no-go theorem.

## C4 symmetry and the source-specific m=4 pressure gate (Appendix Y)

The quarter-turn average of a vector potential creates a C4-equivariant
prepared carrier, but **does not by itself prove that an actual nonlinear
exterior correction shares that symmetry**. If the *complete* periodic
velocity is C4-equivariant, its unique mean-zero physical Poisson pressure
has angular modes only m=0, +/-4, +/-8, ... . If only the carrier is C4,
this Fourier selection applies to the carrier's self-pressure alone;
the mixed and exterior correction pressures need separate analysis.

Under the slice-wise normal-flux condition q_0=0, the leading signed
pressure coefficient in the fully C4-equivariant case is

```
C_pi = C_4 + E_ge8
C_4 = 4*pi*integral a(eta)*Re(Pi_4(eta)*conj(q_4(eta)))deta
abs(E_ge8) <= 1/64*integral a(eta)*norm_L2(dtheta2 Pi)
                                  *norm_L2(q)deta .
```

With a certified upper remaining-flux coefficient `C_other_plus`,
the necessary inward-energy sign gate is verified by

```
C_4 + B_8 + C_other_plus <= -M0*(R0-p/2).
```

With certified lower remaining flux `C_other_minus`,
the same candidate source would be excluded if

```
C_4 - B_8 + C_other_minus > -M0*(R0-p/2).
```

This is a **necessary energy-flux gate**, not a sufficient existence
theorem. One must first authenticate the full source, prove or
separately justify full-correction C4 symmetry, verify the periodic
Poisson pressure and all normal-velocity/moving-interface traces,
and control all non-pressure fluxes with rigorous error bounds.

A fully reconstructed smooth C4-periodic Poisson diagnostic in
Appendix Y gives signed work (per unit axial length) in
(-0.0079871,-0.0079870) at alpha=3/10 and the opposite sign at
alpha=-3/10, with exact rational Fourier/Bessel coefficients.
Thus C4 symmetry cannot force the needed sign.
These fields are NOT original Case006 H8 fields and are NOT
time-dependent unforced solutions.

**H8 source-specific signed coefficient status: OPEN.**

## Planar fourfold pressure multipole source audit (Appendix Z)

Before reconstructing a full 3D periodic pressure, ask whether a
rigorous transverse **free-space planar pressure limit** for the same
H8 source has actually been proved, including axial terms, periodic
images, frame derivatives and exterior-correction errors. Do not
assume this limit merely from scaling exponents.

Under this additional planar-limit hypothesis, for a compact
C4-equivariant solenoidal transverse carrier U=(U_x,U_y), the exact
exterior fourth harmonic is determined by one weighted quadratic
stress moment:

```
zeta = x + i*y
Q4(U) = integral_R2 zeta**2 * (U_x + i*U_y)**2 dx dy
Pi4(R) = (3/(4*pi*R**4))*conj(Q4(U)), outside support
```

If U is the original quarter-turn-average U=(1/4)*sum_{j=0..3} v_j,
the moment contains **all 16 ordered products** j,k, including the
12 off-diagonal overlaps. A diagonal-only estimate is not the
complete source pressure.

Appendix Z contains a finite-regularity compact C4 diagnostic
stream function psi_eps=(1-R**2)^6_+*(1+eps*R**4*cos4theta),
for which exact rational integration yields Q4=8*pi*eps/1001 and
Pi4(R)=6*eps/(1001*R**4), R>1. A disjointly supported C4-solenoidal
exterior field with q=cos4theta produces full planar Poisson work
delta*12*pi*eps/(1001*a**3)+O(delta**3), of either sign for small
delta. This verifies that a compact C4 self-pressure can supply
a nonzero fourth mode, but **does not authenticate original H8**.

Mandatory original H8 source-specific gate:
- Freeze one original vector potential, full cutoff, all shapers,
  four-patch fields, rotated frame, rho, R_star and physical residual.
- Rigorously control planar-limit pressure error for the true
  3D periodic field, or work directly with its full Poisson modes.
- Evaluate the complete Q4 moment and signed exterior normal trace
  with independent interval enclosures; keep correction cross and
  self pressure terms.
- Prove the remaining flux coefficient and the necessary
  inward-energy inequality, a compatible positive seven-ray
  stress, full nonlinear zero-residual correction and terminal
  pointwise retention.

**Gate remains OPEN.** A planar control model does not prove the
original unforced Navier-Stokes singularity claim.

## Periodic-to-planar pressure and near-field necessity (Appendix AA)

The H8 physical component hierarchy in Appendix N is
`Ur=tau^-1/2*Vr`, `Utheta=tau^-(1/2+h)*Vtheta`,
`Uz=tau^-(1/2+h)*Vz` with radial length `tau^1/2`,
axial length `tau^(1/2-h)` and `eps=tau^h`. Exact physical
divergence, for the straight reference-chart form, gives

```
(1/R)*partial_theta Vtheta =
  -eps*((1/R)*partial_R(R*Vr)+partial_eta Vz).
```

If the complete source is genuinely in this chart and has
bounded convergent differentiated profiles, its leading azimuthal
velocity is **axisymmetric**. A leading order-one m=4 swirl
requires a compensating leading derivative and cannot be freely
inserted into the old similarity hierarchy. Verify the actual
implicit physical q/eta chain rule before using this conclusion.

For uniformly compact strong Hs (s>5/2) reference profiles,
the **actual periodic** carrier-only Poisson pressure has a
rigorously justified 2D transverse limit, with the periodic-image
pressure correction O(tau^p) unscaled. The leading
axisymmetric swirl pressure is

```
Pi0(R,eta)=-int_R^infinity Vtheta0(s,eta)^2/s ds.
```

It is zero in a collar outside the swirl support. Thus the
carrier-only pressure contribution to signed boundary energy work
is o(tau^(p-1)) under the bounded exterior trace profiles of
Appendix W. This conclusion is **only about pi[U]**:
the nonlocal mixed `2Q(U,w)` and exterior `pi[w]` can remain
critical, especially for correction stress sourced outside
the compact core.

For a C4-covariant pressure-generating stress with L1 size
at most E_* supported distance d from a shrinking circular
interface of radius ell=tau^1/2, the nonzero fourfold pressure
modes have the rigorous upper bound

```
sup_(m in 4Z, m!=0) |pi_far_m|
    <= C*E_* * tau^2 * d^-7.
tau^(2A)*sup |pi_far_m| <= C*E_* tau^(3+2h)*d^-7.
```

If `d/tau^((3+2h)/7)->infinity`, the fourfold far-field
contribution is subcritical. At h=1/10, exponent=16/35.
This is a pressure-**stress** distance gate; it does not
assume the whole correction is supported away from the boundary,
and is invalid for symmetry-breaking lower angular modes.

The available local Case 006 seed A=(-yz,xz,0) with radial
cutoff chi has Ur=-r(chi+z chi_z), Uz=z(2chi+r chi_r).
Its transverse divergence is **not** zero: its axial divergence
cancels it. Do not apply the planar-solenoidal Appendix Z
moment directly to this 3D seed.

**Still OPEN:** freeze one complete authentic source, including
the true off-axis chart and four-patch overlaps; certify
correction mixed/self pressure, C_other, one-sided seven-ray
positive stress, a zero-residual nonlinear correction and
pointwise terminal retention. The original unforced
singularity theorem has not been proved.

## Two-scale nonlinear exterior correction exclusion (Appendix AB)

For a retained compact H8 carrier with R0>p/2, in the
tau=T-t chart with A=1/2+h, D=1/2-h, p=1/2-3h,
Appendix AB now adds a necessary **correction pressure gradient**.
If w in the moving core is bounded by C*tau^-1/2, its boundary
gradient by C*tau^-1, and the actual carrier self-pressure is
subcritical on the zero-U collar (Appendix AA), the exact local
energy equation and divergence theorem force:

```
pi_c = 2*Q(U,w) + pi[w]
sup_{I_tau, Omega} |grad(pi_c)| >= c*tau^(-3/2-2h)
int_boundary pi_c*(w dot n) = int_Omega w dot grad(pi_c).
```

An exact **two-scale correction no-go theorem** applies to a
hypothetical unforced solution u=U+w_N+w_F when:

- w_N is solenoidal and tau^-1/2 times a uniformly bounded Hs>5/2
  compact reference-scale profile, including the interface;
- w_F is solenoidal, its support is disjoint from U+w_N and
  separated from the moving core by distance >=d(tau), and
  ||w_F||_2^2<=E_* uniformly (no globally small error assumed);
- the strong carrier reference profiles and zero-swirl collar of
  Appendix AA hold;
- d(tau)/tau^(3/8+h/2)->infinity.

Then the **actual periodic Poisson** near pressure is subcritical,
the far pressure gradient satisfies
`||grad pi[w_F]||_infty(Omega)<=C E_* d^-4`, and its signed
interface work obeys

```
|int_boundary pi[w_F]*(u dot n)|
      <= C E_* tau^(1-h)*d^-4 = o(tau^(p-1)).
```

The other boundary fluxes are subcritical, contradicting the
necessary inward energy transfer. **Such a correction architecture
cannot produce the desired exact unforced H8 retained-core solution**.
For h=1/10, the distance threshold exponent is exactly
3/8+h/2=17/40=0.425. The statement is conditional and does not
exclude overlapping near-field stress, a correction of stronger
interface amplitude, loss of scaled regularity, or another mechanism.
It is **not** a global Navier-Stokes regularity theorem.

The next actual source attack must freeze complete Case006 data and
construct an overlapping, genuinely critical near-field exterior
coupling (or another explicit compatible mechanism), then compute
the mixed/self periodic pressure, all signed nonpressure fluxes,
positive one-sided seven-ray stress, exact PDE correction, and
pointwise terminal retention. Status: OPEN.

## Source-independent quadratic stress concentration gate (Appendix AC)

Unlike the separated-halo theorem, this conditional result permits an
overlapping, arbitrarily nonlocal exterior correction and imposes
no symmetry or globally small L2 correction assumption.

Let u=U+w solve the genuine unforced Navier--Stokes equation,
locally retain a compact H8 carrier as in Appendix T, and suppose
the **dyad-integrated** sum of carrier-only pressure work and all
nonpressure boundary fluxes is o(tau^p), with R0>p/2.
Set delta_tau=tau^(-p/2)*sup_{I_tau} ||w||_L2(Omega(t)); then
delta_tau->0. With complete periodic pressure pi_c=pi[U+w]-pi[U]
and complete **quadratic velocity stress**

```
S = U tensor w + w tensor U + w tensor w
pi_c = (-Delta)^(-1)_0 partial_i partial_j S_ij,
```

the necessary inward transport implies

```
sup_I ||grad pi_c||_L2(Omega)
  >= c * tau^(p/2-1) / delta_tau,
sup_I ||grad S||_L2(T3)
  >= c * tau^(p/2-1) / delta_tau,
tau^(1-p/2) * sup_I ||grad S||_L2(T3) -> infinity.
```

The second line follows from the exact periodic rank-one Fourier
pressure multiplier inequality
`||grad pi_c||_2 <= ||grad S||_2` with constant one.
This quadratic velocity stress is **NOT** the constrained positive
seven-ray H8 engineering stress. Do not conflate their norms or cones.

**New no-go:** if an authenticated source plus correction yields
`sup_I ||grad S||_L2(T3)=O(tau^(p/2-1))`, it cannot satisfy
the retained-core pressure transport under these hypotheses.
At h=1/10 the natural stress-gradient exponent is -9/10.
For the same source the physical pointwise pressure-gradient
requirement strengthens to

```
sup_I ||grad pi_c||_Linfty(Omega)
 >= c * |Omega0|^-1/2 * delta_tau^-1 * tau^(-3/2-h).
```

The **remaining constructive frontier** must therefore exhibit
a genuinely super-natural quadratic stress-gradient concentration,
or invalidate a stated flux/retention assumption, while still
closing all H8 source, positive-stress and nonlinear PDE requirements.
A necessary concentration law does not construct the required
singular near-field correction or solve Navier--Stokes.

## Strong local retention versus total energy dissipation (Appendix AD)

Under the pressure-driven inward flux assumption of Appendix AC,
and global pointwise bounds on an actual correction
`||w||_infty<=C*tau^-1/2`,
`||U||_infty<=C*tau^(-1/2-h)` and the usual carrier
gradient scaling, an exact finite-energy unforced solution requires

```
delta_tau=tau^(-p/2)*sup_I ||w||_L2(Omega) -> 0
int_I ||grad w||_2^2 dt >= c*delta_tau^-2*tau^(1/2-h).
```

If `delta_tau=O(tau^(1/4-h/2))`, each late dyadic
interval consumes a positive amount of true unforced
dissipation: this contradicts the finite global kinetic-energy
budget. At h=1/10 it excludes `delta_tau=O(tau^1/5)`.

This is a **conditional no-go**, not an exact nonlinear
source-matched correction or full Navier--Stokes proof.
The original physical source tuple, positive seven-ray stress,
full pressure/flux, terminal-retained correction and full
unforced finite-time singularity remain OPEN.

## Affine Case006 plateau: actual periodic pressure mismatch (Appendix AF)

The local diagnostic Case006 vector-potential seed
`A0=(-y*z,x*z,0)` has curl `(-x,-y,2z)`. The affine velocity
`u_aff=(-x,-y,2z)/(T-t)` with
`p_aff=-3*z²/(T-t)²` solves unforced NS **locally on R3**,
but has infinite spatial kinetic energy and cannot be the
desired finite-energy periodic singular solution.

For **any fixed compact smooth axisymmetric cutoff** chi(R,eta)
with a plateau chi=1, set
`R=r/tau^1/2`, `eta=z/tau^(1/2-h)`, `eps=tau^h`
and freeze the explicit prepared field
`U=curl[tau^-1*chi*A0]`. Then

```
U_r=tau^-1/2*[-R*(chi+eta*chi_eta)]
U_theta=0
U_z=tau^-(1/2+h)*[eta*(2*chi+R*chi_R)]
Pi_tau=tau^(1+2h)*pi_periodic[U].
```

The physical zero-mean periodic pressure obeys, on the
shrinking chart, the quantitative anisotropic Fourier bound

```
sup |partial_eta Pi_tau|
  <= C*tau^(2*h)*(1+abs(log(tau))).
```

On the plateau the exact source-specific **unforced physical
momentum residual** satisfies

```
tau^(3/2+h)*[U_t-Delta U+(U.grad)U+grad pi_periodic[U]]_z
     = 6*eta+O(tau^(2*h)*(1+abs(log(tau)))).
```

Although the velocity remains affine locally, its local affine
pressure does **not** equal the periodic pressure of the
compactified velocity. The physical Poisson equation remains
satisfied: its source is instead balanced predominantly by
transverse pressure curvature.

An exact unforced correction `w` must cancel this plateau
residual. If its complete **nonpressure axial** correction term
is subcritical relative to `tau^(-3/2-h)`, then its actual
periodic correction pressure must satisfy

```
partial_eta[tau^(1+2h)*pi_c] = -6*eta+o(1),
tau^(1+2h)*[pi_c(b)-pi_c(a)] = -3*(b*b-a*a)+o(1)
for 0<=a<b<eta0 and fixed R on the plateau.
```

This is a **signed axial pressure jump**, NOT the separate
radial interface pressure-work coefficient `C_pi`.
The real full H8 source still needs its authentic theta-dependent
four-patch profiles, shapers, and nontrivial cross terms; the
axisymmetric affine seed is a source-native local diagnostic only.
No positive seven-ray inverse, exact nonlinear solution or singular
unforced terminal result has been certified.

## Localized affine pressure-source proximity: no disjoint velocity assumption (Appendix AM)

The exact source-specific pressure gate should decompose the **full quadratic
correction stress**, not the total velocity: S=u tensor u - U tensor U.
For any compact axial plateau P_tau, split S into a cutoff-near part and
a far part supported >=d from P_tau. The split retains every U/w
mixed product and is valid even when the actual unforced velocity has
analytic tails. Finite global kinetic energy gives ||S_far||_L1<=C,
so the full periodic Poisson far pressure obeys

```
||grad pi_far||_Linfty(P_tau) <= C d^-4.
```

The source-only affine-seed physical residual is 6 eta after multiplying
by tau^(2A+D), where A=1/2+h and D=1/2-h. For any *actual* unforced
correction, denote the complete axial nonpressure correction by Q_z.
Then the exact necessary inequality is

```
sup_P |partial_eta[tau^(2A) pi_near] + 6 eta|
   <= C tau^(2h)(1+abs(log tau)) + sup_P|tau^(2A+D) Q_z|
      + C tau^(2A+D) d^-4.
```

If the normalized Q_z is o(1), then any d >> tau^beta with
beta=(2A+D)/4=3/8+h/4 forces near pressure to reconstruct
-6 eta. At h=1/10 this beta is exactly 2/5, the axial shrinkage
exponent. A purported far-only pressure solution with bounded global
energy is then excluded. This is **not** a full four-patch H8 source
construction, a proof of stress positivity, or the sought zero-residual
nonlinear correction. Remaining gates stay OPEN.

## Signed carrier self-advection gate independent of pressure (Appendix AN)

For any fully specified compact shrinking source U with
M=||U||_2^2~M0*tau^p and D=||grad U||_2^2~R0*M0*tau^(p-1),
R0>p/2, let an exact unforced u=U+w retain U locally with
delta_tau=tau^(-p/2)*sup_(I_tau)||w||_L2(Omega)->0.

Exact testing of the unforced PDE against U eliminates the
physical pressure **without** assuming pressure-dominated boundary
flux:
```
d/dt <w,U> =
    <w,U_t+Delta U+(U.grad)U>
  + integral w_i*w_j*partial_j U_i - (1/2)*M' - D.
```
The signed dyad integral of the two interaction terms must equal
K*tau^p+o(tau^p), K=M0*(1-2^(-p))*(R0-p/2)/p>0.

Assuming the carrier profile controls
```
||U_t+Delta U||_2 <= C*tau^(p/2-1)
||grad U||_infty <= C*tau^(-1-h)
||(U.grad)U||_2 <= C*tau^(p/2-1-kappa)
0<=kappa<=h
```
gives delta_tau>=c*tau^max(kappa,h/2). Under carrier
volume <=C*tau^(3/2-h), sup core |w|>=
c*tau^(-1/2-h+max(kappa,h/2)). No global w infinity bound.

**Authentic-source critical test:** for a natural-size retained
correction delta_tau=O(tau^h), all nonlinear work must be
supplied by the signed linear pairing
int_I <w,(U.grad)U>=K*tau^p+o(tau^p); a raw
source acceleration with kappa<h is insufficient.
DO NOT replace the raw source by P[(U.grad)U] when estimating
against local w: Leray P has a nonlocal tail.

The explicit no-swirl compact affine seed has kappa=0,
forcing delta_tau>=c*tau^(h/2), w infinity >=
c*tau^(-1/2-h/2); natural-amplitude w=O(tau^-1/2)
cannot work for that seed even with global tails.
For the true swirling four-patch Case006 carrier, evaluate
the full *physical* acceleration, all twelve C4 overlaps,
and the rotated frame before deciding whether kappa=h
survives. Positivity/periodic pressure/actual correction/
terminal blow-up remain OPEN.

## Axisymmetric swirl cannot supply critical transfer by centrifugal magnitude alone (Appendix AO)

Under uniformly compact smooth H8 similarity profiles with an
AXISYMMETRIC solenoidal carrier U=(Ur,Utheta,Uz) and fixed
h in (0,1/6), define the radial centrifugal potential

```
Psi_tau(r,z) = integral_r^infinity Utheta(s,z)^2 / s ds.
```

It is supported in the **filled radial disk** that contains the
swirl. A retention region limited to an annular support does not
control the full potential and is insufficient for this test.

For ANY globally solenoidal correction w, regardless of an exterior
analytic tail, periodic integration by parts gives exactly

```
int_T3 w . (-(Utheta^2/r) e_r)
     = - int_T3 w_z * partial_z Psi_tau.
```

The derivative of Psi in z has L2 size O(tau^(p/2-1));
the apparently larger centrifugal L2 power tau^(p/2-1-h)
is an unobservable transverse gradient against global w.
All other axisymmetric convective terms have L2 size
O(tau^(p/2-1)). Therefore the exact signed carrier pairing
of AN, with M~M0 tau^p and D~R0 M0 tau^(p-1), R0>p/2,
forces

```
delta_tau >= c*tau^(h/2),
sup_(I_tau) ||w||_Linfty(Omega_filled) >= c*tau^(-1/2-h/2)
```

for a locally retained smooth unforced u=U+w, assuming
Ut+Delta U has L2 size O(tau^(p/2-1)), grad U Linfty
O(tau^(-1-h)), and the full filled-core w L2 deficit
delta_tau ->0.

At h=1/10, this excludes a uniformly O(tau^-1/2)
core correction for the **axisymmetric swirl** class.
It does not exclude the intended authentic C4/nonaxisymmetric
H8 route. Source freeze must evaluate angular advection,
theta-dependent axial velocity and all 12 ordered overlaps
rather than counting the raw centrifugal stress size as a
certified signed energy injection.

## Critical nonaxisymmetric axial angular channel (Appendix AP)

For an authentic compact **C4-equivariant** source with smooth uniformly
bounded H8 similarity profiles, freeze the full theta-dependent
V_r, V_theta, V_z and all 12 ordered patch overlaps.

Exact incompressibility forces the leading azimuthal profile
V_theta^0(R,eta) to be independent of theta, but V_z^0 can retain
nonzero m=4,8,... angular harmonics. After solenoidal cancellation
of the leading centrifugal-gradient contribution, the only
potentially critical angular transfer at natural-amplitude retention is

```
F4(R,theta,eta) = [V_theta^0(R,eta)/R] * partial_theta V_z^0(R,theta,eta)
```

For a smooth unforced u=U+w with AN energy/regularity hypotheses
and local correction deficit delta_tau=O(tau^h), necessity is

```
int_{I_tau} tau(t)^(-2A-1/2) int_{Omega(t)}
         [P_C4_nonzero(w_z)] F4 dx dt = K*tau^p+o(tau^p), K>0
```

where P_C4_nonzero is the nonzero fourfold angular projection and
K=M0*(R0-p/2)*(1-2^(-p))/p. In particular
tau^(-p/2)*sup_I ||P_C4_nonzero(w_z)||_L2(Omega)>=c*tau^h.
If F4 vanishes or the correction lacks matching axial fourfold
harmonics, natural-amplitude retention fails within the hypotheses.

**Kinematic sign-positive control, not PDE closure:** choose
psi_c=R^6 f(R²)g(eta)cos4theta with smooth flat compact f,g,
V_r=-partial_eta(psi_c)/R, V_z=partial_R(psi_c)/R,
V_theta=R*a with a=1 on psi support. A natural-amplitude
solenoidal correction with psi_w=-4R^6 f g sin4theta
has F4=W_z and thus strictly positive signed pairing
int F4² R dR dtheta deta. An exact finite-regularity
polynomial diagnostic gives 4194304*pi/547521975.
This proves only that the signed channel is kinematically allowed.
It does not satisfy the full physical unforced residual,
positive seven-ray source H, periodic pressure or terminal retention.

**Authenticated Case006 source is still missing**: the selected
physical four-patch U and all 12 overlaps, rotated frame E,
positive density rho, compact H and its full nonlinear pressure
and correction must be frozen together. Do not promote the
manufactured kinematic control to an H8 existence witness.

## Exact nonlinear realization (G5--G7)

Writing a residual as the divergence of a positive stress does **not**
solve unforced Navier--Stokes. One must construct `w,q` with

```
w_t - Delta w + (u.grad)w + (w.grad)u + (w.grad)w + grad q
  = -N(u,p),
div w = 0.
```

Required proofs: regular/core right-inverse range, complete Banach
graph-space contraction with numerical constants, periodic pressure,
unforced zero residual, initial data, smoothness and energy equality,
and a strictly subleading corrected velocity on a terminal sequence.
Positive-time spatial analyticity additionally prevents treating an
exact compact velocity bump over an analytic exact background as an
independent local solution; approximate stresses may remain compact.

## Terminal Core A.11 reuse (distinct conditional route)

Reusable tools include rational Bernstein/net lemmas, true same-profile
pressure bookkeeping and total angular-parameter derivatives. A.11's
support-length or terminal pressure conditions are not H8's seven-ray
stress or axial pressure conditions. Check that any baseline *amplitude*
treated as eta-independent actually has zero eta derivative; an
eta-independent exponential decay slope alone is insufficient.

## Release requirement (G8)

- Attach one authenticated common-source manifest and independently
  reproduce all equations, weighted enclosures and source matching.
- Include actual Lean declarations for all analytic bridge hypotheses
  and the final existential witness; check `#print axioms` transitively.
- Verify the *exact* pushed commit with hosted Lean 4.34.0-rc2 CI.
- Do not change any `OPEN` proof gate to `CLOSED` based on a synthetic
  example, a pointwise coefficient inequality or a conditional lemma.

**Current result:** finite joint-cone theorem and corrected physical
frame enclosure; authentic H8 source, compact weighted inverse,
nonlinear exact correction and full unforced theorem remain **OPEN**.
