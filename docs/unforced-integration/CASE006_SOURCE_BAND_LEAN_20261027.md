# Case 006 source-native axial interval: Lean proof boundary

**27 October 2026.** Pinned to Lean `4.34.0-rc2` and the repository's
Mathlib revision `85e3a25e006c35636f0e53b0e9296caca2685bc0`.

The source is the Case 006 portion of the 22-page manuscript
*Unforced Navier--Stokes: Compact symmetric stresses, exact coefficient
margins, and formal verification on the three-torus*.

## What the new theorem proves

`UnforcedPatching/Case006SourceBand.lean` imports the already-formalized
exact seven-ray coefficient cone. It establishes the sharp consequence

\[
 \forall i\in\{1,\dots,7\},\quad |\delta c_i|\le\tau
 \quad\Longrightarrow\quad |A|\le\tau.
\]

With \(\kappa=15971/122900\), source-frame efficiency
\(\alpha=-4443/9832\), \(\rho\ge0\), and the **assumed** physical shear
identity \(T=\alpha\rho+A\), it establishes exactly

\[
 -\frac{143017}{245800}\rho\le T\le
 -\frac{79133}{245800}\rho.
\]

The proof provides feasible seven-ray perturbations attaining both
endpoints. It also formalizes the same implication for **arbitrary
finite nonnegative weighted slices** (including quadrature nodes).

Separately, a rational tensor with
\[
 A=51113/245800,\quad B=15971/983200,\quad
 C=16/1229,\quad D=19171/491600
\]
satisfies **all seven** positive coefficient floors at \(\rho=1\),
while \(|A|>\kappa\). Thus the original absolute budget cannot be
replaced with one-sided positivity in the conditional axial interval.

## What this does *not* prove

- It does not establish the source-frame equality for an authentic H8
  residual, or check the requisite pressure/boundary traces.
- The finite weighted sum is **not** a formalization of the cylindrical
  source integral or its radial fundamental-theorem-of-calculus bridge.
- No global compact symmetric-divergence inverse, rotating frame
  derivative bound, or weighted H8 source estimate is constructed.
- The independent Terminal Core A.11 stress and gauge bounds still
  require the same-profile root, source, interval, and terminal-gauge
  certificates; they cannot be substituted for the seven-ray budget.
- No unforced Navier--Stokes blow-up or global regularity theorem follows.

## Reproduction

From the repository root, with the pinned toolchain installed:

```sh
lake exe cache get
lake build UnforcedPatching.Case006SourceBandSmoke
python -m unittest discover -s tests -p 'test_h8_case006_source_band.py' -v
```

The smoke file prints the axioms used by each key declaration and checks
the explicit one-sided counterexample. The repository's physical-gate
CI workflow now includes the new smoke module.
