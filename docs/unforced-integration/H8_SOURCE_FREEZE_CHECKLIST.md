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
