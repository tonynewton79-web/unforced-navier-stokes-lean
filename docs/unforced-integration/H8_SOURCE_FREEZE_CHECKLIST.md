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
