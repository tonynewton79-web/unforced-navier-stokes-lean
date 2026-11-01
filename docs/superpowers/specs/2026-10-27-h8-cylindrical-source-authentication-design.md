# Full cylindrical H8 source authentication: design

## Intent

Move from a universal rotating-frame commutator to the explicit standard
orthonormal cylindrical frame. Certify every connection term in the
Cartesian tensor divergence, keep all pressure components, and expose
the missing authentic Case 006 source inputs without replacing them.

## Approaches

1. **Exact symbolic Cartesian-to-cylindrical calculation (chosen):**
   construct `E(theta)`, `H(A,B,C,D)`, and `K=E H E^T` symbolically.
   Apply true Cartesian partials via the polar chain rule and compare
   each source component to a hand-derived cylindrical formula.
   Benefits: all three components, exact nonaxisymmetric and pressure
   terms, fast reproducibility. Limitation: SymPy algebraic proof is not
   yet a Lean kernel proof of the source-specific analytic hypotheses.
2. **Assume the cylindrical divergence formula:** fast, but leaves the
   geometric connection calculation untested.
3. **Specialise immediately to a guessed smooth H8 cutoff:** rejected;
   it would falsely authenticate an unspecified source function.

## Mathematical output

For `H=[[-D,C,A],[C,0,B],[A,B,D]]`, `K=E H E^T`,
`E=(e_r,e_theta,e_z)`, `r>0`, and pressure `p`, certify

`f_r = -D_r + C_theta/r + A_z - D/r + p_r`,
`f_theta = C_r + 2C/r + B_z + p_theta/r`,
`f_z = A_r + A/r + B_theta/r + D_z + p_z`.

Also certify `E_r=E_z=0`, `E_theta=E*Omega`,
`E_x=-sin(theta)/r E*Omega`, `E_y=cos(theta)/r E*Omega`.

Under full angular averaging, the theta-derivative terms integrate
to zero with periodic endpoint and integrability assumptions. The
source's axial pressure jump `[D+p]_c^d` is retained; it is not zeroed.

## Fail-closed authentication boundary

The source's H8 coefficients and frame are specified in a *frozen*
co-rotating cylindrical basis. The attached cumulative manuscript
also permits spatially tilted frames. The source architecture names
`u_b=curl(chi A_c)` and independent shapers
`Psi_i=K_i a_i(r)b(r)Xi_i(z)`, but does not supply a single complete
authenticated three-variable cutoff, shaper, pressure representative
and source/stress density tuple. The original 122-page Case 006
manuscript is not in the current uploaded files or located by name
in the accessible Library. No profile may be invented to close that
gate. A manufactured polynomial regression is only a control.

## Acceptance tests

- Exact symbolic residuals vanish separately for r/theta/z.
- Nonconstant C4 profiles and pressure demonstrate nonzero geometric
  terms and nonzero pressure traces.
- A test mutation removing `-D/r`, `2C/r` or `A/r` fails.
- Existing 87 tests, proof-gate ledger and Lean frame proof remain green.
- Manuscript and notes distinguish exact cylindrical geometry from
  authentic H8 source positivity and global PDE closure.
