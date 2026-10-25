# Unforced Navier–Stokes

This directory contains the new cumulative, journal-style research manuscript
by Tony Newton, separate from the repository's historical `paper.tex`.

- `Unforced_Navier_Stokes.tex`: complete LaTeX source, including the proof
  of the restricted compact symmetric-divergence theorem and bibliography.
- `Unforced_Navier_Stokes.pdf`: rendered A4 manuscript.

Build reproducibly from the repository root with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=manuscript/build manuscript/Unforced_Navier_Stokes.tex
```

The analytic meridional inversion theorem has a complete paper argument and
**partially Lean-formalized** pointwise cylindrical component identities:
`UnforcedPatching.MeridionalInverseSmoke` checks the radial and axial
divergences, actual axial integral antiderivative, radial moment integral,
and mixed carrier. A Cartesian tensor-divergence equivalence and global
compact-support theorem remain to be formalized. The seven-ray coefficient
bound, radial pressure-gauge derivative, physical residual expansion, and
conditional terminal-speed retention are also locally Lean-checked under
the pinned `lean-toolchain`.

Section 5 additionally proves an exact pressure-independent obstruction
against a *stronger physical componentwise* weighted bound, supported by
`python -m unittest discover -s tests -p test_meridional_h8.py -v` and
`python meridional_h8_certificate.py`. The new Lean module
`FourFieldPhysical` reconstructs the exact fixed-frame four-field tensor
and its isotropic gauge. Its independent exact test is
`python -m unittest discover -s tests -p test_h8_four_field_map.py -v`.
The `ExactCoefficientCone` Lean theorem reduces the original seven
coefficient inequalities to three exact coupled inequalities, without
the sufficient factor-14 relaxation; the rational test also exhibits
an admissible direction attaining the full original budget.
The `SharpCoefficientDual` Lean theorem proves the support upper
bound, with independent rational extremizers. The test
`h8_sharp_dual_certificate.py` verifies, using 1600 rational Bernstein
rectangles, a **stronger no-go even for the original absolute
coefficient perturbation budget** on the same manufactured source.
Run `python -m unittest discover -s tests -p 'test_h8_sharp_dual*.py' -v`
to reproduce it. This still does not exclude every one-sided positive
seven-ray allocation. The new `PositiveCoefficientCone` Lean theorem
establishes the upper support bound for the exact, asymmetric
one-sided coefficient floor; independent rational maximizing
witnesses establish sharpness. The exact signed-polynomial certificate
`h8_positive_dual_certificate.py` proves, on the *same manufactured*
meridional source and dual field, that the larger cone's support
exceeds the source pairing by more than `1/10000`. This means the
original dual field supplies no obstruction there, **not** that a
positive-cone inverse exists. Reproduce with
`python -m unittest discover -s tests -p 'test_h8_positive*.py' -v`
and `python h8_positive_dual_certificate.py`. The authentic
source and weighted source-matched H8 inverse remain open. The new
`RotatingFrameDual` Lean module proves the exact finite-matrix
conjugation identity and the one-sided dual bound for **arbitrary
pointwise frame values**, with exact independent rational tests in
`tests/test_h8_rotating_frame.py`. This completes only the rotating
frame's **algebraic** bridge. It does not supply the authentic
frame profile, its derivatives, a compact inverse or the continuum
integral certificate. No full unforced finite-time
blow-up proof follows. The official proof-gate ledger is in
`docs/unforced-integration/proof_gates.json`.

The accompanying independent polynomial calculation is a diagnostic of
the local formulas, not a replacement for the continuum proof or Lean.
