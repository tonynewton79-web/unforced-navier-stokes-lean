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
Together these give a restricted no-go for the **sufficient**
four-coordinate smallness estimate on a manufactured meridional source,
not for the weaker original H8 seven-coefficient bound. The authentic
source, any tilted frame and the weighted source-matched H8 inverse
remain open. No full unforced finite-time
blow-up proof follows. The official proof-gate ledger is in
`docs/unforced-integration/proof_gates.json`.

The accompanying independent polynomial calculation is a diagnostic of
the local formulas, not a replacement for the continuum proof or Lean.
